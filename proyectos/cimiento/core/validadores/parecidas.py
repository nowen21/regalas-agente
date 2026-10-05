"""`20·M12` · `EP-004·HU-027` · Las reglas que se parecen a una, por significado.

`M12` manda buscar por concepto antes de crear una regla, y nada lo hacía: en la
sesión del 2026-10-04 `02·F25` repetía y contradecía a `02·F4` sin que nadie lo
viera. **Busca por lo que dice, no por cómo se llama** (análisis 1 del pendiente
116, acuerdo 5), con la búsqueda por significado de `memoria/`, que se importa y
no se copia.

**Avisa y no frena**: decidir si dos reglas dicen lo mismo, o se contradicen, es
criterio de quien escribe.

**Sin la búsqueda, lo dice** (CA-03). Adivinar por palabras sueltas daría una
lista que parece buena y no lo es: es lo mismo que hace `memoria/parecidas.py`.

**El modelo no se abre en cada aviso** (cambio aprobado el 2026-10-05). Abrirlo
tarda de 2 a 6 s y el enganche tiene que responder en menos de 3. El modelo es,
por dentro, una tabla: a cada pedazo de palabra le tocan 256 números, y una
frase vale el promedio de los de sus pedazos. Esa tabla se guarda una vez en una
base de datos y cada regla se traduce buscando solo sus pedazos: 1 s, y los
mismos números que da la librería (una prueba lo compara).
"""
import os
import sqlite3
import sys

from ..comun import AVISO, Git, Hallazgo, Proyecto
from .base import Validador
from .metareglas import CuerpoDeReglas

# Medidos el 2026-10-05 sobre las 257 reglas vigentes, con el título y la
# exigencia (sin los ejemplos ni el checklist): con el texto entero, `02·F4` no
# salía entre las seis primeras de `02·F25`; así sale primera (0,86). La mitad
# de los pares queda en 0,74 y el 1 % pasa de 0,85: con 0,85 cada regla tiene
# en promedio tres parecidas, y el tope corta las que tienen muchas. Con 0,83 el
# promedio sube a ocho y la lista se deja de leer.
# Guion: historico-chat/scripts/2026-10-05/medir_reglas_parecidas.py
UMBRAL = 0.85
TOPE = 5

APAGADA = False     # para pedirle que no busque, como en un ambiente sin la búsqueda


class Diccionario:
    """La tabla de palabras del modelo de `memoria/`, en `memoria/diccionario.db`.

    Vive junto a la memoria y no en cada proyecto: es del modelo, no de las
    reglas, y git la ignora (`*.db`). Se arma sola la primera vez, y otra vez si
    `memoria/` cambia de modelo.
    """

    ARCHIVO = "diccionario.db"
    _LOTE = 900         # cuántos pedazos se piden en una consulta

    def __init__(self, memoria, semantica):
        self.ruta = os.path.join(memoria, self.ARCHIVO)
        self.semantica = semantica
        self._datos = None
        self._tokenizador = None

    def _armar(self):
        """Abre el modelo una vez y guarda su tabla. Se escribe en un archivo
        aparte y se cambia de nombre al final: un enganche que corre al mismo
        tiempo no lee una tabla a medio escribir."""
        import numpy as np
        modelo = self.semantica._cargar()
        if modelo.token_mapping is not None or modelo.weights is not None:
            raise RuntimeError("el modelo de memoria/ usa pesos o remapeo: la tabla no lo reproduce")
        temporal = "%s.%d.tmp" % (self.ruta, os.getpid())
        con = sqlite3.connect(temporal)
        try:
            con.execute("CREATE TABLE datos (clave TEXT PRIMARY KEY, valor TEXT)")
            con.execute("CREATE TABLE pedazos (id INTEGER PRIMARY KEY, vec BLOB)")
            vectores = np.asarray(modelo.embedding, dtype="float32")
            con.executemany("INSERT INTO datos VALUES (?, ?)", (
                ("modelo", self.semantica.MODELO), ("desconocido", str(modelo.unk_token_id)),
                ("largo_mediano", str(modelo.median_token_length)), ("dimension", str(vectores.shape[1])),
                ("tokenizador", modelo.tokenizer.to_str())))
            con.executemany("INSERT INTO pedazos VALUES (?, ?)", ((i, v.tobytes()) for i, v in enumerate(vectores)))
            con.commit()
        finally:
            con.close()
        os.replace(temporal, self.ruta)

    def armado(self):
        """Si la tabla existe y es del modelo que usa `memoria/`."""
        return os.path.isfile(self.ruta) and self._leer_datos().get("modelo") == self.semantica.MODELO

    def _abrir(self):
        if self._datos is None:
            if not self.armado():
                self._armar()
            self._datos = self._leer_datos()
            from tokenizers import Tokenizer
            self._tokenizador = Tokenizer.from_str(self._datos["tokenizador"])
        return self._datos

    def _leer_datos(self):
        try:
            con = sqlite3.connect(self.ruta)
            try:
                return dict(con.execute("SELECT clave, valor FROM datos"))
            finally:
                con.close()
        except sqlite3.Error:
            return {}

    def traducir(self, textos):
        """Un vector de largo 1 por texto, como `semantica.embed` pero sin abrir
        el modelo: el promedio de los pedazos, igual que la librería, que corta
        en 512 pedazos y descarta el desconocido."""
        import numpy as np
        datos = self._abrir()
        desconocido, tope = int(datos["desconocido"]), 512 * int(datos["largo_mediano"])
        listas = [[i for i in c.ids if i != desconocido][:512] for c in
                  self._tokenizador.encode_batch([t[:tope] for t in textos], add_special_tokens=False)]
        unicos = sorted({i for lista in listas for i in lista})
        tabla = {}
        con = sqlite3.connect(self.ruta)
        try:
            for k in range(0, len(unicos), self._LOTE):
                lote = unicos[k:k + self._LOTE]
                tabla.update(con.execute("SELECT id, vec FROM pedazos WHERE id IN (%s)" % ",".join("?" * len(lote)),
                                         lote))
        finally:
            con.close()
        salida = []
        for lista in listas:
            v = (np.mean([np.frombuffer(tabla[i], dtype="float32") for i in lista], axis=0) if lista
                 else np.zeros(int(datos["dimension"]), dtype="float32"))
            salida.append(v / (np.linalg.norm(v) or 1.0))
        return np.asarray(salida, dtype=float)


class ReglasParecidas(Validador):
    """Para cada regla pedida, las que se le parecen por significado."""

    nombre = "parecidas"
    regla = "20·M12"
    descripcion = "reglas que se parecen por significado"

    def __init__(self, proyecto, archivos=None, ids=None, solo_preparados=False, busqueda=None):
        super().__init__(proyecto, archivos)
        self.ids = list(ids or [])
        self.solo_preparados = solo_preparados
        self._busqueda = busqueda

    @staticmethod
    def texto(regla):
        """Lo que se compara: el título y la exigencia, sin ejemplos ni checklist."""
        return regla.titulo + ". " + " ".join(t for _, t in regla.cuerpo)

    def busqueda(self):
        """El módulo `semantica` de `memoria/`, o `None` si no está instalado."""
        if self._busqueda is None:
            self._busqueda = APAGADA
            memoria = os.path.join(Proyecto.estandar() or self.proyecto.raiz, "memoria")
            if os.path.isfile(os.path.join(memoria, "semantica.py")):
                if memoria not in sys.path:
                    sys.path.insert(0, memoria)
                import semantica
                diccionario = Diccionario(memoria, semantica)
                # Con la tabla armada no hace falta el modelo, y preguntar por él
                # cuesta casi un segundo: basta con lo que la tabla usa.
                if (diccionario.armado() and self._hay("numpy", "tokenizers")) or semantica.disponible():
                    self._busqueda = diccionario
        return self._busqueda or None

    @staticmethod
    def _hay(*modulos):
        import importlib.util
        return all(importlib.util.find_spec(m) is not None for m in modulos)

    def de(self, ids, catalogo=None):
        """`{id: [(id parecida, parecido)]}`, de mayor a menor y hasta `TOPE`; o
        `None` si no se puede buscar por significado."""
        diccionario = self.busqueda()
        if diccionario is None:
            return None
        import numpy as np
        vigentes = [r for r in (catalogo or CuerpoDeReglas.leer(self.proyecto.raiz, self.archivos))
                    if not r.derogada]
        posicion = {r.id: i for i, r in enumerate(vigentes)}
        vectores = diccionario.traducir([self.texto(r) for r in vigentes])
        salida = {}
        for id_ in ids:
            if id_ not in posicion:
                continue
            i = posicion[id_]
            parecido = vectores @ vectores[i]
            orden = [j for j in np.argsort(-parecido) if j != i and parecido[j] >= UMBRAL]
            salida[id_] = [(vigentes[j].id, float(parecido[j])) for j in orden[:TOPE]]
        return salida

    def pedidas(self, catalogo):
        """Las reglas a revisar: las pedidas, las de los archivos que entran en
        el commit, o todas."""
        if self.ids:
            return self.ids
        if not self.solo_preparados:
            return [r.id for r in catalogo]
        preparados = set()
        for repo in self.proyecto.repositorios():
            prefijo = self.proyecto.prefijo_de(repo)
            preparados |= {self.proyecto.ruta(prefijo + rel) for rel in Git(repo).preparados()
                           if (prefijo + rel).startswith("base/") and rel.endswith(".md")}
        reales = {Proyecto.ruta_real(p, self.proyecto.raiz) for p in preparados}
        return [r.id for r in catalogo if Proyecto.ruta_real(r.archivo, self.proyecto.raiz) in reales]

    def validar(self):
        catalogo = CuerpoDeReglas.leer(self.proyecto.raiz, self.archivos)
        ids = self.pedidas(catalogo)
        if not ids:
            return []
        parecidas = self.de(ids, catalogo)
        if parecidas is None:
            return [Hallazgo(AVISO, self.proyecto.raiz, 0, self.sin_busqueda(), regla=self.regla)]
        indice = {r.id: r for r in catalogo}
        hallazgos = []
        for id_, lista in parecidas.items():
            if lista:
                r = indice[id_]
                hallazgos.append(Hallazgo(
                    AVISO, r.archivo, r.linea, "`%s·%s` se parece a %s: leerlas antes de crear o cambiar una "
                    "regla — %s" % (r.capitulo, id_, self.lista(lista, indice), self.regla), regla=self.regla))
        return hallazgos

    @staticmethod
    def lista(parecidas, indice):
        return ", ".join("`%s·%s` (%d %%)" % (indice[i].capitulo, i, round(p * 100)) for i, p in parecidas)

    def sin_busqueda(self):
        return ("no se pudo buscar por significado las reglas parecidas: falta instalar la búsqueda de "
                "`memoria/` (numpy y model2vec) — %s" % self.regla)
