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
—`02-flujo-de-trabajo/` y `13-documentacion/`— son reglas temáticas que
solo aplican cuando se toca el tema. Peor: llenar la ventana adelanta el
resumen automático del contexto, y lo primero que se resume es justo lo que se
inyectó al arrancar. Se pagaría el precio completo por una garantía que caduca.

Así que va **literal** lo que manda en todos los turnos sin importar el tema
(`00-*` y `01-*`) y del resto solo el **índice**, con la orden de leer el
archivo completo antes de tocar su tema.

**Y tiene que caber en el canal.** El adaptador que transporta esto tiene un
límite de tamaño, y pasarse no recorta: **tira el paquete entero**. Medido el
2026-09-15 en `master-ciberseguridad`: 82,4 KB de paquete, el canal cortó, la
herramienta lo guardó en un archivo, y el agente trabajó una sesión completa
sin reglas mientras el banner decía «Estándar cargado». **El fallo se vio como
éxito**, que es la peor forma de fallar.

Por eso [`paquete`](#paquete) recibe el tope del canal y recorta en un orden
fijo —primero colapsa el índice, después lo quita, y las reglas nunca— y
devuelve por escrito qué tuvo que dejar afuera. Quien conoce el tope es el
adaptador; acá solo se obedece.
"""
import os
import re

import comun
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
GATE = "02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md"


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


# El `---` no siempre precede al sello: en cinco reglas del núcleo no está.
# Anclar a él dejaba 21 KB adentro, y el recorte parecía hecho.
_SELLO = re.compile("(?ms)^(?:---\s*\n+)?### Checklist.*?(?=^## |\Z)")


def _sin_sellos(texto):
    """El texto de las reglas sin sus bloques de checklist.

    **El sello no le sirve al agente para obedecer**: es el registro de que
    alguien revisó la regla contra el molde, y le sirve a quien mantiene el
    estándar. Inyectarlo cuesta y no aporta.

    Medido el 2026-08-19, cuando el arranque pasó del techo que su propia
    prueba vigila: de los **122,6 KB** que se inyectaban, **70 eran sellos** —
    el 57 %. El texto de las reglas, que es lo único que hay que obedecer,
    cabía en 52.

    **Lo destapó la prueba, no la lectura.** El techo estaba puesto desde la
    fase que midió el arranque, y saltó al partir las reglas del núcleo.
    """
    return _SELLO.sub("", texto).rstrip() + chr(10)


def _por_capitulo(entradas):
    """El índice colapsado a un renglón por capítulo.

    **Existe porque el índice detallado no siempre cabe.** Medido el
    2026-09-15: el paquete del arranque pesaba 82,4 KB y **15,6 eran este
    índice**, archivo por archivo. El canal por donde viaja corta antes de eso,
    así que el índice detallado se llevaba puestas **las reglas**, que son lo
    único que no se puede recortar.

    Colapsado no se pierde el camino: cada capítulo tiene su propio índice
    adentro (`base.md` lista sus reglas), así que el agente llega igual, con
    una lectura más.
    """
    capitulos = {}
    for rel, kb, titulo in entradas:
        capitulo = rel.split("/")[0]
        cuenta, peso, cabeza = capitulos.get(capitulo, (0, 0, ""))
        # El título del capítulo es el de su `base.md` o el del archivo suelto.
        if rel in (f"{capitulo}/base.md", capitulo):
            cabeza = titulo
        capitulos[capitulo] = (cuenta + 1, peso + kb, cabeza)

    lineas = []
    for capitulo in sorted(capitulos):
        cuenta, peso, cabeza = capitulos[capitulo]
        donde = capitulo if capitulo.endswith(".md") else f"{capitulo}/"
        cuantos = "" if cuenta == 1 else f", {cuenta} archivos"
        lineas.append(f"  base/{donde}  ({peso} KB{cuantos})"
                      + (f" — {cabeza}" if cabeza else ""))
    return lineas


def paquete(estandar, gate_ok=True, tope=None):
    """El texto para el agente y los avisos de lo que no cupo.

    Devuelve `(texto, avisos)`. `avisos` va vacío cuando entró todo.

    **`tope` es del canal, no de las reglas.** Lo pone quien conoce el límite
    del adaptador —la herramienta que va a transportar esto—, porque el
    cargador no tiene cómo saberlo. Sin `tope` no se recorta nada, que es el
    comportamiento de siempre.

    **El orden del recorte no es negociable:** primero se colapsa el índice,
    después se quita; **las reglas literales no se tocan nunca**. Un paquete
    sin índice deja al agente con las reglas que rigen todos los turnos y sin
    el mapa del resto; un paquete sin reglas lo deja creyendo que las tiene,
    que es lo que pasó el 2026-09-15.
    """
    base = os.path.join(estandar, "base")
    if not os.path.isdir(base):
        return "", []

    encontradas = reglas(base)
    if not encontradas:
        return "", []

    if not gate_ok:
        return _solo_gate(base, encontradas), []

    literal, entradas = [], []
    for rel, ruta in encontradas:
        texto = _sin_sellos(leer(ruta))
        if rel.split("/")[0].startswith(NUCLEO):
            literal.append(f"<<< base/{rel} >>>\n{texto}")
        else:
            entradas.append((rel, _kb(texto), _titulo(texto)))

    cabeza = [
        "[REGLAS BASE DEL ESTÁNDAR — CARGADAS, OBLIGATORIAS]",
        "Rigen esta sesión completa. Ante cualquier choque gana el núcleo.",
        "",
        "\n\n".join(literal),
    ]

    def _armar(lineas):
        if not lineas:
            return "\n".join(cabeza)
        return "\n".join(cabeza + [
            "",
            "[EL RESTO DE LAS REGLAS — NO ESTÁN CARGADAS, SOLO EL ÍNDICE]",
            "Antes de tocar cualquiera de estos temas, leer el archivo "
            "completo con Read. No trabajar el tema de memoria ni suponer qué "
            "dice la regla: el índice dice de qué trata cada archivo, no qué "
            "manda.",
            "",
            "\n".join(lineas),
        ])

    detallado = [f"  base/{rel}  ({kb} KB) — {titulo}"
                 for rel, kb, titulo in entradas]
    texto = _armar(detallado)
    if tope is None or len(texto.encode("utf-8")) <= tope:
        return texto, []

    colapsado = _por_capitulo(entradas)
    texto = _armar(colapsado)
    if len(texto.encode("utf-8")) <= tope:
        return texto, [
            "el índice del resto de las reglas se colapsó a un renglón por "
            "capítulo para que el paquete entrara en el canal"]

    texto = _armar([])
    avisos = ["el índice del resto de las reglas no cupo y se quitó entero"]
    if len(texto.encode("utf-8")) > tope:
        # Las reglas solas ya no caben. No se recortan: se dice, fuerte, que
        # el paquete va a perderse, porque lo que no se puede permitir es que
        # el agente crea que las tiene.
        avisos.append(
            "LAS REGLAS NO CABEN EN EL CANAL, ni siquiera solas: "
            f"{_kb(texto)} KB contra un tope de {max(1, tope // 1024)} KB. "
            "Es un defecto del estándar y hay que reportarlo (`02·F24`)")
    return texto, avisos


def contexto(estandar, gate_ok=True, tope=None):
    """Solo el texto de [`paquete`](#paquete), para quien no mira los avisos."""
    return paquete(estandar, gate_ok, tope)[0]


if __name__ == "__main__":
    # `53` · Un modulo que se ejecuta solo y no imprime nada dice, con su
    # silencio, lo mismo que diria si hubiera comprobado y estuviera todo bien.
    comun.no_es_punto_de_entrada()
