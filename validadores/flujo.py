#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El plan de trabajo de cada fase — `02·F4.1` y `02·F4.3`.

Recorre `documentacion/epicas/…/<fase>/plan_trabajo.md` (la misma estructura que
`fases.py`) y comprueba dos cosas del plan sin criterio:

  F4.1 · el plan responde las 13 preguntas obligatorias. La plantilla las numera
         como secciones `## 0.` … `## 13.`; se marca cuáles faltan.
  F4.3 · el plan no deja **incertidumbre** sin resolver: `TBD`, `(o similar)`,
         `(o donde esté)`, `(o parecido)`. La línea base debe ir verificada.

No juzga el contenido de cada sección (eso es humano); solo su presencia y las
marcas de duda. **AVISO**: un plan en curso puede estar incompleto a propósito.

Nota: los planes que **preceden** a esta plantilla marcarán secciones faltantes.
Es correcto —no conforman a F4.1—, no un falso positivo.
"""
import os
import re

import fases
from comun import AVISO, FALLA, Hallazgo, leer

CARPETA = "documentacion/epicas"

# F4.1 · las secciones que la plantilla numera 0..13 (una por bloque de preguntas).
_SECCIONES = list(range(0, 14))
_ENCABEZADO = re.compile(r"(?m)^#{1,4}\s*(\d{1,2})\.")

# F4.3 · marcas de que la línea base no se verificó.
_INCERTIDUMBRE = re.compile(
    r"(?i)\bTBD\b|\bpor\s+definir\b|\(o\s+(similar|donde\s+est[eé]|parecid[oa]|equivalente)\)")


def _texto(ruta):
    try:
        return leer(ruta)
    except OSError:
        return ""


def revisar_plan(texto):
    """Núcleo puro: (faltan_secciones, incertidumbres) de un plan_trabajo.
    `faltan_secciones` es la lista de números F4.1 ausentes; `incertidumbres`
    es la lista de (linea, fragmento). Aislado de git."""
    presentes = {int(n) for n in _ENCABEZADO.findall(texto)}
    faltan = [n for n in _SECCIONES if n not in presentes]

    incertidumbres = []
    for i, linea in enumerate(texto.splitlines(), 1):
        m = _INCERTIDUMBRE.search(linea)
        if m:
            incertidumbres.append((i, m.group(0)))
    return faltan, incertidumbres


def validar(proyecto):
    proyecto = os.path.abspath(proyecto)
    raiz = os.path.join(proyecto, *CARPETA.split("/"))
    if not os.path.isdir(raiz):
        return [Hallazgo(FALLA, proyecto, 0, f"no existe `{CARPETA}` (F12.13)")]

    hallazgos = []
    for nombre_epica in fases._subcarpetas(raiz):
        ruta_epica = os.path.join(raiz, nombre_epica)
        for nombre_hu in fases._subcarpetas(ruta_epica):
            ruta_hu = os.path.join(ruta_epica, nombre_hu)
            for nombre_fase in fases._subcarpetas(ruta_hu):
                plan = os.path.join(ruta_hu, nombre_fase, "plan_trabajo.md")
                if not os.path.isfile(plan):
                    continue
                donde = f"{CARPETA}/{nombre_epica}/{nombre_hu}/{nombre_fase}/plan_trabajo.md"
                faltan, incertidumbres = revisar_plan(_texto(plan))
                if faltan:
                    hallazgos.append(Hallazgo(
                        AVISO, donde, 0,
                        "al plan le faltan secciones de las 13 preguntas (F4.1): "
                        + ", ".join(map(str, faltan))))
                for linea, frag in incertidumbres:
                    hallazgos.append(Hallazgo(
                        AVISO, donde, linea,
                        f"marca de incertidumbre `{frag}` en el plan — F4.3 pide "
                        f"la línea base verificada"))
    return hallazgos
