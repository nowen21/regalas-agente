# -*- coding: utf-8 -*-
"""Pendiente 19 · Un sello de checklist que se contradice a sí mismo.

**La tabla es la que se lee.** Nadie recorre veinte filas de prosa: se mira el
renglón de emoticones y se sigue. Un sello donde el texto reprueba la fila 5 y
la tabla la muestra en ✅ afirma dos cosas contrarias, y la que gana es la
falsa — porque es la que se ve.

Salió de aplicarle el checklist a los veinte capítulos: **cinco sellos
escritos en la misma pasada tenían la tabla y su propio texto en desacuerdo**,
y en cuatro de ellos el error era el mismo, correr una casilla del bloque `C`.
Nadie se equivocó en el juicio: se equivocaron al pasarlo a la tabla.

Tres comprobaciones, y cada una nace de algo que pasó de verdad:

- El texto reprueba una fila que la tabla da por buena.
- La línea de totales no coincide con su propia tabla — diez sellos.
- Dos bloques de checklist apilados en la misma regla — `M14` tenía el de la
  `v2.1.0` encima del de la `v2.2.0`, y quien leía de arriba abajo se quedaba
  con el viejo.
"""
import os
import sys
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import metareglas   # noqa: E402

TABLA = u"""| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | %s |
| B · Cómo se identifica | 5–6 | %s |
| C · Cómo está escrita | 7–13 | %s |
| D · Cómo se relaciona | 14–17 | %s |
| E · Fuera de su texto | 18–20 | %s |
"""

OK, NO, NA = u"✅", u"❌", u"N/A"


def tabla(a=None, b=None, c=None, d=None, e=None):
    return TABLA % (
        u" ".join(a or [OK] * 4),
        u" ".join(b or [OK] * 2),
        u" ".join(c or [OK] * 7),
        u" ".join(d or [NA, NA, NA, OK]),
        u" ".join(e or [OK] * 3),
    )


def sello(veredicto=u"NO CUMPLE", cuerpo=None, totales=None, prosa=u"",
          **bloques):
    partes = [u"### Checklist  ·  **%s**" % veredicto,
              u"",
              u"Aplicado el checklist contra **v1.0.0**, el **2026-01-01**.",
              u"",
              cuerpo if cuerpo is not None else tabla(**bloques),
              totales or u"",
              prosa]
    return u"\n".join(partes)


class Regla:
    """Lo mínimo que las tres comprobaciones necesitan."""

    def __init__(self, texto, id="ZZ1"):
        self.texto, self.id = texto, id
        self.archivo, self.linea, self.derogada = "base/x.md", 3, False


class LaTablaYSuTextoDicenLoMismo(unittest.TestCase):

    def test_el_texto_reprueba_una_fila_que_la_tabla_da_por_buena(self):
        """El caso de `C15`: la prosa reprueba la 5 y la tabla la deja en ✅."""
        r = Regla(sello(prosa=u"**Fila 5 · nombra un módulo de un proyecto real**."))
        h = metareglas._sello_se_contradice(r)
        self.assertEqual(1, len(h))
        self.assertIn("fila 5", h[0].mensaje)

    def test_varias_filas_se_nombran_en_plural(self):
        """El de `C10`, que traía dos. Un mensaje que diga «la fila 5, 10» se
        lee como un número raro, no como dos filas."""
        r = Regla(sello(prosa=u"**Fila 5 · tecnología.**\n\n**Fila 10 · no cabe.**"))
        h = metareglas._sello_se_contradice(r)
        self.assertIn("las filas 5 y 10", h[0].mensaje)

    def test_el_texto_agrupado_tambien_cuenta(self):
        """`**Filas 8, 9 y 10**` es la forma que usan la mitad de los sellos."""
        r = Regla(sello(prosa=u"**Filas 8, 9 y 10 ·** son tres reglas en una."))
        self.assertEqual(1, len(metareglas._sello_se_contradice(r)))

    def test_la_tabla_puede_marcar_mas_de_lo_que_el_texto_desglosa(self):
        """**No se reporta al revés.** El texto agrupa —«son tres reglas en
        una»— y no tiene por qué desglosar cada fila que la tabla ya marcó.
        Exigirlo convertiría la comprobación en ruido sobre sellos correctos.
        """
        r = Regla(sello(c=[OK, NO, NO, NO, OK, OK, OK],
                        prosa=u"Son tres reglas en una y no cabe."))
        self.assertEqual([], metareglas._sello_se_contradice(r))

    def test_cuando_coinciden_no_se_reporta(self):
        r = Regla(sello(b=[NO, OK], prosa=u"**Fila 5 · nombra tecnología.**"))
        self.assertEqual([], metareglas._sello_se_contradice(r))

    def test_un_cumple_que_cuenta_lo_que_corrigio_no_se_reporta(self):
        """El caso de `17·I6`, y es el que evita el falso positivo.

        Un sello en CUMPLE suele contar **qué reprobaba antes de corregirlo**.
        Comparar esas filas contra la tabla lo daría por contradictorio cuando
        es justo lo contrario: la regla se arregló y el sello lo explica.
        """
        r = Regla(sello(veredicto=u"CUMPLE",
                        prosa=u"**Fila 8 · el título manda.** Se corrigió."))
        self.assertEqual([], metareglas._sello_se_contradice(r))

    def test_un_cumple_con_una_cruz_en_la_tabla_si_se_reporta(self):
        r = Regla(sello(veredicto=u"CUMPLE", c=[OK, NO, OK, OK, OK, OK, OK]))
        h = metareglas._sello_se_contradice(r)
        self.assertEqual(1, len(h))
        self.assertIn("CUMPLE", h[0].mensaje)

    def test_sin_bloque_de_checklist_no_hay_nada_que_comparar(self):
        self.assertEqual([], metareglas._sello_se_contradice(
            Regla(u"## ZZ1 · Algo\n\nExige algo.\n")))


class LaLineaDeTotalesCuadraConLaTabla(unittest.TestCase):

    def test_los_totales_que_no_coinciden_se_reportan(self):
        """Diez sellos lo tenían mal, casi todos por la misma cuenta de N/A."""
        # La tabla tiene 15 ✅ · 3 ❌ · 2 N/A; el resumen dice otra cosa. Es
        # literalmente lo que decía `C15`, y por el mismo lado: la cuenta de
        # N/A de más y la de ✅ de menos.
        r = Regla(sello(totales=u"**20 filas: 14 ✅ · 3 ❌ · 3 N/A.**",
                        c=[OK, OK, NO, NO, NO, OK, OK],
                        d=[NA, NA, OK, OK]))
        h = metareglas._totales_del_sello(r)
        self.assertEqual(1, len(h))
        self.assertIn(u"14 ✅", h[0].mensaje)

    def test_los_totales_correctos_no_se_reportan(self):
        r = Regla(sello(totales=u"**20 filas: 14 ✅ · 3 ❌ · 3 N/A.**",
                        c=[OK, OK, NO, NO, NO, OK, OK],
                        d=[NA, NA, NA, OK]))
        self.assertEqual([], metareglas._totales_del_sello(r))

    def test_una_tabla_que_no_suma_veinte_se_dice_asi(self):
        """No se corrige un total contra una tabla incompleta: el defecto es
        otro y decirlo mal manda a arreglar lo que no es."""
        r = Regla(sello(totales=u"**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**",
                        cuerpo=u"| A · Dónde va | 1–4 | ✅ ✅ |\n"))
        h = metareglas._totales_del_sello(r)
        self.assertEqual(1, len(h))
        self.assertIn("20 filas", h[0].mensaje)

    def test_sin_linea_de_totales_no_se_reporta(self):
        self.assertEqual([], metareglas._totales_del_sello(Regla(sello())))


class UnSoloSelloPorRegla(unittest.TestCase):

    def test_dos_bloques_apilados_se_reportan(self):
        """Lo de `M14`: el sello de la `v2.1.0` encima del de la `v2.2.0`."""
        r = Regla(sello(veredicto=u"CUMPLE") + u"\n---\n" + sello(veredicto=u"CUMPLE"))
        h = metareglas._un_solo_sello(r)
        self.assertEqual(1, len(h))
        self.assertIn("2 bloques", h[0].mensaje)

    def test_uno_solo_no_se_reporta(self):
        self.assertEqual([], metareglas._un_solo_sello(Regla(sello())))


class ElCuerpoDeReglasNoSeContradice(unittest.TestCase):
    """Sobre `base/` de verdad: las tres comprobaciones en cero.

    Es la prueba que se cae cuando alguien vuelve a escribir un sello a mano,
    que es exactamente cuando hace falta que se caiga.
    """

    def test_ningun_sello_del_estandar_se_contradice(self):
        malos = []
        for r in metareglas.reglas():
            malos += (metareglas._sello_se_contradice(r)
                      + metareglas._totales_del_sello(r)
                      + metareglas._un_solo_sello(r))
        self.assertEqual([], [h.mensaje for h in malos])


if __name__ == "__main__":
    unittest.main()
