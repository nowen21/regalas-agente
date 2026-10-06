# -*- coding: utf-8 -*-
"""El análisis se prende desde un turno anterior (`EP-025·HU-023`).

Sin base: el estado va en archivo (`base=False`). Corren con
`python -m unittest core.enganches.tests_analisis_desde` desde `proyectos/cimiento/`.
"""
import os
import shutil
import tempfile
import unittest

from .analisis_en_curso import AnalisisEnCurso


class ElAnalisisSePrendeDesdeUnTurnoAnterior(unittest.TestCase):

    def setUp(self):
        self.raiz = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.raiz, True)
        carpeta = os.path.join(self.raiz, "pendientes", "7-algo")
        os.makedirs(carpeta)
        with open(os.path.join(carpeta, "pendiente.md"), "w", encoding="utf-8") as f:
            f.write("# Pendiente 7\n")
        os.makedirs(os.path.join(self.raiz, "historico-chat"))
        self.t = os.path.join(self.raiz, "historico-chat", "2026-10-05-sesion.md")
        with open(self.t, "w", encoding="utf-8") as f:
            f.write("".join("### %d · Usuario, 10:00\n\nhola\n\n" % n for n in range(1, 13)))
        self.curso = AnalisisEnCurso(self.raiz, self.t, base=False)

    def test_el_mensaje_dice_desde_que_turno(self):
        self.assertEqual(4, AnalisisEnCurso.turno_pedido("Analicemos: el pendiente 7 desde el turno 4"))
        self.assertIsNone(AnalisisEnCurso.turno_pedido("Analicemos: el pendiente 7"))
        self.assertIsNone(AnalisisEnCurso.turno_pedido("Pregunta: desde el turno 4"))

    def test_prende_desde_el_turno_pedido(self):
        prendido, nota = self.curso.prender(7, self.t, 12, 4)
        self.assertTrue(prendido)
        self.assertEqual("prendido desde el turno 4", nota)
        self.assertEqual(4, self.curso.leer_estado()["desde"])

    def test_si_ya_estaba_prendido_lo_corre(self):
        self.curso.prender(7, self.t, 10)
        self.assertEqual(10, self.curso.leer_estado()["desde"])
        prendido, nota = self.curso.prender(7, self.t, 12, 4)
        self.assertTrue(prendido)
        self.assertIn("desde el turno 4", nota)
        self.assertEqual(4, self.curso.leer_estado()["desde"])

    def test_un_turno_que_no_existe_se_rechaza(self):
        for desde in (0, 13):
            prendido, nota = self.curso.prender(7, self.t, 12, desde)
            self.assertFalse(prendido)
            self.assertIn("van del 1 al 12", nota)
        self.assertIsNone(self.curso.leer_estado())

    def test_sin_desde_sigue_como_antes(self):
        self.assertEqual("prendido desde el turno 12", self.curso.prender(7, self.t, 12)[1])

    def test_la_conversacion_entra_desde_ese_turno(self):
        self.curso.prender(7, self.t, 12, 4)
        self.curso.pasar()
        with open(self.curso.leer_estado()["analisis"], encoding="utf-8") as f:
            texto = f.read()
        self.assertIn("### 4 · Usuario", texto)
        self.assertNotIn("### 3 · Usuario", texto)


if __name__ == "__main__":
    unittest.main()
