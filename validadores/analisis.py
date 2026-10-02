# -*- coding: utf-8 -*-
"""`EP-023 · HU-001 · CA-06` · Un análisis aprobado trae sus cuatro partes.

**Qué comprueba.** Todo `analisis-N.md` que ya tiene la marca «Aprobado» lleva
una sección por cada parte que no habla en la conversación: Cimiento, el
proyecto, lo aprendido y el entorno (análisis 1 del pendiente 103, conclusión
40). Si falta una, el análisis se cerró sin revisar esa parte, y es por esa
brecha por donde salen los hallazgos al ejecutar el plan.

**Lo que no mira, y se declara.**

- El análisis abierto: todavía se está llenando, y exigirle las secciones antes
  de tiempo sería una alarma falsa.
- El análisis de `analisis/` con la forma vieja: se llama distinto y queda como
  está (análisis 1, conclusión 38).
- Si lo escrito en cada sección es acertado: eso es un juicio y se lee.
"""
import os
import re

import comun
from comun import FALLA, Hallazgo, leer

# Las cuatro partes, por el comienzo del título de su sección.
PARTES = ("Cimiento", "El proyecto", "Lo aprendido", "El entorno")

_ARCHIVO = re.compile(r"^analisis-\d+\.md$")
_APROBADO = re.compile(r"^> \*\*Aprobado\*\*", re.M)

# Lo que no es del repositorio: local, generado o de terceros.
FUERA = {".git", ".venv", "venv", "__pycache__", "node_modules", "terceros"}


def analisis(raiz=None):
    """Las rutas de todos los `analisis-N.md` del repositorio."""
    raiz = raiz or comun.RAIZ
    salida = []
    for carpeta, subcarpetas, archivos in os.walk(raiz):
        subcarpetas[:] = [s for s in subcarpetas if s not in FUERA]
        for nombre in archivos:
            if _ARCHIVO.match(nombre):
                salida.append(os.path.join(carpeta, nombre))
    return sorted(salida)


def faltantes(texto):
    """Las partes que no tienen su sección `### ` en el análisis."""
    return [p for p in PARTES
            if not re.search(r"^### %s\b" % re.escape(p), texto, re.M)]


def revisar(raiz=None):
    """Una línea por cada parte que le falta a un análisis aprobado."""
    raiz = raiz or comun.RAIZ
    salida = []
    for ruta in analisis(raiz):
        texto = leer(ruta)
        if not _APROBADO.search(texto):
            continue
        for parte in faltantes(texto):
            salida.append(f"{os.path.relpath(ruta, raiz)}: falta la sección «{parte}»")
    return salida


def validar(raiz=None):
    """Lo mismo que `revisar`, en la forma que reporta `validar.py`."""
    raiz = raiz or comun.RAIZ
    hallazgos = []
    for linea in revisar(raiz):
        ruta, mensaje = linea.split(": ", 1)
        hallazgos.append(Hallazgo(
            FALLA, os.path.join(raiz, ruta), 0,
            f"{mensaje}: el análisis se aprobó sin revisar esa parte"))
    return hallazgos


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("analisis")
