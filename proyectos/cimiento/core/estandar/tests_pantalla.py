# -*- coding: utf-8 -*-
"""`EP-026·HU-005` · Pruebas de la pantalla del estándar: CP-001 a CP-005 de la fase A."""
import io
import os
import shutil
import tempfile

from django.contrib.auth.models import Group, User
from django.core.management import call_command
from django.db import connection
from django.test import TestCase, TransactionTestCase

from core.comun import Proyecto as Carpeta
from core.cuentas.permisos import ADMINISTRADOR, CONSULTA
from core.enganches.recuerdos import Recuerdos
from core.historia.models import ESTANDAR, MENOR, PROYECTO, Cambio, Version
from core.proyectos.models import Proyecto

from .importar import importar
from .models import APROBADA, PENDIENTE, RECHAZADA, Documento, Propuesta, Recuerdo

RESPUESTAS = {"version_obliga": "no", "version_agrega": "si", "version_motivo": "prueba"}
APLICA_C29 = "**Aplica a:** escribir-documento, cambiar-codigo, correr-comando"


class ConEstandar(TestCase):

    @classmethod
    def setUpTestData(cls):
        importar(Carpeta.estandar())
        cls.admin = User.objects.create_user("admin", password="una-clave-larga-1")
        cls.admin.groups.add(Group.objects.get_or_create(name=ADMINISTRADOR)[0])
        cls.mira = User.objects.create_user("mira", password="una-clave-larga-1")
        cls.mira.groups.add(Group.objects.get_or_create(name=CONSULTA)[0])

    def setUp(self):
        self.client.force_login(self.admin)

    def doc(self, ruta):
        return Documento.objects.get(ruta=ruta)


class CambiarUnDocumento(ConEstandar):
    """CP-001."""

    def test_cambia_sube_menor_y_arma_el_mapa_en_la_misma_version(self):
        conducta = self.doc("base/01-conducta.md")
        self.assertIn(APLICA_C29, conducta.contenido)
        self.assertNotIn("C29", self.doc("base/reglas-por-tarea/tocar-git.md").contenido)
        nuevo = conducta.contenido.replace(APLICA_C29, APLICA_C29 + ", tocar-git")
        datos = dict(RESPUESTAS, contenido=nuevo)
        self.client.post("/estandar/documento/%d/" % conducta.pk, datos)
        self.assertIn("tocar-git", self.doc("base/01-conducta.md").contenido)
        version = Version.objects.filter(ambito=ESTANDAR).latest("id")
        self.assertEqual(MENOR, version.tipo)
        self.assertIn("C29", self.doc("base/reglas-por-tarea/tocar-git.md").contenido)
        tablas = set(version.cambios.values_list("fila", flat=True))
        mapa = self.doc("base/reglas-por-tarea/tocar-git.md")
        self.assertIn(str(mapa.pk), tablas)
        self.assertIn(str(conducta.pk), tablas)


class CrearYQuitar(ConEstandar):
    """CP-002."""

    def test_crear_rechazar_fuera_y_quitar(self):
        self.client.post("/estandar/nuevo/", dict(RESPUESTAS, ruta="base/anexo-prueba.md", contenido="# Prueba\n"))
        nuevo = self.doc("base/anexo-prueba.md")
        self.client.post("/estandar/nuevo/", dict(RESPUESTAS, ruta="plantillas/x.md", contenido="x"))
        self.assertFalse(Documento.objects.filter(ruta="plantillas/x.md").exists())
        self.client.post("/estandar/documento/%d/quitar/" % nuevo.pk, RESPUESTAS)
        self.assertFalse(Documento.objects.filter(ruta="base/anexo-prueba.md").exists())
        self.assertTrue(Cambio.objects.filter(tabla="estandar.documento", fila=str(nuevo.pk), accion="borrar").exists())


def _ajustes():
    d = connection.settings_dict
    return {"NAME": d["NAME"], "USER": d["USER"], "PASSWORD": d["PASSWORD"], "HOST": d["HOST"], "PORT": d["PORT"]}


class LaMemoria(TransactionTestCase):
    """CP-003. Con `TransactionTestCase`: el arranque lee la base por otra conexión."""

    serialized_rollback = True

    def test_cambiar_un_recuerdo_y_leer_el_indice_de_la_base(self):
        carpeta = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, carpeta, True)
        proyecto = Proyecto.objects.create(nombre="con memoria", ruta=carpeta)
        indice = Recuerdo.objects.create(proyecto=proyecto, nombre="memory.md", contenido="# Índice en la base\n")
        admin = User.objects.create_user("admin", password="una-clave-larga-1")
        admin.groups.add(Group.objects.get_or_create(name=ADMINISTRADOR)[0])
        self.client.force_login(admin)
        antes = Version.objects.filter(ambito=PROYECTO, proyecto=proyecto).count()
        self.client.post("/estandar/memoria/%d/%d/" % (proyecto.pk, indice.pk),
                         dict(RESPUESTAS, contenido="# Índice cambiado en la pantalla\n"))
        self.assertEqual(antes + 1, Version.objects.filter(ambito=PROYECTO, proyecto=proyecto).count())
        texto, orden = Recuerdos(carpeta).desde_la_base(ajustes=_ajustes())
        self.assertEqual("# Índice cambiado en la pantalla\n", texto)
        self.assertIn("ver_recuerdo", orden)


class LasPropuestas(ConEstandar):
    """CP-004."""

    def proponer(self, texto, motivo):
        archivo = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8")
        archivo.write(texto)
        archivo.close()
        self.addCleanup(os.remove, archivo.name)
        call_command("proponer", ruta="base/tareas.md", archivo=archivo.name, motivo=motivo, stdout=io.StringIO())
        return Propuesta.objects.latest("id")

    def test_aprobar_aplica_y_rechazar_no(self):
        original = self.doc("base/tareas.md").contenido
        propuesta = self.proponer(original + "\nUna línea propuesta.\n", "sumar una línea")
        self.assertEqual(PENDIENTE, propuesta.estado)
        self.assertEqual(original, self.doc("base/tareas.md").contenido)
        self.client.post("/estandar/propuestas/%d/aprobar/" % propuesta.pk, RESPUESTAS)
        propuesta.refresh_from_db()
        self.assertEqual(APROBADA, propuesta.estado)
        self.assertEqual(self.admin, propuesta.resuelta_por)
        self.assertIn("Una línea propuesta.", self.doc("base/tareas.md").contenido)

        otra = self.proponer("texto que no va\n", "no va")
        self.client.post("/estandar/propuestas/%d/rechazar/" % otra.pk)
        otra.refresh_from_db()
        self.assertEqual(RECHAZADA, otra.estado)
        self.assertNotIn("texto que no va", self.doc("base/tareas.md").contenido)


class ConsultaYLectura(ConEstandar):
    """CP-005."""

    def test_consulta_no_cambia_y_las_ordenes_leen_la_base(self):
        self.client.force_login(self.mira)
        tareas = self.doc("base/tareas.md")
        self.assertEqual(200, self.client.get("/estandar/").status_code)
        self.assertEqual(403, self.client.post("/estandar/documento/%d/" % tareas.pk,
                                               dict(RESPUESTAS, contenido="x")).status_code)
        self.assertEqual(403, self.client.post("/estandar/documento/%d/quitar/" % tareas.pk, RESPUESTAS).status_code)
        self.assertNotEqual("x", self.doc("base/tareas.md").contenido)
        salida = io.StringIO()
        call_command("ver_estandar", "base/tareas.md", stdout=salida)
        self.assertEqual(tareas.contenido, salida.getvalue())
