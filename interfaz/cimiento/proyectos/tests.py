# -*- coding: utf-8 -*-
"""Pendiente 75 · El registro de proyectos deja de ser un .md a mano.

Lo que estas pruebas fijan: el ciclo completo del registro (registrar,
consultar, editar, dar de baja) sin editar ningún archivo, la ida y vuelta con
`plantillas/proyectos.md` (que el instalador sigue leyendo), y que dar de baja
saca del .md exportado sin borrar la historia.
"""
import io
import os
import tempfile
from unittest import mock

from django.test import TestCase

from . import core
from .models import Proyecto


class Registro(TestCase):

    def test_ciclo_completo_sin_editar_archivos(self):
        r = self.client.post("/proyectos/nuevo/", {
            "nombre": "demo", "ruta": "C:/tmp/demo", "scope": "proyecto:demo",
            "stack": "por detectar", "activo": "on", "notas": ""})
        self.assertEqual(302, r.status_code)
        p = Proyecto.objects.get(nombre="demo")
        self.client.post(f"/proyectos/{p.pk}/baja/")
        p.refresh_from_db()
        self.assertFalse(p.activo)
        self.assertEqual(200, self.client.get("/proyectos/").status_code)

    def test_exporta_solo_activos_y_no_borra_historia(self):
        Proyecto.objects.create(nombre="vivo", ruta="C:/x", scope="s", stack="k")
        Proyecto.objects.create(nombre="baja", ruta="C:/y", activo=False)
        with tempfile.TemporaryDirectory() as tmp:
            destino = os.path.join(tmp, "proyectos.md")
            with mock.patch.object(core, "REGISTRO_MD", destino):
                filas = core.exportar()
            texto = io.open(destino, encoding="utf-8").read()
        self.assertEqual(1, filas)
        self.assertIn("| vivo |", texto)
        self.assertNotIn("| baja |", texto)
        self.assertTrue(Proyecto.objects.filter(nombre="baja").exists())

    def test_importa_lo_del_instalador_sin_pisar_lo_editado(self):
        Proyecto.objects.create(nombre="editado", ruta="C:/real",
                                stack="Django 5")
        md = core.CABECERA + (
            "| editado | `C:/vieja` | `s` | por detectar |\n"
            "| nuevo-del-instalador | `C:/n` | `proyecto:n` | por detectar |\n")
        with tempfile.TemporaryDirectory() as tmp:
            origen = os.path.join(tmp, "proyectos.md")
            io.open(origen, "w", encoding="utf-8", newline="").write(md)
            with mock.patch.object(core, "REGISTRO_MD", origen):
                nuevas = core.importar()
        self.assertEqual(1, nuevas)
        self.assertEqual("C:/real", Proyecto.objects.get(nombre="editado").ruta)
        self.assertTrue(Proyecto.objects.filter(
            nombre="nuevo-del-instalador").exists())

    def test_medir_muestra_el_expediente(self):
        with tempfile.TemporaryDirectory() as tmp:
            os.makedirs(os.path.join(tmp, "prompts"))
            io.open(os.path.join(tmp, "prompts", "x-planteamiento.md"), "w",
                    encoding="utf-8").write(u"El problema.\n")
            p = Proyecto.objects.create(nombre="medible", ruta=tmp)
            r = self.client.get(f"/proyectos/{p.pk}/medir/")
        self.assertEqual(200, r.status_code)
        self.assertIn(b"Planteamiento", r.content)

    def test_medir_con_ruta_rota_no_revienta(self):
        p = Proyecto.objects.create(nombre="roto", ruta="C:/no-existe-nada")
        r = self.client.get(f"/proyectos/{p.pk}/medir/")
        self.assertEqual(200, r.status_code)
