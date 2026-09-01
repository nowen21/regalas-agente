# -*- coding: utf-8 -*-
"""Los casos del plan de pruebas de la fase `J-EP-016-HU-004`.

**El caso que decide es el CP-002:** que sin decir qué cambió no se publique.
Quien adopte una versión sin registro no puede saber si le toca rehacer algo, y
el aviso de desfase no tiene qué contar.

**Y el que más protege es el CP-001:** que no se publique dos veces el mismo
número. Dos proyectos declarando la misma versión con reglas distintas es un
desorden que no se puede deshacer desde acá.
"""
import io
import os
import shutil
import tempfile

from django.test import TestCase
from unittest import mock

from . import publicacion

REGISTRO = u"""# Registro de cambios

## 37.2.0 — 2026-08-31

**Dos modelos de documento entran.** Y los dos marcan sus huecos.

**MENOR** (aditivo): un proyecto al día no tiene que hacer nada.

## 37.1.0 — 2026-08-31

**MAYOR** (obliga): algo cambió.

**Una norma escrita informa.**

## 37.0.0 — 2026-08-30

**Sin tipo declarado.** Esta entrada no dice si es mayor o menor.
"""


class _Puerta(object):
    def __init__(self, pasa=True, porque=""):
        self.pasa = pasa
        self.porque = porque


class Base(TestCase):

    def setUp(self):
        self.raiz = tempfile.mkdtemp(prefix="prueba-publicacion-")
        self.escribir("CHANGELOG.md", REGISTRO)
        self.escribir("VERSION", u"37.2.0\n")

    def tearDown(self):
        shutil.rmtree(self.raiz, ignore_errors=True)

    def escribir(self, nombre, texto):
        with io.open(os.path.join(self.raiz, nombre), "w", encoding="utf-8",
                     newline="") as archivo:
            archivo.write(texto)

    def leer(self, nombre):
        with io.open(os.path.join(self.raiz, nombre), encoding="utf-8",
                     newline="") as archivo:
            return archivo.read()

    def revisar(self, version, ya_existe=False, puerta_pasa=True):
        with mock.patch.object(publicacion.desfase, "existe",
                               return_value=ya_existe), \
             mock.patch.object(publicacion.puerta, "revisar_antes_de_publicar",
                               return_value=_Puerta(puerta_pasa, "algo rojo")):
            return publicacion.revisar("de-prueba", self.raiz, version)


class CP001NoSePublicaDosVecesElMismoNumero(Base):
    """Dos proyectos con la misma versión y reglas distintas."""

    def test_una_version_ya_publicada_se_rechaza(self):
        revision = self.revisar("37.2.0", ya_existe=True)
        self.assertFalse(revision["se_puede"])
        self.assertTrue(any("ya está publicada" in p
                            for p in revision["problemas"]))

    def test_una_que_no_existe_pasa_esa_comprobacion(self):
        revision = self.revisar("37.2.0", ya_existe=False)
        self.assertFalse(any("ya está publicada" in p
                             for p in revision["problemas"]))


class CP002SinDecirQueCambioNoSePublica(Base):
    """**El caso que decide.**"""

    def test_sin_entrada_en_el_registro_no_se_publica(self):
        revision = self.revisar("40.0.0")
        self.assertFalse(revision["se_puede"])
        self.assertTrue(any("registro de cambios" in p
                            for p in revision["problemas"]))

    def test_con_entrada_se_lee_su_tipo(self):
        self.assertEqual(self.revisar("37.2.0")["tipo"], "MENOR")

    def test_el_tipo_se_lee_este_antes_o_despues_del_titulo(self):
        """El registro se escribió de las dos formas."""
        self.assertEqual(self.revisar("37.1.0")["tipo"], "MAYOR")

    def test_una_entrada_sin_tipo_se_rechaza(self):
        revision = self.revisar("37.0.0")
        self.assertFalse(revision["se_puede"])
        self.assertTrue(any("MAYOR, MENOR o PARCHE" in p
                            for p in revision["problemas"]))

    def test_la_entrada_se_recorta_hasta_la_siguiente(self):
        entrada = publicacion.entrada_del_registro(self.raiz, "37.1.0")
        self.assertIn("Una norma escrita informa", entrada)
        self.assertNotIn("Dos modelos", entrada)


class CP003LoQueRompeNoSePublica(Base):

    def test_con_la_puerta_en_rojo_no_se_publica(self):
        revision = self.revisar("37.2.0", puerta_pasa=False)
        self.assertFalse(revision["se_puede"])
        self.assertTrue(any("puerta no pasa" in p
                            for p in revision["problemas"]))

    def test_con_todo_en_verde_se_puede(self):
        self.assertTrue(self.revisar("37.2.0")["se_puede"])


class CP004PublicarEscribeLaVersion(Base):

    def test_publica_y_deja_la_version_escrita(self):
        with mock.patch.object(publicacion.desfase, "existe",
                               return_value=False), \
             mock.patch.object(publicacion.puerta, "revisar_antes_de_publicar",
                               return_value=_Puerta(True)):
            publicacion.publicar("de-prueba", self.raiz, "37.2.0")
        self.assertEqual(self.leer("VERSION"), u"37.2.0\n")

    def test_si_falta_algo_no_escribe_y_lo_dice_todo_junto(self):
        """Decirlo de a uno obliga a intentar tres veces."""
        with mock.patch.object(publicacion.desfase, "existe",
                               return_value=True), \
             mock.patch.object(publicacion.puerta, "revisar_antes_de_publicar",
                               return_value=_Puerta(False, "rojo")):
            with self.assertRaises(publicacion.NoSePuedePublicar) as caso:
                publicacion.publicar("de-prueba", self.raiz, "40.0.0")
        self.assertGreaterEqual(str(caso.exception).count("\n"), 1)
        self.assertEqual(self.leer("VERSION"), u"37.2.0\n")

    def test_un_numero_que_no_tiene_forma_de_version_se_rechaza(self):
        revision = self.revisar("la que sea")
        self.assertFalse(revision["se_puede"])
