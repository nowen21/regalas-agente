# -*- coding: utf-8 -*-
"""`EP-004·HU-025` · Un carácter que no se ve y rompe la tabla se cuenta.

**El caso que lo hizo falta.** Al ir a agregarle una fila a la tabla de fases de
una historia, la fila que ya estaba **empezaba con un `U+0001`** en vez de con
la barra de la tabla. Esa fila no se renderiza como fila: desaparece del cuadro
y queda como un párrafo suelto debajo. Estaba en 26 archivos, y ningún programa
lo contaba.

Lo que estas pruebas fijan: que se cuente **todo el rango** y no los que
aparecieron, que la limpieza los quite sin tocar el texto visible, y que lo que
sí significa algo dentro de un texto no se toque.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import marcas          # noqa: E402


class LosCaracteresDeControlSeCuentan(unittest.TestCase):

    def test_el_que_rompio_la_tabla_se_cuenta(self):
        linea = chr(0x01) + "| A-EP-001-HU-001 | CA-01 | Terminada |"
        halladas = marcas.marcas_de_linea(linea)
        self.assertTrue(halladas, "el carácter que rompe la fila no se contó")
        self.assertIn("control", halladas[0][1])

    def test_se_cuenta_el_rango_y_no_solo_el_que_aparecio(self):
        """**La decisión que esta prueba fija.** Agregar de a uno los que van
        apareciendo deja el trabajo a medias por definición: el próximo se cuela
        igual. Se barre el rango completo."""
        for codigo in (0x00, 0x07, 0x1B, 0x1F, 0x7F):
            with self.subTest(codigo=codigo):
                self.assertTrue(marcas.marcas_de_linea("a" + chr(codigo) + "b"),
                                "no se cuenta U+%04X" % codigo)

    def test_lo_que_si_significa_algo_no_se_toca(self):
        """El tabulador, el salto de línea y el retorno son parte de cómo se
        escribe un texto. Contarlos convertiría la comprobación en ruido."""
        for codigo in (0x09, 0x0A, 0x0D):
            with self.subTest(codigo=codigo):
                self.assertEqual([], marcas.marcas_de_linea("a" + chr(codigo) + "b"),
                                 "se cuenta U+%04X, y no debía" % codigo)

    def test_la_limpieza_lo_quita_y_no_cambia_el_texto_visible(self):
        antes = "| Fase | Estado |\n|---|---|\n" + chr(0x01) + "| A | Terminada |\n"
        nuevo, cuantos = marcas.limpiar_texto(antes)
        self.assertEqual(1, cuantos)
        self.assertNotIn(chr(0x01), nuevo)
        self.assertEqual(antes.replace(chr(0x01), ""), nuevo,
                         "la limpieza cambió algo más que el carácter invisible")

    def test_el_arbol_de_este_repositorio_no_tiene_ninguno(self):
        """La comprobación que cierra la historia: después de limpiar, cero.

        Se mira lo que el propio contador recorre, que excluye el histórico
        —una transcripción no se reescribe— y los datos de la plataforma, que
        son una copia traída."""
        raiz = os.path.dirname(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))))
        _por_marca, _por_archivo, nombres = marcas.contar(raiz)
        control = [n for n in nombres.values() if "control" in n]
        self.assertEqual([], control,
                         "quedaron caracteres de control: %s" % control)


if __name__ == "__main__":
    unittest.main(verbosity=2)
