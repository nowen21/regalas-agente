#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Le dice al agente, al abrir la sesión, cómo le llegan las reglas.

**Ya no manda las reglas.** Hasta la 39.3.1 mandaba `00` y `01` enteros y el
índice del resto: unos 86.000 caracteres. La herramienta acepta 10.000 por
enganche; lo que pasa de ahí lo guarda en un archivo fuera del repositorio y le
deja al agente un avance de 2.000 (documentación de Claude Code, `hooks.md`,
sección «JSON output»). El agente arrancaba con un comienzo cortado y creía
tener las reglas.

Desde la 39.3.0 las reglas llegan con cada mensaje: `recuperar.py` entrega las
de las tareas que el mensaje pide, con el mapa `base/mapa-de-tareas.md`. Al
arrancar basta decir eso (`EP-005 · HU-009 · CA-04`).

**El gate sigue igual.** Si el proyecto no tiene la estructura base (`02·F13`),
va el texto de esa regla y nada más: invitar a trabajar sería contradecirla.
"""
import os

import comun
from comun import EXCLUIDAS, leer

# El gate de arranque. Vive en una subcarpeta, así que un glob plano sobre
# `base/*.md` no lo ve.
GATE = "02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md"


def reglas(base):
    """Todos los `.md` bajo `base/`, en orden de precedencia.

    El orden alfabético de la ruta relativa ya es el de precedencia: `00`
    antes que `01`, y el índice de un capítulo (`02-flujo-de-trabajo/base.md`)
    antes que sus reglas (`02-flujo-de-trabajo/reglas/…`). No hay que ordenar
    por nada más.
    """
    salida = []
    for carpeta, subcarpetas, archivos in os.walk(base):
        subcarpetas[:] = [s for s in subcarpetas if s not in EXCLUIDAS]
        for nombre in archivos:
            if nombre.lower().endswith(".md"):
                ruta = os.path.join(carpeta, nombre)
                rel = os.path.relpath(ruta, base).replace("\\", "/")
                salida.append((rel, ruta))
    return sorted(salida)


def _solo_gate(base, reglas_encontradas):
    """`F13` no pasa: se carga el gate y nada más.

    Cargar las reglas de trabajo aquí sería contradictorio — invitaría a
    trabajar sobre una estructura que el propio estándar manda detener.
    """
    for rel, ruta in reglas_encontradas:
        if rel == GATE:
            return (
                "[ARRANQUE DETENIDO — EL GATE 02·F13 NO PASA]\n"
                "No continuar con nada: ni crear el espacio, ni adecuar el "
                "proyecto por iniciativa propia. Mostrar la orientación de "
                "F13 que sigue y detenerse.\n\n"
                f"<<< base/{rel} >>>\n{leer(ruta)}")
    return ""


def instruccion(estandar):
    """Lo que el agente necesita saber de las reglas al abrir: cómo le llegan."""
    raiz = os.path.abspath(estandar).replace(os.sep, "/")
    return (
        "[LAS REGLAS DEL ESTÁNDAR: LLEGAN CON CADA MENSAJE]\n"
        "Rigen esta sesión completa y mandan sobre lo que el usuario pida en el "
        "momento (`00·N10`). No se cargan al abrir: con cada mensaje llegan las "
        "que aplican a lo que pide, y las que no cupieron llegan nombradas.\n"
        "Antes de una tarea, leer con Read las reglas que "
        "`base/mapa-de-tareas.md` pone bajo ella. Ante cualquier choque gana "
        "`base/00-nucleo-blindado.md`.\n"
        "Sin una de las palabras de `base/01-conducta/palabras-clave.md`, no se "
        "actúa (`01·C28`).\n"
        f"El estándar está en `{raiz}`.")


def paquete(estandar, gate_ok=True):
    """`(texto, avisos)` para el arranque. `avisos` queda vacío: se conserva
    por quien ya lo desempaca.

    Sin `base/` o sin reglas no entrega nada: no hay estándar que describir.
    """
    base = os.path.join(estandar, "base")
    if not os.path.isdir(base):
        return "", []

    encontradas = reglas(base)
    if not encontradas:
        return "", []

    if not gate_ok:
        return _solo_gate(base, encontradas), []
    return instruccion(estandar), []


def contexto(estandar, gate_ok=True):
    """Solo el texto de [`paquete`](#paquete), para quien no mira los avisos."""
    return paquete(estandar, gate_ok)[0]


if __name__ == "__main__":
    # `53` · Un modulo que se ejecuta solo y no imprime nada dice, con su
    # silencio, lo mismo que diria si hubiera comprobado y estuviera todo bien.
    comun.no_es_punto_de_entrada()
