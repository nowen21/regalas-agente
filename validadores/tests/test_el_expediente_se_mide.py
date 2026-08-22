# -*- coding: utf-8 -*-
"""Frente 3 del ciclo de vida · El expediente se mide, no se adivina.

**El ciclo no hace excepciones**: todos los entregables existen en todo
proyecto, y hasta ahora saber si un proyecto cumplía era abrir carpeta por
carpeta. Estas pruebas fijan lo que el lector promete: encuentra el entregable
por su nombre viva donde viva, distingue completo, en llenado y no-aplica, y
**nunca detiene**: el que falta es aviso, no falla.
"""
import io
import os
import shutil
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import expediente        # noqa: E402
from comun import FALLA  # noqa: E402

MARCA = u"«…»"


class Expediente(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def escribir(self, rel, texto):
        ruta = os.path.join(self.tmp, *rel.split("/"))
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)

    def test_encuentra_por_nombre_viva_donde_viva(self):
        """`prefijo-nombre.md` en cualquier carpeta cuenta igual que el molde."""
        self.escribir("prompts/miproyecto-planteamiento.md", u"El problema.\n")
        self.escribir("docs/22-plan-de-mantenimiento.md", u"Las rutinas.\n")
        lineas, _ = expediente.reporte(self.tmp)
        texto = "\n".join(lineas)
        self.assertIn("prompts/miproyecto-planteamiento.md", texto)
        self.assertIn("docs/22-plan-de-mantenimiento.md", texto)

    def test_el_molde_en_plantillas_no_es_el_entregable(self):
        """Midiendo el estándar, sus propios moldes contaban como expediente."""
        self.escribir("plantillas/ciclo/12-estudio-factibilidad.md",
                      u"Molde con «…».\n")
        lineas, _ = expediente.reporte(self.tmp)
        self.assertIn("| 12 | Estudio de factibilidad | (no hay) | **Falta** |",
                      "\n".join(lineas))

    def test_un_nombre_parecido_no_cuenta(self):
        """`replanteamiento.md` no es el planteamiento."""
        self.escribir("docs/replanteamiento.md", u"Otra cosa.\n")
        lineas, _ = expediente.reporte(self.tmp)
        self.assertIn("| 01 | Planteamiento | (no hay) | **Falta** |",
                      "\n".join(lineas))

    def test_los_tres_estados(self):
        """Completo, en llenado (cuenta los espacios) y no-aplica."""
        self.escribir("a/planteamiento.md", u"Todo escrito.\n")
        self.escribir("a/inventario-funcionalidades.md",
                      u"Falta esto: %s y esto: %s\n" % (MARCA, MARCA))
        self.escribir("a/documentacion-de-api.md",
                      u"No aplica porque el sistema no expone API.\n")
        lineas, _ = expediente.reporte(self.tmp)
        texto = "\n".join(lineas)
        self.assertIn("| Completo |", texto)
        self.assertIn("En llenado (2 espacios)", texto)
        self.assertIn("Declara no aplicar", texto)

    def test_declarar_no_aplica_con_espacios_es_en_llenado(self):
        """La declaración exige su porqué escrito: con huecos no está lista."""
        est, marcas = expediente.estado(u"No aplica porque %s\n" % MARCA)
        self.assertEqual("en llenado", est)
        self.assertEqual(1, marcas)

    def test_lo_que_falta_es_aviso_nunca_falla(self):
        """Informa, no detiene: un proyecto vacío no revienta nada."""
        hallazgos = expediente.validar(self.tmp)
        self.assertTrue(hallazgos)
        self.assertEqual([], [h for h in hallazgos if h.severidad == FALLA])

    def test_cuenta_la_cadena_de_ejecucion(self):
        """Las estaciones 03 a 11 se cuentan por su estructura canónica."""
        self.escribir("documentacion/epicas/EP-001-x/epica.md", u"La épica.\n")
        self.escribir("documentacion/epicas/EP-001-x/HU-001-y/HU-001-y.md",
                      u"La historia.\n")
        self.escribir(
            "documentacion/epicas/EP-001-x/HU-001-y/A-EP-001-HU-001-z/"
            "plan_trabajo.md", u"El plan.\n")
        lineas, _ = expediente.reporte(self.tmp)
        self.assertIn("1 épica(s), 1 HU, 1 fase(s) con plan",
                      "\n".join(lineas))


if __name__ == "__main__":
    unittest.main()
