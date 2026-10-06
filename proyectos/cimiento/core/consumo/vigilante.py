# -*- coding: utf-8 -*-
"""`EP-025·HU-011` · El gasto llega a la base en cuanto Claude Code lo escribe.

Un proceso que queda corriendo (análisis 2 del pendiente 119, acuerdo 1): Windows
avisa cuando cambia un `.jsonl` de `~/.claude/projects/` (`watchdog`) y lo nuevo
se guarda con el mismo lector y el mismo guardado de siempre, que no duplican.

**Los avisos se juntan.** Claude Code escribe varias líneas seguidas; cada dos
segundos se lee una vez cada archivo que cambió. **La lista de proyectos se
vuelve a leer cada minuto**: uno que se registra con el vigilante corriendo
entra solo. **Al arrancar se lee desde donde quedó cada archivo**: lo escrito con
el vigilante apagado no se pierde.

**Guarda su número de proceso** (`04·S10`), para cerrarlo por él con `--parar`.
"""
import os
import threading
import time

from django.db import connections

from core.proyectos.claude import proyectos_de_claude
from core.proyectos.models import Proyecto

from .guardar import GuardadoDeConsumo, leer_lo_nuevo

CADA = 2.0                  # segundos entre una lectura y la siguiente
LISTA_CADA = 60.0           # segundos entre una lectura de los proyectos y la siguiente


def archivo_del_numero():
    """Donde queda el número del proceso: `.agente/` de Cimiento, local e ignorado."""
    cimiento = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    return os.path.join(cimiento, ".agente", "vigilar-consumo.pid")


def proceso_vivo(numero):
    """¿Corre un proceso con ese número?"""
    if not numero:
        return False
    if os.name == "nt":
        import ctypes
        acceso = 0x1000                     # PROCESS_QUERY_LIMITED_INFORMATION
        manija = ctypes.windll.kernel32.OpenProcess(acceso, False, int(numero))
        if not manija:
            return False
        codigo = ctypes.c_ulong()
        ctypes.windll.kernel32.GetExitCodeProcess(manija, ctypes.byref(codigo))
        ctypes.windll.kernel32.CloseHandle(manija)
        return codigo.value == 259          # STILL_ACTIVE
    try:
        os.kill(int(numero), 0)
        return True
    except OSError:
        return False


def numero_guardado(archivo=None):
    archivo = archivo or archivo_del_numero()
    try:
        with open(archivo, encoding="utf-8") as f:
            return int(f.read().strip() or 0)
    except (OSError, ValueError):
        return 0


class VigilanteDeConsumo:
    """Junta los `.jsonl` que cambian y guarda lo nuevo de cada uno."""

    def __init__(self, base=None):
        self.base = os.path.abspath(base or proyectos_de_claude())
        self.cambiados = set()
        self.candado = threading.Lock()
        self.proyectos = {}
        self.leida_la_lista = 0.0
        self.ultimo_error = ""

    def leer_proyectos(self):
        """`{carpeta de Claude Code en minúsculas: proyecto}` de los activos."""
        self.proyectos = {p.carpeta_claude.lower(): p for p in Proyecto.objects.filter(activo=True)}
        self.leida_la_lista = time.monotonic()

    def proyecto_de(self, ruta):
        """El proyecto activo dueño del `.jsonl`, por la primera carpeta bajo la base, o None."""
        try:
            relativa = os.path.relpath(os.path.abspath(ruta), self.base)
        except ValueError:
            return None                     # otra unidad
        partes = relativa.split(os.sep)
        if relativa.startswith("..") or len(partes) < 2:
            return None
        return self.proyectos.get(partes[0].lower())

    def avisar(self, ruta):
        """Lo llama `watchdog` cuando algo cambia. Solo anota."""
        if ruta.endswith(".jsonl"):
            with self.candado:
                self.cambiados.add(os.path.abspath(ruta))

    def guardar_lo_cambiado(self):
        """Lee una vez cada archivo anotado. Devuelve cuántos tenían algo nuevo."""
        # El proceso vive horas: una conexión que MariaDB ya cerró se cambia por
        # otra. Solo esa: `close_old_connections` cierra también las sanas.
        for conexion in connections.all():
            if conexion.connection is not None and not conexion.is_usable():
                conexion.close()
        if time.monotonic() - self.leida_la_lista > LISTA_CADA:
            self.leer_proyectos()
        with self.candado:
            rutas, self.cambiados = self.cambiados, set()
        nuevos = 0
        for ruta in sorted(rutas):
            proyecto = self.proyecto_de(ruta)
            if proyecto is None:
                continue
            # Un archivo que falla no tumba al vigilante (`EP-025·HU-015`): su
            # avance no se movió, así que el próximo cambio lo vuelve a intentar.
            try:
                if GuardadoDeConsumo(proyecto, self.base).leer_archivo(ruta) is not None:
                    nuevos += 1
            except Exception as error:  # noqa: BLE001
                self.ultimo_error = "%s: %s" % (os.path.basename(ruta), error)
        return nuevos

    def arrancar(self):
        """Lo que quedó escrito con el vigilante apagado, y la lista de proyectos."""
        leer_lo_nuevo(self.base)
        self.leer_proyectos()

    def observador(self):
        """El `Observer` de `watchdog` sobre la base, ya andando."""
        from watchdog.events import FileSystemEventHandler
        from watchdog.observers import Observer

        vigilante = self

        class Aviso(FileSystemEventHandler):
            def on_modified(self, evento):
                if not evento.is_directory:
                    vigilante.avisar(evento.src_path)

            def on_created(self, evento):
                if not evento.is_directory:
                    vigilante.avisar(evento.src_path)

        observador = Observer()
        observador.schedule(Aviso(), self.base, recursive=True)
        observador.start()
        return observador

    def correr(self, mientras=lambda: True):
        """Vigila hasta que `mientras()` diga que no."""
        self.arrancar()
        observador = self.observador()
        try:
            while mientras():
                time.sleep(CADA)
                self.guardar_lo_cambiado()
        finally:
            observador.stop()
            observador.join(5)
        self.guardar_lo_cambiado()
