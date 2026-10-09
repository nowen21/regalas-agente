# -*- coding: utf-8 -*-
"""`EP-029·HU-002` · En qué lenguaje está hecho un proyecto, por sus archivos.

**Lo reconoce Cimiento, el proyecto no lo declara** (análisis 1 del pendiente
141, acuerdo 1). Se busca hasta tres carpetas adentro, porque los proyectos que
administra Cimiento suelen tener su programa en `proyectos/<nombre>/`. Se saltan
las carpetas de dependencias, que traen archivos de otros proyectos.

El orden importa: `manage.py` va antes que `requirements.txt`, porque un
proyecto Django también tiene `requirements.txt`.
"""
import os
from collections import namedtuple

Lenguaje = namedtuple("Lenguaje", "nombre carpeta")

DJANGO, LARAVEL, ANGULAR, PYTHON = "Django", "Laravel", "Angular", "Python"
PROFUNDIDAD = 3
SE_SALTAN = {".git", ".venv", "venv", "node_modules", "vendor", "__pycache__", "dist", "build", "_archivo"}

# (lenguaje, archivos que tienen que estar juntos en la misma carpeta)
SENALES = [
    (DJANGO, ("manage.py",)),
    (LARAVEL, ("artisan", "composer.json")),
    (ANGULAR, ("angular.json",)),
    (PYTHON, ("pyproject.toml",)),
    (PYTHON, ("setup.py",)),
    (PYTHON, ("requirements.txt",)),
]


def _carpetas(raiz):
    """La raíz y sus subcarpetas hasta `PROFUNDIDAD`, de la más cercana a la más honda."""
    nivel = [raiz]
    for _ in range(PROFUNDIDAD + 1):
        siguiente = []
        for carpeta in nivel:
            yield carpeta
            try:
                hijas = sorted(e.path for e in os.scandir(carpeta)
                               if e.is_dir() and e.name not in SE_SALTAN and not e.name.startswith("."))
            except OSError:
                hijas = []
            siguiente.extend(hijas)
        nivel = siguiente


def reconocer(raiz):
    """El `Lenguaje` del proyecto en `raiz`, o `None` si no lo reconoce."""
    if not raiz or not os.path.isdir(raiz):
        return None
    carpetas = list(_carpetas(raiz))
    for nombre, archivos in SENALES:
        for carpeta in carpetas:
            if all(os.path.isfile(os.path.join(carpeta, a)) for a in archivos):
                return Lenguaje(nombre, carpeta)
    return None


# Un programa de estos no tiene otro adentro: su `requirements.txt` o su
# `package.json` son suyos (`EP-029·HU-007`).
CONTIENEN = {DJANGO, LARAVEL, ANGULAR}


def reconocer_todos(raiz):
    """`EP-029·HU-007` · Todos los programas del proyecto en `raiz`, de afuera hacia
    adentro (análisis 4 del pendiente 141, acuerdo 2): un frente y un servidor son dos."""
    if not raiz or not os.path.isdir(raiz):
        return []
    encontrados = []
    for carpeta in _carpetas(raiz):
        if any(l.nombre in CONTIENEN and (carpeta == l.carpeta or carpeta.startswith(l.carpeta + os.sep))
               for l in encontrados):
            continue
        for nombre, archivos in SENALES:
            if all(os.path.isfile(os.path.join(carpeta, a)) for a in archivos):
                encontrados.append(Lenguaje(nombre, carpeta))
                break
    return encontrados


def python_del_proyecto(*carpetas):
    """El Python del proyecto (`.venv` o `venv`) en la primera carpeta que lo tenga, o `None`.

    Lo usan la revisión (`EP-029·HU-002`) y el instalador (`EP-029·HU-003`): las
    pruebas del proyecto necesitan sus propias dependencias.
    """
    for carpeta in carpetas:
        for entorno in (".venv", "venv"):
            for partes in (("Scripts", "python.exe"), ("bin", "python")):
                ruta = os.path.join(carpeta, entorno, *partes)
                if os.path.isfile(ruta):
                    return ruta
    return None
