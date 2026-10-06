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
cuando ya se pagó; este llega mientras todavía se puede decidir. También avisa
el enganche o el archivo del turno anterior que pasó el límite de su proyecto
(`EP-025·HU-009`).

Lee la transcripción interna de la herramienta (la ruta llega por la entrada
estándar, en `transcript_path`). La suma y el umbral son de `proyectos/cimiento/core/enganches/presupuesto.py`,
que sirve con cualquier herramienta; la lectura del formato de esta vive en
`proyectos/cimiento/core/consumo/lector.py` (`EP-025·HU-006`), que también
guarda el gasto en la base de Cimiento.

Siempre sale con código 0. Un enganche que detiene el trabajo es peor que el
problema que resuelve — y en esta herramienta, salir con 2 bloquea al usuario.
"""
import argparse
import json
import os
import sys

# Vive en el adaptador, no en `core/`: por eso dice dónde están los módulos
# agnósticos que usa.
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "proyectos", "cimiento"))

from core.comun.consola import entrada_json, preparar_salida     # noqa: E402
from core.consumo.lector import LectorDeClaudeCode               # noqa: E402
from core.enganches.presupuesto import Presupuesto               # noqa: E402
from core.enganches.presupuesto import aviso_de_limites as aviso_de_limites_en_core  # noqa: E402


def consumos_de_transcripcion(ruta):
    """`[{"entrada","salida","cache"}]`, un dict por turno del agente.

    La transcripción es un archivo de líneas JSON; las del agente traen
    `message.usage`. Una línea ilegible se salta: mejor un total corto que
    un enganche caído.
    """
    # `EP-025·HU-006` · El formato lo lee `LectorDeClaudeCode`, que cuenta una vez
    # cada llamada aunque ocupe varias líneas: sumar por línea contaba cada una
    # unas tres veces (sesión `c3d82767`, 2026-10-05).
    return [llamada.como_consumo() for llamada in LectorDeClaudeCode(ruta).leer().llamadas]


def aviso_de_limites(ruta, raiz):
    """El aviso por límite vive en `core/enganches/presupuesto.py` (`EP-025·HU-013`)."""
    return aviso_de_limites_en_core(ruta, raiz, RAIZ)


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
        entrada = entrada_json()
    except (json.JSONDecodeError, ValueError):
        entrada = {}
    ruta = entrada.get("transcript_path") or ""
    if not ruta or not os.path.isfile(ruta):
        return 0

    consumos = consumos_de_transcripcion(ruta)
    if a.modo == "aviso":
        umbral = Presupuesto.TRAMO if a.umbral is None else a.umbral
        cruzo, numero, totales = Presupuesto.cruzo_tramo(consumos, umbral)
        if cruzo:
            print(Presupuesto.aviso_de_tramo(totales, numero, umbral))
        try:
            limites = aviso_de_limites(ruta, a.raiz)
        except Exception:  # noqa: BLE001  Un aviso que falla no puede tumbar el mensaje.
            limites = ""
        if limites:
            print(limites)
        return 0

    totales = Presupuesto.resumen(consumos)
    if totales["turnos"]:
        print(Presupuesto.como_texto(totales, a.umbral or 0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
