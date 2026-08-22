#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Desfase de versión del estándar — `pendiente 04`.

Compara la versión de `base/`+`plantillas/` (el archivo `VERSION` del estándar)
con la que **declara** el proyecto en su `CLAUDE.md` (capa 3). Si el proyecto
quedó por detrás, **avisa** — no migra: subir de versión es decisión del usuario,
y las fases ya cerradas quedan selladas con su versión (regla de retroactividad).

El desfase a secas es **AVISO**: no es un incumplimiento, es una señal para
decidir. Con una sola excepción, y es `02·F22`: si en ese desfase hay una regla
**derogada** sin adoptar, el proyecto no abre ni cierra fase, y eso sí es
**FALLA**. Esa parte la comprueba `validar_fase`, que llama `flujo.py` porque es
el que recorre las fases.
"""
import os
import re

import comun
from comun import AVISO, FALLA, Hallazgo, RAIZ, leer

# Acepta 'X.Y.Z' en la línea "Versión del estándar adoptada: X.Y.Z".
_ADOPTADA = re.compile(
    r"(?i)versi[oó]n\s+del\s+est[aá]ndar\s+adoptada[^\n]*?(\d+\.\d+\.\d+)")

# El encabezado de una regla derogada: '## F6 · … · `[DEROGADA en 4.0.0 → ver 13·DOC1]`'
# (`20·M11`). Solo se mira la línea del encabezado: las tablas de los índices y
# los ejemplos del molde repiten la marca y no son reglas.
# `## 31.9.0 — 2026-08-22` — la cabecera de una entrada del registro.
_ENTRADA_DEL_REGISTRO = re.compile(r"^##\s+(\d+\.\d+\.\d+)\b", re.M)

# `2026-08-20-28.0.0.md` — el registro que el instalador deja por adopción.
_NOMBRE_DE_ADOPCION = re.compile(r"^\d{4}-\d{2}-\d{2}-(\d+\.\d+\.\d+)\.md$")

_ENCABEZADO_DEROGADA = re.compile(
    r"^##\s+(\S+)\s*·[^\n]*?\[DEROGADA\s+en\s+(\d+\.\d+\.\d+)\s*(?:→|->)\s*ver\s+([^\]`]+)\]",
    re.M)


def _tupla(v):
    return tuple(int(x) for x in v.split("."))


def version_estandar():
    """La versión del estándar (primer renglón de `VERSION`), o None."""
    try:
        cabeza = leer(os.path.join(RAIZ, "VERSION")).strip().splitlines()
        return cabeza[0].strip() if cabeza else None
    except OSError:
        return None


def extraer_adoptada(texto):
    """La versión que el `CLAUDE.md` declara adoptada, o None (o sin llenar)."""
    m = _ADOPTADA.search(texto)
    return m.group(1) if m else None


def comparar(adoptada, estandar):
    """Núcleo puro: motivo del desfase, o None si está al día. Aislado de disco."""
    if not estandar:
        return None                             # el estándar sin VERSION: nada que comparar
    if not adoptada:
        return (f"el proyecto no declara qué versión del estándar sigue "
                f"(el estándar va en v{estandar}) — fijarla en su CLAUDE.md")
    if _tupla(adoptada) < _tupla(estandar):
        return (f"el proyecto declara v{adoptada}, el estándar va en v{estandar}: "
                f"subir es decisión del usuario; las fases cerradas quedan selladas")
    return None


def derogaciones(base=None):
    """Las reglas derogadas del estándar: `[(versión, regla, reemplazo)]`.

    Se leen de la marca del encabezado de cada regla (`20·M11`), que es dato
    estructurado. El `CHANGELOG.md` es prosa: nombrar la palabra "derogación"
    ahí no significa que se haya derogado nada.
    """
    base = base or os.path.join(RAIZ, "base")
    encontradas = []
    for carpeta, subcarpetas, archivos in os.walk(base):
        subcarpetas[:] = [s for s in subcarpetas if not s.startswith(".")]
        for nombre in archivos:
            if not nombre.endswith(".md"):
                continue
            try:
                texto = leer(os.path.join(carpeta, nombre))
            except OSError:
                continue
            for regla, version, reemplazo in _ENCABEZADO_DEROGADA.findall(texto):
                entrada = (version, regla, reemplazo.strip())
                if entrada not in encontradas:
                    encontradas.append(entrada)
    return sorted(encontradas, key=lambda e: (_tupla(e[0]), e[1]))


def sin_adoptar(adoptada, estandar, derogadas):
    """Núcleo puro: las derogaciones que caen dentro del desfase. Aislado de disco.

    Cuenta la derogación publicada **después** de la versión que el proyecto
    declara y hasta la vigente. Sin versión adoptada no se puede decidir: se
    devuelve vacío y el desfase lo reporta `validar` como aviso.
    """
    if not adoptada or not estandar:
        return []
    desde, hasta = _tupla(adoptada), _tupla(estandar)
    return [d for d in derogadas if desde < _tupla(d[0]) <= hasta]


def versiones_publicadas(raiz_estandar=None):
    """Las versiones que el registro de cambios publica: `{"31.9.0", ...}`.

    **Se leen del `CHANGELOG.md` y no de `VERSION`**, porque `VERSION` dice
    cuál es la última y la pregunta es otra: si el número que un proyecto
    declara existió alguna vez.
    """
    raiz_estandar = raiz_estandar or RAIZ
    ruta = os.path.join(raiz_estandar, "CHANGELOG.md")
    if not os.path.isfile(ruta):
        return set()
    return set(_ENTRADA_DEL_REGISTRO.findall(leer(ruta)))


def ultima_adopcion(raiz):
    """La versión del último registro de `documentacion/versiones/`, o "".

    El instalador escribe un archivo por actualización, con la versión en el
    nombre. Que ese número y el que el proyecto declara puedan diferir es lo
    que nadie miraba.
    """
    carpeta = os.path.join(os.path.abspath(raiz), "documentacion", "versiones")
    if not os.path.isdir(carpeta):
        return ""
    encontradas = []
    for nombre in os.listdir(carpeta):
        m = _NOMBRE_DE_ADOPCION.match(nombre)
        if m:
            encontradas.append(m.group(1))
    return max(encontradas, key=_tupla) if encontradas else ""


def validar(raiz):
    raiz = os.path.abspath(raiz)
    est = version_estandar()
    claude = os.path.join(raiz, "CLAUDE.md")
    if not os.path.isfile(claude):
        return [Hallazgo(AVISO, raiz, 0,
                         "no se encontró CLAUDE.md; no se puede leer la versión adoptada")]
    adoptada = extraer_adoptada(leer(claude))
    hallazgos = []

    # **Que la versión declarada exista.** Sin esto, un número inventado no
    # solo pasa: si es mayor que la vigente, `comparar` concluye que el
    # proyecto está al día y **apaga el aviso de desfase**. La comprobación se
    # apagaba sola, y el que la apagaba no se enteraba. Es el pendiente 82.
    publicadas = versiones_publicadas()
    if adoptada and publicadas and adoptada not in publicadas:
        hallazgos.append(Hallazgo(
            FALLA, "CLAUDE.md", 0,
            f"el proyecto declara la v{adoptada}, que no existe en el registro "
            f"de cambios del estándar — mientras el número sea falso, el aviso "
            f"de desfase no dice nada"))

    # **Que coincida con el último registro de adopción.** El instalador deja
    # constancia de cada actualización; si esa constancia y la declaración no
    # dicen lo mismo, una de las dos está mal y no se sabe cuál sin mirar.
    ultima = ultima_adopcion(raiz)
    if adoptada and ultima and adoptada != ultima:
        hallazgos.append(Hallazgo(
            FALLA, "CLAUDE.md", 0,
            f"el proyecto declara la v{adoptada} y su último registro de "
            f"adopción dice v{ultima} — una de las dos está mal, y el aviso de "
            f"desfase se calcula sobre la declarada"))

    motivo = comparar(adoptada, est)
    if motivo:
        hallazgos.append(Hallazgo(AVISO, "CLAUDE.md", 0, motivo))
    return hallazgos


def validar_fase(raiz):
    """`02·F22` — con una derogación sin adoptar, el proyecto no avanza de fase.

    Lo llama `flujo.py`, que es el que recorre las fases: la comprobación se
    cobra al abrir y al cerrar una fase, no en cualquier momento.
    """
    raiz = os.path.abspath(raiz)
    claude = os.path.join(raiz, "CLAUDE.md")
    if not os.path.isfile(claude):
        return []
    pendientes = sin_adoptar(extraer_adoptada(leer(claude)),
                             version_estandar(), derogaciones())
    if not pendientes:
        return []
    detalle = " · ".join(f"{regla} (derogada en {ver} → {reemplazo})"
                         for ver, regla, reemplazo in pendientes)
    return [Hallazgo(
        FALLA, "CLAUDE.md", 0,
        f"hay derogaciones sin adoptar y ninguna fase se abre ni se cierra hasta "
        f"adoptarlas (F22): {detalle}. Se abre una fase por cada HU que implementaba "
        f"la regla derogada, y al cerrarla se sube la versión declarada")]


if __name__ == "__main__":
    # `53` · Un modulo que se ejecuta solo y no imprime nada dice, con su
    # silencio, lo mismo que diria si hubiera comprobado y estuviera todo bien.
    comun.no_es_punto_de_entrada("version")
