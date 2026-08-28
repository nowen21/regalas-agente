#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""`EP-005·HU-020` · Al terminar el turno, anota lo que cambió en él.

Lo que habla con esta herramienta; el trabajo vive en `validadores/sesiones.py`.

**Por qué existe.** El registro de la sesión se llenaba solo desde las
herramientas de escritura, y la mayoría de los archivos los escriben guiones que
se corren en la terminal. Por ese hueco entraron **712 líneas de trabajo ajeno**
en un commit, con la comprobación de sesiones diciendo OK (`S-071`, `S-072`).

**Nunca rompe el turno.** Cuando esto corre, la respuesta ya se dio: lo único
que puede lograr un fallo es alarmar sin motivo. Termina en 0 pase lo que pase.

**Y no dice nada cuando no hay nada que decir.** Anotar es trabajo de fondo; un
enganche que informa en cada vuelta se vuelve ruido y se desinstala.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "validadores"))

import sesiones                                          # noqa: E402
from comun import RAIZ, preparar_salida                  # noqa: E402


def raiz_pedida(argv, datos):
    """`--raiz X`, el `cwd` que manda la herramienta, o el estándar."""
    if "--raiz" in argv:
        i = argv.index("--raiz")
        if i + 1 < len(argv):
            return os.path.abspath(argv[i + 1])
    return os.path.abspath(datos.get("cwd") or RAIZ)


def main():
    preparar_salida()
    try:
        datos = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0

    if not isinstance(datos, dict):
        return 0

    sesion = datos.get("session_id") or ""
    if not sesion:
        return 0

    try:
        sesiones.anotar_el_turno(raiz_pedida(sys.argv[1:], datos), sesion)
    except Exception:       # noqa: BLE001
        # Deliberado y declarado: lo que esto protege es que un commit no se
        # lleve trabajo ajeno; lo que arriesga si revienta es la conversación.
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
