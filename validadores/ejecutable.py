#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Toda regla del núcleo dice quién la hace cumplir — `EP-005·HU-012`.

**Por qué existe.** Una regla escrita **informa**; un programa o un enganche
**ejecuta**. El estándar no distinguía las dos cosas, así que una regla del
núcleo podía existir sin que nada la hiciera cumplir y leerse igual que una que
sí. La cuenta del 2026-08-31: de las **18** reglas vigentes del capítulo `00`,
**14** no tenían quién las ejecutara, y siete ni siquiera se nombraban en un
programa.

**Qué comprueba, y qué no.** Comprueba que la declaración **esté**, que traiga
su motivo cuando dice que nadie la hace cumplir, y que la pieza nombrada exista
en el repositorio. **No comprueba que la pieza de verdad la haga cumplir**: eso
se lee. Prometerlo sería el defecto que esta casa persigue — un número que el
lector completa con lo que quiere creer (`S-091`).

**Solo el capítulo `00`.** Es el alcance que la historia fijó (§3.3): el núcleo
es lo que no se relaja, así que es donde más cuesta que una regla mande sin que
nada la sostenga. Se extenderá si el caso se repite fuera de ahí.
"""
import os
import re

import comun
import metareglas
from comun import FALLA, Hallazgo, RAIZ, relativo

# El capítulo que esta comprobación cubre hoy.
CAPITULO = "00"

# Las dos aperturas, y ninguna más. **Un campo de valor libre dejaría pasar
# «pendiente» y «se está viendo»**, que es justo lo que la historia impide.
_QUIEN = re.compile(r"(?m)^>?\s*\*\*Quién la hace cumplir:\*\*\s*(.+?)\s*$")
_NADIE = re.compile(r"(?m)^>?\s*\*\*Nadie la hace cumplir:\*\*\s*(.+?)\s*$")

# Un motivo más corto que esto no es un motivo: es una casilla marcada. El
# número no sale de una teoría — sale de que «no se puede», «es criterio» y «lo
# lee una persona» caben todas por debajo, y ninguna de las tres dice nada.
MOTIVO_MINIMO = 40

# La pieza se nombra por su ruta desde la raíz del repositorio, entre comillas
# invertidas. Se pide la ruta y no el nombre suelto para poder resolverla contra
# el disco: `marcas.py` aparece en tres carpetas, `validadores/marcas.py` en una.
_PIEZA = re.compile(r"`([A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)+)`")

# Dónde se escribe, para que el mensaje diga qué hacer y no solo qué falta
# (`RNF-01`).
DONDE = ("después del ejemplo y antes del checklist, con una de las dos "
         "aperturas: `**Quién la hace cumplir:**` o `**Nadie la hace "
         "cumplir:**`")


def declaracion(regla):
    """`(clase, texto)` de la regla: `"quien"`, `"nadie"` o `(None, "")`."""
    m = _QUIEN.search(regla.texto)
    if m:
        return "quien", m.group(1).strip()
    m = _NADIE.search(regla.texto)
    if m:
        return "nadie", m.group(1).strip()
    return None, ""


def piezas(texto):
    """Las rutas que la declaración nombra, en el orden en que aparecen."""
    salida = []
    for ruta in _PIEZA.findall(texto):
        if ruta not in salida:
            salida.append(ruta)
    return salida


def _del_nucleo(raiz):
    """Las reglas vigentes del capítulo `00`.

    **La derogada queda fuera**, por el mismo motivo que la exime `20·M9`: dejó
    de regir, y pedirle que declare quién la hace cumplir es pedirle cuentas a
    una regla que ya no manda.
    """
    return [r for r in metareglas.reglas(raiz)
            if r.capitulo == CAPITULO and not r.derogada]


def validar(raiz=None):
    """Un hallazgo por regla del núcleo que no dice quién la hace cumplir."""
    raiz = raiz or RAIZ
    hallazgos = []
    for regla in _del_nucleo(raiz):
        clase, texto = declaracion(regla)

        if clase is None:
            hallazgos.append(Hallazgo(
                FALLA, regla.archivo, regla.linea,
                "`%s` no dice quién la hace cumplir. Se escribe %s"
                % (regla.id, DONDE)))
            continue

        if clase == "nadie":
            if len(texto) < MOTIVO_MINIMO:
                hallazgos.append(Hallazgo(
                    FALLA, regla.archivo, regla.linea,
                    "`%s` declara que nadie la hace cumplir y no dice por qué. "
                    "Una casilla marcada sin motivo no es una decisión"
                    % regla.id))
            continue

        nombradas = piezas(texto)
        if not nombradas:
            hallazgos.append(Hallazgo(
                FALLA, regla.archivo, regla.linea,
                "`%s` dice que alguien la hace cumplir y no nombra la pieza. "
                "Va su ruta desde la raíz, entre comillas invertidas — por "
                "ejemplo `validadores/marcas.py`" % regla.id))
            continue

        for ruta in nombradas:
            if not os.path.exists(os.path.join(raiz, ruta.replace("/", os.sep))):
                hallazgos.append(Hallazgo(
                    FALLA, regla.archivo, regla.linea,
                    "`%s` declara como pieza `%s`, que no existe en el "
                    "repositorio" % (regla.id, ruta)))
    return hallazgos


def cuenta(raiz=None):
    """`{"reglas","con_pieza","sin_nadie"}` — la foto que abre y cierra la fase."""
    raiz = raiz or RAIZ
    con, nadie = 0, 0
    reglas = _del_nucleo(raiz)
    for regla in reglas:
        clase, _texto = declaracion(regla)
        if clase == "quien":
            con += 1
        elif clase == "nadie":
            nadie += 1
    return {"reglas": len(reglas), "con_pieza": con, "sin_nadie": nadie}


def como_texto(raiz=None):
    """La línea que se lee al cerrar: cuántas manda un programa y cuántas no."""
    raiz = raiz or RAIZ
    c = cuenta(raiz)
    if not c["reglas"]:
        return ""
    return ("Quién hace cumplir el núcleo (`%s`): %d reglas · %d con pieza que "
            "las ejecuta · %d declaradas sin quien las ejecute\n"
            "  Declararlo no es hacerlas cumplir: que la pieza de verdad las "
            "ejecute lo lee una persona." %
            (relativo(os.path.join(raiz, "base")), c["reglas"],
             c["con_pieza"], c["sin_nadie"]))


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("ejecutable")
