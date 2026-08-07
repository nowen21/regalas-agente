#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El plan y los padres de cada fase — `02·F14`, `02·F17` y `02·F0`.

Recorre `documentacion/epicas/…/<fase>/` (la misma estructura que `fases.py`) y
comprueba sin criterio:

  F0   · cada fase tiene sus **padres**: la épica y la HU de las que cuelga
         existen como documento (no solo como carpeta).
  F14 · el plan responde las 13 preguntas obligatorias. La plantilla las numera
         como secciones `## 0.` … `## 13.`; se marca cuáles faltan.
  F17 · el plan no deja **incertidumbre** sin resolver: `TBD`, `(o similar)`,
         `(o donde esté)`, `(o parecido)`. La línea base debe ir verificada.

No juzga el contenido de cada sección (eso es humano); solo presencia y marcas de
duda. **AVISO**: un plan en curso puede estar incompleto a propósito.

Nota: los planes que **preceden** a esta plantilla marcarán secciones faltantes.
Es correcto —no conforman a F14—, no un falso positivo.
"""
import os
import re

import fases
from comun import AVISO, FALLA, Hallazgo, leer

CARPETA = "documentacion/epicas"

# F14 · las secciones que la plantilla numera 0..13 (una por bloque de preguntas).
_SECCIONES = list(range(0, 14))
_ENCABEZADO = re.compile(r"(?m)^#{1,4}\s*(\d{1,2})\.")

# F17 · marcas de que la línea base no se verificó.
_INCERTIDUMBRE = re.compile(
    r"(?i)\bTBD\b|\bpor\s+definir\b|\(o\s+(similar|donde\s+est[eé]|parecid[oa]|equivalente)\)")


def _texto(ruta):
    try:
        return leer(ruta)
    except OSError:
        return ""


def revisar_plan(texto):
    """Núcleo puro: (faltan_secciones, incertidumbres) de un plan_trabajo.
    `faltan_secciones` es la lista de números F14 ausentes; `incertidumbres`
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
        # F0 · la épica existe como documento, no solo como carpeta.
        tiene_doc_epica = any(
            os.path.isfile(os.path.join(ruta_epica, n))
            for n in ("epica.md", f"{nombre_epica}.md"))
        epica_con_fases = False
        for nombre_hu in fases._subcarpetas(ruta_epica):
            ruta_hu = os.path.join(ruta_epica, nombre_hu)
            tiene_fases = bool(fases._subcarpetas(ruta_hu))
            epica_con_fases = epica_con_fases or tiene_fases
            # F0 · la HU existe como documento.
            if tiene_fases and not os.path.isfile(os.path.join(ruta_hu, f"{nombre_hu}.md")):
                hallazgos.append(Hallazgo(
                    AVISO, f"{CARPETA}/{nombre_epica}/{nombre_hu}", 0,
                    "hay fases pero la HU no tiene su documento (F0: falta el padre)"))
            for nombre_fase in fases._subcarpetas(ruta_hu):
                plan = os.path.join(ruta_hu, nombre_fase, "plan_trabajo.md")
                if not os.path.isfile(plan):
                    continue
                donde = f"{CARPETA}/{nombre_epica}/{nombre_hu}/{nombre_fase}/plan_trabajo.md"
                faltan, incertidumbres = revisar_plan(_texto(plan))
                if faltan:
                    hallazgos.append(Hallazgo(
                        AVISO, donde, 0,
                        "al plan le faltan secciones de las 13 preguntas (F14): "
                        + ", ".join(map(str, faltan))))
                for linea, frag in incertidumbres:
                    hallazgos.append(Hallazgo(
                        AVISO, donde, linea,
                        f"marca de incertidumbre `{frag}` en el plan — F17 pide "
                        f"la línea base verificada"))
        if epica_con_fases and not tiene_doc_epica:
            hallazgos.append(Hallazgo(
                AVISO, f"{CARPETA}/{nombre_epica}", 0,
                "hay fases pero la épica no tiene su documento (F0: falta el padre)"))
    return hallazgos
