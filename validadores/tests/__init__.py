# -*- coding: utf-8 -*-
"""Hace de esta carpeta un paquete, y con eso `unittest discover` la encuentra.

Sin este archivo, la orden documentada desde la primera prueba del repositorio
---`python -m unittest discover -s validadores/tests`--- se cae con
`ImportError: Start directory is not importable` **antes de correr nada**. Estuvo
así mientras se escribían 67 archivos y 650 pruebas, y nadie lo vio: el error se
leía como ruido.

Está vacío a propósito. Lo que corre la carpeta y cuenta lo que corrió es
`validadores/corredor.py`, porque `discover` sobre una carpeta vacía **termina
en 0**, y ese silencio en verde es el defecto que originó todo esto.
"""
