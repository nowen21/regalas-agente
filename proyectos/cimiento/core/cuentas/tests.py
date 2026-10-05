"""Quién entra y qué puede hacer: entrada obligatoria, contraseña equivocada,
permiso por grupo y la orden `crear_cuenta`. Corren en la base de pruebas que
Django crea en MariaDB."""
import io
from unittest import mock

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.management import CommandError, call_command
from django.http import HttpResponse
from django.test import TestCase, override_settings
from django.urls import include, path
from django.views import View

from core.cuentas.permisos import ADMINISTRADOR, CONSULTA, SoloAdministrador

CLAVE = "una-clave-larga-de-prueba"


class VistaDeAdministrador(SoloAdministrador, View):
    def get(self, peticion):
        return HttpResponse("contenido protegido")


urlpatterns = [
    path("", include("config.urls")),
    path("prueba/administrar/", VistaDeAdministrador.as_view()),
]


def cuenta(usuario, grupo=None, **extra):
    nueva = get_user_model().objects.create_user(usuario, password=CLAVE, **extra)
    if grupo:
        nueva.groups.add(Group.objects.get(name=grupo))
    return nueva


class SinCuentaSePideEntrar(TestCase):

    def test_la_pagina_de_inicio_manda_a_entrar(self):
        respuesta = self.client.get("/")
        self.assertRedirects(respuesta, "/entrar/?next=/", fetch_redirect_response=False)

    def test_con_la_cuenta_vuelve_a_la_pagina_pedida(self):
        cuenta("ana")
        respuesta = self.client.post("/entrar/", {"username": "ana", "password": CLAVE, "next": "/"})
        self.assertRedirects(respuesta, "/", fetch_redirect_response=False)
        pagina = self.client.get("/")
        self.assertContains(pagina, "ana")
        self.assertContains(pagina, "Salir")

    def test_salir_vuelve_a_pedir_entrar(self):
        self.client.force_login(cuenta("ana"))
        self.assertRedirects(self.client.post("/salir/"), "/entrar/", fetch_redirect_response=False)
        self.assertEqual(self.client.get("/").status_code, 302)

    def test_la_entrada_se_ve_sin_cuenta(self):
        self.assertContains(self.client.get("/entrar/"), "Contraseña")


class LaContrasenaEquivocadaNoDejaEntrar(TestCase):

    def entrar(self, usuario, clave):
        return self.client.post("/entrar/", {"username": usuario, "password": clave})

    def test_contrasena_equivocada(self):
        cuenta("ana")
        respuesta = self.entrar("ana", "otra-cosa")
        self.assertContains(respuesta, "El usuario o la contraseña no son correctos.")
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_usuario_que_no_existe_recibe_el_mismo_mensaje(self):
        cuenta("ana")
        for usuario in ("ana", "nadie"):
            with self.subTest(usuario=usuario):
                respuesta = self.entrar(usuario, "otra-cosa")
                self.assertContains(respuesta, "El usuario o la contraseña no son correctos.")
                self.assertNotContains(respuesta, "no existe")


@override_settings(ROOT_URLCONF=__name__)
class CadaGrupoHaceLoSuyo(TestCase):

    def pedir_como(self, quien):
        self.client.force_login(quien)
        return self.client.get("/prueba/administrar/")

    def test_consulta_recibe_403_sin_el_contenido(self):
        respuesta = self.pedir_como(cuenta("carlos", CONSULTA))
        self.assertContains(respuesta, "No tiene permiso", status_code=403)
        self.assertNotContains(respuesta, "contenido protegido", status_code=403)

    def test_administrador_la_abre(self):
        self.assertContains(self.pedir_como(cuenta("ana", ADMINISTRADOR)), "contenido protegido")

    def test_un_superusuario_cuenta_como_administrador(self):
        jefe = cuenta("jefe", is_superuser=True, is_staff=True)
        self.assertContains(self.pedir_como(jefe), "contenido protegido")

    def test_sin_grupo_tampoco_puede(self):
        self.assertEqual(self.pedir_como(cuenta("suelto")).status_code, 403)


class CrearCuenta(TestCase):

    def crear(self, usuario="u", grupo=CONSULTA, claves=(CLAVE, CLAVE)):
        salida = io.StringIO()
        with mock.patch("core.cuentas.management.commands.crear_cuenta.Command.pedir_clave",
                        return_value=claves):
            call_command("crear_cuenta", usuario=usuario, grupo=grupo, stdout=salida)
        return salida.getvalue()

    def test_los_dos_grupos_existen(self):
        self.assertTrue(Group.objects.filter(name=ADMINISTRADOR).exists())
        self.assertTrue(Group.objects.filter(name=CONSULTA).exists())

    def test_crea_la_cuenta_en_su_grupo(self):
        self.assertIn("quedó en el grupo consulta", self.crear())
        nueva = get_user_model().objects.get(username="u")
        self.assertTrue(nueva.groups.filter(name=CONSULTA).exists())
        self.assertTrue(nueva.check_password(CLAVE))
        self.assertNotEqual(nueva.password, CLAVE)

    def test_claves_distintas_no_crean_nada(self):
        with self.assertRaisesMessage(CommandError, "no coinciden"):
            self.crear(claves=(CLAVE, CLAVE + "x"))
        self.assertFalse(get_user_model().objects.filter(username="u").exists())

    def test_grupo_que_no_existe(self):
        with self.assertRaisesMessage(CommandError, "administrador, consulta"):
            self.crear(grupo="jefes")

    def test_usuario_que_ya_existe_no_se_cambia(self):
        cuenta("u", ADMINISTRADOR)
        with self.assertRaisesMessage(CommandError, "ya existe"):
            self.crear()
        self.assertFalse(get_user_model().objects.get(username="u").groups.filter(name=CONSULTA).exists())

    def test_una_clave_debil_se_rechaza(self):
        with self.assertRaises(CommandError):
            self.crear(claves=("123", "123"))
        self.assertFalse(get_user_model().objects.filter(username="u").exists())
