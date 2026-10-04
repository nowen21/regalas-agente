"""Recorrer el código versionado de un proyecto, y lo que comparten los
validadores que lo revisan.

`RecorridoDeCodigo` no opina: entrega cada archivo con su texto. `Bloques`
encuentra el cuerpo de una función o de un bucle. `ValidadorDeCodigo` junta las
dos cosas: recorre una vez y le pasa cada texto a `revisar_texto`, que es lo
único que escribe cada validador.
"""
import os
import re

from ..comun import Archivos, Git
from .base import Validador

# Extensiones de código que vale la pena abrir: sin binarios, imágenes,
# archivos de bloqueo ni documentación.
EXTENSIONES = frozenset({
    ".php", ".py", ".js", ".ts", ".jsx", ".tsx", ".mjs", ".cjs", ".vue",
    ".rb", ".go", ".java", ".kt", ".cs", ".rs", ".swift", ".scala", ".sql",
})

# Lo de terceros y lo generado: se buscan olores de código, y esos árboles son
# salida, no fuente.
_SALTAR = re.compile(
    r"(^|/)(vendor|node_modules|dist|build|\.git|public|static|staticfiles)/|\.min\.(js|css)$")


class RecorridoDeCodigo:
    """Los archivos de código versionados de un proyecto, uno por uno."""

    def __init__(self, proyecto, archivos=None, extensiones=EXTENSIONES):
        self.proyecto = proyecto
        self.lector = archivos or Archivos()
        self.extensiones = extensiones

    @staticmethod
    def linea_de(texto, posicion):
        """Número de línea (desde 1) del carácter en `posicion`."""
        return texto.count("\n", 0, posicion) + 1

    def es_codigo(self, relativa):
        return (not _SALTAR.search(relativa)
                and os.path.splitext(relativa)[1].lower() in self.extensiones)

    def archivos(self):
        """`(ruta mostrada, texto)` por cada archivo de código versionado."""
        for repo in self.proyecto.repositorios():
            etiqueta = os.path.relpath(repo, self.proyecto.raiz).replace("\\", "/")
            prefijo = "" if etiqueta == "." else etiqueta + "/"
            for relativa in Git(repo).versionados():
                if self.es_codigo(relativa):
                    yield prefijo + relativa, self.lector.leer(os.path.join(repo, relativa))


class Bloques:
    """El cuerpo de una función o de un bucle, en lenguajes con llaves o con sangría.

    Estaba escrito dos veces, en el validador de funciones largas y en el de
    consultas en bucle (análisis 1 del pendiente 116).
    """

    @staticmethod
    def llaves(texto, abre):
        """Del `{` en `abre` a su `}` pareja, ambos incluidos."""
        profundidad = 0
        for k in range(abre, len(texto)):
            if texto[k] == "{":
                profundidad += 1
            elif texto[k] == "}":
                profundidad -= 1
                if profundidad == 0:
                    return texto[abre:k + 1]
        return texto[abre:]

    @classmethod
    def llaves_tras_condicion(cls, texto, parentesis):
        """El bloque `{…}` que sigue a una condición `(…)` que abre en `parentesis`,
        o `None` si después de la condición no hay llaves."""
        profundidad, i = 0, parentesis
        while i < len(texto):
            if texto[i] == "(":
                profundidad += 1
            elif texto[i] == ")":
                profundidad -= 1
                if profundidad == 0:
                    break
            i += 1
        j = i + 1
        while j < len(texto) and texto[j] in " \t\r\n":
            j += 1
        if j >= len(texto) or texto[j] != "{":
            return None
        return cls.llaves(texto, j)

    @staticmethod
    def sangria(lineas, desde, sangria):
        """Las líneas del bloque que empieza en `desde` y tiene más sangría que
        `sangria`. Las vacías del medio cuentan como parte del bloque."""
        cuerpo = []
        for linea in lineas[desde:]:
            if linea.strip() and len(linea) - len(linea.lstrip()) <= sangria:
                break
            cuerpo.append(linea)
        return cuerpo


class ValidadorDeCodigo(Validador):
    """Un validador que revisa el texto de cada archivo de código.

    Cada subclase escribe solo `revisar_texto`; el recorrido es este.
    """

    def validar(self):
        hallazgos = []
        for donde, texto in RecorridoDeCodigo(self.proyecto, self.archivos).archivos():
            if self.aplica_a(donde):
                hallazgos += self.revisar_texto(texto, donde)
        return hallazgos

    def aplica_a(self, donde):
        """Si este archivo se revisa. Por defecto, todo el código."""
        return True

    def revisar_texto(self, texto, donde=""):
        """El núcleo puro: los hallazgos de un texto."""
        raise NotImplementedError("%s no escribió revisar_texto()" % type(self).__name__)
