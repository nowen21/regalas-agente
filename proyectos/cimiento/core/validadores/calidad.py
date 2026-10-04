"""`07·Q3` · Funciones pequeñas: cada función hace una cosa.

Lo que se comprueba sin criterio es la **longitud**: una función muy larga casi
siempre hace varias cosas. Es aviso, no falla: marca lo que conviene mirar.

Lee funciones con llaves y `function` (PHP, JavaScript) y `def` de Python.
"""
import re

from ..comun import AVISO, Hallazgo
from .codigo import Bloques, RecorridoDeCodigo, ValidadorDeCodigo

_FUNC_LLAVES = re.compile(r"\bfunction\b[^\n;(]*\([^;{]*\)\s*(?::\s*[\w\\|?]+\s*)?\{")
_DEF_PYTHON = re.compile(r"^(\s*)def\s+\w+\s*\(")


class FuncionesLargas(ValidadorDeCodigo):
    """Avisa de las funciones cuyo cuerpo pasa de `tope` líneas."""

    nombre = "calidad"
    regla = "07·Q3"
    descripcion = "funciones demasiado largas"
    tope = 60

    def revisar_texto(self, texto, donde=""):
        hallazgos = []
        for m in _FUNC_LLAVES.finditer(texto):
            largo = Bloques.llaves(texto, texto.find("{", m.start())).count("\n") - 1
            if largo > self.tope:
                hallazgos.append(self._aviso(donde, RecorridoDeCodigo.linea_de(texto, m.start()), largo))
        lineas = texto.splitlines()
        for i, linea in enumerate(lineas):
            m = _DEF_PYTHON.match(linea)
            if m:
                largo = sum(1 for l in Bloques.sangria(lineas, i + 1, len(m.group(1))) if l.strip())
                if largo > self.tope:
                    hallazgos.append(self._aviso(donde, i + 1, largo))
        return hallazgos

    def _aviso(self, donde, linea, largo):
        return Hallazgo(AVISO, donde, linea, "función de ~%d líneas (tope %d) — %s: una función, "
                        "una cosa" % (largo, self.tope, self.regla), regla=self.regla)
