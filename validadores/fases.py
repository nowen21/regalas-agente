#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Jerarquía y nomenclatura de fases — `base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md`.

Recorre `documentacion/epicas/` y comprueba lo que F12 dice sin ambigüedad:

  F12.1/F12.3/F12.4 — una fase pertenece a UNA sola HU, y su identificador no
                      aparece bajo dos HU distintas.
  F12.2  — una HU tiene al menos una fase.
  F12.6  — nombre de fase: [consecutivo]-EP[nn]-HU[nn]-[descripción].
  F12.7  — el consecutivo no se repite dentro de la misma HU.
  F12.11 — jerarquía Épica → HU → Fase.
  F12.13 — cada fase lleva sus cuatro documentos.

**Qué se exige del formato y qué no.** F12 escribe `EP-001` y `HU-003` en sus
cuatro ejemplos y en el árbol: el **guion separador** es deliberado y se exige.
El **ancho de los números** no: la regla nunca dice "tres dígitos", y los
proyectos alternan `HU-01` y `HU-013`. Exigir lo que la norma no declara sería
inventar la regla desde el código — el error que este validador vino a evitar.
"""
import os
import re

from comun import AVISO, FALLA, Hallazgo

CARPETA = "documentacion/epicas"

# F12.13 · los cuatro documentos de una fase.
DOCUMENTOS = ["plan_trabajo.md", "plan_pruebas.md",
              "funcionalidad_implementada.md", "estado-fase.md"]

_EPICA = re.compile(r"^EP-(\d+)-(.+)$")
_HU = re.compile(r"^HU-(\d+)-(.+)$")

# F12.6  ·  [consecutivo]-EP-[nnn]-HU-[nnn]-[descripción]
# F12.12 ·  [consecutivo]-[consecutivo-que-complementa]-EP-[nnn]-HU-[nnn]-[desc]
_FASE = re.compile(
    r"^(?P<consecutivo>[A-Z]{1,3})"
    r"(?:-(?P<complementa>[A-Z]{1,3}))?"
    r"-EP-(?P<epica>\d+)"
    r"-HU-(?P<hu>\d+)"
    r"-(?P<descripcion>.+)$")


def _numero(texto):
    """`002` y `2` son el mismo número de épica."""
    return int(texto)


def _orden_letras(letras):
    """A=1, B=2, …, Z=26, AA=27, AB=28… (base 26 bijectiva). Ordena el consecutivo."""
    n = 0
    for c in letras.upper():
        n = n * 26 + (ord(c) - ord("A") + 1)
    return n


def _subcarpetas(ruta):
    if not os.path.isdir(ruta):
        return []
    return sorted(n for n in os.listdir(ruta)
                  if os.path.isdir(os.path.join(ruta, n)))


def validar(proyecto):
    proyecto = os.path.abspath(proyecto)
    raiz = os.path.join(proyecto, *CARPETA.split("/"))
    hallazgos = []

    if not os.path.isdir(raiz):
        return [Hallazgo(FALLA, proyecto, 0,
                         f"no existe `{CARPETA}` — F12.13 la exige")]

    for nombre_epica in _subcarpetas(raiz):
        ruta_epica = os.path.join(raiz, nombre_epica)
        donde_epica = f"{CARPETA}/{nombre_epica}"

        m_epica = _EPICA.match(nombre_epica)
        if not m_epica:
            hallazgos.append(Hallazgo(
                FALLA, donde_epica, 0,
                "no parece una épica: se espera `EP-<número>-<slug>` (F12.13)"))
            continue
        num_epica = _numero(m_epica.group(1))

        # F12.13 · la épica lleva su documento. El nombre exacto varía entre la
        # norma (`epica.md`) y los proyectos (`EP-000-slug.md`): basta con que
        # exista uno de los dos.
        if not any(os.path.isfile(os.path.join(ruta_epica, n))
                   for n in ("epica.md", f"{nombre_epica}.md")):
            hallazgos.append(Hallazgo(
                AVISO, donde_epica, 0,
                "sin documento de épica (`epica.md` o "
                f"`{nombre_epica}.md`)"))

        hijas = _subcarpetas(ruta_epica)
        if not hijas:
            continue

        for nombre_hu in hijas:
            ruta_hu = os.path.join(ruta_epica, nombre_hu)
            donde_hu = f"{donde_epica}/{nombre_hu}"

            m_hu = _HU.match(nombre_hu)
            if not m_hu:
                # F12.11 · dentro de una épica solo van HU.
                hallazgos.append(Hallazgo(
                    FALLA, donde_hu, 0,
                    "dentro de una épica solo van HU — se espera "
                    "`HU-<número>-<slug>` (F12.11)"))
                continue
            num_hu = _numero(m_hu.group(1))

            if not os.path.isfile(os.path.join(ruta_hu, f"{nombre_hu}.md")):
                hallazgos.append(Hallazgo(
                    AVISO, donde_hu, 0, f"sin documento `{nombre_hu}.md`"))

            hallazgos += _validar_fases(ruta_hu, donde_hu, num_epica, num_hu)

    return hallazgos


def _validar_fases(ruta_hu, donde_hu, num_epica, num_hu):
    hallazgos = []
    fases = _subcarpetas(ruta_hu)

    if not fases:
        # F12.2 · toda HU tiene al menos una fase. AVISO y no FALLA: una HU
        # recién abierta todavía no tiene ninguna, y eso no es incumplimiento.
        return [Hallazgo(AVISO, donde_hu, 0,
                         "sin fases — F12.2 pide al menos una")]

    vistos = {}
    for nombre in fases:
        donde = f"{donde_hu}/{nombre}"
        m = _FASE.match(nombre)

        if not m:
            hallazgos.append(Hallazgo(
                FALLA, donde, 0,
                "el nombre no sigue F12.6 — se espera "
                "`<consecutivo>-EP-<número>-HU-<número>-<descripción>`, "
                "p. ej. `A-EP-001-HU-003-Configuración inicial`"))
            continue

        # F12.1 / F12.3 / F12.4 · la fase declara a qué épica y HU pertenece;
        # si no coincide con dónde está guardada, la trazabilidad es falsa.
        if _numero(m.group("epica")) != num_epica:
            hallazgos.append(Hallazgo(
                FALLA, donde, 0,
                f"declara la épica {m.group('epica')} pero está guardada en la "
                f"{num_epica} (F12.1)"))
        if _numero(m.group("hu")) != num_hu:
            hallazgos.append(Hallazgo(
                FALLA, donde, 0,
                f"declara la HU {m.group('hu')} pero está guardada en la "
                f"{num_hu} (F12.3 · una fase no se comparte entre HU)"))

        # F12.7 · el consecutivo ordena las fases dentro de la HU; repetirlo
        # deja el orden indefinido.
        consecutivo = m.group("consecutivo").upper()
        if consecutivo in vistos:
            hallazgos.append(Hallazgo(
                FALLA, donde, 0,
                f"el consecutivo «{consecutivo}» ya lo usa "
                f"«{vistos[consecutivo]}» (F12.7)"))
        else:
            vistos[consecutivo] = nombre

        faltan = [d for d in DOCUMENTOS
                  if not os.path.isfile(os.path.join(ruta_hu, nombre, d))]
        if faltan:
            hallazgos.append(Hallazgo(
                AVISO, donde, 0,
                f"faltan documentos de la fase (F12.13): {', '.join(faltan)}"))

    # F12.5 · el consecutivo alfabético forma la secuencia A, B, C… sin huecos.
    # AVISO y no FALLA: una fase diferida deja un hueco legítimo que mira un humano.
    if vistos:
        orden = sorted(_orden_letras(c) for c in vistos)
        if orden != list(range(1, len(orden) + 1)):
            hallazgos.append(Hallazgo(
                AVISO, donde_hu, 0,
                "el consecutivo de fases no es A, B, C… sin huecos (F12.5): "
                + ", ".join(sorted(vistos))))

    return hallazgos
