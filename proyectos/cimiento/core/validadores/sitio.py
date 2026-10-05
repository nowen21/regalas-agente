"""`EP-005·HU-011` · El mapa del sitio no envejece en silencio.

El mapa (`anatomia/mapa-del-sitio.md`) dice dónde vive cada cosa: es la puerta
de entrada de quien abre el repositorio por primera vez. Se escribe a mano, y
una carpeta nueva no aparece ahí hasta que alguien se acuerde; quien lo lea
creerá que no existe.

**Se mira por los dos lados**, igual que el mapa del amarre: la carpeta que
existe y el mapa no nombra, y la que el mapa nombra y ya no existe. **Lo que no
se comprueba** es si la descripción es acertada: eso se lee.
"""
import os
import re

from ..comun import AVISO, FALLA, Hallazgo
from .base import Validador

MAPA = os.path.join("anatomia", "mapa-del-sitio.md")

# Lo que no es del mapa: generado, local o de terceros. Se nombra una por una y
# no por patrón amplio, para que una carpeta nueva de verdad no se cuele.
FUERA = {
    ".git", ".venv", "venv", "__pycache__", ".pytest_cache", ".idea", ".vscode",
    "node_modules", "terceros", ".mypy_cache", ".ruff_cache", "dist", "build",
}


def _nombrada(nombre, texto):
    """`mis-plantillas/` no nombra `plantillas/`."""
    return re.search(r"(?<![\w/-])%s/" % re.escape(nombre), texto) is not None


class MapaDelSitio(Validador):
    """Las dos formas de envejecer de un mapa escrito a mano."""

    nombre = "sitio"
    regla = "EP-005·HU-011"
    descripcion = "el mapa del sitio nombra toda carpeta que existe: no envejece"

    @property
    def mapa(self):
        return os.path.join(self.proyecto.raiz, *MAPA.split(os.sep))

    def _texto(self):
        return self.archivos.leer(self.mapa) if os.path.isfile(self.mapa) else ""

    def carpetas(self):
        """Las carpetas de primer nivel que el mapa debería nombrar."""
        raiz = self.proyecto.raiz
        return [n for n in sorted(os.listdir(raiz))
                if n not in FUERA and not n.startswith(".") and os.path.isdir(os.path.join(raiz, n))]

    def validar(self):
        archivo, texto = self.mapa, self._texto()
        if not texto:
            return [Hallazgo(FALLA, archivo, 0, "falta el mapa del sitio, que es por donde entra quien abre el "
                                                "repositorio y no sabe dónde está nada")]
        existentes = self.carpetas()
        hallazgos = [Hallazgo(FALLA, archivo, 0, "`%s/` no está en el mapa — quien lo lea va a creer que esa "
                                                 "carpeta no existe" % nombre)
                     for nombre in existentes if not _nombrada(nombre, texto)]
        return hallazgos + [Hallazgo(AVISO, archivo, 0, "el mapa nombra `%s/`, que ya no existe — se movió o se "
                                                        "borró, y el mapa manda a alguien a un sitio vacío" % citada)
                            for citada in sorted(set(re.findall(r"`([a-z0-9][\w.-]*)/`", texto)))
                            if citada not in existentes and citada not in FUERA]

    def linea_resumen(self):
        """El recuento, para poder mirarlo sin abrir el mapa."""
        texto = self._texto()
        if not texto:
            return ""
        existentes = self.carpetas()
        nombradas = sum(1 for n in existentes if _nombrada(n, texto))
        return ("Carpetas de primer nivel: %d · nombradas en el mapa: %d · sin nombrar: %d"
                % (len(existentes), nombradas, len(existentes) - nombradas))
