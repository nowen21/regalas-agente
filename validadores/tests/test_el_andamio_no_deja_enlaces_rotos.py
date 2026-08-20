# -*- coding: utf-8 -*-
"""`EP-004 · HU-005 · CA-05` — lo que el andamio levanta no nace con enlaces rotos (fase C)."""
import io
import os
import shutil
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ = os.path.dirname(VALIDADORES)
sys.path.insert(0, VALIDADORES)

import andamio    # noqa: E402
import enlaces    # noqa: E402
from comun import FALLA, leer   # noqa: E402


def arbol():
    """Copia de `plantillas/` y de `base/`, con una épica y una HU de mentira."""
    tmp = tempfile.mkdtemp()
    shutil.copytree(os.path.join(RAIZ, "plantillas"), os.path.join(tmp, "plantillas"))
    shutil.copytree(os.path.join(RAIZ, "base"), os.path.join(tmp, "base"))
    os.makedirs(os.path.join(tmp, "documentacion", "epicas", "EP-001-p", "HU-001-p"))
    return tmp


class CA05ElEsqueletoNaceBien(unittest.TestCase):

    def setUp(self):
        self.tmp = arbol()
        self.addCleanup(lambda: shutil.rmtree(self.tmp, ignore_errors=True))
        self.fase, _ = andamio.crear(self.tmp, "EP-001-p", "HU-001-p", "prueba", escribir=True)

    def test_cp_001_sin_el_enlace_crudo_ni_el_marcador(self):
        for nombre in os.listdir(self.fase):
            texto = leer(os.path.join(self.fase, nombre))
            with self.subTest(archivo=nombre):
                self.assertNotIn("](../../base/", texto)
                self.assertNotIn(andamio.MARCADOR_RAIZ, texto)
        for nombre in ("resultado_pruebas.md", "estado-fase.md"):
            self.assertIn("](../../../../../base/", leer(os.path.join(self.fase, nombre)), nombre)

    def test_cp_002_el_validador_de_enlaces_lo_da_por_bueno(self):
        rotos = [h for h in enlaces.validar_enlaces(self.tmp)
                 if h.severidad == FALLA and os.path.basename(self.fase) in str(h)]
        self.assertEqual([], [str(h) for h in rotos])


class Limites(unittest.TestCase):

    def test_cp_003_un_enlace_que_no_llega_a_la_raiz_no_se_toca(self):
        origen = os.path.join(RAIZ, "plantillas", "planes", "x.md")
        destino = os.path.join(RAIZ, "documentacion", "epicas", "EP", "HU", "A-EP-001-HU-001-p")
        texto = "ver [otra](../otra/cosa.md) y [raiz](../../base/x.md) y [fuera](../../../x.md)"
        salida = andamio._reenlazar(texto, origen, destino, RAIZ)
        self.assertIn("](../otra/cosa.md)", salida)
        self.assertIn("](../../../../../base/x.md)", salida)
        self.assertIn("](../../../x.md)", salida)       # más allá de la raíz: no se sabe adónde iba


if __name__ == "__main__":
    unittest.main(verbosity=2)
