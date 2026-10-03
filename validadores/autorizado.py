# -*- coding: utf-8 -*-
"""`EP-023·HU-007` · Lo que una regla autoriza escribir sin que un plan lo nombre.

Hay archivos que se escriben siempre: la transcripción, el resumen, el análisis,
los guiones de apoyo. No los autoriza un plan, los autoriza **la regla que los
pide**, y lo dice en una línea que va después de `**Aplica a:**`:

    **Autoriza escribir:** `historico-chat/resumenes/**` · `historico-chat/*.md`

Se lee de las reglas de `base/` del estándar y de las del proyecto, en
`.agente/reglas-proyecto.md` (análisis 1 del pendiente 103, conclusión 46). En
las rutas, `*` vale por un tramo del nombre y `**` por cualquier cantidad de
carpetas. La usan el `pre-commit` (`validar.py plan --preparados`) y, desde la
fase `B` de la HU-007, el freno.

**Solo autoriza la regla vigente** (análisis 11 del pendiente 103, acuerdos 2 y
3). El estado vive en la regla misma: la que sale se deroga y lleva
`[DEROGADA…]` en su título, y la *opt-in* de un capítulo que el proyecto apagó
no rige. Ninguna de las dos autoriza, aunque conserve su línea. Así una regla
entra o sale sin tocar este programa.
"""
import os
import re

import comun
import recuperar

_LINEA = re.compile(r"^(?:-\s*)?\*\*Autoriza escribir:\*\*(.*)$")
_RUTA = re.compile(r"`([^`]+)`")
_TITULO = re.compile(r"^##\s+([A-Z]{1,4}\d+(?:\.\d+)?)\s+·")
_ID_ARCHIVO = re.compile(r"^([A-Z]{1,4}\d+(?:\.\d+)?)-")
_CAPITULO = re.compile(r"^(\d{2})-")
_ID_PROYECTO = re.compile(r"^#{2,4}\s+(P\d+)\b")

REGLAS_PROYECTO = os.path.join(".agente", "reglas-proyecto.md")


def _patron(ruta):
    """La ruta con comodines, como expresión regular de la ruta entera."""
    salida, i = "", 0
    while i < len(ruta):
        if ruta.startswith("**/", i):
            salida += "(?:.*/)?"
            i += 3
        elif ruta.startswith("**", i):
            salida += ".*"
            i += 2
        elif ruta[i] == "*":
            salida += "[^/]*"
            i += 1
        else:
            salida += re.escape(ruta[i])
            i += 1
    return re.compile(salida + r"\Z")


def _id_de(titulo, archivo):
    """La regla dueña de la línea: el título `## ID ·` anterior, o el archivo."""
    if titulo:
        regla = titulo
    else:
        m = _ID_ARCHIVO.match(os.path.basename(archivo))
        regla = m.group(1) if m else os.path.basename(archivo)
    for parte in os.path.relpath(archivo, comun.RAIZ).replace("\\", "/").split("/"):
        c = _CAPITULO.match(parte)
        if c:
            return "%s·%s" % (c.group(1), regla)
    return regla


def _lineas(texto, titulo=_TITULO):
    """`(id, encabezado, rutas)` de cada línea; la de un bloque de código es un ejemplo."""
    ultimo, encabezado = None, ""
    for _, linea in comun.lineas_utiles(texto):
        if linea.startswith("## "):
            encabezado = linea
        t = titulo.match(linea)
        if t:
            ultimo = t.group(1)
        m = _LINEA.match(linea)
        if m:
            rutas = [r.strip().lstrip("./") for r in _RUTA.findall(m.group(1))]
            yield ultimo, encabezado, [r for r in rutas if r]


def vigente(encabezado, capitulo, apagados):
    """¿La regla rige? No si está derogada, ni si es *opt-in* de un capítulo apagado."""
    if "[DEROGADA" in encabezado.upper():
        return False
    return not ("opt-in" in encabezado.lower() and capitulo in apagados)


def de_la_base(estandar=None, proyecto=None):
    """`[(regla, [rutas])]` de toda regla vigente de `base/` que autoriza escribir."""
    base = os.path.join(estandar or comun.RAIZ, "base")
    apagados = recuperar.opt_in_apagados(proyecto) if proyecto else frozenset()
    salida = []
    for actual, carpetas, archivos in os.walk(base):
        # Las reglas por tarea son copias de las del capítulo: se leen una vez.
        carpetas[:] = sorted(c for c in carpetas if c != "reglas-por-tarea")
        for nombre in sorted(archivos):
            if not nombre.endswith(".md"):
                continue
            archivo = os.path.join(actual, nombre)
            texto = comun.leer(archivo)
            for titulo, encabezado, rutas in _lineas(texto):
                regla = _id_de(titulo, archivo)
                if vigente(encabezado, regla.split("·")[0], apagados):
                    salida.append((regla, rutas))
    return salida


def del_proyecto(proyecto):
    """`[(regla, [rutas])]` de las reglas propias del proyecto."""
    archivo = os.path.join(proyecto, REGLAS_PROYECTO)
    if not os.path.isfile(archivo):
        return []
    texto = comun.leer(archivo)
    return [(titulo or "reglas-proyecto", rutas)
            for titulo, _, rutas in _lineas(texto, _ID_PROYECTO)]


def reglas(proyecto, estandar=None):
    """Lo autorizado para ese proyecto: lo de `base/` y lo suyo."""
    return de_la_base(estandar, proyecto) + del_proyecto(proyecto)


def quien_autoriza(ruta, autorizadas):
    """La regla que autoriza escribir esa ruta, o `None`."""
    ruta = ruta.replace("\\", "/").lstrip("./")
    for regla, rutas in autorizadas:
        for r in rutas:
            if _patron(r).match(ruta):
                return regla
    return None


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("plan")
