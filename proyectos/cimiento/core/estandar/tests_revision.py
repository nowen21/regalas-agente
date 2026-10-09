"""`EP-030·HU-002` · Los cambios de los documentos se revisan y se aprueban en la pantalla, para cualquier tipo."""
import tempfile

from django.contrib.auth.models import Group, User
from django.test import TestCase
from django.urls import reverse

from core.cuentas.permisos import ADMINISTRADOR
from core.estandar import documentos
from core.estandar.cambios import aplicar
from core.estandar.models import APROBADA, Documento, Propuesta, Recuerdo
from core.proyectos.models import Proyecto


class ConPropuestas(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.admin = User.objects.create_user("revisa", password="-".join(["una", "clave", "de", "prueba"]))
        cls.admin.groups.add(Group.objects.get_or_create(name=ADMINISTRADOR)[0])

    def setUp(self):
        self.client.force_login(self.admin)
        Documento.objects.create(ruta="base/99-prueba.md", contenido="# Prueba\nlinea vieja\n")
        self.proyecto = Proyecto.objects.create(nombre="revisado", ruta=tempfile.mkdtemp())
        Recuerdo.objects.create(proyecto=self.proyecto, nombre="memory.md", contenido="# Memoria\nrecuerdo viejo\n")
        self.del_documento = documentos.proponer("estandar", documentos.EDITAR, "base/99-prueba.md",
                                                 "# Prueba\nlinea nueva\n", "prueba")
        self.del_recuerdo = documentos.proponer("recuerdo", documentos.EDITAR, "memory.md",
                                                "# Memoria\nrecuerdo nuevo\n", "prueba", proyecto=self.proyecto)


class LaPantallaMuestraLoQueCambio(ConPropuestas):
    """CP-001."""

    def test_se_ven_el_antes_y_el_despues_de_cada_tipo(self):
        pagina = self.client.get(reverse("estandar:propuestas")).content.decode("utf-8")
        for texto in ("linea vieja", "linea nueva", "recuerdo viejo", "recuerdo nuevo"):
            self.assertIn(texto, pagina)


class SeApruebaConUnBoton(ConPropuestas):
    """CP-002."""

    def test_aprobar_cambia_el_texto_y_guarda_quien_y_cuando(self):
        for propuesta in (self.del_documento, self.del_recuerdo):
            self.client.post(reverse("estandar:aprobar", args=[propuesta.pk]))
            propuesta.refresh_from_db()
            self.assertEqual((propuesta.estado, propuesta.resuelta_por), (APROBADA, self.admin))
            self.assertIsNotNone(propuesta.resuelta)
        self.assertIn("linea nueva", Documento.objects.get(ruta="base/99-prueba.md").contenido)
        self.assertIn("recuerdo nuevo", Recuerdo.objects.get(nombre="memory.md").contenido)


class UnTipoNuevoSeSirveSolo(ConPropuestas):
    """CP-003: el tipo que se registre aplica sus propuestas sin tocar `cambios.py`."""

    def test_aprobar_le_pregunta_al_tipo(self):
        llamados = []

        class DePrueba(documentos.DeLaMemoria):
            nombre = "de-prueba"

            def aplicar(self, propuesta, raiz=None):
                llamados.append(propuesta.pk)

        original = documentos.TIPOS["recuerdo"]
        documentos.TIPOS["recuerdo"] = DePrueba()
        try:
            aplicar(self.del_recuerdo, None)
        finally:
            documentos.TIPOS["recuerdo"] = original
        self.assertEqual(llamados, [self.del_recuerdo.pk])
        self.assertEqual(Propuesta.objects.get(pk=self.del_recuerdo.pk).estado, APROBADA)
