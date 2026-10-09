"""`EP-025·HU-030` · El Resumen del gasto suma por hora en la base y la pantalla junta los avisos.

CP-001 y CP-003 del plan de pruebas; CP-002 es la medición sobre la base real."""
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import connection
from django.test import TestCase
from django.test.utils import CaptureQueriesContext
from django.utils import timezone

from core.consumo.models import Llamada
from core.consumo.tablero import GastoDelPeriodo
from core.cuentas.permisos import CONSULTA
from core.proyectos.models import Proyecto


class CadaLlamadaEnSuDia(TestCase):
    """CP-001."""

    def setUp(self):
        proyecto = Proyecto.objects.create(nombre="uno", ruta="C:/no/existe/uno")
        self.ahora = timezone.localtime().replace(hour=15, minute=0, second=0, microsecond=0)
        hoy = self.ahora.replace(hour=0)
        for n, (fecha, entrada) in enumerate(((hoy - timedelta(minutes=30), 100),     # ayer, 23:30
                                              (hoy + timedelta(minutes=30), 20),      # hoy, 00:30
                                              (hoy + timedelta(hours=12), 3),         # hoy, mediodía
                                              (hoy + timedelta(hours=12, minutes=5), 0))):
            Llamada.objects.create(proyecto=proyecto, sesion="s", mensaje="m-%d" % n, fecha=fecha, modelo="m",
                                   entrada=entrada, cache_creada=1, cache_leida=0, salida=0)

    def test_por_tipo_cada_llamada_cae_en_su_dia_local(self):
        dias = GastoDelPeriodo(ahora=self.ahora).por_dia_por_tipo()
        self.assertEqual([100, 23], dias["entrada"][-2:])
        self.assertEqual([1, 3], dias["creada"][-2:])
        self.assertEqual(0, sum(dias["entrada"][:-2]))

    def test_el_total_por_dia_da_lo_mismo(self):
        dias = GastoDelPeriodo(ahora=self.ahora).por_dia()
        self.assertEqual([101, 26], [total for _dia, total in dias[-2:]])
        self.assertEqual(7, len(dias))

    def test_la_base_devuelve_una_fila_por_hora(self):
        with CaptureQueriesContext(connection) as consultas:
            GastoDelPeriodo(ahora=self.ahora).por_dia_por_tipo()
        self.assertEqual(1, len(consultas))
        # La base agrupa: las dos llamadas del mediodía llegan sumadas en una fila.
        self.assertIn("GROUP BY", consultas[0]["sql"].upper())


class LaPantallaJuntaLosAvisos(TestCase):
    """CP-003."""

    def setUp(self):
        cuenta = get_user_model().objects.create_user("consulta")
        cuenta.groups.add(Group.objects.get(name=CONSULTA))
        self.client.force_login(cuenta)
        self.pagina = self.client.get("/gasto/").content.decode("utf-8")

    def test_el_aviso_pasa_por_la_espera_de_30_segundos(self):
        self.assertIn("var ESPERA_ENTRE_REFRESCOS = 30000;", self.pagina)
        self.assertIn('addEventListener("gasto", alLlegarAviso)', self.pagina)
        aviso = self.pagina.index('addEventListener("gasto"')
        self.assertNotIn('dispatchEvent(new Event("actualizar"))', self.pagina[aviso:aviso + 80])

    def test_escondida_no_refresca_y_al_volver_si(self):
        self.assertIn('addEventListener("visibilitychange"', self.pagina)
        self.assertIn("if (document.hidden) { return; }", self.pagina)
        self.assertIn("if (!document.hidden && llegoAviso) { alLlegarAviso(); }", self.pagina)

    def test_el_boton_actualiza_en_el_momento(self):
        boton = self.pagina.index('getElementById("actualizar").addEventListener("click"')
        self.assertIn('document.body.dispatchEvent(new Event("actualizar"));', self.pagina[boton:boton + 150])
