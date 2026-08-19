# -*- coding: utf-8 -*-
"""`20·M18` · `EP-002 · HU-006` — Una sola numeración, aunque haya dos sesiones.

**El caso está medido.** El 2026-08-14 dos sesiones abiertas sobre el mismo
repositorio dejaron dos numeraciones vivas: una escribió la `10.0.0` mientras la
otra subía la `9.0.0`, la `9.1.0` y la `9.2.0`. Y quedó rastro en el propio
registro del estándar: **dos entradas para la `15.4.0`**, de días distintos.

**Lo que no se puede comprobar** es que el número se haya elegido al guardar:
eso es un hábito, no algo que quede en el archivo. Lo que sí se comprueba es
**el resultado de no haberlo hecho**.

`git` no es obligatorio: sin repositorio no hay con qué comparar, y eso no es
un fallo.
"""
import io
import os
import subprocess
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import numeracion      # noqa: E402
from comun import AVISO, FALLA   # noqa: E402

CABEZA = u"# Cambios del estándar\n\n"


def _entrada(v, extra=u"", fecha=u"2026-08-18"):
    return u"## %s — %s%s\n\nUna cosa cambió, y por esto.\n\n" % (v, fecha, extra)


class Base(unittest.TestCase):

    def repo(self, version, registro, guardar=None, git=False):
        """Un repositorio de mentira. `guardar` es lo que queda en `HEAD`."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        r = tmp.name

        def escribir(nombre, texto):
            with io.open(os.path.join(r, nombre), "w", encoding="utf-8") as f:
                f.write(texto)

        if git or guardar is not None:
            for orden in (["init", "-q"],
                          ["config", "user.email", "p@p"],
                          ["config", "user.name", "p"]):
                subprocess.run(["git", "-C", r] + orden, capture_output=True)
            escribir("VERSION", (guardar or version) + u"\n")
            escribir("CHANGELOG.md", registro)
            subprocess.run(["git", "-C", r, "add", "-A"], capture_output=True)
            subprocess.run(["git", "-C", r, "commit", "-qm", "x"], capture_output=True)

        escribir("VERSION", version + u"\n")
        escribir("CHANGELOG.md", registro)
        return r

    def fallas(self, hs):
        return [h for h in hs if h.severidad == FALLA]

    def avisos(self, hs):
        return [h for h in hs if h.severidad == AVISO]


class SeQuedoAtras(Base):
    """El defecto que da origen a todo: otra sesión guardó primero."""

    def test_por_debajo_de_lo_guardado_es_falla(self):
        r = self.repo(u"9.2.0", CABEZA + _entrada(u"9.2.0"), guardar=u"10.0.0")
        self.assertTrue(self.fallas(numeracion.validar(r)))

    def test_el_mensaje_dice_los_dos_numeros(self):
        r = self.repo(u"9.2.0", CABEZA + _entrada(u"9.2.0"), guardar=u"10.0.0")
        m = self.fallas(numeracion.validar(r))[0].mensaje
        self.assertIn(u"9.2.0", m)
        self.assertIn(u"10.0.0", m)

    def test_igual_a_lo_guardado_no_es_falla(self):
        """**Recién guardado, coinciden.** Es lo normal, no un defecto: fue el
        primer falso positivo que dio este validador contra el repo real."""
        r = self.repo(u"9.2.0", CABEZA + _entrada(u"9.2.0"), guardar=u"9.2.0")
        self.assertEqual([], self.fallas(numeracion.validar(r)))

    def test_por_encima_de_lo_guardado_no_es_falla(self):
        r = self.repo(u"10.0.0", CABEZA + _entrada(u"10.0.0"), guardar=u"9.2.0")
        self.assertEqual([], self.fallas(numeracion.validar(r)))

    def test_sin_repositorio_no_dice_nada_de_esto(self):
        """Sin `git` no hay con qué comparar. No es un fallo."""
        r = self.repo(u"9.2.0", CABEZA + _entrada(u"9.2.0"))
        self.assertEqual([], self.fallas(numeracion.validar(r)))


class TieneSuEntrada(Base):

    def test_version_sin_entrada_es_falla(self):
        r = self.repo(u"10.0.0", CABEZA + _entrada(u"9.2.0"))
        self.assertTrue(self.fallas(numeracion.validar(r)))

    def test_con_su_entrada_calla(self):
        r = self.repo(u"10.0.0", CABEZA + _entrada(u"10.0.0"))
        self.assertEqual([], self.fallas(numeracion.validar(r)))

    def test_la_entrada_puede_traer_algo_mas_en_el_titulo(self):
        r = self.repo(u"10.0.0", CABEZA + _entrada(u"10.0.0", u"  ·  algo"))
        self.assertEqual([], self.fallas(numeracion.validar(r)))


class NoRepite(Base):
    """El rastro real: dos entradas para la `15.4.0`, de días distintos."""

    def test_numero_repetido_es_falla(self):
        reg = CABEZA + _entrada(u"15.4.0", fecha=u"2026-08-15") \
                     + _entrada(u"15.4.0", fecha=u"2026-08-14")
        r = self.repo(u"15.4.0", reg)
        self.assertTrue(self.fallas(numeracion.validar(r)))

    def test_el_mensaje_dice_cuantas_veces(self):
        reg = CABEZA + _entrada(u"15.4.0") * 3
        m = self.fallas(numeracion.validar(self.repo(u"15.4.0", reg)))[0].mensaje
        self.assertIn(u"3 entradas", m)

    def test_reconocido_en_el_registro_baja_a_aviso(self):
        """**No se renumera.** Un proyecto pudo haber adoptado ese número, y
        cambiárselo ahora le movería el piso sin que se entere. Marcado en el
        registro, deja de detener y sigue a la vista."""
        reg = CABEZA + _entrada(u"15.4.0", u"  ·  ⚠ **número repetido**") \
                     + _entrada(u"15.4.0", fecha=u"2026-08-14")
        hs = numeracion.validar(self.repo(u"15.4.0", reg))
        self.assertEqual([], self.fallas(hs))
        self.assertTrue(self.avisos(hs))

    def test_reconocerlo_no_lo_borra_del_informe(self):
        reg = CABEZA + _entrada(u"15.4.0", u"  ·  ⚠ **número repetido**") \
                     + _entrada(u"15.4.0", fecha=u"2026-08-14")
        m = self.avisos(numeracion.validar(self.repo(u"15.4.0", reg)))[0].mensaje
        self.assertIn(u"15.4.0", m)

    def test_sin_repetidos_calla(self):
        reg = CABEZA + _entrada(u"15.5.0") + _entrada(u"15.4.0")
        r = self.repo(u"15.5.0", reg)
        self.assertEqual([], self.fallas(numeracion.validar(r)))


class Huecos(Base):
    """Un salto puede ser a propósito. Se avisa, no se detiene."""

    def test_el_hueco_avisa(self):
        reg = CABEZA + _entrada(u"1.0.3") + _entrada(u"1.0.0")
        hs = numeracion.validar(self.repo(u"1.0.3", reg))
        self.assertEqual([], self.fallas(hs))
        self.assertTrue(self.avisos(hs))

    def test_consecutivos_no_avisan(self):
        reg = CABEZA + _entrada(u"1.0.1") + _entrada(u"1.0.0")
        self.assertEqual([], numeracion.validar(self.repo(u"1.0.1", reg)))


class Bordes(Base):

    def test_version_con_forma_rara_es_falla_y_no_revienta(self):
        r = self.repo(u"v10", CABEZA + _entrada(u"10.0.0"))
        self.assertEqual(1, len(self.fallas(numeracion.validar(r))))

    def test_sin_los_archivos_no_dice_nada(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.assertEqual([], numeracion.validar(tmp.name))

    def test_registro_vacio_no_revienta(self):
        r = self.repo(u"1.0.0", CABEZA)
        self.assertTrue(self.fallas(numeracion.validar(r)))

    def test_no_es_punto_de_entrada(self):
        """`validar.py` es la única puerta."""
        with io.open(os.path.join(VALIDADORES, "numeracion.py"),
                     encoding="utf-8") as f:
            fuente = f.read()
        self.assertIn(u"no_es_punto_de_entrada", fuente)


if __name__ == "__main__":
    unittest.main(verbosity=2)
