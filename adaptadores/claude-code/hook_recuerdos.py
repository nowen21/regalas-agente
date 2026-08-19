#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganche de Claude Code: la memoria del agente no se queda en la herramienta.

    python hook_recuerdos.py --raiz "C:/ruta/del/proyecto"

Se instala en dos eventos, y por dos motivos distintos:

  - `SessionStart` — recoge lo que haya quedado de sesiones anteriores, antes
    de que el agente escriba nada.
  - `PostToolUse` sobre `Write|Edit` — recoge el recuerdo **en el momento** en
    que se escribió. Sin esto, el archivo pasaría toda la sesión en la carpeta
    equivocada y el agente lo daría por guardado.

Mientras esto dependa de que el agente se acuerde, no se cumple: la herramienta
escribe su memoria donde ella decide. Una instrucción **informa**; un enganche
**ejecuta** (`01·C19`).

**Solo mueve. No borra nada, nunca**, y no hace nada si el almacén ya está
enlazado a la carpeta del repositorio (ver `recuerdos.py`). Un enganche que
corre solo, en cada arranque y en cada edición, no puede tener permiso de
destruir: se equivoca una vez y se lleva la memoria entera sin que nadie lo pida.

A diferencia de los demás enganches, este **sí corre en el propio estándar**:
ahí es justamente donde vive la memoria del usuario.

Siempre sale con código 0: mover un archivo mal ubicado no es motivo para
romperle la sesión a nadie.
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

import recuerdos                             # noqa: E402
from comun import preparar_salida            # noqa: E402


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
    evento = datos.get("hook_event_name") or "SessionStart"

    try:
        movidos = recuerdos.migrar(raiz, aplicar=True)
    except OSError as e:        # permisos, archivo en uso: se avisa, no se rompe
        print(f"No se pudo mover la memoria del agente: {e}", file=sys.stderr)
        return 0

    if not movidos:
        return 0                # la carpeta local está vacía: nada que decir

    detalle = "\n".join(f"  - {p}" for p in recuerdos.pasos(movidos))
    carpeta = recuerdos.CARPETA.replace(os.sep, "/")
    resumen = (f"Memoria del agente: {len(movidos)} archivo(s) movidos a "
               f"{carpeta}/")

    print(json.dumps({
        "systemMessage": resumen,
        "hookSpecificOutput": {
            "hookEventName": evento,
            "additionalContext": (
                f"[Memoria del agente — movida al repositorio]\n{detalle}\n\n"
                f"La memoria vive en `{carpeta}/` del proyecto, versionada, un "
                f"archivo por recuerdo (`01·C19`). La carpeta local de la "
                f"herramienta queda vacía: no escribir nada ahí, ni siquiera un "
                f"puntero. Agregar la línea del recuerdo al índice "
                f"`{carpeta}/{recuerdos.INDICE}`, y si algún nombre terminó en "
                f"`-local` decidir con el usuario cuál manda."),
        },
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
