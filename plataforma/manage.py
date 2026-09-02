#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Punto de entrada de la plataforma. Se corre desde la carpeta `plataforma/`.

**El puerto sale del `.env`, no de la memoria de quien la levanta.** Correr
`runserver` sin decirle nada usa el puerto que esta máquina tenga declarado, y
si no hay ninguno usa el 8000 de siempre. Escribirlo a mano cada vez es cómo se
terminan levantando tres servidores en el mismo puerto sin que nadie lo note.
"""
import os
import sys

PUERTO_DE_FABRICA = "8000"


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
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
    from config import ambiente
    ambiente.cargar(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 ".env"))
    from django.core.management import execute_from_command_line
    execute_from_command_line(con_el_puerto(sys.argv))


if __name__ == "__main__":
    main()
