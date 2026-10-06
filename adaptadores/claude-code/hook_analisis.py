#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganche del análisis en curso: la conversación pasa sola al análisis prendido.

    python hook_analisis.py --modo mensaje --raiz "C:/ruta/del/proyecto"
    python hook_analisis.py --modo cierre  --raiz "C:/ruta/del/proyecto"

- **`--modo mensaje`** (`UserPromptSubmit`): lee con qué palabra abre el
  mensaje. «Analicemos: el pendiente N» prende, «Pare» pausa y «Apruebo el
  análisis» pone la marca. Después le dice al agente a qué análisis entra la
  conversación, o que ninguno está prendido.
- **`--modo cierre`**: pasa la conversación al análisis prendido, y lo apaga
  cuando ya está aprobado y la respuesta entró. El instalador ya no lo
  registra en `Stop`: lo hace `hook_historico.py` apenas escribe la
  respuesta, para que no corran a la vez. Queda para las instalaciones que
  todavía lo llaman.

**Vive en el adaptador, no en `validadores/`.** Acá solo está lo que habla con
esta herramienta; el trabajo está en
`proyectos/cimiento/core/enganches/analisis_en_curso.py`, que guarda un estado
por sesión: la sesión se reconoce por su transcripción.

Sale siempre con código 0: un enganche que pasa la conversación no puede
costarle el turno a nadie.
"""
import datetime
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "proyectos", "cimiento"))

from core.comun.consola import preparar_salida                 # noqa: E402
from core.enganches.analisis_en_curso import AnalisisEnCurso   # noqa: E402
from core.enganches.historico import Historico                 # noqa: E402


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


def _avisar_lo_resuelto(raiz):
    """El aviso a los proyectos sale cuando el análisis aprobado cierra su reporte,
    si Cimiento ya lo comprobó en el proyecto (análisis 1 del pendiente 110,
    acuerdo 7). Solo desde el estándar."""
    if os.path.normcase(os.path.abspath(raiz)) != os.path.normcase(os.path.abspath(RAIZ)):
        return ""
    try:
        from core.enganches.aviso_resuelto import AvisoResuelto
        version_txt = os.path.join(raiz, "VERSION")
        version = open(version_txt, encoding="utf-8").read().strip() if os.path.isfile(version_txt) else ""
        escritos, sin_entregar = AvisoResuelto(raiz).avisar(datetime.date.today().isoformat(), version)
    except Exception as error:      # noqa: BLE001 — el aviso no puede tumbar la aprobación
        return "; el aviso de resuelto no salió: %s" % error
    partes = []
    if escritos:
        partes.append("aviso de resuelto en %s" % ", ".join(escritos))
    if sin_entregar:
        partes.append("sin aviso: " + "; ".join("%s (%s)" % (os.path.basename(c), p) for c, p in sin_entregar))
    return ("; " + "; ".join(partes)) if partes else ""


def mensaje(raiz, entrada):
    """Aplica la palabra del mensaje y devuelve el aviso para el agente."""
    texto = entrada.get("prompt", "") or ""
    transcripcion = Historico(raiz).archivo_de_sesion(entrada.get("session_id") or "")
    curso = AnalisisEnCurso(raiz, transcripcion)
    curso.esperar(transcripcion)
    turno = curso.ultimo_turno(transcripcion)
    # El análisis aprobado que quedó prendido se cierra aquí: la respuesta al
    # turno que lo aprobó ya está en la transcripción.
    curso.pasar()
    curso.borrar_corrija()
    limpio = curso.limpio(texto)
    nota = ""
    if limpio.startswith("corrija"):
        curso.marcar_corrija(turno)
        nota = ("«Corrija»: en esta respuesta se pueden corregir las herramientas del proceso "
                "(validadores/, adaptadores/) sin abrir análisis; lo corregido se anota en el resumen "
                "de la sesión (02·F8)")

    numero = curso.pendiente_pedido(texto)
    if numero is not None and transcripcion:
        _, nota = curso.prender(numero, transcripcion, turno, curso.turno_pedido(texto))
    elif limpio.startswith("pare"):
        if curso.pausar(turno):
            nota = "pausado en el turno %d" % turno
    elif limpio.startswith("apruebo el analisis"):
        faltan = curso.por_que_no_se_aprueba()
        if faltan:
            nota = "no se aprobó: " + "; ".join(faltan)
        elif curso.aprobar(turno, datetime.date.today().isoformat()):
            nota = "marca de aprobado puesta en el turno %d; se apaga al terminar esta respuesta" % turno
            nota += _avisar_lo_resuelto(raiz)
    return curso.aviso(nota)


def main():
    preparar_salida()
    entrada = _entrada()
    raiz = os.path.abspath(opcion(sys.argv[1:], "--raiz") or entrada.get("cwd") or os.getcwd())
    modo = opcion(sys.argv[1:], "--modo", "mensaje")
    try:
        if modo == "cierre":
            transcripcion = Historico(raiz).archivo_de_sesion(entrada.get("session_id") or "")
            AnalisisEnCurso(raiz, transcripcion).pasar()
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
