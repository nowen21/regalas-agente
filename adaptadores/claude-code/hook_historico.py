#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganches de Claude Code que escriben el histórico de la sesión.

Se conectan en `.claude/settings.json`:

    UserPromptSubmit -> python hook_historico.py --modo usuario --raiz <proyecto>
    Stop             -> python hook_historico.py --modo agente  --raiz <proyecto>

El primero anota el mensaje del usuario apenas lo envía; el segundo anota la
respuesta del agente apenas termina. Entre los dos, la transcripción queda
completa sin que nadie tenga que acordarse de escribirla.

El de `UserPromptSubmit` hace algo más: cuando el archivo todavía se llama
`AAAA-MM-DD-sesion.md` y la sesión ya tuvo una respuesta, escribe en la salida
el recordatorio de ponerle el tema al nombre. Claude Code le pasa al agente lo
que este enganche imprime, así que el recordatorio le llega en ese turno. Se
pide una sola vez por sesión y lo aprueba el usuario: el enganche no renombra
nada por su cuenta.

Sin `--raiz` usa el `cwd` que manda Claude Code, así que el mismo archivo sirve
para cualquier proyecto que tenga carpeta `historico-chat/`. El que no la tenga
no se ve afectado: el enganche sale sin hacer nada.

Siempre sale con código 0. Un histórico que no se pudo escribir es un problema;
una sesión que no arranca por eso, uno peor.
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

import historico                        # noqa: E402
from comun import preparar_salida       # noqa: E402


def opcion(argv, nombre, por_defecto=""):
    if nombre in argv:
        i = argv.index(nombre)
        if i + 1 < len(argv):
            return argv[i + 1]
    return por_defecto


def _entrada():
    """El JSON que manda Claude Code, leído como UTF-8 sí o sí.

    Se leen bytes y se decodifica a mano en vez de `json.load(sys.stdin)`: en
    Windows la entrada estándar usa la codificación de la consola, y un mensaje
    con tildes llegaba al histórico como `abrÃ­`. Lo mandan siempre en UTF-8.
    """
    try:
        crudo = sys.stdin.buffer.read()
    except (AttributeError, ValueError):
        crudo = (sys.stdin.read() or "").encode("utf-8", "replace")
    try:
        return json.loads(crudo.decode("utf-8", "replace"))
    except (json.JSONDecodeError, ValueError):
        return None


def main():
    preparar_salida()
    argv = sys.argv[1:]
    modo = opcion(argv, "--modo", "usuario")

    datos = _entrada()
    if datos is None:
        return 0                        # sin JSON no hay nada que anotar

    raiz = opcion(argv, "--raiz") or datos.get("cwd") or os.getcwd()
    raiz = os.path.abspath(raiz)
    sesion = datos.get("session_id") or ""

    try:
        if modo == "agente":
            historico.anotar_agente(raiz, sesion, datos.get("transcript_path", ""))
        else:
            ruta = historico.anotar_usuario(raiz, sesion, datos.get("prompt", ""))
            aviso = historico.aviso_de_nombre(ruta)
            if aviso:
                print(aviso)
    except Exception as e:               # noqa: BLE001 — nunca romper la sesión
        print(f"No se pudo escribir el histórico: {e}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
