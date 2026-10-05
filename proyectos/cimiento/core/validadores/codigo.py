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
            prefijo = self.proyecto.prefijo_de(repo)
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


_FUNC_LLAVES = re.compile(r"\bfunction\b\s*&?\s*(\w*)[^\n;(]*\([^;{]*\)\s*(?::\s*[\w\\|?]+\s*)?\{")
_DEF_PYTHON = re.compile(r"^(\s*)def\s+(\w+)\s*\(")


class Funciones:
    """Las funciones de un texto: con llaves y `function` (PHP, JavaScript) y `def`
    de Python. La usan el validador de funciones largas (`07·Q3`) y el de
    funciones repetidas (`07·Q4`): separarlas dos veces es justo lo que `Q4` prohíbe."""

    LLAVES = "llaves"
    SANGRIA = "sangria"

    @staticmethod
    def de(texto):
        """`[(nombre, línea, cuerpo, forma)]`. El cuerpo con llaves va de `{` a `}`;
        el de sangría son las líneas del bloque, unidas."""
        salida = []
        for m in _FUNC_LLAVES.finditer(texto):
            cuerpo = Bloques.llaves(texto, texto.find("{", m.start()))
            salida.append((m.group(1), RecorridoDeCodigo.linea_de(texto, m.start()), cuerpo, Funciones.LLAVES))
        lineas = texto.splitlines()
        for i, linea in enumerate(lineas):
            m = _DEF_PYTHON.match(linea)
            if m:
                cuerpo = "\n".join(Bloques.sangria(lineas, i + 1, len(m.group(1))))
                salida.append((m.group(2), i + 1, cuerpo, Funciones.SANGRIA))
        return salida

    @classmethod
    def largo(cls, cuerpo, forma):
        """Las líneas que cuenta `07·Q3`: entre las llaves, o las no vacías del bloque."""
        if forma == cls.LLAVES:
            return cuerpo.count("\n") - 1
        return sum(1 for l in cuerpo.splitlines() if l.strip())


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
