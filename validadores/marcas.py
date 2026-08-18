# -*- coding: utf-8 -*-
"""`00·ID8` · Las marcas que delatan generación automática, contadas.

La regla manda escribir sin las marcas de
[`base/00-identidad-y-rol/marcadores-de-ia.md`](../base/00-identidad-y-rol/marcadores-de-ia.md).
El [pendiente 11](../pendientes/11-limpiar-marcadores-de-ia-del-texto-del-estandar.md)
pide **contar antes de tocar**: sin el recuento no se sabe si limpiar el
estándar son dos horas o dos días.

**Solo se cuenta lo mecánico.** El anexo tiene ocho secciones y la mayoría pide
criterio —si la raya larga aparece «muy seguido», si el paralelismo es
«perfecto», si el español «no es de acá»—. Un programa que opinara de eso
llenaría de ruido lo que hoy nadie mira. Acá van las marcas que se cuentan sin
equivocarse, y el anexo mismo dice cuáles son: *«las únicas que un script
cuenta sin equivocarse»*.

**Lo que no se mira:**

- **Dentro de un bloque cercado o de comillas invertidas.** Ahí las marcas son
  ejemplos de lo que no hay que hacer, no marcas.
- **El propio anexo y esta documentación.** Un catálogo de marcas está lleno de
  marcas por definición, y contarlas sería contar el catálogo.
- **`historico-chat/`**, que es transcripción literal de lo que se dijo: no se
  reescribe, así que contarlo con lo demás mezcla deuda con lo que no lo es.
  Se cuenta aparte, para saber cuánto hay.
"""
import argparse
import os
import re
import sys

import comun
from comun import (AVISO, Hallazgo, RAIZ, leer, lineas_utiles, recorrer_md,
                   relativo, reportar, preparar_salida, sin_codigo_en_linea)

# Los archivos que hablan **de** las marcas: contarlas ahí es contar el catálogo.
CATALOGO = (
    "base/00-identidad-y-rol/marcadores-de-ia.md",
    "base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md",
    "validadores/marcas.py",
)

HISTORICO = "historico-chat"

# ── Sección 3 del anexo · las invisibles ──────────────────────────────────
INVISIBLES = {
    " ": "espacio duro (U+00A0)",
    "​": "ancho cero (U+200B)",
    "﻿": "marca de orden de bytes (U+FEFF)",
    "­": "guion suave (U+00AD)",
    "…": "puntos suspensivos en un solo carácter (…)",
    "–": "semiraya (–) donde va un guion",
    " ": "espacio fino (U+2009)",
    " ": "espacio fino sin salto (U+202F)",
}

# ── Sección 2 del anexo · lo que se cuenta sin opinar ─────────────────────
# El punto medio que **no** forma parte de una cita `NN·ID` ni de un `A · B`
# de encabezado: los dos son notación definida del estándar.
_CITA = re.compile(r"\d{2}·[A-Z]")

_RAYA = "—"

# `- **Algo:** ...` — la viñeta que abre con negrita y dos puntos.
_VINETA_NEGRITA = re.compile(r"^\s*[-*+]\s+\*\*[^*]+:\*\*")

# `→` o `✓` abriendo una línea, usados como viñeta.
_FLECHA_VINETA = re.compile(r"^\s*[→✓]\s")

_SEMAFORO = re.compile(r"[\U0001F534\U0001F7E1\U0001F7E2]")

# `## Título:` — dos puntos al final del encabezado.
_ENCABEZADO_DOS_PUNTOS = re.compile(r"^#{1,6}\s+.*:\s*$")

_COMILLA_CURVA = re.compile(r"[“”]")


def _excluido(raiz, archivo):
    rel = os.path.relpath(archivo, raiz).replace("\\", "/")
    return rel in CATALOGO


def _es_historico(raiz, archivo):
    rel = os.path.relpath(archivo, raiz).replace("\\", "/")
    return rel.split("/")[0] == HISTORICO


def marcas_de_linea(linea):
    """Las marcas mecánicas de una línea ya limpia de código. `[(clave, qué)]`."""
    salida = []
    for caracter, nombre in INVISIBLES.items():
        for _ in range(linea.count(caracter)):
            salida.append((caracter, nombre))

    for _ in range(linea.count(_RAYA)):
        salida.append(("raya", "raya larga (—) como inciso"))

    # El punto medio, descontando el de la cita `NN·ID`.
    puntos = linea.count("·") - len(_CITA.findall(linea))
    for _ in range(max(puntos, 0)):
        salida.append(("punto-medio", "punto medio (·) fuera de una cita `NN·ID`"))

    for _ in _COMILLA_CURVA.findall(linea):
        salida.append(("comilla", "comilla curva (“ ”)"))
    if _VINETA_NEGRITA.match(linea):
        salida.append(("vineta", "viñeta que abre con negrita y dos puntos"))
    if _FLECHA_VINETA.match(linea):
        salida.append(("flecha", "flecha o visto usado como viñeta"))
    for _ in _SEMAFORO.findall(linea):
        salida.append(("semaforo", "semáforo (🔴 🟡 🟢) en un documento formal"))
    if _ENCABEZADO_DOS_PUNTOS.match(linea):
        salida.append(("encabezado", "encabezado que termina en dos puntos"))
    return salida


def contar(raiz=None, incluir_historico=False):
    """`{clave: cuántas}` y `{archivo: cuántas}` sobre el árbol.

    Es el paso 1 del pendiente 11 —*contar antes de tocar*— y por eso devuelve
    dos repartos: **por marca**, para saber qué pesa; y **por archivo**, para
    saber por dónde empezar.
    """
    raiz = raiz or RAIZ
    por_marca, por_archivo, nombres = {}, {}, {}

    for archivo in recorrer_md(raiz):
        if _excluido(raiz, archivo):
            continue
        if _es_historico(raiz, archivo) and not incluir_historico:
            continue
        cuantas = 0
        for _n, linea in lineas_utiles(leer(archivo)):
            for clave, nombre in marcas_de_linea(sin_codigo_en_linea(linea)):
                por_marca[clave] = por_marca.get(clave, 0) + 1
                nombres[clave] = nombre
                cuantas += 1
        if cuantas:
            por_archivo[relativo(archivo)] = cuantas
    return por_marca, por_archivo, nombres


def validar(raiz=None):
    """Las marcas de lo que se hereda: `base/` y `plantillas/`.

    **Solo esas dos carpetas**, y es el paso 2 del pendiente: son lo que viaja
    a los proyectos. `notas/`, `analisis/` y el histórico son bitácora y pueden
    esperar — reportarlos hoy sepultaría lo que sí hay que arreglar.
    """
    raiz = raiz or RAIZ
    hallazgos = []
    for archivo in recorrer_md(raiz):
        if _excluido(raiz, archivo):
            continue
        rel = os.path.relpath(archivo, raiz).replace("\\", "/").split("/")[0]
        if rel not in ("base", "plantillas"):
            continue
        for n, linea in lineas_utiles(leer(archivo)):
            vistas = set()
            for clave, nombre in marcas_de_linea(sin_codigo_en_linea(linea)):
                if clave in vistas:
                    continue        # una vez por línea: el conteo va en `contar`
                vistas.add(clave)
                hallazgos.append(Hallazgo(
                    AVISO, archivo, n,
                    f"{nombre} — `00·ID8` pide entregar sin las marcas del anexo"))
    return hallazgos


def main():
    preparar_salida()
    p = argparse.ArgumentParser(
        description="Cuenta las marcas mecánicas de `00·ID8`.")
    p.add_argument("--raiz", default=RAIZ)
    p.add_argument("--historico", action="store_true",
                   help="incluye `historico-chat/`, que no se reescribe")
    p.add_argument("--archivos", type=int, default=15,
                   help="cuántos archivos listar, de mayor a menor")
    a = p.parse_args()

    por_marca, por_archivo, nombres = contar(a.raiz, a.historico)
    total = sum(por_marca.values())
    print(f"== Marcas mecánicas de `00·ID8` ==\n")
    print(f"{total} en {len(por_archivo)} archivos\n")

    print("Por marca:")
    for clave, cuantas in sorted(por_marca.items(), key=lambda x: -x[1]):
        print(f"  {cuantas:>6}  {nombres[clave]}")

    print(f"\nPor archivo, los {a.archivos} primeros:")
    for archivo, cuantas in sorted(por_archivo.items(),
                                   key=lambda x: -x[1])[:a.archivos]:
        print(f"  {cuantas:>6}  {archivo}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
