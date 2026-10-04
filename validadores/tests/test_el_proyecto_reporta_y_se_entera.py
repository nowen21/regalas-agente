# -*- coding: utf-8 -*-
"""`EP-023 · HU-003 · fase C` · El proyecto reporta a la HU y se entera.

Los casos CP-002 y CP-003 del plan de pruebas de la fase, sobre un estándar y
un proyecto de prueba en dos carpetas temporales enlazadas entre sí.
"""
import io
import os
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import aviso_resuelto   # noqa: E402
import pendientes       # noqa: E402

EPICA = "documentacion/epicas/EP-009-algo"
HU = EPICA + "/HU-001-una-cosa"
REPORTADO = EPICA + "/pendientes/110-algo-falla"
RESUMEN = "historico-chat/resumenes/2026-10-02"
SEGUIMIENTO = RESUMEN + "/pendientes/5-espera"

PENDIENTE = ("# Pendiente: algo falla\n\n| | |\n|---|---|\n| **De dónde sale** | {origen} |\n\n"
             "## El problema\n\nAlgo.\n\n## Por qué importa\n\nAlgo.\n")
ANALISIS = ("# Análisis 1: algo\n\n> **Aprobado** por el usuario el 2026-10-02, en el turno 3.\n\n"
            "## Lo que se tiene que hacer\n\n"
            "| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |\n|---|---|---|---|\n"
            "| 1 | Hacer algo | 1 | [HU-001](../../HU-001-una-cosa/HU-001-una-cosa.md) |\n")
HU_MD = "# HU-001 · Una cosa\n\n| Campo | Valor |\n|---|---|\n| **Estado** | {estado} |\n"
SESION = ("# Sesión\n\n### H-1 · Algo del estándar falla\n\n| Campo | Valor |\n|---|---|\n"
          "| Qué pasó | Algo. |\n| Pendiente | [5](pendientes/5-espera/pendiente.md) |\n")


class Base(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.estandar = os.path.join(self.tmp.name, "estandar")
        self.proyecto = os.path.join(self.tmp.name, "proyecto")
        self.escribir(self.estandar, HU + "/HU-001-una-cosa.md", HU_MD.format(estado="Lista"))
        self.escribir(self.estandar, REPORTADO + "/pendiente.md", PENDIENTE.format(
            origen="[H-1 del proyecto](../../../../../../proyecto/%s/sesion.md)" % RESUMEN))
        self.escribir(self.estandar, REPORTADO + "/analisis-1.md", ANALISIS)
        self.escribir(self.proyecto, RESUMEN + "/sesion.md", SESION)
        self.escribir(self.proyecto, SEGUIMIENTO + "/pendiente.md", PENDIENTE.format(
            origen="[110](../../../../../../estandar/%s/pendiente.md)" % REPORTADO))
        self.seguimiento = os.path.join(self.proyecto, *SEGUIMIENTO.split("/"))
        self.aviso = os.path.join(self.seguimiento, aviso_resuelto.AVISO)

    def tearDown(self):
        self.tmp.cleanup()

    def escribir(self, raiz, relativa, texto):
        ruta = os.path.join(raiz, *relativa.split("/"))
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
        return ruta

    def cumplir(self, prueba=True):
        self.escribir(self.estandar, HU + "/HU-001-una-cosa.md", HU_MD.format(estado="Terminada"))
        if prueba is not None:
            # `02·F29`: Cimiento probó la corrección en una copia del proyecto
            # (análisis 1 del pendiente 110, acuerdo 7).
            aviso_resuelto.anotar_prueba(os.path.join(self.estandar, *REPORTADO.split("/")), "2026-10-04",
                                         "una copia del proyecto", [("el caso", "reproducirlo", prueba)])

    def avisar(self):
        return aviso_resuelto.avisar(self.estandar, "2026-10-04", "53.0.0")


class CP002ElAvisoLlegaAlLadoDelSeguimiento(Base):

    def test_1_con_el_plan_sin_cumplir_no_escribe(self):
        self.assertEqual(([], []), self.avisar())
        self.assertFalse(os.path.exists(self.aviso))

    def test_2_con_el_plan_cumplido_y_la_prueba_escribe_el_aviso(self):
        self.cumplir()
        escritos, sin_entregar = self.avisar()
        self.assertEqual([self.aviso], escritos)
        self.assertEqual([], sin_entregar)
        texto = io.open(self.aviso, encoding="utf-8").read()
        self.assertIn("**Comprobado:** 2026-10-04", texto)
        self.assertIn("| el caso | reproducirlo | Pasa |", texto)
        self.assertIn(REPORTADO, texto)

    def test_3_otra_vez_no_lo_duplica(self):
        self.cumplir()
        self.avisar()
        io.open(self.aviso, "a", encoding="utf-8").write("lo que escribió el proyecto\n")
        self.assertEqual(([], []), self.avisar())
        self.assertIn("lo que escribió el proyecto", io.open(self.aviso, encoding="utf-8").read())

    def test_4_con_el_enlace_roto_no_escribe_y_dice_cual(self):
        self.cumplir()
        self.escribir(self.proyecto, RESUMEN + "/sesion.md", SESION.replace("5-espera", "6-no-existe"))
        escritos, sin_entregar = self.avisar()
        self.assertEqual([], escritos)
        self.assertEqual(1, len(sin_entregar))
        self.assertIn("H-1", sin_entregar[0][1])
        self.assertFalse(os.path.exists(self.aviso))


class CP003CimientoCompruebaAntesDeAvisar(Base):
    """Análisis 1 del pendiente 110, acuerdo 7: el proyecto no tiene que comprobar."""

    def test_1_sin_prueba_en_el_proyecto_no_hay_aviso(self):
        self.cumplir(prueba=None)
        escritos, sin_entregar = self.avisar()
        self.assertEqual([], escritos)
        self.assertIn(aviso_resuelto.PRUEBA, sin_entregar[0][1])
        self.assertEqual("abierto", pendientes.estado(self.seguimiento, self.proyecto))

    def test_2_con_la_prueba_fallida_no_hay_aviso(self):
        self.cumplir(prueba=False)
        self.assertEqual([], self.avisar()[0])
        self.assertFalse(os.path.exists(self.aviso))

    def test_3_con_la_prueba_aprobada_el_seguimiento_cierra_al_llegar_el_aviso(self):
        self.cumplir()
        self.avisar()
        self.assertEqual("cerrado", pendientes.estado(self.seguimiento, self.proyecto))


if __name__ == "__main__":
    unittest.main()
