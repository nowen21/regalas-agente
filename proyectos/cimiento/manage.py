#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Punto de entrada de Cimiento. Se corre desde la carpeta `proyectos/cimiento/`.

**El puerto sale del `.env`, no de la memoria de quien la levanta.** Correr
`runserver` sin decirle nada usa el puerto que esta máquina tenga declarado, y
si no hay ninguno usa el 8000 de siempre. Escribirlo a mano cada vez es cómo se
terminan levantando tres servidores en el mismo puerto sin que nadie lo note.

**Corre con el Python de Cimiento, lo abra quien lo abra** (`EP-026·HU-011`). El
aviso de cada sesión dice `python manage.py …`, y ese `python` es el del
computador, que no trae el conector de MySQL. Si el que corre no es el de
`.venv`, `manage.py` se vuelve a abrir con ese y devuelve lo que él devuelva.
"""
import os
import subprocess
import sys

PUERTO_DE_FABRICA = "8000"
CARPETA = os.path.dirname(os.path.abspath(__file__))


def _misma(una, otra):
    return os.path.normcase(os.path.abspath(una)) == os.path.normcase(os.path.abspath(otra))


def python_que_toca(carpeta=CARPETA, prefijo=None):
    """El Python de `.venv` si hay que volver a abrir con él; `None` si no.

    `None` cuando no hay `.venv`, o cuando ya corre con él: se compara la carpeta
    del ambiente (`sys.prefix`) y no el ejecutable, para que `pythonw` del mismo
    ambiente cuente como el mismo.
    """
    ambiente = os.path.join(carpeta, ".venv")
    if _misma(prefijo or sys.prefix, ambiente):
        return None
    return next((p for p in (os.path.join(ambiente, "Scripts", "python.exe"),
                             os.path.join(ambiente, "bin", "python"))
                 if os.path.isfile(p)), None)


def en_utf8():
    """La salida y los errores en UTF-8: la consola de Windows daña las tildes si no."""
    for flujo in (sys.stdout, sys.stderr):
        if hasattr(flujo, "reconfigure"):
            flujo.reconfigure(encoding="utf-8", errors="replace")


def puerto_declarado():
    """El puerto de esta máquina, o el de fábrica si no declaró ninguno."""
    return os.environ.get("PUERTO", PUERTO_DE_FABRICA)


def con_el_puerto(argumentos):
    """Los argumentos, con el puerto puesto si es `runserver` y no lo trae.

    **Solo se mete cuando no se dijo nada.** Quien escriba `runserver 9000`
    quiere el 9000, y el archivo no le discute.
    """
    if len(argumentos) < 2 or argumentos[1] != "runserver":
        return argumentos
    resto = [uno for uno in argumentos[2:] if not uno.startswith("-")]
    if resto:
        return argumentos
    return argumentos[:2] + [puerto_declarado()] + argumentos[2:]


def main():
    otro = python_que_toca()
    if otro:
        entorno = dict(os.environ, PYTHONIOENCODING="utf-8")
        sys.exit(subprocess.call([otro, os.path.abspath(__file__)] + sys.argv[1:], env=entorno))
    en_utf8()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
    from config import ambiente
    ambiente.cargar(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 ".env"))
    from django.core.management import execute_from_command_line
    execute_from_command_line(con_el_puerto(sys.argv))


if __name__ == "__main__":
    main()
