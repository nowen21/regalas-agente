# -*- coding: utf-8 -*-
"""`EP-005 · HU-021` fase B — la otra batería de este repositorio también se corre.

**El caso está medido, y costó un día.** El 2026-08-31 la subida de versión de la
mañana puso en rojo dos de las 187 pruebas de la plataforma. `validar.py internas`
no las mira, así que el rojo estuvo puesto toda la jornada y se supo por la tarde,
por casualidad, al abrir una fase que tocaba esa carpeta. Es `S-097`.

**Lo que estas pruebas fijan no es que corra: es que no pueda callarse.** Cero
pruebas es rojo, una batería que falla es rojo, y **no tener plataforma se dice**
en vez de saltarse en silencio. Un proyecto que hereda el estándar no tiene
plataforma, y ahí el silencio sería lo mismo que no mirar.
"""
import io
import os
import shutil
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import corredor                     # noqa: E402
from comun import AVISO, FALLA      # noqa: E402

SALTO = chr(10)

# Una prueba de mentiras que pasa, para armar un repositorio chico.
UNA_PRUEBA = SALTO.join([
    "import unittest", "", "",
    "class Una(unittest.TestCase):",
    "    def test_pasa(self):",
    "        self.assertTrue(True)", ""])


class Base(unittest.TestCase):

    def repo(self, con_plataforma=True):
        """Un repositorio de mentiras, con o sin plataforma."""
        raiz = tempfile.mkdtemp(prefix="prueba-corredor-")
        self.addCleanup(shutil.rmtree, raiz, True)
        if con_plataforma:
            carpeta = os.path.join(raiz, corredor.PLATAFORMA)
            os.makedirs(carpeta)
            with io.open(os.path.join(carpeta, "manage.py"), "w",
                         encoding="utf-8", newline=SALTO) as f:
                f.write(u"# un punto de entrada de mentiras" + SALTO)
        return raiz

    def repo_con_una_prueba(self):
        """Un repositorio con una sola prueba propia y sin plataforma."""
        raiz = self.repo(False)
        carpeta = os.path.join(raiz, "validadores", "tests")
        os.makedirs(carpeta)
        with io.open(os.path.join(carpeta, "test_una.py"), "w",
                     encoding="utf-8", newline=SALTO) as f:
            f.write(UNA_PRUEBA)
        return raiz


class SinPlataformaSeDice(Base):
    """El caso del proyecto que hereda: no tiene, y eso no es estar en verde."""

    def test_sin_plataforma_avisa(self):
        hallazgos, cuantas = corredor.correr_la_plataforma(self.repo(False))
        self.assertEqual(0, cuantas)
        self.assertEqual(1, len(hallazgos))
        self.assertEqual(AVISO, hallazgos[0].severidad)

    def test_el_aviso_dice_que_no_es_lo_mismo_que_estar_bien(self):
        hallazgos, _c = corredor.correr_la_plataforma(self.repo(False))
        self.assertIn("No es lo mismo que estar en verde", hallazgos[0].mensaje)

    def test_no_avisa_como_falla(self):
        """**No tener plataforma no es un defecto.** Si fuera falla, todo
        proyecto que hereda el estándar tendría un rojo permanente, y un rojo
        que siempre está se apaga."""
        hallazgos, _c = corredor.correr_la_plataforma(self.repo(False))
        self.assertEqual([], [h for h in hallazgos if h.severidad == FALLA])


class LaCorridaQueNoCorreNadaEsRoja(Base):
    """La misma regla que ya rige para la otra batería."""

    def test_cero_pruebas_es_falla(self):
        """El punto de entrada de mentiras no corre nada: eso es rojo."""
        hallazgos, cuantas = corredor.correr_la_plataforma(self.repo())
        self.assertEqual(0, cuantas)
        self.assertEqual([FALLA], [h.severidad for h in hallazgos])

    def test_el_mensaje_dice_que_cero_no_es_verde(self):
        hallazgos, _c = corredor.correr_la_plataforma(self.repo())
        self.assertIn("cero no es verde", hallazgos[0].mensaje)


class LasDosBateriasSeCuentanAparte(Base):
    """Sumarlas en un solo número escondería cuál de las dos se cayó.

    **Se arma un repositorio chico, y no se corre el de verdad.** Llamar acá a
    la corrida completa la metería dentro de una de sus propias pruebas: las 724
    corriendo dentro de la 725. Se vio al escribir esta clase, y por eso queda
    dicho.
    """

    def _resumen(self, hallazgos):
        lineas = [h for h in hallazgos if h.severidad == AVISO
                  and "prueba(s) en" in h.mensaje]
        self.assertEqual(1, len(lineas))
        return lineas[0].mensaje

    def test_el_resumen_nombra_las_dos(self):
        raiz = self.repo_con_una_prueba()
        self.assertIn("de la plataforma", self._resumen(corredor.validar(raiz)))

    def test_las_dos_cifras_van_separadas(self):
        raiz = self.repo_con_una_prueba()
        resumen = self._resumen(corredor.validar(raiz))
        self.assertIn("1 prueba(s) en 1 archivo(s)", resumen)
        self.assertIn("0 prueba(s) de la plataforma", resumen)

    def test_pedir_un_subconjunto_no_arrastra_la_otra_bateria(self):
        """`02·F5`: una fase corre lo que toca. Arrastrar 187 pruebas ajenas
        volvería esa orden un peaje, y un peaje se apaga."""
        raiz = self.repo_con_una_prueba()
        resumen = self._resumen(corredor.validar(raiz, solo=["test_una.py"]))
        self.assertNotIn("de la plataforma", resumen)


class SobreLaPlataformaDeVerdad(unittest.TestCase):
    """Contra la que hay, no contra una inventada.

    **Tarda medio minuto**, porque corre las 187 de verdad. Es el precio de no
    dar por buena una integración mirando solo repositorios de mentiras.
    """

    def test_corre_las_pruebas_que_hay_y_las_dice(self):
        hallazgos, cuantas = corredor.correr_la_plataforma()
        if cuantas == 0 and hallazgos and hallazgos[0].severidad == AVISO:
            self.skipTest("este repositorio no tiene plataforma")
        self.assertGreater(cuantas, 100)
        self.assertEqual([], [h for h in hallazgos if h.severidad == FALLA])


if __name__ == "__main__":
    unittest.main(verbosity=2)
