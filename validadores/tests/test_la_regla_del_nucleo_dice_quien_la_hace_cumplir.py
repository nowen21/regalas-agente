# -*- coding: utf-8 -*-
"""`EP-005 · HU-012` — una regla del núcleo dice quién la hace cumplir.

**El caso está medido.** El 2026-08-31 se contaron las 18 reglas vigentes del
capítulo `00` y se buscó su identificador dentro de los programas y de los
enganches: **siete no aparecían en ninguno**, y de las once que sí, solo dos
—`ID8` y `N6`— tenían una pieza que de verdad las ejecutara. Catorce de
dieciocho dependían de que el agente se acordara.

**Lo que esta comprobación puede decir, y lo que no.** Puede decir que la
declaración esté, que traiga su motivo y que la pieza nombrada exista. **No
puede decir que la pieza haga cumplir la regla**: eso se lee. Prometerlo sería
el número que el lector completa con lo que quiere creer (`S-091`).
"""
import io
import os
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import ejecutable          # noqa: E402
from comun import FALLA    # noqa: E402

CHECKLIST = u"""
---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../20-meta-reglas/checklist.md) contra
**v1.0.0**, el **2026-01-02**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
"""


def regla(id, declaracion=u""):
    """Una regla con su molde: encabezado, cuerpo, ejemplo y checklist."""
    return (u"> Regla del capítulo `00 · Prueba`.\n\n"
            u"## %s · Título de prueba\n\n"
            u"El cuerpo pide una sola cosa, en presente.\n\n"
            u"```\nINCORRECTO: hacerlo mal\nCORRECTO:   hacerlo bien\n```\n\n"
            u"%s%s" % (id, declaracion + u"\n\n" if declaracion else u"",
                       CHECKLIST))


class Base(unittest.TestCase):

    def cuerpo_de_reglas(self, *reglas):
        """Un `base/` de mentiras, con las reglas que la prueba necesita."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        carpeta = os.path.join(tmp.name, "base", "00-prueba")
        os.makedirs(carpeta)
        os.makedirs(os.path.join(tmp.name, "validadores"))
        with io.open(os.path.join(tmp.name, "validadores", "marcas.py"),
                     "w", encoding="utf-8") as f:
            f.write(u"# una pieza que existe de verdad\n")
        for id, declaracion in reglas:
            with io.open(os.path.join(carpeta, "%s-de-prueba.md" % id),
                         "w", encoding="utf-8") as f:
                f.write(regla(id, declaracion))
        return tmp.name


class SinDeclaracionSeReporta(Base):
    """`CA-01` — la regla que no dice quién la hace cumplir se reporta."""

    def test_la_regla_sin_declaracion_se_reporta(self):
        raiz = self.cuerpo_de_reglas(("N1", u""))
        self.assertEqual(1, len(ejecutable.validar(raiz)))

    def test_el_hallazgo_es_falla_y_la_corrida_termina_con_error(self):
        raiz = self.cuerpo_de_reglas(("N1", u""))
        self.assertEqual(FALLA, ejecutable.validar(raiz)[0].severidad)

    def test_el_mensaje_nombra_la_regla(self):
        raiz = self.cuerpo_de_reglas(("N1", u""))
        self.assertIn(u"`N1`", ejecutable.validar(raiz)[0].mensaje)

    def test_el_mensaje_dice_donde_escribirlo(self):
        """`RNF-01` — decir que algo falta sin decir dónde no sirve."""
        mensaje = ejecutable.validar(self.cuerpo_de_reglas(("N1", u"")))[0].mensaje
        self.assertIn(u"Quién la hace cumplir", mensaje)
        self.assertIn(u"antes del checklist", mensaje)

    def test_la_que_declara_su_pieza_no_se_reporta(self):
        raiz = self.cuerpo_de_reglas(
            ("N1", u"**Quién la hace cumplir:** `validadores/marcas.py`, que la "
                   u"cuenta sobre lo que se entrega."))
        self.assertEqual([], ejecutable.validar(raiz))

    def test_solo_se_reporta_la_que_falta(self):
        raiz = self.cuerpo_de_reglas(
            ("N1", u"**Quién la hace cumplir:** `validadores/marcas.py`, que la "
                   u"cuenta sobre lo que se entrega."),
            ("N2", u""))
        hallazgos = ejecutable.validar(raiz)
        self.assertEqual(1, len(hallazgos))
        self.assertIn(u"`N2`", hallazgos[0].mensaje)

    def test_la_derogada_queda_fuera(self):
        """Dejó de regir: pedirle cuentas es pedírselas a una regla que no manda."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        carpeta = os.path.join(tmp.name, "base", "00-prueba")
        os.makedirs(carpeta)
        with io.open(os.path.join(carpeta, "N3-de-prueba.md"),
                     "w", encoding="utf-8") as f:
            f.write(u"## N3 · Título de prueba `[DEROGADA en 2.0.0 → ver N4]`\n\n"
                    u"El cuerpo que ya no manda.\n" + CHECKLIST)
        self.assertEqual([], ejecutable.validar(tmp.name))


class NadieValeConMotivo(Base):
    """`CA-02` — «nadie la hace cumplir» es una respuesta válida, con su motivo."""

    MOTIVO = (u"**Nadie la hace cumplir:** ningún programa ve si el usuario "
              u"aprobó, porque la aprobación ocurre en el chat.")

    def test_con_motivo_no_se_reporta(self):
        raiz = self.cuerpo_de_reglas(("N1", self.MOTIVO))
        self.assertEqual([], ejecutable.validar(raiz))

    def test_sin_motivo_se_reporta(self):
        raiz = self.cuerpo_de_reglas(("N1", u"**Nadie la hace cumplir:** no."))
        self.assertEqual(1, len(ejecutable.validar(raiz)))

    def test_el_mensaje_dice_que_falta_el_motivo(self):
        raiz = self.cuerpo_de_reglas(("N1", u"**Nadie la hace cumplir:** no."))
        self.assertIn(u"no dice por qué", ejecutable.validar(raiz)[0].mensaje)

    def test_una_casilla_marcada_no_es_una_decision(self):
        """El motivo se mide por largo, y el umbral está escrito con su porqué."""
        corto = u"**Nadie la hace cumplir:** es criterio."
        self.assertLess(len(corto.split(u"**")[-1].strip()),
                        ejecutable.MOTIVO_MINIMO)
        raiz = self.cuerpo_de_reglas(("N1", corto))
        self.assertEqual(1, len(ejecutable.validar(raiz)))


class LaPiezaDeclaradaExiste(Base):
    """`CA-03` — nombrar una pieza que no existe es peor que no nombrar ninguna."""

    def test_la_pieza_inventada_se_reporta(self):
        raiz = self.cuerpo_de_reglas(
            ("N1", u"**Quién la hace cumplir:** `validadores/inventado.py`."))
        self.assertEqual(1, len(ejecutable.validar(raiz)))

    def test_el_mensaje_nombra_la_pieza_que_no_resolvio(self):
        raiz = self.cuerpo_de_reglas(
            ("N1", u"**Quién la hace cumplir:** `validadores/inventado.py`."))
        self.assertIn(u"`validadores/inventado.py`",
                      ejecutable.validar(raiz)[0].mensaje)

    def test_la_pieza_real_no_se_reporta(self):
        raiz = self.cuerpo_de_reglas(
            ("N1", u"**Quién la hace cumplir:** `validadores/marcas.py`."))
        self.assertEqual([], ejecutable.validar(raiz))

    def test_decir_que_alguien_la_hace_cumplir_sin_nombrarlo_se_reporta(self):
        raiz = self.cuerpo_de_reglas(
            ("N1", u"**Quién la hace cumplir:** un enganche del estándar."))
        self.assertIn(u"no nombra la pieza",
                      ejecutable.validar(raiz)[0].mensaje)

    def test_dos_piezas_declaradas_se_revisan_las_dos(self):
        """Uno de los dos límites que la HU pide con comportamiento definido."""
        raiz = self.cuerpo_de_reglas(
            ("N1", u"**Quién la hace cumplir:** `validadores/marcas.py` y "
                   u"`validadores/inventado.py`."))
        hallazgos = ejecutable.validar(raiz)
        self.assertEqual(1, len(hallazgos))
        self.assertIn(u"inventado.py", hallazgos[0].mensaje)


class ElNucleoDeVerdad(unittest.TestCase):
    """`CA-04` y la no regresión: sobre el estándar tal como está publicado."""

    def test_ninguna_regla_del_nucleo_queda_sin_declarar(self):
        self.assertEqual([], ejecutable.validar())

    def test_las_dieciocho_estan_contadas(self):
        c = ejecutable.cuenta()
        self.assertEqual(c["reglas"], c["con_pieza"] + c["sin_nadie"])

    def test_id9_declara_su_decision(self):
        """El caso que originó la historia."""
        reglas = ejecutable._del_nucleo(ejecutable.RAIZ)
        id9 = [r for r in reglas if r.id == "ID9"][0]
        clase, texto = ejecutable.declaracion(id9)
        self.assertEqual("quien", clase)
        self.assertIn(u"brevedad.py", texto)

    def test_id10_declara_su_decision(self):
        reglas = ejecutable._del_nucleo(ejecutable.RAIZ)
        id10 = [r for r in reglas if r.id == "ID10"][0]
        clase, texto = ejecutable.declaracion(id10)
        self.assertEqual("quien", clase)
        self.assertIn(u"redaccion.py", texto)

    def test_dos_corridas_dan_lo_mismo(self):
        """`RNF-02` — el mismo cuerpo de reglas da el mismo resultado."""
        self.assertEqual([h.mensaje for h in ejecutable.validar()],
                         [h.mensaje for h in ejecutable.validar()])

    def test_la_linea_de_cierre_dice_las_dos_cifras(self):
        texto = ejecutable.como_texto()
        self.assertIn(u"con pieza que las ejecuta", texto)
        self.assertIn(u"sin quien las ejecute", texto)

    def test_declararlo_no_se_anuncia_como_hacerlas_cumplir(self):
        """El aviso que impide leer la cuenta de más."""
        self.assertIn(u"lo lee una persona", ejecutable.como_texto())

    def test_no_es_punto_de_entrada(self):
        with io.open(os.path.join(VALIDADORES, "ejecutable.py"),
                     encoding="utf-8") as f:
            self.assertIn(u"no_es_punto_de_entrada", f.read())


if __name__ == "__main__":
    unittest.main(verbosity=2)
