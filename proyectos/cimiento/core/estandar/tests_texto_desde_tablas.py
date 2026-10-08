# -*- coding: utf-8 -*-
"""`EP-027·HU-003` · Pruebas de la fase A: todo cambio pasa por las tablas (CP-001 a CP-003)."""
import io
from unittest import mock

from django.contrib.auth.models import Group, User
from django.core.management import call_command
from django.test import TestCase

from core.comun import Proyecto as Carpeta
from core.cuentas.permisos import ADMINISTRADOR
from core.historia.registro import quien_y_por_que

from . import cambios, importar as importar_modulo
from .importar import importar
from .models import CAMBIAR, DOCUMENTO, Documento, Propuesta, Regla
from .reglas import pasar_todo, texto_armado

F1 = "base/02-flujo-de-trabajo/reglas/F1-carga-el-contexto-antes-de-actuar.md"
F2 = "base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md"
RESPUESTAS = {"version_obliga": "no", "version_agrega": "no", "version_motivo": "prueba"}
NUEVA = "Antes de analizar, lee la documentación del proyecto y la del estándar."


class ConLasTablasLlenas(TestCase):

    @classmethod
    def setUpTestData(cls):
        importar(Carpeta.estandar())
        with quien_y_por_que(quien="prueba", motivo="prueba"):
            pasar_todo(Carpeta.estandar())
        cls.admin = User.objects.create_user("admin", password="una-clave-larga-1")
        cls.admin.groups.add(Group.objects.get_or_create(name=ADMINISTRADOR)[0])

    def regla(self, codigo):
        return Regla.objects.get(codigo=codigo, proyecto__isnull=True)

    def doc(self, ruta):
        return Documento.objects.get(ruta=ruta)

    def con_exigencia_nueva(self, ruta, codigo):
        return self.doc(ruta).contenido.replace(self.regla(codigo).exigencia, NUEVA)

    def assertArmado(self, documento):
        documento.refresh_from_db()
        self.assertEqual(texto_armado(documento), documento.contenido.replace("\r\n", "\n"))


class CambiarPasaPorLasTablas(ConLasTablasLlenas):
    """CP-001."""

    def test_desde_la_pantalla(self):
        self.client.force_login(self.admin)
        documento = self.doc(F1)
        self.client.post("/estandar/documento/%d/" % documento.pk,
                         dict(RESPUESTAS, contenido=self.con_exigencia_nueva(F1, "F1")))
        self.assertEqual(NUEVA, self.regla("F1").exigencia)
        self.assertArmado(documento)

    def test_al_aprobar_una_propuesta(self):
        texto = self.doc(F1).contenido.replace("Carga el contexto antes de actuar", "Carga el contexto primero", 1)
        propuesta = Propuesta.objects.create(objeto=DOCUMENTO, accion=CAMBIAR, ruta=F1, contenido=texto,
                                             quien="agente")
        with quien_y_por_que(cuenta=self.admin, motivo="prueba"):
            cambios.aplicar(propuesta, self.admin)
        self.assertEqual("Carga el contexto primero", self.regla("F1").titulo)
        self.assertArmado(self.doc(F1))

    def test_al_sincronizar_con_git(self):
        en_base = dict(Documento.objects.values_list("ruta", "contenido"))
        en_base[F2] = self.con_exigencia_nueva(F2, "F2")
        with mock.patch.object(importar_modulo, "_en_git", return_value=en_base):
            importar_modulo.sincronizar(Carpeta.estandar())
        self.assertEqual(NUEVA, self.regla("F2").exigencia)
        self.assertArmado(self.doc(F2))


class NadaSeBorra(ConLasTablasLlenas):
    """CP-002."""

    def test_quitar_el_documento_deja_la_regla_sin_documento(self):
        with quien_y_por_que(cuenta=self.admin, motivo="prueba"):
            cambios.quitar_documento(self.doc(F2))
        f2 = self.regla("F2")
        self.assertIsNone(f2.documento)
        self.assertFalse(Documento.objects.filter(ruta=F2).exists())

    def test_la_regla_que_sale_del_texto_queda_sin_documento(self):
        documento = self.doc("base/01-conducta.md")
        texto = documento.contenido.replace("\r\n", "\n")
        inicio = texto.index("## C1 · ")
        fin = texto.index("## C2 · ")
        with quien_y_por_que(cuenta=self.admin, motivo="prueba"):
            cambios.guardar_documento(documento.ruta, texto[:inicio] + texto[fin:])
        self.assertIsNone(self.regla("C1").documento)
        self.assertEqual(documento, self.regla("C2").documento)


class ElAgenteRecibeElTextoArmado(ConLasTablasLlenas):
    """CP-003."""

    def test_ver_estandar(self):
        with quien_y_por_que(cuenta=self.admin, motivo="prueba"):
            cambios.guardar_documento(F1, self.con_exigencia_nueva(F1, "F1"))
        salida = io.StringIO()
        call_command("ver_estandar", F1, stdout=salida)
        self.assertIn(NUEVA, salida.getvalue())
        self.assertEqual(texto_armado(self.doc(F1)), salida.getvalue().replace("\r\n", "\n"))
