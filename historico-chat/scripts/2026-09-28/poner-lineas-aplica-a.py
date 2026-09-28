# -*- coding: utf-8 -*-
"""Pone la línea `**Aplica a:**` en cada regla, desde `clasificacion-de-tareas.tsv`.

Fase `B` de `EP-005·HU-023`, tarea T-06. La tabla la llenó el agente leyendo cada
regla; este guion solo la escribe. No se vuelve a correr: si se corre otra vez
no duplica, porque salta las reglas que ya declaran sus tareas.

**Dónde va la línea.** Después del cuerpo y del ejemplo, antes de lo que cierra
la regla: el separador `---`, un subtítulo (`###` o `##`) o la regla siguiente.
Lo que está dentro de un bloque de código no cuenta, porque ahí un `---` es
parte del ejemplo.
"""
import collections
import io
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "validadores"))

import mapa_tareas   # noqa: E402
import metareglas    # noqa: E402


def tabla():
    salida = {}
    with io.open(os.path.join(AQUI, "clasificacion-de-tareas.tsv"), encoding="utf-8") as f:
        for linea in f:
            if linea.strip():
                id, tareas = linea.rstrip("\n").split("\t")
                salida[id.strip()] = tareas.strip()
    return salida


def _punto(lineas, desde, hasta):
    """El índice antes del cual va la línea, dentro de `[desde, hasta)`."""
    en_bloque = False
    for j in range(desde, hasta):
        s = lineas[j].strip()
        if s.startswith("```") or s.startswith("~~~"):
            en_bloque = not en_bloque
            continue
        if en_bloque:
            continue
        if s == "---" or s.startswith("## ") or s.startswith("### "):
            return j
    j = hasta
    while j > desde and not lineas[j - 1].strip():
        j -= 1
    return j


def main():
    decididas = tabla()
    lista = set(mapa_tareas.tareas(RAIZ))
    por_archivo = collections.defaultdict(list)
    for r in metareglas.reglas(RAIZ):
        if r.derogada or mapa_tareas.declaradas(r):
            continue
        if r.id not in decididas:
            sys.exit("falta en la tabla: %s·%s" % (r.capitulo, r.id))
        for t in decididas[r.id].split(","):
            if t.strip() not in lista:
                sys.exit("%s nombra una tarea que no está en la lista: %s" % (r.id, t))
        por_archivo[r.archivo].append(r)

    puestas = 0
    for archivo, reglas in por_archivo.items():
        with io.open(archivo, encoding="utf-8", newline="") as f:
            crudo = f.read()
        salto = "\r\n" if "\r\n" in crudo else "\n"
        lineas = crudo.split(salto)
        # Todos los encabezados de regla del archivo, vigentes o no, para saber
        # dónde termina cada una.
        todas = [r for r in metareglas.reglas(RAIZ) if r.archivo == archivo]
        inicios = sorted(lineas.index(r.encabezado) for r in todas)
        # De abajo hacia arriba, para que insertar no corra los índices.
        for r in sorted(reglas, key=lambda x: -lineas.index(x.encabezado)):
            ini = lineas.index(r.encabezado)
            siguientes = [i for i in inicios if i > ini]
            fin = siguientes[0] if siguientes else len(lineas)
            j = _punto(lineas, ini + 1, fin)
            nueva = "**Aplica a:** " + ", ".join(
                t.strip() for t in decididas[r.id].split(","))
            bloque = [nueva, ""] if (j > 0 and not lineas[j - 1].strip()) else ["", nueva, ""]
            lineas[j:j] = bloque
            puestas += 1
        with io.open(archivo, "w", encoding="utf-8", newline="") as f:
            f.write(salto.join(lineas))
    print("líneas puestas:", puestas)


if __name__ == "__main__":
    main()
