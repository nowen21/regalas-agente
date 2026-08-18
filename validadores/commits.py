#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Valida el mensaje de un commit contra `base/09-git.md`.

  - G2 — primera línea breve e imperativa; si hay cuerpo, va separado por una
    línea en blanco.
  - G8 — el mensaje no lleva firma de herramienta (`Co-Authored-By`, marcas de
    "generado con").

Todo lo que se comprueba aquí está escrito en la norma. Si aparece la necesidad
de exigir algo más, **primero se escribe en `09-git.md`** y después se comprueba:
un validador que hace cumplir una regla que nadie escribió bloquea trabajo por
un motivo que no se puede consultar en ninguna parte.

Lo que NO se comprueba, por no ser medible: que el cuerpo arranque con la idea
del usuario (G8). Un programa no puede distinguir la necesidad de la ejecución;
eso queda a criterio de quien escribe.
"""
import re
import subprocess

import comun
from comun import AVISO, FALLA, Hallazgo

LARGO_MAXIMO = 72

# Mensajes que no dicen nada — el ejemplo INCORRECTO de G2.
VACIOS = {
    "cambios", "cambio", "fix", "wip", "update", "actualizacion",
    "actualización", "varios", "arreglo", "arreglos", "ajustes", "ajuste",
    "commit", "misc", "temp", "prueba", "test",
}

# G8: el historial cuenta qué se decidió, no con qué se escribió.
PROHIBIDOS = [
    # `[ \t]*` y no `\s*`: `\s` incluye el salto de línea y haría que el
    # hallazgo se anclara en la línea anterior.
    (re.compile(r"^[ \t]*Co-Authored-By:", re.IGNORECASE | re.MULTILINE),
     "Co-Authored-By"),
    (re.compile(r"Generated with \[?Claude Code", re.IGNORECASE),
     "firma de herramienta"),
]


def leer_de_git(revision="HEAD"):
    """Mensaje completo de un commit ya hecho."""
    salida = subprocess.run(
        ["git", "log", "-1", "--pretty=%B", revision],
        capture_output=True, text=True, encoding="utf-8", check=True)
    return salida.stdout


def validar(mensaje, origen="(mensaje)"):
    hallazgos = []

    # Las líneas que git ignora no cuentan para nada.
    lineas = [l for l in mensaje.splitlines() if not l.startswith("#")]
    while lineas and not lineas[-1].strip():
        lineas.pop()

    if not lineas or not lineas[0].strip():
        return [Hallazgo(FALLA, origen, 1, "el mensaje está vacío")]

    asunto = lineas[0].rstrip()

    if asunto.strip().lower().rstrip(".") in VACIOS:
        hallazgos.append(Hallazgo(
            FALLA, origen, 1,
            f"asunto sin contenido: «{asunto}» — G2 pide qué y por qué"))

    if asunto.endswith("."):
        hallazgos.append(Hallazgo(
            AVISO, origen, 1, "el asunto no lleva punto final"))

    if len(asunto) > LARGO_MAXIMO:
        hallazgos.append(Hallazgo(
            AVISO, origen, 1,
            f"asunto de {len(asunto)} caracteres; G2 lo pide breve "
            f"(referencia: {LARGO_MAXIMO})"))

    # G2: si hay cuerpo, va separado del asunto por una línea en blanco.
    if len(lineas) > 1 and lineas[1].strip():
        hallazgos.append(Hallazgo(
            FALLA, origen, 2,
            "falta la línea en blanco entre el asunto y el cuerpo"))

    for patron, nombre in PROHIBIDOS:
        m = patron.search(mensaje)
        if m:
            n = mensaje[:m.start()].count("\n") + 1
            hallazgos.append(Hallazgo(
                FALLA, origen, n,
                f"el mensaje incluye {nombre} — G8 no firma con la herramienta"))

    return hallazgos


if __name__ == "__main__":
    # `53` · Un modulo que se ejecuta solo y no imprime nada dice, con su
    # silencio, lo mismo que diria si hubiera comprobado y estuviera todo bien.
    comun.no_es_punto_de_entrada("commit")
