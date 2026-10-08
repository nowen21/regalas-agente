# -*- coding: utf-8 -*-
"""`EP-028·HU-007` · Pruebas de la fase A: Cimiento usa AdminLTE 4 (CP-001 a CP-003)."""
import glob
import os
import re

from django.contrib.auth.models import Group, User
from django.test import TestCase
from django.urls import reverse

from core.cuentas.permisos import ADMINISTRADOR

# Las clases propias de Tabler que Cimiento usaba; ni Bootstrap ni AdminLTE las tienen.
DE_TABLER = {"table-vcenter", "card-table", "form-hint", "btn-list", "badge-sm", "card-sm", "card-md", "row-cards",
             "subheader", "empty", "empty-title", "empty-subtitle", "empty-action", "alert-title", "text-red-fg",
             "page", "page-wrapper", "page-header", "page-body", "page-title", "page-center", "container-tight",
             "navbar-vertical", "navbar-brand-autodark", "nav-link-icon", "nav-link-title", "dropdown-item-icon",
             "card-status-top", "modal-status", "bg-blue-lt", "bg-azure-lt", "bg-purple-lt", "bg-green-lt",
             "bg-red-lt", "bg-yellow-lt", "bg-secondary-lt", "bg-success-lt", "bg-danger-lt", "bg-warning-lt"}


class ConCuenta(TestCase):

    def setUp(self):
        cuenta = User.objects.create_user("admin", password="una-clave-larga-1")
        cuenta.groups.add(Group.objects.get_or_create(name=ADMINISTRADOR)[0])
        self.client.force_login(cuenta)


class LasPantallasUsanAdminLTE(ConCuenta):
    """CP-001."""

    def test_cargan_adminlte_y_no_tabler(self):
        for url in ("/", "/estandar/", "/historia/", "/proyectos/", "/gasto/"):
            html = self.client.get(url).content.decode()
            self.assertIn("css/adminlte.min.css", html, url)
            self.assertIn("js/bootstrap.bundle.min.js", html, url)
            self.assertNotIn("tabler", html.replace("tablero", ""), url)
            for parte in ("app-wrapper", "app-header", "app-sidebar", "app-main"):
                self.assertIn(parte, html, url)

    def test_la_entrada_es_la_de_adminlte(self):
        self.client.logout()
        html = self.client.get(reverse("cuentas:entrar")).content.decode()
        self.assertIn("login-box", html)
        self.assertIn("css/adminlte.min.css", html)


class NingunaClaseDeTabler(TestCase):
    """CP-003."""

    def test_ni_en_las_plantillas_ni_en_presentar(self):
        raiz = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        archivos = glob.glob(os.path.join(raiz, "templates", "**", "*.html"), recursive=True)
        archivos += glob.glob(os.path.join(raiz, "core", "**", "templates", "**", "*.html"), recursive=True)
        archivos.append(os.path.join(raiz, "core", "estandar", "presentar.py"))
        quedan = []
        for ruta in archivos:
            texto = open(ruta, encoding="utf-8").read()
            for valor in re.findall(r'class="([^"]*)"', texto):
                for clase in re.sub(r"\{[%{].*?[%}]\}", " ", valor).split():
                    if clase in DE_TABLER or re.fullmatch(r"bg-[a-z]+-lt", clase):
                        quedan.append("%s: %s" % (os.path.relpath(ruta, raiz), clase))
        self.assertEqual([], quedan)
