# -*- coding: utf-8 -*-
"""`09·12` · Crea el esqueleto de una fase: carpeta, documentos y consecutivo.

**Hoy esto se hace a mano y es donde se cometen los errores** que `fases.py` y
`trazabilidad.py` detectan después: el consecutivo repetido, el nombre que no
sigue el molde, el enlace que falta en uno de los dos lados. La estructura se
corrige en vez de nacer bien.

**Genera el esqueleto y nada de contenido**, que es la advertencia que trae el
propio pendiente y la más importante de todas:

> *Un generador que además rellena texto produce documentos que pasan el
> validador sin decir nada, que es la peor combinación posible.*

Por eso los marcadores `«…»` de las plantillas **se dejan intactos**: lo único
que se sustituye es lo estructural —identificadores, rutas, enlaces—, que es
justamente lo que un programa puede saber y una persona escribe mal.

**El consecutivo se calcula leyendo lo que hay**, no se pide: es lo mismo que
`fases.py` ya sabe hacer para comprobarlo, usado al revés.

**Se corre solo, no por `validar.py`**, y la separación es la de siempre en esta
casa: `validar.py` es la puerta de lo que **comprueba**; esto **escribe**, como
`cerrar.py` o `historico.py`.

    python validadores/andamio.py EP-001-… HU-003-… descripcion-de-la-fase
"""
import os
import re

import comun
from comun import leer

CARPETA = os.path.join("documentacion", "epicas")

# Los cinco documentos de una fase (`02·F12.13`) y la plantilla de cada uno.
DOCUMENTOS = [
    ("plan_trabajo.md", os.path.join("plantillas", "planes", "trabajo.md")),
    ("plan_pruebas.md", os.path.join("plantillas", "planes", "pruebas.md")),
    ("resultado_pruebas.md", os.path.join("plantillas", "planes", "resultados.md")),
    ("estado-fase.md", os.path.join("plantillas", "estado-fase.md")),
    ("funcionalidad_implementada.md",
     os.path.join("plantillas", "funcionalidad-implementada.md")),
]

_CONSECUTIVO = re.compile(r"^([A-Z]{1,3})(?:-[A-Z]{1,3})?-EP-")


def _letras(n):
    """`1 → A`, `26 → Z`, `27 → AA`. El consecutivo de `02·F12.5`."""
    salida = ""
    while n > 0:
        n, resto = divmod(n - 1, 26)
        salida = chr(ord("A") + resto) + salida
    return salida


def siguiente_consecutivo(carpeta_hu):
    """La letra que le toca a la próxima fase de esa HU.

    **Se lee lo que hay en vez de contar cuántas hay**: si existen `A` y `C`
    porque la `B` se renombró, contar daría `C` y pisaría una fase viva.
    """
    usadas = set()
    if os.path.isdir(carpeta_hu):
        for nombre in os.listdir(carpeta_hu):
            m = _CONSECUTIVO.match(nombre)
            if m and os.path.isdir(os.path.join(carpeta_hu, nombre)):
                usadas.add(m.group(1))
    n = 1
    while _letras(n) in usadas:
        n += 1
    return _letras(n)


def _sustituciones(consecutivo, epica, hu, descripcion, nombre_fase):
    """Solo lo **estructural**. Los `«…»` de contenido no se tocan."""
    return {
        "«CONSECUTIVO»": consecutivo,
        "«EPICA»": epica,
        "«HU»": hu,
        "«FASE»": nombre_fase,
        "«DESCRIPCION-FASE»": descripcion,
    }


def crear(raiz, epica, hu, descripcion, escribir=False):
    """Crea la fase y devuelve `(ruta, [archivos])`. Sin `escribir`, simula.

    `epica` y `hu` van como los nombres de sus carpetas — `EP-001-…`, `HU-003-…`.
    """
    raiz = os.path.abspath(raiz)
    carpeta_hu = os.path.join(raiz, CARPETA, epica, hu)
    if not os.path.isdir(carpeta_hu):
        raise ValueError("no existe la HU: %s" % os.path.join(CARPETA, epica, hu))

    num_ep = re.match(r"^EP-(\d+)", epica)
    num_hu = re.match(r"^HU-(\d+)", hu)
    if not num_ep or not num_hu:
        raise ValueError("la épica o la HU no siguen el molde de `02·F12`")

    consecutivo = siguiente_consecutivo(carpeta_hu)
    nombre = "%s-EP-%s-HU-%s-%s" % (consecutivo, num_ep.group(1),
                                    num_hu.group(1), descripcion)
    destino = os.path.join(carpeta_hu, nombre)

    subs = _sustituciones(consecutivo, epica, hu, descripcion, nombre)
    escritos = []
    for archivo, plantilla in DOCUMENTOS:
        origen = os.path.join(raiz, plantilla)
        if not os.path.isfile(origen):
            continue
        texto = leer(origen)
        for viejo, nuevo in subs.items():
            texto = texto.replace(viejo, nuevo)
        escritos.append(archivo)
        if escribir:
            os.makedirs(destino, exist_ok=True)
            with open(os.path.join(destino, archivo), "w",
                      encoding="utf-8", newline="\n") as f:
                f.write(texto)
    return destino, escritos


def main():
    """`09·12` · el andamio se pide, no se ejecuta solo."""
    import argparse
    p = argparse.ArgumentParser(
        description="Crea el esqueleto de una fase: carpeta, documentos y consecutivo. "
                    "No escribe contenido: los marcadores «…» quedan para llenarse.")
    p.add_argument("epica", help="carpeta de la épica, p. ej. EP-001-cuerpo-de-reglas")
    p.add_argument("hu", help="carpeta de la HU, p. ej. HU-003-nucleo")
    p.add_argument("descripcion", help="qué hace la fase, en minúsculas con guiones")
    p.add_argument("--raiz", default=comun.RAIZ)
    p.add_argument("--aplicar", action="store_true",
                   help="escribe de verdad; sin esto solo dice qué crearía")
    a = p.parse_args()

    destino, escritos = crear(a.raiz, a.epica, a.hu, a.descripcion, a.aplicar)
    marca = "creada" if a.aplicar else "simulado; agrega --aplicar"
    print("%s  (%s)" % (comun.relativo(destino), marca))
    for e in escritos:
        print("  · %s" % e)
    print("\nLos marcadores «…» quedan sin llenar a propósito: el andamio no "
          "escribe contenido.")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
