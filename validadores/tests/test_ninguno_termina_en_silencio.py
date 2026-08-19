# -*- coding: utf-8 -*-
"""Pendiente 53 · Ningún validador termina en silencio con código 0.

Un módulo de comprobación que se ejecuta solo, no imprime nada y sale con 0
dice —con su silencio— exactamente lo mismo que diría si hubiera mirado todo y
estuviera en orden. Es la peor mentira que puede decir un validador: **afirma
sin haber comprobado**.

Ya costó una métrica falsa. El 2026-08-16 la fase `B-EP-005-HU-008` corrió
`enlaces.py` a mano, no vio salida y escribió «cero enlaces rotos» en su
resultado de pruebas. El entrypoint real reportaba veinte.

Esta prueba recorre **todos** los `.py` de `validadores/` y exige de cada uno
una de dos cosas: que haga algo, o que diga por dónde se corre. La lista no se
escribe a mano: se lee del disco, así que el programa número treinta y siete
entra solo.
"""
import os
import subprocess
import sys
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Los que sí son puntos de entrada: se corren solos a propósito.
#
# `citas.py` está acá y no es un descuido: no es un validador sino el
# **reparador** que enlaza las citas sueltas. Corriéndolo sin argumentos
# simula y dice qué haría, que es justo lo contrario de callar. Su mitad de
# comprobación sí vive dentro de `validar.py estandar`.
#
# `cerrar.py` está por lo mismo: es la herramienta que mueve un pendiente a
# `hecho/` arrastrando sus citas. Sin argumentos, `argparse` explica qué le
# falta y sale con 2 — dice algo, que es lo que esta prueba exige.
#
# `marcas.py` también: su trabajo principal es **el recuento** del pendiente
# 11 —cuántas marcas hay y dónde—, y eso no cabe en un hallazgo por línea.
# Corriéndolo solo imprime el reparto entero. Su mitad de comprobación, la de
# lo que se hereda, sí vive dentro de `validar.py marcas`.
# Los que **se corren solos a propósito**: no comprueban, hacen algo que se
# pide. `validar.py` es la puerta de lo que comprueba; estos escriben.
CON_ARRANQUE_PROPIO = {"validar.py", "pruebas.py", "instalar.py", "historico.py",
                       "comun.py", "citas.py", "cerrar.py", "marcas.py",
                       "andamio.py", "respaldo.py"}


def modulos():
    """Los `.py` de `validadores/` que no son entrada ni enganche."""
    for nombre in sorted(os.listdir(VALIDADORES)):
        if not nombre.endswith(".py") or nombre.startswith("__"):
            continue
        if nombre in CON_ARRANQUE_PROPIO or nombre.startswith("hook_"):
            continue
        yield nombre


def correr(nombre):
    """Ejecuta el módulo solo, como lo haría alguien en una terminal."""
    return subprocess.run(
        [sys.executable, os.path.join(VALIDADORES, nombre)],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
        timeout=60)


class NingunoTerminaEnSilencio(unittest.TestCase):

    def test_hay_modulos_que_revisar(self):
        """Si la lista queda vacía, la prueba pasaría sin comprobar nada — que
        es el mismo defecto que esta prueba persigue."""
        self.assertGreaterEqual(len(list(modulos())), 20,
                                "la lista de módulos salió vacía o muy corta")

    def test_ninguno_sale_con_cero_sin_decir_nada(self):
        mudos = []
        for nombre in modulos():
            r = correr(nombre)
            if r.returncode == 0 and not (r.stdout.strip() or r.stderr.strip()):
                mudos.append(nombre)
        self.assertEqual([], mudos,
                         "estos salen con 0 sin imprimir nada, y ese silencio "
                         "se lee como «no hay hallazgos»: " + ", ".join(mudos))

    def test_el_que_no_es_entrada_dice_por_donde_se_corre(self):
        sin_indicacion = []
        for nombre in modulos():
            r = correr(nombre)
            salida = (r.stdout + r.stderr).lower()
            if "validar.py" not in salida:
                sin_indicacion.append("%s (código %d)" % (nombre, r.returncode))
        self.assertEqual([], sin_indicacion,
                         "estos no dicen por dónde se corren: "
                         + ", ".join(sin_indicacion))

    def test_el_codigo_de_salida_distingue_no_comprobe_de_hay_fallas(self):
        """Sale con **2**, no con 0 ni con 1.

        Un guion que llame al módulo por error tiene que poder distinguir «no
        comprobé nada» de «comprobé y hay fallas». Con 1 los dos casos se
        confunden, y el que no comprobó nada se leería como que encontró algo.
        """
        malos = []
        for nombre in modulos():
            r = correr(nombre)
            if r.returncode != 2:
                malos.append("%s (código %d)" % (nombre, r.returncode))
        self.assertEqual([], malos,
                         "estos no salen con código 2: " + ", ".join(malos))

    def test_los_dos_casos_del_pendiente(self):
        """`enlaces.py` y `metareglas.py`, que son los que lo destaparon."""
        for nombre, subcomando in (("enlaces.py", "estandar"),
                                   ("metareglas.py", "metareglas")):
            with self.subTest(modulo=nombre):
                r = correr(nombre)
                salida = r.stdout + r.stderr
                self.assertEqual(2, r.returncode)
                self.assertIn("no comprueba nada", salida)
                self.assertIn("validar.py " + subcomando, salida)


class MetareglasSeCorreDesdeLaEntrada(unittest.TestCase):
    """El punto 2 del pendiente 53: era el único programa que comprueba once de
    las veinte filas del checklist del estándar, y no tenía por dónde correrse.

    Entre esas once están la fila 5 —que `M3` necesita— y la 15, que impide que
    una regla normal mande sobre una `[BLINDADA]`.
    """

    def test_el_subcomando_existe_y_comprueba_algo(self):
        r = subprocess.run(
            [sys.executable, os.path.join(VALIDADORES, "validar.py"), "metareglas"],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
            timeout=180)
        self.assertIn("meta-reglas", (r.stdout + r.stderr).lower())
        # Da hallazgos: el capítulo 20 no se cumple a sí mismo — pendiente 19.
        # Lo que importa acá no es cuántos, sino que la corrida diga algo.
        self.assertTrue(r.stdout.strip(), "la corrida no imprimió nada")


if __name__ == "__main__":
    unittest.main()
