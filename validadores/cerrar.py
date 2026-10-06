#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Puerta de `cerrar.py`: el programa vive en `proyectos/cimiento/core/herramientas/cerrar.py`.

Se queda en esta ruta porque las reglas, las plantillas y los proyectos
instalados la nombran así (análisis 1 del pendiente 116, fila 21). Solo agrega
Cimiento a la ruta de Python y le pasa la orden tal como llega.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "proyectos", "cimiento"))

from core.herramientas.cerrar import main  # noqa: E402

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
