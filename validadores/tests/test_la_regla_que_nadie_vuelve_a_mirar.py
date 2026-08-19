# -*- coding: utf-8 -*-
"""Pendiente 14 · `EP-001·HU-007·CA-04` — la vigencia de una regla se mide.

**Una regla equivocada se comporta exactamente igual que una correcta.** Sigue
ahí, sigue pasando su checklist de forma, y el agente la sigue obedeciendo. Lo
único que cambió fue el mundo que describía, y eso no rompe nada.

**Lo que estas pruebas fijan es dónde está el límite del programa.** Decidir si
una regla sigue valiendo es criterio y nada lo automatiza: acá se comprueba lo
mecánico —leer la fecha, ordenar, no inventar un umbral— y sobre todo **que
nunca detenga nada**, que es la decisión que hace útil el reporte.
"""
import os
import sys
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import vigencia   # noqa: E402
from comun import FALLA, RAIZ   # noqa: E402


class Regla:
    """Lo mínimo que `vigencia` necesita de una regla."""

    def __init__(self, id, texto):
        self.id, self.texto = id, texto
        self.archivo, self.linea = "base/x.md", 1


SELLO = ("Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) "
         "contra **v24.0.0**, el **2026-08-11**.")


class LasDosFechasNoSonLaMisma(unittest.TestCase):
    """Confundirlas era el defecto que este módulo viene a corregir."""

    def test_el_sello_no_cuenta_como_revision_de_fondo(self):
        """Dice que se le aplicó el molde, no que el problema siga existiendo."""
        r = Regla("X1", SELLO)
        self.assertEqual("2026-08-11", vigencia.fecha_del_sello(r))
        self.assertEqual("", vigencia.revisada(r))

    def test_la_linea_de_revision_si_cuenta(self):
        r = Regla("X1", SELLO + "\n> Revisada contra la realidad el 2026-08-19.")
        self.assertEqual("2026-08-19", vigencia.revisada(r))

    def test_una_regla_sin_nada_no_revienta(self):
        """La regla partida ayer todavía no tiene sello, y tiene que salir igual."""
        r = Regla("X1", "")
        self.assertEqual("", vigencia.revisada(r))
        self.assertEqual("", vigencia.fecha_del_sello(r))


class LoQueNoHace(unittest.TestCase):
    """La mitad que suele faltar: que el programa se quede quieto."""

    def test_nunca_detiene_nada(self):
        """**No hay umbral, y es una decisión.**

        Un umbral inventado produce una alarma que se aprende a ignorar, y
        entonces el día que importe tampoco se mira. Se ordena y se muestra;
        cada cuánto revisar se decide después de mirar la lista.
        """
        for h in vigencia.validar(RAIZ):
            self.assertNotEqual(FALLA, h.severidad, h.mensaje)

    def test_avisa_una_sola_vez_y_no_una_por_regla(self):
        """245 avisos idénticos entierran los hallazgos que sí piden acción."""
        self.assertLessEqual(len(vigencia.validar(RAIZ)), 1)

    def test_calla_cuando_todas_estan_revisadas(self):
        """Sin esto, el aviso saldría siempre y nadie lo leería."""
        datos = [(Regla("X1", ""), "2026-08-19", "2026-08-11", 0)]
        real = vigencia.listado
        try:
            vigencia.listado = lambda raiz=None: datos
            self.assertEqual([], vigencia.validar(RAIZ))
        finally:
            vigencia.listado = real


class ElOrden(unittest.TestCase):

    def test_la_que_nunca_se_reviso_encabeza(self):
        datos = vigencia.listado(RAIZ)
        self.assertTrue(datos, "el estándar tiene reglas")
        sin = [d for d in datos if not d[1]]
        if sin:
            self.assertEqual("", datos[0][1],
                             "si hay alguna sin revisar, va primero")

    def test_entre_las_no_revisadas_manda_el_sello_mas_viejo(self):
        sin = [d for d in vigencia.listado(RAIZ) if not d[1]]
        fechas = [d[2] for d in sin]
        self.assertEqual(sorted(fechas), fechas)


if __name__ == "__main__":
    unittest.main()
