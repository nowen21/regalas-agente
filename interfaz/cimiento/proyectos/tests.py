# -*- coding: utf-8 -*-
"""Pendiente 75 · El registro de proyectos deja de ser un .md a mano.
Pendiente 76 · El registro real nunca se vacía por accidente.

Lo que estas pruebas fijan: el ciclo completo del registro (registrar,
consultar, editar, dar de baja) sin editar ningún archivo, la ida y vuelta con
`plantillas/proyectos.md` (que el instalador sigue leyendo), que dar de baja
saca del .md exportado sin borrar la historia, y que exportar **nunca** escribe
cero filas sobre un archivo que tenía filas.

**Y que ninguna prueba toque el registro real.** La primera versión de estas
pruebas lo hizo: las vistas exportaban la base de pruebas, vacía, sobre
`plantillas/proyectos.md`, y los proyectos reprobaban «registro» en cada
mensaje. Por eso todas corren con el .md apuntando a una carpeta temporal.
"""
import io
import os
import shutil
import tempfile
from unittest import mock

from django.core.management import call_command
from django.test import TestCase

from . import core
from .models import Proyecto


class Registro(TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.md = os.path.join(self.tmp, "proyectos.md")
        self._parche = mock.patch.object(core, "REGISTRO_MD", self.md)
        self._parche.start()

    def tearDown(self):
        self._parche.stop()
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _leer_md(self):
        return io.open(self.md, encoding="utf-8").read()

    def test_ciclo_completo_sin_editar_archivos(self):
        r = self.client.post("/proyectos/nuevo/", {
            "nombre": "demo", "ruta": "C:/tmp/demo", "scope": "proyecto:demo",
            "stack": "por detectar", "activo": "on", "notas": ""})
        self.assertEqual(302, r.status_code)
        p = Proyecto.objects.get(nombre="demo")
        self.assertIn("| demo |", self._leer_md())
        self.client.post(f"/proyectos/{p.pk}/baja/")
        p.refresh_from_db()
        self.assertFalse(p.activo)
        self.assertEqual(200, self.client.get("/proyectos/").status_code)

    def test_exporta_solo_activos_y_no_borra_historia(self):
        Proyecto.objects.create(nombre="vivo", ruta="C:/x", scope="s", stack="k")
        Proyecto.objects.create(nombre="baja", ruta="C:/y", activo=False)
        filas = core.exportar()
        texto = self._leer_md()
        self.assertEqual(1, filas)
        self.assertIn("| vivo |", texto)
        self.assertNotIn("| baja |", texto)
        self.assertTrue(Proyecto.objects.filter(nombre="baja").exists())

    def test_exportar_vacio_no_pisa_un_md_con_filas(self):
        """Pendiente 76: la base vacía nunca borra la lista real."""
        io.open(self.md, "w", encoding="utf-8", newline="").write(
            core.CABECERA + "| real | `C:/r` | `s` | k |\n")
        with self.assertRaises(core.RegistroVacio):
            core.exportar()
        self.assertIn("| real |", self._leer_md())

    def test_exportar_vacio_sobre_md_vacio_si_escribe(self):
        """Un registro vacío de verdad sí se exporta: no hay nada que perder."""
        self.assertEqual(0, core.exportar())
        self.assertNotIn("| ", self._leer_md().split("|---|---|---|---|")[1])

    def test_importa_lo_del_instalador_sin_pisar_lo_editado(self):
        Proyecto.objects.create(nombre="editado", ruta="C:/real",
                                stack="Django 5")
        io.open(self.md, "w", encoding="utf-8", newline="").write(
            core.CABECERA +
            "| editado | `C:/vieja` | `s` | por detectar |\n"
            "| nuevo-del-instalador | `C:/n` | `proyecto:n` | por detectar |\n")
        self.assertEqual(1, core.importar())
        self.assertEqual("C:/real", Proyecto.objects.get(nombre="editado").ruta)
        self.assertTrue(Proyecto.objects.filter(
            nombre="nuevo-del-instalador").exists())

    def test_el_comando_registrar_da_de_alta_y_exporta(self):
        """La puerta del instalador: alta en el registro y .md regenerado."""
        call_command("registrar", nombre="nuevo", ruta="C:/nuevo",
                     scope="proyecto:nuevo")
        self.assertTrue(Proyecto.objects.filter(nombre="nuevo").exists())
        self.assertIn("| nuevo |", self._leer_md())
        call_command("registrar", nombre="nuevo", ruta="C:/movido")
        self.assertEqual("C:/movido", Proyecto.objects.get(nombre="nuevo").ruta)
        self.assertEqual(1, Proyecto.objects.filter(nombre="nuevo").count())

    def test_medir_muestra_el_expediente(self):
        os.makedirs(os.path.join(self.tmp, "prompts"))
        io.open(os.path.join(self.tmp, "prompts", "x-planteamiento.md"), "w",
                encoding="utf-8").write(u"El problema.\n")
        p = Proyecto.objects.create(nombre="medible", ruta=self.tmp)
        r = self.client.get(f"/proyectos/{p.pk}/medir/")
        self.assertEqual(200, r.status_code)
        self.assertIn(b"Planteamiento", r.content)

    def test_medir_con_ruta_rota_no_revienta(self):
        p = Proyecto.objects.create(nombre="roto", ruta="C:/no-existe-nada")
        r = self.client.get(f"/proyectos/{p.pk}/medir/")
        self.assertEqual(200, r.status_code)
