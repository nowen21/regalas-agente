# -*- coding: utf-8 -*-
"""`EP-005 · HU-011` · El mapa del amarre no envejece en silencio.

**Qué contesta.** Si mañana el usuario trabaja con otro agente, ¿qué se queda y
qué hay que rehacer? La respuesta vive en
[`anatomia/que-esta-amarrado-a-la-herramienta.md`](../anatomia/que-esta-amarrado-a-la-herramienta.md),
y este programa comprueba que siga siendo cierta.

**Por qué hace falta comprobarlo.** El mapa se escribe a mano, y **todo mapa
escrito a mano envejece en silencio**: un archivo nuevo bajo `validadores/` no
aparece ahí hasta que alguien se acuerde.

**Se mira por los dos lados**, y el segundo no lo pedía la historia:

1. La pieza que **existe y el mapa no nombra**.
2. La pieza que **el mapa nombra y ya no existe** — arreglar solo el primero
   deja la mitad del problema.

**Lo que no comprueba, y se declara.** Si la clasificación es la **correcta**.
Que `pruebas.py` sea «pruebas *de* los adaptadores» y no adaptador es un juicio,
y se lee. Acá se comprueba que **esté clasificada**.
"""
import os
import re

import comun
from comun import AVISO, FALLA, Hallazgo, leer

MAPA = os.path.join("anatomia", "que-esta-amarrado-a-la-herramienta.md")

# La **misma** lista con que se escribió el mapa. Si acá dijera otra cosa, el
# programa y el mapa medirían distinto y nadie lo notaría — es el riesgo `R-01`
# del plan, y hay un caso que compara los dos recuentos.
MARCA = re.compile(
    r"\.claude\b|CLAUDE\.md|settings\.json|hook[s]?_|PostToolUse|UserPromptSubmit|"
    r"SessionStart|\bStop\b|claude_code|CLAUDE_", re.I)

# Este archivo nombra la herramienta porque **la mide**. Exceptuarlo por nombre,
# como los datos de prueba del detector de secretos: lo que existe para hablar
# de algo no es una instancia de ese algo.
EXENTOS = ("amarre.py",)


def piezas(raiz=None):
    """`{nombre: cuántas marcas}` de cada programa de `validadores/`."""
    raiz = raiz or comun.RAIZ
    carpeta = os.path.join(raiz, "validadores")
    if not os.path.isdir(carpeta):
        return {}
    salida = {}
    for nombre in sorted(os.listdir(carpeta)):
        if not nombre.endswith(".py") or nombre in EXENTOS:
            continue
        try:
            salida[nombre] = len(MARCA.findall(leer(os.path.join(carpeta, nombre))))
        except OSError:
            continue
    return salida


def _mapa(raiz):
    archivo = os.path.join(raiz or comun.RAIZ, *MAPA.split(os.sep))
    return archivo, (leer(archivo) if os.path.isfile(archivo) else "")


def validar(raiz=None):
    """Las dos formas de envejecer, y el desacuerdo entre el mapa y la medición."""
    raiz = raiz or comun.RAIZ
    archivo, texto = _mapa(raiz)
    if not texto:
        return [Hallazgo(FALLA, archivo, 0,
                         "falta el mapa del amarre — sin él nadie sabe qué se "
                         "cae si mañana el agente es otro")]

    hallazgos = []
    encontradas = piezas(raiz)

    # 1 · La que existe y el mapa no nombra.
    for nombre in sorted(encontradas):
        if nombre not in texto and nombre[:-3] not in texto:
            hallazgos.append(Hallazgo(
                FALLA, archivo, 0,
                f"`{nombre}` no está en el mapa — nadie sabe si se queda o hay "
                f"que rehacerla el día que cambie el agente"))

    # 2 · La que el mapa nombra y ya no existe. **No lo pedía la historia**,
    # y sin esto el mapa envejece igual, solo que por el otro lado: promete
    # clasificar algo que no está.
    for citada in sorted(set(re.findall(r"`([a-z_]+\.py)`", texto))):
        if citada not in encontradas and citada not in EXENTOS:
            hallazgos.append(Hallazgo(
                AVISO, archivo, 0,
                f"el mapa nombra `{citada}`, que ya no existe — se movió o se "
                f"borró, y el mapa promete clasificar algo que no está"))

    return hallazgos


def linea_resumen(raiz=None):
    """El recuento, para poder compararlo con lo que el mapa dice."""
    encontradas = piezas(raiz)
    if not encontradas:
        return ""
    amarradas = sum(1 for n in encontradas.values() if n > 0)
    return ("Piezas de `validadores/`: %d · amarradas a la herramienta: %d · "
            "libres: %d" % (len(encontradas), amarradas,
                            len(encontradas) - amarradas))


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("amarre")
