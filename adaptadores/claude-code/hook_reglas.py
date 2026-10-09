#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganche `UserPromptSubmit`: entrega con el mensaje las reglas que le faltan.

    python hook_reglas.py --raiz "C:/ruta/del/proyecto"

**Por qué existe.** Las reglas no se cargan al abrir la sesión. Cargarlas una
vez perdía de dos maneras:

  - **El paquete no entraba.** La herramienta acepta 10.000 caracteres por
    enganche; lo demás lo guarda en un archivo fuera del repositorio y le deja
    al agente un avance de 2.000. Hasta la 39.3.1 el arranque mandaba unos
    86.000 (`EP-005 · HU-009 · CA-04`).
  - **Lo que entra se resume primero.** Llenar la ventana adelanta el resumen
    automático del contexto, y lo primero que se resume es lo que se inyectó
    al arrancar.

**Desde la `EP-005·HU-025`, con el mensaje llega solo lo que falta**
(análisis 1 del pendiente 133, acuerdos 1 y 2): las reglas de `responder`, y
las de `recibir-pedido` cuando la palabra autoriza cambiar algo, una sola vez
en la sesión, más la regla que el mensaje cita. Las de cada tarea llegan antes
de la acción, con `hook_reglas_accion.py`. El bloque «LAS REGLAS DE CADA TURNO»
salió: repetía seis reglas que `responder` ya trae.

**Y devuelve la medición.** `hook_redaccion.py` ya cuenta las marcas de lo que
el agente acaba de escribir, pero corre en `Stop` e imprime donde nadie lo ve:
ni el usuario ni el modelo. Acá esa misma cuenta se vuelve a sacar sobre la
respuesta anterior y entra al turno siguiente, que es donde todavía sirve para
corregir. Mide la misma función (`redaccion.linea_de_cierre`), así que las dos
dicen siempre lo mismo.

**Las reglas van al agente, no a la pantalla.** Es contexto, no alerta: por
eso salen por `additionalContext`. Por `systemMessage` sale **solo** la medición, y solo cuando hay algo que decir —
que es la regla de oro de los avisos de esta casa.

Sale siempre con código 0: recordar una regla no puede costarle el turno a
nadie.
"""
import json
import os
import sys

# **Vive en el adaptador, no en `core/`.** Por eso tiene que decir
# dónde están los módulos que usa: el trabajo es agnóstico y sigue allá;
# acá sólo está lo que habla con esta herramienta.
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "proyectos", "cimiento"))

from core.comun.consola import preparar_salida                       # noqa: E402
from core.enganches.historico import Transcript                      # noqa: E402
from core.herramientas.entrega_de_reglas import EntregaDeReglas      # noqa: E402
from core.validadores.redaccion import Redaccion                     # noqa: E402

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


def medicion(raiz, entrada):
    """Cómo quedó escrita la respuesta anterior, o `""` si no hay nada que decir.

    Es la misma cuenta de `hook_redaccion.py`, que corre al cerrar el turno y
    la imprime donde nadie la lee. Acá llega **al turno siguiente**, que es
    cuando todavía se puede corregir.
    """
    ruta = entrada.get("transcript_path") or ""
    if not ruta or not os.path.isfile(ruta):
        return ""
    try:
        texto, _marca = Transcript.ultima_respuesta(ruta)
        if not texto:
            return ""
        return Redaccion.linea_de_cierre(texto)
    except Exception:                     # noqa: BLE001 — medir no cuesta el turno
        return ""


def reglas_del_mensaje(entrada, raiz):
    """Las reglas que le faltan al agente con este mensaje, o `""`.

    `raiz` es la del **proyecto**: ahí se guarda lo ya entregado en la sesión, y
    de ahí salen los capítulos opt-in apagados. Las reglas salen del estándar
    (`RAIZ`).

    Nunca cuesta el turno: si la entrega falla, el turno sigue sin ella.
    """
    try:
        return EntregaDeReglas(raiz, estandar=RAIZ).para_el_mensaje(
            entrada.get("session_id") or "", entrada.get("prompt", ""))
    except Exception:                     # noqa: BLE001
        return ""


def main():
    # `EP-025·HU-032` · Si este momento está suspendido en Cimiento, sale sin hacer nada.
    from core.enganches.suspendidos import salir_si_esta_suspendido
    salir_si_esta_suspendido(__file__)
    preparar_salida()
    entrada = _entrada()
    raiz = opcion(sys.argv[1:], "--raiz") or entrada.get("cwd") or os.getcwd()
    raiz = os.path.abspath(raiz)

    partes = []
    pedidas = reglas_del_mensaje(entrada, raiz)
    if pedidas:
        partes.append(pedidas)

    cuenta = medicion(raiz, entrada)
    if cuenta:
        partes.append(
            f"[LA RESPUESTA ANTERIOR, MEDIDA]\n{cuenta}\n"
            "Corregir eso en esta respuesta, y no volver a entregarlo así.")

    if not partes:
        return 0

    salida = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": "\n\n".join(partes),
        },
    }

    # Por la pantalla del usuario sale **solo** la medición, y solo cuando hay
    # algo que decir. Las reglas son contexto del agente: como banner se
    # dejarían de leer a los dos días y se llevarían puesto el aviso que sí
    # importaba.
    if cuenta:
        salida["systemMessage"] = cuenta

    print(json.dumps(salida, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
