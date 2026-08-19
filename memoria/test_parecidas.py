# -*- coding: utf-8 -*-
"""`09·16` · Marcar pares de señales parecidas, sin prometer más de lo que se puede.

**Una memoria con dos señales opuestas activas es peor que una vacía:** da
respuestas seguras y contradictorias según cuál se encuentre primero.

**Se llama «parecidas», no «contradicciones», y es la decisión de diseño.**
Decidir si dos señales se oponen o se complementan es criterio, no cálculo — un
aviso que promete de más se termina apagando.
"""
import os
import sqlite3
import sys
import tempfile
import unittest

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import parecidas    # noqa: E402


def base(*senales):
    """Una memoria de mentira. `(id, tipo, scope, titulo, why, estado)`."""
    tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
    tmp.close()
    con = sqlite3.connect(tmp.name)
    con.execute("CREATE TABLE senales (id TEXT, tipo TEXT, titulo TEXT, why TEXT, "
                "scope TEXT, estado TEXT)")
    for s in senales:
        con.execute("INSERT INTO senales (id,tipo,scope,titulo,why,estado) "
                    "VALUES (?,?,?,?,?,?)", s)
    con.commit()
    return tmp.name, con


class SoloMiraLoQuePuedeChocar(unittest.TestCase):

    def test_solo_las_activas(self):
        _f, con = base(("S-1", "decision", "org", "a", "porque sí", "activa"),
                       ("S-2", "decision", "org", "b", "porque no", "reemplazada"))
        self.addCleanup(con.close)
        self.assertEqual(1, len(parecidas.activas(con)))

    def test_solo_los_tipos_que_deciden(self):
        """**Un `gotcha` repetido es ruido, no una trampa.**"""
        _f, con = base(("S-1", "gotcha", "org", "a", "x", "activa"),
                       ("S-2", "gotcha", "org", "b", "x", "activa"))
        self.addCleanup(con.close)
        self.assertEqual([], parecidas.activas(con))

    def test_los_cuatro_tipos_que_deciden_estan(self):
        for t in ("decision", "patron", "restriccion", "supuesto"):
            self.assertIn(t, parecidas.TIPOS_QUE_DECIDEN)

    def test_con_una_sola_no_hay_par(self):
        _f, con = base(("S-1", "decision", "org", "a", "x", "activa"))
        self.addCleanup(con.close)
        self.assertEqual([], parecidas.pares(con))


class DistintoAlcanceNoEsChoque(unittest.TestCase):
    """**El proyecto ajusta a la organización**: que digan cosas distintas es
    como está diseñado el alcance, no un defecto."""

    def test_org_y_proyecto_no_se_comparan(self):
        _f, con = base(
            ("S-1", "decision", "organizacion", "a", "el mismo porqué exacto", "activa"),
            ("S-2", "decision", "proyecto:x", "b", "el mismo porqué exacto", "activa"))
        self.addCleanup(con.close)
        self.assertEqual([], parecidas.pares(con, umbral=0.1))

    def test_distinto_tipo_tampoco(self):
        _f, con = base(
            ("S-1", "decision", "org", "a", "el mismo porqué exacto", "activa"),
            ("S-2", "patron", "org", "b", "el mismo porqué exacto", "activa"))
        self.addCleanup(con.close)
        self.assertEqual([], parecidas.pares(con, umbral=0.1))


class SinSemanticaNoAdivina(unittest.TestCase):
    """**Comparar por palabras sueltas daría pares por casualidad**, y un par
    por casualidad enseña a ignorar la lista entera."""

    def test_lo_dice_en_vez_de_callarse(self):
        import semantica
        if semantica.disponible():
            self.skipTest("el módulo semántico está disponible")
        _f, con = base(("S-1", "decision", "org", "a", "x", "activa"))
        self.addCleanup(con.close)
        self.assertIn("no se revisó nada", parecidas.informe())


class ElInforme(unittest.TestCase):

    def test_sin_base_lo_dice(self):
        self.assertIn("no hay memoria", parecidas.informe("/no/existe.db"))

    def test_no_promete_que_se_contradigan(self):
        """**Es el nombre lo que evita el daño.** Decir «contradicción» haría
        que quien lo lea confíe en un juicio que el programa no hizo."""
        texto = parecidas.informe()
        self.assertNotIn("contradicen (", texto)

    def test_el_umbral_es_el_medido(self):
        """0.86 daba seis pares que había que descartar a mano, y descartar seis
        enseña a no mirar la lista."""
        self.assertEqual(0.90, parecidas.UMBRAL)


if __name__ == "__main__":
    unittest.main(verbosity=2)
