# -*- coding: utf-8 -*-
"""`EP-025·HU-018`: la ayuda en cada campo y en cada pantalla, y el manual con su cobertura."""
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.template import Context, Template
from django.test import TestCase, override_settings
from django.urls import URLPattern, URLResolver, get_resolver

from core.ayuda import claves
from core.ayuda.secciones import NO_SON_PANTALLAS, SECCIONES, tiene_seccion
from core.ayuda.textos import CAMPOS, PANTALLAS
from core.cuentas.permisos import CONSULTA
from core.proyectos import ajustes


def _nombres(patrones, espacio=""):
    """Los nombres de todas las rutas, con su espacio: `proyectos:lista`."""
    for patron in patrones:
        if isinstance(patron, URLResolver):
            adentro = ":".join(p for p in (espacio, patron.namespace or "") if p)
            yield from _nombres(patron.url_patterns, adentro)
        elif isinstance(patron, URLPattern) and patron.name:
            yield "%s:%s" % (espacio, patron.name) if espacio else patron.name


class ConCuenta(TestCase):

    def setUp(self):
        cuenta = get_user_model().objects.create_user("consulta")
        cuenta.groups.add(Group.objects.get(name=CONSULTA))
        self.client.force_login(cuenta)


class LaAyudaEnCamposYPantallas(ConCuenta):
    """CP-001."""

    def test_configuracion_trae_el_globo_y_los_botones(self):
        respuesta = self.client.get("/proyectos/configuracion/")
        self.assertContains(respuesta, 'class="ayuda-icono"')
        self.assertContains(respuesta, "¿Cómo salen las rutas en los avisos?")
        self.assertContains(respuesta, "¿Para qué sirve?")
        self.assertContains(respuesta, "Cómo encaja en el sistema")

    def test_toda_pantalla_trae_el_boton_y_el_panel(self):
        respuesta = self.client.get("/proyectos/")
        self.assertContains(respuesta, 'data-ayuda-url="/ayuda/pantalla/?vista=proyectos%3Alista"')
        self.assertContains(respuesta, 'id="ayuda-contenido"')
        self.assertContains(respuesta, "ayuda/ayuda.js")

    def test_el_panel_trae_la_seccion_de_la_pantalla(self):
        respuesta = self.client.get("/ayuda/pantalla/?vista=proyectos:suspensiones")
        self.assertContains(respuesta, "<h3 class=\"h3 mb-3\">Suspensiones</h3>", html=False)
        self.assertContains(self.client.get("/ayuda/pantalla/?vista=no:existe"), "Primeros pasos")

    @override_settings(DEBUG=True)
    def test_una_clave_sin_texto_sale_en_rojo_en_desarrollo(self):
        html = Template('{% load ayuda %}{% ayuda_campo "no.existe" %}').render(Context())
        self.assertIn("ayuda-icono-falta", html)

    def test_en_produccion_una_clave_sin_texto_no_pinta_nada(self):
        self.assertEqual("", Template('{% load ayuda %}{% ayuda_campo "no.existe" %}').render(Context()).strip())


class ElManualYSuCobertura(ConCuenta):
    """CP-002."""

    def test_el_manual_trae_todas_las_secciones(self):
        respuesta = self.client.get("/ayuda/")
        for _slug, titulo, _vistas in SECCIONES:
            self.assertContains(respuesta, titulo)
        self.assertContains(respuesta, "window.print()")

    def test_una_seccion_que_no_existe_es_404(self):
        self.assertEqual(404, self.client.get("/ayuda/no-existe/").status_code)

    def test_ninguna_pantalla_queda_sin_seccion(self):
        nombres = {n for n in _nombres(get_resolver().url_patterns) if not n.startswith("admin:")}
        sin_seccion = sorted(n for n in nombres - NO_SON_PANTALLAS if not tiene_seccion(n))
        self.assertEqual([], sin_seccion)

    def test_toda_clave_usada_tiene_texto(self):
        campos, pantallas = claves.usadas()
        self.assertTrue(campos)
        self.assertEqual(set(), campos - set(CAMPOS))
        self.assertEqual(set(), pantallas - set(PANTALLAS))
        # «Configuración» arma sus claves con el nombre de cada ajuste.
        self.assertEqual(set(), {"configuracion." + c for c in ajustes.AJUSTES} - set(CAMPOS))
