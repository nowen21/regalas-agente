# -*- coding: utf-8 -*-
"""`EP-026·HU-009` · La vista previa de las reglas: CP-004 de la fase A."""
import tempfile
from unittest import mock

from django.contrib.auth.models import User
from django.test import TestCase

from core.historia.models import Cambio
from core.proyectos.models import Proyecto


class LaVistaPrevia(TestCase):
    """CP-004."""

    def test_muestra_el_bloque_y_no_guarda_nada(self):
        carpeta = tempfile.TemporaryDirectory()
        self.addCleanup(carpeta.cleanup)
        proyecto = Proyecto.objects.create(nombre="uno", ruta=carpeta.name)
        self.client.force_login(User.objects.create_user("mira"))
        antes = Cambio.objects.count()
        with mock.patch("core.herramientas.recuperar.RecuperadorDeReglas.como_texto",
                        return_value="[REGLAS] 02·F8") as como_texto:
            respuesta = self.client.get("/estandar/vista-previa/", {"proyecto": proyecto.pk,
                                                                    "mensaje": "Hágalo: corrija el plan"})
        self.assertContains(respuesta, "[REGLAS] 02·F8")
        self.assertContains(respuesta, "15 · registros inmutables: no")
        como_texto.assert_called_once_with("Hágalo: corrija el plan", proyecto=proyecto.ruta)
        self.assertEqual(antes, Cambio.objects.count())

    def test_con_el_estandar_real_trae_las_reglas(self):
        carpeta = tempfile.TemporaryDirectory()
        self.addCleanup(carpeta.cleanup)
        proyecto = Proyecto.objects.create(nombre="uno", ruta=carpeta.name)
        self.client.force_login(User.objects.create_user("mira"))
        respuesta = self.client.get("/estandar/vista-previa/", {"proyecto": proyecto.pk,
                                                                "mensaje": "Hágalo: haga el commit"})
        self.assertContains(respuesta, "Lo que le llegaría al agente")
        self.assertContains(respuesta, "09·")
