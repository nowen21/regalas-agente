# -*- coding: utf-8 -*-
"""`EP-004 · HU-009` · Por cuál regla se incumple más.

**Para qué sirve el número.** Una regla que produce cien hallazgos por semana
casi nunca significa un equipo descuidado: significa una regla mal escrita, o
una que hace falta automatizar. Sin el número esa conversación es opinión
contra opinión, y [`20·M19`](../../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md)
pide justamente ese dato antes de construir un validador.

**El caso que decide es `CP-002`:** el registro **no puede contener** el texto
del hallazgo. En un mensaje de incumplimiento viaja el contenido revisado, y ahí
puede ir una clave. Un archivo de métricas que copie lo revisado es una fuga con
nombre de estadística.
"""
import io
import json
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import comun                              # noqa: E402
import conteo                             # noqa: E402
from comun import AVISO, FALLA, Hallazgo  # noqa: E402


class ConteoPorRegla(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        with io.open(os.path.join(self.tmp, "VERSION"), "w",
                     encoding="utf-8", newline="\n") as f:
            f.write("31.10.0\n")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def leer_registro(self):
        ruta = os.path.join(self.tmp, "metricas", "conteo-por-regla.jsonl")
        with io.open(ruta, encoding="utf-8") as f:
            return f.read()

    # ── la regla sale del hallazgo que ya se construye ───────────────────

    def test_cp001_la_regla_se_deduce_del_mensaje(self):
        """Los 24 validadores ya citan su regla: no hay que tocarlos."""
        h = Hallazgo(FALLA, "a.md", 3,
                     "el cuerpo de `M5` mide 400 caracteres (20·M5 · fila 10)")
        self.assertEqual("20·M5", h.regla)

    def test_cp001b_la_cita_con_capitulo_gana_a_la_suelta(self):
        """El capítulo hace único al identificador: `F5` existe en dos sitios."""
        h = Hallazgo(AVISO, "a.md", 0, "esto toca `T5` y también `08·T5`")
        self.assertEqual("08·T5", h.regla)

    def test_cp001c_la_declarada_manda_sobre_la_deducida(self):
        h = Hallazgo(AVISO, "a.md", 0, "habla de `M5`", regla="09·G2")
        self.assertEqual("09·G2", h.regla)

    def test_cp001d_lo_que_no_nombra_ninguna_se_cuenta_aparte(self):
        """Repartirlo entre las demás falsearía el número que se usa para
        decidir qué regla cambiar."""
        cuenta = comun.conteo_por_regla([
            Hallazgo(FALLA, "a.md", 0, "algo sin regla"),
            Hallazgo(FALLA, "b.md", 0, "otra cosa suelta"),
            Hallazgo(AVISO, "c.md", 0, "esto sí es de `20·M5`")])
        self.assertEqual({"(sin regla)": 2, "20·M5": 1}, cuenta)

    # ── el registro no guarda lo revisado ────────────────────────────────

    def test_cp002_el_registro_no_contiene_el_texto_del_hallazgo(self):
        """El caso que decide: en el mensaje puede viajar una clave."""
        secreto = "AKIA1234567890ABCDEF"
        conteo.anotar([Hallazgo(FALLA, "config.py", 9,
                                "posible secreto en el código (%s) · 04·S4" % secreto)],
                      self.tmp, cuando="2026-08-22 10:00:00")
        guardado = self.leer_registro()
        self.assertNotIn(secreto, guardado)
        self.assertNotIn("config.py", guardado, "tampoco la ruta revisada")
        self.assertIn("04·S4", guardado)
        self.assertIn("31.10.0", guardado, "sin la versión no se puede comparar")

    def test_cp002b_una_linea_por_corrida(self):
        for i in range(3):
            conteo.anotar([Hallazgo(AVISO, "a.md", 0, "de `20·M5`")],
                          self.tmp, cuando="2026-08-22 1%d:00:00" % i)
        self.assertEqual(3, len(self.leer_registro().strip().splitlines()))
        self.assertEqual(3, len(conteo.corridas(self.tmp)))

    # ── dos corridas se pueden comparar ──────────────────────────────────

    def test_cp003_dos_corridas_con_un_arreglo_en_medio_muestran_la_baja(self):
        conteo.anotar([Hallazgo(FALLA, "a.md", 0, "de `20·M5`"),
                       Hallazgo(FALLA, "b.md", 0, "de `20·M5`"),
                       Hallazgo(FALLA, "c.md", 0, "de `09·G2`")],
                      self.tmp, cuando="2026-08-22 10:00:00")
        conteo.anotar([Hallazgo(FALLA, "c.md", 0, "de `09·G2`")],
                      self.tmp, cuando="2026-08-22 11:00:00")
        cambios = dict((r, (a, b)) for r, a, b in conteo.comparar(self.tmp))
        self.assertEqual((2, 0), cambios["20·M5"])
        self.assertNotIn("09·G2", cambios, "lo que no cambió no se reporta")

    def test_cp003b_con_una_sola_corrida_no_hay_con_que_comparar(self):
        conteo.anotar([Hallazgo(FALLA, "a.md", 0, "de `20·M5`")],
                      self.tmp, cuando="2026-08-22 10:00:00")
        self.assertEqual([], conteo.comparar(self.tmp))

    # ── el campo nuevo no rompe nada ─────────────────────────────────────

    def test_cp004_el_hallazgo_se_sigue_imprimiendo_igual(self):
        h = Hallazgo(FALLA, "a.md", 3, "el mensaje de siempre")
        self.assertIn("el mensaje de siempre", str(h))
        self.assertTrue(str(h).startswith("[FALLA]"))

    def test_cp004b_una_linea_rota_no_se_lleva_el_registro(self):
        conteo.anotar([Hallazgo(AVISO, "a.md", 0, "de `20·M5`")],
                      self.tmp, cuando="2026-08-22 10:00:00")
        ruta = os.path.join(self.tmp, "metricas", "conteo-por-regla.jsonl")
        with io.open(ruta, "a", encoding="utf-8", newline="\n") as f:
            f.write("esto no es json\n")
        self.assertEqual(1, len(conteo.corridas(self.tmp)))

    def test_cp004c_lo_que_se_imprime_ordena_por_cuantos(self):
        lineas = conteo.lineas_del_conteo([
            Hallazgo(FALLA, "a.md", 0, "de `20·M5`"),
            Hallazgo(FALLA, "b.md", 0, "de `20·M5`"),
            Hallazgo(FALLA, "c.md", 0, "de `09·G2`")], self.tmp)
        texto = "\n".join(lineas)
        self.assertIn("3 en total", texto)
        self.assertLess(texto.index("20·M5"), texto.index("09·G2"),
                        "la regla con más hallazgos va primero")


if __name__ == "__main__":
    unittest.main()
