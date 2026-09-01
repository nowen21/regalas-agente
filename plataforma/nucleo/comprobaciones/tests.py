# -*- coding: utf-8 -*-
"""Los casos del plan de pruebas de la fase `D-EP-015-HU-001`.

**El caso que decide es el CP-003:** que un proyecto sin el estándar instalado
no reciba veredicto. «Sin comprobar» y «no cumple» son cosas distintas, y
confundirlas hace que nadie mire los rojos de verdad.

**Y el que más protege es el CP-005:** cero comprobaciones corridas no es verde.
Una corrida que no comprobó nada y termina bien es un silencio que se lee como
éxito.
"""
import io
import os
import shutil
import tempfile

from django.test import TestCase

from nucleo.proyectos.models import Proyecto
from . import core


class Base(TestCase):

    def setUp(self):
        self.carpeta = tempfile.mkdtemp(prefix="prueba-comprob-")

    def tearDown(self):
        shutil.rmtree(self.carpeta, ignore_errors=True)

    def registrar(self, ruta=None, identificador="de-prueba"):
        ruta = ruta if ruta is not None else self.carpeta
        return Proyecto.objects.create(
            identificador=identificador, nombre="De prueba", ruta_codigo=ruta,
            ruta_normalizada=ruta.lower(), conectado="conectado")

    def con_estandar(self):
        """Una carpeta que parece tener el estándar instalado."""
        base = os.path.join(self.carpeta, "base")
        os.makedirs(base, exist_ok=True)
        with io.open(os.path.join(base, "00-nucleo-blindado.md"), "w",
                     encoding="utf-8", newline="\n") as archivo:
            archivo.write(u"# Núcleo\n")


class CP003SinEstandarNoHayVeredicto(Base):
    """**El caso que decide.** Sin comprobar no es lo mismo que en verde."""

    def test_una_carpeta_sin_el_estandar_lo_dice(self):
        self.registrar()
        veredicto = core.comprobar("de-prueba")
        self.assertFalse(veredicto.se_pudo)
        self.assertIn("estándar", veredicto.porque)

    def test_y_no_dice_que_cumple(self):
        self.registrar()
        self.assertFalse(core.comprobar("de-prueba").cumple)

    def test_una_carpeta_que_ya_no_esta_lo_dice(self):
        self.registrar(ruta=os.path.join(self.carpeta, "no", "existe"))
        veredicto = core.comprobar("de-prueba")
        self.assertFalse(veredicto.se_pudo)
        self.assertIn("carpeta", veredicto.porque)

    def test_un_proyecto_que_no_existe_lo_dice(self):
        veredicto = core.comprobar("no-registrado")
        self.assertFalse(veredicto.se_pudo)
        self.assertFalse(veredicto.cumple)


class CP005CeroEsRojo(TestCase):
    """Una corrida que no comprobó nada no puede terminar en verde."""

    def test_cero_comprobaciones_no_cumple(self):
        self.assertFalse(core.Veredicto(True, corridas=0, con_fallas=0).cumple)

    def test_con_comprobaciones_y_sin_fallas_cumple(self):
        self.assertTrue(core.Veredicto(True, corridas=32, con_fallas=0).cumple)

    def test_con_fallas_no_cumple(self):
        self.assertFalse(core.Veredicto(True, corridas=32, con_fallas=1).cumple)

    def test_lo_que_no_se_pudo_comprobar_tampoco_cumple(self):
        self.assertFalse(core.Veredicto(False, "sin estándar").cumple)


class SeLeeElResumenDelEstandar(TestCase):
    """Lo que el estándar imprime, leído tal como lo imprime."""

    def test_el_resumen_da_los_dos_numeros(self):
        encontrado = core._RESUMEN.search(
            u"32 comprobación(es) corridas · 1 con fallas")
        self.assertEqual(encontrado.group(1), "32")
        self.assertEqual(encontrado.group(2), "1")

    def test_una_falla_trae_su_archivo_y_su_linea(self):
        fallas = core._FALLA.findall(
            u"[FALLA] documentacion/x.md:107 — enlace roto: y.md\n")
        self.assertEqual(fallas[0][0], "documentacion/x.md:107")
        self.assertIn("enlace roto", fallas[0][1])

    def test_varias_fallas_salen_todas(self):
        salida = (u"[FALLA] a.md:1 — una\n"
                  u"algo que no es una falla\n"
                  u"[FALLA] b.md:2 — otra\n")
        self.assertEqual(len(core._FALLA.findall(salida)), 2)

    def test_una_linea_que_no_es_falla_no_se_cuenta(self):
        self.assertEqual(core._FALLA.findall(u"[AVISO] a.md:1 — no es falla\n"),
                         [])


class ComprobarNoModificaNada(Base):
    """`RN-1`: se comprueba, no se corrige."""

    def test_la_carpeta_queda_igual(self):
        self.con_estandar()
        self.registrar()
        antes = self._retrato()
        core.comprobar("de-prueba")
        self.assertEqual(antes, self._retrato())

    def _retrato(self):
        retrato = []
        for base, _, archivos in os.walk(self.carpeta):
            for nombre in sorted(archivos):
                completa = os.path.join(base, nombre)
                retrato.append((os.path.relpath(completa, self.carpeta),
                                os.path.getsize(completa)))
        return sorted(retrato)
