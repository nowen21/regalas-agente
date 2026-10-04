"""Leer archivos sin que uno roto tumbe la corrida entera."""
import os

from .hallazgos import AVISO, Hallazgo


class Archivos:
    """Lee texto y anota lo que no pudo leer bien.

    **Ni excepción ni silencio.** Un archivo mal codificado no detiene la
    corrida, porque se llevaría los hallazgos ya encontrados; pero tampoco se
    calla, porque un archivo roto leído a medias parece sano. Se sigue, y queda
    anotado para que `ilegibles()` lo diga con su ruta.
    """

    def __init__(self):
        self._ilegibles = {}

    def leer(self, ruta):
        """El texto del archivo; `""` si no se pudo abrir. Nunca revienta."""
        clave = os.path.abspath(ruta)
        try:
            with open(ruta, encoding="utf-8") as f:
                texto = f.read()
        except UnicodeDecodeError as e:
            self._ilegibles[clave] = (
                "no es UTF-8 (posición %d) — se leyó reemplazando lo que no se "
                "entiende, así que lo dicho de este archivo puede estar incompleto" % e.start)
            with open(ruta, encoding="utf-8", errors="replace") as f:
                return f.read()
        except OSError as e:
            self._ilegibles[clave] = "no se pudo abrir: %s" % (e.strerror or e)
            return ""
        self._ilegibles.pop(clave, None)
        return texto

    def ilegibles(self):
        """Un aviso por cada archivo que no se leyó bien: de él no se puede opinar."""
        return [Hallazgo(AVISO, ruta, 0, motivo) for ruta, motivo in sorted(self._ilegibles.items())]
