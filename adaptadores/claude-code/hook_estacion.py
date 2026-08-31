#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""`EP-005·HU-019` · Lo que el enganche de git llama después de cada commit.

Pregunta a git qué archivos entraron y cuál es el hash, y le pasa las dos cosas
a `estacion_commit`, que decide dónde escribir. Acá no hay reglas: solo la
conversación con git.

**Termina en 0 pase lo que pase.** Cuando esto corre, el commit **ya está
hecho**: lo único que puede lograr un fallo acá es ensuciar la salida o
—peor— hacer creer que algo se rompió. Un automatismo que asusta después de un
commit correcto se desinstala el mismo día.
"""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import estacion_commit                                   # noqa: E402


def raiz_pedida(argv):
    if "--raiz" in argv:
        i = argv.index("--raiz")
        if i + 1 < len(argv):
            return os.path.abspath(argv[i + 1])
    return os.getcwd()


def _git(raiz, *args):
    return subprocess.run(["git"] + list(args), cwd=raiz, capture_output=True,
                          text=True, encoding="utf-8", errors="replace")


def main():
    raiz = raiz_pedida(sys.argv[1:])

    hash_corto = _git(raiz, "rev-parse", "--short", "HEAD").stdout.strip()
    if not hash_corto:
        return 0

    archivos = [l.strip() for l in _git(
        raiz, "show", "--name-only", "--pretty=format:", "HEAD"
    ).stdout.splitlines() if l.strip()]
    if not archivos:
        return 0

    def cerrada_en_git(ruta_cierre):
        """El documento de cierre de esa fase, ¿ya está guardado?

        Una fase cuyo cierre no está en git **no se marca**: diría que se
        commiteó algo que no se commiteó.
        """
        if not os.path.isfile(ruta_cierre):
            return False
        salida = _git(raiz, "log", "--oneline", "-1", "--", ruta_cierre)
        return bool(salida.stdout.strip())

    tocadas = estacion_commit.marcar_las_fases(
        raiz, archivos, hash_corto, cerrada_en_git)

    for carpeta in tocadas:
        # **Se dice, y se dice que quedó sin guardar.** El archivo se modifica
        # después de que el commit se cerró, así que entra en el siguiente: si
        # no se avisa, parece trabajo sin guardar que nadie recuerda haber hecho.
        print("post-commit: anotado `%s` en la estación 12 de %s "
              "— queda sin guardar, y entra en el commit siguiente."
              % (hash_corto, os.path.basename(carpeta)))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:       # noqa: BLE001
        # Deliberado y declarado: el commit ya está hecho. Nada que pase acá
        # justifica alarmar a quien acaba de commitear bien.
        sys.exit(0)
