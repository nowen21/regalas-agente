# -*- coding: utf-8 -*-
"""`EP-005 · HU-005` · Un cambio de reglas no se guarda sin su versión.

**Lo que protege.** `20·M10` exige que todo cambio de `base/` o `plantillas/`
suba `VERSION` y escriba su entrada en el registro. Hasta el 2026-08-22 eso
dependía de que alguien se acordara, y el propio repositorio tiene la prueba de
que acordarse no alcanza: hay entradas escritas a destiempo y números repetidos
por dos sesiones a la vez.

**El caso que decide es `CP-003`**: un cambio que no toca la norma no puede
notar nada. Sin él, la comprobación pediría versión en cada commit de
documentación, y a la semana alguien la apaga.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import guardian_version as guardian    # noqa: E402
from comun import FALLA                # noqa: E402


class ElCambioDeReglasLlevaSuVersion(unittest.TestCase):

    def hallazgos(self, *preparados):
        return guardian.validar(".", preparados=list(preparados))

    def test_cp001_sin_version_ni_entrada_no_pasa(self):
        h = self.hallazgos("base/09-git.md")
        self.assertEqual(1, len(h))
        self.assertEqual(FALLA, h[0].severidad, "tiene que detener, no avisar")
        self.assertIn("VERSION", h[0].mensaje)
        self.assertIn("CHANGELOG.md", h[0].mensaje)

    def test_cp001b_con_las_dos_pasa(self):
        self.assertEqual([], self.hallazgos("base/09-git.md", "VERSION",
                                            "CHANGELOG.md"))

    def test_cp002_el_cambio_mezclado_se_detecta_igual(self):
        """Meter la regla junto a diez archivos que no son norma no la esconde."""
        h = self.hallazgos("validadores/enlaces.py", "documentacion/x.md",
                           "plantillas/CLAUDE.md.plantilla")
        self.assertEqual(1, len(h))
        self.assertIn("plantillas/CLAUDE.md.plantilla", h[0].mensaje)

    def test_cp003_lo_que_no_toca_reglas_no_nota_nada(self):
        """El caso que decide: pedir versión donde no toca apaga el control."""
        self.assertEqual([], self.hallazgos("documentacion/epicas/x.md",
                                            "pendientes/y.md",
                                            "validadores/z.py",
                                            "historico-chat/a.md"))

    def test_cp004_el_rechazo_dice_exactamente_qué_falta(self):
        solo_registro = self.hallazgos("base/09-git.md", "VERSION")
        self.assertIn("CHANGELOG.md", solo_registro[0].mensaje)
        self.assertNotIn("subir `VERSION`", solo_registro[0].mensaje)

        solo_version = self.hallazgos("base/09-git.md", "CHANGELOG.md")
        self.assertIn("subir `VERSION`", solo_version[0].mensaje)

    def test_cp005_varios_archivos_de_norma_se_cuentan(self):
        h = self.hallazgos("base/09-git.md", "base/03-datos.md",
                           "plantillas/ADR.md")
        self.assertIn("2 archivo(s) más de la norma", h[0].mensaje)

    def test_cp006_un_commit_vacio_no_revienta(self):
        self.assertEqual([], self.hallazgos())


if __name__ == "__main__":
    unittest.main()
