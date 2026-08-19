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
import io
import os
import sys
import tempfile
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


class LaMarcaBlindadaEsDelNucleo(unittest.TestCase):
    """`20·M1` · Una regla no se declara intocable viviendo fuera del núcleo.

    **Es la única mitad de `M1` que un programa puede juzgar.** Que un nivel «no
    contradiga al de arriba» exige leer las dos reglas; que una regla lleve la
    marca del capítulo `00` estando en otro capítulo, no.

    **Y es la vía por la que la jerarquía se rompería sin ruido:** una regla de
    capa 2 con la marca queda por encima de las demás sin haber pasado por el
    núcleo — se saltó el nivel en vez de contradecirlo.

    Quedó pendiente desde el 2026-08-07, en el punto 8 del pendiente 33.
    """

    def repo(self, archivo, encabezado):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        base = os.path.join(tmp.name, "base")
        os.makedirs(base)
        ruta = os.path.join(base, archivo)
        with io.open(ruta, "w", encoding="utf-8") as f:
            f.write(u"# Capítulo\n\n## %s\n\nUna exigencia corta.\n\n"
                    u"```\nINCORRECTO: no\nCORRECTO:   sí\n```\n" % encabezado)
        return tmp.name

    def _blindadas(self, raiz):
        reglas = metareglas.reglas(raiz)
        return metareglas._blindada_solo_en_el_nucleo(reglas)

    def test_en_el_nucleo_no_se_reporta(self):
        raiz = self.repo("00-nucleo-blindado.md", u"N9 · Algo `[BLINDADA]`")
        self.assertEqual([], self._blindadas(raiz))

    def test_fuera_del_nucleo_es_falla(self):
        raiz = self.repo("07-calidad-de-codigo.md", u"Q9 · Algo `[BLINDADA]`")
        self.assertEqual(1, len(self._blindadas(raiz)))

    def test_el_mensaje_nombra_la_regla(self):
        raiz = self.repo("07-calidad-de-codigo.md", u"Q9 · Algo `[BLINDADA]`")
        self.assertIn(u"Q9", self._blindadas(raiz)[0].mensaje)

    def test_una_regla_sin_la_marca_no_se_reporta(self):
        raiz = self.repo("07-calidad-de-codigo.md", u"Q9 · Algo corriente")
        self.assertEqual([], self._blindadas(raiz))

    def test_la_palabra_en_la_prosa_no_cuenta(self):
        """**El ancla es lo que hace usable este control.** `BLINDADA` aparece
        en prosa en seis archivos; sin anclar al encabezado, el validador
        reportaría de más — y uno que reporta de más se termina apagando."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        base = os.path.join(tmp.name, "base")
        os.makedirs(base)
        with io.open(os.path.join(base, "07-calidad-de-codigo.md"),
                     "w", encoding="utf-8") as f:
            f.write(u"# Capítulo\n\n## Q9 · Algo corriente\n\n"
                    u"Esto no puede tocar una regla `[BLINDADA]` del núcleo.\n\n"
                    u"```\nINCORRECTO: no\nCORRECTO:   sí\n```\n")
        self.assertEqual([], self._blindadas(tmp.name))


class ElSelloVenceSoloPorSuPropiaRegla(unittest.TestCase):
    """`52` · Editar una regla no puede vencer el sello de sus vecinas.

    **Medido el 2026-08-19: 119 avisos en una corrida.** La comprobación miraba
    la fecha del **archivo**, y un capítulo es un archivo con veinte reglas
    dentro: tocar una las vencía todas.

    **Un validador que reporta ciento diecinueve cosas no lo lee nadie**, y su
    propio texto ya lo había anticipado — *«si esto produce demasiado ruido, la
    huella queda como el paso siguiente, ya con datos»*.
    """

    def test_sobre_el_estandar_no_queda_ninguno_vencido(self):
        vencidos = [h for h in metareglas.validar() if "se aplicó el" in h.mensaje]
        self.assertEqual([], [h.mensaje[:60] for h in vencidos])

    def test_la_regla_sin_cambios_no_vence(self):
        """Lo guardado y lo de ahora coinciden: no hay nada que revisar."""
        r = [x for x in metareglas.reglas() if x.id == "D2"][0]
        self.assertFalse(metareglas._cambio_de_verdad(r))

    def test_el_encabezado_no_cuenta_al_comparar(self):
        """**Fue el primer intento y falló entero.** `regla.texto` no trae el
        encabezado, así que compararlo contra el lado guardado *con* encabezado
        daba distinto siempre — y la comprobación quedaba igual de ruidosa,
        pero con más código."""
        r = [x for x in metareglas.reglas() if x.id == "D2"][0]
        self.assertFalse(r.texto.lstrip().startswith("## "))
