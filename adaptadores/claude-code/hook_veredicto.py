#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganche de Claude Code que copia el veredicto de la fase — `EP-005 · HU-003`, fase C.

Se conecta en `.claude/settings.json`:

    PostToolUse (Write|Edit) -> python hook_veredicto.py --raiz <proyecto>

Cuando el archivo escrito es el `resultado_pruebas.md` de una fase y su §6
ya tiene concepto, `validadores/veredicto.py` deja ese veredicto en la fila de
la historia y en los dos README, y acá se dice qué se tocó. Si no hay dónde
copiarlo, se dice también: callar se leería como hecho.

**No toca el `estado-fase.md`**: es el checkpoint, y lo escribe el agente.

Siempre sale con código 0.
"""
import datetime
import json
import os
import sys

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "validadores"))
import veredicto                        # noqa: E402
from comun import preparar_salida       # noqa: E402


def raiz_pedida(argv):
    if "--raiz" in argv:
        i = argv.index("--raiz")
        if i + 1 < len(argv):
            return os.path.abspath(argv[i + 1])
    return os.path.abspath(os.getcwd())


def archivo_editado(datos):
    entrada = datos.get("tool_input") or {}
    respuesta = datos.get("tool_response") or {}
    return (entrada.get("file_path") or respuesta.get("filePath")
            or respuesta.get("file_path") or "")


def main():
    preparar_salida()
    raiz = raiz_pedida(sys.argv[1:])
    try:
        datos = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    if not isinstance(datos, dict):
        return 0
    ruta = archivo_editado(datos)
    if not ruta or os.path.basename(ruta) != veredicto.RESULTADO:
        return 0
    try:
        tocados, avisos = veredicto.propagar(ruta, datetime.date.today().isoformat())
    except Exception as e:                                  # noqa: BLE001
        print(f"[el enganche del veredicto no pudo correr: {e}]")
        return 0

    def rel(p):
        try:
            return os.path.relpath(p, raiz).replace("\\", "/")
        except ValueError:
            return p
    if tocados:
        print("[EL VEREDICTO DE LA FASE SE COPIÓ A] " + " · ".join(rel(t) for t in tocados))
    for a in avisos:
        print("[EL VEREDICTO NO TIENE DÓNDE COPIARSE] " + a)
    return 0


if __name__ == "__main__":
    sys.exit(main())
