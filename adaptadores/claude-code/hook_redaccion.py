#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganche de cierre: mide cómo quedó escrito lo que el agente acaba de decir.

Se conecta como hook `Stop` en `.claude/settings.json`.

**Por qué existe** (`EP-005·HU-012`). Tres reglas del núcleo hablan de cómo
escribe el agente, y ninguna tenía quien la hiciera cumplir: `00·ID8` las marcas
de escritura automática, `00·ID9` cuánto ocupa la respuesta, y `00·ID10` la
persona y la forma verbal. Dependían de que el agente se acordara, y la evidencia
de que eso no basta está contada: el usuario pidió «menos es más» siete veces en
tres días, y cada vez se anotó el caso sin que cambiara nada.

**Mide y no detiene**, y eso es deliberado. Cuando este enganche corre, el texto
ya salió: no hay nada que bloquear. Lo que sí puede hacer es **dejarlo a la
vista**, que es lo que la historia acepta como forma de hacer cumplir cuando no
hay forma de impedir.

**Se calla cuando todo está bien.** Un aviso que sale en cada turno deja de
leerse a la tercera, y entonces tampoco se lee el que sí importaba.

Códigos de salida:
  0 — siempre. Este enganche nunca rompe la sesión ni devuelve nada al modelo.
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "proyectos", "cimiento"))

from core.comun.consola import entrada_json, preparar_salida, raiz_pedida     # noqa: E402
from core.enganches.historico import Historico, Transcript       # noqa: E402
from core.validadores.brevedad import Respuestas                 # noqa: E402
from core.validadores.redaccion import Redaccion                 # noqa: E402


def _mediana_de_la_sesion(raiz, sesion):
    """Cuánto ocupa una respuesta típica de esta sesión, o 0 si no se sabe.

    Sirve para no reclamar por el largo en abstracto: lo que importa no es que
    una respuesta sea larga, sino que **se salga de lo que esta conversación
    viene siendo**.
    """
    try:
        archivo = Historico(raiz).archivo(sesion, crear=False)
        if not archivo:
            return 0
        return Respuestas.resumen(archivo).get("mediana", 0)
    except Exception:                     # noqa: BLE001 — nunca romper el cierre
        return 0


def main():
    # `EP-025·HU-032` · Si este momento está suspendido en Cimiento, sale sin hacer nada.
    from core.enganches.suspendidos import salir_si_esta_suspendido
    salir_si_esta_suspendido(__file__)
    preparar_salida()
    raiz = raiz_pedida(sys.argv[1:], RAIZ)

    try:
        datos = entrada_json()
    except (json.JSONDecodeError, ValueError):
        return 0

    try:
        texto, _marca = Transcript.ultima_respuesta(
            datos.get("transcript_path", ""))
        if not texto:
            return 0
        mediana = _mediana_de_la_sesion(raiz, datos.get("session_id") or "")
        linea = Redaccion.linea_de_cierre(texto, mediana)
        if linea:
            print(linea)
    except Exception:                     # noqa: BLE001
        pass                              # medir no puede costarle el turno a nadie
    return 0


if __name__ == "__main__":
    sys.exit(main())
