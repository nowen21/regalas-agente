"""`09·G3` · Qué está versionado que no debería.

G3 manda fuera del repositorio los secretos, los datos reales, lo generado y la
configuración de cada máquina, y pide versionar en su lugar una plantilla de
ejemplo sin valores.

La fuente es `git ls-files`: lo que git tiene registrado, no lo que hay en el
disco. **Un secreto subido no se borra editándolo**: queda en el historial de
todos los que clonaron. Por eso los secretos son falla y no aviso.
"""
import os
import re

from ..comun import AVISO, FALLA, Git, Hallazgo
from .base import Validador

# Plantillas de ejemplo: G3 las quiere versionadas.
EJEMPLOS = re.compile(r"\.(example|sample|template|dist|ejemplo|plantilla)$|"
                      r"^\.env\.(example|sample|template|dist)$", re.IGNORECASE)

# Falla: no hay lectura sana en que estén bien.
PROHIBIDO = [
    (re.compile(r"(^|/)\.env(\.|$)", re.IGNORECASE), "entorno real con valores"),
    (re.compile(r"(^|/)node_modules/"), "dependencias instaladas"),
    (re.compile(r"\.(pem|key|p12|pfx|jks|keystore|ppk)$", re.IGNORECASE), "archivo de clave"),
    (re.compile(r"(^|/)id_(rsa|dsa|ecdsa|ed25519)$"), "clave SSH privada"),
    (re.compile(r"(^|/)\.npmrc$|(^|/)\.pypirc$|(^|/)\.netrc$"), "credenciales de repositorio"),
]

# Aviso: puede ser deliberado. El `.sql` se decide por contenido, no por extensión.
DUDOSO = [
    (re.compile(r"\.(log)$", re.IGNORECASE), "registro generado"),
    (re.compile(r"\.(sqlite|sqlite3|db|mdb)$", re.IGNORECASE), "base de datos"),
    (re.compile(r"(^|/)(\.idea|\.vscode)/"), "config local del editor"),
    (re.compile(r"(^|/)__pycache__/|\.pyc$"), "compilado de Python"),
    (re.compile(r"(^|/)(dist|build)/"), "artefacto de compilación"),
    (re.compile(r"(^|/)(\.DS_Store|Thumbs\.db)$"), "basura del sistema"),
]

MINIMO_INSERTS = 5
_INSERT = re.compile(r"\bINSERT\s+INTO\b", re.IGNORECASE)


class ArchivosVersionados(Validador):
    """Revisa lo versionado, o solo lo que entra en el próximo commit."""

    nombre = "versionado"
    regla = "09·G3"
    descripcion = "lo que está versionado y no debería"

    def __init__(self, proyecto, archivos=None, solo_preparados=False):
        super().__init__(proyecto, archivos)
        self.solo_preparados = solo_preparados

    def validar(self):
        hallazgos = []
        for repo in self.proyecto.repositorios():
            hallazgos += self.revisar_repositorio(repo, self.proyecto.prefijo_de(repo) or repo)
        return hallazgos

    def revisar_repositorio(self, repo, origen):
        """Los hallazgos de un repositorio; `origen` es cómo se nombra en el reporte.

        Con `solo_preparados` se mira solo lo que entra ahora: si se mirara todo,
        un archivo dudoso de hace meses bloquearía cada commit futuro.
        """
        git = Git(repo)
        versionados = git.preparados() if self.solo_preparados else git.versionados()
        hallazgos = []
        for archivo in versionados:
            veredicto = self.clasificar(repo, archivo)
            if veredicto:
                severidad, motivo = veredicto
                texto = "versionado y no debería" if severidad == FALLA else "¿debería estar versionado?"
                hallazgos.append(Hallazgo(severidad, origen, 0, "%s (%s): %s" % (texto, motivo, archivo)))
        if self.solo_preparados:
            return hallazgos            # el molde se revisa sobre el repositorio completo
        hay_molde = any(a.lower().startswith(".env.") and EJEMPLOS.search(a) for a in versionados)
        if os.path.isfile(os.path.join(repo, ".env")) and not hay_molde:
            hallazgos.append(Hallazgo(AVISO, origen, 0, "existe `.env` pero no hay plantilla de ejemplo "
                                                        "versionada (G3: se versiona el molde sin valores)"))
        return hallazgos

    @classmethod
    def clasificar(cls, repo, archivo):
        """`(severidad, motivo)` si el archivo no debería estar versionado, o `None`.

        Se clasifica una sola vez, en orden: exento, prohibido, dudoso.
        """
        if EJEMPLOS.search(archivo):
            return None
        # `vendor/` en la raíz son dependencias de Composer; más adentro
        # (`public/vendor/…`) es una librería copiada a propósito para andar sin
        # internet, y se versiona entera a conciencia.
        if archivo.startswith("vendor/"):
            return FALLA, "dependencias instaladas"
        for patron, motivo in PROHIBIDO:
            if patron.search(archivo):
                return FALLA, motivo
        if "/vendor/" in "/" + archivo:
            return None
        if archivo.lower().endswith(".sql"):
            return (AVISO, "volcado con datos reales") if cls._es_volcado(os.path.join(repo, archivo)) else None
        for patron, motivo in DUDOSO:
            if patron.search(archivo):
                return AVISO, motivo
        return None

    @staticmethod
    def _es_volcado(ruta):
        """¿Este `.sql` trae datos o solo estructura? Varios `INSERT INTO` es un
        volcado; marcarlo por la extensión daba falsos positivos en todos lados."""
        try:
            with open(ruta, encoding="utf-8", errors="replace") as f:
                muestra = f.read(2_000_000)
        except OSError:
            return False
        return len(_INSERT.findall(muestra)) >= MINIMO_INSERTS
