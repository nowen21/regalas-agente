# -*- coding: utf-8 -*-
"""`EP-005 · HU-011` · El mapa del sitio no envejece en silencio.

**Qué protege.** El mapa del sitio es la puerta de entrada: quien abre el
repositorio y no sabe dónde está nada, entra por ahí. Y un mapa escrito a mano
envejece **sin avisar** — la carpeta nueva simplemente no aparece, y quien lo
lea creerá que no existe.

**El caso que decide es `CP-04`.** Después de nombrar la carpeta, la
comprobación tiene que **callarse**. Sin él, `CP-01` pasaría con un programa que
reporta siempre, y uno que reporta siempre se apaga a la semana: es el patrón
que este repositorio ya vio cuatro veces.

**Y se prueba el segundo lado**, que es el que casi nunca se prueba: el mapa que
nombra una carpeta que ya no existe manda a alguien a un sitio vacío. Eso es
aviso, no falla: molesta, pero no engaña sobre lo que hay.
"""
import io
import os
import shutil
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import sitio                          # noqa: E402
from comun import AVISO, FALLA        # noqa: E402


class MapaDelSitio(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.tmp, "anatomia"))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def carpeta(self, nombre):
        os.makedirs(os.path.join(self.tmp, nombre), exist_ok=True)

    def mapa(self, texto):
        ruta = os.path.join(self.tmp, "anatomia", "mapa-del-sitio.md")
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)

    def test_cp01_la_carpeta_nueva_que_el_mapa_no_nombra_es_falla(self):
        self.carpeta("validadores")
        self.mapa(u"# Mapa\n\nanatomia/ es esto.\n")
        fallas = [h for h in sitio.validar(self.tmp) if h.severidad == FALLA]
        self.assertTrue(any("validadores/" in h.mensaje for h in fallas))

    def test_cp02_falta_el_mapa_entero(self):
        self.carpeta("base")
        hallazgos = sitio.validar(self.tmp)
        self.assertEqual(FALLA, hallazgos[0].severidad)
        self.assertIn("falta el mapa del sitio", hallazgos[0].mensaje)

    def test_cp03_la_carpeta_que_el_mapa_nombra_y_ya_no_existe_es_aviso(self):
        """Molesta, pero no engaña sobre lo que hay: por eso no detiene."""
        self.carpeta("base")
        self.mapa(u"# Mapa\n\n- `base/` la norma\n- `diplomado-ia/` apuntes\n"
                  u"- anatomia/ este archivo\n")
        hallazgos = sitio.validar(self.tmp)
        self.assertEqual([], [h for h in hallazgos if h.severidad == FALLA])
        avisos = [h for h in hallazgos if h.severidad == AVISO]
        self.assertTrue(any("diplomado-ia/" in h.mensaje for h in avisos))

    def test_cp04_nombrada_la_carpeta_se_calla(self):
        """El caso que decide: un validador que reporta siempre se apaga."""
        self.carpeta("base")
        self.carpeta("validadores")
        self.mapa(u"# Mapa\n\nbase/ la norma · validadores/ los programas ·\n"
                  u"anatomia/ este archivo\n")
        self.assertEqual([], sitio.validar(self.tmp))

    def test_cp05_lo_local_y_lo_generado_no_es_del_mapa(self):
        """`.venv`, `__pycache__` y `terceros/` no viajan: nombrarlos es ruido."""
        for nombre in (".venv", "__pycache__", "terceros", "node_modules"):
            self.carpeta(nombre)
        self.mapa(u"# Mapa\n\nanatomia/ este archivo\n")
        self.assertEqual([], sitio.validar(self.tmp))

    def test_cp06_el_recuento_se_puede_mirar_sin_abrir_el_mapa(self):
        self.carpeta("base")
        self.carpeta("plantillas")
        self.mapa(u"# Mapa\n\nbase/ la norma · anatomia/ este archivo\n")
        linea = sitio.linea_resumen(self.tmp)
        self.assertIn("Carpetas de primer nivel: 3", linea)
        self.assertIn("sin nombrar: 1", linea)

    def test_cp07_el_nombre_parecido_no_cuenta_por_la_carpeta(self):
        """`mis-plantillas/` no es `plantillas/`: el mapa tiene que nombrarla."""
        self.carpeta("plantillas")
        self.mapa(u"# Mapa\n\nmis-plantillas/ otra cosa · anatomia/ este archivo\n")
        fallas = [h for h in sitio.validar(self.tmp) if h.severidad == FALLA]
        self.assertTrue(any("`plantillas/`" in h.mensaje for h in fallas))


if __name__ == "__main__":
    unittest.main()
