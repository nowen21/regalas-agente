# -*- coding: utf-8 -*-
"""Los casos del plan de pruebas de la fase `C-EP-014-HU-001`.

**El caso que decide es el CP-003:** que lo importado no se altere. Tapar no se
deshace, y los 7 documentos que el tapador tocaría en este repositorio son los
que **documentan el tapador**: sus casos de prueba escritos.

**Y el que más protege es el CP-005:** sin enmascarador no se escribe. Devolver
el texto tal cual sería exactamente el daño que esto viene a evitar.
"""
import io
import os
import shutil
import tempfile

from django.test import TestCase, override_settings

from nucleo.importacion.models import Traido
from nucleo.proyectos.models import Proyecto
from . import claves, revision

CON_CLAVE = u'password: "inventada123"'
SIN_CLAVE = u"Un texto normal, con nombres de variable y nada más."


class ElTapadorTapa(TestCase):
    """Lo básico del puente. El reconocimiento vive en el estándar."""

    def test_una_clave_entre_comillas_queda_tapada(self):
        tapado, cuantas = claves.tapar(CON_CLAVE)
        self.assertEqual(cuantas, 1)
        self.assertNotIn(u"inventada123", tapado)

    def test_el_nombre_de_la_variable_queda_intacto(self):
        """Taparlo haría el documento ilegible sin proteger nada."""
        tapado, _ = claves.tapar(CON_CLAVE)
        self.assertIn(u"password", tapado)

    def test_una_clave_sin_comillas_tambien(self):
        tapado, cuantas = claves.tapar(u"API_KEY=inventada456")
        self.assertEqual(cuantas, 1)
        self.assertNotIn(u"inventada456", tapado)
        self.assertIn(u"API_KEY", tapado)

    def test_un_texto_limpio_sale_identico(self):
        """Tapar no puede cambiar lo que no era una clave."""
        tapado, cuantas = claves.tapar(SIN_CLAVE)
        self.assertEqual(cuantas, 0)
        self.assertEqual(tapado, SIN_CLAVE)

    def test_sin_enmascarador_revienta_en_vez_de_escribir(self):
        """`00·N6`: escribir sin tapar es el daño que esto viene a evitar."""
        with override_settings(CARPETA_VALIDADORES="/no/existe/en/ninguna/parte"):
            with self.assertRaises(claves.NoHayConQueTapar):
                claves.tapar(CON_CLAVE)


class LoQueParece(TestCase):
    """Contar sin tocar."""

    def test_dice_cuales_y_cuantas(self):
        encontrados = revision.parecen_traer_claves([
            (u"uno.md", CON_CLAVE),
            (u"dos.md", SIN_CLAVE),
            (u"tres.md", CON_CLAVE + u"\nAPI_KEY=inventada456"),
        ])
        self.assertEqual([n for n, _ in encontrados], [u"tres.md", u"uno.md"])
        self.assertEqual(encontrados[0][1], 2)

    def test_no_modifica_lo_que_revisa(self):
        original = CON_CLAVE
        revision.parecen_traer_claves([(u"uno.md", original)])
        self.assertEqual(original, CON_CLAVE)

    def test_un_proyecto_limpio_no_devuelve_nada(self):
        self.assertEqual(
            revision.parecen_traer_claves([(u"uno.md", SIN_CLAVE)]), [])


class AlLlenarSeTapa(TestCase):
    """El camino que teclea, que es el que esta fase agrega."""

    def setUp(self):
        self.datos = tempfile.mkdtemp(prefix="prueba-seg-datos-")
        self.proyecto = tempfile.mkdtemp(prefix="prueba-seg-proy-")
        self.contexto = override_settings(CARPETA_DATOS=self.datos)
        self.contexto.enable()
        Proyecto.objects.create(identificador="de-prueba", nombre="De prueba",
                                ruta_codigo=self.proyecto,
                                ruta_normalizada=self.proyecto.lower(),
                                conectado="conectado")
        self.real = os.path.join(self.proyecto, "x.md")
        for destino in (self.real,
                        os.path.join(self.datos, "proyectos", "de-prueba",
                                     "traido", "x.md")):
            os.makedirs(os.path.dirname(destino), exist_ok=True)
            with io.open(destino, "w", encoding="utf-8", newline="") as f:
                f.write(u"| Clave | «…» |\n")
        Traido.objects.create(proyecto="de-prueba", origen="x.md",
                              tipo="índice",
                              guardado_en="proyectos/de-prueba/traido/x.md")

    def tearDown(self):
        self.contexto.disable()
        for carpeta in (self.datos, self.proyecto):
            shutil.rmtree(carpeta, ignore_errors=True)

    def leer(self):
        with io.open(self.real, encoding="utf-8", newline="") as f:
            return f.read()

    def test_una_clave_tecleada_no_llega_al_archivo(self):
        from nucleo.ciclo_de_vida import core
        core.llenar("de-prueba", "x.md", 1, CON_CLAVE)
        self.assertNotIn(u"inventada123", self.leer())
        self.assertIn(u"password", self.leer())

    def test_se_dice_cuantas_se_taparon(self):
        """Tapar en silencio deja al usuario creyendo que escribió otra cosa."""
        from nucleo.ciclo_de_vida import core
        quedan = core.llenar("de-prueba", "x.md", 1, CON_CLAVE)
        self.assertEqual(quedan["tapadas"], 1)

    def test_un_texto_sin_clave_se_escribe_tal_cual(self):
        from nucleo.ciclo_de_vida import core
        quedan = core.llenar("de-prueba", "x.md", 1, u"Ing. José")
        self.assertEqual(quedan["tapadas"], 0)
        self.assertIn(u"Ing. José", self.leer())


class LoImportadoNoSeAltera(TestCase):
    """**El caso de «que NO pase».** Tapar no se deshace."""

    def setUp(self):
        self.datos = tempfile.mkdtemp(prefix="prueba-seg-import-")
        self.contexto = override_settings(CARPETA_DATOS=self.datos)
        self.contexto.enable()

    def tearDown(self):
        self.contexto.disable()
        shutil.rmtree(self.datos, ignore_errors=True)

    def test_un_documento_con_clave_de_ejemplo_se_guarda_tal_cual(self):
        guardado = "proyectos/de-prueba/traido/y.md"
        destino = os.path.join(self.datos, guardado.replace("/", os.sep))
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        con_ejemplo = (u"| 1 | Registrar con `%s` | La clave no aparece |\n"
                       % CON_CLAVE)
        with io.open(destino, "w", encoding="utf-8", newline="") as f:
            f.write(con_ejemplo)
        Traido.objects.create(proyecto="de-prueba", origen="y.md",
                              tipo="índice", guardado_en=guardado)

        from nucleo.ciclo_de_vida import core
        traido = Traido.objects.get(proyecto="de-prueba", origen="y.md")
        self.assertEqual(core._texto_de(traido), con_ejemplo)
        self.assertIn(u"inventada123", core._texto_de(traido))

    def test_revisar_lo_encuentra_sin_tocarlo(self):
        """Se cuenta y se nombra; la decisión queda donde corresponde."""
        con_ejemplo = u"Un ejemplo escrito: `%s`" % CON_CLAVE
        encontrados = revision.parecen_traer_claves([(u"y.md", con_ejemplo)])
        self.assertEqual(len(encontrados), 1)
        self.assertIn(u"inventada123", con_ejemplo)
