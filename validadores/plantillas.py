#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Valida un documento contra la plantilla de la que salió.

La plantilla es la fuente de verdad: NADA se codifica aquí. El validador abre
`plantillas/X.md`, ve qué secciones y qué marcadores tiene, y compara. Si la
plantilla cambia, el validador cambia con ella sin tocar este archivo.

Tres comprobaciones:
  1. Marcadores sin llenar    — FALLA. Quedó texto textual de la plantilla.
  2. Notas de plantilla       — AVISO. Las instrucciones `>` no se borraron.
  3. Secciones ausentes       — AVISO. Las plantillas permiten borrar lo que no
                                aplica, así que no se puede afirmar que falte.
"""
import os
import re

from comun import (AVISO, FALLA, Hallazgo, RAIZ, encabezados, leer,
                   lineas_utiles, marcadores)

# Cómo se deduce la plantilla a partir del H1 del documento.
# El prefijo del ID basta: "HU-014 — Registrar cliente" -> plantillas/HU.md
POR_PREFIJO = {
    "HU-": "plantillas/HU.md",
    "EP-": "plantillas/epica.md",
    "ADR-": "plantillas/ADR.md",
}

# Cuando el ID no dice nada, se deduce por el nombre del archivo.
POR_NOMBRE = {
    "brief": "plantillas/brief.md",
    "dominio": "plantillas/dominio.md",
    "stack": "plantillas/stack.md",
    "fase": "plantillas/fase.md",
    "trabajo": "plantillas/planes/trabajo.md",
    "pruebas": "plantillas/planes/pruebas.md",
    "marco-normativo": "plantillas/marco-normativo.md",
    "mapeo-nombres": "plantillas/mapeo-nombres.md",
    "cierre-analisis": "plantillas/cierre-analisis.md",
    "estado-fase": "plantillas/estado-fase.md",
    # Documentos del proyecto con su nombre real en `documentacion/…`.
    "plan_trabajo": "plantillas/planes/trabajo.md",
    "plan_pruebas": "plantillas/planes/pruebas.md",
    "funcionalidad_implementada": "plantillas/funcionalidad-implementada.md",
    "catalogo-modulos": "plantillas/catalogo-modulos.md",
    "modulos": "plantillas/catalogo-modulos.md",
    "reglas-proyecto": "plantillas/reglas-proyecto.md",
    "mapa-dependencias": "plantillas/mapa-dependencias.md",
    "adr": "plantillas/ADR.md",
}

_H1 = re.compile(r"^#\s+(.*?)\s*$")
_MARCADOR_EN_TITULO = re.compile(r"\[[^\[\]\n]+\](?!\()")


def _ruta(relativa):
    """Las tablas de arriba usan `/`; en Windows hay que normalizar el separador."""
    return os.path.normpath(os.path.join(RAIZ, *relativa.split("/")))


def deducir_plantilla(ruta_documento, texto):
    """Devuelve la ruta de la plantilla correspondiente, o None si no se sabe."""
    for _, linea in lineas_utiles(texto):
        m = _H1.match(linea)
        if m:
            titulo = m.group(1).strip()
            for prefijo, plantilla in POR_PREFIJO.items():
                if titulo.upper().startswith(prefijo):
                    return _ruta(plantilla)
            break

    base = os.path.splitext(os.path.basename(ruta_documento))[0].lower()
    if base in POR_NOMBRE:
        return _ruta(POR_NOMBRE[base])
    return None


def _notas(texto):
    """Líneas de cita `>` — en las plantillas son instrucciones para quien llena."""
    salida = []
    for n, linea in lineas_utiles(texto):
        recortada = linea.strip()
        if recortada.startswith(">"):
            salida.append((n, recortada))
    return salida


def validar(ruta_documento, ruta_plantilla):
    documento = leer(ruta_documento)
    plantilla = leer(ruta_plantilla)
    hallazgos = []

    # 1. Líneas que quedaron TAL CUAL estaban en la plantilla y llevan marcador.
    #
    #    Se compara la línea entera, no el marcador suelto. Comparar marcadores
    #    daba falsos positivos con las etiquetas que el documento conserva a
    #    propósito: la plantilla trae `- [ ] [Backend] …` y el documento escribe
    #    `- [ ] **T1** · [Backend] Interpretación del Markdown` — la tarea está
    #    llena, y `[Backend]` es una etiqueta, no un hueco.
    lineas_plantilla = {l.strip() for _, l in lineas_utiles(plantilla) if l.strip()}
    con_marcador = {n for n, _ in marcadores(documento)}
    for n, linea in lineas_utiles(documento):
        if n in con_marcador and linea.strip() in lineas_plantilla:
            recorte = linea.strip()
            if len(recorte) > 60:
                recorte = recorte[:57] + "..."
            hallazgos.append(Hallazgo(
                FALLA, ruta_documento, n,
                f"línea sin llenar, igual que en la plantilla: {recorte}"))

    # 2. Notas de instrucción que había que borrar al llenar el documento.
    notas_plantilla = {texto for _, texto in _notas(plantilla)}
    for n, texto in _notas(documento):
        if texto in notas_plantilla:
            recorte = texto if len(texto) <= 60 else texto[:57] + "..."
            hallazgos.append(Hallazgo(
                AVISO, ruta_documento, n,
                f"nota de la plantilla sin borrar: {recorte}"))

    # 3. Secciones de la plantilla ausentes en el documento.
    #    AVISO y no FALLA: las plantillas dicen explícitamente "elimine las
    #    secciones que no apliquen", así que ausencia != incumplimiento.
    #    Mientras la norma no declare cuáles son obligatorias, no se puede
    #    afirmar más que esto.
    #    Se saltan los encabezados que llevan un marcador dentro
    #    (`### CA-01 — [Nombre del escenario…]`): son ejemplos, y su nombre
    #    cambia en cada documento, así que compararlos por título no dice nada.
    presentes = {t for _, t in encabezados(documento)}
    for _, titulo in encabezados(plantilla):
        if _MARCADOR_EN_TITULO.search(titulo):
            continue
        if titulo not in presentes:
            hallazgos.append(Hallazgo(
                AVISO, ruta_documento, 0,
                f"sección de la plantilla ausente: «{titulo}» "
                f"— confirma que no aplica"))

    return hallazgos
