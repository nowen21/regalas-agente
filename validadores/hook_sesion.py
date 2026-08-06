#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganche `SessionStart` de Claude Code — carga el estándar y avisa cómo quedó.

    python hook_sesion.py --raiz "C:/ruta/del/proyecto"

Hace dos cosas, y conviene no confundirlas:

  - **Avisa:** revisa que el estándar esté bien puesto (`sesion.py`) y devuelve
    un `systemMessage` que Claude Code le muestra al usuario.
  - **Carga:** mete las reglas base en el contexto del agente (`cargador.py`),
    que antes dependía de que el agente se acordara de leerlas.

Siempre sale con código 0: esto **informa**, no bloquea — una sesión que no
arranca porque falta una sección del `CLAUDE.md` sería peor que el problema
que resuelve.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import cargador                                 # noqa: E402
import instalar                                 # noqa: E402
import sesion                                   # noqa: E402
from comun import RAIZ, preparar_salida         # noqa: E402


def raiz_pedida(argv):
    if "--raiz" in argv:
        i = argv.index("--raiz")
        if i + 1 < len(argv):
            return os.path.abspath(argv[i + 1])
    return os.path.abspath(os.getcwd())


def main():
    preparar_salida()
    proyecto = raiz_pedida(sys.argv[1:])

    # El propio estándar no se revisa a sí mismo como si fuera un proyecto.
    if os.path.normcase(proyecto) == os.path.normcase(RAIZ):
        return 0

    try:
        hallazgos = sesion.revisar(proyecto, RAIZ)
    except Exception as e:      # noqa: BLE001 — nunca romper el arranque
        _responder(f"No se pudo revisar el arranque del estándar: {e}", [], "")
        return 0

    # Las reglas se cargan aunque la revisión encuentre fallas: un CLAUDE.md
    # desactualizado no es motivo para trabajar sin reglas. La excepción es
    # F13, que es un gate — ahí `cargador` decide solo qué corresponde dar.
    try:
        reglas = cargador.contexto(RAIZ, instalar.cumple_f13(proyecto))
    except Exception as e:      # noqa: BLE001 — nunca romper el arranque
        reglas = f"[No se pudieron cargar las reglas base: {e}]"

    _responder(sesion.resumen(proyecto, hallazgos), hallazgos, reglas)
    return 0


def _responder(resumen, hallazgos, reglas):
    """Sale por dos canales, a propósito.

    `systemMessage` lo muestra Claude Code al usuario. `additionalContext` se
    lo inyecta al agente. Van los dos porque el primero depende de que la
    interfaz lo dibuje, y si no lo dibuja el aviso se pierde sin dejar rastro
    — que es justo el problema que este enganche vino a resolver. Con el
    segundo, el agente lo sabe y puede decirlo aunque el banner no aparezca.

    Las reglas van **solo** por `additionalContext`. En `systemMessage` serían
    decenas de KB de banner en la pantalla del usuario.
    """
    detalle = "\n".join(f"  - {h}" for h in hallazgos)
    contexto = resumen if not detalle else f"{resumen}\n{detalle}"
    contexto = f"[Revisión de arranque del estándar]\n{contexto}"
    if reglas:
        contexto = f"{contexto}\n\n{reglas}"

    print(json.dumps({
        "systemMessage": resumen,
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": contexto,
        },
    }, ensure_ascii=False))


if __name__ == "__main__":
    sys.exit(main())
