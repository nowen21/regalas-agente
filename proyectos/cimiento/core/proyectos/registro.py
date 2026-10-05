# -*- coding: utf-8 -*-
"""Lo que entra al registro de proyectos desde afuera de las pantallas.

- **Traer** los proyectos que ya estaban anotados en `plantillas/proyectos.md`,
  la lista local que el instalador llena en cada máquina. Lo usa la migración
  `0002`, para que la base nueva arranque con los proyectos que existen.
- **Registrar** uno solo: la puerta del instalador (`manage.py registrar`).

`proyectos.md` sigue siendo una lista aparte: el instalador y los avisos de
cierre la leen, y lleva columnas (memoria, stack) que el registro no guarda.
"""
import io
import os
import re
import tempfile

from .claude import carpeta_de_claude

_FILA = re.compile(r"^\|\s*(?P<nombre>[^|]+?)\s*\|\s*`?(?P<ruta>[^|`]+?)`?\s*\|")


def proyectos_md():
    """`plantillas/proyectos.md` del estándar en el que está Cimiento."""
    estandar = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))))
    return os.path.join(estandar, "plantillas", "proyectos.md")


def filas_de_proyectos_md(ruta_md):
    """`(nombre, ruta)` de cada fila de la tabla de `proyectos.md`."""
    if not os.path.isfile(ruta_md):
        return []
    filas = []
    for linea in io.open(ruta_md, encoding="utf-8"):
        m = _FILA.match(linea.strip())
        if not m:
            continue
        nombre, ruta = m.group("nombre").strip(), m.group("ruta").strip()
        if nombre == "Proyecto" or set(nombre) <= {"-"} or not ruta:
            continue
        filas.append((nombre, ruta))
    return filas


def _temporal(ruta):
    temporal = os.path.normcase(os.path.realpath(tempfile.gettempdir())) + os.sep
    return os.path.normcase(os.path.realpath(ruta)).startswith(temporal)


def traer_de_proyectos_md(modelo, ruta_md):
    """Crea en el registro los proyectos de `proyectos.md` que falten.

    Se salta la carpeta que no existe en esta máquina, la temporal (es de una
    prueba) y la que ya está, con cualquier mayúscula. Devuelve los nombres
    creados. `modelo` puede ser el histórico de una migración: por eso la
    carpeta de Claude Code se calcula acá y no en `save`.
    """
    creados = []
    for nombre, ruta in filas_de_proyectos_md(ruta_md):
        ruta = os.path.abspath(ruta)
        nombre = nombre[:100]
        if not os.path.isdir(ruta) or _temporal(ruta):
            continue
        if modelo.objects.filter(ruta__iexact=ruta).exists() or \
                modelo.objects.filter(nombre=nombre).exists():
            continue
        modelo.objects.create(nombre=nombre, ruta=ruta, carpeta_claude=carpeta_de_claude(ruta))
        creados.append(nombre)
    return creados


def registrar(modelo, nombre, ruta):
    """Alta de un proyecto desde el instalador. `True` si se creó.

    Si la carpeta ya está registrada, con cualquier mayúscula, no se toca: el
    nombre y los límites pudieron editarse en la pantalla. Si el nombre ya lo
    usa otra carpeta, se le suma un número.
    """
    ruta = os.path.abspath(ruta)
    if modelo.objects.filter(ruta__iexact=ruta).exists():
        return False
    base, libre, n = nombre[:95], nombre[:100], 2
    while modelo.objects.filter(nombre=libre).exists():
        libre = f"{base} ({n})"
        n += 1
    modelo.objects.create(nombre=libre, ruta=ruta, carpeta_claude=carpeta_de_claude(ruta))
    return True
