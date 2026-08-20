#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganche de Claude Code que reporta el consumo de la sesión.

Se conecta en `.claude/settings.json`, en dos momentos:

    Stop             -> python hook_presupuesto.py --raiz <proyecto> [--umbral <fichas>]
    UserPromptSubmit -> python hook_presupuesto.py --modo aviso --raiz <proyecto> [--umbral <fichas>]

El modo `cierre` (el de siempre, y el que corre sin `--modo`) suma las fichas
de cada turno y deja el total a la vista al terminar la respuesta. El modo
`aviso` (`EP-005 · HU-014`) corre en cada mensaje y habla **solo** si el último
turno cruzó un tramo de consumo, una vez por tramo: el total al cierre llega
cuando ya se pagó; este llega mientras todavía se puede decidir.

Lee la transcripción interna de la herramienta (la ruta llega por la entrada
estándar, en `transcript_path`). La suma y el umbral son de `validadores/presupuesto.py`,
que sirve con cualquier herramienta; **acá vive solo la lectura del formato
de esta**.

Siempre sale con código 0. Un enganche que detiene el trabajo es peor que el
problema que resuelve — y en esta herramienta, salir con 2 bloquea al usuario.
"""
import argparse
import json
import os
import sys

# Vive en el adaptador, no en `validadores/`: por eso dice dónde están los
# módulos agnósticos que usa.
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "validadores"))
import presupuesto                      # noqa: E402
from comun import preparar_salida       # noqa: E402


def consumos_de_transcripcion(ruta):
    """`[{"entrada","salida","cache"}]`, un dict por turno del agente.

    La transcripción es un archivo de líneas JSON; las del agente traen
    `message.usage`. Una línea ilegible se salta: mejor un total corto que
    un enganche caído.
    """
    salida = []
    try:
        with open(ruta, encoding="utf-8", errors="replace") as f:
            lineas = f.readlines()
    except OSError:
        return salida
    for linea in lineas:
        try:
            dato = json.loads(linea)
        except (json.JSONDecodeError, ValueError):
            continue
        uso = ((dato.get("message") or {}).get("usage")
               if isinstance(dato, dict) else None)
        if not isinstance(uso, dict):
            continue
        salida.append({
            "entrada": (uso.get("input_tokens") or 0)
            + (uso.get("cache_creation_input_tokens") or 0),
            "salida": uso.get("output_tokens") or 0,
            "cache": uso.get("cache_read_input_tokens") or 0,
        })
    return salida


def main():
    preparar_salida()
    p = argparse.ArgumentParser()
    p.add_argument("--modo", choices=("cierre", "aviso"), default="cierre")
    p.add_argument("--raiz", default=".")
    p.add_argument("--umbral", type=int, default=None,
                   help="cierre: fichas a partir de las que avisa (0 = solo informa). "
                        "aviso: tamaño del tramo (0 = apagado); por defecto, un millón")
    a = p.parse_args()

    try:
        entrada = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        entrada = {}
    ruta = entrada.get("transcript_path") or ""
    if not ruta or not os.path.isfile(ruta):
        return 0

    consumos = consumos_de_transcripcion(ruta)
    if a.modo == "aviso":
        umbral = presupuesto.TRAMO if a.umbral is None else a.umbral
        cruzo, numero, totales = presupuesto.cruzo_tramo(consumos, umbral)
        if cruzo:
            print(presupuesto.aviso_de_tramo(totales, numero, umbral))
        return 0

    totales = presupuesto.resumen(consumos)
    if totales["turnos"]:
        print(presupuesto.como_texto(totales, a.umbral or 0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
