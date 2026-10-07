# -*- coding: utf-8 -*-
"""`EP-026·HU-007` · Pruebas del botón de git: CP-001 a CP-004 de la fase A, con un repositorio temporal."""
import os
import shutil
import subprocess
import tempfile
from unittest import mock

from django.contrib.auth.models import Group, User
from django.test import TestCase

from core.cuentas.permisos import ADMINISTRADOR, CONSULTA
from core.validadores.sesiones import Sesiones

UNO, DOS = "aaaa1111-uno", "bbbb2222-dos"


def _git(raiz, *argumentos):
    return subprocess.run(["git"] + list(argumentos), cwd=raiz, capture_output=True, text=True, encoding="utf-8")


class ConRepositorio(TestCase):

    def setUp(self):
        self.raiz = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.raiz, True)
        _git(self.raiz, "init", "-q")
        _git(self.raiz, "config", "user.email", "prueba@ejemplo.org")
        _git(self.raiz, "config", "user.name", "Prueba")
        self.escribir(".gitignore", "historico-chat/.tocado/\n")
        _git(self.raiz, "add", ".gitignore")
        _git(self.raiz, "commit", "-q", "-m", "inicio")
        sesiones = Sesiones(self.raiz)
        for nombre, sesion in (("uno.txt", UNO), ("dos.txt", DOS), ("los-dos.txt", UNO), ("los-dos.txt", DOS)):
            self.escribir(nombre, "texto de %s\n" % nombre)
            sesiones.anotar(sesion, os.path.join(self.raiz, nombre))
        parche = mock.patch("core.estandar.views.raiz_del_repositorio", return_value=self.raiz)
        parche.start()
        self.addCleanup(parche.stop)
        self.admin = User.objects.create_user("admin", password="una-clave-larga-1")
        self.admin.groups.add(Group.objects.get_or_create(name=ADMINISTRADOR)[0])
        self.mira = User.objects.create_user("mira", password="una-clave-larga-1")
        self.mira.groups.add(Group.objects.get_or_create(name=CONSULTA)[0])

    def escribir(self, nombre, texto):
        with open(os.path.join(self.raiz, nombre), "w", encoding="utf-8") as f:
            f.write(texto)

    def commits(self):
        return int(_git(self.raiz, "rev-list", "--count", "HEAD").stdout.strip())

    def enviar(self, cuenta, **datos):
        self.client.force_login(cuenta)
        base = {"sesion": UNO, "asunto": "feat: lo de la sesión uno", "idea": "La idea del usuario.",
                "hecho": "Lo que hizo el agente."}
        base.update(datos)
        return self.client.post("/estandar/git/", base, follow=True)


class LoQueCambioCadaSesion(ConRepositorio):
    """CP-001."""

    def test_lista_cada_sesion_y_lo_compartido(self):
        self.client.force_login(self.mira)
        respuesta = self.client.get("/estandar/git/")
        self.assertContains(respuesta, "uno.txt")
        self.assertContains(respuesta, "dos.txt")
        self.assertContains(respuesta, "Los tocaron dos sesiones")
        self.assertContains(respuesta, "los-dos.txt")


class ElCommitDeUnaSesion(ConRepositorio):
    """CP-002."""

    def test_solo_lo_de_la_sesion_con_la_idea_primero(self):
        antes = self.commits()
        self.enviar(self.admin)
        self.assertEqual(antes + 1, self.commits())
        archivos = _git(self.raiz, "show", "--name-only", "--format=", "HEAD").stdout.split()
        self.assertEqual(["uno.txt"], archivos)
        cuerpo = _git(self.raiz, "log", "-1", "--format=%B").stdout
        self.assertLess(cuerpo.index("La idea del usuario."), cuerpo.index("Lo que hizo el agente."))
        self.assertNotIn("Co-Authored-By", cuerpo)


class SiFalla(ConRepositorio):
    """CP-003."""

    def test_nada_queda_preparado_ni_hay_commit(self):
        gancho = os.path.join(self.raiz, ".git", "hooks", "pre-commit")
        with open(gancho, "w", newline="\n") as f:
            f.write("#!/bin/sh\necho rechazado por la prueba\nexit 1\n")
        os.chmod(gancho, 0o755)
        antes = self.commits()
        respuesta = self.enviar(self.admin)
        self.assertEqual(antes, self.commits())
        self.assertEqual("", _git(self.raiz, "diff", "--cached", "--name-only").stdout.strip())
        self.assertContains(respuesta, "Sin subir")


class ConsultaNoHaceCommits(ConRepositorio):
    """CP-004."""

    def test_403_y_sin_commit(self):
        antes = self.commits()
        self.client.force_login(self.mira)
        self.assertEqual(403, self.client.post("/estandar/git/", {"sesion": UNO, "asunto": "x"}).status_code)
        self.assertEqual(antes, self.commits())
