"""`EP-005·HU-018` · Avisa cuando el agente escribe fuera del proyecto.

`04·S9` dice que el agente escribe solo dentro de la carpeta del proyecto, y se
incumplió cuatro días seguidos: 38 guiones en la carpeta temporal del sistema y
dos clones enteros de la plataforma (`S-057`). Lo que fallaba no era la regla:
era que nada la hacía cumplir, y la herramienta ofrece una carpeta temporal
como el sitio recomendado.

**Se compara por tramos y no por prefijo.** `.../agente` es prefijo de
`.../agente-viejo`: un `startswith` daría la hermana por dentro, y el aviso
callaría justo donde debía hablar.

**Ante la duda no se acusa** (`04·R4`). Un aviso falso vale menos que uno que
falta: el agente escribe decenas de archivos por sesión, y un falso positivo por
sesión lo vuelve ruido que se apaga.

**Avisa, no mueve ni borra** (`EP-004 §10.2`): mover lo que el agente acaba de
escribir rompe lo que estaba haciendo y esconde el incumplimiento.

No usa `Proyecto.contiene`: esa no tiene una salida para la ruta que no se
deja resolver, y esta calla en ese caso; esa diferencia es la regla.
"""
import os

# Dónde van los guiones de apoyo. Se nombra en el aviso porque un aviso que
# no dice qué hacer se aprende a ignorar.
DESTINO = "historico-chat/scripts/AAAA-MM-DD/"


class RutasFuera:
    """Todo es estático: compara dos rutas, no guarda estado."""

    DESTINO = DESTINO

    @staticmethod
    def _partes(ruta):
        """Los tramos de una ruta, normalizados para comparar. `normcase` hace
        que en Windows `C:\\Ing` y `c:\\ing` sean la misma carpeta, y en Linux no."""
        normal = os.path.normcase(os.path.normpath(ruta))
        return [tramo for tramo in normal.replace("\\", "/").split("/") if tramo]

    @classmethod
    def dentro_del_proyecto(cls, ruta, proyecto):
        """`True` si `ruta` cae dentro de `proyecto`, **o si no se pudo saber**."""
        # `strip()` y no solo `not ruta`: una ruta de puros espacios no es una ruta.
        if not (ruta or "").strip() or not (proyecto or "").strip():
            return True
        try:
            # Por `os.path.realpath` y no importada aparte: así una prueba puede
            # forzar el fallo y tocar la rama de la duda.
            suya = cls._partes(os.path.realpath(os.path.abspath(ruta)))
            casa = cls._partes(os.path.realpath(os.path.abspath(proyecto)))
        except (OSError, ValueError, TypeError):
            return True
        if not casa:
            return True
        return suya[:len(casa)] == casa

    @classmethod
    def aviso(cls, ruta, proyecto):
        """El texto que se muestra, o `""` si la ruta está donde debe. Dice la
        ruta escrita y dónde debía ir: sin la primera no se sabe qué archivo, y
        sin la segunda hay que ir a buscarlo."""
        if cls.dentro_del_proyecto(ruta, proyecto):
            return ""
        return (
            "[AVISO] se escribió fuera del proyecto: %s — los guiones de apoyo van "
            "en `%s`, y se quedan ahí versionados (`04·S9`, EP-005·HU-018). "
            "Leer fuera sí vale; escribir, no." % (ruta, DESTINO))
