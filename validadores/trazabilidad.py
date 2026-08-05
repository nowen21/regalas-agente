#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trazabilidad de la documentación de fases — `02·F4` y `13·DOC`.

Recorre `documentacion/epicas/` (la misma estructura que valida `fases.py`) y
comprueba lo que se puede sin criterio:

  DOC16 — enlace bidireccional: cada HU declara su épica; la épica lista sus HU.
  DOC12 — el `plan_trabajo` de cada fase declara ORIGEN.
  DOC3/DOC11 — la `funcionalidad_implementada` trae la tabla de trazabilidad;
               los ítems ❌ se marcan para que un humano confirme su justificación.

No juzga contenido: solo presencia de campos, cruces de identificadores y señales
estructurales. La norma vive en los `.md`; aquí no se reescribe.

Casi todo es **AVISO**: un documento recién abierto todavía no tiene todo, y un
validador que grita por cada archivo en curso se termina ignorando.
"""
import os
import re

import fases
from comun import AVISO, FALLA, Hallazgo, leer, lineas_utiles

CARPETA = "documentacion/epicas"


def _texto(ruta):
    try:
        return leer(ruta)
    except OSError:
        return ""


def _sin_codigo(texto):
    """El cuerpo sin los bloques ``` — así un ejemplo no cuenta como contenido."""
    return "\n".join(l for _, l in lineas_utiles(texto))


def _menciona(texto, prefijo, numero):
    """¿El texto nombra `EP-2` / `EP-002` / `EP2` (o `HU-…`)? El ancho no importa."""
    return re.search(rf"{prefijo}-?0*{numero}\b", texto) is not None


def validar(proyecto):
    proyecto = os.path.abspath(proyecto)
    raiz = os.path.join(proyecto, *CARPETA.split("/"))
    hallazgos = []

    if not os.path.isdir(raiz):
        return [Hallazgo(FALLA, proyecto, 0, f"no existe `{CARPETA}` (F12.13)")]

    for nombre_epica in fases._subcarpetas(raiz):
        m_ep = fases._EPICA.match(nombre_epica)
        if not m_ep:
            continue                        # el nombre inválido lo reporta fases.py
        ruta_epica = os.path.join(raiz, nombre_epica)
        donde_ep = f"{CARPETA}/{nombre_epica}"
        num_ep = fases._numero(m_ep.group(1))

        doc_epica = ""
        for n in ("epica.md", f"{nombre_epica}.md"):
            p = os.path.join(ruta_epica, n)
            if os.path.isfile(p):
                doc_epica = _sin_codigo(_texto(p))
                break

        for nombre_hu in fases._subcarpetas(ruta_epica):
            m_hu = fases._HU.match(nombre_hu)
            if not m_hu:
                continue                    # dentro de épica solo HU: lo ve fases.py
            ruta_hu = os.path.join(ruta_epica, nombre_hu)
            donde_hu = f"{donde_ep}/{nombre_hu}"
            num_hu = fases._numero(m_hu.group(1))

            # DOC16 · la HU declara su épica.
            doc_hu = _sin_codigo(_texto(os.path.join(ruta_hu, f"{nombre_hu}.md")))
            if doc_hu and not _menciona(doc_hu, "EP", num_ep):
                hallazgos.append(Hallazgo(
                    AVISO, donde_hu, 0,
                    f"la HU no declara su épica EP-{num_ep} (DOC16 · enlace bidireccional)"))

            # DOC16 · la épica lista esta HU.
            if doc_epica and not _menciona(doc_epica, "HU", num_hu):
                hallazgos.append(Hallazgo(
                    AVISO, donde_ep, 0,
                    f"la épica no lista la HU-{num_hu} que cuelga de ella (DOC16)"))

            for nombre_fase in fases._subcarpetas(ruta_hu):
                if not fases._FASE.match(nombre_fase):
                    continue                # nombre de fase inválido: lo ve fases.py
                ruta_fase = os.path.join(ruta_hu, nombre_fase)
                donde_f = f"{donde_hu}/{nombre_fase}"

                # DOC12 · ORIGEN en el plan_trabajo. Mayúscula a propósito: es el
                # nombre del campo; buscar "origen" en minúscula matcharía prosa.
                plan = _texto(os.path.join(ruta_fase, "plan_trabajo.md"))
                if plan and not re.search(r"\bORIGEN\b", plan):
                    hallazgos.append(Hallazgo(
                        AVISO, donde_f, 0,
                        "el plan_trabajo no declara ORIGEN (DOC12)"))

                # DOC3/DOC11 · tabla de trazabilidad en la funcionalidad_implementada.
                fi = _texto(os.path.join(ruta_fase, "funcionalidad_implementada.md"))
                if fi and "|" not in fi:
                    hallazgos.append(Hallazgo(
                        AVISO, donde_f, 0,
                        "la funcionalidad_implementada no trae tabla de trazabilidad (DOC11)"))
                elif "❌" in fi:
                    hallazgos.append(Hallazgo(
                        AVISO, donde_f, 0,
                        "hay ítems ❌ en la trazabilidad — confirmar que estén justificados (DOC11)"))

    return hallazgos
