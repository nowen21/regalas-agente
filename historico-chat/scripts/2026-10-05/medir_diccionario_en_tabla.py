"""HU-027 · ¿Traducir una regla buscando sus palabras en una tabla es más rápido
que abrir el diccionario completo, y da lo mismo?

El modelo `potion-base-8M` es una tabla: a cada pedazo de palabra le tocan 256
números, y una frase vale el promedio de los de sus pedazos. Este guion:

1. `preparar`: abre el modelo una vez y guarda esa tabla en SQLite, con los
   vectores de todas las reglas y el de `02·F25` traducido por la librería.
2. `medir`: en un proceso nuevo, sin cargar el modelo, traduce `02·F25` con la
   tabla, la compara con lo que dio la librería, y busca sus parecidas contra
   los vectores guardados. Imprime el tiempo de cada paso.

Se corre desde la raíz del estándar:
    python historico-chat/scripts/2026-10-05/medir_diccionario_en_tabla.py preparar
    python historico-chat/scripts/2026-10-05/medir_diccionario_en_tabla.py medir
La tabla queda en `.tmp-agente/diccionario.db`, que git ignora.
"""
import os
import sqlite3
import sys
import time

INICIO = time.time()
RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "proyectos", "cimiento"))
BD = os.path.join(RAIZ, ".tmp-agente", "diccionario.db")
MODELO = "minishlab/potion-base-8M"


def reglas():
    from core.comun import Proyecto
    from core.validadores.metareglas import CuerpoDeReglas
    from core.validadores.parecidas import ReglasParecidas
    vigentes = [r for r in CuerpoDeReglas.leer(Proyecto.estandar()) if not r.derogada]
    return vigentes, ReglasParecidas.texto


def preparar():
    import numpy as np
    from model2vec import StaticModel
    modelo = StaticModel.from_pretrained(MODELO)
    assert modelo.token_mapping is None and modelo.weights is None, "el modelo usa remapeo o pesos"
    os.makedirs(os.path.dirname(BD), exist_ok=True)
    if os.path.exists(BD):
        os.remove(BD)
    con = sqlite3.connect(BD)
    con.execute("CREATE TABLE pedazos (id INTEGER PRIMARY KEY, vec BLOB)")
    con.execute("CREATE TABLE datos (clave TEXT PRIMARY KEY, valor TEXT)")
    con.execute("CREATE TABLE reglas (id TEXT PRIMARY KEY, vec BLOB)")
    embedding = np.asarray(modelo.embedding, dtype="float32")
    con.executemany("INSERT INTO pedazos VALUES (?, ?)", ((i, v.tobytes()) for i, v in enumerate(embedding)))
    con.executemany("INSERT INTO datos VALUES (?, ?)", (
        ("desconocido", str(modelo.unk_token_id)), ("largo_mediano", str(modelo.median_token_length)),
        ("normalizar", str(int(modelo.normalize)))))
    vigentes, texto = reglas()
    vectores = modelo.encode([texto(r) for r in vigentes])
    con.executemany("INSERT INTO reglas VALUES (?, ?)",
                    ((r.id, np.asarray(v, dtype="float32").tobytes()) for r, v in zip(vigentes, vectores)))
    f25 = [r for r in vigentes if r.id == "F25"][0]
    con.execute("INSERT INTO datos VALUES ('f25_libreria', ?)",
                (np.asarray(modelo.encode([texto(f25)])[0], dtype="float32").tobytes().hex(),))
    con.commit()
    print("tabla lista: %d pedazos de %d números, %d reglas, %.1f MB" % (
        len(embedding), embedding.shape[1], len(vigentes), os.path.getsize(BD) / 1e6))


def medir():
    import numpy as np
    t_numpy = time.time()
    from tokenizers import Tokenizer
    import glob
    carpeta = glob.glob(os.path.expanduser(
        "~/.cache/huggingface/hub/models--minishlab--potion-base-8M/snapshots/*"))[0]
    tokenizador = Tokenizer.from_file(os.path.join(carpeta, "tokenizer.json"))
    t_tokenizador = time.time()
    vigentes, texto = reglas()
    t_reglas = time.time()
    con = sqlite3.connect(BD)
    datos = dict(con.execute("SELECT clave, valor FROM datos"))
    f25 = [r for r in vigentes if r.id == "F25"][0]
    frase = texto(f25)[:512 * int(datos["largo_mediano"])]
    ids = [i for i in tokenizador.encode(frase, add_special_tokens=False).ids if i != int(datos["desconocido"])][:512]
    unicos = sorted(set(ids))
    filas = dict(con.execute("SELECT id, vec FROM pedazos WHERE id IN (%s)" % ",".join("?" * len(unicos)), unicos))
    vec = np.mean([np.frombuffer(filas[i], dtype="float32") for i in ids], axis=0)
    if datos["normalizar"] == "1":
        vec = vec / (np.linalg.norm(vec) + 1e-32)
    t_traducir = time.time()
    libreria = np.frombuffer(bytes.fromhex(datos["f25_libreria"]), dtype="float32")
    diferencia = float(np.abs(vec - libreria).max())
    guardadas = con.execute("SELECT id, vec FROM reglas").fetchall()
    matriz = np.array([np.frombuffer(v, dtype="float32") for _, v in guardadas], dtype=float)
    matriz /= np.linalg.norm(matriz, axis=1, keepdims=True)
    parecido = matriz @ (vec / np.linalg.norm(vec))
    orden = [j for j in np.argsort(-parecido) if guardadas[j][0] != "F25"][:5]
    t_fin = time.time()
    print("arranque e import de numpy %.2f s, tokenizador %.2f s, leer las reglas %.2f s, traducir F25 %.2f s, "
          "comparar %.2f s · total %.2f s" % (t_numpy - INICIO, t_tokenizador - t_numpy, t_reglas - t_tokenizador,
                                              t_traducir - t_reglas, t_fin - t_traducir, t_fin - INICIO))
    print("diferencia máxima con la librería: %.2e" % diferencia)
    print("parecidas a F25:", ", ".join("%s %.2f" % (guardadas[j][0], parecido[j]) for j in orden))


if __name__ == "__main__":
    {"preparar": preparar, "medir": medir}[sys.argv[1]]()
