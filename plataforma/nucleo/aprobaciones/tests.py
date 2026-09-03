# -*- coding: utf-8 -*-
"""Los casos del plan de pruebas de las fases `M`, `N` y `O` de `EP-017`.

**El caso que decide es el CP-003:** que editar un documento aprobado le quite
la aprobación. Sin eso, «está aprobado» no dice nada: el documento pudo haber
cambiado tres veces desde entonces.

**Y el que más protege es el CP-004:** que la aprobación anterior no se borre.
Es la historia de qué se autorizó, y sin ella el documento queda como si nunca
hubiera pasado por nadie.
"""
import io
import os
import shutil
import tempfile

from django.test import TestCase

from nucleo.proyectos.models import Proyecto
from nucleo.acceso import grupos, para_probar
from . import core
from .models import Aprobacion


class Base(TestCase):

    def setUp(self):
        # Desde `EP-022`, `quien` no es un texto: es una cuenta con permiso
        # para aprobar. Aprobar con un nombre inventado ya no se puede, que es
        # justamente lo que esa épica vino a arreglar.
        for cuenta in ("ing-jose", "quien-manda", "el-primero", "el-segundo"):
            para_probar._cuenta(cuenta, grupos.USUARIO)
        self.carpeta = tempfile.mkdtemp(prefix="prueba-aprobaciones-")
        Proyecto.objects.create(identificador="de-prueba", nombre="De prueba",
                                ruta_codigo=self.carpeta,
                                ruta_normalizada=self.carpeta.lower(),
                                conectado="conectado")
        self.escribir("documentacion/x.md", u"# Un documento\n\nSu texto.\n")

    def tearDown(self):
        shutil.rmtree(self.carpeta, ignore_errors=True)

    def escribir(self, relativa, texto):
        completa = os.path.join(self.carpeta, relativa.replace("/", os.sep))
        os.makedirs(os.path.dirname(completa), exist_ok=True)
        with io.open(completa, "w", encoding="utf-8", newline="\n") as archivo:
            archivo.write(texto)


class CP001SeRegistraQuienAproboYSobreQue(Base):

    def test_queda_quien_cuando_y_sobre_que_texto(self):
        una = core.aprobar("de-prueba", "documentacion/x.md", "ing-jose")
        self.assertEqual(una.quien, "ing-jose")
        self.assertTrue(una.cuando)
        self.assertTrue(una.huella)
        self.assertGreater(una.tamano, 0)

    def test_la_huella_es_la_del_texto_aprobado(self):
        """Sin la huella, «está aprobado» no dice nada."""
        una = core.aprobar("de-prueba", "documentacion/x.md", "quien-manda")
        self.assertEqual(una.huella,
                         core.huella(u"# Un documento\n\nSu texto.\n"))

    def test_se_puede_consultar_despues(self):
        core.aprobar("de-prueba", "documentacion/x.md", "quien-manda")
        self.assertEqual(len(core.historia_de("de-prueba",
                                              "documentacion/x.md")), 1)

    def test_aprobar_queda_registrado_en_la_auditoria(self):
        from nucleo.auditoria.models import Registro
        antes = Registro.objects.count()
        core.aprobar("de-prueba", "documentacion/x.md", "quien-manda")
        self.assertEqual(Registro.objects.count(), antes + 1)


class CP002NoSeApruebaLoQueNoExiste(Base):
    """Aprobar algo que no está sería firmar en blanco."""

    def test_un_documento_que_no_existe_se_rechaza(self):
        with self.assertRaises(core.NoSePuedeAprobar):
            core.aprobar("de-prueba", "documentacion/no-esta.md", "quien-manda")

    def test_y_no_queda_nada_registrado(self):
        try:
            core.aprobar("de-prueba", "documentacion/no-esta.md", "quien-manda")
        except core.NoSePuedeAprobar:
            pass
        self.assertEqual(Aprobacion.objects.count(), 0)

    def test_un_proyecto_que_no_existe_tambien_se_rechaza(self):
        with self.assertRaises(core.NoSePuedeAprobar):
            core.aprobar("no-registrado", "documentacion/x.md", "quien-manda")


class CP003EditarQuitaLaAprobacion(Base):
    """**El caso que decide.**"""

    def test_sin_tocar_el_documento_sigue_aprobado(self):
        core.aprobar("de-prueba", "documentacion/x.md", "quien-manda")
        estado = core.estado_de("de-prueba", "documentacion/x.md")
        self.assertEqual(estado["estado"], core.APROBADO)

    def test_al_editarlo_la_aprobacion_caduca(self):
        core.aprobar("de-prueba", "documentacion/x.md", "quien-manda")
        self.escribir("documentacion/x.md", u"# Un documento\n\nOtro texto.\n")
        estado = core.estado_de("de-prueba", "documentacion/x.md")
        self.assertEqual(estado["estado"], core.CADUCADA)

    def test_y_se_ve_cuanto_cambio(self):
        core.aprobar("de-prueba", "documentacion/x.md", "quien-manda")
        self.escribir("documentacion/x.md",
                      u"# Un documento\n\nSu texto, y bastante más.\n")
        de_mas, de_menos = core.que_cambio("de-prueba", "documentacion/x.md")
        self.assertGreater(de_mas, 0)
        self.assertEqual(de_menos, 0)

    def test_si_el_documento_desaparece_tambien_caduca(self):
        core.aprobar("de-prueba", "documentacion/x.md", "quien-manda")
        os.remove(os.path.join(self.carpeta, "documentacion", "x.md"))
        estado = core.estado_de("de-prueba", "documentacion/x.md")
        self.assertEqual(estado["estado"], core.CADUCADA)
        self.assertFalse(estado["existe"])


class CP004LaAprobacionAnteriorNoSeBorra(Base):
    """Es la historia de qué se autorizó y cuándo."""

    def test_al_volver_a_aprobar_quedan_las_dos(self):
        core.aprobar("de-prueba", "documentacion/x.md", "el-primero")
        self.escribir("documentacion/x.md", u"# Otro texto\n")
        core.aprobar("de-prueba", "documentacion/x.md", "el-segundo")
        self.assertEqual(len(core.historia_de("de-prueba",
                                              "documentacion/x.md")), 2)

    def test_la_que_manda_es_la_ultima(self):
        core.aprobar("de-prueba", "documentacion/x.md", "el-primero")
        self.escribir("documentacion/x.md", u"# Otro texto\n")
        core.aprobar("de-prueba", "documentacion/x.md", "el-segundo")
        estado = core.estado_de("de-prueba", "documentacion/x.md")
        self.assertEqual(estado["quien"], "el-segundo")
        self.assertEqual(estado["estado"], core.APROBADO)
        self.assertEqual(estado["cuantas"], 2)


class CP005LosTresEstadosSeDicenConPalabras(Base):
    """Quien no distingue colores tiene que poder saberlo igual."""

    def test_un_documento_sin_aprobacion_aparece_asi_no_vacio(self):
        estado = core.estado_de("de-prueba", "documentacion/x.md")
        self.assertEqual(estado["estado"], core.SIN_APROBACION)
        self.assertIn("Sin aprobación", estado["en_palabras"])

    def test_los_tres_estados_tienen_su_frase(self):
        for uno in (core.APROBADO, core.CADUCADA, core.SIN_APROBACION):
            self.assertTrue(core.EN_PALABRAS[uno])

    def test_la_frase_de_caducada_dice_por_que(self):
        self.assertIn("cambió", core.EN_PALABRAS[core.CADUCADA])

    def test_varios_documentos_salen_todos_con_su_estado(self):
        self.escribir("documentacion/y.md", u"# Otro\n")
        core.aprobar("de-prueba", "documentacion/x.md", "quien-manda")
        lista = core.de_un_proyecto("de-prueba",
                                    ["documentacion/x.md", "documentacion/y.md"])
        estados = [uno["estado"] for uno in lista]
        self.assertEqual(estados, [core.APROBADO, core.SIN_APROBACION])
