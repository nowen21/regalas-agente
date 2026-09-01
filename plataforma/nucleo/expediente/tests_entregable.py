# -*- coding: utf-8 -*-
"""Los casos del plan de pruebas de la fase `A-EP-012-HU-002`.

**El criterio que decide es el `CA-02`:** las listas dentro de una celda salen
como listas, sin marcas del texto de origen. En este repositorio casi toda tabla
las tiene, y es donde estos convertidores dejan la marca a la vista.

**Y el segundo es el `CA-03`:** generar dos veces da el mismo archivo. Por eso no
se escribe la fecha de generación adentro — una fecha haría distintos dos
archivos idénticos, y el criterio no se podría comprobar más que de palabra.
"""
import io
import os
import re
import shutil
import tempfile

from django.test import TestCase, override_settings

from nucleo.importacion.models import Traido
from nucleo.proyectos.models import Proyecto
from . import entregable, marcado


class ElMarcadoNoDejaMarcasALaVista(TestCase):
    """`CA-02` — lo difícil, y por eso va primero."""

    def test_una_lista_dentro_de_una_celda_sale_como_lista(self):
        salida = marcado.a_marcado(u"| A | B |\n|---|---|\n| uno · dos | x |")
        self.assertIn(u"<td><ul><li>uno</li><li>dos</li></ul></td>", salida)
        self.assertNotIn(u"·", salida)

    def test_una_celda_sin_lista_queda_como_texto(self):
        self.assertEqual(u"solo esto", marcado.celda(u"solo esto"))

    def test_el_separador_dentro_de_una_negrita_no_parte(self):
        """«1 · Ver lo que hay», en negrita, se partía en dos y dejaba los
        asteriscos a la vista: eran 174 en el entregable real."""
        self.assertEqual(u"<strong>1 · Ver lo que hay</strong>",
                         marcado.celda(u"**1 · Ver lo que hay**"))

    def test_una_tabla_dentro_de_una_cita_se_convierte(self):
        """Pegar la cita como prosa dejaba las barras a la vista: eran 31."""
        salida = marcado.a_marcado(u"> Lo que hay:\n>\n> | A |\n> |---|\n> | uno |")
        self.assertIn(u"<blockquote>", salida)
        self.assertIn(u"<table>", salida)
        self.assertNotIn(u"| A |", salida)

    def test_lo_que_va_entre_cercas_queda_tal_cual(self):
        salida = marcado.a_marcado(u"```\n| esto es un dibujo |\n```")
        self.assertIn(u"<pre><code>| esto es un dibujo |</code></pre>", salida)

    def test_el_marcado_de_afuera_se_escapa(self):
        """**Nunca se inventa una etiqueta.** Lo que venga en el texto se
        escapa: un convertidor que adivina produce algo que dice otra cosa."""
        self.assertIn(u"&lt;script&gt;", marcado.a_marcado(u"<script>malo</script>"))

    def test_los_encabezados_llevan_su_nivel(self):
        self.assertIn(u"<h3>Tres</h3>", marcado.a_marcado(u"### Tres"))

    def test_el_codigo_gana_sobre_la_negrita(self):
        salida = marcado.en_linea(u"`**esto no es negrita**`")
        self.assertIn(u"<code>**esto no es negrita**</code>", salida)


class Base(TestCase):

    def setUp(self):
        self.datos = tempfile.mkdtemp(prefix="prueba-entregable-")
        self.contexto = override_settings(CARPETA_DATOS=self.datos)
        self.contexto.enable()
        Proyecto.objects.create(identificador="de-prueba", nombre="De prueba",
                                ruta_codigo="/no/importa",
                                ruta_normalizada="/no/importa",
                                conectado="2026-01-02")

    def tearDown(self):
        self.contexto.disable()
        shutil.rmtree(self.datos, ignore_errors=True)

    def traer(self, origen, tipo, texto=u"# Un documento\n\nAlgo dicho.\n"):
        guardado = "proyectos/de-prueba/traido/" + origen
        completa = os.path.join(self.datos, guardado.replace("/", os.sep))
        os.makedirs(os.path.dirname(completa), exist_ok=True)
        with io.open(completa, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
        return Traido.objects.create(proyecto="de-prueba", origen=origen,
                                     tipo=tipo, guardado_en=guardado)

    def leer_entregable(self):
        ruta = os.path.join(self.datos,
                            entregable.nombre_del_archivo("de-prueba")
                            .replace("/", os.sep))
        with io.open(ruta, encoding="utf-8") as f:
            return f.read()


class ElEntregableTraeTodo(Base):
    """`CA-01` — todas las secciones, en el mismo orden."""

    def test_trae_cada_documento_del_expediente(self):
        self.traer("documentacion/epicas/EP-001-x/epica.md", "épica")
        self.traer("cvds/diseno/modelo-de-datos.md", "modelo de datos")
        entregable.generar("de-prueba")
        html = self.leer_entregable()
        self.assertEqual(2, html.count('class="documento"'))

    def test_el_orden_es_el_del_expediente(self):
        self.traer("documentacion/epicas/EP-001-x/epica.md", "épica")
        self.traer("cvds/diseno/modelo-de-datos.md", "modelo de datos")
        html = self.leer_entregable() if False else None
        entregable.generar("de-prueba")
        html = self.leer_entregable()
        self.assertLess(html.index(u"Diseño"), html.index(u"Épicas"))

    def test_trae_su_propia_tabla_de_contenido(self):
        self.traer("documentacion/epicas/EP-001-x/epica.md", "épica")
        entregable.generar("de-prueba")
        self.assertIn(u"<h2>Contenido</h2>", self.leer_entregable())

    def test_un_proyecto_sin_documentos_no_genera_nada(self):
        nombre, avisos = entregable.generar("de-prueba")
        self.assertEqual("", nombre)
        self.assertTrue(avisos)


class GenerarDosVecesDaLoMismo(Base):
    """`CA-03` — y por eso no se escribe la fecha adentro."""

    def test_dos_corridas_dan_el_mismo_archivo(self):
        self.traer("documentacion/epicas/EP-001-x/epica.md", "épica")
        entregable.generar("de-prueba")
        primera = self.leer_entregable()
        entregable.generar("de-prueba")
        self.assertEqual(primera, self.leer_entregable())

    def test_el_archivo_no_trae_la_fecha_de_generacion(self):
        """Una fecha haría distintos dos archivos idénticos, y entonces el
        criterio no se podría comprobar más que de palabra. Cuándo se generó
        vive en la auditoría, que es donde va esa pregunta."""
        self.traer("documentacion/epicas/EP-001-x/epica.md", "épica")
        entregable.generar("de-prueba")
        self.assertIsNone(re.search(r"\d{4}-\d{2}-\d{2}T", self.leer_entregable()))


class AvisaSinImpedir(Base):
    """`CA-04` — la decisión de entregar algo incompleto es del usuario."""

    def test_avisa_de_lo_que_falta(self):
        for tipo in ("plan de trabajo", "plan de pruebas"):
            self.traer("documentacion/epicas/EP-001-x/HU-001-y/"
                       "A-EP-001-HU-001-una/%s.md" % tipo.replace(" ", "_"), tipo)
        _nombre, avisos = entregable.generar("de-prueba")
        self.assertTrue(any(u"Faltan" in a for a in avisos))

    def test_avisa_de_lo_incompleto(self):
        self.traer("documentacion/epicas/EP-001-x/epica.md", "épica",
                   u"# Épica\n\n| Campo | «…» |\n")
        _nombre, avisos = entregable.generar("de-prueba")
        self.assertTrue(any(u"sin llenar" in a for a in avisos))

    def test_genera_igual(self):
        """**Avisa y no impide.** El programa informa; decide el usuario."""
        self.traer("documentacion/epicas/EP-001-x/epica.md", "épica",
                   u"# Épica\n\n| Campo | «…» |\n")
        nombre, _avisos = entregable.generar("de-prueba")
        self.assertTrue(nombre)
        self.assertIn(u"<h1>", self.leer_entregable())

    def test_lo_que_falta_va_dentro_del_archivo(self):
        """Quien lo recibe tiene que ver lo mismo que vio quien lo generó."""
        self.traer("documentacion/epicas/EP-001-x/epica.md", "épica",
                   u"# Épica\n\n| Campo | «…» |\n")
        entregable.generar("de-prueba")
        self.assertIn(u"Este expediente no está completo", self.leer_entregable())


class GenerarNoTocaLosDocumentos(Base):
    """El transversal: la fuente es el texto y no se toca."""

    def test_ningun_documento_traido_cambia(self):
        self.traer("documentacion/epicas/EP-001-x/epica.md", "épica")
        traido = os.path.join(self.datos, "proyectos", "de-prueba", "traido")

        def retrato():
            salida = {}
            for base, _d, nombres in os.walk(traido):
                for nombre in nombres:
                    con = os.path.join(base, nombre)
                    with io.open(con, encoding="utf-8") as f:
                        salida[con] = f.read()
            return salida

        antes = retrato()
        entregable.generar("de-prueba")
        self.assertEqual(antes, retrato())

    def test_el_archivo_no_sale_a_la_red(self):
        """Un entregable que necesita internet para verse bien no es un
        entregable: ni fuentes, ni hojas de estilo, ni guiones de afuera."""
        self.traer("documentacion/epicas/EP-001-x/epica.md", "épica")
        entregable.generar("de-prueba")
        html = self.leer_entregable()
        self.assertNotIn(u"http://", html.replace(u"http://www.w3.org", u""))
        self.assertNotIn(u"<script", html)
