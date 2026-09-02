# -*- coding: utf-8 -*-
"""Los casos del plan de pruebas de las fases `P` y `Q` de `EP-018`.

**El caso que decide es el CP-003:** que dar de baja no borre. Lo que se borra
no se puede volver a leer para entender por qué se creyó.

**Y el que más protege es el CP-002:** que corregir deje constancia de qué
decía antes. Un recuerdo que cambia sin dejar rastro no se distingue de uno que
siempre dijo eso.
"""
import io
import os
import shutil
import tempfile

from django.test import TestCase

from nucleo.proyectos.models import Proyecto
from . import core

UNO = u"""# Aprobar antes de commit

No se commitea sin que el usuario lo apruebe.
"""

OTRO = u"""# Español colombiano

Se escribe en tercera persona.
"""


class Base(TestCase):

    def setUp(self):
        self.carpeta = tempfile.mkdtemp(prefix="prueba-memoria-")
        Proyecto.objects.create(identificador="de-prueba", nombre="De prueba",
                                ruta_codigo=self.carpeta,
                                ruta_normalizada=self.carpeta.lower(),
                                conectado="conectado")
        self.escribir("aprobar-antes-de-commit.md", UNO)
        self.escribir("espanol-colombiano.md", OTRO)
        self.escribir(core.INDICE, u"# Memoria\n\nEl índice, que no es un recuerdo.\n")

    def tearDown(self):
        shutil.rmtree(self.carpeta, ignore_errors=True)

    def escribir(self, nombre, texto):
        completa = os.path.join(self.carpeta, core.CARPETA, nombre)
        os.makedirs(os.path.dirname(completa), exist_ok=True)
        with io.open(completa, "w", encoding="utf-8", newline="\n") as archivo:
            archivo.write(texto)

    def leer(self, nombre):
        with io.open(os.path.join(self.carpeta, core.CARPETA, nombre),
                     encoding="utf-8", newline="") as archivo:
            return archivo.read()


class CP001SeGuardaYSeRecupera(Base):

    def test_los_recuerdos_se_leen_con_su_titulo(self):
        recuerdos = core.todos("de-prueba")
        self.assertEqual(len(recuerdos), 2)
        self.assertEqual(recuerdos[0]["titulo"], "Aprobar antes de commit")

    def test_el_indice_no_es_un_recuerdo(self):
        nombres = [uno["nombre"] for uno in core.todos("de-prueba")]
        self.assertNotIn(core.INDICE, nombres)

    def test_se_guarda_uno_nuevo(self):
        core.guardar("de-prueba", "uno-nuevo", u"# Uno nuevo\n\nAlgo.\n")
        self.assertEqual(len(core.todos("de-prueba")), 3)

    def test_no_pisa_uno_que_ya_existe(self):
        """Para cambiarlo está corregir, que conserva lo anterior."""
        with self.assertRaises(core.NoHayMemoria):
            core.guardar("de-prueba", "espanol-colombiano.md", u"# Otra cosa\n")

    def test_un_proyecto_sin_memoria_lo_dice(self):
        shutil.rmtree(os.path.join(self.carpeta, core.CARPETA),
                      ignore_errors=True)
        with self.assertRaises(core.NoHayMemoria):
            core.todos("de-prueba")

    def test_se_busca_por_palabra(self):
        encontrados = core.buscar("de-prueba", "commit")
        self.assertEqual(len(encontrados), 1)
        self.assertEqual(encontrados[0]["nombre"], "aprobar-antes-de-commit.md")

    def test_una_palabra_que_no_esta_no_devuelve_nada(self):
        self.assertEqual(core.buscar("de-prueba", "arepa"), [])

    def test_lo_de_un_proyecto_no_se_mezcla_con_otro(self):
        """Cada proyecto tiene su carpeta."""
        otro = tempfile.mkdtemp(prefix="prueba-memoria-otro-")
        try:
            Proyecto.objects.create(
                identificador="otro", nombre="Otro", ruta_codigo=otro,
                ruta_normalizada=otro.lower(), conectado="conectado")
            os.makedirs(os.path.join(otro, core.CARPETA), exist_ok=True)
            self.assertEqual(core.todos("otro"), [])
            self.assertEqual(len(core.todos("de-prueba")), 2)
        finally:
            shutil.rmtree(otro, ignore_errors=True)


class CP002CorregirDejaConstancia(Base):
    """Un recuerdo que cambia sin rastro no se distingue de uno que siempre dijo eso."""

    def test_lo_anterior_se_conserva_debajo(self):
        core.corregir("de-prueba", "espanol-colombiano.md",
                      u"# Español colombiano\n\nY sin rayas largas.\n",
                      cuando="2026-09-01")
        texto = self.leer("espanol-colombiano.md")
        self.assertIn(u"Y sin rayas largas.", texto)
        self.assertIn(u"Se escribe en tercera persona.", texto)

    def test_y_dice_desde_cuando(self):
        core.corregir("de-prueba", "espanol-colombiano.md", u"# Otra cosa\n",
                      cuando="2026-09-01")
        self.assertIn(u"hasta el 2026-09-01",
                      self.leer("espanol-colombiano.md"))

    def test_corregir_uno_que_no_existe_lo_dice(self):
        with self.assertRaises(core.NoHayMemoria):
            core.corregir("de-prueba", "no-existe.md", u"# Algo\n")


class CP003DarDeBajaNoBorra(Base):
    """**El caso que decide.**"""

    def test_el_texto_se_conserva(self):
        core.dar_de_baja("de-prueba", "espanol-colombiano.md",
                         u"Ya no aplica.", cuando="2026-09-01")
        texto = self.leer("espanol-colombiano.md")
        self.assertIn(u"Se escribe en tercera persona.", texto)
        self.assertIn(u"Ya no vale", texto)

    def test_deja_de_entregarse_al_agente(self):
        core.dar_de_baja("de-prueba", "espanol-colombiano.md", u"Ya no aplica.")
        vigentes = [uno["nombre"] for uno in core.vigentes("de-prueba")]
        self.assertNotIn("espanol-colombiano.md", vigentes)

    def test_pero_sigue_estando(self):
        core.dar_de_baja("de-prueba", "espanol-colombiano.md", u"Ya no aplica.")
        self.assertEqual(len(core.todos("de-prueba")), 2)

    def test_y_no_sale_en_las_busquedas(self):
        core.dar_de_baja("de-prueba", "aprobar-antes-de-commit.md", u"Ya no.")
        self.assertEqual(core.buscar("de-prueba", "commit"), [])

    def test_uno_ya_dado_de_baja_lo_dice(self):
        core.dar_de_baja("de-prueba", "espanol-colombiano.md", u"Ya no.")
        with self.assertRaises(core.NoHayMemoria):
            core.dar_de_baja("de-prueba", "espanol-colombiano.md", u"Otra vez.")

    def test_el_resumen_cuenta_las_dos_clases(self):
        core.dar_de_baja("de-prueba", "espanol-colombiano.md", u"Ya no.")
        cuenta = core.resumen("de-prueba")
        self.assertEqual(cuenta["todos"], 2)
        self.assertEqual(cuenta["vigentes"], 1)
        self.assertEqual(cuenta["de_baja"], 1)
