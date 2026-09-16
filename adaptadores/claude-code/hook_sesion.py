#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganche `SessionStart` de Claude Code — carga el estándar y avisa cómo quedó.

    python hook_sesion.py --raiz "C:/ruta/del/proyecto"

Hace dos cosas, y conviene no confundirlas:

  - **Avisa:** revisa que el estándar esté bien puesto (`sesion.py`) y devuelve
    un `systemMessage` que Claude Code le muestra al usuario.
  - **Carga:** mete en el contexto del agente lo que la sesión nueva no tiene
    forma de saber sola — antes dependía de que se acordara de leerlo:
      · las reglas base (`cargador.py`);
      · la memoria del proyecto (`recuerdos.py`), que dejó de vivir en la
        herramienta y por eso ya no la carga nadie;
      · el índice del histórico (`historico.py`): qué se habló en cada sesión
        anterior. Un chat nuevo arranca sin memoria de los anteriores, y sin el
        índice no sabe siquiera que existen.

En el propio estándar se carga lo mismo que en un proyecto —las reglas, la
memoria y el histórico— y no se revisa la instalación, porque ahí no hay
ninguna. Hasta la 27.1.0 la carpeta del estándar recibía memoria e histórico
y **ninguna regla**: 30 de 30 aperturas medidas. El gate `F13` tampoco se le
aplica: no es un proyecto, es donde viven las reglas (`EP-005 · HU-009`).

Siempre sale con código 0: esto **informa**, no bloquea — una sesión que no
arranca porque falta una sección del `CLAUDE.md` sería peor que el problema
que resuelve.
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

import cargador                                 # noqa: E402
import historico                                # noqa: E402
import instalar                                 # noqa: E402
import recuerdos                                # noqa: E402
import sesion                                   # noqa: E402
from comun import RAIZ, preparar_salida         # noqa: E402

# El tope del canal, en bytes. **Pasarse no recorta: tira el paquete entero.**
#
# Medido el 2026-09-15 en `master-ciberseguridad`: un `additionalContext` de
# 82,4 KB no llegó al agente. La herramienta lo guardó en un archivo, le dejó
# 2 KB de vista previa y no dijo que hubiera perdido nada; el banner siguió
# diciendo «Estándar cargado» y la sesión trabajó sin reglas.
#
# **El número exacto del límite no está documentado.** Lo que se sabe es lo
# medido: 82,4 KB no pasaron, y la herramienta reportó el corte en 80,5. Así
# que el tope queda un 10% por debajo de ahí, que es margen y no frontera.
#
# **No se puede apretar más de lo que pesan las reglas.** Solas ocupan 62,3 KB,
# y son lo único que no se recorta: un tope por debajo de eso obligaría a
# botar el índice en cada arranque sin necesidad. Si el paquete vuelve a
# perderse por tamaño, se baja este número y se recortará el índice solo.
TOPE_DEL_CANAL = 72 * 1024


def raiz_pedida(argv):
    if "--raiz" in argv:
        i = argv.index("--raiz")
        if i + 1 < len(argv):
            return os.path.abspath(argv[i + 1])
    return os.path.abspath(os.getcwd())


def _del_proyecto(proyecto):
    """La memoria y el índice del histórico. Nunca rompe el arranque."""
    partes = []
    for cargar in (recuerdos.contexto, historico.contexto):
        try:
            texto = cargar(proyecto)
        except Exception as e:  # noqa: BLE001 — nunca romper el arranque
            texto = f"[No se pudo cargar {cargar.__module__}: {e}]"
        if texto:
            partes.append(texto)
    return "\n\n".join(partes)


def main():
    preparar_salida()
    proyecto = raiz_pedida(sys.argv[1:])
    del_proyecto = _del_proyecto(proyecto)

    # El propio estándar no se revisa a sí mismo como si fuera un proyecto,
    # pero recibe las reglas igual que cualquiera —sin el gate `F13`, que es
    # para proyectos— más su memoria y su histórico, que son los del usuario.
    if os.path.normcase(proyecto) == os.path.normcase(RAIZ):
        reglas, avisos = _reglas(True, del_proyecto)
        _responder("", [], f"{reglas}\n\n{del_proyecto}" if del_proyecto else reglas,
                   avisos)
        return 0

    try:
        hallazgos = sesion.revisar(proyecto, RAIZ)
    except Exception as e:      # noqa: BLE001 — nunca romper el arranque
        _responder(f"No se pudo revisar el arranque del estándar: {e}", [],
                   del_proyecto)
        return 0

    # Las reglas se cargan aunque la revisión encuentre fallas: un CLAUDE.md
    # desactualizado no es motivo para trabajar sin reglas. La excepción es
    # F13, que es un gate — ahí `cargador` decide solo qué corresponde dar.
    reglas, avisos = _reglas(instalar.cumple_f13(proyecto), del_proyecto)

    _responder(sesion.resumen(proyecto, hallazgos), hallazgos,
               f"{reglas}\n\n{del_proyecto}" if del_proyecto else reglas,
               avisos)
    return 0


def _reglas(gate_ok, del_proyecto):
    """Las reglas recortadas a lo que cabe, y los avisos de lo que no cupo.

    **El tope se le descuenta lo que viaja al lado.** La memoria y el índice
    del histórico van en el mismo `additionalContext`, así que medir solo las
    reglas contra el tope dejaría pasar un paquete que igual se pierde. Eso es
    exactamente lo que ocurrió el 2026-09-15: las reglas pesaban 62,3 KB y lo
    que se perdió fueron los 82,4 del total.
    """
    margen = TOPE_DEL_CANAL - len(del_proyecto.encode("utf-8")) - 1024
    try:
        return cargador.paquete(RAIZ, gate_ok, max(margen, 8 * 1024))
    except Exception as e:      # noqa: BLE001 — nunca romper el arranque
        return f"[No se pudieron cargar las reglas base: {e}]", []


def _responder(resumen, hallazgos, reglas, avisos=()):
    """Sale por dos canales, a propósito.

    `systemMessage` lo muestra Claude Code al usuario. `additionalContext` se
    lo inyecta al agente. Van los dos porque el primero depende de que la
    interfaz lo dibuje, y si no lo dibuja el aviso se pierde sin dejar rastro
    — que es justo el problema que este enganche vino a resolver. Con el
    segundo, el agente lo sabe y puede decirlo aunque el banner no aparezca.

    Las reglas van **solo** por `additionalContext`. En `systemMessage` serían
    decenas de KB de banner en la pantalla del usuario.

    **Lo que no cupo sí se dice por los dos canales.** Un recorte silencioso es
    el defecto del 2026-09-15 otra vez: el banner decía que todo estaba
    cargado mientras el paquete se perdía. Un aviso que nadie ve no es un
    aviso.
    """
    partes = []
    if resumen:
        detalle = "\n".join(f"  - {h}" for h in hallazgos)
        partes.append(f"[Revisión de arranque del estándar]\n{resumen}"
                      + (f"\n{detalle}" if detalle else ""))
    if reglas:
        partes.append(reglas)
    contexto = "\n\n".join(partes)

    # La última comprobación es sobre lo que de verdad se manda, ya armado.
    # Medir solo las reglas dejaba afuera el encabezado de la revisión, la
    # memoria y el histórico, que viajan en el mismo campo.
    exceso = len(contexto.encode("utf-8")) - TOPE_DEL_CANAL
    avisos = list(avisos)
    if exceso > 0:
        avisos.append(
            f"el paquete quedó {exceso // 1024 + 1} KB por encima del tope del "
            "canal y la herramienta puede descartarlo entero. Si esta sesión "
            "arranca sin reglas, es esto: leerlas con Read desde `base/00-*` y "
            "`base/01-*`, y reportarlo (`02·F24`)")

    if avisos:
        pie = "\n".join(f"  - {a}" for a in avisos)
        contexto += f"\n\n[LO QUE NO CUPO EN EL ARRANQUE]\n{pie}"
        resumen = (f"{resumen}\n" if resumen else "") + \
            "[arranque] no cupo todo en el canal:\n" + pie

    print(json.dumps({
        "systemMessage": resumen,
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": contexto,
        },
    }, ensure_ascii=False))


if __name__ == "__main__":
    sys.exit(main())
