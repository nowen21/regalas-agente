#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganche que recuerda escribir la señal en el momento en que aparece.

Se conecta en `.claude/settings.json`:

    UserPromptSubmit -> python hook_senales.py --raiz <proyecto>

**Por qué existe.** [`13·DOC5`](../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)
manda registrar como señal lo que no se recupera del código, y el archivo donde
escribirlas no existió en este repositorio hasta el 2026-08-14 — después de una
sesión entera de la que casi todo lo aprendido se quedó en la transcripción.

Es la misma lección del histórico y del resumen: **lo que depende de que alguien
se acuerde, no pasa.** El histórico dejó de perderse cuando lo escribió un
programa; el resumen, cuando un enganche lo creó y avisó de lo que le faltaba.

**Al cerrar la sesión no sirve.** Un chat no tiene final: nadie sabe cuál fue el
último mensaje hasta mucho después. Por eso el aviso va en el turno, no al final.

**Lo que este enganche NO hace, y es deliberado.** No escribe señales ni decide
qué merece serlo — eso es criterio y es del agente. Tampoco repite el aviso en
cada turno, que es la forma más rápida de que se deje de leer: avisa **una sola
vez por sesión**, y solo cuando el archivo existe y la sesión ya produjo algo.

Siempre sale con código 0. Un enganche que detiene el trabajo es peor que el
problema que resuelve.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import comun                                        # noqa: E402
from comun import RAIZ, leer, preparar_salida       # noqa: E402

ARCHIVO = "documentacion/senales.md"

# La marca queda dentro del propio archivo de señales, no en un temporal: un
# aviso que se olvida al reiniciar vuelve a salir, y volver a salir es lo que lo
# vuelve ruido. Va en un comentario que no se ve al leer el documento.
MARCA = "<!-- avisado: %s -->"

_AVISO = """[LA SEÑAL SE ESCRIBE CUANDO APARECE, NO AL CERRAR]
Lo que se decidió, lo que costó averiguar y lo que no se recupera leyendo el
código va a `%s` — con el molde corto: **qué pasó · por qué importa · qué se
decidió · dónde queda**.

No es al final de la sesión: un chat no tiene final. Se escribe en el momento.

Lo que **falta hacer** no es una señal: eso va a `pendientes/`. Los dos salen
del mismo momento y por eso se confunden."""


def _sesion(argv=None):
    """El identificador de sesión que la herramienta pasa por el entorno."""
    return os.environ.get("CLAUDE_SESSION_ID", "")


def ya_avisado(texto, sesion):
    return bool(sesion) and (MARCA % sesion) in texto


def marcar(ruta, texto, sesion):
    """Deja constancia de que esta sesión ya recibió el aviso."""
    if not sesion:
        return
    try:
        with open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto.rstrip("\n") + "\n\n" + (MARCA % sesion) + "\n")
    except OSError:
        pass                    # sin permiso o sin espacio: el aviso no detiene


def aviso(raiz, sesion):
    """El texto a mostrar, o "" si no hay nada que decir."""
    ruta = os.path.join(raiz, *ARCHIVO.split("/"))
    if not os.path.isfile(ruta):
        return ""               # el proyecto no lleva señales: no se inventa
    try:
        texto = leer(ruta)
    except OSError:
        return ""
    if ya_avisado(texto, sesion):
        return ""
    marcar(ruta, texto, sesion)
    return _AVISO % ARCHIVO


def main():
    preparar_salida()
    p = argparse.ArgumentParser(
        description="Recuerda escribir la señal en el momento en que aparece.")
    p.add_argument("--raiz", default=RAIZ, help="carpeta del proyecto")
    a = p.parse_args()

    texto = aviso(os.path.abspath(a.raiz), _sesion())
    if texto:
        print(texto)
    return 0


if __name__ == "__main__":
    sys.exit(main())
