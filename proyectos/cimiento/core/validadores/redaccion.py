"""`00·ID10` · Lo que se puede medir sobre lo que el agente acaba de escribir.

Tres reglas del núcleo hablan de cómo escribe el agente: `ID8` (las marcas),
`ID9` (cuánto ocupa) e `ID10` (la persona y la forma verbal). Lo propio de este
módulo es el **trato**: «usted», «tú» y sus formas, que `ID10` descarta sin
discusión. Las marcas las cuenta `marcas.py` y el umbral de largo es el de
`brevedad.py`; acá se juntan las tres cifras en una línea sobre **un** texto.

No mide la variedad del idioma ni si un imperativo lo es de verdad: eso pide
leer. **Mide y no detiene**, y por eso el resultado se imprime al cerrar cada turno.
"""
import re

from ..comun import Markdown
from .brevedad import HOLGADO
from .marcas import Marcas

# El trato directo, en las formas que aparecen de verdad. Cada una se reconoce
# sin contexto; la que necesite contexto no se cuenta, se lee.
_TRATO = re.compile(
    r"(?i)(?<![\w-])(usted(?:es)?|t[úu]|ti|tuyos?|tuyas?|contigo|"
    r"vosotros|os)(?![\w-])")

# Lo que cita la pantalla o al usuario no es redacción del agente.
_CITA = re.compile(r"[«\"'][^«»\"']*[»\"']")


def _es_cerca(linea):
    return linea.lstrip().startswith("```") or linea.lstrip().startswith("~~~")


class Redaccion:
    """Las tres cifras de un turno. Todo es estático."""

    @staticmethod
    def sin_citas(linea):
        """La línea sin lo citado ni lo que va en código."""
        return _CITA.sub(" ", Markdown.sin_codigo_en_linea(linea))

    @classmethod
    def tratos(cls, texto):
        """`[(línea, palabra)]` de cada trato directo fuera de una cita."""
        salida, cercado = [], False
        for n, linea in enumerate(texto.split("\n"), 1):
            if _es_cerca(linea):
                cercado = not cercado
                continue
            if not cercado:
                salida += [(n, m.group(1)) for m in _TRATO.finditer(cls.sin_citas(linea))]
        return salida

    @classmethod
    def medir(cls, texto):
        """`{"caracteres","tratos","marcas"}` de una respuesta. Ninguna cifra decide nada."""
        cercado, cuantas = False, 0
        for linea in texto.split("\n"):
            if _es_cerca(linea):
                cercado = not cercado
                continue
            if not cercado:
                cuantas += len(Marcas.de_linea(Markdown.sin_codigo_en_linea(linea)))
        return {"caracteres": len(texto.strip()), "tratos": cls.tratos(texto), "marcas": cuantas}

    @classmethod
    def linea_de_cierre(cls, texto, mediana=0):
        """La línea que el enganche imprime, o `""` si no hay nada que decir.

        **Se calla cuando todo está bien**: un aviso que sale en cada turno deja
        de leerse a la tercera, y entonces tampoco se lee el que importaba.
        """
        m = cls.medir(texto)
        partes = []
        if m["marcas"]:
            partes.append("%d marca(s) de `00·ID8`" % m["marcas"])
        if m["tratos"]:
            partes.append("trato directo de `00·ID10`: %s" % ", ".join(sorted({p.lower() for _n, p in m["tratos"]})))
        if m["caracteres"] > HOLGADO:
            cuanto = "%d caracteres (holgado: %d)" % (m["caracteres"], HOLGADO)
            if mediana:
                cuanto += ", mediana de la sesión %d" % mediana
            partes.append("`00·ID9`: " + cuanto)
        return "[redacción] " + " · ".join(partes) if partes else ""
