# -*- coding: utf-8 -*-
"""La fila 10 mide el cuerpo **leído**, no el escrito.

`M5` da cuatro líneas de ochenta columnas — 320 caracteres — y `M15` exige que
**toda** cita a otra regla lleve su enlace. Contando el marcado, cada enlace
cuesta unos cincuenta caracteres que nadie lee, así que **las dos reglas del
estándar tiraban en direcciones contrarias y perdía la que se cumplía**: citar
bien te hacía reprobar por largo.

Medido el 2026-08-18, antes de corregirlo: de las **108** reglas que se pasaban
del límite, **27 se pasaban solo por eso**. `ID3` contaba 561 y son 265.

Esto no relaja la fila: la regla que de verdad no cabe sigue sin caber. Lo que
cambia es qué se cuenta.
"""
import os
import sys
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import metareglas   # noqa: E402

RAIZ = os.path.dirname(VALIDADORES)


class Cuerpo:
    """Lo mínimo que `Regla.largo()` necesita."""

    def __init__(self, *lineas):
        self.cuerpo = [(n, t) for n, t in enumerate(lineas, start=1)]

    largo = metareglas.Regla.largo


class ElLargoNoCuentaElMarcado(unittest.TestCase):

    def test_el_enlace_cuenta_por_su_texto(self):
        con_enlace = ("Ver la regla [`04·S4`](../04-seguridad.md#s4--gestión-de-secretos)"
                      " y seguirla.")
        como_se_lee = "Ver la regla `04·S4` y seguirla."
        self.assertEqual(len(como_se_lee), Cuerpo(con_enlace).largo(),
                         "el destino del enlace se está contando")

    def test_el_texto_sin_enlaces_no_cambia(self):
        texto = "Una regla corta y sin citas."
        self.assertEqual(len(texto), Cuerpo(texto).largo())

    def test_varios_enlaces_en_la_misma_linea(self):
        """Dos enlaces de destinos muy distintos cuentan lo mismo si su texto
        es igual de largo: lo que pesa es lo que se lee."""
        corto = Cuerpo("Ver [a](x.md) y [b](y.md).").largo()
        largo = Cuerpo("Ver [a](un/destino/mucho/mas/largo.md) y "
                       "[b](otro/todavia/peor.md).").largo()
        self.assertEqual(corto, largo)
        self.assertEqual(len("Ver a y b."), corto)

    def test_la_regla_que_de_verdad_no_cabe_sigue_sin_caber(self):
        """El arreglo no puede volverse una excusa para relajar la fila."""
        larga = Cuerpo("x" * 400)
        self.assertGreater(larga.largo(), metareglas.LIMITE_CUERPO)


class SobreElRepositorioDeVerdad(unittest.TestCase):

    def test_ninguna_regla_se_pasa_solo_por_el_marcado(self):
        """Lo que esta corrección garantiza: si una regla se reporta larga, es
        porque su texto es largo — no porque cite bien."""
        import re
        enlace = re.compile(r"\[([^\]]*)\]\([^)]*\)")
        culpables = []
        for r in metareglas.reglas(RAIZ):
            crudo = sum(len(t) for _, t in r.cuerpo)
            if crudo > metareglas.LIMITE_CUERPO >= r.largo():
                culpables.append((r.id, crudo, r.largo()))
        # No se afirma que sean cero: se afirma que **ninguna se reporta** por
        # eso. Las de la lista son justamente las que dejaron de reportarse.
        for id, crudo, leido in culpables:
            self.assertLessEqual(leido, metareglas.LIMITE_CUERPO,
                                 f"`{id}` sigue reportándose por el marcado")
        self.assertTrue(culpables, "la corrección no rescató ninguna regla: "
                                   "o ya no hace falta, o dejó de aplicarse")


if __name__ == "__main__":
    unittest.main()
