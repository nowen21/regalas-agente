"""`EP-025·HU-008`: el tablero suma el gasto de todos los proyectos y se filtra.
`EP-025·HU-026`: la franja de arriba y las cinco pestañas, sin intervalos."""
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
        self.assertContains(respuesta, "6.515")
        self.assertContains(respuesta, 'id="franja"')
        self.assertContains(respuesta, 'id="pestana"')
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
        return self.client.get("/gasto/franja/" + consulta).context["franja"]

    def test_por_proyecto(self):
        self.assertEqual(1, self.totales(f"?proyecto={self.dos.pk}")["llamadas"])

    def test_por_periodo(self):
        self.assertEqual(2, self.totales("?dias=7")["llamadas"])
        self.assertEqual(3, self.totales("?dias=30")["llamadas"])

    def test_lo_que_no_existe_se_ignora(self):
        self.assertEqual(2, self.totales("?dias=99&proyecto=x")["llamadas"])
        self.assertEqual(2, self.totales("?dias=abc&proyecto=9999")["llamadas"])


class SeActualizaConElBoton(ConGasto):
    """CP-003 de la HU-008, rehecho en la `HU-026`: nada se pide cada cierto tiempo."""

    def test_la_parte_que_se_recarga_trae_lo_nuevo(self):
        self.entrar()
        antes = self.client.get("/gasto/franja/").context["franja"]["llamadas"]
        self.llamada(self.dos, "b-2", HOY, entrada=1, creada=0, leida=0, salida=1, sesion="s-2")
        self.assertEqual(antes + 1, self.client.get("/gasto/franja/").context["franja"]["llamadas"])

    def test_sin_intervalos_y_con_los_filtros(self):
        self.entrar()
        respuesta = self.client.get(f"/gasto/?proyecto={self.uno.pk}&dias=30")
        self.assertNotContains(respuesta, "every ")
        self.assertContains(respuesta, 'hx-trigger="actualizar from:body"')
        self.assertContains(respuesta, f'hx-get="/gasto/franja/?dias=30&amp;proyecto={self.uno.pk}"')

    def test_al_abrir_no_lee_el_jsonl(self):
        """`EP-025·HU-011 · CP-003`: lo trae el vigilante; el tablero solo consulta la base."""
        carpeta = os.path.join(self.base, self.uno.carpeta_claude)
        os.makedirs(carpeta)
        escribir_jsonl(os.path.join(carpeta, SESION + ".jsonl"), muestra())
        self.entrar()
        with mock.patch("core.consumo.guardar.LectorDeClaudeCode") as lector:
            self.assertEqual(200, self.client.get("/gasto/").status_code)
            self.client.get("/gasto/franja/")
            self.client.get("/gasto/pestana/resumen/")
        lector.assert_not_called()
        self.assertFalse(Llamada.objects.filter(mensaje="m-1").exists())


class LaFranja(ConGasto):
    """`EP-025·HU-026` · CP-001 y CP-002."""

    def setUp(self):
        super().setUp()
        self.entrar()

    def test_total_llamadas_cache_y_maximo(self):
        franja = self.client.get("/gasto/franja/").context["franja"]
        self.assertEqual((6515, 2, 77, 6200), (franja["total"], franja["llamadas"], franja["cache_pct"], franja["maximo"]))
        # El tramo anterior de 7 días trae la llamada de hace 10 días: 7 tokens.
        self.assertEqual((7, round((6515 - 7) * 100 / 7)), (franja["anterior"], franja["variacion"]))
        sin_antes = self.client.get(f"/gasto/franja/?proyecto={self.dos.pk}").context["franja"]
        self.assertIsNone(sin_antes["variacion"])
        self.assertContains(self.client.get(f"/gasto/franja/?proyecto={self.dos.pk}"), "Sin gasto en el tramo anterior")

    def test_sin_cuenta_manda_a_entrar(self):
        self.client.logout()
        self.assertEqual(302, self.client.get("/gasto/franja/").status_code)

    def test_compara_con_el_tramo_anterior_a_la_misma_hora(self):
        ahora = timezone.localtime().replace(hour=12, minute=0, second=0, microsecond=0)
        ayer = ahora - timedelta(days=1)
        self.llamada(self.dos, "ayer-antes", ayer - timedelta(hours=1), entrada=100, creada=0, leida=0, salida=0)
        self.llamada(self.dos, "ayer-despues", ayer + timedelta(hours=1), entrada=900, creada=0, leida=0, salida=0)
        gasto = GastoDelPeriodo(1, self.dos, ahora=ahora)
        self.assertEqual(100, gasto.anterior())
        self.assertEqual(round((gasto.totales()["total"] - 100) * 100 / 100), gasto.franja()["variacion"])


class LasPestanas(ConGasto):
    """`EP-025·HU-026` · CP-003 a CP-006."""

    def setUp(self):
        super().setUp()
        self.entrar()

    def test_cada_pestana_tiene_su_ruta_y_la_que_no_existe_da_404(self):
        for nombre in ("resumen", "donde", "contexto", "ahorro", "actividad"):
            with self.subTest(pestana=nombre):
                self.assertEqual(200, self.client.get("/gasto/pestana/%s/" % nombre).status_code)
        self.assertEqual(404, self.client.get("/gasto/pestana/otra/").status_code)

    def test_resumen_trae_sus_dos_graficas(self):
        respuesta = self.client.get("/gasto/pestana/resumen/")
        self.assertContains(respuesta, 'id="datos-resumen"')
        self.assertEqual(4, len(respuesta.context["datos_graficas"]["tipos"]))
        self.assertEqual(5000, respuesta.context["datos_graficas"]["dias"]["leida"][-1])

    def test_donde_agrupa_con_porcentaje(self):
        filas = self.client.get("/gasto/pestana/donde/?agrupar=proyecto").context["filas"]
        self.assertEqual([("uno", 6500, 100), ("dos", 15, 0)], [(f["nombre"], f["total"], f["pct"]) for f in filas])
        self.assertEqual("modelo", self.client.get("/gasto/pestana/donde/?agrupar=modelo").context["por"])
        self.assertEqual("proyecto", self.client.get("/gasto/pestana/donde/?agrupar=nada").context["por"])

    def test_sin_repetidos(self):
        respuesta = self.client.get("/gasto/")
        self.assertNotContains(respuesta, "grafica-proyectos")
        # La tabla por tipo de token salió: los tipos solo van a la dona.
        self.assertNotIn("tipos", self.client.get("/gasto/pestana/resumen/").context)

    def test_contexto_trae_promedio_maximo_y_limite_sin_marcar(self):
        contexto = self.client.get(f"/gasto/pestana/contexto/?proyecto={self.uno.pk}").context
        self.assertEqual([("Revisando las reglas...", 3, 100, 100)],
                         [(f["nombre"], f["veces"], f["promedio"], f["maximo"]) for f in contexto["enganches"]])
        self.assertEqual(int(self.uno.ajuste("limite_enganche")), contexto["limite_enganche"])
        self.assertNotContains(self.client.get("/gasto/pestana/contexto/"), "pasa el límite")
