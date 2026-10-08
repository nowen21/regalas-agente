# -*- coding: utf-8 -*-
"""`EP-027·HU-005` · CP-001 de la fase A: propuestas y memoria con nombres legibles."""
from django.contrib.auth.models import Group, User
from django.test import TestCase

from core.cuentas.permisos import ADMINISTRADOR
from core.proyectos.models import Proyecto

from .models import CAMBIAR, DOCUMENTO, Documento, Propuesta, Recuerdo, Regla

F8 = "base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md"
TEXTO_F8 = "> Regla del capítulo.\n\n## F8 · Edita solo los archivos que el plan aprobado declara\n\nNada más.\n"
RECUERDO = "---\nname: aprendizaje-compactar-al-promover\ndescription: Al promover una regla, se compacta.\n---\n\nTexto.\n"


class NombresLegibles(TestCase):

    def setUp(self):
        self.admin = User.objects.create_user("admin", password="una-clave-larga-1")
        self.admin.groups.add(Group.objects.get_or_create(name=ADMINISTRADOR)[0])
        self.client.force_login(self.admin)
        self.documento = Documento.objects.create(ruta=F8, contenido=TEXTO_F8)
        self.proyecto = Proyecto.objects.create(nombre="Prueba", ruta="C:/prueba")
        self.recuerdo = Recuerdo.objects.create(proyecto=self.proyecto, nombre="aprendizaje_compactar_al_promover.md",
                                                contenido=RECUERDO)

    def test_la_propuesta_dice_el_nombre_de_la_regla(self):
        Propuesta.objects.create(objeto=DOCUMENTO, accion=CAMBIAR, ruta=F8, contenido=TEXTO_F8, quien="agente")
        html = self.client.get("/estandar/propuestas/").content.decode()
        self.assertIn("F8 · Edita solo los archivos que el plan aprobado declara", html)
        self.assertNotIn(F8, html)

    def test_la_memoria_dice_el_nombre_y_la_descripcion(self):
        html = self.client.get("/estandar/memoria/%d/" % self.proyecto.pk).content.decode()
        self.assertIn("Aprendizaje compactar al promover", html)
        self.assertIn("Al promover una regla, se compacta.", html)
        self.assertNotIn("aprendizaje_compactar_al_promover.md", html)

    def test_cada_cosa_sabe_su_nombre_legible(self):
        self.assertEqual("F8 · Edita solo los archivos que el plan aprobado declara", self.documento.nombre_legible())
        self.assertEqual("Aprendizaje compactar al promover", self.recuerdo.nombre_legible())
        regla = Regla(codigo="F8", titulo="Edita solo los archivos que el plan aprobado declara")
        self.assertEqual("F8 · Edita solo los archivos que el plan aprobado declara", regla.nombre_legible())
        con_titulo = Recuerdo(nombre="x.md", contenido="---\nname: x\n---\n\n# Aprobar antes de commit\n")
        self.assertEqual("Aprobar antes de commit", con_titulo.nombre_legible())
