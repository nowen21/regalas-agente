# -*- coding: utf-8 -*-
"""`EP-026·HU-009` · Los capítulos opt-in en la base: CP-001 a CP-003 de la fase A.

La lectura sin Django va con `TransactionTestCase`: abre su propia conexión con
PyMySQL, y desde ella no se ve lo que una prueba deja sin confirmar.
"""
import os
import tempfile

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import connection
from django.test import TestCase, TransactionTestCase

from core.cuentas.permisos import ADMINISTRADOR
from core.enganches.configuracion import ConfiguracionDelProyecto
from core.herramientas.recuperar import RecuperadorDeReglas
from core.historia.models import PROYECTO, Cambio, Version
from core.proyectos import copia
from core.proyectos.models import AjusteDelProyecto, Proyecto
from core.proyectos.opt_in import pasar_a_la_base


def _ajustes():
    d = connection.settings_dict
    return {"NAME": d["NAME"], "USER": d["USER"], "PASSWORD": d["PASSWORD"], "HOST": d["HOST"], "PORT": d["PORT"]}


def _carpeta(test, claude_md=""):
    carpeta = tempfile.TemporaryDirectory()
    test.addCleanup(carpeta.cleanup)
    if claude_md:
        with open(os.path.join(carpeta.name, "CLAUDE.md"), "w", encoding="utf-8") as f:
            f.write(claude_md)
    return carpeta.name


CLAUDE_MD = ("- **Patrón opt-in `15` (registros inmutables):** no\n"
             "- **Patrón opt-in `18` (despliegue e infraestructura):** sí\n")


class LosOptInSonAjustes(TestCase):
    """CP-001."""

    def test_prender_uno_guarda_historia_version_y_copia(self):
        proyecto = Proyecto.objects.create(nombre="uno", ruta=_carpeta(self))
        cuenta = get_user_model().objects.create_user("admin")
        cuenta.groups.add(Group.objects.get(name=ADMINISTRADOR))
        self.client.force_login(cuenta)
        antes = Version.objects.filter(ambito=PROYECTO, proyecto=proyecto).count()
        self.client.post("/proyectos/%d/editar/" % proyecto.pk,
                         {"nombre": "uno", "ruta": proyecto.ruta, "activo": "on", "opt_in_15": "sí"})
        self.assertEqual("sí", AjusteDelProyecto.objects.get(proyecto=proyecto, clave="opt_in_15").valor)
        self.assertTrue(Cambio.objects.filter(tabla="proyectos.ajustedelproyecto").exists())
        self.assertGreater(Version.objects.filter(ambito=PROYECTO, proyecto=proyecto).count(), antes)
        with open(os.path.join(proyecto.ruta, copia.ARCHIVO), encoding="utf-8") as f:
            self.assertIn("| Patrón opt-in 15 (registros inmutables) | sí | proyecto |", f.read())


class LasReglasSeEligenConLaBase(TransactionTestCase):
    """CP-002."""

    serialized_rollback = True

    def test_manda_la_base_y_sin_registro_el_claude_md(self):
        carpeta = _carpeta(self, CLAUDE_MD)
        sin_registro = ConfiguracionDelProyecto(carpeta, ajustes=_ajustes())
        self.assertIn("15", RecuperadorDeReglas.opt_in_apagados(carpeta, configuracion=sin_registro))
        self.assertNotIn("18", RecuperadorDeReglas.opt_in_apagados(
            carpeta, configuracion=ConfiguracionDelProyecto(carpeta, ajustes=_ajustes())))

        proyecto = Proyecto.objects.create(nombre="uno", ruta=carpeta)
        AjusteDelProyecto.objects.create(proyecto=proyecto, clave="opt_in_15", valor="sí")
        apagados = RecuperadorDeReglas.opt_in_apagados(
            carpeta, configuracion=ConfiguracionDelProyecto(carpeta, ajustes=_ajustes()))
        self.assertNotIn("15", apagados)
        self.assertIn("18", apagados)           # la base no lo prendió: vale el de fábrica


class ElClaudeMdPasaALaBase(TestCase):
    """CP-003."""

    def test_pasa_una_vez_sin_pisar(self):
        proyecto = Proyecto.objects.create(nombre="uno", ruta=_carpeta(self, CLAUDE_MD))
        self.assertEqual(6, pasar_a_la_base(Proyecto, AjusteDelProyecto))    # el 17 ya no es opt-in (EP-028·HU-001)
        guardados = dict(proyecto.ajustes_propios.values_list("clave", "valor"))
        self.assertEqual("no", guardados["opt_in_15"])
        self.assertEqual("sí", guardados["opt_in_18"])
        self.assertEqual("sí", guardados["opt_in_21"])    # no lo nombra: regía, y sigue rigiendo
        self.assertEqual(0, pasar_a_la_base(Proyecto, AjusteDelProyecto))
