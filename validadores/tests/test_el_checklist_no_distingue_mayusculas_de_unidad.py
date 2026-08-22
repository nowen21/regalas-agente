# -*- coding: utf-8 -*-
"""Pendiente 72 · El checklist compara rutas, no texto: `c:/x` y `C:/x` son iguales.

Reportado por `matematica`: con los 16 enganches bien puestos, correr
`validar.py checklist --raiz` con la letra de unidad en minúscula los daba
todos por faltantes, y el agente anunciaba una instalación incompleta que no
lo era. Se compara normalizado en los dos lados.
"""
import io
import json
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import checklist  # noqa: E402
import instalar   # noqa: E402


def _otra_unidad(ruta, mayuscula):
    unidad, resto = os.path.splitdrive(ruta)
    if not unidad:
        return ruta
    return (unidad.upper() if mayuscula else unidad.lower()) + resto


class MayusculaDeUnidad(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="cimiento-unidad-")
        self.proyecto = os.path.join(self.tmp, "proyecto")
        os.makedirs(os.path.join(self.proyecto, ".claude"))
        self.estandar = os.path.join(self.tmp, "estandar")
        os.makedirs(self.estandar)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _escribir_enganches(self, estandar, proyecto):
        hooks = {}
        for evento, _, guion, mensaje, args in instalar.HOOKS_CLAUDE:
            h = instalar._hook_claude(estandar.replace("\\", "/"),
                                      proyecto.replace("\\", "/"),
                                      guion, mensaje, args)
            hooks.setdefault(evento, []).append({"hooks": [h]})
        ruta = os.path.join(self.proyecto, ".claude", "settings.json")
        io.open(ruta, "w", encoding="utf-8").write(json.dumps({"hooks": hooks}))

    @unittest.skipUnless(os.name == "nt", "solo Windows ignora la mayúscula de la unidad")
    def test_minuscula_y_mayuscula_dan_lo_mismo(self):
        self._escribir_enganches(_otra_unidad(self.estandar, True),
                                 _otra_unidad(self.proyecto, True))
        ok_may, _ = checklist._enganches_claude(
            _otra_unidad(self.proyecto, True), _otra_unidad(self.estandar, True))
        ok_min, msg = checklist._enganches_claude(
            _otra_unidad(self.proyecto, False), _otra_unidad(self.estandar, False))
        self.assertTrue(ok_may)
        self.assertTrue(ok_min, msg)

    def test_un_enganche_de_otro_estandar_si_se_reporta(self):
        """Normalizar no es aflojar: apuntar a otro estándar sigue siendo falta."""
        self._escribir_enganches(os.path.join(self.tmp, "otro-estandar"),
                                 self.proyecto)
        ok, msg = checklist._enganches_claude(self.proyecto, self.estandar)
        self.assertFalse(ok)
        self.assertIn("sin poner o vencidos", msg)


if __name__ == "__main__":
    unittest.main()
