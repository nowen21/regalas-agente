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


# **Las dos carpetas donde puede haber código, y por eso son dos.**
#
# El 2026-08-19 los ocho enganches se mudaron a `adaptadores/claude-code/`.
# Mirar solo `validadores/` habría dejado el amarre **fuera del recuento** justo
# después de reúnirlo: el mapa habría dicho «diez amarrados de 51» y sonaría a
# mejora, cuando lo que pasó fue una mudanza.
#
# Y hacia adelante importa más: un adaptador nuevo que nadie mire vuelve a ser
# el problema que este mapa vino a resolver.
CARPETAS = (os.path.join("validadores"),
            os.path.join("adaptadores", "claude-code"))


def piezas(raiz=None):
    """`{nombre: cuántas marcas}` de cada programa, en las dos carpetas."""
    raiz = raiz or comun.RAIZ
    salida = {}
    for rel in CARPETAS:
        carpeta = os.path.join(raiz, rel)
        if not os.path.isdir(carpeta):
            continue
        for nombre in sorted(os.listdir(carpeta)):
            if not nombre.endswith(".py") or nombre in EXENTOS:
                continue
            try:
                salida[nombre] = len(MARCA.findall(
                    leer(os.path.join(carpeta, nombre))))
            except OSError:
                continue
    return salida


# `EP-005·HU-023` · Una línea que no dice nada más que nombres: la lista de las
# piezas libres, `` `acciones.py` · `aislamiento.py` · … ``.
_SOLO_NOMBRES = re.compile(r"^(`[\w.]+`[\s·,.]*)+$")


def _clasificacion(texto):
    """Solo las líneas que clasifican: filas de tabla y listas de nombres.

    **Por qué no todo el texto** (`EP-005·HU-023`, CA-06). Antes bastaba con que
    el nombre apareciera en cualquier parte, y una frase que decía «estas dos
    piezas siguen sin clasificar», nombrándolas, las daba por clasificadas: el
    validador pasó de dos fallas a verde con el mapa incompleto. Nombrar una pieza
    en una frase no dice en qué columna va; una fila de tabla o la lista de
    libres, sí.
    """
    return "\n".join(l.strip() for l in texto.splitlines()
                     if l.strip().startswith("|") or _SOLO_NOMBRES.match(l.strip()))


def _clasificada(nombre, clasificacion):
    """Si la pieza aparece, entre comillas invertidas, en una línea que clasifica.

    Los enganches van a veces sin la extensión (`` `hook_resumen` ``), y por eso
    se acepta el nombre con `.py` o sin él.
    """
    base = re.escape(nombre[:-3])
    return re.search(r"`%s(\.py)?`" % base, clasificacion) is not None


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
    clasificacion = _clasificacion(texto)

    # 1 · La que existe y el mapa no clasifica.
    for nombre in sorted(encontradas):
        if not _clasificada(nombre, clasificacion):
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
