# -*- coding: utf-8 -*-
"""`EP-028·HU-004` · La pantalla de propuestas y las preguntas de versión se entienden: CP-001 y CP-002."""
from django.contrib.auth.models import Group, User
from django.test import TestCase
from django.urls import reverse

from core.cuentas.permisos import ADMINISTRADOR

from .models import CAMBIAR, DOCUMENTO, PENDIENTE, RECHAZADA, Documento, Propuesta


class ConPropuesta(TestCase):

    def setUp(self):
        cuenta = User.objects.create_user("admin", password="una-clave-larga-1")
        cuenta.groups.add(Group.objects.get_or_create(name=ADMINISTRADOR)[0])
        self.client.force_login(cuenta)
        Documento.objects.create(ruta="base/prueba.md", contenido="# Prueba\n\nla línea vieja\notra igual\n")
        self.propuesta = Propuesta.objects.create(objeto=DOCUMENTO, accion=CAMBIAR, ruta="base/prueba.md",
                                                  contenido="# Prueba\n\nla línea nueva\notra igual\n",
                                                  motivo="probar", quien="agente", estado=PENDIENTE)


class SeVeQueCambia(ConPropuesta):
    """CP-001."""

    def test_cp001_muestra_lo_que_sale_y_lo_que_entra(self):
        pagina = self.client.get(reverse("estandar:propuestas")).content.decode()
        self.assertIn('text-danger">− la línea vieja', pagina)
        self.assertIn('text-success">+ la línea nueva', pagina)

    def test_cp001_rechazar_pide_el_motivo(self):
        url = reverse("estandar:rechazar", args=[self.propuesta.pk])
        self.client.post(url, {})
        self.propuesta.refresh_from_db()
        self.assertEqual(PENDIENTE, self.propuesta.estado)
        self.client.post(url, {"motivo_rechazo": "repite otra regla"})
        self.propuesta.refresh_from_db()
        self.assertEqual(RECHAZADA, self.propuesta.estado)
        self.assertEqual("repite otra regla", self.propuesta.motivo_rechazo)


class LasPreguntasSeEntienden(ConPropuesta):
    """CP-002."""

    def test_cp002_preguntas_claras_con_su_ayuda_y_el_tipo_a_la_vista(self):
        pagina = self.client.get(reverse("estandar:propuestas")).content.decode()
        self.assertIn("¿Algún proyecto tiene que cambiar algo para seguir cumpliendo el estándar?", pagina)
        self.assertIn("¿El cambio agrega algo nuevo que un proyecto puede usar si quiere?", pagina)
        self.assertIn("resultado-version", pagina)
        self.assertNotIn("nadie está obligado a usar?", pagina)
        self.assertIn("¿Algún proyecto tiene que cambiar algo?", pagina)       # el título del «?»
        self.assertIn("¿Agrega algo nuevo que se puede usar si se quiere?", pagina)
        self.assertNotIn("Falta el texto de ayuda", pagina)
