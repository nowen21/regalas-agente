# -*- coding: utf-8 -*-
"""`EP-025·HU-011` · El gasto llega a la base en cuanto Claude Code lo escribe.

Un proceso que queda corriendo (análisis 2 del pendiente 119, acuerdo 1): Windows
avisa cuando cambia un `.jsonl` de `~/.claude/projects/` (`watchdog`) y lo nuevo
se guarda con el mismo lector y el mismo guardado de siempre, que no duplican.

**Sin relojes** (`EP-025·HU-025`, análisis 1 del pendiente 124, acuerdos 4 y 6).
Cada aviso guarda en el acto: el lector solo toma líneas completas y recuerda
hasta dónde leyó, así que varios avisos seguidos no duplican nada. **La lista de
proyectos se relee cuando llega un archivo de una carpeta que no conoce**, y no
cada cierto tiempo. **Al arrancar se lee desde donde quedó cada archivo**: lo
escrito con el vigilante apagado no se pierde. **Espera sin despertar**: se
detiene con `--parar`, que cierra el proceso por su número.

**Guarda su número de proceso** (`04·S10`), para cerrarlo por él con `--parar`.
"""
import os
import threading

from django.db import connections

from core.proyectos.claude import proyectos_de_claude
from core.proyectos.models import Proyecto

from .guardar import GuardadoDeConsumo, leer_lo_nuevo


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
    """Guarda lo nuevo de cada `.jsonl` en el momento en que Windows avisa que cambió."""

    def __init__(self, base=None):
        self.base = os.path.abspath(base or proyectos_de_claude())
        self.candado = threading.Lock()
        self.proyectos = {}
        self.ultimo_error = ""

    def leer_proyectos(self):
        """`{carpeta de Claude Code en minúsculas: proyecto}` de los activos."""
        self.proyectos = {p.carpeta_claude.lower(): p for p in Proyecto.objects.filter(activo=True)}

    def carpeta_de(self, ruta):
        """La primera carpeta bajo la base, en minúsculas, o None si el archivo no está debajo."""
        try:
            relativa = os.path.relpath(os.path.abspath(ruta), self.base)
        except ValueError:
            return None                     # otra unidad
        partes = relativa.split(os.sep)
        if relativa.startswith("..") or len(partes) < 2:
            return None
        return partes[0].lower()

    def proyecto_de(self, ruta):
        """El proyecto activo dueño del `.jsonl`, o None.

        Si la carpeta no está en la lista, la relee en ese momento: así entra el
        proyecto que se registró con el vigilante prendido (acuerdo 6).
        """
        carpeta = self.carpeta_de(ruta)
        if carpeta is None:
            return None
        if carpeta not in self.proyectos:
            self.leer_proyectos()
        return self.proyectos.get(carpeta)

    def avisar(self, ruta):
        """Lo llama `watchdog` cuando algo cambia, y guarda en el acto. `True` si había algo nuevo."""
        if not ruta.endswith(".jsonl"):
            return False
        with self.candado:
            # El proceso vive horas: una conexión que MariaDB ya cerró se cambia por
            # otra. Solo esa: `close_old_connections` cierra también las sanas.
            for conexion in connections.all():
                if conexion.connection is not None and not conexion.is_usable():
                    conexion.close()
            proyecto = self.proyecto_de(ruta)
            if proyecto is None:
                return False
            # Un archivo que falla no tumba al vigilante (`EP-025·HU-015`): su
            # avance no se movió, así que el próximo cambio lo vuelve a intentar.
            try:
                return GuardadoDeConsumo(proyecto, self.base).leer_archivo(os.path.abspath(ruta)) is not None
            except Exception as error:  # noqa: BLE001
                self.ultimo_error = "%s: %s" % (os.path.basename(ruta), error)
                return False

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

    def correr(self, parar=None):
        """Vigila hasta que `parar` (un `threading.Event`) se active; sin él, hasta que
        se cierre el proceso. Espera sin despertar: no hay nada que revisar entre avisos."""
        parar = parar or threading.Event()
        self.arrancar()
        observador = self.observador()
        try:
            parar.wait()
        finally:
            observador.stop()
            observador.join(5)
