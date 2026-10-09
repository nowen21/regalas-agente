#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganche de Claude Code que reclama el checkpoint de la fase — `EP-005 · HU-013`.

Se conecta en `.claude/settings.json`:

    PostToolUse (Write|Edit) -> python hook_checkpoint.py --raiz <proyecto>

Lee por la entrada estándar el JSON que envía la herramienta, saca la ruta del
archivo escrito y le pregunta a `proyectos/cimiento/core/enganches/checkpoint.py` si esa escritura
pasó una puerta de la fase sin su `estado-fase.md`. Si sí, imprime el aviso.
Lo que no es de puerta, o no está en una fase, se ignora en silencio.

**No escribe el checkpoint.** Decir en qué estación va la fase es criterio.

Siempre sale con código 0: un enganche que detiene el trabajo es peor que el
problema que resuelve.
"""
import json
import os
import sys

# Vive en el adaptador, no en `core/`: por eso dice dónde están los módulos
# agnósticos que usa.
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "proyectos", "cimiento"))

from core.comun.consola import archivo_editado, entrada_json, preparar_salida, raiz_pedida     # noqa: E402
from core.enganches.checkpoint import Checkpoint                 # noqa: E402


def main():
    # `EP-025·HU-032` · Si este momento está suspendido en Cimiento, sale sin hacer nada.
    from core.enganches.suspendidos import salir_si_esta_suspendido
    salir_si_esta_suspendido(__file__)
    preparar_salida()
    raiz = raiz_pedida(sys.argv[1:], os.getcwd())
    try:
        datos = entrada_json()
    except (json.JSONDecodeError, ValueError):
        return 0                        # sin JSON válido no hay nada que mirar
    if not isinstance(datos, dict):
        return 0
    ruta = archivo_editado(datos)
    if not ruta:
        return 0
    try:
        hallazgo = Checkpoint.rezago(ruta)
    except Exception as e:                                  # noqa: BLE001
        print(f"[el enganche del checkpoint no pudo correr: {e}]")
        return 0
    if hallazgo:
        print(Checkpoint.como_texto(hallazgo, raiz))
    return 0


if __name__ == "__main__":
    sys.exit(main())
