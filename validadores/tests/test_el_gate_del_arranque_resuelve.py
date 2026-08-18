# -*- coding: utf-8 -*-
"""Punto 5 del pendiente 33 · El `GATE` del arranque apunta a un archivo real.

`cargador.GATE` es la ruta de la regla que se muestra cuando el proyecto no
tiene su estructura base: es lo único que se carga en ese caso, y lo que
detiene el arranque.

**Renombrar un archivo lo dejó apuntando a una ruta que ya no existía, y
ninguna de las 191 pruebas de entonces lo detectó** — se descubrió a mano. La
puerta no se rompe con estrépito: `_solo_gate()` recorre las reglas
encontradas, no halla ninguna que coincida, devuelve cadena vacía y **la
puerta desaparece en silencio**. Un proyecto sin estructura arrancaría como si
la tuviera.

Es el defecto más barato de arreglar de toda esa lista y el más caro de dejar:
cuesta una prueba, y sin ella la puerta puede evaporarse en cualquier
renombre.
"""
import os
import sys
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import cargador   # noqa: E402

RAIZ = os.path.dirname(VALIDADORES)


class ElGateResuelveAUnArchivoQueExiste(unittest.TestCase):

    def test_el_archivo_del_gate_existe(self):
        ruta = os.path.join(RAIZ, "base", *cargador.GATE.split("/"))
        self.assertTrue(os.path.isfile(ruta),
                        f"`cargador.GATE` apunta a {cargador.GATE}, que no "
                        f"existe. La puerta del arranque desaparecería en "
                        f"silencio: sin coincidencia, `_solo_gate()` devuelve "
                        f"cadena vacía y el proyecto arranca como si tuviera "
                        f"su estructura.")

    def test_el_gate_es_la_regla_que_dice_ser(self):
        """No basta con que exista un archivo: tiene que ser `F13`.

        Un renombre que dejara la ruta apuntando a otra regla pasaría la
        prueba de arriba y seguiría estando mal — mostraría la orientación
        equivocada a quien no puede arrancar.
        """
        ruta = os.path.join(RAIZ, "base", *cargador.GATE.split("/"))
        with open(ruta, encoding="utf-8") as f:
            texto = f.read()
        self.assertIn("F13", texto[:400],
                      "el archivo del gate no es la regla F13")

    def test_la_puerta_de_verdad_devuelve_algo(self):
        """Por el camino real, no comprobando la constante.

        Es la diferencia que importa: la constante puede estar bien y el
        recorrido no encontrarla igual — que es exactamente cómo se rompió.
        """
        # Sin `skipTest`: saltarse la prueba porque la función cambió de
        # nombre es la misma desaparición silenciosa que esto persigue.
        base = os.path.join(RAIZ, "base")
        texto = cargador._solo_gate(base, list(cargador.reglas(base)))
        self.assertTrue(texto, "la puerta no devolvió nada: desapareció")
        self.assertIn("ARRANQUE DETENIDO", texto)


if __name__ == "__main__":
    unittest.main()
