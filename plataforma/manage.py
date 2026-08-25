#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Punto de entrada de la plataforma. Se corre desde la carpeta `plataforma/`."""
import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
