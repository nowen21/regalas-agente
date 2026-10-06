# -*- coding: utf-8 -*-
"""`EP-025·HU-017` · Un guion de apoyo que repite lo que Cimiento ya hace, o a otro guion.

**Lo que se repite es una funcionalidad de Cimiento, no un guion** (análisis 2
del pendiente 119, acuerdo 6). El 2026-10-05 se escribieron cinco guiones casi
iguales para cerrar fases y otro para separar los cambios por sesión; desde la
`EP-025·HU-016` eso lo hacen `cerrar_fase` y `cambios_por_sesion`.

- **Lo que Cimiento hace** se reconoce por lo que el guion toca: los archivos y
  carpetas que solo toca esa tarea. El freno lo detiene y nombra la orden.
- **Lo parecido** a un guion anterior de `historico-chat/scripts/` (el mismo
  nombre sin sus números, o casi el mismo texto) se avisa: la tarea se repite y
  va como funcionalidad. No se detiene: puede ser algo nuevo que se parece.
"""
import difflib
import os
import re

CARPETA = "historico-chat/scripts/"

# (qué hace, la orden que lo hace, las señales en el texto del guion)
FUNCIONALIDADES = [
    ("cerrar o reabrir una fase", "manage.py cerrar_fase «fase» (o reabrir_fase)",
     re.compile(r"estado-fase\.md|resultado_pruebas\.md|funcionalidad_implementada\.md")),
    ("separar los cambios de cada sesión", "manage.py cambios_por_sesion",
     re.compile(r"\.tocado\b|cambios_de_la_sesion")),
    ("crear o quitar una HU, una fase o un pendiente", "python validadores/andamio.py (hu, pendiente o quitar)",
     re.compile(r"ciclo-vida-proyectos[/\\]+0[47]-|plantillas[/\\]+pendiente\.md")),
    ("cerrar o reabrir un pendiente", "python validadores/cerrar.py (o cerrar.py reabrir)",
     re.compile(r"pendientes[/\\]+hecho")),
    ("instalar o desinstalar el estándar", "python validadores/instalar.py (o --desinstalar)",
     re.compile(r"\.githooks|core\.hooksPath")),
    ("leer el gasto de tokens", "manage.py vigilar_consumo (o leer_consumo)",
     re.compile(r"\.claude[/\\]+projects|\bmessage\.usage\b|cache_read_input_tokens")),
]

PARECIDO = 0.7      # parte del texto igual desde la que dos guiones son la misma tarea
TOPE = 200_000      # un guion más grande no se compara: no es un guion de apoyo


def es_guion(rel):
    return (rel or "").startswith(CARPETA) and rel.endswith(".py")


def lo_hace_cimiento(texto):
    """`(qué hace, orden)` si el texto hace algo que Cimiento ya hace, o None."""
    for que, orden, senal in FUNCIONALIDADES:
        if senal.search(texto or ""):
            return que, orden
    return None


def _raiz_del_nombre(nombre):
    return re.sub(r"[\d_-]+", "", os.path.splitext(nombre)[0]).lower()


def parecido_a(raiz, rel, texto):
    """El guion anterior al que se parece el nuevo (`rel`, con `/`), o ""."""
    carpeta = os.path.join(raiz, *CARPETA.rstrip("/").split("/"))
    if not os.path.isdir(carpeta):
        return ""
    propio = os.path.normcase(os.path.join(raiz, *rel.split("/")))
    nombre = _raiz_del_nombre(os.path.basename(rel))
    candidatos = []
    for dia in sorted(os.listdir(carpeta)):
        dentro = os.path.join(carpeta, dia)
        if not os.path.isdir(dentro):
            continue
        for otro in sorted(os.listdir(dentro)):
            ruta = os.path.join(dentro, otro)
            if otro.endswith(".py") and os.path.normcase(ruta) != propio:
                candidatos.append((ruta, CARPETA + dia + "/" + otro))
    for ruta, mostrado in candidatos:
        if nombre and _raiz_del_nombre(os.path.basename(ruta)) == nombre:
            return mostrado
    if not texto or len(texto) > TOPE:
        return ""
    for ruta, mostrado in candidatos:
        try:
            if os.path.getsize(ruta) > TOPE:
                continue
            with open(ruta, encoding="utf-8", errors="replace") as f:
                anterior = f.read()
        except OSError:
            continue
        comparar = difflib.SequenceMatcher(None, anterior, texto, autojunk=False)
        if comparar.real_quick_ratio() >= PARECIDO and comparar.quick_ratio() >= PARECIDO \
                and comparar.ratio() >= PARECIDO:
            return mostrado
    return ""
