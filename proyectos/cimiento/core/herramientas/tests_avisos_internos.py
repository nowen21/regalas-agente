# -*- coding: utf-8 -*-
"""`EP-005·HU-024`, fase B: el enganche de reglas no le aplica nada a un aviso interno."""
import unittest

from core.herramientas.recuperar import RecuperadorDeReglas


class LasReglasNoSeAplicanAlAviso(unittest.TestCase):
    """CP-001."""

    @classmethod
    def setUpClass(cls):
        cls.recuperador = RecuperadorDeReglas()

    def test_los_avisos_internos_no_reciben_nada(self):
        for aviso in ("<task-notification>\n<task-id>x</task-id>\n</task-notification>",
                      '<agent-message from="a1">\ninforme\n</agent-message>'):
            with self.subTest(aviso=aviso[:20]):
                self.assertEqual("", self.recuperador.como_texto(aviso))

    def test_un_mensaje_sin_palabra_sigue_recibiendo_el_aviso(self):
        self.assertIn("01·C28", self.recuperador.como_texto("hola"))
