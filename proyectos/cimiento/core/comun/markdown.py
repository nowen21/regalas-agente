"""Leer documentos Markdown: las líneas que cuentan, sus encabezados, sus enlaces y sus tablas."""
import re

_CERCA = re.compile(r"^\s*(```|~~~)")
_ENCABEZADO = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
_ENLACE = re.compile(r"\[([^\]\n]*)\]\(([^)\s]+)")
# Un marcador de plantilla, `[texto]`, que no es enlace ni casilla de verificación.
_MARCADOR = re.compile(r"\[([^\[\]\n]+)\](?!\()")
# Un tramo `entre comillas invertidas`, con una o varias de apertura.
_CODIGO_EN_LINEA = re.compile(r"(`+)(?:(?!\1).)*?\1")


class Markdown:
    """Lo que los validadores leen de un `.md`. Todo es estático: no guarda estado."""

    @staticmethod
    def lineas_utiles(texto):
        """`(número de línea, contenido)` saltando los bloques de código: un
        ejemplo dentro de ``` no es contenido del documento."""
        dentro = False
        for n, linea in enumerate(texto.splitlines(), start=1):
            if _CERCA.match(linea):
                dentro = not dentro
                continue
            if not dentro:
                yield n, linea

    @staticmethod
    def sin_codigo_en_linea(linea):
        """La línea con los tramos `entre comillas invertidas` en blanco: ahí hay
        muestras de cómo se escribe algo, no contenido. Se rellena con espacios
        para no correr las columnas."""
        return _CODIGO_EN_LINEA.sub(lambda m: " " * len(m.group(0)), linea)

    @classmethod
    def enlaces(cls, texto):
        """`[(línea, texto, destino)]` de los enlaces, fuera de bloques y de comillas invertidas."""
        return [(n, m.group(1), m.group(2)) for n, linea in cls.lineas_utiles(texto)
                for m in _ENLACE.finditer(cls.sin_codigo_en_linea(linea))]

    @classmethod
    def encabezados(cls, texto, desde_nivel=2):
        """`[(línea, título)]` del nivel dado hacia abajo. El H1 se salta a propósito:
        en un documento real lleva el identificador y el título concretos."""
        return [(n, m.group(2).strip()) for n, linea in cls.lineas_utiles(texto)
                for m in [_ENCABEZADO.match(linea)] if m and len(m.group(1)) >= desde_nivel]

    @classmethod
    def marcadores(cls, texto):
        """`[(línea, marcador)]` de los `[así]` sin llenar."""
        return [(n, m.group(0)) for n, linea in cls.lineas_utiles(texto)
                for m in _MARCADOR.finditer(linea) if m.group(1).strip() not in ("", "x", "X")]

    @staticmethod
    def _celdas(linea):
        return [c.strip() for c in linea.strip().strip("|").split("|")]

    @staticmethod
    def _es_separador(celdas):
        return bool(celdas) and all(re.fullmatch(r":?-{2,}:?", c) for c in celdas)

    @classmethod
    def tablas(cls, texto):
        """`[(encabezados, [(línea, celdas)])]` de cada tabla del documento.

        Una tabla es un bloque de renglones que empiezan por `|` cuya segunda
        línea es la de guiones: sin ella, Markdown no la dibuja como tabla.
        """
        salida, bloque = [], []

        def cerrar():
            if len(bloque) >= 2 and cls._es_separador(cls._celdas(bloque[1][1])):
                salida.append((cls._celdas(bloque[0][1]),
                               [(n, cls._celdas(l)) for n, l in bloque[2:]]))
            bloque.clear()

        for n, linea in cls.lineas_utiles(texto):
            if linea.strip().startswith("|"):
                bloque.append((n, linea))
            else:
                cerrar()
        cerrar()
        return salida

    @classmethod
    def filas_de(cls, texto, *columnas):
        """`[(línea, {columna: valor})]` de la primera tabla que tenga todas esas
        columnas. Se busca por nombre y no por posición: una tabla que gana una
        columna al final no rompe a quien la lee."""
        objetivo = [c.lower() for c in columnas]
        for encabezados, filas in cls.tablas(texto):
            bajos = [e.lower() for e in encabezados]
            if all(c in bajos for c in objetivo):
                return [(n, {e: (celdas[i] if i < len(celdas) else "") for i, e in enumerate(bajos)})
                        for n, celdas in filas]
        return []

    @staticmethod
    def valor_limpio(celda):
        """El contenido de una celda sin comillas invertidas. Una celda vacía, con
        raya o con el `«…»` de la plantilla vale `""`: nadie la llenó."""
        v = celda.strip().strip("`").strip()
        if not v or v in ("—", "-", "–") or ("«" in v and "»" in v):
            return ""
        return v
