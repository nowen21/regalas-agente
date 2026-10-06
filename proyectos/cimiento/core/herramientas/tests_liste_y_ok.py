"""`EP-001 · HU-036 · fase C`: «Liste» y «OK» entran a la lista de `01·C28`."""

import unittest

from core.enganches.tests_freno import RAIZ
from core.herramientas.recuperar import RecuperadorDeReglas


class ListeYOkEntranALaLista(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.r = RecuperadorDeReglas(RAIZ)

    def test_cp_001_liste_y_ok_estan_en_la_lista_y_no_reciben_el_aviso(self):
        lista = self.r.palabras_de_la_lista()
        self.assertIn("Liste", lista)
        self.assertIn("OK", lista)
        self.assertEqual("OK", self.r.palabra_clave("ok"))
        self.assertEqual("Liste", self.r.palabra_clave("Liste las palabras"))
        self.assertTrue(self.r.trae_palabra_clave("OK, entendido"))
        self.assertNotIn("NO ABRE CON UNA PALABRA", self.r.como_texto("ok"))

    def test_cp_002_ok_no_autoriza_ninguna_tarea(self):
        self.assertEqual({}, self.r.tareas_del_mensaje("ok"))
        self.assertEqual({}, self.r.tareas_del_mensaje("Liste las palabras"))

    def test_cp_003_la_pregunta_entre_signos_se_trata_como_ausente(self):
        lista = self.r.palabras_de_la_lista()
        self.assertEqual([], [p for p in lista if p.startswith("¿")])
        self.assertFalse(self.r.trae_palabra_clave("¿qué sigue?"))
        self.assertNotIn("¿", self.r.aviso_sin_palabra().split("Las palabras son:")[1])
