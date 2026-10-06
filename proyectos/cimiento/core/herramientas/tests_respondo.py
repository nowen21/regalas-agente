"""`EP-001 · HU-036 · fase B`: «Respondo» contesta la pregunta del agente."""

import unittest

from core.enganches.tests_freno import RAIZ
from core.herramientas.recuperar import RecuperadorDeReglas


class RespondoContestaLaPregunta(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.r = RecuperadorDeReglas(RAIZ)

    def test_cp_001_respondo_esta_en_la_lista_y_no_recibe_el_aviso(self):
        self.assertIn("Respondo", self.r.palabras_de_la_lista())
        self.assertEqual("Respondo", self.r.palabra_clave("respondo que sí"))
        self.assertNotIn("NO ABRE CON UNA PALABRA", self.r.como_texto("Respondo: la B"))

    def test_cp_002_respondo_no_pide_tarea_propia(self):
        self.assertEqual({}, self.r.tareas_del_mensaje("Respondo: la B"))
