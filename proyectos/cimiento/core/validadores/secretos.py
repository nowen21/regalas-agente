"""`04·S4` y `00·N6` · Ningún secreto escrito en el código.

El validador de versionado (`09·G3`) mira **nombres** de archivo; este mira el
**contenido** del código y la configuración versionados, buscando un secreto
escrito a mano.

  Falla — la forma **es** el secreto: clave de AWS, bloque de clave privada,
          token de un proveedor. Un secreto en git no se borra editándolo.
  Aviso — una variable con pinta de secreto asignada a un texto fijo. Puede ser
          un molde o un dato de prueba; lo confirma una persona.

Los `.md` quedan fuera a propósito: la documentación muestra secretos de ejemplo.
"""
import os
import re

from ..comun import AVISO, FALLA, Git, Hallazgo
from .base import Validador

EXTENSIONES = {
    ".php", ".py", ".js", ".ts", ".jsx", ".tsx", ".vue", ".mjs", ".cjs",
    ".rb", ".go", ".java", ".kt", ".cs", ".rs", ".swift", ".scala",
    ".yml", ".yaml", ".ini", ".conf", ".cfg", ".toml", ".properties",
    ".sh", ".bash", ".ps1", ".xml", ".env",
}
SALTAR = re.compile(r"(^|/)(vendor|node_modules|dist|build|\.git)/|"
                    r"(^|/)(composer\.lock|package-lock\.json|yarn\.lock|pnpm-lock\.yaml)$|\.min\.(js|css)$")

# Las pruebas de este mismo detector traen claves falsas a propósito. Se nombran
# **una por una, nunca por carpeta**: exceptuar `tests/` entero dejaría ciego al
# detector sobre lo que se escriba ahí mañana. Quien agregue una prueba con algo
# con forma de clave pone su nombre acá en la misma vuelta.
EXENTOS = (
    "validadores/tests/test_la_clave_no_llega_al_historico.py",
    "validadores/tests/test_el_validador_no_revisa_lo_ajeno.py",
    "validadores/tests/test_la_clave_sin_comillas_se_enmascara.py",
    "validadores/tests/test_el_conteo_por_regla.py",
    "validadores/pruebas.py",
    "proyectos/cimiento/core/validadores/tests_repositorio.py",
)

SEGUROS = [
    (re.compile(r"AKIA[0-9A-Z]{16}"), "clave de acceso AWS"),
    (re.compile(r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY-----"), "bloque de clave privada"),
    (re.compile(r"\bsk_live_[0-9A-Za-z]{16,}"), "clave secreta de Stripe (live)"),
    (re.compile(r"\bSG\.[\w\-]{16,}\.[\w\-]{16,}"), "clave de SendGrid"),
    (re.compile(r"\bxox[baprs]-[0-9A-Za-z\-]{10,}"), "token de Slack"),
    (re.compile(r"\bgh[pousr]_[0-9A-Za-z]{20,}"), "token de GitHub"),
    (re.compile(r"\bglpat-[\w\-]{20,}"), "token de acceso de GitLab"),
    (re.compile(r"\bAIza[0-9A-Za-z_\-]{35}"), "clave de API de Google"),
]

# Una variable con pinta de secreto igualada a un literal. La usa también el
# enmascarador del histórico: la misma clave, tecleada por una persona.
ASIGNA = re.compile(
    r"(?i)\b(?P<clave>pass(?:word|wd)?|secret|api[_-]?key|apikey|"
    r"access[_-]?key|client[_-]?secret|auth[_-]?token|private[_-]?key)\b"
    r"\s*[:=]>?\s*(?P<comilla>['\"])(?P<valor>[^'\"]{6,})(?P=comilla)")
# Si la misma línea lee del entorno o de la configuración, no hay nada escrito.
_ENTORNO = re.compile(r"(?i)\benv\b|getenv|os\.environ|process\.env|\bconfig\(|\$\{|\bimport\b")
_MOLDE_EXACTO = re.compile(r"(?i)^(x{3,}|\.{3,}|\*{3,}|changeme|placeholder|dummy|sample|example|"
                           r"ejemplo|null|none|password|secret|test|123456|abc123|<.+>)$")
_MOLDE_PREFIJO = re.compile(r"(?i)^(your|tu|my|mi|example|ejemplo|placeholder|sample|dummy|test|x{3,})[_\- ]")


class SecretosEnElCodigo(Validador):
    """Busca secretos escritos en el código y la configuración versionados."""

    nombre = "secretos"
    regla = "04·S4, 00·N6"
    descripcion = "secretos incrustados en el código"

    def validar(self):
        repos = self.proyecto.repositorios()
        if not repos:
            return [Hallazgo(FALLA, self.proyecto.raiz, 0, "no hay repositorios git que revisar")]
        hallazgos = []
        for repo in repos:
            prefijo = self.proyecto.prefijo_de(repo)
            for archivo in Git(repo).versionados():
                if (SALTAR.search(archivo) or archivo in EXENTOS or prefijo + archivo in EXENTOS
                        or os.path.splitext(archivo)[1].lower() not in EXTENSIONES):
                    continue
                try:
                    with open(os.path.join(repo, archivo), encoding="utf-8", errors="replace") as f:
                        texto = f.read(1_000_000)       # más de 1 MB es dato, no código
                except OSError:
                    continue
                hallazgos += self.revisar_texto(texto, prefijo + archivo)
        return hallazgos

    @staticmethod
    def _parece_secreto(valor):
        v = valor.strip()
        return not (_MOLDE_EXACTO.match(v) or _MOLDE_PREFIJO.match(v))

    @classmethod
    def revisar_texto(cls, texto, donde=""):
        """El núcleo puro: una falla o un aviso por línea, como mucho."""
        hallazgos = []
        for n, linea in enumerate(texto.splitlines(), 1):
            seguro = next((motivo for patron, motivo in SEGUROS if patron.search(linea)), None)
            if seguro:
                hallazgos.append(Hallazgo(FALLA, donde, n, "posible secreto en el código (%s) · S4/N6" % seguro))
                continue
            m = ASIGNA.search(linea)
            if m and cls._parece_secreto(m.group("valor")) and not _ENTORNO.search(linea):
                hallazgos.append(Hallazgo(AVISO, donde, n, "`%s` asignada a un texto fijo — ¿debería leerse "
                                                           "del entorno? (S4)" % m.group("clave")))
        return hallazgos
