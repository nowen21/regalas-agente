# -*- coding: utf-8 -*-
"""`EP-025·HU-029` · El vigilante se reinicia solo cuando cambia el código de Cimiento.

Un proceso que vive días se queda con el código con que arrancó: el 2026-10-08 se
encontró uno que llevaba tres días sin guardar las líneas de sesión, porque había
arrancado antes de la `HU-025`. Reiniciarlo a mano no sirve: nadie se entera.

**Sin relojes** (análisis 1 del pendiente 124, acuerdos 4 y 6). El vigilante sabe
que cambió un `.py` porque `watchdog` le avisa, igual que con los `.jsonl`; nada
revisa cada cierto tiempo. Las únicas esperas son dos, y acotadas:

- **La calma**: un cambio de varios archivos produce un solo reinicio, cuando el
  código lleva `CALMA` segundos sin cambiar. Así el nuevo no arranca con un
  archivo a medio escribir.
- **El relevo**: el viejo lanza el nuevo y solo se detiene cuando el nuevo ya
  escribió su número de proceso (`04·S10`). Si no lo escribe en `ESPERA_DEL_NUEVO`
  segundos, el viejo sigue, vuelve a escribir el suyo y anota por qué.

Va aparte de `vigilante.py`, que sigue sin ninguna espera (`test_no_tiene_relojes`).
"""
import os
import subprocess
import sys
import threading
import time

from .vigilante import archivo_del_numero, numero_guardado, proceso_vivo

CIMIENTO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CALMA = 10.0
ESPERA_DEL_NUEVO = 60.0
# Carpetas que no son el código que corre el vigilante.
_FUERA = {".venv", "venv", "__pycache__", "node_modules", ".agente", ".git"}


def es_codigo(ruta, raiz=CIMIENTO):
    """¿Es un `.py` de Cimiento que el vigilante corre? Las pruebas no cuentan."""
    if not (ruta or "").endswith(".py"):
        return False
    try:
        relativa = os.path.relpath(os.path.abspath(ruta), raiz)
    except ValueError:
        return False                        # otra unidad
    partes = relativa.split(os.sep)
    if relativa.startswith("..") or any(p in _FUERA for p in partes):
        return False
    return not partes[-1].startswith(("tests", "test_"))


def orden_del_vigilante():
    """Cómo se arranca otro vigilante: el mismo Python, sin ventana si hay `pythonw`."""
    python = sys.executable
    pythonw = os.path.join(os.path.dirname(python), "pythonw.exe")
    return [pythonw if os.path.isfile(pythonw) else python, os.path.join(CIMIENTO, "manage.py"), "vigilar_consumo"]


class Reinicio:
    """Recibe los avisos de código y, pasada la calma, releva al vigilante."""

    def __init__(self, parar, orden=None, lanzar=subprocess.Popen, archivo=None, numero=None,
                 calma=CALMA, espera=ESPERA_DEL_NUEVO, raiz=CIMIENTO):
        self.parar = parar
        self.raiz = raiz
        self.orden = orden or orden_del_vigilante()
        self.lanzar = lanzar
        self.archivo = archivo or archivo_del_numero()
        self.numero = numero or os.getpid()
        self.calma, self.espera = calma, espera
        self.candado = threading.Lock()
        self.temporizador = None
        self.ultimo_error = ""

    def aviso(self, ruta):
        """Lo llama `watchdog`. `True` si el cambio es de código y quedó un reinicio en espera."""
        if self.parar.is_set() or not es_codigo(ruta, self.raiz):
            return False
        with self.candado:
            if self.temporizador is not None:
                self.temporizador.cancel()
            self.temporizador = threading.Timer(self.calma, self.reiniciar)
            self.temporizador.daemon = True
            self.temporizador.start()
        return True

    def escribir_el_propio(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            f.write(str(self.numero))

    def reiniciar(self):
        """Lanza el nuevo y se detiene cuando el nuevo ya escribió su número. `True` si hubo relevo."""
        if numero_guardado(self.archivo) == self.numero and os.path.isfile(self.archivo):
            os.remove(self.archivo)         # si no, el nuevo vería al viejo vivo y se iría
        banderas = getattr(subprocess, "DETACHED_PROCESS", 0) | getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0)
        try:
            self.lanzar(self.orden, cwd=CIMIENTO, creationflags=banderas, close_fds=True,
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
        except OSError as error:
            self.ultimo_error = "no se pudo arrancar el vigilante nuevo: %s" % error
            self.escribir_el_propio()
            return False
        if self.esperar_al_nuevo():
            self.parar.set()
            return True
        self.ultimo_error = "el vigilante nuevo no arrancó en %d segundos; sigue el de antes" % self.espera
        numero = numero_guardado(self.archivo)
        if not (numero and proceso_vivo(numero)):
            self.escribir_el_propio()
        return False

    def esperar_al_nuevo(self):
        """¿Escribió el nuevo su número, y está vivo? Espera a lo sumo `espera` segundos."""
        limite = time.monotonic() + self.espera
        while time.monotonic() < limite:
            numero = numero_guardado(self.archivo)
            if numero and numero != self.numero and proceso_vivo(numero):
                return True
            if self.parar.wait(0.5):
                return False
        return False
