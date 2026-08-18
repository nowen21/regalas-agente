# -*- coding: utf-8 -*-
"""Pendiente 46 · El registro de versión no dice que falta escribirse.

El apartado «Qué quedó pendiente» se calculaba **antes** de escribir el
archivo, así que el registro recién nacido se listaba a sí mismo como faltante:

    - **versiones** — lo instalado dice `21.2.1` y el último registro dice
      `20.0.1`: falta registrar la actualización

El registro que «falta» es el archivo que uno está leyendo. Era cierto un
instante antes de escribirse y falso desde entonces, y nadie lo volvía a tocar.
`dp` lo recibió así dos veces el mismo día: no es una condición de carrera, es
el orden en que estaba escrito.

No bloqueaba nada, y ese es el problema — «Qué quedó pendiente» es la única
parte del registro que el usuario tiene que leer y actuar. Si la primera vez
dice algo que no es, la segunda no la lee.
"""
import os
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import versiones   # noqa: E402


class LaFotoSeTomaAlFinal(unittest.TestCase):

    def _proyecto(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        return tmp.name

    def _registrar(self, proyecto, pendientes, version="1.0.0"):
        ruta = versiones.registrar(
            proyecto, version, {}, {"x": "huella"}, ["se aplicó algo"],
            pendientes=pendientes, anterior="0.9.0")
        with open(ruta, encoding="utf-8") as f:
            return ruta, f.read()

    def test_el_apartado_se_calcula_con_el_archivo_ya_escrito(self):
        """El caso del pendiente: al calcular los faltantes, el registro existe.

        Es lo único que hay que comprobar, y se comprueba desde dentro: la
        función que los calcula mira el disco y encuentra el archivo. Si se
        llamara antes, la carpeta estaría vacía.
        """
        proyecto = self._proyecto()
        visto = {}

        def faltantes():
            carpeta = versiones.carpeta_registros(proyecto)
            visto["archivos"] = (sorted(os.listdir(carpeta))
                                 if os.path.isdir(carpeta) else [])
            return []

        ruta, _texto = self._registrar(proyecto, faltantes)
        # En la carpeta están el registro y su índice; lo que importa es que el
        # registro ya estuviera cuando se preguntó qué falta.
        self.assertIn(os.path.basename(ruta), visto["archivos"],
                      "el apartado se calculó antes de escribir el registro")

    def test_lo_que_de_verdad_falta_si_se_escribe(self):
        """El arreglo no puede volverse una excusa para callar."""
        _ruta, texto = self._registrar(
            self._proyecto(), lambda: ["**algo** — que sí decide el usuario"])
        self.assertIn("Qué quedó pendiente", texto)
        self.assertIn("que sí decide el usuario", texto)

    def test_sin_faltantes_no_se_escribe_el_apartado(self):
        """Un apartado vacío invita a buscar lo que no hay."""
        _ruta, texto = self._registrar(self._proyecto(), lambda: [])
        self.assertNotIn("Qué quedó pendiente", texto)

    def test_la_lista_ya_calculada_sigue_valiendo(self):
        """Compatibilidad: quien pase una lista en vez de una función no se
        rompe. Se acepta, aunque pierda la gracia — una lista ya calculada da
        igual cuándo se use, porque la foto ya se tomó."""
        _ruta, texto = self._registrar(self._proyecto(), ["**x** — algo"])
        self.assertIn("Qué quedó pendiente", texto)

    def test_el_registro_queda_bien_formado_con_las_dos_escrituras(self):
        """Se escribe dos veces; la segunda no puede dejarlo a medias."""
        _ruta, texto = self._registrar(self._proyecto(), lambda: ["**x** — algo"])
        self.assertEqual(1, texto.count("# Actualización a 1.0.0"))
        self.assertEqual(1, texto.count("## Qué se aplicó"))
        self.assertEqual(1, texto.count("## Qué quedó pendiente"))
        self.assertEqual(1, texto.count("No se edita a mano"))
        self.assertLess(texto.index("## Qué quedó pendiente"),
                        texto.index("No se edita a mano"),
                        "el apartado quedó después del cierre del documento")

    def test_el_indice_queda_escrito_igual(self):
        proyecto = self._proyecto()
        self._registrar(proyecto, lambda: [])
        indice = os.path.join(versiones.carpeta_registros(proyecto), "README.md")
        self.assertTrue(os.path.isfile(indice), "el índice no se escribió")


if __name__ == "__main__":
    unittest.main()
