#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganche `UserPromptSubmit`: revisa el stack de instalación en cada mensaje.

    python hook_checklist.py --raiz "C:/ruta/del/proyecto"

Mientras falte un componente, en **cada** mensaje del usuario:

  - escribe `.agente/INSTALACION-INCOMPLETA.md` con la lista y cómo se arregla;
  - se lo muestra al usuario (`systemMessage`);
  - se lo pasa al agente (`additionalContext`), que debe decirlo.

Cuando ya no falta nada, borra la marca y **calla**. Un aviso que aparece
siempre, aunque todo esté bien, se deja de leer a los dos días.

No bloquea: un proyecto a medio instalar igual puede necesitar trabajo urgente.
El único que detiene es el gate `02·F13`, que ya lo hacía antes que esto.

Sale siempre con código 0.
"""
import json
import os
import sys

# **Vive en el adaptador, no en `validadores/`.** Por eso tiene que decir
# dónde están los módulos que usa: el trabajo es agnóstico y sigue allá;
# acá sólo está lo que habla con esta herramienta.
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "validadores"))

import checklist                            # noqa: E402
from comun import RAIZ, preparar_salida     # noqa: E402


def opcion(argv, nombre, por_defecto=""):
    if nombre in argv:
        i = argv.index(nombre)
        if i + 1 < len(argv):
            return argv[i + 1]
    return por_defecto


def _entrada():
    try:
        crudo = sys.stdin.buffer.read()
    except (AttributeError, ValueError):
        crudo = (sys.stdin.read() or "").encode("utf-8", "replace")
    try:
        return json.loads(crudo.decode("utf-8", "replace"))
    except (json.JSONDecodeError, ValueError):
        return {}


def main():
    preparar_salida()
    datos = _entrada()

    raiz = opcion(sys.argv[1:], "--raiz") or datos.get("cwd") or os.getcwd()
    raiz = os.path.abspath(raiz)

    # El propio estándar no se instala a sí mismo: es donde viven las reglas.
    if os.path.normcase(raiz) == os.path.normcase(RAIZ):
        return 0

    try:
        puntos = checklist.revisar(raiz)
        checklist.escribir_marca(raiz, puntos)
    except Exception as e:      # noqa: BLE001 — nunca romper la sesión
        print(f"No se pudo revisar la instalación: {e}", file=sys.stderr)
        return 0

    if not checklist.pendientes(puntos):
        return 0                # instalación completa: nada que decir

    resumen = checklist.resumen(raiz, puntos)
    contexto = (f"[Instalación del agente incompleta]\n{resumen}\n\n"
                f"{checklist.detalle(puntos)}\n\n"
                f"Decíselo al usuario en esta respuesta: qué falta y cómo se "
                f"arregla. El detalle también quedó en "
                f"`{checklist.MARCA.replace(os.sep, '/')}`.")

    print(json.dumps({
        "systemMessage": resumen,
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": contexto,
        },
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
