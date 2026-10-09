# -*- coding: utf-8 -*-
"""`manage.py vigilar_consumo`: guarda el gasto en cuanto Claude Code lo escribe (`EP-025·HU-011`).

    python manage.py vigilar_consumo            queda corriendo
    python manage.py vigilar_consumo --parar    lo detiene por su número de proceso

La instalación del estándar lo arranca al iniciar sesión. Si ya hay uno
corriendo, no arranca otro. Cuando cambia el código de Cimiento, arranca uno
nuevo y se va (`EP-025·HU-029`).
"""
import os
import signal
import sys

from django.core.management.base import BaseCommand, OutputWrapper

from core.comun.consola import preparar_salida

from ...vigilante import VigilanteDeConsumo, archivo_del_numero, numero_guardado, proceso_vivo


def parar(archivo=None):
    """Detiene el vigilante guardado y borra su número. Devuelve el texto de lo que pasó."""
    archivo = archivo or archivo_del_numero()
    numero = numero_guardado(archivo)
    if proceso_vivo(numero):
        os.kill(numero, signal.SIGTERM)
        texto = "detenido el vigilante del consumo (proceso %d)" % numero
    else:
        texto = "el vigilante del consumo no estaba corriendo"
    if os.path.isfile(archivo):
        os.remove(archivo)
    return texto


def sin_consola(comando=None):
    """`EP-025·HU-029` · Arrancado con `pythonw` desde el inicio de sesión no hay consola:
    `sys.stdout` es `None` y el primer mensaje tumbaba al vigilante justo después de
    escribir su número. Sin consola, lo que diga se va a `os.devnull`."""
    for nombre in ("stdout", "stderr"):
        if getattr(sys, nombre) is None:
            setattr(sys, nombre, open(os.devnull, "w", encoding="utf-8"))
    if comando is not None:
        comando.stdout, comando.stderr = OutputWrapper(sys.stdout), OutputWrapper(sys.stderr)


class Command(BaseCommand):
    help = "Guarda el gasto de los .jsonl de los proyectos activos en cuanto cambian."

    def add_arguments(self, parser):
        parser.add_argument("--parar", action="store_true", help="detiene el que está corriendo")

    def handle(self, *args, **opciones):
        if self.stdout._out is None or sys.stdout is None:
            sin_consola(self)       # el `OutputWrapper` se armó antes, con `None`
        preparar_salida()
        archivo = archivo_del_numero()
        if opciones["parar"]:
            self.stdout.write(parar(archivo))
            return
        numero = numero_guardado(archivo)
        if numero != os.getpid() and proceso_vivo(numero):
            self.stdout.write("ya corre un vigilante del consumo (proceso %d)" % numero)
            return
        os.makedirs(os.path.dirname(archivo), exist_ok=True)
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(str(os.getpid()))
        self.stdout.write("vigilando el consumo (proceso %d); se detiene con --parar" % os.getpid())
        try:
            VigilanteDeConsumo(reiniciar_solo=True).correr()
        except KeyboardInterrupt:
            pass
        finally:
            if numero_guardado(archivo) == os.getpid():
                os.remove(archivo)
