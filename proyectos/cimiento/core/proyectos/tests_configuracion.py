# -*- coding: utf-8 -*-
"""`EP-025·HU-013`: la configuración en tres capas, las suspensiones y la copia.

La lectura sin Django va con `TransactionTestCase`: abre su propia conexión con
PyMySQL, y desde ella no se ve lo que una prueba deja sin confirmar.
"""
import importlib
import os
import tempfile
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import connection
from django.test import SimpleTestCase, TestCase, TransactionTestCase
from django.utils import timezone

from core.cuentas.permisos import ADMINISTRADOR, CONSULTA
from core.enganches.configuracion import ConfiguracionDelProyecto
from core.enganches.freno import Freno
from core.enganches.niveles import TODAS, NivelesDelProyecto
from core.niveles.models import NivelDeRegla
from core.proyectos import ajustes as catalogo
from core.proyectos import copia
from core.proyectos.models import AjusteBase, AjusteDelProyecto, Proyecto, Suspension


def _ajustes(**cambios):
    d = connection.settings_dict
    return dict({"NAME": d["NAME"], "USER": d["USER"], "PASSWORD": d["PASSWORD"],
                 "HOST": d["HOST"], "PORT": d["PORT"]}, **cambios)


class ConProyecto:

    def armar(self):
        carpeta = tempfile.TemporaryDirectory()
        self.addCleanup(carpeta.cleanup)
        self.proyecto = Proyecto.objects.create(nombre="uno", ruta=carpeta.name)

    def suspender(self, nombre="02·F8", tipo=catalogo.REGLA, dias=1, **otros):
        return Suspension.objects.create(proyecto=self.proyecto, tipo=tipo, nombre=nombre, motivo="probar",
                                         vence=timezone.now() + timedelta(days=dias), **otros)


class ElCatalogo(SimpleTestCase):

    def test_el_nucleo_y_el_historico_no_se_suspenden(self):
        self.assertFalse(catalogo.se_puede_suspender(catalogo.REGLA, "00·N6"))
        self.assertFalse(catalogo.se_puede_suspender(catalogo.REGLA, "00·N1"))
        self.assertFalse(catalogo.se_puede_suspender(catalogo.ENGANCHE, "hook_historico.py"))
        self.assertTrue(catalogo.se_puede_suspender(catalogo.REGLA, "02·F8"))
        self.assertTrue(catalogo.se_puede_suspender(catalogo.ENGANCHE, catalogo.FRENO))

    def test_cada_capa_tapa_la_de_abajo(self):
        efectivos = catalogo.efectivos({"limite_enganche": "300", "rutas_en_avisos": "completas"},
                                       {"limite_enganche": "100"})
        self.assertEqual((100, "proyecto"), efectivos["limite_enganche"])
        self.assertEqual(("completas", "base"), efectivos["rutas_en_avisos"])
        self.assertEqual((10000, "fábrica"), efectivos["limite_archivo"])

    def test_un_valor_roto_cuenta_como_vacio(self):
        self.assertEqual((2000, "fábrica"), catalogo.efectivos({"limite_enganche": "x"})["limite_enganche"])


class LasCapasSinDjango(ConProyecto, TransactionTestCase):
    """CP-001, pasos 1 a 4."""

    serialized_rollback = True

    def setUp(self):
        self.armar()

    def leer(self, **cambios):
        return ConfiguracionDelProyecto(self.proyecto.ruta, ajustes=_ajustes(**cambios)).efectivos()

    def test_fabrica_base_y_proyecto(self):
        self.assertEqual((2000, "fábrica"), self.leer()["limite_enganche"])
        AjusteBase.objects.create(clave="limite_enganche", valor="300")
        self.assertEqual((300, "base"), self.leer()["limite_enganche"])
        AjusteDelProyecto.objects.create(proyecto=self.proyecto, clave="limite_enganche", valor="100")
        AjusteBase.objects.filter(clave="limite_enganche").update(valor="400")
        self.assertEqual((100, "proyecto"), self.leer()["limite_enganche"])

    def test_sin_base_el_de_fabrica(self):
        AjusteBase.objects.create(clave="limite_enganche", valor="300")
        self.assertEqual((2000, "fábrica"), self.leer(PORT="1")["limite_enganche"])


class ElFrenoAplicaLasSuspensiones(ConProyecto, TransactionTestCase):
    """CP-002, pasos 1 a 3."""

    serialized_rollback = True

    def setUp(self):
        self.armar()
        NivelDeRegla.objects.create(proyecto=self.proyecto, regla="02·F9", nivel="avisa")

    def niveles(self):
        return NivelesDelProyecto(self.proyecto.ruta, ajustes=_ajustes()).todos()

    def test_la_regla_suspendida_queda_apagada(self):
        self.suspender("02·F8")
        self.assertEqual({"02·F8": "apagada", "02·F9": "avisa"}, self.niveles())

    def test_el_freno_entero_apaga_todo_menos_el_nucleo(self):
        self.suspender(catalogo.FRENO, catalogo.ENGANCHE)
        niveles = self.niveles()
        self.assertEqual("apagada", niveles[TODAS])
        self.assertEqual("apagada", Freno.nivel_para("02·F8", niveles))
        self.assertEqual("avisa", Freno.nivel_para("02·F9", niveles))
        self.assertEqual("frena", Freno.nivel_para("00·N6", niveles))

    def test_vencida_o_levantada_ya_no_cuenta(self):
        self.suspender("02·F8", dias=-1)
        self.suspender("02·F8", levantada=timezone.now())
        self.assertEqual({"02·F9": "avisa"}, self.niveles())


class ConCuentas(ConProyecto, TestCase):

    def setUp(self):
        self.armar()

    def entrar(self, grupo=ADMINISTRADOR):
        cuenta = get_user_model().objects.create_user("cuenta-%s" % grupo)
        cuenta.groups.add(Group.objects.get(name=grupo))
        self.client.force_login(cuenta)
        return cuenta

    def copia(self):
        with open(os.path.join(self.proyecto.ruta, copia.ARCHIVO), encoding="utf-8") as f:
            return f.read()


class LasPantallas(ConCuentas):
    """CP-001, pasos 5 y 6, y CP-003, paso 1."""

    def test_configuracion_la_guarda_el_administrador(self):
        self.entrar()
        self.assertContains(self.client.get("/proyectos/configuracion/"), "Rutas en los avisos")
        respuesta = self.client.post("/proyectos/configuracion/", {"rutas_en_avisos": "completas",
                                                                   "limite_enganche": "300", "limite_archivo": ""})
        self.assertRedirects(respuesta, "/proyectos/configuracion/", fetch_redirect_response=False)
        self.assertEqual({"rutas_en_avisos": "completas", "limite_enganche": "300"},
                         dict(AjusteBase.objects.values_list("clave", "valor")))
        self.assertIn("| Límite por enganche | 300 | base |", self.copia())

    def test_la_consulta_solo_mira(self):
        self.entrar(CONSULTA)
        self.assertEqual(200, self.client.get("/proyectos/configuracion/").status_code)
        self.assertEqual(403, self.client.post("/proyectos/configuracion/", {"limite_enganche": "5"}).status_code)
        self.assertFalse(AjusteBase.objects.exists())

    def test_el_proyecto_guarda_y_vacia_lo_suyo(self):
        self.entrar()
        datos = {"nombre": "uno", "ruta": self.proyecto.ruta, "activo": "on", "limite_archivo": "700",
                 "rutas_en_avisos": "completas"}
        self.client.post("/proyectos/%d/editar/" % self.proyecto.pk, datos)
        self.assertEqual({"limite_archivo": "700", "rutas_en_avisos": "completas"},
                         dict(self.proyecto.ajustes_propios.values_list("clave", "valor")))
        self.assertIn("| Límite por archivo | 700 | proyecto |", self.copia())
        self.client.post("/proyectos/%d/editar/" % self.proyecto.pk, dict(datos, limite_archivo=""))
        self.assertEqual(10000, self.proyecto.ajuste("limite_archivo"))

    def test_un_valor_que_no_vale_no_se_guarda(self):
        self.entrar()
        respuesta = self.client.post("/proyectos/configuracion/", {"rutas_en_avisos": "otras"})
        self.assertEqual(200, respuesta.status_code)
        self.assertFalse(AjusteBase.objects.exists())


class SuspenderYLevantar(ConCuentas):
    """CP-002, pasos 3 y 4, y CP-003, paso 1."""

    def suspension(self, **datos):
        vence = timezone.localtime(timezone.now() + timedelta(days=2)).strftime("%Y-%m-%dT%H:%M")
        return self.client.post("/proyectos/%d/suspensiones/" % self.proyecto.pk,
                                dict({"tipo": "regla", "nombre": "02·F8", "motivo": "el plan se corrige", "vence": vence},
                                     **datos))

    def test_suspender_y_levantar(self):
        cuenta = self.entrar()
        self.assertEqual(302, self.suspension().status_code)
        suspension = Suspension.objects.get()
        self.assertEqual((cuenta, "02·F8"), (suspension.creada_por, suspension.nombre))
        self.assertIn("| 02·F8 | el plan se corrige |", self.copia())
        self.client.post("/proyectos/%d/suspensiones/%d/levantar/" % (self.proyecto.pk, suspension.pk))
        suspension.refresh_from_db()
        self.assertEqual(cuenta, suspension.levantada_por)
        self.assertFalse(suspension.vigente())
        self.assertIn("Ninguna.", self.copia())

    def test_el_freno_entero_se_guarda_como_freno(self):
        self.entrar()
        self.suspension(tipo="enganche", nombre="hook_historico.py")
        self.assertEqual("freno", Suspension.objects.get().nombre)

    def test_lo_que_no_se_suspende(self):
        self.entrar()
        ahora = timezone.localtime(timezone.now())
        for datos in ({"nombre": "00·N6"}, {"nombre": "00·N1"}, {"nombre": "99·Z1"}, {"motivo": ""},
                      {"vence": (ahora + timedelta(days=31)).strftime("%Y-%m-%dT%H:%M")},
                      {"vence": (ahora - timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M")}):
            with self.subTest(datos=datos):
                self.assertEqual(200, self.suspension(**datos).status_code)
        self.assertFalse(Suspension.objects.exists())

    def test_la_consulta_no_suspende_ni_levanta(self):
        suspension = self.suspender()
        self.entrar(CONSULTA)
        self.assertEqual(403, self.suspension().status_code)
        self.assertEqual(403, self.client.post("/proyectos/%d/suspensiones/%d/levantar/"
                                               % (self.proyecto.pk, suspension.pk)).status_code)
        self.assertEqual(1, Suspension.objects.count())


class LaMigracionPasaLosLimites(ConProyecto, TestCase):
    """CP-003, paso 3: lo que tenía cada proyecto en sus columnas pasa a sus ajustes, y vuelve."""

    def setUp(self):
        self.armar()

    def test_ida_y_vuelta(self):
        migracion = importlib.import_module("core.proyectos.migrations.0004_tres_capas")

        class Viejo:
            def __init__(self, proyecto, **limites):
                self.pk, self.id = proyecto.pk, proyecto.pk
                self.__dict__.update(limites)

        viejos = [Viejo(self.proyecto, limite_enganche=500, limite_archivo=10000)]
        devueltos = {}

        class Filas(list):
            def update(self, **valores):
                devueltos.update(valores)

        class Manejador:
            def all(self):
                return viejos

            def filter(self, pk):
                return Filas()

        class ProyectoViejo:
            objects = Manejador()

        class Apps:
            def get_model(self, app, nombre):
                return ProyectoViejo if nombre == "Proyecto" else AjusteDelProyecto

        migracion.pasar_a_ajustes(Apps(), None)
        self.assertEqual({"limite_enganche": "500"}, dict(self.proyecto.ajustes_propios.values_list("clave", "valor")))
        migracion.devolver_a_columnas(Apps(), None)
        self.assertEqual({"limite_enganche": 500}, devueltos)
