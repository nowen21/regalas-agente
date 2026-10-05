"""La base de las pantallas: la página de inicio, la base apagada y `preparar_base`.

La página se pide con una cuenta en la base de pruebas que Django crea en
MariaDB. La base apagada se prueba con la conexión sustituida o con un puerto
donde no hay servidor.
"""
import io
from unittest import mock

from django.contrib.auth import get_user_model
from django.contrib.staticfiles.views import serve
from django.core.management import CommandError, call_command
from django.db import OperationalError, connection
from django.http import Http404
from django.test import RequestFactory, SimpleTestCase, TestCase, override_settings

from core.inicio.base_de_datos import BaseDeDatos, BaseInalcanzable

AJUSTES = {"NAME": "cimiento", "USER": "root", "PASSWORD": "",
           "HOST": "127.0.0.1", "PORT": "3307"}

# Los que pide la plantilla común; vienen de `npm ci`.
ESTATICOS = ("css/tabler.min.css", "js/tabler.min.js", "htmx.min.js", "apexcharts.min.js")


class LaPaginaDeInicioUsaLaPlantillaComun(TestCase):
    """Con cuenta (`EP-025·HU-002`): sin ella, la página manda a entrar."""

    def setUp(self):
        self.client.force_login(get_user_model().objects.create_user("ana"))

    def pedir(self):
        with mock.patch.object(BaseDeDatos, "version", return_value="11.4.9"):
            return self.client.get("/")

    def test_responde_con_menu_y_cabecera(self):
        respuesta = self.pedir()
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "navbar-vertical")
        self.assertContains(respuesta, '<span class="nav-link-title">Inicio</span>', html=True)
        self.assertContains(respuesta, "page-title")

    def test_carga_tabler_htmx_y_apexcharts(self):
        respuesta = self.pedir()
        for archivo in ESTATICOS:
            self.assertContains(respuesta, f"/static/{archivo}")

    def test_dice_a_que_base_esta_conectada(self):
        nombre = connection.settings_dict["NAME"]
        self.assertContains(self.pedir(), f"Base de datos: {nombre}, en MariaDB 11.4.9")


@override_settings(DEBUG=True)     # la vista solo sirve en desarrollo
class LosEstaticosDeNpmSeSirven(SimpleTestCase):
    """Con prefijo en `STATICFILES_DIRS` Django no los servía en Windows: la
    plantilla los pedía y el navegador recibía 404 sin que nada lo dijera."""

    def test_la_vista_de_estaticos_los_entrega(self):
        for archivo in ESTATICOS:
            with self.subTest(archivo=archivo):
                try:
                    respuesta = serve(RequestFactory().get(f"/static/{archivo}"), archivo)
                except Http404:
                    self.fail(f"{archivo} no se sirve: correr `npm ci` en proyectos/cimiento/")
                self.assertEqual(respuesta.status_code, 200)


class SinBaseLaPantallaDiceQueHacer(SimpleTestCase):
    """Sin cuenta: la base se revisa antes que la entrada."""

    def test_responde_503_con_servidor_y_puerto(self):
        apagada = OperationalError(2003, "Can't connect to server on '127.0.0.1' (10061)")
        with mock.patch("core.inicio.middleware.connection") as conexion:
            conexion.ensure_connection.side_effect = apagada
            respuesta = self.client.get("/")
        self.assertEqual(respuesta.status_code, 503)
        self.assertContains(respuesta, "MariaDB no responde en", status_code=503)
        self.assertContains(respuesta, "Hay que prenderla", status_code=503)
        self.assertNotContains(respuesta, "10061", status_code=503)


class ElErrorSeTraduceAQueHacer(SimpleTestCase):

    def setUp(self):
        self.base = BaseDeDatos(AJUSTES)

    def test_servidor_apagado(self):
        self.assertIn("prenderla", self.base.explicar(OperationalError(2003, "x")))

    def test_usuario_sin_permiso(self):
        self.assertIn("DB_USUARIO", self.base.explicar(OperationalError(1045, "x")))

    def test_base_que_no_existe(self):
        self.assertIn("preparar_base", self.base.explicar(OperationalError(1049, "x")))

    def test_otro_error_da_su_codigo(self):
        self.assertIn("1146", self.base.explicar(OperationalError(1146, "x")))

    def test_un_puerto_sin_servidor_no_responde(self):
        sin_servidor = BaseDeDatos(dict(AJUSTES, PORT="3399"))
        with self.assertRaisesMessage(BaseInalcanzable, "no responde en 127.0.0.1:3399"):
            sin_servidor.crear_si_falta()


class LasTablasSonInnoDB(TestCase):
    """Con MyISAM, una escritura a medias queda a medias y Django no puede
    deshacer nada: las pruebas veían la base vaciada entre caso y caso."""

    def test_la_conexion_crea_tablas_innodb(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT DISTINCT ENGINE FROM information_schema.TABLES "
                           "WHERE TABLE_SCHEMA = %s AND TABLE_TYPE = 'BASE TABLE'",
                           [connection.settings_dict["NAME"]])
            self.assertEqual([fila[0] for fila in cursor.fetchall()], ["InnoDB"])

    def test_no_queda_nada_que_pasar(self):
        self.assertEqual(BaseDeDatos().pasar_a_innodb(), [])


class PrepararBase(SimpleTestCase):

    def correr(self):
        salida = io.StringIO()
        call_command("preparar_base", stdout=salida)
        return salida.getvalue()

    def test_sin_mariadb_falla_con_el_mensaje(self):
        with mock.patch.object(BaseDeDatos, "crear_si_falta",
                               side_effect=BaseInalcanzable("MariaDB no responde en x")):
            with self.assertRaisesMessage(CommandError, "MariaDB no responde en x"):
                self.correr()

    def test_crea_la_base_y_migra(self):
        with mock.patch.object(BaseDeDatos, "crear_si_falta", return_value=True), \
                mock.patch("core.inicio.management.commands.preparar_base.call_command") as migrar:
            salida = self.correr()
        migrar.assert_called_once_with("migrate", interactive=False, verbosity=0)
        self.assertIn("se creó ahora", salida)

    def test_dice_cuantas_tablas_paso_a_innodb(self):
        with mock.patch.object(BaseDeDatos, "crear_si_falta", return_value=False), \
                mock.patch.object(BaseDeDatos, "pasar_a_innodb", return_value=["a", "b"]), \
                mock.patch("core.inicio.management.commands.preparar_base.call_command"):
            self.assertIn("2 tabla(s) pasaron de MyISAM a InnoDB", self.correr())

    def test_repetirla_no_crea_otra_vez(self):
        with mock.patch.object(BaseDeDatos, "crear_si_falta", return_value=False), \
                mock.patch("core.inicio.management.commands.preparar_base.call_command"):
            salida = self.correr()
        self.assertNotIn("se creó", salida)
        self.assertIn("está lista", salida)
