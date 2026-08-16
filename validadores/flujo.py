#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El plan y los padres de cada fase — `02·F14`, `02·F17`, `02·F0`, `02·F2` y
`02·F18`.

Recorre `documentacion/epicas/…/<fase>/` (la misma estructura que `fases.py`) y
comprueba sin criterio:

  F0   · cada fase tiene sus **padres**: la épica y la HU de las que cuelga
         existen como documento (no solo como carpeta).
  F2   · el plan **declara su especificación** y esa especificación existe. Sin especificación acordada no hay
         código, y un plan que no la nombra es código sin respaldo. La otra
         mitad —que ningún módulo del proyecto tenga código sin especificación— se
         comprueba contra los módulos declarados en `.agente/dominio.md`.
  F14 · el plan responde las 13 preguntas obligatorias. La plantilla las numera
         como secciones `## 0.` … `## 13.`; se marca cuáles faltan.
  F17 · el plan no deja **incertidumbre** sin resolver: `TBD`, `(o similar)`,
         `(o donde esté)`, `(o parecido)`. La línea base debe ir verificada.
  F18 · toda intervención del plan cuelga de un **criterio de aceptación**: cada
         tarea vive bajo su `### CA-nn`, cada CA declarado tiene su desglose y
         no aparece un CA que la fase no declaró.

No juzga el contenido de cada sección (eso es humano); solo presencia, marcas de
duda y a qué cuelga cada tarea. **AVISO**: un plan en curso puede estar
incompleto a propósito.

Nota: los planes que **preceden** a esta plantilla marcarán secciones faltantes.
Es correcto —no conforman a F14—, no un falso positivo.
"""
import os
import re

import declaracion
import fases
import version
from comun import AVISO, FALLA, Hallazgo, filas_de, leer, valor_limpio

CARPETA = "documentacion/epicas"

# F14 · las secciones que la plantilla numera 0..13 (una por bloque de preguntas).
_SECCIONES = list(range(0, 14))
_ENCABEZADO = re.compile(r"(?m)^#{1,4}\s*(\d{1,2})\.")

# F17 · marcas de que la línea base no se verificó.
_INCERTIDUMBRE = re.compile(
    r"(?i)\bTBD\b|\bpor\s+definir\b|\(o\s+(similar|donde\s+est[eé]|parecid[oa]|equivalente)\)")

# F18 · el desglose por criterio de aceptación.
_CA = re.compile(r"\bCA-(\d+)\b")
_TITULO_CA = re.compile(r"(?m)^#{2,4}\s*(CA-\d+|RNF)\b")
_TITULO = re.compile(r"(?m)^(#{1,4})\s*(.+?)\s*$")
_TAREA = re.compile(r"^\|\s*`?(T-\d+)`?\s*\|")
_SOPORTE = re.compile(r"(?i)soporte\s+(?:técnico\s+)?(?:de\s+)?CA-\d+")

# F2 · la fila del plan donde va la especificación, y el marcador que la plantilla trae
# sin llenar.
_SIN_LLENAR = re.compile(r"(?i)^\[?enlace\b|^«|^\.\.\.$")


def _texto(ruta):
    try:
        return leer(ruta)
    except OSError:
        return ""


def revisar_plan(texto):
    """Núcleo puro: (faltan_secciones, incertidumbres) de un plan_trabajo.
    `faltan_secciones` es la lista de números F14 ausentes; `incertidumbres`
    es la lista de (linea, fragmento). Aislado de git."""
    presentes = {int(n) for n in _ENCABEZADO.findall(texto)}
    faltan = [n for n in _SECCIONES if n not in presentes]

    incertidumbres = []
    for i, linea in enumerate(texto.splitlines(), 1):
        m = _INCERTIDUMBRE.search(linea)
        if m:
            incertidumbres.append((i, m.group(0)))
    return faltan, incertidumbres


def revisar_ca(texto):
    """Núcleo puro de `F18`: cómo cuelga cada intervención de su CA.

    Devuelve `(tareas_sueltas, ca_sin_desglose, ca_no_declarados)`:

      tareas_sueltas    `[(línea, tarea)]` de las que no viven bajo ningún CA.
      ca_sin_desglose   CA que la fase declara en §0 y no desglosa en §3.
      ca_no_declarados  CA que aparecen en §3 y que la fase no declaró.

    La excepción de la regla —el ítem de **soporte técnico**, que se admite sin
    CA propio si se declara— se respeta: la fila que dice "soporte de CA-x" no
    cuenta como suelta.
    """
    seccion, ca_actual = None, None
    declarados, desglosados, sueltas = set(), set(), []

    for n, linea in enumerate(texto.splitlines(), start=1):
        titulo = _TITULO.match(linea)
        if titulo:
            m = _ENCABEZADO.match(linea)
            if m:
                seccion = int(m.group(1))
            marca = _TITULO_CA.match(linea)
            ca_actual = marca.group(1) if marca else None
            if marca and seccion == 3 and marca.group(1) != "RNF":
                desglosados.add(marca.group(1))
            continue

        if seccion in (None, 0):
            declarados |= {f"CA-{d}" for d in _CA.findall(linea)}
        if seccion == 3 and _TAREA.match(linea) and not ca_actual:
            if not _SOPORTE.search(linea) and not _CA.search(linea):
                sueltas.append((n, _TAREA.match(linea).group(1)))

    return (sueltas,
            sorted(declarados - desglosados),
            sorted(desglosados - declarados))


def revisar_especificacion(texto):
    """Núcleo puro de `F2`: qué declara el plan como especificación del módulo.

    Devuelve la ruta declarada, o "" si el plan no la declara (o dejó el
    marcador de la plantilla sin reemplazar).
    """
    for _, fila in filas_de(texto, "campo", "valor"):
        campo = fila["campo"].lower()
        if "especificación" not in campo:
            continue
        crudo = fila["valor"].strip()
        enlace = re.search(r"\]\(([^)\s]+)", crudo)
        if enlace:
            return enlace.group(1)
        valor = valor_limpio(crudo)
        if not valor or _SIN_LLENAR.match(valor) or valor.startswith("["):
            return ""
        return valor
    return ""


def _especificacion_existe(proyecto, carpeta_fase, ruta):
    """La especificación se busca donde la escribiría cualquiera: relativa al plan, o
    desde la raíz del proyecto."""
    ruta = ruta.split("#", 1)[0].replace("\\", "/")
    if not ruta or ruta.startswith(("http://", "https://")):
        return True
    for base in (carpeta_fase, proyecto):
        if os.path.exists(os.path.normpath(os.path.join(base, *ruta.split("/")))):
            return True
    return False


def _modulos_sin_especificacion(proyecto):
    """F2 visto desde el otro lado: un módulo declarado cuya especificación no está."""
    d = declaracion.leer_declaracion(proyecto)
    hallazgos = []
    for modulo in d.modulos:
        if not modulo.especificacion:
            hallazgos.append(Hallazgo(
                AVISO, os.path.join(proyecto, declaracion.DOMINIO), 0,
                f"el módulo `{modulo.nombre}` no declara su especificación — F2: sin especificación "
                f"acordada no hay código"))
            continue
        ruta = os.path.normpath(os.path.join(proyecto, *modulo.especificacion.split("/")))
        if not os.path.exists(ruta):
            hallazgos.append(Hallazgo(
                AVISO, os.path.join(proyecto, declaracion.DOMINIO), 0,
                f"el módulo `{modulo.nombre}` declara la especificación `{modulo.especificacion}` "
                f"y ese archivo no existe (F2)"))
    return hallazgos


def validar(proyecto):
    proyecto = os.path.abspath(proyecto)
    raiz = os.path.join(proyecto, *CARPETA.split("/"))
    if not os.path.isdir(raiz):
        return [Hallazgo(FALLA, proyecto, 0, f"no existe `{CARPETA}` (F12.13)")]

    hallazgos = []
    hay_fases = False
    for nombre_epica in fases._subcarpetas(raiz):
        ruta_epica = os.path.join(raiz, nombre_epica)
        # F0 · la épica existe como documento, no solo como carpeta.
        tiene_doc_epica = any(
            os.path.isfile(os.path.join(ruta_epica, n))
            for n in ("epica.md", f"{nombre_epica}.md"))
        epica_con_fases = False
        for nombre_hu in fases._subcarpetas(ruta_epica):
            ruta_hu = os.path.join(ruta_epica, nombre_hu)
            tiene_fases = bool(fases._subcarpetas(ruta_hu))
            epica_con_fases = epica_con_fases or tiene_fases
            # F0 · la HU existe como documento.
            if tiene_fases and not os.path.isfile(os.path.join(ruta_hu, f"{nombre_hu}.md")):
                hallazgos.append(Hallazgo(
                    AVISO, f"{CARPETA}/{nombre_epica}/{nombre_hu}", 0,
                    "hay fases pero la HU no tiene su documento (F0: falta el padre)"))
            for nombre_fase in fases._subcarpetas(ruta_hu):
                plan = os.path.join(ruta_hu, nombre_fase, "plan_trabajo.md")
                if not os.path.isfile(plan):
                    continue
                donde = f"{CARPETA}/{nombre_epica}/{nombre_hu}/{nombre_fase}/plan_trabajo.md"
                texto_plan = _texto(plan)
                faltan, incertidumbres = revisar_plan(texto_plan)

                # F2 · el plan declara su especificación, y la especificación existe.
                especificación = revisar_especificacion(texto_plan)
                if not especificación:
                    hallazgos.append(Hallazgo(
                        AVISO, donde, 0,
                        "el plan no declara la especificación del módulo (F2: sin especificación "
                        "acordada no hay código)"))
                elif not _especificacion_existe(proyecto, os.path.dirname(plan), especificación):
                    hallazgos.append(Hallazgo(
                        AVISO, donde, 0,
                        f"el plan declara la especificación `{especificación}` y ese archivo no "
                        f"existe (F2)"))

                # F18 · cada intervención cuelga de un CA.
                sueltas, sin_desglose, no_declarados = revisar_ca(texto_plan)
                for linea, tarea in sueltas:
                    hallazgos.append(Hallazgo(
                        AVISO, donde, linea,
                        f"la intervención `{tarea}` no cuelga de ningún criterio "
                        f"de aceptación (F18)"))
                if sin_desglose:
                    hallazgos.append(Hallazgo(
                        AVISO, donde, 0,
                        "la fase declara criterios que no desglosa en tareas: "
                        + ", ".join(sin_desglose) + " (F18)"))
                if no_declarados:
                    hallazgos.append(Hallazgo(
                        AVISO, donde, 0,
                        "el plan desglosa criterios que la fase no declaró en §0: "
                        + ", ".join(no_declarados) + " (F18)"))

                if faltan:
                    hallazgos.append(Hallazgo(
                        AVISO, donde, 0,
                        "al plan le faltan secciones de las 13 preguntas (F14): "
                        + ", ".join(map(str, faltan))))
                for linea, frag in incertidumbres:
                    hallazgos.append(Hallazgo(
                        AVISO, donde, linea,
                        f"marca de incertidumbre `{frag}` en el plan — F17 pide "
                        f"la línea base verificada"))
        if epica_con_fases and not tiene_doc_epica:
            hallazgos.append(Hallazgo(
                AVISO, f"{CARPETA}/{nombre_epica}", 0,
                "hay fases pero la épica no tiene su documento (F0: falta el padre)"))
        hay_fases = hay_fases or epica_con_fases

    # F22 · con una derogación sin adoptar no se abre ni se cierra fase. Solo
    # se cobra donde hay fases: sin ellas, el desfase se queda en aviso.
    if hay_fases:
        hallazgos += version.validar_fase(proyecto)
    return hallazgos + _modulos_sin_especificacion(proyecto)
