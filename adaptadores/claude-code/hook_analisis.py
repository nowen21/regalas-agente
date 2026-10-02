#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganche del análisis en curso: la conversación pasa sola al análisis prendido.

    python hook_analisis.py --modo mensaje --raiz "C:/ruta/del/proyecto"
    python hook_analisis.py --modo cierre  --raiz "C:/ruta/del/proyecto"

- **`--modo mensaje`** (`UserPromptSubmit`): lee con qué palabra abre el
  mensaje. «Analicemos: el pendiente N» prende, «Pare» pausa y «Apruebo el
  análisis» pone la marca. Después le dice al agente a qué análisis entra la
  conversación, o que ninguno está prendido.
- **`--modo cierre`** (`Stop`): pasa la conversación al análisis prendido, y
  lo apaga cuando ya está aprobado y la respuesta entró. Si al cerrar la
  respuesta todavía no estaba, lo apaga el mensaje siguiente.

**Vive en el adaptador, no en `validadores/`.** Acá solo está lo que habla con
esta herramienta; el trabajo está en `validadores/analisis_en_curso.py`.

Sale siempre con código 0: un enganche que pasa la conversación no puede
costarle el turno a nadie.
"""
import datetime
import json
import os
import sys

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "validadores"))

import analisis_en_curso as curso                   # noqa: E402
import historico                                    # noqa: E402
from comun import preparar_salida                   # noqa: E402


def opcion(argv, nombre, por_defecto=""):
    if nombre in argv:
        i = argv.index(nombre)
        if i + 1 < len(argv):
            return argv[i + 1]
    return por_defecto


def _entrada():
    """Lo que la herramienta manda por la entrada estándar, o `{}`."""
    try:
        crudo = sys.stdin.buffer.read()
    except (AttributeError, ValueError):
        crudo = (sys.stdin.read() or "").encode("utf-8", "replace")
    try:
        return json.loads(crudo.decode("utf-8", "replace"))
    except (json.JSONDecodeError, ValueError):
        return {}


def mensaje(raiz, entrada):
    """Aplica la palabra del mensaje y devuelve el aviso para el agente."""
    texto = entrada.get("prompt", "") or ""
    transcripcion = historico.archivo_de_sesion(raiz, entrada.get("session_id") or "")
    curso.esperar(transcripcion)
    turno = curso.ultimo_turno(transcripcion)
    # El análisis aprobado que quedó prendido se cierra aquí: la respuesta al
    # turno que lo aprobó ya está en la transcripción.
    curso.pasar(raiz)
    limpio = curso._limpio(texto)
    nota = ""

    numero = curso.pendiente_pedido(texto)
    if numero is not None and transcripcion:
        _, nota = curso.prender(raiz, numero, transcripcion, turno)
    elif limpio.startswith("pare"):
        if curso.pausar(raiz, turno):
            nota = "pausado en el turno %d" % turno
    elif limpio.startswith("apruebo el analisis"):
        if curso.aprobar(raiz, turno, datetime.date.today().isoformat()):
            nota = "marca de aprobado puesta en el turno %d; se apaga al terminar esta respuesta" % turno
    return curso.aviso(raiz, nota)


def main():
    preparar_salida()
    entrada = _entrada()
    raiz = os.path.abspath(opcion(sys.argv[1:], "--raiz") or entrada.get("cwd") or os.getcwd())
    modo = opcion(sys.argv[1:], "--modo", "mensaje")
    try:
        if modo == "cierre":
            curso.pasar(raiz)
            return 0
        texto = mensaje(raiz, entrada)
    except (OSError, ValueError) as error:
        print(f"El análisis en curso no se actualizó: {error}", file=sys.stderr)
        return 0
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "UserPromptSubmit",
        "additionalContext": texto,
    }}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
