# -*- coding: utf-8 -*-
"""`EP-026·HU-003` · Pruebas de la importación: CP-001 a CP-003 de la fase A."""
import io
import os
import shutil
import tempfile

from django.test import TestCase

from core.comun import Proyecto as Carpeta
from core.historia import versiones
from core.historia.models import ESTANDAR, Cambio, Version
from core.proyectos.models import Proyecto

from .importar import MEMORIA, YaImportado, documentos, importar
from .models import Documento, Recuerdo


class LaImportacion(TestCase):

    def setUp(self):
        self.raiz = Carpeta.estandar()
        carpeta = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, carpeta, True)
        memoria = os.path.join(carpeta, MEMORIA)
        os.makedirs(memoria)
        for nombre, texto in (("memory.md", "# Índice\n"), ("uno.md", "Primero.\r\nCon CRLF.\r\n"),
                              ("dos.md", "Segundo.\n")):
            with io.open(os.path.join(memoria, nombre), "w", encoding="utf-8", newline="") as f:
                f.write(texto)
        self.proyecto = Proyecto.objects.create(nombre="con memoria", ruta=carpeta)

    def test_cp001_todo_base_entra_identico(self):
        importar(self.raiz)
        en_disco = documentos(self.raiz)
        self.assertEqual(len(en_disco), Documento.objects.count())
        self.assertGreater(len(en_disco), 100)
        for ruta, completa in en_disco:
            with io.open(completa, encoding="utf-8", newline="") as f:
                self.assertEqual(f.read(), Documento.objects.get(ruta=ruta).contenido, ruta)
        self.assertTrue(Documento.objects.filter(ruta="base/01-conducta.md").exists())
        self.assertTrue(Documento.objects.filter(ruta="base/tareas.md").exists())

    def test_cp002_la_memoria_de_cada_proyecto_entra(self):
        importar(self.raiz)
        nombres = set(Recuerdo.objects.filter(proyecto=self.proyecto).values_list("nombre", flat=True))
        self.assertEqual({"memory.md", "uno.md", "dos.md"}, nombres)
        self.assertEqual("Primero.\r\nCon CRLF.\r\n", Recuerdo.objects.get(proyecto=self.proyecto, nombre="uno.md").contenido)

    def test_cp003_version_de_partida_y_una_sola_vez(self):
        numero = versiones.del_archivo()
        version, n_doc, _ = importar(self.raiz)
        self.assertEqual("%d.%d.%d" % numero, version.numero)
        self.assertEqual(ESTANDAR, version.ambito)
        self.assertEqual(n_doc, Cambio.objects.filter(tabla="estandar.documento", version=version).count())
        self.assertEqual(1, Version.objects.filter(ambito=ESTANDAR).count())
        with self.assertRaises(YaImportado):
            importar(self.raiz)
        self.assertEqual(n_doc, Documento.objects.count())
