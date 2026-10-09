#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganche de Claude Code que copia el veredicto de la fase — `EP-005 · HU-003`, fase C.

Se conecta en `.claude/settings.json`:

    PostToolUse (Write|Edit) -> python hook_veredicto.py --raiz <proyecto>

Cuando el archivo escrito es el `resultado_pruebas.md` de una fase y su §6
ya tiene concepto, `proyectos/cimiento/core/enganches/veredicto.py` deja ese veredicto en la fila de
la historia y en los dos README, y acá se dice qué se tocó. Si no hay dónde
copiarlo, se dice también: callar se leería como hecho.

**No toca el `estado-fase.md`**: es el checkpoint, y lo escribe el agente.

Siempre sale con código 0.
"""
import datetime
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "proyectos", "cimiento"))

from core.comun import Proyecto                                  # noqa: E402
from core.comun.consola import archivo_editado, entrada_json, preparar_salida, raiz_pedida     # noqa: E402
from core.enganches.veredicto import CopiaDelVeredicto           # noqa: E402


def main():
    # `EP-025·HU-032` · Si este momento está suspendido en Cimiento, sale sin hacer nada.
    from core.enganches.suspendidos import salir_si_esta_suspendido
    salir_si_esta_suspendido(__file__)
    preparar_salida()
    raiz = raiz_pedida(sys.argv[1:], os.getcwd())
    try:
        datos = entrada_json()
    except (json.JSONDecodeError, ValueError):
        return 0
    if not isinstance(datos, dict):
        return 0
    ruta = archivo_editado(datos)
    if not ruta or os.path.basename(ruta) != CopiaDelVeredicto.RESULTADO:
        return 0
    try:
        tocados, avisos = CopiaDelVeredicto.propagar(ruta, datetime.date.today().isoformat())
    except Exception as e:                                  # noqa: BLE001
        print(f"[el enganche del veredicto no pudo correr: {e}]")
        return 0

    def rel(p):
        # Como diga «Rutas en los avisos» del proyecto (`EP-025·HU-014`).
        return Proyecto(raiz).mostrar(p)
    if tocados:
        print("[EL VEREDICTO DE LA FASE SE COPIÓ A] " + " · ".join(rel(t) for t in tocados))
    for a in avisos:
        print("[EL VEREDICTO NO TIENE DÓNDE COPIARSE] " + a)
    return 0


if __name__ == "__main__":
    sys.exit(main())
