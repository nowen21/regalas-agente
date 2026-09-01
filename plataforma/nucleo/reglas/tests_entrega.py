# -*- coding: utf-8 -*-
"""Los casos del plan de pruebas de las fases `K` y `L` de `EP-016`.

**El caso que decide en la entrega es el CP-003:** que si esto no responde, se
diga dónde está la fuente. Devolver una lista vacía se leería como «este
proyecto no tiene reglas», que es la peor respuesta posible.

**Y el que decide en el desfase es el CP-006:** que un número inventado no pase
por estar al día. A simple vista se parece a ir adelantado.
"""
import io
import os
import shutil
import tempfile

from django.test import TestCase
from unittest import mock

from . import desfase, entrega

UNA_REGLA = u"""> Regla del capítulo [`20 · Meta-reglas`](../base.md).

## M1 · Un tema, un capítulo

Cada tema tiene un capítulo dueño.
"""


class Base(TestCase):

    def setUp(self):
        self.raiz = tempfile.mkdtemp(prefix="prueba-entrega-")
        self.escribir("base/00-nucleo-blindado.md", u"# Núcleo\n")
        self.escribir("base/20-meta-reglas/base.md", u"# 20 · Meta-reglas\n")
        self.escribir("base/20-meta-reglas/reglas/M1-un-tema.md", UNA_REGLA)

    def tearDown(self):
        shutil.rmtree(self.raiz, ignore_errors=True)

    def escribir(self, relativa, texto):
        completa = os.path.join(self.raiz, relativa.replace("/", os.sep))
        os.makedirs(os.path.dirname(completa), exist_ok=True)
        with io.open(completa, "w", encoding="utf-8", newline="\n") as archivo:
            archivo.write(texto)


class CP001SeEntreganLasReglas(Base):

    def test_se_entregan_los_capitulos_con_su_texto(self):
        entregada = entrega.entregar(self.raiz)
        self.assertTrue(entregada["se_pudo"])
        self.assertEqual(len(entregada["capitulos"]), 3)
        self.assertGreater(entregada["caracteres"], 0)

    def test_se_entrega_el_texto_y_no_un_resumen(self):
        """Un resumen de una regla es otra regla."""
        entregada = entrega.entregar(self.raiz)
        completo = u"".join(c["texto"] for c in entregada["capitulos"])
        self.assertIn(u"Cada tema tiene un capítulo dueño.", completo)

    def test_dice_cuantas_vigentes_y_bajo_que_version(self):
        entregada = entrega.entregar(self.raiz, "37.2.0")
        self.assertEqual(entregada["vigentes"], 1)
        self.assertIn("37.2.0", entrega.encabezado(entregada))

    def test_las_rutas_salen_relativas_al_proyecto(self):
        entregada = entrega.entregar(self.raiz)
        self.assertTrue(all(c["ruta"].startswith("base/")
                            for c in entregada["capitulos"]))


class CP002EntregarEsRapido(Base):

    def test_se_reporta_cuanto_tardo(self):
        self.assertGreaterEqual(entrega.entregar(self.raiz)["segundos"], 0)

    def test_no_tarda_mas_de_dos_segundos(self):
        """Es el `CA-2` de la ficha, y se mide, no se supone."""
        self.assertLess(entrega.entregar(self.raiz)["segundos"], 2.0)


class CP003SinPlataformaLaFuenteSigueAhi(Base):
    """**El caso que decide.** Una lista vacía se leería como «no hay reglas»."""

    def test_un_proyecto_sin_cuerpo_de_reglas_lo_dice(self):
        shutil.rmtree(os.path.join(self.raiz, "base"), ignore_errors=True)
        entregada = entrega.entregar(self.raiz)
        self.assertFalse(entregada["se_pudo"])
        self.assertIn("no tiene cuerpo de reglas", entregada["porque"])

    def test_y_dice_donde_esta_la_fuente(self):
        shutil.rmtree(os.path.join(self.raiz, "base"), ignore_errors=True)
        entregada = entrega.entregar(self.raiz)
        self.assertTrue(entregada["donde_esta_la_fuente"])
        self.assertIn("fuente sigue siendo legible", entrega.encabezado(entregada))

    def test_la_fuente_se_dice_tambien_cuando_todo_salio_bien(self):
        self.assertTrue(entrega.entregar(self.raiz)["donde_esta_la_fuente"])


class CP004ElDesfaseDiceQueCambio(TestCase):

    def _lector(self, publicadas, estandar, tramo, motivo):
        lector = mock.MagicMock()
        lector.version_estandar.return_value = estandar
        lector.versiones_publicadas.return_value = publicadas
        lector.tramo.return_value = tramo
        lector.comparar.return_value = motivo
        lector._resumen_del_tramo.return_value = ". Qué cambió: van %d" % len(tramo)
        return lector

    def test_al_dia_no_avisa(self):
        lector = self._lector(["37.2.0"], "37.2.0", [], None)
        with mock.patch.object(desfase, "_lector", return_value=lector):
            revision = desfase.revisar("37.2.0")
        self.assertTrue(revision["al_dia"])
        self.assertEqual(desfase.dicho(revision), "Al día.")

    def test_quedo_atras_dice_que_cambio(self):
        tramo = [("37.0.0", "MAYOR", "Algo grande"),
                 ("36.0.0", "MENOR", "Algo menos grande")]
        lector = self._lector(["35.0.0", "37.2.0"], "37.2.0", tramo, "va atrás")
        with mock.patch.object(desfase, "_lector", return_value=lector):
            revision = desfase.revisar("35.0.0")
        self.assertFalse(revision["al_dia"])
        self.assertEqual(len(revision["cambios"]), 2)
        self.assertIn("Qué cambió", desfase.dicho(revision))

    def test_dice_cuales_obligan_a_migrar(self):
        """Es lo único del aviso que cambia qué hacer."""
        tramo = [("37.0.0", "MAYOR", "Algo grande"),
                 ("36.0.0", "MENOR", "Algo menos")]
        lector = self._lector(["35.0.0"], "37.2.0", tramo, "va atrás")
        with mock.patch.object(desfase, "_lector", return_value=lector):
            self.assertEqual(desfase.revisar("35.0.0")["obligan"], ["37.0.0"])


class CP005UnNumeroInventadoNoEstaAlDia(TestCase):
    """**A simple vista se parece a ir adelantado.**"""

    def test_una_version_que_no_existe_se_dice(self):
        lector = mock.MagicMock()
        lector.version_estandar.return_value = "37.2.0"
        lector.versiones_publicadas.return_value = ["37.2.0", "35.0.0"]
        with mock.patch.object(desfase, "_lector", return_value=lector):
            revision = desfase.revisar("99.0.0")
        self.assertFalse(revision["existe"])
        self.assertFalse(revision["al_dia"])
        self.assertIn("no existió nunca", desfase.dicho(revision))

    def test_no_declarar_nada_no_es_declarar_algo_falso(self):
        lector = mock.MagicMock()
        lector.version_estandar.return_value = "37.2.0"
        lector.versiones_publicadas.return_value = []
        lector.comparar.return_value = "no declara"
        lector.tramo.return_value = []
        lector._resumen_del_tramo.return_value = ""
        with mock.patch.object(desfase, "_lector", return_value=lector):
            revision = desfase.revisar("")
        self.assertTrue(revision["existe"])
