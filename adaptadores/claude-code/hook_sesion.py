#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganche `SessionStart` de Claude Code — revisa el estándar y avisa cómo quedó.

    python hook_sesion.py --raiz "C:/ruta/del/proyecto"

Hace dos cosas, y conviene no confundirlas:

  - **Avisa:** revisa que el estándar esté bien puesto (`sesion.py`) y devuelve
    un `systemMessage` que Claude Code le muestra al usuario.
  - **Carga:** mete en el contexto del agente lo que la sesión nueva no tiene
    forma de saber sola — antes dependía de que se acordara de leerlo:
      · cómo le llegan las reglas (`cargador.py`), o el gate `F13` si el
        proyecto no tiene su estructura base;
      · la memoria del proyecto (`recuerdos.py`), que dejó de vivir en la
        herramienta y por eso ya no la carga nadie;
      · el índice del histórico (`historico.py`): qué se habló en cada sesión
        anterior. Un chat nuevo arranca sin memoria de los anteriores, y sin el
        índice no sabe siquiera que existen.

**Las reglas no van acá.** Llegan con cada mensaje, por `hook_reglas.py`. Hasta
la 39.3.1 este enganche mandaba `00` y `01` enteros, unos 86.000 caracteres, y
la herramienta los guardaba fuera del repositorio (`EP-005 · HU-009 · CA-04`).

En el propio estándar se carga lo mismo que en un proyecto y no se revisa la
instalación, porque ahí no hay ninguna. El gate `F13` tampoco se le aplica: no
es un proyecto, es donde viven las reglas.

Siempre sale con código 0: esto **informa**, no bloquea — una sesión que no
arranca porque falta una sección del `CLAUDE.md` sería peor que el problema
que resuelve.
"""
import json
import os
import sys

# **Vive en el adaptador, no en `core/`.** Por eso tiene que decir
# dónde están los módulos que usa: el trabajo es agnóstico y sigue allá;
# acá sólo está lo que habla con esta herramienta.
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "proyectos", "cimiento"))

from core.comun import Proyecto                                  # noqa: E402
from core.comun.consola import preparar_salida, raiz_pedida                   # noqa: E402
from core.enganches import historico, recuerdos                  # noqa: E402
from core.enganches.cargador import Cargador                     # noqa: E402
from core.enganches.historico import Historico                   # noqa: E402
from core.enganches.recuerdos import Recuerdos                   # noqa: E402
from core.enganches.sesion import ArranqueDeSesion               # noqa: E402
from core.herramientas.instalar import Instalador                # noqa: E402

# El tope del canal, **en caracteres**. Lo que un enganche entregue por encima
# de 10.000, la herramienta lo guarda en un archivo fuera del repositorio y le
# deja al agente un avance de 2.000, sin pedirle que lea el resto
# (documentación de Claude Code, `hooks.md`, sección «JSON output»). El límite
# es por enganche y no se puede subir.
#
# Hasta la 39.3.1 este número era 72 KB, sacado de una medición del
# 2026-09-15 que creyó el corte cerca de 80 KB. Todo arranque desde entonces
# llegó cortado.
TOPE_DEL_CANAL = 10_000

# Lo que se aparta para el aviso de lo que no cupo, que va al final.
RESERVA_AVISOS = 600


def _ruta(modulo):
    """Dónde está el índice entero que ese módulo recorta."""
    return f"{modulo.CARPETA}/{modulo.INDICE}".replace(os.sep, "/")


def _relativo(ruta):
    """Ruta relativa al estándar; absoluta si el archivo vive fuera de él, o si
    «Rutas en los avisos» dice completas (`EP-025·HU-014`)."""
    return Proyecto(RAIZ).mostrar(ruta)


def _linea(h):
    """`[FALLA] ruta:línea — mensaje`."""
    rel = _relativo(h.archivo)
    donde = f"{rel}:{h.linea}" if h.linea else rel
    return f"[{h.severidad}] {donde} — {h.mensaje}"


def _memoria(proyecto, tope=None):
    return Recuerdos(proyecto).contexto(tope=tope)


def _historico(proyecto, tope=None):
    return Historico(proyecto).contexto(tope=tope)


def _del_proyecto(proyecto, disponible):
    """La memoria y el índice del histórico, recortados a `disponible`.

    Devuelve `(texto, avisos)`. Va primero la memoria, porque trae las
    preferencias del usuario; el histórico toma lo que quede. Nunca rompe el
    arranque.
    """
    partes, avisos = [], []
    for nombre, cargar, donde, modulo in (
            ("la memoria", _memoria, _ruta(recuerdos), "recuerdos"),
            ("el índice del histórico", _historico, _ruta(historico), "historico")):
        try:
            entero = cargar(proyecto)
            texto = entero
            if len(entero) > disponible:
                texto = cargar(proyecto, tope=disponible)
                avisos.append(f"{nombre} se recortó para caber; completa, en "
                              f"`{donde}`")
        except Exception as e:  # noqa: BLE001 — nunca romper el arranque
            texto = f"[No se pudo cargar {modulo}: {e}]"
        if texto:
            partes.append(texto)
            disponible -= len(texto) + 2
    return "\n\n".join(partes), avisos


def main():
    preparar_salida()
    proyecto = raiz_pedida(sys.argv[1:], os.getcwd())

    # El propio estándar no se revisa a sí mismo como si fuera un proyecto,
    # y no se le aplica el gate `F13`, que es para proyectos.
    if os.path.normcase(proyecto) == os.path.normcase(RAIZ):
        _responder("", [], _reglas(True), proyecto)
        return 0

    try:
        hallazgos = ArranqueDeSesion(proyecto, estandar=RAIZ).revisar()
    except Exception as e:      # noqa: BLE001 — nunca romper el arranque
        _responder(f"No se pudo revisar el arranque del estándar: {e}", [],
                   "", proyecto)
        return 0

    # Lo de las reglas va aunque la revisión encuentre fallas: un CLAUDE.md
    # desactualizado no es motivo para trabajar sin saber cómo llegan. La
    # excepción es F13, que es un gate — ahí `cargador` decide qué dar.
    _responder(ArranqueDeSesion.resumen(proyecto, hallazgos), hallazgos,
               _reglas(Instalador.cumple_f13(proyecto)), proyecto)
    return 0


def _reglas(gate_ok):
    """Cómo llegan las reglas, o el gate. Nunca rompe el arranque."""
    try:
        return Cargador.contexto(RAIZ, gate_ok)
    except Exception as e:      # noqa: BLE001 — nunca romper el arranque
        return f"[No se pudo decir cómo llegan las reglas: {e}]"


def armar(resumen, hallazgos, reglas, proyecto):
    """`(contexto, avisos)`: lo que se le inyecta al agente, dentro del tope.

    Va en orden de prioridad, y lo que no cabe se recorta desde el final: la
    revisión o el gate, cómo llegan las reglas, la memoria, el histórico.
    """
    partes = []
    if resumen:
        detalle = "\n".join(f"  - {_linea(h)}" for h in hallazgos)
        partes.append(f"[Revisión de arranque del estándar]\n{resumen}"
                      + (f"\n{detalle}" if detalle else ""))
    if reglas:
        partes.append(reglas)
    fijo = "\n\n".join(partes)

    disponible = TOPE_DEL_CANAL - RESERVA_AVISOS - len(fijo) - 2
    del_proyecto, avisos = _del_proyecto(proyecto, max(disponible, 0))
    contexto = "\n\n".join(p for p in (fijo, del_proyecto) if p)

    # La última comprobación es sobre lo que de verdad se manda, ya armado.
    exceso = len(contexto) - (TOPE_DEL_CANAL - RESERVA_AVISOS)
    if exceso > 0:
        avisos.append(
            f"el arranque quedó {exceso} caracteres por encima del tope del "
            "canal y la herramienta guarda el resto fuera del repositorio. "
            f"Leer con Read `{_ruta(recuerdos)}` y reportarlo (`02·F24`)")
    return contexto, avisos


def _responder(resumen, hallazgos, reglas, proyecto):
    """Sale por dos canales, a propósito.

    `systemMessage` lo muestra Claude Code al usuario. `additionalContext` se
    lo inyecta al agente. Van los dos porque el primero depende de que la
    interfaz lo dibuje, y si no lo dibuja el aviso se pierde sin dejar rastro
    — que es justo el problema que este enganche vino a resolver. Con el
    segundo, el agente lo sabe y puede decirlo aunque el banner no aparezca.

    **Lo que no cupo se dice por los dos canales.** Un recorte silencioso deja
    al agente creyendo que tiene lo que no tiene.
    """
    contexto, avisos = armar(resumen, hallazgos, reglas, proyecto)

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
