"""Los niveles de las reglas: el catálogo, el cambio en un solo proyecto, el
núcleo y los envíos inválidos, el historial y el permiso por grupo."""
import tempfile

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import SimpleTestCase, TestCase

from core.cuentas.permisos import ADMINISTRADOR, CONSULTA
from core.niveles.catalogo import es_del_nucleo, reglas_configurables
from core.niveles.models import AVISA, CambioDeNivel, NivelDeRegla
from core.proyectos.models import Proyecto

REGLA = "02·F8"


class ElCatalogo(SimpleTestCase):

    def test_trae_las_reglas_del_flujo(self):
        ids = {regla.id for regla in reglas_configurables()}
        self.assertIn(REGLA, ids)
        self.assertGreater(len(ids), 200)

    def test_no_trae_el_nucleo(self):
        self.assertFalse([r.id for r in reglas_configurables() if es_del_nucleo(r.id)])

    def test_reconoce_el_nucleo(self):
        self.assertTrue(es_del_nucleo("00·N1"))
        self.assertFalse(es_del_nucleo("00·ID8"))
        self.assertFalse(es_del_nucleo(REGLA))


class ConProyectos(TestCase):

    def setUp(self):
        carpetas = [tempfile.TemporaryDirectory() for _ in range(2)]
        for carpeta in carpetas:
            self.addCleanup(carpeta.cleanup)
        self.uno = Proyecto.objects.create(nombre="uno", ruta=carpetas[0].name)
        self.otro = Proyecto.objects.create(nombre="otro", ruta=carpetas[1].name)

    def entrar(self, grupo):
        self.cuenta = get_user_model().objects.create_user(f"cuenta-{grupo}")
        self.cuenta.groups.add(Group.objects.get(name=grupo))
        self.client.force_login(self.cuenta)

    def enviar(self, proyecto, **niveles):
        datos = {f"nivel-{regla}": nivel for regla, nivel in niveles.items()}
        return self.client.post(f"/proyectos/{proyecto.pk}/reglas/", datos, follow=True)

    def nivel(self, proyecto, regla=REGLA):
        fila = NivelDeRegla.objects.filter(proyecto=proyecto, regla=regla).first()
        return fila.nivel if fila else "frena"


class UnAdministradorCambiaUnNivel(ConProyectos):

    def setUp(self):
        super().setUp()
        self.entrar(ADMINISTRADOR)

    def test_todas_empiezan_en_frena(self):
        pagina = self.client.get(f"/proyectos/{self.uno.pk}/reglas/")
        self.assertContains(pagina, REGLA)
        self.assertNotContains(pagina, 'value="avisa" selected')

    def test_cambia_solo_en_ese_proyecto(self):
        respuesta = self.enviar(self.uno, **{REGLA: AVISA})
        self.assertContains(respuesta, "1 nivel(es) cambiado(s).")
        self.assertEqual(self.nivel(self.uno), AVISA)
        self.assertEqual(self.nivel(self.otro), "frena")

    def test_enviar_sin_cambios_no_guarda_nada(self):
        self.enviar(self.uno, **{REGLA: "frena"})
        self.assertEqual(NivelDeRegla.objects.count(), 0)
        self.assertEqual(CambioDeNivel.objects.count(), 0)


class ElNucleoYLoInvalidoNoSeGuardan(ConProyectos):

    def setUp(self):
        super().setUp()
        self.entrar(ADMINISTRADOR)

    def test_el_nucleo_no_aparece(self):
        self.assertNotContains(self.client.get(f"/proyectos/{self.uno.pk}/reglas/"), "00·N1")

    def test_el_nucleo_tumba_todo_el_envio(self):
        respuesta = self.enviar(self.uno, **{"00·N1": "apagada", REGLA: AVISA})
        self.assertContains(respuesta, "no se pueden cambiar: 00·N1")
        self.assertEqual(NivelDeRegla.objects.count(), 0)

    def test_una_regla_inventada(self):
        self.assertContains(self.enviar(self.uno, **{"99·Z1": AVISA}), "99·Z1")
        self.assertEqual(NivelDeRegla.objects.count(), 0)

    def test_un_nivel_que_no_existe(self):
        self.assertContains(self.enviar(self.uno, **{REGLA: "a-medias"}), "Nivel que no existe")
        self.assertEqual(NivelDeRegla.objects.count(), 0)


class CadaCambioQuedaRegistrado(ConProyectos):

    def test_el_historial_dice_que_quien_y_cuando(self):
        self.entrar(ADMINISTRADOR)
        self.enviar(self.uno, **{REGLA: AVISA})
        cambio = CambioDeNivel.objects.get()
        self.assertEqual((cambio.regla, cambio.anterior, cambio.nuevo, cambio.cuenta),
                         (REGLA, "frena", AVISA, self.cuenta))
        self.assertIsNotNone(cambio.fecha)
        historial = self.client.get(f"/proyectos/{self.uno.pk}/reglas/historial/")
        for texto in (REGLA, "Frena", "Avisa", self.cuenta.username):
            self.assertContains(historial, texto)


class ConsultaSoloVeLosNiveles(ConProyectos):

    def setUp(self):
        super().setUp()
        self.entrar(CONSULTA)

    def test_ve_los_niveles_sin_guardar(self):
        pagina = self.client.get(f"/proyectos/{self.uno.pk}/reglas/")
        self.assertContains(pagina, REGLA)
        self.assertNotContains(pagina, "<select")
        self.assertNotContains(pagina, "Guardar")

    def test_su_envio_recibe_403(self):
        respuesta = self.client.post(f"/proyectos/{self.uno.pk}/reglas/", {f"nivel-{REGLA}": AVISA})
        self.assertEqual(respuesta.status_code, 403)
        self.assertEqual(NivelDeRegla.objects.count(), 0)
