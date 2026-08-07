#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Carga las reglas base en el contexto del agente al abrir la sesión.

**Por qué existe:** el `CLAUDE.md` manda, en el paso 1 del arranque, cargar
todas las reglas de `base/`. Pero leer un archivo es una acción que el agente
decide tomar — y cuando no la tomaba, la sesión avanzaba sin reglas y no
quedaba señal de nada. Mismo problema que resolvió `sesion.py` con C18: pasar
de una promesa a un hecho. Aquí las reglas llegan al contexto sin depender del
criterio del agente.

**Por qué no se inyecta todo.** Los archivos completos son ~162 KB (~46k
tokens, casi una cuarta parte de la ventana de contexto) y la mitad de ese peso
—`02-flujo-de-trabajo/` y `13-documentacion.md`— son reglas temáticas que
solo aplican cuando se toca el tema. Peor: llenar la ventana adelanta el
resumen automático del contexto, y lo primero que se resume es justo lo que se
inyectó al arrancar. Se pagaría el precio completo por una garantía que caduca.

Así que va **literal** lo que manda en todos los turnos sin importar el tema
(`00-*` y `01-*`) y del resto solo el **índice**, con la orden de leer el
archivo completo antes de tocar su tema.
"""
import os

from comun import EXCLUIDAS, leer, lineas_utiles

# Prefijos que van literales: gobiernan todos los turnos, no un tema concreto.
# Por prefijo y no por lista fija, para que un `01-` nuevo del estándar entre
# solo, sin tocar este archivo.
#
# Se mira el **primer tramo** de la ruta, no el nombre del archivo: un capítulo
# puede vivir en un archivo suelto (`00-nucleo-blindado.md`) o en su carpeta
# (`00-identidad-y-rol/base.md`). Mirando el nombre, el segundo caería al
# índice y el agente arrancaría sin su identidad.
NUCLEO = ("00-", "01-")

# El gate de arranque. Vive en una subcarpeta, así que un glob plano sobre
# `base/*.md` no lo ve.
GATE = "02-flujo-de-trabajo/reglas/F13-detente-si-el-proyecto-no-tiene-su-estructura-base.md"


def reglas(base):
    """Todos los `.md` bajo `base/`, en orden de precedencia.

    El orden alfabético de la ruta relativa ya es el de precedencia: `00`
    antes que `01`, y el índice de un capítulo (`02-flujo-de-trabajo/base.md`)
    antes que sus reglas (`02-flujo-de-trabajo/reglas/…`). No hay que ordenar
    por nada más.
    """
    salida = []
    for carpeta, subcarpetas, archivos in os.walk(base):
        subcarpetas[:] = [s for s in subcarpetas if s not in EXCLUIDAS]
        for nombre in archivos:
            if nombre.lower().endswith(".md"):
                ruta = os.path.join(carpeta, nombre)
                rel = os.path.relpath(ruta, base).replace("\\", "/")
                salida.append((rel, ruta))
    return sorted(salida)


def _titulo(texto):
    """El H1 del documento — describe el archivo mejor que cualquier resumen.

    Se saca del propio archivo y no de una tabla escrita a mano para que el
    índice no envejezca: si el estándar renombra una regla, el índice cambia
    solo.

    Un archivo que contiene **una sola regla** no lleva H1: su encabezado es el
    de la regla (`## M4 · …`), porque el molde de `M5` empieza en `##`. Para
    esos, el título es ese encabezado — si no, el índice los listaría a todos
    como "(sin título)" y no diría nada.
    """
    respaldo = None
    for _, linea in lineas_utiles(texto):
        if linea.startswith("# "):
            return linea[2:].strip()
        if respaldo is None and linea.startswith("## "):
            respaldo = linea[3:].strip()
    return respaldo or "(sin título)"


def _kb(texto):
    return max(1, round(len(texto.encode("utf-8")) / 1024))


def _solo_gate(base, reglas_encontradas):
    """`F13` no pasa: se carga el gate y nada más.

    Cargar las reglas de trabajo aquí sería contradictorio — invitaría a
    trabajar sobre una estructura que el propio estándar manda detener.
    """
    for rel, ruta in reglas_encontradas:
        if rel == GATE:
            return (
                "[ARRANQUE DETENIDO — EL GATE 02·F13 NO PASA]\n"
                "No continuar con nada: ni crear el espacio, ni adecuar el "
                "proyecto por iniciativa propia. Mostrar la orientación de "
                "F13 que sigue y detenerse.\n\n"
                f"<<< base/{rel} >>>\n{leer(ruta)}")
    return ""


def contexto(estandar, gate_ok=True):
    """El texto que se le inyecta al agente. Cadena vacía si no hay nada que dar."""
    base = os.path.join(estandar, "base")
    if not os.path.isdir(base):
        return ""

    encontradas = reglas(base)
    if not encontradas:
        return ""

    if not gate_ok:
        return _solo_gate(base, encontradas)

    literal, indice = [], []
    for rel, ruta in encontradas:
        texto = leer(ruta)
        if rel.split("/")[0].startswith(NUCLEO):
            literal.append(f"<<< base/{rel} >>>\n{texto}")
        else:
            indice.append(f"  base/{rel}  ({_kb(texto)} KB) — {_titulo(texto)}")

    partes = [
        "[REGLAS BASE DEL ESTÁNDAR — CARGADAS, OBLIGATORIAS]",
        "Rigen esta sesión completa. Ante cualquier choque gana el núcleo.",
        "",
        "\n\n".join(literal),
    ]

    if indice:
        partes += [
            "",
            "[EL RESTO DE LAS REGLAS — NO ESTÁN CARGADAS, SOLO EL ÍNDICE]",
            "Antes de tocar cualquiera de estos temas, leer el archivo "
            "completo con Read. No trabajar el tema de memoria ni suponer qué "
            "dice la regla: el índice dice de qué trata cada archivo, no qué "
            "manda.",
            "",
            "\n".join(indice),
        ]

    return "\n".join(partes)
