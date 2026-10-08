# -*- coding: utf-8 -*-
"""`EP-027·HU-001` · CP-001: las tablas tienen las casillas del molde."""
from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import (BLINDADA, DEPENDE, FALTA_EL_PROGRAMA, Capitulo, Dependencia, Documento, Regla, ReglaTarea,
                     Tarea)


class LasTablasGuardanLasCasillas(TestCase):

    def setUp(self):
        self.documento = Documento.objects.create(ruta="base/99-prueba.md", contenido="# 99 · Prueba\n")
        self.capitulo = Capitulo.objects.create(clave="99-prueba", numero="99", nombre="99 · Prueba",
                                                prefijo="PB", documento=self.documento)

    def regla(self, **cambios):
        datos = dict(capitulo=self.capitulo, documento=self.documento, codigo="PB1", titulo="Prueba algo",
                     marca=BLINDADA, exigencia="Prueba algo siempre.", excepcion="**Excepción** — nunca (condición)",
                     excepcion_condicion="nunca", ejemplo="INCORRECTO: no probar\nCORRECTO:   probar",
                     ejemplo_incorrecto="no probar", ejemplo_correcto="probar", quien_cumple="**Nadie la hace cumplir:** x",
                     validable=FALTA_EL_PROGRAMA, autoriza_escribir="**Autoriza escribir:** `x/*.md`",
                     sello="### Checklist  ·  **CUMPLE**", sello_resultado="CUMPLE", sello_version="2.5.0",
                     sello_fecha="2026-08-07", sello_observacion="Nada.")
        datos.update(cambios)
        return Regla(**datos)

    def test_se_guarda_y_se_lee_igual(self):
        regla = self.regla()
        regla.full_clean()
        regla.save()
        uno, dos = Tarea.objects.create(nombre="cambiar-codigo"), Tarea.objects.create(nombre="tocar-git")
        ReglaTarea.objects.create(regla=regla, tarea=dos, orden=0)
        ReglaTarea.objects.create(regla=regla, tarea=uno, orden=1)
        otra = self.regla(codigo="PB2", marca="")
        otra.save()
        Dependencia.objects.create(regla=regla, tipo=DEPENDE, codigo="PB2", destino=otra)
        leida = Regla.objects.get(pk=regla.pk)
        self.assertEqual(("PB1", BLINDADA, FALTA_EL_PROGRAMA, "2.5.0"),
                         (leida.codigo, leida.marca, leida.validable, leida.sello_version))
        self.assertEqual(["tocar-git", "cambiar-codigo"], [a.tarea.nombre for a in leida.aplica.all()])
        self.assertEqual([("depende de", "PB2")], [(d.tipo, d.destino.codigo) for d in leida.dependencias.all()])
        self.assertEqual(["PB1"], [d.regla.codigo for d in otra.dependientes.all()])

    def test_marca_dependencia_y_validable_solo_con_sus_valores(self):
        for campo, valor in (("marca", "secreta"), ("validable", "quizas")):
            with self.assertRaises(ValidationError):
                self.regla(**{campo: valor}).full_clean()
        regla = self.regla()
        regla.save()
        with self.assertRaises(ValidationError):
            Dependencia(regla=regla, tipo="copia", codigo="PB2").full_clean()

    def test_el_codigo_no_se_repite(self):
        self.regla().save()
        with self.assertRaises(ValidationError):
            self.regla(titulo="Otra con el mismo código").full_clean()
