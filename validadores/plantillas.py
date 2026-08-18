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

import comun
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
    "planteamiento": "plantillas/planteamiento.md",
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
    "spec": "plantillas/plantilla-spec-modulo.md",
}

# La especificación de módulo, para saber cuándo mirar sus reglas de negocio.
SPEC_MODULO = "plantillas/plantilla-spec-modulo.md"

# `## 4. Reglas de negocio` y el siguiente encabezado del mismo nivel.
_SECCION_REGLAS = re.compile(
    r"^##\s+\d*\.?\s*Reglas de negocio\s*$(.*?)(?=^##\s|\Z)",
    re.M | re.S | re.I)

# Un ítem de la lista numerada del §4.
_REGLA = re.compile(r"^\s*\d+\.\s+(.*\S)\s*$", re.M)

# Un identificador de origen: `RF-13`, `HU-001`, `D-22`, `RN-05`, `CA-01`…
_IDENTIFICADOR = re.compile(r"\b[A-ZÁÉÍÓÚÑ]{1,6}-\d+\b")

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


def reglas_sin_origen(texto, plantilla_texto=""):
    """Las reglas de negocio del §4 que no dicen de dónde bajan: `[(línea, regla)]`.

    Una regla de negocio no se inventa en la especificación de un módulo: baja
    de un requisito, de una historia o de una decisión. Cuando la plantilla
    pedía solo el porqué, una regla con buena justificación y ninguna
    procedencia entraba sin resistencia — y de ahí bajaba sola a decisiones,
    trazabilidad, pruebas y criterios de aceptación (v22.0.0).

    Se busca un identificador (`RF-13`, `HU-001`, `D-22`) y no una frase:
    «lo pidió el cliente» no se puede seguir hasta ninguna parte.

    Lo que sigue igual que en la plantilla no se cuenta: de eso ya se queja la
    comprobación de líneas sin llenar, y reportar dos veces lo mismo enseña a
    ignorar los hallazgos.
    """
    seccion = _SECCION_REGLAS.search(texto)
    if not seccion:
        return []
    del_molde = {m.group(1).strip()
                 for s in _SECCION_REGLAS.finditer(plantilla_texto or "")
                 for m in _REGLA.finditer(s.group(1))}

    sin_origen = []
    for m in _REGLA.finditer(seccion.group(1)):
        regla = m.group(1).strip()
        if regla in del_molde or not regla.strip("«»…. "):
            continue
        if _IDENTIFICADOR.search(regla):
            continue
        linea = texto[:seccion.start(1) + m.start()].count("\n") + 1
        sin_origen.append((linea, regla))
    return sin_origen


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

    # 4. Reglas de negocio sin procedencia, solo en la especificación de módulo.
    #    Un `## 4. Reglas de negocio` en otro documento puede querer decir otra
    #    cosa, así que la comprobación se ata a la plantilla, no al título.
    if os.path.normpath(ruta_plantilla) == _ruta(SPEC_MODULO):
        for linea, regla in reglas_sin_origen(documento, plantilla):
            recorte = regla if len(regla) <= 60 else regla[:57] + "..."
            hallazgos.append(Hallazgo(
                FALLA, ruta_documento, linea,
                f"regla de negocio sin decir de dónde baja: {recorte} "
                f"— falta el identificador del requisito, la historia o la "
                f"decisión; si no lo tiene, la regla se sube a la historia "
                f"que corresponda y baja desde allá"))

    return hallazgos


if __name__ == "__main__":
    # `53` · Un modulo que se ejecuta solo y no imprime nada dice, con su
    # silencio, lo mismo que diria si hubiera comprobado y estuviera todo bien.
    comun.no_es_punto_de_entrada("plantilla")
