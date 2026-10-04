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
