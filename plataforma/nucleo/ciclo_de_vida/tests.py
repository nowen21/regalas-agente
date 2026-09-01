# -*- coding: utf-8 -*-
"""Los casos del plan de pruebas de la fase `A-EP-013-HU-001`.

**El caso que decide es el CP-003**: que un hueco con nombre no entre en la
cuenta. Se midió antes de construir sobre las 130 historias reales, y de 341
marcas ninguna era un hueco sin llenar. Una cuenta que las incluya da por
incompleto un documento bien escrito.

**Y dos son de lo que NO debe pasar:** que un tipo sin molde reciba el molde de
otro, y que mirar modifique un documento.
"""
import io
import os
import shutil
import tempfile

from django.test import TestCase, override_settings

from nucleo.importacion.models import Traido
from . import core, huecos, moldes

MOLDE_DE_MENTIRAS = u"""# «TITULO»

| Campo | Valor |
|---|---|
| **Responsable** | «RESPONSABLE» |
| **Fecha** | «AAAA-MM-DD» |

Lo que va acá: «…»

En «RUTA-ESTANDAR»/base/ viven las reglas.
"""


class Base(TestCase):

    def setUp(self):
        self.datos = tempfile.mkdtemp(prefix="prueba-ciclo-datos-")
        self.plantillas = tempfile.mkdtemp(prefix="prueba-ciclo-moldes-")
        self.contexto = override_settings(CARPETA_DATOS=self.datos,
                                          CARPETA_PLANTILLAS=self.plantillas)
        self.contexto.enable()

    def tearDown(self):
        self.contexto.disable()
        shutil.rmtree(self.datos, ignore_errors=True)
        shutil.rmtree(self.plantillas, ignore_errors=True)

    def molde(self, ruta, texto=MOLDE_DE_MENTIRAS):
        completa = os.path.join(self.plantillas, ruta.replace("/", os.sep))
        os.makedirs(os.path.dirname(completa), exist_ok=True)
        with io.open(completa, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)

    def traer(self, origen, tipo, texto=u"# Un documento\n"):
        guardado = "proyectos/de-prueba/traido/" + origen
        completa = os.path.join(self.datos, guardado.replace("/", os.sep))
        os.makedirs(os.path.dirname(completa), exist_ok=True)
        with io.open(completa, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
        return Traido.objects.create(proyecto="de-prueba", origen=origen,
                                     tipo=tipo, guardado_en=guardado)


class CP001SeDiceQueMoldeSigue(Base):
    """El molde sale del tipo, y los que no son directos también."""

    def test_los_tipos_del_ciclo_dan_su_molde(self):
        self.assertEqual(moldes.molde_de("plan de trabajo"),
                         "ciclo-vida-proyectos/07-plan-trabajo.md")
        self.assertEqual(moldes.molde_de("épica"),
                         "ciclo-vida-proyectos/03-epica.md")

    def test_los_tres_moldes_que_viven_fuera_de_la_carpeta_del_ciclo(self):
        """Son la razón de que la tabla se declare en vez de deducirse."""
        self.assertEqual(moldes.molde_de("señales"), "senales.md")
        self.assertEqual(moldes.molde_de("decisiones de arquitectura"),
                         "cvds/diseno/decisiones-de-arquitectura.md")
        self.assertEqual(
            moldes.molde_de("etapa del ciclo de vida", "cvds/diseno/README.md"),
            "cvds/diseno/README.md")

    def test_la_etapa_sale_de_donde_esta_y_no_de_su_nombre(self):
        """Todas se llaman `README.md`: el nombre no las distingue."""
        self.assertEqual(
            moldes.molde_de("etapa del ciclo de vida", "cvds/pruebas/README.md"),
            "cvds/pruebas/README.md")
        self.assertEqual(
            moldes.molde_de("etapa del ciclo de vida", "otra/parte/README.md"),
            "")

    def test_los_dos_tipos_sin_molde_dicen_por_que(self):
        for tipo in ("índice", "registro de versión"):
            self.assertEqual(moldes.molde_de(tipo), "")
            self.assertTrue(moldes.por_que_no_tiene_molde(tipo))

    def test_un_tipo_con_molde_no_declara_que_no_lo_tiene(self):
        self.assertEqual(moldes.por_que_no_tiene_molde("épica"), "")

    def test_el_documento_traido_dice_su_tipo_y_su_molde(self):
        self.molde("ciclo-vida-proyectos/07-plan-trabajo.md")
        self.traer("documentacion/x/plan_trabajo.md", "plan de trabajo")
        falta = core.que_le_falta("de-prueba",
                                  "documentacion/x/plan_trabajo.md")
        self.assertEqual(falta["tipo"], "plan de trabajo")
        self.assertEqual(falta["molde"],
                         "ciclo-vida-proyectos/07-plan-trabajo.md")

    def test_un_documento_que_no_esta_traido_devuelve_nada(self):
        self.assertIsNone(core.que_le_falta("de-prueba", "no/existe.md"))


class CP002SeListanLosHuecos(Base):
    """Cuántos son y dónde está cada uno."""

    def test_tres_huecos_dan_tres_con_su_linea(self):
        texto = u"uno «…»\ndos\ntres «…»\ncuatro «…»\n"
        falta = core.de_un_texto(texto, "índice")
        self.assertEqual(falta["cuantos"], 3)
        self.assertEqual([uno["linea"] for uno in falta["ciertos"]], [1, 3, 4])

    def test_dos_huecos_en_la_misma_linea_se_distinguen(self):
        falta = core.de_un_texto(u"«…» y también «…»\n", "índice")
        self.assertEqual(falta["cuantos"], 2)
        columnas = [uno["columna"] for uno in falta["ciertos"]]
        self.assertEqual(len(set(columnas)), 2)

    def test_cada_hueco_trae_el_texto_que_lo_rodea(self):
        """La `HU-002` va a escribir ahí, y la línea sola no dice si se movió."""
        falta = core.de_un_texto(u"| **Responsable** | «…» |\n", "índice")
        self.assertIn("Responsable", falta["ciertos"][0]["contexto"])

    def test_una_marca_dentro_de_un_bloque_cercado_no_se_cuenta(self):
        """Ahí se escribe para que se vea, no para llenarla."""
        texto = u"antes «…»\n```\nejemplo «…»\n```\ndespués\n"
        falta = core.de_un_texto(texto, "índice")
        self.assertEqual(falta["cuantos"], 1)
        self.assertEqual(falta["ciertos"][0]["linea"], 1)

    def test_un_documento_sin_huecos_lo_dice(self):
        falta = core.de_un_texto(u"# Todo escrito\n", "índice")
        self.assertTrue(falta["completo"])
        self.assertEqual(falta["cuantos"], 0)


class CP002Lista(Base):
    """La lista de todo un proyecto."""

    def test_va_del_que_mas_le_falta_al_que_menos(self):
        self.traer("a.md", "índice", u"«…»\n")
        self.traer("b.md", "índice", u"«…»\n«…»\n«…»\n")
        self.traer("c.md", "índice", u"nada\n")
        lista = core.de_un_proyecto("de-prueba")
        self.assertEqual([uno["origen"] for uno in lista], ["b.md", "a.md"])
        self.assertEqual([uno["cuantos"] for uno in lista], [3, 1])

    def test_los_completos_no_salen(self):
        """La lista es de trabajo por hacer, y un documento completo no lo es."""
        self.traer("c.md", "índice", u"nada\n")
        self.assertEqual(core.de_un_proyecto("de-prueba"), [])


class CP003SoloElCiertoCuenta(Base):
    """**El caso que la medición cambió.**"""

    def test_el_hueco_con_nombre_no_entra_en_la_cuenta(self):
        self.molde("ciclo-vida-proyectos/04-HU.md")
        texto = u"| **Responsable** | «RESPONSABLE» |\nLo que va acá: «…»\n"
        falta = core.de_un_texto(texto, "historia de usuario",
                                 "documentacion/x/HU-001-y.md")
        self.assertEqual(falta["cuantos"], 1)
        self.assertEqual(len(falta["posibles"]), 1)
        self.assertEqual(falta["posibles"][0]["marca"], u"«RESPONSABLE»")

    def test_una_cita_del_autor_ni_se_cuenta_ni_se_lista(self):
        """No está en el molde, así que no es ni siquiera un posible."""
        self.molde("ciclo-vida-proyectos/04-HU.md")
        falta = core.de_un_texto(u"El usuario dijo «hágale» y se hizo.\n",
                                 "historia de usuario",
                                 "documentacion/x/HU-001-y.md")
        self.assertEqual(falta["cuantos"], 0)
        self.assertEqual(falta["posibles"], [])

    def test_sin_molde_no_hay_posibles_pero_los_ciertos_siguen(self):
        """Un tipo sin molde igual se puede contar: `«…»` no necesita molde."""
        falta = core.de_un_texto(u"«…» y «CUALQUIER COSA»\n", "índice")
        self.assertEqual(falta["cuantos"], 1)
        self.assertEqual(falta["posibles"], [])


class CP004LoDeLaInstalacionNoSePregunta(Base):
    """134 preguntas que el usuario no responde."""

    def test_la_marca_de_instalacion_no_entra_en_la_cuenta(self):
        falta = core.de_un_texto(u"«RUTA-ESTANDAR»/base/ y un «…»\n", "índice")
        self.assertEqual(falta["cuantos"], 1)

    def test_pero_tampoco_desaparece_en_silencio(self):
        """Borrarla de la cuenta sin decirlo es perder en silencio."""
        falta = core.de_un_texto(u"«RUTA-ESTANDAR»/base/ y un «…»\n", "índice")
        self.assertEqual(len(falta["instalacion"]), 1)
        self.assertEqual(falta["instalacion"][0]["marca"], u"«RUTA-ESTANDAR»")

    def test_dos_de_instalacion_y_ningun_hueco_dan_documento_completo(self):
        falta = core.de_un_texto(u"«RUTA-ESTANDAR»\n«RUTA-ESTANDAR»\n", "índice")
        self.assertTrue(falta["completo"])
        self.assertEqual(len(falta["instalacion"]), 2)


class CP005ElTipoDesconocidoLoDice(Base):

    def test_sin_tipo_se_dice_y_no_se_le_atribuye_molde(self):
        falta = core.de_un_texto(u"«…»\n", "")
        self.assertTrue(falta["sin_tipo"])
        self.assertEqual(falta["molde"], "")

    def test_un_tipo_inventado_no_recibe_el_molde_de_otro(self):
        self.assertEqual(moldes.molde_de("cualquier cosa"), "")


class CP006MirarNoModifica(Base):

    def test_pedir_que_falta_no_toca_el_archivo(self):
        traido = self.traer("x.md", "índice", u"«…»\n")
        ruta = os.path.join(self.datos, traido.guardado_en.replace("/", os.sep))
        antes = (io.open(ruta, encoding="utf-8").read(), os.path.getmtime(ruta))
        core.que_le_falta("de-prueba", "x.md")
        despues = (io.open(ruta, encoding="utf-8").read(),
                   os.path.getmtime(ruta))
        self.assertEqual(antes, despues)


class LaMarcaSeBusca(TestCase):
    """Los bordes de la búsqueda, sin base de datos."""

    def test_una_marca_partida_entre_dos_lineas_no_es_una_marca(self):
        self.assertEqual(huecos.encontrar(u"«\n…»\n"), [])

    def test_dos_comillas_lejanas_de_un_parrafo_no_son_una_marca(self):
        largo = u"«" + (u"x" * 200) + u"»"
        self.assertEqual(huecos.encontrar(largo), [])

    def test_las_marcas_del_molde_se_leen_del_molde(self):
        del_molde = huecos.marcas_del_molde(MOLDE_DE_MENTIRAS)
        self.assertIn(u"«RESPONSABLE»", del_molde)
        self.assertIn(u"«…»", del_molde)
