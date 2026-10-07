# -*- coding: utf-8 -*-
"""`EP-026·HU-004` · Pruebas de leer el estándar de la base: CP-001 a CP-004 de la fase A."""
import io
import os
from unittest import mock

from django.test import TestCase

from core.comun import Archivos
from core.comun import Proyecto as Carpeta
from core.enganches import autorizado
from core.enganches.autorizado import Autorizaciones
from core.enganches.cargador import Cargador
from core.enganches.niveles import BaseSinRespuesta
from core.herramientas import recuperar
from core.herramientas.recuperar import RecuperadorDeReglas
from core.historia.models import ESTANDAR, Version
from core.validadores.metareglas import CuerpoDeReglas

from . import en_base
from .importar import documentos, importar, sincronizar
from .models import Documento

MENSAJES = ["Analicemos: cómo se versiona", "Escriba el resumen", "Suba a git", "Pregunta: qué es C29",
            "Hágalo y corra las pruebas", "hola"]


def _del_disco(raiz):
    salida = {}
    for ruta, completa in documentos(raiz):
        with io.open(completa, encoding="utf-8", newline="") as f:
            salida[ruta] = f.read()
    return salida


class LeerDeLaBase(TestCase):

    def setUp(self):
        self.raiz = Carpeta.estandar()
        self.docs = _del_disco(self.raiz)
        en_base.olvidar()
        self.addCleanup(en_base.olvidar)

    def lector(self, docs=None):
        return en_base.ArchivosEnBase(self.raiz, dict(docs or self.docs))

    def test_cp001_lo_que_dice_la_base_es_lo_que_se_lee(self):
        docs = dict(self.docs)
        ruta = "base/01-conducta.md"
        docs[ruta] = docs[ruta].replace("## C29 · Guarda dentro", "## C29 · CAMBIADA EN LA BASE Guarda dentro")
        lector = self.lector(docs)
        c29 = [r for r in CuerpoDeReglas.leer(self.raiz, lector) if r.id == "C29"][0]
        self.assertTrue(c29.titulo.startswith("CAMBIADA EN LA BASE"))
        self.assertEqual(Cargador.reglas(os.path.join(self.raiz, "base")),
                         Cargador.reglas(os.path.join(self.raiz, "base"), self.lector()))
        self.assertTrue(Autorizaciones(lector).de_la_base(self.raiz))

    def test_cp001_el_orden_es_el_de_la_carpeta(self):
        disco = list(Carpeta(self.raiz).recorrer_md("base"))
        self.assertEqual([os.path.normcase(r) for r in disco],
                         [os.path.normcase(r) for r in self.lector().recorrer("base", {"reglas-por-tarea", ".git",
                                                                                     "__pycache__"})])

    def test_cp002_sin_base_se_dice_y_no_se_autoriza(self):
        with mock.patch("core.estandar.en_base.fuente", side_effect=BaseSinRespuesta("MariaDB no responde")):
            texto = RecuperadorDeReglas(self.raiz).como_texto("Hágalo")
            self.assertIn("SIN BASE NO HAY REGLAS", texto)
            self.assertIn("MariaDB no responde", texto)
            self.assertEqual([], Autorizaciones().de_la_base(self.raiz))
            self.assertIn("SIN BASE", Cargador.contexto(self.raiz))
        self.assertTrue(recuperar.SIN_BASE and autorizado)

    def test_cp003_las_mismas_reglas(self):
        desde_base = RecuperadorDeReglas(self.raiz, self.lector())
        desde_disco = RecuperadorDeReglas(self.raiz, Archivos())
        aviso = "; se leen de la base con `manage.py ver_estandar <ruta>`"
        for mensaje in MENSAJES:
            # `EP-026·HU-006` · El texto de la base dice además cómo leer las reglas completas.
            # Sin tope: el aviso ocupa bytes y con el tope de siempre caben otras reglas.
            sin_tope = 10 ** 7
            self.assertEqual(desde_disco.como_texto(mensaje, tope=sin_tope),
                             desde_base.como_texto(mensaje, tope=sin_tope).replace(aviso, ""), mensaje)


class SincronizarConGit(TestCase):
    """CP-004."""

    def test_trae_lo_de_git_y_sin_diferencias_no_sube(self):
        raiz = Carpeta.estandar()
        importar(raiz)
        sincronizar(raiz)
        antes = Version.objects.filter(ambito=ESTANDAR).count()
        documento = Documento.objects.get(ruta="base/tareas.md")
        original = documento.contenido
        documento.contenido = "cambiado a mano en la base"
        documento.save()
        despues_del_cambio = Version.objects.filter(ambito=ESTANDAR).count()
        self.assertEqual((0, 1, 0), sincronizar(raiz))
        documento.refresh_from_db()
        self.assertEqual(original.replace("\r\n", "\n"), documento.contenido.replace("\r\n", "\n"))
        self.assertEqual(despues_del_cambio + 1, Version.objects.filter(ambito=ESTANDAR).count())
        self.assertEqual((0, 0, 0), sincronizar(raiz))
        self.assertGreater(Version.objects.filter(ambito=ESTANDAR).count(), antes)
