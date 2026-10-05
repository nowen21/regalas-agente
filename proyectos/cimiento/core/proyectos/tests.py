"""El registro de proyectos: la carpeta de Claude Code, el registro, lo que no
vale, la edición y el permiso por grupo. Las rutas son carpetas temporales."""
import os
import tempfile

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import SimpleTestCase, TestCase

from core.cuentas.permisos import ADMINISTRADOR, CONSULTA
from core.proyectos.claude import carpeta_de_claude, nombre_de_carpeta
from core.proyectos.models import LIMITE_ARCHIVO, LIMITE_ENGANCHE, Proyecto


class LaCarpetaDeClaudeSaleDeLaRuta(SimpleTestCase):

    def test_la_del_estandar(self):
        self.assertEqual(nombre_de_carpeta("C:\\Ing. Jose\\ia\\agente"), "c--Ing--Jose-ia-agente")

    def test_cada_caracter_que_no_es_letra_ni_numero_da_guion(self):
        self.assertEqual(nombre_de_carpeta("C:\\Escom\\Especialización en ciberseguridad\\sena - copia"),
                         "c--Escom-Especializaci-n-en-ciberseguridad-sena---copia")

    def test_si_existe_con_la_unidad_en_mayuscula_la_encuentra(self):
        # En Windows las dos letras dan la misma carpeta; en otro sistema, la
        # función devuelve la que existe.
        with tempfile.TemporaryDirectory() as base:
            os.makedirs(os.path.join(base, "C--X-y"))
            self.assertTrue(os.path.isdir(os.path.join(base, carpeta_de_claude("C:\\X\\y", base))))

    def test_si_no_existe_ninguna_queda_en_minuscula(self):
        with tempfile.TemporaryDirectory() as base:
            self.assertEqual(carpeta_de_claude("C:\\X\\y", base), "c--X-y")


class ConCuentas(TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.ruta = self.tmp.name

    def entrar(self, grupo):
        cuenta = get_user_model().objects.create_user(f"cuenta-{grupo}")
        cuenta.groups.add(Group.objects.get(name=grupo))
        self.client.force_login(cuenta)

    def registrar(self, **datos):
        datos = {"nombre": "agente", "ruta": self.ruta, "limite_enganche": LIMITE_ENGANCHE,
                 "limite_archivo": LIMITE_ARCHIVO, "activo": "on", **datos}
        return self.client.post("/proyectos/registrar/", datos)


class UnAdministradorRegistra(ConCuentas):

    def setUp(self):
        super().setUp()
        self.entrar(ADMINISTRADOR)

    def test_queda_en_la_lista_con_su_carpeta(self):
        self.assertRedirects(self.registrar(), "/proyectos/", fetch_redirect_response=False)
        proyecto = Proyecto.objects.get(nombre="agente")
        self.assertTrue(proyecto.activo)
        self.assertEqual(proyecto.carpeta_claude, carpeta_de_claude(self.ruta))
        lista = self.client.get("/proyectos/")
        self.assertContains(lista, "agente")
        self.assertContains(lista, proyecto.carpeta_claude)

    def test_sin_limites_quedan_los_de_por_defecto(self):
        proyecto = Proyecto.objects.create(nombre="x", ruta=self.ruta)
        self.assertEqual((proyecto.limite_enganche, proyecto.limite_archivo), (2000, 10000))

    def test_con_limites_escritos(self):
        self.registrar(limite_enganche=500, limite_archivo=700)
        proyecto = Proyecto.objects.get(nombre="agente")
        self.assertEqual((proyecto.limite_enganche, proyecto.limite_archivo), (500, 700))


class LoQueNoValeNoSeGuarda(ConCuentas):

    def setUp(self):
        super().setUp()
        self.entrar(ADMINISTRADOR)
        Proyecto.objects.create(nombre="existente", ruta=self.ruta)

    def no_guarda(self, mensaje, **datos):
        respuesta = self.registrar(**datos)
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, mensaje)
        self.assertEqual(Proyecto.objects.count(), 1)

    def test_ruta_que_no_existe(self):
        self.no_guarda("La carpeta no existe", nombre="otro", ruta=os.path.join(self.ruta, "no-esta"))

    def test_ruta_repetida_con_otras_mayusculas(self):
        self.no_guarda("ya está registrada como «existente»", nombre="otro", ruta=self.ruta.upper())

    def test_nombre_repetido(self):
        otra = tempfile.TemporaryDirectory()
        self.addCleanup(otra.cleanup)
        self.no_guarda("Ya existe", nombre="existente", ruta=otra.name)

    def test_limites_cero_o_negativos(self):
        otra = tempfile.TemporaryDirectory()
        self.addCleanup(otra.cleanup)
        for limite in (0, -5):
            with self.subTest(limite=limite):
                self.no_guarda("mayor o igual a", nombre="otro", ruta=otra.name, limite_enganche=limite)

    def test_nombre_vacio(self):
        self.no_guarda("Este campo es obligatorio", nombre="")


class SeEditaYSeDesactiva(ConCuentas):

    def setUp(self):
        super().setUp()
        self.entrar(ADMINISTRADOR)
        self.proyecto = Proyecto.objects.create(nombre="agente", ruta=self.ruta)

    def editar(self, **datos):
        datos = {"nombre": "agente", "ruta": self.ruta, "limite_enganche": 2000,
                 "limite_archivo": 10000, "activo": "on", **datos}
        return self.client.post(f"/proyectos/{self.proyecto.pk}/editar/", datos)

    def test_cambiar_un_limite(self):
        self.assertRedirects(self.editar(limite_enganche=1234), "/proyectos/", fetch_redirect_response=False)
        self.assertContains(self.client.get("/proyectos/"), "1234")

    def test_desactivar_no_borra(self):
        datos = {"nombre": "agente", "ruta": self.ruta, "limite_enganche": 2000, "limite_archivo": 10000}
        self.client.post(f"/proyectos/{self.proyecto.pk}/editar/", datos)
        self.proyecto.refresh_from_db()
        self.assertFalse(self.proyecto.activo)
        self.assertContains(self.client.get("/proyectos/"), "Inactivo")

    def test_editar_sin_cambiar_la_ruta_no_la_da_por_repetida(self):
        self.assertEqual(self.editar(nombre="agente nuevo").status_code, 302)


class ConsultaSoloVe(ConCuentas):

    def setUp(self):
        super().setUp()
        self.entrar(CONSULTA)
        self.proyecto = Proyecto.objects.create(nombre="agente", ruta=self.ruta)

    def test_ve_la_lista_sin_botones(self):
        lista = self.client.get("/proyectos/")
        self.assertContains(lista, "agente")
        self.assertNotContains(lista, "Registrar")
        self.assertNotContains(lista, "Editar")

    def test_los_formularios_le_dan_403(self):
        self.assertEqual(self.client.get("/proyectos/registrar/").status_code, 403)
        self.assertEqual(self.client.get(f"/proyectos/{self.proyecto.pk}/editar/").status_code, 403)

    def test_registrar_por_post_no_guarda(self):
        otra = tempfile.TemporaryDirectory()
        self.addCleanup(otra.cleanup)
        self.assertEqual(self.registrar(nombre="otro", ruta=otra.name).status_code, 403)
        self.assertEqual(Proyecto.objects.count(), 1)
