# -*- coding: utf-8 -*-
"""La evidencia de los CA-03 y CA-04 sobre el historico de verdad.

**CA-04 · indexar no toca el historico.** Se retrata la carpeta archivo por
archivo (nombre, tamano y huella del contenido), se indexa, y se vuelve a
retratar. Comparar los dos retratos es lo unico que prueba que no se toco nada:
mirar la fecha de modificacion no alcanza, porque un programa puede escribir el
mismo contenido y dejarla igual.

**CA-03 · ninguna credencial queda en lo indexado.** Se le pasa a lo indexado el
detector de secretos del estandar, que es el que conoce las formas de clave.
Escribir aca una lista propia daria por limpio lo que esa lista no conozca.

Se corre desde la raiz del repositorio.
"""
import hashlib
import io
import os
import sys
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(RAIZ, "validadores"))
sys.path.insert(0, os.path.join(RAIZ, "plataforma"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
import django                                                    # noqa: E402
django.setup()

from nucleo.medicion import core                                 # noqa: E402
from nucleo.medicion.models import Mensaje, Sesion               # noqa: E402
from nucleo.proyectos.models import Proyecto                     # noqa: E402

import secretos                                                  # noqa: E402


def retrato(carpeta):
    """Nombre, tamano y huella de cada archivo. Lo que cambia, se ve."""
    salida = {}
    for base, _, nombres in os.walk(carpeta):
        for nombre in nombres:
            completa = os.path.join(base, nombre)
            try:
                with io.open(completa, "rb") as abierto:
                    datos = abierto.read()
            except OSError:
                continue
            salida[os.path.relpath(completa, carpeta)] = (
                len(datos), hashlib.sha256(datos).hexdigest())
    return salida


def main():
    proyectos = list(Proyecto.objects.all())
    if not proyectos:
        print("No hay proyectos conectados: no hay que indexar.")
        return 1

    for proyecto in proyectos:
        carpeta = os.path.join(proyecto.ruta_codigo, core.CARPETA)
        if not os.path.isdir(carpeta):
            print("%s: no tiene %s" % (proyecto.nombre, core.CARPETA))
            continue

        print("== %s ==" % proyecto.nombre)
        antes = retrato(carpeta)
        print("  archivos en el historico: %d" % len(antes))

        arranque = time.time()
        cuenta = core.indexar(proyecto)
        tardo = time.time() - arranque

        despues = retrato(carpeta)
        print("  indexado: %d sesion(es), %d mensaje(s), en %.1f s"
              % (cuenta["sesiones"], cuenta["mensajes"], tardo))
        for nombre, motivo in cuenta["ilegibles"]:
            print("    no se pudo leer %s: %s" % (nombre, motivo))

        # CA-04
        cambiados = [n for n in set(antes) | set(despues)
                     if antes.get(n) != despues.get(n)]
        print("  CA-04 · archivos del historico que cambiaron: %d" % len(cambiados))
        for n in cambiados[:5]:
            print("    %s" % n)

    # CA-03: el detector del estandar sobre todo lo indexado.
    print("\n== CA-03 · credenciales en lo indexado ==")
    hallazgos = []
    for mensaje in Mensaje.objects.all().iterator():
        hallazgos.extend(secretos.revisar_texto(
            mensaje.texto, donde="mensaje %d" % mensaje.id))

    print("  mensajes indexados: %d" % Mensaje.objects.count())
    print("  sesiones indexadas: %d" % Sesion.objects.count())
    print("  con forma de credencial: %d" % len(hallazgos))
    return 0


if __name__ == "__main__":
    sys.exit(main())
