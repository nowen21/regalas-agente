"""Qué archivo tocó cada sesión, para que un commit no se lleve lo ajeno.

El 2026-08-22 dos sesiones trabajaron a la vez sobre el repositorio y una
commiteó todo el árbol: se llevó un validador a medio corregir y moldes sin
llenar (pendiente 80).

**Lo que se comprueba no es de quién es el commit, sino que mezcle.** `git` no
sabe qué sesión lo lanza, y no hace falta: si lo que entra lo tocaron dos
sesiones distintas, alguien publica trabajo que no es suyo. **Avisa, no detiene**:
retomar lo que otra dejó a medias es normal; hacerlo sin darse cuenta, no.

**El registro no se versiona.** Es estado de trabajo y vive en
`historico-chat/.tocado/`, que está en el `.gitignore`: versionado sería el
próximo archivo que dos sesiones se pisan.
"""
import io
import os
import subprocess
import time

from ..comun import AVISO, Hallazgo, Proyecto
from .base import Validador

CARPETA = os.path.join("historico-chat", ".tocado")

# Una sesión que lleva más de esto sin escribir ya no está viva. Doce horas
# cubre una jornada larga sin cubrir la del día siguiente.
VIGENCIA = 12 * 3600


def _limpio(sesion):
    """El identificador, sin nada que pueda salirse de la carpeta."""
    return "".join(c for c in str(sesion) if c.isalnum() or c in "-_")[:64]


class Sesiones:
    """El registro de lo que tocó cada sesión en un proyecto."""

    def __init__(self, proyecto):
        self.proyecto = proyecto if isinstance(proyecto, Proyecto) else Proyecto(proyecto)

    @property
    def carpeta(self):
        return os.path.join(self.proyecto.raiz, CARPETA)

    def ruta_de(self, sesion):
        return os.path.join(self.carpeta, _limpio(sesion) + ".txt")

    @staticmethod
    def leer_sesion(ruta):
        if not os.path.isfile(ruta):
            return set()
        with io.open(ruta, encoding="utf-8") as f:
            return {l.strip() for l in f if l.strip()}

    def anotar(self, sesion, archivo):
        """Deja escrito que `sesion` tocó `archivo`. Sin sesión, no hace nada."""
        if not sesion or not archivo:
            return
        if not os.path.isdir(self.carpeta):
            os.makedirs(self.carpeta)
        rel = self.proyecto.relativa(archivo)
        if rel is None:
            return                      # de otro proyecto: no es asunto de acá
        ruta = self.ruta_de(sesion)
        if rel in self.leer_sesion(ruta):
            # Sin esto el registro crece sin límite, y la hora de la última
            # escritura deja de decir cuándo la sesión hizo algo nuevo.
            os.utime(ruta, None)
            return
        with io.open(ruta, "a", encoding="utf-8", newline="\n") as f:
            f.write(rel + "\n")

    def estado_de_git(self):
        """`(cambiadas, borradas)` según git. Vacías si acá no hay repositorio.

        `EP-005·HU-020` · Se anota lo que cambió, lo escriba quien lo escriba:
        el registro solo se llenaba desde las herramientas de escritura, y un
        archivo escrito por un guion no parecía de otro, parecía de nadie.
        """
        try:
            salida = subprocess.check_output(["git", "status", "--porcelain"],
                                             cwd=self.proyecto.raiz, stderr=subprocess.DEVNULL)
        except (OSError, subprocess.CalledProcessError):
            return ([], [])
        cambiadas, borradas = [], []
        for linea in salida.decode("utf-8", "replace").splitlines():
            if len(linea) < 4:
                continue
            marca, ruta = linea[:2], linea[3:].strip().strip('"')
            if " -> " in ruta:                  # renombrado: cuenta el destino
                ruta = ruta.split(" -> ")[-1]
            # Los ignorados no se piden a propósito: no son trabajo versionado,
            # y el propio registro vive en uno de ellos.
            (borradas if "D" in marca else cambiadas).append(ruta)
        return (cambiadas, borradas)

    def cambios_del_turno(self, desde):
        """Lo que cambió después de `desde`. Con `desde` en `None`, **nada**.

        La primera vuelta no reclama nada: sin fecha contra la cual comparar,
        la primera sesión del día se atribuiría el árbol entero. Un borrado se
        anota siempre, porque no tiene fecha que mirar.
        """
        if desde is None:
            return []
        cambiadas, borradas = self.estado_de_git()
        salida = list(borradas)
        for ruta in cambiadas:
            try:
                if os.path.getmtime(os.path.join(self.proyecto.raiz, *ruta.split("/"))) > desde:
                    salida.append(ruta)
            except OSError:
                continue                        # desapareció entre medias: no se afirma
        return salida

    def anotar_el_turno(self, sesion):
        """Anota lo que cambió desde la última vuelta y lo devuelve. La fecha de
        la vuelta anterior es la del propio registro: no hace falta estado nuevo."""
        if not sesion or not os.path.isdir(self.proyecto.raiz):
            # Crear una carpeta que ya no está sería escribir fuera de todo proyecto (`04·S9`).
            return []
        ruta = self.ruta_de(sesion)
        desde = os.path.getmtime(ruta) if os.path.isfile(ruta) else None
        nuevos = self.cambios_del_turno(desde)
        for archivo in nuevos:
            self.anotar(sesion, os.path.join(self.proyecto.raiz, *archivo.split("/")))
        if desde is None:
            # Arranca el reloj sin reclamar nada.
            if not os.path.isdir(self.carpeta):
                os.makedirs(self.carpeta)
            io.open(ruta, "a", encoding="utf-8").close()
        return nuevos

    def registros(self, ahora=None):
        """`{sesión: {archivos}}` de las sesiones todavía vivas."""
        if not os.path.isdir(self.carpeta):
            return {}
        ahora = ahora if ahora is not None else time.time()
        salida = {}
        for nombre in sorted(os.listdir(self.carpeta)):
            if not nombre.endswith(".txt"):
                continue
            ruta = os.path.join(self.carpeta, nombre)
            if ahora - os.path.getmtime(ruta) > VIGENCIA:
                continue
            archivos = self.leer_sesion(ruta)
            if archivos:
                salida[nombre[:-4]] = archivos
        return salida


class SesionesMezcladas(Validador):
    """Avisa si lo que entra al commit lo tocaron dos sesiones."""

    nombre = "sesiones"
    regla = ""
    descripcion = "que el commit no mezcle el trabajo de dos sesiones: avisa"

    def __init__(self, proyecto, archivos=None, ahora=None):
        super().__init__(proyecto, archivos)
        self.sesiones = Sesiones(self.proyecto)
        self.ahora = ahora

    def preparados(self):
        """Lo que entra en el commit, en rutas del repositorio."""
        try:
            salida = subprocess.check_output(["git", "diff", "--cached", "--name-only"],
                                             cwd=self.proyecto.raiz, stderr=subprocess.DEVNULL)
        except (OSError, subprocess.CalledProcessError):
            return []
        return [l.strip() for l in salida.decode("utf-8", "replace").splitlines() if l.strip()]

    def validar(self):
        entrando = set(self.preparados())
        if not entrando:
            return []
        de_quien = {sesion: entrando & archivos for sesion, archivos in self.sesiones.registros(self.ahora).items()
                    if entrando & archivos}
        if len(de_quien) < 2:
            return []
        detalle = " · ".join("%s: %d" % (sesion[:8], len(archivos)) for sesion, archivos in sorted(de_quien.items()))
        ejemplos = sorted(a for _sesion, archivos in sorted(de_quien.items())[1:] for a in archivos)[:3]
        return [Hallazgo(AVISO, os.path.join(self.proyecto.raiz, ".git"), 0,
                         "este commit mezcla archivos de %d sesiones (%s) — si no es a propósito, saca del commit "
                         "lo que no salió de esta conversación; empieza por %s"
                         % (len(de_quien), detalle, ", ".join(ejemplos)))]
