"""`05·E1` y `05·E5` · Errores visibles y logs sin secretos.

E1: un error capturado se maneja visible y trazable. Lo comprobable es el caso
extremo: una captura con el cuerpo **vacío**.

E5: los logs no llevan secretos. Lo comprobable es una llamada de log que
nombra un campo con nombre de secreto (`password`, `token`, `cvv`…).

Todo es aviso: puede ser deliberado y estar bien; lo confirma una persona.
"""
import re

from ..comun import AVISO, Hallazgo
from .codigo import RecorridoDeCodigo, ValidadorDeCodigo

# E1 · `catch (…) {}` o `catch {}` con el cuerpo vacío, aunque ocupe varias líneas.
_CATCH_LLAVES = re.compile(r"catch\s*(?:\([^)]*\))?\s*\{\s*\}")
# E1 · Python: `except …:` cuyo único cuerpo es `pass`.
_EXCEPT_PASS = re.compile(r"except\b[^:\n]*:[ \t]*(?:\r?\n[ \t]*)?pass\b")

# E5 · una llamada de log y, en la misma línea, un campo con pinta de secreto.
_LOG = re.compile(
    r"(?i)(console\.(log|error|warn|info|debug)|Log::\w+|\blogger\.\w+|"
    r"\blogging\.\w+|\blog\.\w+|\blogger\s*\(|error_log\s*\()")
_SENSIBLE = re.compile(
    r"(?i)\b(pass(?:word|wd)?|contrase\w+|secret|token|api[_-]?key|apikey|"
    r"authorization|cvv|tarjeta|card[_-]?number|numero_tarjeta)\b")


class CapturasYLogs(ValidadorDeCodigo):
    """Avisa de las capturas de error vacías y de los logs con secretos."""

    nombre = "errores"
    regla = "05·E1, 05·E5"
    descripcion = "capturas vacías y secretos en los logs"

    def revisar_texto(self, texto, donde=""):
        hallazgos = []
        for patron, forma in ((_CATCH_LLAVES, "catch"), (_EXCEPT_PASS, "except: pass")):
            for m in patron.finditer(texto):
                hallazgos.append(Hallazgo(
                    AVISO, donde, RecorridoDeCodigo.linea_de(texto, m.start()),
                    "captura de error vacía (`%s`) — E1 pide manejo visible y trazable" % forma))
        for n, linea in enumerate(texto.splitlines(), 1):
            if _LOG.search(linea) and _SENSIBLE.search(linea):
                hallazgos.append(Hallazgo(
                    AVISO, donde, n,
                    "posible secreto en un log — E5: los logs no llevan contraseñas/tokens"))
        return hallazgos
