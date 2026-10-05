"""`EP-025·HU-008`: el tablero suma el gasto de todos los proyectos, se filtra,
se actualiza solo y lee lo nuevo de los `.jsonl` al abrirse."""
import os
import shutil
import tempfile
from datetime import timedelta
from unittest import mock

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase
from django.utils import timezone

from core.consumo.formato import miles
from core.consumo.models import GastoDeArchivo, GastoDeEnganche, Llamada
from core.consumo.tablero import GastoDelPeriodo
from core.consumo.tests import SESION, escribir_jsonl, muestra
from core.cuentas.permisos import CONSULTA
from core.proyectos.models import Proyecto

HOY = timezone.now()
HACE_10_DIAS = HOY - timedelta(days=10)


class ConGasto(TestCase):
    """Dos proyectos: «uno» con gasto de hoy y de hace 10 días; «dos», de hoy."""

    def setUp(self):
        self.base = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.base, True)
        rutas = [tempfile.mkdtemp(), tempfile.mkdtemp()]
        for ruta in rutas:
            self.addCleanup(shutil.rmtree, ruta, True)
        self.uno = Proyecto.objects.create(nombre="uno", ruta=rutas[0])
        self.dos = Proyecto.objects.create(nombre="dos", ruta=rutas[1])
        self.llamada(self.uno, "a-1", HOY, entrada=1000, creada=200, leida=5000, salida=300)
        self.llamada(self.uno, "a-2", HACE_10_DIAS, entrada=7, creada=0, leida=0, salida=0)
        self.llamada(self.dos, "b-1", HOY, entrada=10, creada=0, leida=0, salida=5, sesion="s-2")
        for n in range(3):
            GastoDeEnganche.objects.create(proyecto=self.uno, sesion="s-1", identificador=f"e-{n}", fecha=HOY,
                                           nombre="Revisando las reglas...", caracteres=350)
        for n in range(2):
            GastoDeArchivo.objects.create(proyecto=self.uno, sesion="s-1", identificador=f"t-{n}", fecha=HOY,
                                          ruta="C:/p/analisis.md", caracteres=7000)
        parche = mock.patch("core.consumo.guardar.proyectos_de_claude", return_value=self.base)
        parche.start()
        self.addCleanup(parche.stop)

    @staticmethod
    def llamada(proyecto, mensaje, fecha, entrada, creada, leida, salida, sesion="s-1"):
        Llamada.objects.create(proyecto=proyecto, sesion=sesion, mensaje=mensaje, fecha=fecha, modelo="m",
                               entrada=entrada, cache_creada=creada, cache_leida=leida, salida=salida)

    def entrar(self):
        cuenta = get_user_model().objects.create_user("consulta")
        cuenta.groups.add(Group.objects.get(name=CONSULTA))
        self.client.force_login(cuenta)


class ElTableroSuma(ConGasto):
    """CP-001, paso 1."""

    def test_totales_y_niveles(self):
        todo = GastoDelPeriodo().todo()
        self.assertEqual({"llamadas": 2, "entrada": 1210, "salida": 305, "cache": 5000, "total": 6515},
                         todo["totales"])
        self.assertEqual(["uno", "dos"], [p["proyecto__nombre"] for p in todo["proyectos"]])
        self.assertEqual(6500, todo["proyectos"][0]["total"])
        self.assertEqual({"s-1", "s-2"}, {s["sesion"] for s in todo["sesiones"]})
        self.assertEqual([{"nombre": "Revisando las reglas...", "veces": 3, "tokens": 300}], todo["enganches"])
        self.assertEqual([{"nombre": "C:/p/analisis.md", "veces": 2, "tokens": 4000}], todo["archivos"])

    def test_por_dia_trae_cada_dia_y_hoy_al_final(self):
        dias = GastoDelPeriodo().todo()["graficas"]["dias"]
        self.assertEqual(7, len(dias["fechas"]))
        self.assertEqual(6515, dias["totales"][-1])
        self.assertEqual(0, sum(dias["totales"][:-1]))


class LaPaginaMuestraElGasto(ConGasto):
    """CP-001, pasos 2 y 3."""

    def test_con_cuenta_de_consulta(self):
        self.entrar()
        respuesta = self.client.get("/gasto/")
        self.assertEqual(200, respuesta.status_code)
        self.assertContains(respuesta, "1.210")
        self.assertContains(respuesta, "5.000")
        self.assertContains(respuesta, 'id="datos-graficas"')
        self.assertContains(respuesta, "Gasto</span>")

    def test_sin_cuenta_manda_a_entrar(self):
        respuesta = self.client.get("/gasto/")
        self.assertEqual(302, respuesta.status_code)
        self.assertIn("/entrar/", respuesta["Location"])

    def test_miles_con_punto(self):
        self.assertEqual(("1.756.000", "0", "999"), (miles(1756000), miles(None), miles(999)))


class SeFiltra(ConGasto):
    """CP-002."""

    def setUp(self):
        super().setUp()
        self.entrar()

    def totales(self, consulta):
        return self.client.get("/gasto/datos/" + consulta).context["totales"]

    def test_por_proyecto(self):
        self.assertEqual(1, self.totales(f"?proyecto={self.dos.pk}")["llamadas"])

    def test_por_periodo(self):
        self.assertEqual(2, self.totales("?dias=7")["llamadas"])
        self.assertEqual(3, self.totales("?dias=30")["llamadas"])

    def test_lo_que_no_existe_se_ignora(self):
        self.assertEqual(2, self.totales("?dias=99&proyecto=x")["llamadas"])
        self.assertEqual(2, self.totales("?dias=abc&proyecto=9999")["llamadas"])


class SeActualizaSolo(ConGasto):
    """CP-003."""

    def test_la_parte_que_se_recarga_trae_lo_nuevo(self):
        self.entrar()
        antes = self.client.get("/gasto/datos/").context["totales"]["llamadas"]
        self.llamada(self.dos, "b-2", HOY, entrada=1, creada=0, leida=0, salida=1, sesion="s-2")
        self.assertEqual(antes + 1, self.client.get("/gasto/datos/").context["totales"]["llamadas"])

    def test_la_pagina_pide_la_parte_cada_10_segundos(self):
        self.entrar()
        respuesta = self.client.get(f"/gasto/?proyecto={self.uno.pk}&dias=30")
        self.assertContains(respuesta, 'hx-trigger="every 10s"')
        self.assertContains(respuesta, f'hx-get="/gasto/datos/?dias=30&amp;proyecto={self.uno.pk}"')

    def test_al_abrir_lee_lo_nuevo_del_jsonl(self):
        carpeta = os.path.join(self.base, self.uno.carpeta_claude)
        os.makedirs(carpeta)
        escribir_jsonl(os.path.join(carpeta, SESION + ".jsonl"), muestra())
        self.entrar()
        self.client.get("/gasto/")
        self.assertTrue(Llamada.objects.filter(mensaje="m-1").exists())
        self.client.get("/gasto/datos/")
        self.assertEqual(1, Llamada.objects.filter(mensaje="m-1").count())
