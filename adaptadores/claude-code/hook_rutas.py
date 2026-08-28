#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""`EP-005·HU-018` · Avisa, al escribir, si el archivo cayó fuera del proyecto.

Lo que habla con esta herramienta; el trabajo vive en `validadores/rutas_fuera.py`.

**Nunca detiene la escritura.** Un enganche que bloquea el trabajo se
desinstala el mismo día, y entonces no queda nada avisando. Cualquier problema
de este guion termina en silencio y código 0.

**No ve lo que se escribe por `Bash`.** La herramienta le pasa la ruta de
`Write` y `Edit`; una redirección dentro de un comando no la trae. Está dicho
en el §3.3 de la historia para que la cobertura no se lea de más.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "validadores"))

import rutas_fuera                                       # noqa: E402
from comun import RAIZ, preparar_salida                  # noqa: E402


def raiz_pedida(argv):
    """La carpeta del proyecto: `--raiz X`, o el estándar si no se indica."""
    if "--raiz" in argv:
        i = argv.index("--raiz")
        if i + 1 < len(argv):
            return os.path.abspath(argv[i + 1])
    return RAIZ


def archivo_editado(datos):
    """La ruta escrita, mirando primero la entrada y luego la respuesta."""
    entrada = datos.get("tool_input") or {}
    respuesta = datos.get("tool_response") or {}
    return (entrada.get("file_path")
            or respuesta.get("filePath")
            or respuesta.get("file_path")
            or "")


def main():
    preparar_salida()
    raiz = raiz_pedida(sys.argv[1:])

    try:
        datos = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0            # sin JSON válido no hay ruta que mirar

    if not isinstance(datos, dict):
        return 0

    try:
        texto = rutas_fuera.aviso(archivo_editado(datos), raiz)
    except Exception:       # noqa: BLE001
        # **Deliberado.** Lo que este guion protege es una convención de orden;
        # lo que arriesga si revienta es la sesión entera del usuario. Ante
        # cualquier cosa que no se previó, callar sale más barato.
        return 0

    if texto:
        print(texto)
    return 0


if __name__ == "__main__":
    sys.exit(main())
