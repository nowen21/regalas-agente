# -*- coding: utf-8 -*-
"""`EP-029·HU-005` · Las pruebas de navegador: CP-001 a CP-003 de la fase A.

`npx`, pip y Playwright se simulan (`08·T3`): ninguna prueba abre un navegador
ni baja nada. La salida de `npx playwright test --reporter=json` sigue la
documentación de Playwright: `stats` con `expected` y `unexpected`.
"""
import json
import os
import tempfile
from types import SimpleNamespace

from django.contrib.auth.models import Group, User
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from core.cuentas.permisos import ADMINISTRADOR
from core.herramientas.desinstalar import Desinstalador
from core.herramientas.instalar import Instalador
from core.proyectos.models import Proyecto
from core.pruebas.models import Revision
from core.pruebas.navegador import FALLARON, PASARON, SIN_PRUEBAS, Navegador

CIMIENTO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _carpeta(test, archivos):
    tmp = tempfile.TemporaryDirectory()
    test.addCleanup(tmp.cleanup)
    for archivo, texto in archivos.items():
        ruta = os.path.join(tmp.name, *archivo.split("/"))
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(texto)
    return tmp.name


class Falsa:
    def __init__(self, stdout="", returncode=0):
        self.stdout, self.returncode = stdout, returncode
        self.ordenes = []

    def __call__(self, partes, **_):
        self.ordenes.append(partes)
        return SimpleNamespace(stdout=self.stdout, stderr="", returncode=self.returncode)


def _json(bien, mal):
    return json.dumps({"stats": {"expected": bien, "unexpected": mal, "flaky": 0, "skipped": 0}})


class LaRevisionCorreLasPruebasDeNavegador(SimpleTestCase):
    """CP-001."""

    def test_con_playwright_config_pasaron(self):
        raiz = _carpeta(self, {"playwright.config.ts": "", "package.json": "{}"})
        falsa = Falsa(stdout=_json(3, 0))
        campos = Navegador(correr=falsa, buscar=lambda _: "npx").revisar(raiz)
        self.assertEqual(PASARON, campos["navegador"])
        self.assertIn("3", campos["navegador_detalle"])
        self.assertEqual(["npx", "playwright", "test", "--reporter=json"], falsa.ordenes[0])

    def test_con_playwright_config_fallaron(self):
        raiz = _carpeta(self, {"playwright.config.ts": ""})
        campos = Navegador(correr=Falsa(stdout=_json(2, 1)), buscar=lambda _: "npx").revisar(raiz)
        self.assertEqual(FALLARON, campos["navegador"])

    def test_django_con_un_archivo_que_usa_playwright(self):
        raiz = _carpeta(self, {"manage.py": "", ".venv/Scripts/python.exe": "",
                               "app/tests_pantallas.py": "from playwright.sync_api import sync_playwright\n",
                               "app/tests.py": "import unittest\n"})
        falsa = Falsa()
        campos = Navegador(correr=falsa).revisar(raiz)
        self.assertEqual(PASARON, campos["navegador"])
        self.assertEqual(["manage.py", "test", "--noinput", "app.tests_pantallas"], falsa.ordenes[0][1:])

    def test_sin_ninguna(self):
        falsa = Falsa()
        campos = Navegador(correr=falsa).revisar(_carpeta(self, {"manage.py": ""}))
        self.assertEqual(SIN_PRUEBAS, campos["navegador"])
        self.assertEqual([], falsa.ordenes)


class ElResultadoSaleEnLaPagina(TestCase):
    """CP-002."""

    def test_la_fila_dice_pasaron(self):
        cuenta = User.objects.create_user("admin", password="una-clave-larga-1")
        cuenta.groups.add(Group.objects.get_or_create(name=ADMINISTRADOR)[0])
        self.client.force_login(cuenta)
        proyecto = Proyecto.objects.create(nombre="uno", ruta=_carpeta(self, {}))
        Revision.objects.create(proyecto=proyecto, navegador=Revision.PASARON)
        self.assertContains(self.client.get(reverse("pruebas:lista")), '<td class="t-navegador">Pasaron</td>')


class PlaywrightEnCimiento(SimpleTestCase):
    """CP-003."""

    def setUp(self):
        self.instalador = Instalador.__new__(Instalador)
        self.instalador.estandar = os.path.dirname(os.path.dirname(CIMIENTO))
        self.python = Instalador.python_de_cimiento(CIMIENTO)
        if self.python is None:
            self.skipTest("Cimiento no tiene su ambiente en esta máquina")

    def test_preparar_sin_el_paquete(self):
        ordenes = []

        def ejecutar(partes, **_):
            ordenes.append(partes[1:])
            return SimpleNamespace(returncode=1 if partes[1:3] == ["-c", "import playwright"] else 0,
                                   stdout="", stderr="")
        pasos = self.instalador.preparar_playwright(True, ejecutar=ejecutar)
        self.assertIn(["-m", "pip", "install", "playwright==1.63.0"], ordenes)
        self.assertIn(["-m", "playwright", "install", "chromium"], ordenes)
        self.assertEqual(2, len(pasos))

    def test_quitar(self):
        ordenes = []
        pasos = Desinstalador(self.instalador).quitar_playwright(
            True, ejecutar=lambda partes, **_: ordenes.append(partes[1:]))
        self.assertEqual([["-m", "playwright", "uninstall", "--all"]], ordenes)
        self.assertEqual(1, len(pasos))

    def test_las_dependencias(self):
        with open(os.path.join(CIMIENTO, "requirements", "base.txt"), encoding="utf-8") as f:
            self.assertIn("playwright>=1.63,<2", f.read())
        with open(os.path.join(CIMIENTO, "requirements", "lock.txt"), encoding="utf-8") as f:
            lock = f.read().split()
        for exacta in ("playwright==1.63.0", "greenlet==3.5.6", "pyee==13.0.1", "typing_extensions==4.16.0"):
            self.assertIn(exacta, lock)


class LosDatosDeCoverageNoQuedanEnElProyecto(SimpleTestCase):
    """Defecto encontrado al cerrar la HU-005: `coverage run` dejaba `.coverage` en el proyecto."""

    def test_van_a_la_carpeta_temporal(self):
        from core.pruebas.revisar import Revisor
        entornos = []

        def correr(partes, **k):
            entornos.append(k.get("env", {}).get("COVERAGE_FILE"))
            return SimpleNamespace(stdout="", stderr="", returncode=0)
        raiz = _carpeta(self, {"manage.py": "", ".venv/Scripts/python.exe": ""})
        Revisor(correr=correr).revisar(raiz)
        self.assertTrue(entornos and all(entornos))
        self.assertFalse(any(os.path.dirname(e) == raiz for e in entornos))
