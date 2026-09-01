# -*- coding: utf-8 -*-
"""Los casos del plan de pruebas de la fase `B-EP-013-HU-002`.

**El caso que decide es el CP-002:** que nada cambie fuera del hueco. Se compara
el archivo entero, carácter por carácter. Un guardado que reformatea obliga a
revisar el documento cada vez, y entonces conviene más abrir el editor.

**Y el que más protege es el CP-004:** que un cambio ajeno no se pise. Es la
primera pieza de la plataforma que escribe en el repositorio del usuario.
"""
import io
import os
import shutil
import tempfile

from django.test import TestCase, override_settings

from nucleo.importacion.models import Traido
from nucleo.proyectos.models import Proyecto
from . import core, escritura

LARGO = (u"# Un documento\n"
         u"\n"
         u"| Campo | Valor |\n"
         u"|---|---|\n"
         u"| **Responsable** | «…» |\n"
         u"| **Fecha** | 2026-09-01 |\n"
         u"\n"
         u"Un párrafo con **negrita** y `código`.\n"
         u"\n"
         u"Lo que sigue: «…»\n"
         u"\n"
         u"- una viñeta\n"
         u"- otra\n")


class Base(TestCase):

    def setUp(self):
        self.datos = tempfile.mkdtemp(prefix="prueba-escritura-datos-")
        self.proyecto = tempfile.mkdtemp(prefix="prueba-escritura-proy-")
        self.plantillas = tempfile.mkdtemp(prefix="prueba-escritura-moldes-")
        self.contexto = override_settings(CARPETA_DATOS=self.datos,
                                          CARPETA_PLANTILLAS=self.plantillas)
        self.contexto.enable()
        Proyecto.objects.create(identificador="de-prueba", nombre="De prueba",
                                ruta_codigo=self.proyecto,
                                ruta_normalizada=self.proyecto.lower(),
                                conectado="conectado")

    def tearDown(self):
        self.contexto.disable()
        for carpeta in (self.datos, self.proyecto, self.plantillas):
            shutil.rmtree(carpeta, ignore_errors=True)

    def documento(self, origen="documentacion/x.md", texto=LARGO,
                  tipo="índice", finales="\n"):
        """Un documento en el proyecto, con su copia en datos."""
        if finales != "\n":
            texto = texto.replace("\n", finales)
        real = os.path.join(self.proyecto, origen.replace("/", os.sep))
        os.makedirs(os.path.dirname(real), exist_ok=True)
        with io.open(real, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(texto)

        guardado = "proyectos/de-prueba/traido/" + origen
        copia = os.path.join(self.datos, guardado.replace("/", os.sep))
        os.makedirs(os.path.dirname(copia), exist_ok=True)
        with io.open(copia, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(texto)

        Traido.objects.create(proyecto="de-prueba", origen=origen, tipo=tipo,
                              guardado_en=guardado)
        return real

    def tal_cual(self, ruta):
        with io.open(ruta, encoding="utf-8", newline="") as archivo:
            return archivo.read()


class CP001QuedaEnElArchivo(Base):

    def test_lo_escrito_queda_en_el_archivo_del_proyecto(self):
        real = self.documento()
        core.llenar("de-prueba", "documentacion/x.md", 1, u"Ing. José")
        self.assertIn(u"| **Responsable** | Ing. José |", self.tal_cual(real))

    def test_se_escribe_en_el_original_y_no_solo_en_la_copia(self):
        """Escribir solo en la copia dejaría el proyecto igual."""
        real = self.documento()
        core.llenar("de-prueba", "documentacion/x.md", 1, u"quien sea")
        self.assertNotIn(u"«…»", self.tal_cual(real).split("\n")[4])

    def test_la_copia_queda_igual_que_el_original(self):
        """Si no, la cuenta seguiría mostrando el hueco que ya se llenó."""
        self.documento()
        core.llenar("de-prueba", "documentacion/x.md", 1, u"quien sea")
        copia = os.path.join(self.datos, "proyectos", "de-prueba", "traido",
                             "documentacion", "x.md")
        self.assertIn(u"quien sea", self.tal_cual(copia))

    def test_un_documento_que_no_esta_traido_devuelve_nada(self):
        self.assertIsNone(core.llenar("de-prueba", "no/existe.md", 1, u"x"))


class CP002NadaMasCambia(Base):
    """**El caso que decide la fase.**"""

    def test_solo_cambia_el_hueco_en_un_documento_con_tablas(self):
        real = self.documento()
        antes = self.tal_cual(real)
        core.llenar("de-prueba", "documentacion/x.md", 1, u"Ing. José")
        despues = self.tal_cual(real)
        self.assertEqual(antes.replace(u"«…»", u"Ing. José", 1), despues)

    def test_los_finales_de_linea_de_windows_no_se_traducen(self):
        """Traducirlos cambiaría **todos** los renglones sin que se vea."""
        real = self.documento(finales="\r\n")
        core.llenar("de-prueba", "documentacion/x.md", 1, u"Ing. José")
        despues = self.tal_cual(real)
        self.assertIn(u"\r\n", despues)
        self.assertNotIn(u"\n\n", despues.replace(u"\r\n", u"\r"))

    def test_el_ultimo_salto_de_linea_se_conserva(self):
        real = self.documento()
        core.llenar("de-prueba", "documentacion/x.md", 2, u"lo que va")
        self.assertTrue(self.tal_cual(real).endswith(u"- otra\n"))

    def test_llenar_el_segundo_no_corre_al_primero(self):
        real = self.documento()
        core.llenar("de-prueba", "documentacion/x.md", 2, u"lo segundo")
        texto = self.tal_cual(real)
        self.assertIn(u"| **Responsable** | «…» |", texto)
        self.assertIn(u"Lo que sigue: lo segundo", texto)


class CP003LaCuentaBaja(Base):

    def test_la_cuenta_baja_en_uno(self):
        self.documento()
        quedan = core.llenar("de-prueba", "documentacion/x.md", 1, u"algo")
        self.assertEqual(quedan["cuantos"], 1)

    def test_llenar_los_dos_deja_el_documento_completo(self):
        self.documento()
        core.llenar("de-prueba", "documentacion/x.md", 1, u"algo")
        quedan = core.llenar("de-prueba", "documentacion/x.md", 1, u"otra cosa")
        self.assertTrue(quedan["completo"])


class CP004ElCambioAjenoNoSePisa(Base):
    """Escribir encima de un cambio ajeno pierde trabajo de otro."""

    def test_si_el_archivo_cambio_por_fuera_no_se_escribe(self):
        real = self.documento()
        _, huella_de_antes, falta = core.huecos_del_original(
            "de-prueba", "documentacion/x.md")

        with io.open(real, "a", encoding="utf-8", newline="") as archivo:
            archivo.write(u"\nUna línea que escribió otro.\n")
        cambiado = self.tal_cual(real)

        with self.assertRaises(escritura.CambioAjeno):
            core.llenar("de-prueba", "documentacion/x.md", 1, u"algo",
                        huella_de_cuando_se_leyo=huella_de_antes)

        self.assertEqual(self.tal_cual(real), cambiado)
        self.assertIn(u"Una línea que escribió otro.", self.tal_cual(real))

    def test_sin_cambio_ajeno_la_huella_deja_escribir(self):
        self.documento()
        _, huella, _ = core.huecos_del_original("de-prueba",
                                                "documentacion/x.md")
        quedan = core.llenar("de-prueba", "documentacion/x.md", 1, u"algo",
                             huella_de_cuando_se_leyo=huella)
        self.assertEqual(quedan["cuantos"], 1)


class CP005QuedaRegistrado(Base):

    def test_llenar_deja_constancia_con_el_hueco_nombrado(self):
        from nucleo.auditoria.models import Registro
        self.documento()
        core.llenar("de-prueba", "documentacion/x.md", 1, u"algo",
                    quien="el usuario")
        ultima = Registro.objects.order_by("-id").first()
        self.assertIn("llenar un espacio", ultima.que_se_hizo)
        self.assertEqual(ultima.sobre_que, "documentacion/x.md")
        self.assertIn("linea 5", ultima.que_cambio)

    def test_un_intento_que_no_escribio_no_deja_constancia_de_un_cambio(self):
        from nucleo.auditoria.models import Registro
        self.documento()
        antes = Registro.objects.count()
        with self.assertRaises(ValueError):
            core.llenar("de-prueba", "documentacion/x.md", 99, u"algo")
        self.assertEqual(Registro.objects.count(), antes)


class CP006NoSeEscribeEnElHuecoEquivocado(Base):

    def test_una_linea_que_ya_no_dice_lo_mismo_no_se_escribe(self):
        hueco = {"linea": 1, "columna": 1, "marca": u"«…»",
                 "contexto": u"otra cosa"}
        with self.assertRaises(escritura.SeMovio):
            escritura.reemplazar(u"«…» acá\n", hueco, u"algo")

    def test_una_posicion_que_ya_no_tiene_la_marca_no_se_escribe(self):
        hueco = {"linea": 1, "columna": 9, "marca": u"«…»",
                 "contexto": u"«…» acá"}
        with self.assertRaises(escritura.SeMovio):
            escritura.reemplazar(u"«…» acá\n", hueco, u"algo")

    def test_una_linea_que_ya_no_existe_no_se_escribe(self):
        hueco = {"linea": 40, "columna": 1, "marca": u"«…»", "contexto": u"«…»"}
        with self.assertRaises(escritura.SeMovio):
            escritura.reemplazar(u"«…»\n", hueco, u"algo")

    def test_dos_marcas_iguales_en_la_misma_linea_no_se_confunden(self):
        texto = u"«…» y «…»\n"
        from . import huecos
        segundo = huecos.encontrar(texto)[1]
        self.assertEqual(escritura.reemplazar(texto, segundo, u"B"),
                         u"«…» y B\n")

    def test_llenar_con_nada_no_hace_nada(self):
        """Borrar la marca sin poner nada deja el documento peor."""
        hueco = {"linea": 1, "columna": 1, "marca": u"«…»", "contexto": u"«…»"}
        with self.assertRaises(ValueError):
            escritura.reemplazar(u"«…»\n", hueco, u"")

    def test_un_documento_sin_huecos_no_se_puede_llenar(self):
        self.documento(texto=u"# Todo escrito\n")
        with self.assertRaises(ValueError):
            core.llenar("de-prueba", "documentacion/x.md", 1, u"algo")


class ElGuardadoNoDejaElArchivoAMedias(Base):

    def test_se_escribe_al_lado_y_se_pone_en_su_sitio(self):
        ruta = os.path.join(self.proyecto, "y.md")
        with io.open(ruta, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(u"antes\n")
        escritura.guardar_de_un_golpe(ruta, u"después\n")
        self.assertEqual(self.tal_cual(ruta), u"después\n")

    def test_no_queda_el_archivo_de_al_lado(self):
        ruta = os.path.join(self.proyecto, "y.md")
        escritura.guardar_de_un_golpe(ruta, u"algo\n")
        sobrantes = [n for n in os.listdir(self.proyecto)
                     if n.endswith(".escribiendo")]
        self.assertEqual(sobrantes, [])
