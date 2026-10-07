# -*- coding: utf-8 -*-
"""`EP-028·HU-006` · Las tablas de Cimiento usan los recursos de tablas de la plantilla: CP-001 y CP-002."""
import os
import tempfile

from django.contrib.auth.models import Group, User
from django.test import TestCase
from django.urls import reverse

from core.cuentas.permisos import ADMINISTRADOR
from core.proyectos.models import Proyecto

CORE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CIMIENTO = os.path.dirname(CORE)

# plantilla → si pagina en la página (las que pagina la base, no)
TABLAS = {
    "proyectos/templates/proyectos/lista.html": True,
    "proyectos/templates/proyectos/suspensiones.html": True,
    "niveles/templates/niveles/historial.html": True,
    "estandar/templates/estandar/propuestas.html": True,
    "estandar/templates/estandar/reportes.html": True,
    "historia/templates/historia/lista.html": False,
    "historia/templates/historia/versiones.html": False,
}


def _leer(*partes):
    with open(os.path.join(*partes), encoding="utf-8") as f:
        return f.read()


class LasListas(TestCase):
    """CP-001."""

    def test_cp001_la_lista_de_proyectos_ordena_filtra_y_pagina(self):
        cuenta = User.objects.create_user("admin", password="una-clave-larga-1")
        cuenta.groups.add(Group.objects.get_or_create(name=ADMINISTRADOR)[0])
        self.client.force_login(cuenta)
        carpeta = tempfile.TemporaryDirectory()
        self.addCleanup(carpeta.cleanup)
        Proyecto.objects.create(nombre="uno", ruta=carpeta.name)
        pagina = self.client.get(reverse("proyectos:lista")).content.decode()
        self.assertIn('data-tabla-avanzada data-por-pagina="10"', pagina)
        self.assertIn('class="table-sort" data-sort="t-nombre"', pagina)
        self.assertIn('data-filtro="t-nombre"', pagina)
        self.assertIn('class="table-tbody"', pagina)
        self.assertIn("filas por página", pagina)
        self.assertIn("libs/list.js/dist/list.min.js", pagina)


class UnSoloCodigo(TestCase):
    """CP-002."""

    def test_cp002_todas_usan_el_mismo_patron_y_el_mismo_pie(self):
        for rel, pagina in TABLAS.items():
            texto = _leer(CORE, *rel.split("/"))
            self.assertIn("data-tabla-avanzada", texto, rel)
            self.assertIn("table-sort", texto, rel)
            self.assertIn("data-filtro", texto, rel)
            self.assertEqual(pagina, 'includes/tabla_pie.html' in texto, rel)
        self.assertIn("new List(", _leer(CIMIENTO, "static", "tablas.js"))
        base = _leer(CIMIENTO, "templates", "base.html")
        self.assertIn("libs/list.js/dist/list.min.js", base)
        self.assertIn("tablas.js", base)
