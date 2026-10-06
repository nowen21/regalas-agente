#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganche para Claude Code: revisa los enlaces tras editar un `.md`.

Se conecta como hook `PostToolUse` sobre `Write|Edit` en `.claude/settings.json`.
Lee por la entrada estándar el JSON que envía Claude Code y se lo pasa a
`proyectos/cimiento/core/enganches/md.py`, donde vive lo que hace
(`EP-025·HU-014`): anotar que la sesión tocó el archivo y, si es un `.md` del
proyecto, revisar enlaces e índices y medir las marcas de redacción de lo que
se acaba de escribir (`00·ID8`).

    python hook_md.py [--raiz <carpeta del proyecto>]

Sin `--raiz` revisa el repositorio del estándar. Con `--raiz` revisa el proyecto
indicado — así el mismo archivo sirve para todos los proyectos sin copiarse.

Códigos de salida:
  0 — todo bien, no aplicaba, o solo hay marcas: esas van por el contexto.
  2 — hay enlaces rotos; Claude Code se lo devuelve al modelo para que los
      corrija, y si hay marcas se nombran en el mismo mensaje.
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "proyectos", "cimiento"))

from core.comun.consola import entrada_json, preparar_salida, raiz_pedida  # noqa: E402
from core.enganches.md import revisar                                      # noqa: E402


def main():
    preparar_salida()
    raiz = raiz_pedida(sys.argv[1:], RAIZ)
    try:
        datos = entrada_json()
    except (json.JSONDecodeError, ValueError):
        return 0            # sin JSON válido no hay nada que revisar

    codigo, para_el_agente, error = revisar(raiz, datos)
    if para_el_agente:
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": para_el_agente}}, ensure_ascii=False))
    if error:
        print(error, file=sys.stderr)
    return codigo


if __name__ == "__main__":
    sys.exit(main())
