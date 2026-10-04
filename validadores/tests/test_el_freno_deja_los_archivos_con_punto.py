# -*- coding: utf-8 -*-
"""El análisis puede autorizar un archivo cuyo nombre empieza con punto.

`rutas_de_una` le quitaba a cada ruta todos los `.` y `/` del comienzo, y
`.gitignore` quedaba como `gitignore`: ningún análisis lo podía autorizar
(sesión del 2026-10-04, «Corrija»).
"""
import os
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import freno  # noqa: E402


class ElFrenoDejaLosArchivosConPunto(unittest.TestCase):

    def rutas(self, celda):
        with tempfile.TemporaryDirectory() as tmp:
            ruta = os.path.join(tmp, "analisis-1.md")
            with open(ruta, "w", encoding="utf-8") as f:
                f.write("## Lo que se tiene que hacer\n\n"
                        "| # | Qué | Sale de | Pasó a |\n|---|---|---|---|\n"
                        "| 1 | algo | 1 | %s |\n" % celda)
            return freno.rutas_de_una(ruta)

    def test_el_punto_del_nombre_se_conserva(self):
        rutas = self.rutas("Este análisis, de una y sin fase: `.gitignore`, `proyectos/x/.env`")
        self.assertEqual(rutas, {".gitignore", "proyectos/x/.env"})

    def test_el_punto_barra_del_comienzo_se_quita(self):
        self.assertEqual(self.rutas("de una: `./validadores/comun.py`"), {"validadores/comun.py"})


if __name__ == "__main__":
    unittest.main()
