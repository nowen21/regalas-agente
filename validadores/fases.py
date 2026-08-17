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
DOCUMENTOS = ["plan_trabajo.md", "plan_pruebas.md", "resultado_pruebas.md",
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


# El veredicto, en las dos formas que hay escritas en el repositorio.
_CONCEPTO_FILA = re.compile(r"^\|\s*\*\*Concepto\*\*\s*\|([^|]+)\|", re.M)
_CONCEPTO_SUELTO = re.compile(r"\*\*Concepto:\s*([^*.]+)", re.M)

# `CA cumplidos` en las fases nuevas, `Criterios cumplidos` en las viejas.
_CONTEO = re.compile(
    r"\*\*(?:CA|Criterios)\s+cumplidos\*\*\s*\|\s*\**(\d+)\**\s+de\s+\**(\d+)",
    re.I)

# El §5 del resultado: la tabla de veredicto por exigencia.
_SECCION_5 = re.compile(r"^##\s+5\.[^\n]*\n(.*?)(?=^##\s)", re.M | re.S)


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


def _leer(ruta):
    try:
        with open(ruta, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def _concepto(texto):
    """El veredicto que declara un documento, normalizado, o "" si no lo dice.

    Se reconocen las dos formas que hay escritas: la fila de tabla
    `| **Concepto** | Cumple |` y la del molde viejo, `**Concepto: Cumple.**`.
    Reprobar por la forma vieja sería reabrir fases cerradas, y el estándar no
    reabre lo cerrado.
    """
    m = _CONCEPTO_FILA.search(texto) or _CONCEPTO_SUELTO.search(texto)
    if not m:
        return ""
    # La salvedad que va al lado —«Cumple, con una salvedad»— no es otro
    # veredicto: se compara lo que el concepto dice, no cómo se matiza.
    crudo = m.group(1).strip().lower().replace("*", "")
    return "no cumple" if crudo.startswith("no cumple") else (
        "cumple" if crudo.startswith("cumple") else "")


def _conteo(texto):
    """`(cumplidos, total)` de los criterios, o None si el documento no lo dice."""
    m = _CONTEO.search(texto)
    return (m.group(1), m.group(2)) if m else None


def _exigencias_en_no(texto):
    """Las filas del §5 del resultado cuya última columna es «No»."""
    seccion = _SECCION_5.search(texto)
    if not seccion:
        return []
    salida = []
    for fila in seccion.group(1).splitlines():
        celdas = [c.strip() for c in fila.strip().strip("|").split("|")]
        if len(celdas) >= 3 and celdas[-1].replace("*", "").lower() == "no":
            nombre = celdas[0].replace("*", "").strip()
            if nombre and not nombre.startswith("-"):
                salida.append(nombre)
    return salida


def veredicto(ruta_fase, donde):
    """`HU-014` — el `resultado_pruebas` y el `estado-fase` dicen lo mismo.

    El veredicto de una fase se escribe **dos veces a mano**, y el `estado-fase`
    es el que se mira para pasar la puerta de verificación: si dice que cumple,
    la fase pasa sin que nadie abra el resultado, que es donde está la verdad.
    Ya pasó una vez, en `A-EP-003-HU-010`.

    No comprueba si el veredicto es **cierto** —eso no lo puede saber un
    programa—: comprueba que los dos documentos no digan cosas distintas.
    """
    resultado = _leer(os.path.join(ruta_fase, "resultado_pruebas.md"))
    estado = _leer(os.path.join(ruta_fase, "estado-fase.md"))
    if not resultado or not estado:
        return []                       # una fase a medio escribir no se cobra acá

    hallazgos = []
    v_resultado, v_estado = _concepto(resultado), _concepto(estado)

    if v_resultado and v_estado and v_resultado != v_estado:
        hallazgos.append(Hallazgo(
            FALLA, donde, 0,
            f"los dos veredictos de la fase no coinciden (HU-014): "
            f"`resultado_pruebas` dice «{v_resultado}» y `estado-fase` dice "
            f"«{v_estado}». La puerta de verificación mira el segundo"))

    if v_estado == "cumple":
        for exigencia in _exigencias_en_no(resultado):
            hallazgos.append(Hallazgo(
                FALLA, donde, 0,
                f"la fase se da por cumplida y el `resultado_pruebas` tiene "
                f"«{exigencia}» en No (HU-014)"))

    c_resultado, c_estado = _conteo(resultado), _conteo(estado)
    if c_resultado and c_estado and c_resultado != c_estado:
        hallazgos.append(Hallazgo(
            FALLA, donde, 0,
            f"el conteo de criterios no cuadra (HU-014): `resultado_pruebas` "
            f"dice {c_resultado[0]} de {c_resultado[1]} y `estado-fase` dice "
            f"{c_estado[0]} de {c_estado[1]}"))
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

        hallazgos += veredicto(os.path.join(ruta_hu, nombre), donde)

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
