"""`EP-029·HU-008` · Dañar el código a propósito: casos CP-001 a CP-006 del plan de pruebas."""
import io
import json
import os
import shutil
import sys
import tempfile
import unittest

from django.core.management import call_command
from django.core.management.base import CommandError

from .danar import DETECTADO, NO_DETECTADO, NO_SE_APLICO, SE_COLGO, Danar, Dano, correr_orden

SUMA = '''def suma(a, b):
    return a + b


def resta_sin_probar(a, b):
    return a - b
'''

PRUEBA = '''import unittest

import suma


class LaSuma(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma.suma(2, 3), 5)
'''

ORDEN = '"%s" -m unittest -q' % sys.executable


class ProyectoDeJuguete(unittest.TestCase):
    def setUp(self):
        self.raiz = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.raiz, True)
        self._escribir("suma.py", SUMA)
        self._escribir("test_suma.py", PRUEBA)

    def _escribir(self, nombre, texto):
        with open(os.path.join(self.raiz, nombre), "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)

    def _leer(self, nombre):
        with open(os.path.join(self.raiz, nombre), encoding="utf-8") as f:
            return f.read()

    def _correr(self, *danos, **opciones):
        return dict((d.nombre, r) for d, r in Danar(self.raiz, ORDEN, **opciones).correr(list(danos)))


class DiceQueDetectan(ProyectoDeJuguete):
    """CP-001 y CP-002."""

    def test_un_dano_detectado_y_otro_no(self):
        r = self._correr(Dano("la suma resta", "suma.py", "return a + b", "return a - b"),
                         Dano("la resta suma", "suma.py", "return a - b", "return a + b"))
        self.assertEqual(r["la suma resta"], DETECTADO)
        self.assertEqual(r["la resta suma"], NO_DETECTADO)
        self.assertEqual(self._leer("suma.py"), SUMA)

    def test_el_texto_que_no_aparece_o_aparece_dos_veces_no_se_aplica(self):
        r = self._correr(Dano("no está", "suma.py", "return a * b", "return 0"),
                         Dano("dos veces", "suma.py", "(a, b)", "(b, a)"),
                         Dano("sin archivo", "no_existe.py", "x", "y"))
        self.assertTrue(all(v.startswith(NO_SE_APLICO) for v in r.values()), r)
        self.assertEqual(self._leer("suma.py"), SUMA)

    def test_reconoce_el_texto_aunque_el_archivo_use_saltos_de_windows(self):
        with open(os.path.join(self.raiz, "suma.py"), "wb") as f:
            f.write(SUMA.replace("\n", "\r\n").encode("utf-8"))
        r = self._correr(Dano("dos líneas", "suma.py", "def suma(a, b):\n    return a + b",
                              "def suma(a, b):\n    return a - b"))
        self.assertEqual(r["dos líneas"], DETECTADO)


class QuedaComoEstaba(ProyectoDeJuguete):
    """CP-003, CP-004 y CP-005."""

    def test_borra_lo_que_el_dano_escribio(self):
        danar = Danar(self.raiz, ORDEN)
        danar.correr([Dano("deja rastro", "suma.py", "return a + b",
                           "open('rastro.txt', 'w').write('x')\n    return a + b")])
        self.assertFalse(os.path.exists(os.path.join(self.raiz, "rastro.txt")))
        self.assertIn("rastro.txt", danar.borrados)
        self.assertEqual(self._leer("suma.py"), SUMA)

    def test_el_dano_que_cuelga_las_pruebas_cuenta_como_detectado(self):
        r = self._correr(Dano("ciclo sin fin", "suma.py", "return a + b", "while True:\n        pass"), tiempo=5)
        self.assertEqual(r["ciclo sin fin"], SE_COLGO)
        self.assertEqual(self._leer("suma.py"), SUMA)

    def test_si_se_cae_con_el_dano_puesto_el_archivo_vuelve(self):
        llamadas = []

        def correr(orden, carpeta, tiempo):
            llamadas.append(1)
            if len(llamadas) == 2:          # la primera es sin daños; la segunda, con el daño puesto
                raise RuntimeError("se cayó")
            return correr_orden(orden, carpeta, tiempo)

        with self.assertRaises(RuntimeError):
            Danar(self.raiz, ORDEN, correr=correr).correr([Dano("x", "suma.py", "return a + b", "return 0")])
        self.assertEqual(self._leer("suma.py"), SUMA)


class SinPruebasQuePasenNoDana(ProyectoDeJuguete):
    """CP-006."""

    def test_no_toca_nada_si_las_pruebas_fallan_sin_danos(self):
        self._escribir("test_suma.py", PRUEBA.replace("5)", "6)"))
        salida = io.StringIO()
        danos = os.path.join(self.raiz, "..", os.path.basename(self.raiz) + "_danos.json")
        self.addCleanup(lambda: os.path.exists(danos) and os.remove(danos))
        with open(danos, "w", encoding="utf-8") as f:
            json.dump([{"nombre": "x", "archivo": "suma.py", "antes": "return a + b", "despues": "return 0"}], f)
        with self.assertRaisesRegex(CommandError, "primero hay que arreglarlas"):
            call_command("danar_a_proposito", danos=danos, pruebas=ORDEN, raiz=self.raiz, stdout=salida)
        self.assertEqual(self._leer("suma.py"), SUMA)


class ElComando(ProyectoDeJuguete):
    def test_escribe_la_tabla(self):
        danos = os.path.join(self.raiz, "..", os.path.basename(self.raiz) + "_danos.json")
        self.addCleanup(lambda: os.path.exists(danos) and os.remove(danos))
        with open(danos, "w", encoding="utf-8") as f:
            json.dump([{"nombre": "la suma resta", "archivo": "suma.py", "antes": "return a + b",
                        "despues": "return a - b"}], f)
        salida = io.StringIO()
        call_command("danar_a_proposito", danos=danos, pruebas=ORDEN, raiz=self.raiz, stdout=salida)
        self.assertIn("la suma resta  detectado", salida.getvalue())
        self.assertIn("1 daños, 0 sin detectar", salida.getvalue())
