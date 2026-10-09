# -*- coding: utf-8 -*-
"""`EP-029·HU-007` · Cada programa de un proyecto: CP-001 a CP-003 de la fase A.

La herramienta de cada lenguaje se simula (`08·T3`). Los valores esperados salen
de la HU (RN-01 a RN-04), no del código (`08·T8`).
"""
import json
import os
import tempfile
from types import SimpleNamespace

from django.contrib.auth.models import Group, User
from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.utils import timezone

from core.cuentas.permisos import ADMINISTRADOR
from core.proyectos.models import Proyecto
from core.pruebas.lenguaje import ANGULAR, DJANGO, PYTHON, reconocer_todos
from core.pruebas.models import Revision
from core.pruebas.parte import ParteQueRevisa
from core.pruebas.revisar import Revisor, revisar_y_guardar


def _carpeta(test, *archivos):
    tmp = tempfile.TemporaryDirectory()
    test.addCleanup(tmp.cleanup)
    for archivo in archivos:
        ruta = os.path.join(tmp.name, *archivo.split("/"))
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        open(ruta, "w").close()
    return tmp.name


def _frente_y_servidor(test):
    return _carpeta(test, "proyectos/front/angular.json", "proyectos/back/requirements.txt",
                    "proyectos/back/.venv/Scripts/python.exe")


class Falsa:
    """Hace de cada herramienta: coverage.py con 75%, ng test con 62,5%."""

    def __init__(self):
        self.ordenes = []

    def __call__(self, partes, **_):
        self.ordenes.append(partes)
        if "-o" in partes:
            with open(partes[partes.index("-o") + 1], "w", encoding="utf-8") as f:
                json.dump({"totals": {"percent_covered": 75.0}, "files": {}}, f)
        salida = "Lines        : 62.5% ( 5/8 )\n" if "ng" in partes else ""
        codigo = 1 if partes[1:3] == ["-c", "import coverage"] else 0
        return SimpleNamespace(stdout=salida, stderr="", returncode=codigo)


class EncuentraTodosLosProgramas(SimpleTestCase):
    """CP-001."""

    def test_frente_y_servidor(self):
        raiz = _frente_y_servidor(self)
        programas = {(l.nombre, os.path.relpath(l.carpeta, raiz).replace("\\", "/")) for l in reconocer_todos(raiz)}
        self.assertEqual({(ANGULAR, "proyectos/front"), (PYTHON, "proyectos/back")}, programas)

    def test_lo_de_adentro_de_django_es_de_django(self):
        raiz = _carpeta(self, "manage.py", "docs/requirements.txt")
        self.assertEqual([DJANGO], [l.nombre for l in reconocer_todos(raiz)])


class RevisaYPonLaParteEnCadaUno(TestCase):
    """CP-002."""

    def test_dos_revisiones_con_la_misma_fecha(self):
        raiz = _frente_y_servidor(self)
        proyecto = Proyecto.objects.create(nombre="rni", ruta=raiz)
        revisar_y_guardar(proyecto, Revisor(correr=Falsa(), buscar=lambda nombre: nombre))
        ultimas = Revision.ultimas(proyecto)
        self.assertEqual(["proyectos/back", "proyectos/front"], [r.programa for r in ultimas])
        self.assertEqual(1, len({r.fecha for r in ultimas}))
        self.assertEqual({"coverage.py", "ng test"}, {r.herramienta for r in ultimas})

    def test_la_parte_en_cada_uno(self):
        falsa = Falsa()
        pasos, _, puesta = ParteQueRevisa(ejecutar=falsa).poner(_frente_y_servidor(self), aplicar=True)
        self.assertTrue(puesta)
        self.assertIn(["-m", "pip", "install", "coverage"], [o[1:] for o in falsa.ordenes])
        self.assertTrue(any("proyectos/front" in p for p in pasos))
        self.assertTrue(any("proyectos/back" in p for p in pasos))


class LaFilaYElDetalle(TestCase):
    """CP-003."""

    def test_la_fila_dice_la_de_menos_y_el_detalle_las_dos(self):
        cuenta = User.objects.create_user("admin", password="una-clave-larga-1")
        cuenta.groups.add(Group.objects.get_or_create(name=ADMINISTRADOR)[0])
        self.client.force_login(cuenta)
        proyecto = Proyecto.objects.create(nombre="rni", ruta=_frente_y_servidor(self))
        ahora = timezone.now()
        Revision.objects.create(proyecto=proyecto, fecha=ahora, programa="proyectos/front", porcentaje=80)
        Revision.objects.create(proyecto=proyecto, fecha=ahora, programa="proyectos/back", porcentaje=30)
        lista = self.client.get(reverse("pruebas:lista")).content.decode()
        self.assertIn('t-porcentaje">30,0%', lista)      # con coma decimal, como en Colombia
        self.assertIn("Angular y Python", lista)
        detalle = self.client.get(reverse("pruebas:detalle", args=[proyecto.pk])).content.decode()
        self.assertIn("proyectos/front: última revisión", detalle)
        self.assertIn("proyectos/back: última revisión", detalle)
