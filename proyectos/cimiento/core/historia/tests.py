# -*- coding: utf-8 -*-
"""`EP-026·HU-001` · Pruebas de la historia: CP-001 a CP-004 de la fase A."""
import shutil
import tempfile

from django.contrib.auth.models import Group, User
from django.db import connection
from django.test import TestCase, TransactionTestCase

from core.cuentas.permisos import ADMINISTRADOR, CONSULTA
from core.enganches.estado_en_base import EstadoEnBase
from core.proyectos.models import AjusteDelProyecto, Proyecto

from .models import BORRAR, CAMBIAR, CREAR, Cambio
from .registro import CAMBIADA, quien_y_por_que


def _proyecto(test):
    raiz = tempfile.mkdtemp()
    test.addCleanup(shutil.rmtree, raiz, True)
    return Proyecto.objects.create(nombre="uno", ruta=raiz)


class CrearCambiarYBorrarQuedan(TestCase):
    """CP-001."""

    def setUp(self):
        self.cuenta = User.objects.create_user("ana", password="una-clave-larga-1")
        self.proyecto = _proyecto(self)

    def ultimo(self, tabla="proyectos.ajustedelproyecto"):
        return Cambio.objects.filter(tabla=tabla).order_by("-id").first()

    def test_crear_cambiar_y_borrar(self):
        ajuste = AjusteDelProyecto.objects.create(proyecto=self.proyecto, clave="limite_enganche", valor="2000")
        creado = self.ultimo()
        self.assertEqual(CREAR, creado.accion)
        self.assertEqual("2000", creado.despues["valor"])
        self.assertEqual(str(ajuste.pk), creado.fila)

        with quien_y_por_que(cuenta=self.cuenta, motivo="el enganche de reglas pasa de 2000"):
            ajuste.valor = "3000"
            ajuste.save()
        cambio = self.ultimo()
        self.assertEqual(CAMBIAR, cambio.accion)
        self.assertEqual({"valor": "2000"}, cambio.antes)
        self.assertEqual({"valor": "3000"}, cambio.despues)
        self.assertEqual(self.cuenta, cambio.cuenta)
        self.assertEqual("el enganche de reglas pasa de 2000", cambio.motivo)

        antes = Cambio.objects.count()
        ajuste.save()
        self.assertEqual(antes, Cambio.objects.count())

        pk = ajuste.pk
        ajuste.delete()
        borrado = self.ultimo()
        self.assertEqual(BORRAR, borrado.accion)
        self.assertEqual("3000", borrado.antes["valor"])
        self.assertEqual(str(pk), borrado.fila)

    def test_las_cuentas_y_los_grupos_tambien(self):
        grupo = Group.objects.create(name="revisores")
        self.assertEqual(CREAR, self.ultimo("auth.group").accion)
        self.cuenta.groups.add(grupo)
        cambio = self.ultimo("auth.user")
        self.assertEqual({"groups+": [grupo.pk]}, cambio.despues)

    def test_sin_cuenta_queda_a_nombre_del_programa(self):
        AjusteDelProyecto.objects.create(proyecto=self.proyecto, clave="limite_archivo", valor="9000")
        self.assertTrue(self.ultimo().quien)
        self.assertIsNone(self.ultimo().cuenta)


def _ajustes():
    d = connection.settings_dict
    return {"NAME": d["NAME"], "USER": d["USER"], "PASSWORD": d["PASSWORD"], "HOST": d["HOST"], "PORT": d["PORT"]}


class LoQueEscribeElEngancheQueda(TransactionTestCase):
    """CP-002. Con `TransactionTestCase`: el enganche escribe por otra conexión."""

    serialized_rollback = True

    def test_guardar_y_borrar_el_estado(self):
        proyecto = _proyecto(self)
        base = EstadoEnBase(proyecto.ruta, ajustes=_ajustes())
        base.guardar({"sesion": "historico-chat/s.md", "analisis": "pendientes/7/analisis-1.md", "desde": 1})
        base.guardar({"sesion": "historico-chat/s.md", "analisis": "pendientes/7/analisis-1.md", "desde": 1,
                      "pausa": 4})
        base.borrar("historico-chat/s.md")
        cambios = list(Cambio.objects.filter(tabla="proyectos.analisisprendido").order_by("id"))
        self.assertEqual([CREAR, CAMBIAR, BORRAR], [c.accion for c in cambios])
        self.assertEqual({"agente"}, {c.quien for c in cambios})
        self.assertEqual({"pausa": 4}, cambios[1].despues)


class DeshacerDesdeLaPantalla(TestCase):
    """CP-003."""

    def setUp(self):
        self.admin = User.objects.create_user("admin", password="una-clave-larga-1")
        self.admin.groups.add(Group.objects.get_or_create(name=ADMINISTRADOR)[0])
        self.consulta = User.objects.create_user("mira", password="una-clave-larga-1")
        self.consulta.groups.add(Group.objects.get_or_create(name=CONSULTA)[0])
        proyecto = _proyecto(self)
        self.ajuste = AjusteDelProyecto.objects.create(proyecto=proyecto, clave="limite_enganche", valor="2000")
        self.ajuste.valor = "3000"
        self.ajuste.save()
        self.cambio = Cambio.objects.filter(tabla="proyectos.ajustedelproyecto", accion=CAMBIAR).latest("id")

    def test_la_lista_muestra_el_cambio(self):
        self.client.force_login(self.consulta)
        respuesta = self.client.get("/historia/")
        self.assertContains(respuesta, "proyectos.ajustedelproyecto")
        self.assertNotContains(respuesta, "/deshacer/")

    def test_consulta_no_deshace(self):
        self.client.force_login(self.consulta)
        self.assertEqual(403, self.client.post("/historia/%d/deshacer/" % self.cambio.pk).status_code)
        self.ajuste.refresh_from_db()
        self.assertEqual("3000", self.ajuste.valor)

    def test_el_administrador_deshace_y_queda_otro_cambio(self):
        self.client.force_login(self.admin)
        self.client.post("/historia/%d/deshacer/" % self.cambio.pk, {"motivo": "me equivoqué"})
        self.ajuste.refresh_from_db()
        self.assertEqual("2000", self.ajuste.valor)
        nuevo = Cambio.objects.latest("id")
        self.assertEqual(self.cambio, nuevo.deshace)
        self.assertEqual(self.admin, nuevo.cuenta)
        self.assertIn("deshace el cambio %d" % self.cambio.pk, nuevo.motivo)


class SinClavesEnLaHistoria(TestCase):
    """CP-004."""

    def test_la_contrasena_queda_como_cambiada(self):
        cuenta = User.objects.create_user("ana", password="una-clave-larga-1")
        cuenta.set_password("otra-clave-larga-2")
        cuenta.save()
        cambio = Cambio.objects.filter(tabla="auth.user", accion=CAMBIAR).latest("id")
        self.assertEqual(CAMBIADA, cambio.despues["password"])
        self.assertEqual(CAMBIADA, cambio.antes["password"])

    def test_la_clave_del_motivo_se_tapa(self):
        proyecto = _proyecto(self)
        clave = "API_KEY=" + "abc123" * 4
        with quien_y_por_que(motivo="lo pegué así: " + clave):
            AjusteDelProyecto.objects.create(proyecto=proyecto, clave="limite_enganche", valor="2000")
        cambio = Cambio.objects.latest("id")
        self.assertNotIn("abc123abc123", cambio.motivo)
