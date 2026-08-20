# -*- coding: utf-8 -*-
"""`EP-004 · HU-008 · CA-04` — los índices que escriben los enganches cumplen `13·DOC14` (fase C)."""
import io
import os
import shutil
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import enlaces     # noqa: E402
import historico   # noqa: E402
import resumen     # noqa: E402


def escribir(ruta, texto):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with io.open(ruta, "w", encoding="utf-8") as f:
        f.write(texto)


class CA04LosIndicesNacenLegibles(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(lambda: shutil.rmtree(self.tmp, ignore_errors=True))
        self.carpeta = os.path.join(self.tmp, "historico-chat")

    def test_cp_001_el_enlace_al_resumen_dice_donde_vive(self):
        escribir(os.path.join(self.carpeta, "resumenes", "2026-01-01", "tema.md"), "# x\n")
        enlace = historico._enlace_al_resumen(self.carpeta, "2026-01-01-tema.md")
        self.assertEqual(" · [historico-chat/resumenes/2026-01-01/tema.md](resumenes/2026-01-01/tema.md)", enlace)

    def test_cp_002_la_linea_del_dia_dice_donde_vive(self):
        indice = os.path.join(self.carpeta, "resumenes", "README.md")
        escribir(indice, "# Resúmenes\n\n## Días\n\n")
        escribir(os.path.join(self.carpeta, "README.md"), "# Histórico\n")
        resumen._indexar_dias(self.tmp, "2026-01-01")
        texto = io.open(indice, encoding="utf-8").read()
        linea = "- [historico-chat/resumenes/2026-01-01/](2026-01-01/) — sin escribir todavía."
        self.assertIn(linea, texto)
        # El validador la da por bien escrita: es el mismo cálculo que usa DOC14.
        os.makedirs(os.path.join(self.carpeta, "resumenes", "2026-01-01"))
        for _n, t, d in enlaces.enlaces(texto):
            self.assertIsNone(enlaces._texto_esperado(self.tmp, indice, t, d))


if __name__ == "__main__":
    unittest.main(verbosity=2)
