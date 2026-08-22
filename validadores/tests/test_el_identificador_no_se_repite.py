# -*- coding: utf-8 -*-
"""`EP-004 · HU-011 · CP-002` · Un identificador de regla se usa una vez.

**El hueco, medido el 2026-08-22.** El programa comprobaba que el prefijo fuera
exclusivo del capítulo, pero no que el número no se repitiera dentro de él. Dos
`F27` en archivos distintos pasaban sin ruido, y desde ahí **toda cita a `F27`
es ambigua**: la regla que uno cree estar citando puede no ser la que manda.

Se contó a mano ese día —249 identificadores, 249 distintos— y esa fue la
señal: el orden estaba bien por costumbre, no por comprobación.

**Las derogadas cuentan igual.** `20·M11` prohíbe reutilizar el ID de una regla
derogada, y ese es justo el caso donde alguien lo repetiría sin querer, porque
la regla vieja ya no se lee.
"""
import io
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import metareglas              # noqa: E402
from comun import FALLA        # noqa: E402


class ElIdentificadorNoSeRepite(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.tmp, "base"))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def capitulo(self, nombre, cuerpo):
        ruta = os.path.join(self.tmp, "base", nombre)
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(cuerpo)

    def repetidos(self):
        return metareglas._identificador_repetido(metareglas.reglas(self.tmp))

    def test_dos_reglas_con_el_mismo_identificador_se_reportan(self):
        self.capitulo("09-git.md",
                      u"# 09 · Git  ·  `[CAPA 2]`\n\n## G1 · Uno\n\ntexto\n\n"
                      u"## G1 · Dos\n\ntexto\n")
        h = self.repetidos()
        self.assertEqual(2, len(h), "se reporta en las dos, no solo en la segunda")
        self.assertEqual(FALLA, h[0].severidad)
        self.assertIn("`G1`", h[0].mensaje)

    def test_el_hallazgo_nombra_las_dos_en_conflicto(self):
        """Sin las dos rutas, quien lo lea tiene que buscar la otra a mano."""
        self.capitulo("09-git.md", u"# 09 · Git\n\n## G1 · Uno\n\ntexto\n")
        self.capitulo("03-datos.md", u"# 03 · Datos\n\n## G1 · Otra\n\ntexto\n")
        h = self.repetidos()
        self.assertTrue(h)
        self.assertIn("09-git.md", h[0].mensaje)
        self.assertIn("03-datos.md", h[0].mensaje)

    def test_un_cuerpo_sin_repetidos_no_dice_nada(self):
        """El caso que decide: un programa que reporta siempre se apaga."""
        self.capitulo("09-git.md",
                      u"# 09 · Git\n\n## G1 · Uno\n\ntexto\n\n## G2 · Dos\n\ntexto\n")
        self.assertEqual([], self.repetidos())

    def test_la_derogada_sigue_ocupando_su_identificador(self):
        """`20·M11`: el ID de una regla derogada no se reutiliza."""
        self.capitulo("09-git.md",
                      u"# 09 · Git\n\n"
                      u"## G1 · Vieja  ·  `[DEROGADA en 3.0.0 → ver G2]`\n\ntexto\n\n"
                      u"## G1 · Nueva\n\ntexto\n")
        self.assertTrue(self.repetidos(),
                        "reutilizar el ID de una derogada tiene que reportarse")

    def test_el_cuerpo_real_del_estandar_no_tiene_ninguno(self):
        """La comprobación corre sobre el estándar de verdad y sale en cero."""
        RAIZ = os.path.dirname(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))))
        self.assertEqual(
            [], metareglas._identificador_repetido(metareglas.reglas(RAIZ)))


if __name__ == "__main__":
    unittest.main()
