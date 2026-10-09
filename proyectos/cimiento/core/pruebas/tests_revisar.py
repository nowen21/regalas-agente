# -*- coding: utf-8 -*-
"""`EP-029·HU-002` · Revisar y su página: CP-001 a CP-009 de la fase A.

La herramienta de cada lenguaje se simula (`08·T3`): `Falsa` hace lo que hace
cada una según su documentación, sin correrla. Los valores esperados salen de
la HU, no del código (`08·T8`).
"""
import json
import os
import tempfile
from datetime import timedelta
from types import SimpleNamespace
from unittest import mock

from django.contrib.auth.models import Group, User
from django.core.management import call_command
from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.utils import timezone

from core.cuentas.permisos import ADMINISTRADOR
from core.proyectos.models import Proyecto
from core.pruebas.lenguaje import ANGULAR, DJANGO, LARAVEL, PYTHON, reconocer
from core.pruebas.models import AL_DIA, NUNCA, PruebasDelProyecto, Revision
from core.pruebas.revisar import FALTA_HERRAMIENTA, SIN_PYTHON, Revisor


def _carpeta(test, *archivos):
    tmp = tempfile.TemporaryDirectory()
    test.addCleanup(tmp.cleanup)
    for archivo in archivos:
        ruta = os.path.join(tmp.name, *archivo.split("/"))
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        open(ruta, "w").close()
    return tmp.name


def _django(test):
    return _carpeta(test, "manage.py", ".venv/Scripts/python.exe")


COVERAGE_JSON = {"totals": {"percent_covered": 75.0},
                 "files": {"app\\vistas.py": {"summary": {"percent_covered": 90.0}, "missing_lines": [7]},
                           "app/modelos.py": {"summary": {"percent_covered": 30.0}, "missing_lines": [3, 4, 5]}}}

CLOVER = """<?xml version="1.0"?>
<coverage><project>
  <file name="app/Pago.php"><line num="3" type="stmt" count="0"/><metrics statements="10" coveredstatements="5"/></file>
  <file name="app/Cuenta.php"><metrics statements="40" coveredstatements="35"/></file>
  <metrics statements="50" coveredstatements="40"/>
</project></coverage>"""


class Falsa:
    """Hace de la herramienta: escribe el reporte donde se lo piden y devuelve lo que se le diga."""

    def __init__(self, stdout="", stderr="", returncode=0, reporte=None):
        self.stdout, self.stderr, self.returncode, self.reporte = stdout, stderr, returncode, reporte
        self.ordenes = []

    def __call__(self, partes, **_):
        self.ordenes.append(partes)
        destino = None
        if "json" in partes and "-o" in partes:
            destino = partes[partes.index("-o") + 1]
        if "--coverage-clover" in partes:
            destino = partes[partes.index("--coverage-clover") + 1]
        if destino and self.reporte is not None:
            with open(destino, "w", encoding="utf-8") as f:
                f.write(self.reporte if isinstance(self.reporte, str) else json.dumps(self.reporte))
        return SimpleNamespace(stdout=self.stdout, stderr=self.stderr, returncode=self.returncode)


class ReconoceCadaLenguaje(SimpleTestCase):
    """CP-001."""

    def test_cada_uno(self):
        self.assertEqual(DJANGO, reconocer(_carpeta(self, "manage.py", "requirements.txt")).nombre)
        self.assertEqual(LARAVEL, reconocer(_carpeta(self, "artisan", "composer.json")).nombre)
        self.assertEqual(ANGULAR, reconocer(_carpeta(self, "angular.json", "package.json")).nombre)
        self.assertEqual(PYTHON, reconocer(_carpeta(self, "requirements.txt")).nombre)

    def test_dentro_de_proyectos(self):
        raiz = _carpeta(self, "proyectos/app/manage.py")
        lenguaje = reconocer(raiz)
        self.assertEqual(DJANGO, lenguaje.nombre)
        self.assertEqual(os.path.join(raiz, "proyectos", "app"), lenguaje.carpeta)

    def test_no_cuenta_lo_que_esta_en_las_dependencias(self):
        self.assertIsNone(reconocer(_carpeta(self, "node_modules/x/manage.py", ".venv/y/manage.py")))


class ElQueNoReconoceQuedaSinMedicion(SimpleTestCase):
    """CP-002."""

    def test_carpeta_vacia(self):
        campos = Revisor(correr=Falsa()).revisar(_carpeta(self))
        self.assertEqual(Revision.SIN_MEDICION, campos["resultado"])
        self.assertTrue(campos["mensaje"])


class DjangoGuardaPorcentajeYArchivos(SimpleTestCase):
    """CP-003."""

    def test_reporte(self):
        falsa = Falsa(reporte=COVERAGE_JSON)
        campos = Revisor(correr=falsa).revisar(_django(self))
        self.assertEqual(Revision.HECHA, campos["resultado"])
        self.assertEqual(75.0, campos["porcentaje"])
        self.assertEqual(["app/modelos.py", "app/vistas.py"], [a["archivo"] for a in campos["archivos"]])
        self.assertEqual([3, 4, 5], campos["archivos"][0]["sin_pruebas"])
        self.assertIn("manage.py", falsa.ordenes[0])


class LaravelYAngularLeenSuResultado(SimpleTestCase):
    """CP-004."""

    def test_laravel(self):
        raiz = _carpeta(self, "artisan", "composer.json", "vendor/bin/phpunit")
        campos = Revisor(correr=Falsa(reporte=CLOVER), buscar=lambda _: "php").revisar(raiz)
        self.assertEqual(80.0, campos["porcentaje"])
        self.assertEqual("app/Pago.php", campos["archivos"][0]["archivo"])
        self.assertEqual([3], campos["archivos"][0]["sin_pruebas"])

    def test_angular(self):
        salida = "=== Coverage summary ===\nStatements   : 70% ( 7/10 )\nLines        : 62.5% ( 5/8 )\n"
        campos = Revisor(correr=Falsa(stdout=salida), buscar=lambda _: "npx").revisar(_carpeta(self, "angular.json"))
        self.assertEqual(62.5, campos["porcentaje"])


class FaltaLaHerramientaOElPython(SimpleTestCase):
    """CP-005."""

    def test_sin_python_del_proyecto(self):
        campos = Revisor(correr=Falsa()).revisar(_carpeta(self, "manage.py"))
        self.assertEqual((Revision.FALLO, SIN_PYTHON), (campos["resultado"], campos["mensaje"]))

    def test_sin_coverage(self):
        falsa = Falsa(stderr="C:\\x\\python.exe: No module named coverage", returncode=1)
        campos = Revisor(correr=falsa).revisar(_django(self))
        self.assertEqual((Revision.FALLO, FALTA_HERRAMIENTA), (campos["resultado"], campos["mensaje"]))


class ConCuenta(TestCase):

    def entrar(self, administra=True):
        cuenta = User.objects.create_user("persona", password="una-clave-larga-1")
        if administra:
            cuenta.groups.add(Group.objects.get_or_create(name=ADMINISTRADOR)[0])
        self.client.force_login(cuenta)


class ElBotonArrancaLaRevisionAparte(ConCuenta):
    """CP-006."""

    def test_quien_administra(self):
        self.entrar()
        proyecto = Proyecto.objects.create(nombre="uno", ruta=_django(self))
        with mock.patch("core.pruebas.views.lanzar") as lanzar:
            pagina = self.client.post(reverse("pruebas:revisar", args=[proyecto.pk]), follow=True)
        lanzar.assert_called_once_with(proyecto)
        self.assertContains(pagina, "Revisando")
        self.assertIsNotNone(PruebasDelProyecto.de(proyecto).revisando_desde)

    def test_quien_no_administra(self):
        self.entrar(administra=False)
        proyecto = Proyecto.objects.create(nombre="uno", ruta=_django(self))
        with mock.patch("core.pruebas.views.lanzar") as lanzar:
            respuesta = self.client.post(reverse("pruebas:revisar", args=[proyecto.pk]))
        self.assertEqual(403, respuesta.status_code)
        lanzar.assert_not_called()


class LaOrdenHaceLaMismaRevision(TestCase):
    """CP-007."""

    def test_call_command(self):
        proyecto = Proyecto.objects.create(nombre="uno", ruta=_django(self))
        with mock.patch("core.pruebas.revisar.subprocess.run", Falsa(reporte=COVERAGE_JSON)):
            call_command("revisar_pruebas", proyecto="uno", stdout=open(os.devnull, "w"))
        self.assertEqual(75.0, Revision.ultima(proyecto).porcentaje)
        self.assertIsNone(PruebasDelProyecto.de(proyecto).revisando_desde)


class LaPaginaMuestraTodosLosProyectos(ConCuenta):
    """CP-008."""

    def test_dos_filas(self):
        self.entrar()
        revisado = Proyecto.objects.create(nombre="revisado", ruta=_django(self))
        Proyecto.objects.create(nombre="nuevo", ruta=_carpeta(self))
        Revision.objects.create(proyecto=revisado, fecha=timezone.now() - timedelta(days=2), porcentaje=50)
        pagina = self.client.get(reverse("pruebas:lista")).content.decode()
        self.assertIn("revisado", pagina)
        self.assertIn("nuevo", pagina)
        self.assertIn(AL_DIA, pagina)
        self.assertIn(NUNCA, pagina)

    def test_el_menu_lleva(self):
        self.entrar()
        self.assertContains(self.client.get("/"), 'href="%s"' % reverse("pruebas:lista"))


class ElDetalleYSuContraria(ConCuenta):
    """CP-009."""

    def test_menos_pruebas_primero_y_borrar(self):
        self.entrar()
        proyecto = Proyecto.objects.create(nombre="uno", ruta=_django(self))
        with mock.patch("core.pruebas.revisar.subprocess.run", Falsa(reporte=COVERAGE_JSON)):
            call_command("revisar_pruebas", proyecto="uno", stdout=open(os.devnull, "w"))
        pagina = self.client.get(reverse("pruebas:detalle", args=[proyecto.pk])).content.decode()
        self.assertLess(pagina.index("app/modelos.py"), pagina.index("app/vistas.py"))
        revision = Revision.ultima(proyecto)
        self.client.post(reverse("pruebas:borrar", args=[revision.pk]))
        self.assertFalse(Revision.objects.filter(pk=revision.pk).exists())
