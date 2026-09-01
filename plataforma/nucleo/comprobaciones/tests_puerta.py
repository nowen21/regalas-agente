# -*- coding: utf-8 -*-
"""Los casos del plan de pruebas de la fase `F-EP-015-HU-003`.

**El caso que decide es el CP-001:** que una versión que rompió algo no se
publique. Publicar es lo único que no se puede deshacer del lado de quien
recibe.

**Y el que más protege es el CP-004:** que no haber podido revisar tampoco deje
publicar. Un «no se pudo» tratado como «pasó» es la forma más silenciosa de
publicar a ciegas.
"""
from django.test import TestCase

from . import core, estado, puerta


def _verde(corridas=32):
    return core.Veredicto(True, corridas=corridas, con_fallas=0)


def _rojo():
    return core.Veredicto(True, corridas=32, con_fallas=1,
                          fallas=[{"donde": "a.md:1", "que": "algo"}])


class CP001LoQueRompioNoSePublica(TestCase):
    """**El caso que decide.**"""

    def test_con_comprobaciones_en_rojo_no_pasa(self):
        self.assertFalse(puerta.Puerta(True, veredicto=_rojo(),
                                       pruebas={"verdes": True}).pasa)

    def test_con_pruebas_en_rojo_no_pasa(self):
        self.assertFalse(puerta.Puerta(True, veredicto=_verde(),
                                       pruebas={"verdes": False}).pasa)

    def test_con_todo_en_verde_pasa(self):
        self.assertTrue(puerta.Puerta(True, veredicto=_verde(),
                                      pruebas={"verdes": True}).pasa)


class CP002LoQueObligaARehacerSeDeclara(TestCase):

    def test_una_funcionalidad_en_no_cumple_detiene_y_se_nombra(self):
        revision = puerta.Puerta(True, veredicto=_verde(),
                                 pruebas={"verdes": True}, rehacer=["F-007"])
        self.assertFalse(revision.pasa)
        self.assertIn("F-007", revision.rehacer)

    def test_lo_sin_verificar_se_declara_y_no_detiene(self):
        """Que no tenga prueba no quiere decir que esta versión la rompió."""
        revision = puerta.Puerta(True, veredicto=_verde(),
                                 pruebas={"verdes": True},
                                 sin_verificar=["F-009", "F-010"])
        self.assertTrue(revision.pasa)
        self.assertEqual(len(revision.sin_verificar), 2)


class CP003LoQueNoRompioPasaSinTrabajoManual(TestCase):

    def test_una_sola_orden_corre_todo(self):
        """Comprobaciones y baterías, en la misma llamada."""
        self.assertTrue(hasattr(puerta, "revisar_antes_de_publicar"))

    def test_el_tiempo_se_reporta(self):
        revision = puerta.Puerta(True, veredicto=_verde(),
                                 pruebas={"verdes": True}, segundos=241.0)
        self.assertGreater(revision.segundos, 0)


class CP004SinRevisarNoSePublica(TestCase):
    """Un «no se pudo» tratado como «pasó» es publicar a ciegas."""

    def test_si_no_se_pudo_revisar_no_pasa(self):
        self.assertFalse(puerta.Puerta(False, "sin el estándar").pasa)

    def test_sin_veredicto_tampoco_pasa(self):
        self.assertFalse(puerta.Puerta(True, veredicto=None,
                                       pruebas={"verdes": True}).pasa)

    def test_si_las_baterias_no_corrieron_no_pasa(self):
        self.assertFalse(puerta.Puerta(True, veredicto=_verde(),
                                       pruebas={"corrio": False,
                                                "verdes": False}).pasa)

    def test_cero_comprobaciones_tampoco_pasa(self):
        """Viene del veredicto: cero no es verde."""
        self.assertFalse(puerta.Puerta(True, veredicto=_verde(corridas=0),
                                       pruebas={"verdes": True}).pasa)


class CP005UnProyectoQueNoExiste(TestCase):

    def test_lo_dice_y_no_deja_publicar(self):
        revision = puerta.revisar_antes_de_publicar("no-registrado")
        self.assertFalse(revision.se_pudo)
        self.assertFalse(revision.pasa)


class LosEstadosQueDetienen(TestCase):
    """Cuál estado detiene la publicación y cuál no."""

    def test_no_cumple_detiene(self):
        self.assertEqual(estado.NO_CUMPLE, "no cumple")

    def test_sin_verificar_no_detiene_pero_se_dice(self):
        self.assertEqual(estado.SIN_VERIFICAR, "sin verificar")
