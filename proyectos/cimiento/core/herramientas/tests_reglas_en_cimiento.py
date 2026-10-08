# -*- coding: utf-8 -*-
"""`EP-027·HU-006` · CP-001 de la fase E: la plantilla dice dónde viven las reglas del proyecto."""
import os
import unittest

from .tests_instalacion import callado, carpeta, claude_md_completo


class LaPlantillaDiceDondeViven(unittest.TestCase):

    def setUp(self):
        self.texto = claude_md_completo("demo")

    def test_el_paso_4_y_el_punto_5_2(self):
        paso_4 = self.texto[self.texto.index("4. **Aplicar las reglas propias del proyecto**"):]
        paso_4 = paso_4[:paso_4.index("\n5. ")]
        self.assertIn("registrado en Cimiento", paso_4)
        self.assertIn("índice", paso_4)
        self.assertIn("./.agente/reglas-proyecto.md", paso_4)
        punto = self.texto[self.texto.index("### 5.2"):]
        self.assertIn("Reglas de cada proyecto", punto)
        self.assertIn("pasar_reglas_proyecto", punto)
        self.assertNotIn("Si existe `./.agente/reglas-proyecto.md`,** leerlo", self.texto)

    def test_no_queda_ningun_espacio_por_llenar_nuevo(self):
        punto = self.texto[self.texto.index("### 5.2"):self.texto.index("## 6.")]
        self.assertNotIn("«", punto)

    def test_el_instalador_no_crea_el_archivo(self):
        from .instalar import Instalador

        destino = carpeta(self)
        callado(Instalador().instalar_agente_config, destino, True)
        self.assertTrue(os.path.isdir(os.path.join(destino, ".agente")))
        self.assertFalse(os.path.exists(os.path.join(destino, ".agente", "reglas-proyecto.md")))
