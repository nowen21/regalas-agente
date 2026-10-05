#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Puerta de `validar.py`: el programa vive en `proyectos/cimiento/core/herramientas/validar.py`.

Existe porque los `.githooks` de cada proyecto instalado llaman a
`<estándar>/validadores/validar.py` por esa ruta: moverla rompería los
enganches de todos. Solo agrega Cimiento a la ruta de Python y le pasa la orden.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "proyectos", "cimiento"))

from core.herramientas.validar import FUERA_DE_LA_CORRIDA, main, raiz_del_proyecto  # noqa: E402,F401

if __name__ == "__main__":
    sys.exit(main())
