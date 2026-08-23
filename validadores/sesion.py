#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Revisión de arranque de sesión — la señal de que el estándar se cargó.

Responde tres preguntas al abrir una sesión en un proyecto:

  1. ¿Cumple `02·F13`?          (existe `proyectos/`)
  2. ¿El `CLAUDE.md` está al día con la plantilla central?   (`01·C18`)
  3. ¿Los enganches automáticos están puestos?

**Por qué existe:** C18 manda sincronizar el `CLAUDE.md`, pero era una regla que
el agente cumplía si se acordaba — y cuando no lo hacía, no quedaba ninguna
señal. El usuario no tenía forma de saber si el estándar se había cargado o no.
Esto lo vuelve un hecho comprobable en vez de una promesa.

Se usa de dos formas:
  - a mano:        python validadores/validar.py sesion --raiz "C:/ruta"
  - como enganche: hook `SessionStart` de Claude Code (ver hook_sesion.py)
"""
import os
import re

import instalar
import version
import comun
from comun import AVISO, FALLA, Hallazgo, encabezados, leer

PLANTILLA_CLAUDE = "plantillas/CLAUDE.md.plantilla"

# La plantilla marca lo que hay que reemplazar con «comillas angulares». Se
# excluye «…» a propósito: no es un marcador, es cómo se nombra a un marcador
# cuando el texto habla de ellos. Tratarlo como hueco deja al `CLAUDE.md`
# reprobando por una frase que está bien escrita.
_SIN_LLENAR = re.compile(r"«(?!…»)[^»\n]+»")


def _ruta_plantilla(estandar):
    return os.path.join(estandar, *PLANTILLA_CLAUDE.split("/"))


def revisar_claude_md(proyecto, estandar):
    """`01·C18` — el `CLAUDE.md` local contra la plantilla central.

    Solo se informa lo que **falta**; nunca lo que sobra. C18 es aditiva: el
    proyecto puede tener sus propias secciones y nadie las cuestiona.
    """
    local = os.path.join(proyecto, "CLAUDE.md")
    plantilla = _ruta_plantilla(estandar)

    if not os.path.isfile(local):
        return [Hallazgo(FALLA, local, 0,
                         "no existe el CLAUDE.md del proyecto")]
    if not os.path.isfile(plantilla):
        return [Hallazgo(AVISO, plantilla, 0,
                         "no se encontró la plantilla central")]

    texto = leer(local)
    hallazgos = []

    presentes = {t for _, t in encabezados(texto)}
    for _, titulo in encabezados(leer(plantilla)):
        if titulo not in presentes:
            hallazgos.append(Hallazgo(
                AVISO, local, 0,
                f"la plantilla central tiene «{titulo}» y este CLAUDE.md no "
                f"— C18: agregar la sección vacía, sin pisar lo escrito"))

    for n, linea in enumerate(texto.splitlines(), start=1):
        for m in _SIN_LLENAR.finditer(linea):
            hallazgos.append(Hallazgo(
                FALLA, local, n,
                f"quedó sin reemplazar: {m.group(0)}"))

    # Comparar títulos solo detecta secciones enteras que faltan. Un cambio
    # dentro de una sección que ya existe —un paso nuevo en una lista, por
    # ejemplo— pasa desapercibido. La fecha sí lo delata: si la plantilla
    # central cambió después, hay algo que mirar. No dice QUÉ cambió, dice
    # que hay que mirar, que es justo lo que C18 pide hacer.
    if os.path.getmtime(plantilla) > os.path.getmtime(local):
        hallazgos.append(Hallazgo(
            AVISO, local, 0,
            "la plantilla central cambió después de este CLAUDE.md "
            "— C18: revisar si hay algo nuevo que agregar"))

    return hallazgos


_ESTANDAR_EN_HOOK = re.compile(r'^ESTANDAR="([^"]+)"', re.MULTILINE)


def revisar_enganches(proyecto, estandar):
    """¿Los enganches están puestos y apuntando a este estándar?

    Se compara contra la línea `ESTANDAR="…"` del propio enganche. Buscar la
    ruta completa del validador no sirve: en el guion está partida entre la
    variable y su uso (`"$ESTANDAR/validadores/validar.py"`), así que la cadena
    entera nunca aparece y todo daba «apunta a otro estándar».
    """
    hallazgos = []
    esperado = os.path.normcase(estandar.replace(os.sep, "/"))

    for repo in instalar.repositorios_git(proyecto):
        etiqueta = os.path.relpath(repo, proyecto).replace("\\", "/")
        donde = repo if etiqueta == "." else f"{etiqueta}/"
        for nombre, _, _ in instalar.HOOKS:
            archivo = os.path.join(repo, ".githooks", nombre)
            if not os.path.isfile(archivo):
                hallazgos.append(Hallazgo(
                    AVISO, donde, 0,
                    f"falta el enganche {nombre} — correr "
                    f"validadores/instalar.py"))
                continue
            m = _ESTANDAR_EN_HOOK.search(leer(archivo))
            apunta = os.path.normcase(m.group(1)) if m else None
            if apunta != esperado:
                hallazgos.append(Hallazgo(
                    AVISO, donde, 0,
                    f"el enganche {nombre} apunta a «{apunta or '?'}» y no a "
                    f"este estándar — reinstalar"))

    return hallazgos


def revisar(proyecto, estandar):
    """Todas las comprobaciones de arranque, en orden de precedencia."""
    proyecto = os.path.abspath(proyecto)

    # F13 primero: sin la estructura base, lo demás no tiene sentido todavía.
    # Ya no es un muro — la carpeta la crea el instalador—, así que si falta es
    # que el proyecto nunca se instaló, y eso se arregla con una línea.
    if not instalar.cumple_f13(proyecto):
        return [Hallazgo(FALLA, proyecto, 0,
                         "falta la carpeta `proyectos/` (02·F13): este proyecto "
                         "no está instalado — correr validadores/instalar.py "
                         "--aplicar")]

    # **El aviso de quedarse atrás va acá, y no es un añadido cualquiera.**
    # Existía como subcomando y había que pedirlo a mano, así que nunca
    # llegaba al proyecto: la funcionalidad central de su historia se veía
    # funcionar solo en el repositorio del estándar, donde el agente corre
    # las comprobaciones de a una. Es el pendiente 83.
    return (revisar_claude_md(proyecto, estandar)
            + revisar_enganches(proyecto, estandar)
            + version.validar(proyecto))


def resumen(proyecto, hallazgos):
    """Una línea para mostrarle al usuario al abrir la sesión."""
    nombre = os.path.basename(os.path.abspath(proyecto))
    fallas = sum(1 for h in hallazgos if h.severidad == FALLA)
    avisos = len(hallazgos) - fallas

    if not hallazgos:
        return f"Estándar cargado · {nombre} · F13 ok · CLAUDE.md al día · enganches puestos"

    partes = []
    if fallas:
        partes.append(f"{fallas} falla(s)")
    if avisos:
        partes.append(f"{avisos} aviso(s)")
    detalle = "; ".join(h.mensaje for h in hallazgos[:3])
    if len(hallazgos) > 3:
        detalle += f"; y {len(hallazgos) - 3} más"
    return f"Estándar cargado · {nombre} · {' y '.join(partes)}: {detalle}"


if __name__ == "__main__":
    # `53` · Un modulo que se ejecuta solo y no imprime nada dice, con su
    # silencio, lo mismo que diria si hubiera comprobado y estuviera todo bien.
    comun.no_es_punto_de_entrada()
