# -*- coding: utf-8 -*-
"""`EP-005 · HU-001` · El histórico se puede buscar por tema, no solo por fecha.

**El problema.** Una sesión trata varios temas, y el índice del histórico solo
la nombra por su título: buscar «por qué se decidió esto» era abrir sesión por
sesión. Los temas ya estaban escritos, en los hallazgos de cada resumen.

**El caso que decide es `CP-05`.** Generado dos veces sobre lo mismo, el
archivo tiene que salir **idéntico**. Sin eso, cada corrida ensuciaría el
control de versiones con un archivo que cambia solo, y a la semana nadie lo
volvería a generar.
"""
import io
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import temas                     # noqa: E402
from comun import AVISO, FALLA   # noqa: E402


class IndiceTematico(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def resumen(self, dia, nombre, texto):
        carpeta = os.path.join(self.tmp, "historico-chat", "resumenes", dia)
        os.makedirs(carpeta, exist_ok=True)
        with io.open(os.path.join(carpeta, nombre), "w",
                     encoding="utf-8", newline="\n") as f:
            f.write(texto)

    def test_cp01_recoge_los_hallazgos_de_todos_los_resumenes(self):
        self.resumen("2026-01-02", "uno.md",
                     u"# 2026-01-02 · lo que quedó\n\n"
                     u"### H-1 · La primera cosa\n\ntexto\n\n"
                     u"### H-2 · La segunda cosa\n\ntexto\n")
        self.resumen("2026-01-03", "dos.md",
                     u"# 2026-01-03 · lo que quedó\n\n### H-1 · Otra cosa\n")
        salida = temas.generar(self.tmp)
        self.assertIn("La primera cosa", salida)
        self.assertIn("La segunda cosa", salida)
        self.assertIn("Otra cosa", salida)
        self.assertIn("**3 hallazgos** en **2 resúmenes**", salida)

    def test_cp02_cada_hallazgo_enlaza_a_su_resumen(self):
        """Sin el enlace el índice dice de qué se habló y no dónde leerlo."""
        self.resumen("2026-01-02", "el-tema.md",
                     u"# 2026-01-02 · lo que quedó\n\n### H-1 · La cosa\n")
        self.assertIn("(2026-01-02/el-tema.md)", temas.generar(self.tmp))

    def test_cp03_el_resumen_sin_hallazgos_no_ensucia(self):
        """Una sesión que no dejó nada es un dato, no una línea vacía."""
        self.resumen("2026-01-02", "vacio.md",
                     u"# 2026-01-02 · lo que quedó\n\nNada.\n")
        salida = temas.generar(self.tmp)
        self.assertNotIn("vacio.md", salida)
        self.assertIn("sin ningún hallazgo: 1", temas.linea_resumen(self.tmp))

    def test_cp04_el_readme_de_la_carpeta_no_es_un_resumen(self):
        self.resumen("2026-01-02", "README.md",
                     u"# Índice\n\n### H-1 · Esto no es un hallazgo\n")
        self.assertNotIn("Esto no es un hallazgo", temas.generar(self.tmp))

    def test_cp05_generar_dos_veces_da_lo_mismo(self):
        """El caso que decide: un archivo que cambia solo se deja de generar."""
        self.resumen("2026-01-02", "uno.md",
                     u"# 2026-01-02 · lo que quedó\n\n### H-1 · La cosa\n")
        self.assertEqual(temas.generar(self.tmp), temas.generar(self.tmp))

    def test_cp06_avisa_cuando_queda_atras_y_nunca_detiene(self):
        self.resumen("2026-01-02", "uno.md",
                     u"# 2026-01-02 · lo que quedó\n\n### H-1 · La cosa\n")
        hallazgos = temas.validar(self.tmp)
        self.assertTrue(hallazgos)
        self.assertEqual([], [h for h in hallazgos if h.severidad == FALLA])
        self.assertEqual(AVISO, hallazgos[0].severidad)

        temas.escribir(self.tmp)
        self.assertEqual([], temas.validar(self.tmp))

        self.resumen("2026-01-03", "dos.md",
                     u"# 2026-01-03 · lo que quedó\n\n### H-1 · Nueva\n")
        avisos = temas.validar(self.tmp)
        self.assertTrue(any("quedó atrás" in h.mensaje for h in avisos))

    def test_cp07_sin_resumenes_no_revienta(self):
        self.assertIn("Todavía no hay resúmenes", temas.generar(self.tmp))
        self.assertEqual("", temas.linea_resumen(self.tmp))


if __name__ == "__main__":
    unittest.main()
