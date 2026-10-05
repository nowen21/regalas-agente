# -*- coding: utf-8 -*-
"""Los límites de aviso por defecto de un proyecto, en tokens estimados.

Viven aparte del modelo porque los usa también el enganche del presupuesto
(`EP-025·HU-009`), que corre sin Django.
"""
LIMITE_ENGANCHE = 2000
LIMITE_ARCHIVO = 10000
