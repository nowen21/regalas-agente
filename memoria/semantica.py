#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Búsqueda semántica de la memoria — opcional (pendiente 05).

FTS5 encuentra **palabras**; esto encuentra **significado**. Es un complemento,
no un reemplazo: la búsqueda de `memoria.py` combina las dos (híbrida).

Es **opt-in**: si `model2vec`/`numpy` no están instalados, `disponible()` da
False y la memoria sigue funcionando solo con FTS5. Los embeddings se calculan
**localmente** (el contenido de las señales nunca sale de la máquina — `00·N6`) y
se guardan en la misma `senales.db`, como blobs. Se buscan por coseno en memoria:
a esta escala (cientos-miles) es instantáneo y evita cargar extensiones nativas.

    pip install -r requirements-semantica.txt
    python memoria.py indexar          # calcula/actualiza los vectores
    python memoria.py search "..."     # híbrida en automático si está disponible
"""
import hashlib
import os

MODELO = os.environ.get("MEMORIA_MODELO", "minishlab/potion-base-8M")

_modelo = None


def disponible():
    """¿Están las dependencias opcionales? Si no, la memoria degrada a léxica."""
    try:
        import numpy        # noqa: F401
        import model2vec    # noqa: F401
        return True
    except ImportError:
        return False


def _cargar():
    global _modelo
    if _modelo is None:
        from model2vec import StaticModel
        _modelo = StaticModel.from_pretrained(MODELO)
    return _modelo


def embed(textos):
    import numpy as np
    return np.asarray(_cargar().encode(list(textos)), dtype="float32")


def asegurar_tabla(con):
    con.execute("CREATE TABLE IF NOT EXISTS senales_vec ("
                "rowid INTEGER PRIMARY KEY, hash TEXT, vec BLOB)")


def _texto(fila):
    """Los mismos campos que indexa FTS5, concatenados."""
    return " ".join(p for p in (fila["titulo"], fila["what"], fila["why"],
                                fila["learned"]) if p)


def indexar(con):
    """Calcula el vector de las señales nuevas o cambiadas (por hash del texto).
    Solo carga el modelo si hay algo que embeber. Devuelve cuántas actualizó."""
    asegurar_tabla(con)
    filas = con.execute("SELECT rowid,titulo,what,why,learned FROM senales").fetchall()
    tengo = dict(con.execute("SELECT rowid,hash FROM senales_vec").fetchall())
    faltan = []
    for f in filas:
        txt = _texto(f)
        h = hashlib.sha1(txt.encode("utf-8")).hexdigest()
        if tengo.get(f["rowid"]) != h:
            faltan.append((f["rowid"], txt, h))
    if not faltan:
        return 0
    vs = embed([t for _, t, _ in faltan])
    con.executemany("INSERT OR REPLACE INTO senales_vec(rowid,hash,vec) VALUES(?,?,?)",
                    [(rid, h, v.tobytes()) for (rid, _, h), v in zip(faltan, vs)])
    con.commit()
    return len(faltan)


def ranking(qvec, ids, matriz):
    """Núcleo puro: rowids ordenados por coseno con `qvec`. Sin base ni modelo."""
    import numpy as np
    if not len(ids):
        return []
    M = matriz / (np.linalg.norm(matriz, axis=1, keepdims=True) + 1e-9)
    q = qvec / (np.linalg.norm(qvec) + 1e-9)
    sims = M @ q
    orden = np.argsort(-sims)
    return [(int(ids[i]), float(sims[i])) for i in orden]


def buscar(con, query, k=50):
    """(rowid, similitud) de las señales más parecidas a `query`. [] si no hay."""
    import numpy as np
    asegurar_tabla(con)
    filas = con.execute("SELECT rowid,vec FROM senales_vec").fetchall()
    if not filas:
        return []
    ids = [r[0] for r in filas]
    matriz = np.stack([np.frombuffer(r[1], dtype="float32") for r in filas])
    return ranking(embed([query])[0], ids, matriz)[:k]
