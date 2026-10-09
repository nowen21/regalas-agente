"""`EP-030·HU-001` · Un solo camino para leer y escribir documentos, con un comando fijo por tipo."""
import io
import os
import tempfile

from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import TestCase

from core.estandar import documentos
from core.estandar.cambios import aplicar
from core.estandar.models import PENDIENTE, Documento, Propuesta, Recuerdo
from core.historia.models import Cambio
from core.proyectos.models import Proyecto


def _correr(*args, **opciones):
    salida = io.StringIO()
    call_command(*args, stdout=salida, **opciones)
    return salida.getvalue()


class ConDocumentos(TestCase):

    def setUp(self):
        Documento.objects.create(ruta="base/01-conducta.md", contenido="# Conducta\n")
        Documento.objects.create(ruta="base/02-flujo.md", contenido="# Flujo\n")
        self.carpeta = tempfile.mkdtemp()
        self.proyecto = Proyecto.objects.create(nombre="de prueba", ruta=self.carpeta)
        Recuerdo.objects.create(proyecto=self.proyecto, nombre="memory.md", contenido="# Memoria\n")
        archivo = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8", newline="")
        archivo.write("# Texto nuevo\n")
        archivo.close()
        self.archivo = archivo.name

    def tearDown(self):
        os.unlink(self.archivo)


class ListarYVer(ConDocumentos):
    """CP-001."""

    def test_lista_las_rutas_que_empiezan_asi(self):
        self.assertEqual(_correr("documento", "listar", "estandar", "base/01").split(), ["base/01-conducta.md"])

    def test_muestra_el_texto_exacto(self):
        self.assertEqual(_correr("documento", "ver", "estandar", "base/02-flujo.md"), "# Flujo\n")

    def test_muestra_un_recuerdo_del_proyecto(self):
        self.assertEqual(_correr("documento", "ver", "recuerdo", "memory.md", proyecto=self.carpeta), "# Memoria\n")

    def test_lo_que_no_esta_da_error(self):
        with self.assertRaisesMessage(CommandError, "no está"):
            _correr("documento", "ver", "estandar", "base/no-existe.md")


class CrearEditarQuitar(ConDocumentos):
    """CP-002: escribir deja una propuesta; nada cambia todavía."""

    def test_crear_un_recuerdo_deja_la_propuesta(self):
        _correr("documento", "crear", "recuerdo", "nuevo.md", proyecto=self.carpeta, archivo=self.archivo,
                motivo="prueba")
        p = Propuesta.objects.get()
        self.assertEqual((p.accion, p.estado, p.nombre, p.contenido), ("crear", PENDIENTE, "nuevo.md", "# Texto nuevo\n"))
        self.assertFalse(Recuerdo.objects.filter(nombre="nuevo.md").exists())

    def test_editar_no_cambia_el_texto_hasta_aprobar(self):
        _correr("documento", "editar", "estandar", "base/01-conducta.md", archivo=self.archivo, motivo="prueba")
        self.assertEqual(Propuesta.objects.get().accion, "cambiar")
        self.assertEqual(Documento.objects.get(ruta="base/01-conducta.md").contenido, "# Conducta\n")

    def test_quitar_deja_la_propuesta_de_quitar(self):
        _correr("documento", "quitar", "estandar", "base/02-flujo.md", motivo="prueba")
        self.assertEqual(Propuesta.objects.get().accion, "quitar")

    def test_crear_lo_que_ya_existe_da_error(self):
        with self.assertRaisesMessage(CommandError, "ya existe"):
            _correr("documento", "crear", "estandar", "base/01-conducta.md", archivo=self.archivo, motivo="prueba")

    def test_sin_motivo_da_error(self):
        with self.assertRaisesMessage(CommandError, "motivo"):
            _correr("documento", "editar", "estandar", "base/01-conducta.md", archivo=self.archivo)

    def test_un_tipo_que_no_existe_lista_los_que_hay(self):
        with self.assertRaisesMessage(CommandError, "estandar, recuerdo"):
            _correr("documento", "ver", "pendiente", "x")


class LasOrdenesDeAntesUsanElCamino(ConDocumentos):
    """CP-003."""

    def test_ver_estandar_da_lo_mismo(self):
        self.assertEqual(_correr("ver_estandar", "base/01-conducta.md"),
                         _correr("documento", "ver", "estandar", "base/01-conducta.md"))

    def test_ver_estandar_lista_igual(self):
        self.assertEqual(_correr("ver_estandar", "base/", lista=True),
                         _correr("documento", "listar", "estandar", "base/"))

    def test_ver_recuerdo_da_lo_mismo(self):
        self.assertEqual(_correr("ver_recuerdo", "memory.md", proyecto=self.carpeta),
                         _correr("documento", "ver", "recuerdo", "memory.md", proyecto=self.carpeta))

    def test_proponer_deja_la_misma_propuesta(self):
        _correr("proponer", ruta="base/01-conducta.md", archivo=self.archivo, motivo="prueba")
        p = Propuesta.objects.get()
        self.assertEqual((p.objeto, p.accion, p.ruta), ("documento", "cambiar", "base/01-conducta.md"))

    def test_el_camino_es_uno_solo(self):
        self.assertEqual(sorted(documentos.TIPOS), ["estandar", "recuerdo"])


class LaHistoria(ConDocumentos):
    """CP-004."""

    def test_aprobar_deja_el_antes_y_el_despues(self):
        propuesta = documentos.proponer("recuerdo", documentos.EDITAR, "memory.md", "# Cambiada\n", "prueba",
                                        proyecto=self.proyecto)
        aplicar(propuesta, None)
        cambio = Cambio.objects.filter(tabla="estandar.recuerdo", accion="cambiar").latest("id")
        self.assertEqual((cambio.antes["contenido"], cambio.despues["contenido"]), ("# Memoria\n", "# Cambiada\n"))
