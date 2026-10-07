# -*- coding: utf-8 -*-
"""`EP-026·HU-002` · Pruebas de las versiones: CP-001 a CP-004 de la fase A."""
import shutil
import tempfile

from django.contrib.auth.models import Group, User
from django.test import TestCase

from core.cuentas.permisos import ADMINISTRADOR
from core.niveles.catalogo import reglas_configurables
from core.proyectos.models import AjusteBase, Proyecto

from . import versiones
from .models import ESTANDAR, MAYOR, MENOR, PARCHE, PROYECTO, Cambio, Version
from .registro import quien_y_por_que


class ConProyecto(TestCase):

    def setUp(self):
        raiz = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, raiz, True)
        self.proyecto = Proyecto.objects.create(nombre="uno", ruta=raiz)
        self.admin = User.objects.create_user("admin", password="una-clave-larga-1")
        self.admin.groups.add(Group.objects.get_or_create(name=ADMINISTRADOR)[0])
        self.client.force_login(self.admin)
        reglas = reglas_configurables()
        self.r1, self.r2 = reglas[0].id, reglas[1].id

    def guardar_niveles(self, obliga, agrega, **niveles):
        datos = {"version_obliga": obliga, "version_agrega": agrega, "version_motivo": "prueba"}
        datos.update({"nivel-" + regla: nivel for regla, nivel in niveles.items()})
        return self.client.post("/proyectos/%d/reglas/" % self.proyecto.pk, datos)

    def version_del_proyecto(self):
        return Version.objects.filter(ambito=PROYECTO, proyecto=self.proyecto).latest("id")


class UnCambioDeProyectoSubeSuVersion(ConProyecto):
    """CP-001."""

    def test_un_nivel_sube_un_parche_del_proyecto_y_no_el_estandar(self):
        antes_estandar = versiones.actual(ESTANDAR)
        antes = versiones.ultima(PROYECTO, self.proyecto.pk)
        creadas = Version.objects.count()
        self.guardar_niveles("no", "no", **{self.r1: "avisa"})
        version = self.version_del_proyecto()
        self.assertEqual("%d.%d.%d" % versiones.siguiente(antes, PARCHE), version.numero)
        self.assertEqual(PARCHE, version.tipo)
        self.assertEqual("prueba", version.resumen)
        cambio = Cambio.objects.filter(tabla="niveles.nivelderegla").latest("id")
        self.assertEqual(version, cambio.version)
        self.assertEqual(antes_estandar, versiones.actual(ESTANDAR))
        self.assertEqual(creadas + 1, Version.objects.count())

    def test_lo_de_un_mismo_envio_es_una_sola_version(self):
        creadas = Version.objects.count()
        self.guardar_niveles("no", "no", **{self.r1: "avisa", self.r2: "apagada"})
        self.assertEqual(creadas + 1, Version.objects.count())
        self.assertEqual(2, self.version_del_proyecto().cambios.filter(tabla="niveles.nivelderegla").count())


class LasDosPreguntasFijanElTipo(ConProyecto):
    """CP-002."""

    def test_mayor_menor_y_parche(self):
        mayor = versiones.ultima(PROYECTO, self.proyecto.pk)[0]
        self.guardar_niveles("si", "no", **{self.r1: "avisa"})
        self.assertEqual((MAYOR, "%d.0.0" % (mayor + 1)), (self.version_del_proyecto().tipo, self.version_del_proyecto().numero))
        self.guardar_niveles("no", "si", **{self.r1: "apagada"})
        self.assertEqual((MENOR, "%d.1.0" % (mayor + 1)), (self.version_del_proyecto().tipo, self.version_del_proyecto().numero))
        self.guardar_niveles("no", "no", **{self.r1: "frena"})
        self.assertEqual((PARCHE, "%d.1.1" % (mayor + 1)), (self.version_del_proyecto().tipo, self.version_del_proyecto().numero))

    def test_los_formularios_traen_las_preguntas(self):
        for url in ("/proyectos/%d/reglas/" % self.proyecto.pk, "/proyectos/configuracion/",
                    "/proyectos/%d/editar/" % self.proyecto.pk, "/proyectos/%d/suspensiones/" % self.proyecto.pk):
            self.assertContains(self.client.get(url), 'name="version_obliga"', msg_prefix=url)


class UnAjusteComunSubeElEstandar(TestCase):
    """CP-003."""

    def test_el_ajuste_de_capa_1_sube_un_parche_del_estandar(self):
        mayor, menor, parche = versiones.ultima(ESTANDAR)
        with quien_y_por_que(quien="prueba", tipo=PARCHE):
            AjusteBase.objects.create(clave="limite_enganche", valor="2500")
        version = Version.objects.filter(ambito=ESTANDAR).latest("id")
        self.assertEqual("%d.%d.%d" % (mayor, menor, parche + 1), version.numero)


class LasVersionesSeVen(ConProyecto):
    """CP-004."""

    def test_la_pantalla_lista_las_versiones(self):
        self.guardar_niveles("no", "si", **{self.r1: "avisa"})
        respuesta = self.client.get("/historia/versiones/")
        self.assertContains(respuesta, self.version_del_proyecto().numero)
        self.assertContains(respuesta, "niveles.nivelderegla")
