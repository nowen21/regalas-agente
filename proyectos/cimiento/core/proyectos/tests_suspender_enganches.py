"""`EP-025·HU-032`, fase A · Cada momento de un enganche y cada revisión de git tiene nombre y se suspende."""
from collections import Counter
from datetime import timedelta

from django.test import SimpleTestCase
from django.utils import timezone

from core.comun.enganches import FRENO, HOOKS_CLAUDE, MOMENTOS, NO_CONVIENE, REVISIONES_GIT, suspendibles
from core.proyectos.models import Suspension

from .tests_configuracion import ConCuentas


class ElCatalogoNombraTodo(SimpleTestCase):
    """CP-001."""

    def test_cada_momento_tiene_nombre_y_solo_el_freno_se_repite(self):
        nombres = [MOMENTOS[(evento, guion)] for evento, _f, guion, _m, _a in HOOKS_CLAUDE]
        self.assertEqual(len(HOOKS_CLAUDE), len(nombres))
        repetidos = {n for n, veces in Counter(nombres).items() if veces > 1}
        self.assertEqual({FRENO}, repetidos)
        self.assertEqual(FRENO, MOMENTOS[("PreToolUse", "hook_antes.py")])
        self.assertEqual(FRENO, MOMENTOS[("PostToolUse", "hook_despues.py")])

    def test_los_momentos_y_las_revisiones_no_comparten_nombre(self):
        todos = [n for n, _q, _m in suspendibles()]
        self.assertEqual(len(todos), len(set(todos)))
        self.assertTrue({n for n, _t in REVISIONES_GIT.values()} <= set(todos))
        self.assertTrue(set(NO_CONVIENE) <= set(todos))


class LaPantallaDejaSuspenderCualquiera(ConCuentas):
    """CP-002."""

    def suspender(self, nombre, tipo="enganche"):
        vence = timezone.localtime(timezone.now() + timedelta(days=2)).strftime("%Y-%m-%dT%H:%M")
        return self.client.post("/proyectos/%d/suspensiones/" % self.proyecto.pk,
                                {"tipo": tipo, "nombre": nombre, "motivo": "estorba en este proyecto", "vence": vence})

    def test_el_historico_y_una_revision_de_git_se_suspenden(self):
        self.entrar()
        self.assertEqual(302, self.suspender("historico-del-usuario").status_code)
        self.assertEqual(302, self.suspender("git-versionado").status_code)
        self.assertEqual({"historico-del-usuario", "git-versionado"},
                         set(Suspension.objects.values_list("nombre", flat=True)))

    def test_un_nombre_fuera_del_catalogo_se_rechaza(self):
        self.entrar()
        respuesta = self.suspender("hook_inventado.py")
        self.assertEqual(200, respuesta.status_code)
        self.assertContains(respuesta, "no es un enganche ni una revisión de git del catálogo")
        self.assertFalse(Suspension.objects.exists())

    def test_la_pantalla_muestra_la_recomendacion(self):
        self.entrar()
        respuesta = self.client.get("/proyectos/%d/suspensiones/" % self.proyecto.pk)
        self.assertContains(respuesta, 'id="tabla-enganches"')
        self.assertContains(respuesta, "<code>historico-del-usuario</code>")
        self.assertContains(respuesta, NO_CONVIENE["historico-del-usuario"])
        self.assertContains(respuesta, '<option value="git-marcas">')


class LaPantallaEnPestanas(ConCuentas):
    """`EP-025·HU-032`, fase D · CP-008 y CP-009."""

    def pagina(self):
        return self.client.get("/proyectos/%d/suspensiones/" % self.proyecto.pk)

    def test_tres_pestanas_con_suspensiones_abierta(self):
        self.entrar()
        respuesta = self.pagina()
        self.assertContains(respuesta, '<a href="#pestana-suspensiones" class="nav-link active"')
        self.assertContains(respuesta, '<a href="#pestana-reglas" class="nav-link"')
        self.assertContains(respuesta, '<a href="#pestana-enganches" class="nav-link"')

    def test_reglas_y_enganches_en_tablas_como_la_de_suspensiones(self):
        self.entrar()
        respuesta = self.pagina()
        self.assertContains(respuesta, '<div id="tabla-reglas" data-tabla-avanzada')
        self.assertContains(respuesta, '<td class="r-codigo"><code>02·F8</code></td>')
        self.assertContains(respuesta, '<div id="tabla-enganches" data-tabla-avanzada')
        self.assertContains(respuesta, '<td class="e-nombre"><code>historico-del-usuario</code></td>')

    def test_el_boton_abre_el_modal_y_con_errores_vuelve_abierto(self):
        self.entrar()
        respuesta = self.pagina()
        self.assertContains(respuesta, 'data-bs-toggle="modal" data-bs-target="#suspender"')
        self.assertContains(respuesta, '<div class="modal fade" id="suspender"')
        self.assertNotContains(respuesta, "bootstrap.Modal.getOrCreateInstance")
        vence = timezone.localtime(timezone.now() + timedelta(days=2)).strftime("%Y-%m-%dT%H:%M")
        con_error = self.client.post("/proyectos/%d/suspensiones/" % self.proyecto.pk,
                                     {"tipo": "enganche", "nombre": "no-existe", "motivo": "x", "vence": vence})
        self.assertContains(con_error, "bootstrap.Modal.getOrCreateInstance")
        self.assertContains(con_error, "no es un enganche ni una revisión de git del catálogo")

    def test_quien_solo_consulta_no_ve_el_boton_ni_el_modal(self):
        from core.cuentas.permisos import CONSULTA
        self.entrar(CONSULTA)
        respuesta = self.pagina()
        self.assertNotContains(respuesta, 'id="abrir-suspender"')
        self.assertNotContains(respuesta, 'id="suspender"')
        self.assertContains(respuesta, 'id="tabla-reglas"')
