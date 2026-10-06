"""El proyecto que se revisa: su raíz y las rutas dentro de ella.

Junta lo que estaba repartido: la raíz pedida con `--raiz` (copiada en diez
enganches), la ruta `/c/...` de la consola de Git (arreglada en `freno.py` y
olvidada en `rutas_fuera.py`) y las dos formas distintas de saber si una ruta
queda dentro del proyecto (análisis 1 del pendiente 116).
"""
import os
import re

from .git import Git

_UNIDAD_GIT_BASH = re.compile(r"^/([a-zA-Z])(?=/|$)")

# Carpetas que nunca se recorren. `reglas-por-tarea/` son copias de las reglas
# de `base/`: recorridas, se contarían como reglas repetidas.
EXCLUIDAS = {".git", "__pycache__", ".venv", "venv", "node_modules", "vendor", "reglas-por-tarea"}

# Lo que se salta por su **ruta**, no por su nombre (`datos` es un nombre que
# cualquier proyecto le puede dar a una carpeta suya): los proyectos que viven
# en `proyectos/` se validan desde su carpeta, y `datos/proyectos` es lo que
# Cimiento trajo de otros proyectos, con enlaces que resuelven allá.
EXCLUIDAS_POR_RUTA = ("proyectos", "datos/proyectos")

# `EP-025·HU-014` · «Rutas en los avisos» de cada proyecto, leído una vez por proceso.
_RUTAS = {}

# Lo que distingue la carpeta del estándar: su núcleo.
_SENA_DEL_ESTANDAR = os.path.join("base", "00-nucleo-blindado.md")


class Proyecto:
    """Una carpeta de proyecto, con todo lo que se pregunta sobre sus rutas."""

    def __init__(self, raiz):
        self.raiz = os.path.realpath(os.path.abspath(raiz))

    @classmethod
    def desde_argumentos(cls, argumentos, por_defecto):
        """`--raiz X` si viene en la orden; si no, `por_defecto`."""
        if "--raiz" in argumentos:
            i = argumentos.index("--raiz")
            if i + 1 < len(argumentos):
                return cls(argumentos[i + 1])
        return cls(por_defecto)

    @staticmethod
    def ruta_real(ruta, desde):
        """La ruta absoluta y resuelta: variables, `~`, `..`, enlaces y `/c/...`."""
        ruta = os.path.expanduser(os.path.expandvars(ruta.strip().strip("\"'")))
        if os.name == "nt":
            ruta = _UNIDAD_GIT_BASH.sub(lambda m: m.group(1).upper() + ":", ruta)
        if not os.path.isabs(ruta):
            ruta = os.path.join(desde, ruta)
        return os.path.realpath(ruta)

    def relativa(self, ruta):
        """La ruta dentro del proyecto, con `/`, o `None` si queda afuera.

        Se compara por partes y no con `startswith` del texto: `.../agente` es
        prefijo de `.../agente-viejo` y no lo contiene.
        """
        absoluta = self.ruta_real(ruta, self.raiz)
        raiz = os.path.normcase(self.raiz).rstrip(os.sep)
        destino = os.path.normcase(absoluta)
        if destino != raiz and not destino.startswith(raiz + os.sep):
            return None
        return os.path.relpath(absoluta, self.raiz).replace("\\", "/")

    def contiene(self, ruta):
        return self.relativa(ruta) is not None

    def ruta(self, relativa):
        """La ruta absoluta de algo escrito con `/` desde la raíz."""
        return os.path.join(self.raiz, *relativa.split("/"))

    @staticmethod
    def estandar():
        """La carpeta del estándar (`base/`, `plantillas/`): `CIMIENTO` si está
        puesta, o la primera que se encuentra subiendo desde este archivo."""
        puesta = os.environ.get("CIMIENTO")
        if puesta:
            return os.path.abspath(puesta)
        carpeta = os.path.dirname(os.path.abspath(__file__))
        while True:
            if os.path.isfile(os.path.join(carpeta, _SENA_DEL_ESTANDAR)):
                return carpeta
            arriba = os.path.dirname(carpeta)
            if arriba == carpeta:
                return None
            carpeta = arriba

    def mostrar(self, ruta):
        """Cómo se nombra una ruta en un reporte: desde la raíz si queda adentro,
        completa si queda afuera.

        `EP-025·HU-014` · Si el ajuste «Rutas en los avisos» del proyecto dice
        «completas», sale completa aunque quede adentro.
        """
        completa = os.path.abspath(ruta).replace("\\", "/")
        relativa = self.relativa(ruta)
        if relativa is None or self.rutas_en_avisos() == "completas":
            return completa
        return relativa

    def rutas_en_avisos(self):
        """El ajuste del proyecto, leído una vez por proceso. Si no se puede leer, «relativas»."""
        clave = os.path.normcase(self.raiz)
        if clave not in _RUTAS:
            try:
                from ..enganches.configuracion import ConfiguracionDelProyecto
                _RUTAS[clave] = ConfiguracionDelProyecto(self.raiz).valor("rutas_en_avisos")
            except Exception:  # noqa: BLE001  Mostrar una ruta no puede tumbar a quien la muestra.
                _RUTAS[clave] = "relativas"
        return _RUTAS[clave]

    def es_excluida(self, relativa):
        """¿Esta ruta (con `/`, desde la raíz) se salta por su ubicación?"""
        return any(relativa == fuera or relativa.startswith(fuera + "/") for fuera in EXCLUIDAS_POR_RUTA)

    def recorrer_md(self, desde=""):
        """Todos los `.md` del proyecto, o de la carpeta `desde` (con `/`, desde
        la raíz), sin las carpetas excluidas."""
        for carpeta, subcarpetas, archivos in os.walk(self.ruta(desde) if desde else self.raiz):
            subcarpetas[:] = [s for s in subcarpetas if s not in EXCLUIDAS]
            if self.es_excluida(os.path.relpath(carpeta, self.raiz).replace("\\", "/")):
                subcarpetas[:] = []
                continue
            for nombre in sorted(archivos):
                if nombre.lower().endswith(".md"):
                    yield os.path.join(carpeta, nombre)

    def prefijo_de(self, repo):
        """Cómo se nombra lo de un repositorio: `""` si es la raíz, `"carpeta/"`
        si vive dentro (`proyectos/x/`). Estaba repetido en cada validador."""
        etiqueta = os.path.relpath(repo, self.raiz).replace("\\", "/")
        return "" if etiqueta == "." else etiqueta + "/"

    def repositorios(self):
        """La raíz si es repositorio, más cada repositorio dentro de `proyectos/` (`02·F13`)."""
        encontrados = [self.raiz] if Git.es_repositorio(self.raiz) else []
        proyectos = os.path.join(self.raiz, "proyectos")
        if os.path.isdir(proyectos):
            for nombre in sorted(os.listdir(proyectos)):
                sub = os.path.join(proyectos, nombre)
                if os.path.isdir(sub) and Git.es_repositorio(sub):
                    encontrados.append(sub)
        return encontrados
