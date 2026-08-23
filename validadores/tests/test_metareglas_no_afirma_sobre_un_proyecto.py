# -*- coding: utf-8 -*-
"""`81` · Apuntar las meta-reglas a un proyecto no inventa incumplimientos.

`validar.py metareglas --raiz <proyecto>` corría **las meta-reglas del estándar
contra la carpeta de un proyecto**, que no tiene cuerpo de reglas. Buscaba allí
el registro de cambios, el número de versión y dos archivos más, no los
encontraba, y **reportaba igual**: una falla y cuatro avisos, los cinco falsos.

Y la falla decía «`VERSION` dice  y el CHANGELOG», con el hueco vacío donde iba
el dato que no pudo leer. Ese es el defecto visto de cerca: **una comprobación
que no pudo abrir su archivo no debe afirmar nada**.

Importa porque `--raiz` es la bandera que en casi todos los subcomandos
significa «mira este proyecto». Que en este signifique otra cosa era una trampa
puesta, y un veredicto falso enseña a no creerle a ninguno.
"""
import io
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import metareglas                  # noqa: E402
from comun import AVISO, FALLA, RAIZ  # noqa: E402


class ApuntarAUnProyecto(unittest.TestCase):

    def setUp(self):
        self.proyecto = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.proyecto, ".agente"))
        with io.open(os.path.join(self.proyecto, "CLAUDE.md"), "w",
                     encoding="utf-8", newline="\n") as f:
            f.write(u"# Un proyecto cualquiera\n")

    def tearDown(self):
        shutil.rmtree(self.proyecto, ignore_errors=True)

    def test_no_se_reporta_ninguna_falla_sobre_un_proyecto(self):
        hallazgos = metareglas.validar(self.proyecto)
        self.assertEqual([], [h for h in hallazgos if h.severidad == FALLA],
                         "no hay meta-reglas que comprobar en un proyecto")

    def test_lo_que_devuelve_dice_qué_hacer_en_su_lugar(self):
        hallazgos = metareglas.validar(self.proyecto)
        self.assertEqual(1, len(hallazgos))
        self.assertEqual(AVISO, hallazgos[0].severidad)
        self.assertIn(u"--catalogo", hallazgos[0].mensaje,
                      "sin decir la bandera correcta, el aviso deja igual de perdido")

    def test_el_estandar_se_reconoce_por_lo_que_solo_el_tiene(self):
        self.assertTrue(metareglas.es_el_estandar(RAIZ))
        self.assertFalse(metareglas.es_el_estandar(self.proyecto))

    def test_una_carpeta_con_base_pero_sin_version_no_es_el_estandar(self):
        os.makedirs(os.path.join(self.proyecto, "base"))
        self.assertFalse(metareglas.es_el_estandar(self.proyecto))

    # ── que lo de siempre siga funcionando ───────────────────────────────

    def test_sobre_el_estandar_sigue_comprobando_de_verdad(self):
        """El guardián no puede volver mudo al validador donde sí sirve."""
        hallazgos = metareglas.validar(RAIZ)
        self.assertFalse(any(u"--catalogo" in h.mensaje for h in hallazgos),
                         "sobre el estándar no debe salir el aviso de carpeta ajena")


class NoSeAfirmaSinElDato(unittest.TestCase):
    """La otra mitad: leer devuelve vacío, no levanta excepción."""

    def test_sin_los_archivos_no_se_reporta_nada(self):
        vacia = tempfile.mkdtemp()
        try:
            self.assertEqual([], metareglas._fila19_version(vacia))
        finally:
            shutil.rmtree(vacia, ignore_errors=True)

    def test_con_los_archivos_sigue_comprobando(self):
        carpeta = tempfile.mkdtemp()
        try:
            with io.open(os.path.join(carpeta, "VERSION"), "w",
                         encoding="utf-8", newline="\n") as f:
                f.write(u"9.9.9\n")
            with io.open(os.path.join(carpeta, "CHANGELOG.md"), "w",
                         encoding="utf-8", newline="\n") as f:
                f.write(u"# Cambios\n\n## 1.0.0 — 2026-01-01\n\nAlgo.\n")
            hallazgos = metareglas._fila19_version(carpeta)
            self.assertEqual(1, len(hallazgos), "la versión no tiene su entrada")
            self.assertIn(u"9.9.9", hallazgos[0].mensaje,
                          "y el mensaje trae el dato, no un hueco")
        finally:
            shutil.rmtree(carpeta, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
