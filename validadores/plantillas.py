#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Valida un documento contra la plantilla de la que salió.

La plantilla es la fuente de verdad: NADA se codifica aquí. El validador abre
`plantillas/X.md`, ve qué secciones y qué marcadores tiene, y compara. Si la
plantilla cambia, el validador cambia con ella sin tocar este archivo.

Cinco comprobaciones:
  1. Marcadores sin llenar    — FALLA. Quedó texto textual de la plantilla.
  2. Notas de plantilla       — AVISO. Las instrucciones `>` no se borraron.
  3. Secciones ausentes       — AVISO. Las plantillas permiten borrar lo que no
                                aplica, así que no se puede afirmar que falte.
  4. Reglas sin origen        — FALLA, solo en la especificación de módulo.
  5. El bloque fijo perdido   — FALLA. La plantilla pone un texto antes de su
                                primer separador que no es instrucción para
                                borrar sino instrucción de uso, y el documento
                                lo borró o lo reemplazó por otra cosa.
"""
import os
import re

import comun
from comun import (AVISO, FALLA, Hallazgo, RAIZ, encabezados, leer,
                   lineas_utiles, marcadores)

# Cómo se deduce la plantilla a partir del H1 del documento.
# El prefijo del ID basta: "HU-014 — Registrar cliente" -> plantillas/ciclo-vida-proyectos/04-HU.md
POR_PREFIJO = {
    "HU-": "plantillas/ciclo-vida-proyectos/04-HU.md",
    "EP-": "plantillas/ciclo-vida-proyectos/03-epica.md",
    "ADR-": "plantillas/ADR.md",
}

# Cuando el ID no dice nada, se deduce por el nombre del archivo.
POR_NOMBRE = {
    "planteamiento": "plantillas/ciclo-vida-proyectos/01-planteamiento.md",
    "dominio": "plantillas/dominio.md",
    "stack": "plantillas/stack.md",
    "fase": "plantillas/ciclo-vida-proyectos/05-fase.md",
    "trabajo": "plantillas/ciclo-vida-proyectos/07-plan-trabajo.md",
    "pruebas": "plantillas/ciclo-vida-proyectos/08-plan-pruebas.md",
    "marco-normativo": "plantillas/marco-normativo.md",
    "mapeo-nombres": "plantillas/mapeo-nombres.md",
    "cierre-analisis": "plantillas/cierre-analisis.md",
    "estado-fase": "plantillas/ciclo-vida-proyectos/10-estado-fase.md",
    # Documentos del proyecto con su nombre real en `documentacion/…`.
    "plan_trabajo": "plantillas/ciclo-vida-proyectos/07-plan-trabajo.md",
    "plan_pruebas": "plantillas/ciclo-vida-proyectos/08-plan-pruebas.md",
    "funcionalidad_implementada": "plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md",
    "catalogo-modulos": "plantillas/catalogo-modulos.md",
    "modulos": "plantillas/catalogo-modulos.md",
    "reglas-proyecto": "plantillas/reglas-proyecto.md",
    "mapa-dependencias": "plantillas/mapa-dependencias.md",
    "adr": "plantillas/ADR.md",
    "spec": "plantillas/ciclo-vida-proyectos/06-especificacion-modulo.md",
}

# La especificación de módulo, para saber cuándo mirar sus reglas de negocio.
SPEC_MODULO = "plantillas/ciclo-vida-proyectos/06-especificacion-modulo.md"

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

    # El planteamiento con su prefijo: `cimiento-planteamiento.md`. El molde
    # manda nombrarlo así —«copiar como `prompts/<slug>-planteamiento.md`»— y
    # buscando solo el nombre pelado no se resolvía ninguno de los que produce.
    #
    # **Se exige además la carpeta**, y no es celo: el sufijo suelto resuelve
    # mal. Medido sobre el repositorio, aceptar cualquier `*-planteamiento.md`
    # se lleva por delante un pendiente que se llama
    # `el-estandar-tiene-su-planteamiento.md`, y la misma idea aplicada a las
    # demás claves toma cada `resultado_pruebas.md` por un plan de pruebas y
    # cada regla terminada en `-trabajo` por un plan de trabajo: 29 documentos
    # comparados contra el molde que no es.
    carpeta = os.path.basename(os.path.dirname(os.path.abspath(ruta_documento)))
    if carpeta.lower() == "prompts" and base.endswith("-planteamiento"):
        return _ruta(POR_NOMBRE["planteamiento"])
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


# Una fecha completa. En el bloque fijo delata que ahí se contó de dónde salió
# el documento, que es lo que desplazó al encuadre la vez que pasó.
_FECHA = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")

# Donde termina la cabecera de un documento: el primer separador, o el primer
# encabezado de sección si no hay separador.
_FIN_DE_CABECERA = re.compile(r"^(?:-{3,}\s*|##\s+.*)$")


def bloque_fijo(texto):
    """El texto que la plantilla pone antes de su primer separador: `[(línea, texto)]`.

    **No es el recuadro que se borra.** El recuadro son líneas de cita `>` y
    dice cómo llenar el documento; esto es lo que queda debajo, en prosa, y
    dice **cómo se usa** el documento ya llenado. En el molde del planteamiento
    es el encuadre que le recuerda al agente que eso es insumo y no una orden
    de entregar código.

    Se identifica **por posición y no por su etiqueta**. La etiqueta cambia:
    se llamó «Encuadre para el agente» y hoy se llama de otra forma. Un
    validador atado a una redacción reprueba lo que está bien la primera vez
    que alguien corrige el molde, y eso enseña a ignorar los veredictos.
    """
    salida = []
    for n, linea in lineas_utiles(texto):
        recortada = linea.strip()
        if not recortada:
            continue
        if _FIN_DE_CABECERA.match(recortada):
            break
        if recortada.startswith(("#", ">", "|")):
            continue
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

    # 5. El bloque fijo de la plantilla, perdido al llenar el documento.
    #
    #    Ya pasó: el planteamiento de este repositorio se escribió con una nota
    #    de procedencia —fecha, fuentes, el pendiente que cerraba— en el lugar
    #    del encuadre, y el encuadre desapareció. Nadie lo notó hasta que se
    #    preguntó qué aportaba ese párrafo.
    #
    #    **Lo que se exige sale de la plantilla, no de acá.** Si la plantilla no
    #    tiene bloque fijo, no se pide ninguno; si lo tiene pero no cita reglas
    #    —el plan de trabajo es así—, tampoco se le piden citas al documento.
    fijo_plantilla = bloque_fijo(plantilla)
    if fijo_plantilla:
        fijo_documento = bloque_fijo(documento)
        muestra = fijo_plantilla[0][1]
        if len(muestra) > 60:
            muestra = muestra[:57] + "..."
        if not fijo_documento:
            hallazgos.append(Hallazgo(
                FALLA, ruta_documento, 0,
                f"falta el texto que la plantilla fija antes de su primer "
                f"separador: «{muestra}» — no es relleno, es la instrucción "
                f"de uso del documento, y se conserva al llenarlo"))
        elif (any(_FECHA.search(t) for _, t in fijo_documento)
              and not any(_FECHA.search(t) for _, t in fijo_plantilla)):
            hallazgos.append(Hallazgo(
                FALLA, ruta_documento, fijo_documento[0][0],
                f"el texto fijo trae una fecha, y el de la plantilla no: ahí "
                f"se está contando de dónde salió el documento en vez de cómo "
                f"se usa — la procedencia va en la identificación, y ese lugar "
                f"lo ocupa lo que la plantilla pone: «{muestra}»"))

    return hallazgos


if __name__ == "__main__":
    # `53` · Un modulo que se ejecuta solo y no imprime nada dice, con su
    # silencio, lo mismo que diria si hubiera comprobado y estuviera todo bien.
    comun.no_es_punto_de_entrada("plantilla")
