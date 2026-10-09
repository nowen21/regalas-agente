# -*- coding: utf-8 -*-
"""`EP-028·HU-003` · El menú y el inicio llevan a cada función: CP-001 y CP-002."""
import tempfile

from django.contrib.auth.models import Group, User
from django.test import TestCase
from django.urls import reverse

from core.cuentas.permisos import ADMINISTRADOR
from core.estandar.models import ABIERTO, DOCUMENTO, PENDIENTE, Propuesta, Reporte
from core.proyectos.models import Proyecto

# Toda pantalla que no es el detalle de un registro (`17·I7`).
EN_EL_MENU = ["inicio:inicio", "proyectos:lista", "proyectos:registrar", "proyectos:configuracion",
              "estandar:lista", "estandar:propuestas", "estandar:reportes", "estandar:vista_previa",
              "estandar:git", "consumo:tablero", "pruebas:lista", "historia:lista", "historia:versiones", "ayuda:manual"]


class ConCuenta(TestCase):

    def setUp(self):
        cuenta = User.objects.create_user("admin", password="una-clave-larga-1")
        cuenta.groups.add(Group.objects.get_or_create(name=ADMINISTRADOR)[0])
        self.client.force_login(cuenta)


class ElMenu(ConCuenta):
    """CP-001."""

    def test_cp001_toda_pantalla_esta_y_se_marca_la_activa(self):
        pagina = self.client.get(reverse("inicio:inicio")).content.decode()
        for vista in EN_EL_MENU:
            self.assertIn('href="%s"' % reverse(vista), pagina, vista)
        propuestas = self.client.get(reverse("estandar:propuestas")).content.decode()
        self.assertIn('nav-link active" href="%s"' % reverse("estandar:propuestas"), propuestas)


class ElInicio(ConCuenta):
    """CP-002."""

    def test_cp002_dice_lo_que_espera_y_lleva_a_cada_pantalla(self):
        carpeta = tempfile.TemporaryDirectory()
        self.addCleanup(carpeta.cleanup)
        proyecto = Proyecto.objects.create(nombre="uno", ruta=carpeta.name)
        for n in range(2):
            Propuesta.objects.create(objeto=DOCUMENTO, accion="cambiar", ruta="base/x%d.md" % n, quien="agente",
                                     estado=PENDIENTE)
        Reporte.objects.create(proyecto=proyecto, titulo="algo mal", quien="agente", estado=ABIERTO)
        pagina = self.client.get(reverse("inicio:inicio")).content.decode()
        self.assertIn("Propuestas por aprobar", pagina)
        self.assertIn("Reporte abierto", pagina)
        self.assertIn('href="%s"' % reverse("estandar:reportes"), pagina)
        self.assertIn('fs-3">2</span>', pagina)
        self.assertIn('text-bg-danger me-3">3</span>', pagina)          # el menú suma los dos

    def test_cp002_sin_pendientes_lo_dice(self):
        self.assertContains(self.client.get(reverse("inicio:inicio")), "No hay nada esperando una decisión")


class LosIconos(ConCuenta):
    """CP-003 · `EP-028·HU-003`, fase B; desde `EP-028·HU-007`, con Bootstrap Icons de AdminLTE."""

    def test_cp003_cada_entrada_y_cada_item_lleva_su_icono(self):
        import re

        html = self.client.get("/").content.decode()
        menu = html[html.index('class="nav sidebar-menu'):html.index("</nav>", html.index('class="nav sidebar-menu'))]
        enlaces = re.findall(r'<a class="nav-link[^"]*"[^>]*>\s*<i class="nav-icon bi bi-[\w-]+" aria-hidden="true">', menu)
        todos = re.findall(r'<a class="nav-link', menu)
        self.assertEqual(len(todos), len(enlaces))
        self.assertGreaterEqual(len(enlaces), 15)
