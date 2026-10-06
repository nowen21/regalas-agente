#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Puerta de `retirar.py`: el programa vive en `proyectos/cimiento/core/herramientas/retirar.py`.

Va junto a las demás órdenes que se piden a mano (`andamio.py`, `cerrar.py`),
para que un proyecto la encuentre donde busca esas (análisis 1 del pendiente
116, fila 26). Solo agrega Cimiento a la ruta de Python y le pasa la orden.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "proyectos", "cimiento"))

from core.herramientas.retirar import main  # noqa: E402

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
