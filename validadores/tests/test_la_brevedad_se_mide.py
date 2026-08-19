# -*- coding: utf-8 -*-
"""`00·ID9` · `EP-005 · HU-012` — medir lo que se contesta, sin detener nada.

**El caso está medido, y en otro proyecto.** En `shopnest-mesa` el usuario pidió
«menos es más» **siete veces en tres días**: una el 2026-08-15, cinco el 16 y
una el 17. Cada vez se anotó el caso en un recuerdo, con su porqué y su ejemplo.
**Anotarlo no cambió nada**, y a la séptima el usuario lo dijo así — *«¿de qué
le sirve anotarlo tanto si no lo está cumpliendo?»*.

**Lo que faltaba no era otro recordatorio: era un número.** «Me parece que
contesta largo» no se puede revisar al cerrar la sesión; una mediana sí.

**Esto no comprueba `ID9` y no pretende hacerlo.** `reglas-validables.md` ya
declara que no se puede: contar renglones es fácil, decidir cuál sobra exige
entender qué cambia la decisión del que lee. Se cuenta lo primero.
"""
import io
import os
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import brevedad     # noqa: E402
from comun import FALLA      # noqa: E402


def transcripcion(*respuestas):
    """Una transcripción como la escribe `hook_historico.py`."""
    partes = ["<!-- sesion: abc -->\n\n# 2026-01-02 — Sesión\n\n## Conversación\n"]
    for i, texto in enumerate(respuestas, 1):
        partes.append("\n### %d · Usuario — 2026-01-02 10:0%d:00\n> algo\n" % (i, i))
        partes.append("\n**Agente** — 2026-01-02 10:0%d:30\n"
                      "<!-- agente: %d -->\n\n%s\n" % (i, i, texto))
    return "".join(partes)


class Base(unittest.TestCase):

    def archivo(self, contenido, nombre="2026-01-02-sesion.md"):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        carpeta = os.path.join(tmp.name, "historico-chat")
        os.makedirs(carpeta)
        ruta = os.path.join(carpeta, nombre)
        with io.open(ruta, "w", encoding="utf-8") as f:
            f.write(contenido)
        return tmp.name, ruta


class SeCuentaLoQueSeLee(Base):

    def test_cuenta_una_respuesta(self):
        _r, a = self.archivo(transcripcion(u"hola"))
        self.assertEqual(1, len(brevedad.respuestas(a)))

    def test_cuenta_varias(self):
        _r, a = self.archivo(transcripcion(u"una", u"dos", u"tres"))
        self.assertEqual(3, len(brevedad.respuestas(a)))

    def test_el_largo_es_el_del_texto(self):
        _r, a = self.archivo(transcripcion(u"12345"))
        self.assertEqual(5, brevedad.respuestas(a)[0][1])

    def test_los_comentarios_de_maquina_no_cuentan(self):
        """**El enganche deja marcas HTML** y el usuario no las lee."""
        _r, a = self.archivo(transcripcion(u"12345"))
        self.assertEqual(5, brevedad.respuestas(a)[0][1])

    def test_el_mensaje_del_usuario_no_cuenta(self):
        """Se mide lo que **el agente** escribe, no la conversación entera."""
        _r, a = self.archivo(transcripcion(u"abc"))
        self.assertEqual(3, sum(n for _f, n in brevedad.respuestas(a)))

    def test_una_respuesta_vacia_no_entra(self):
        _r, a = self.archivo(transcripcion(u"", u"algo"))
        self.assertEqual(1, len(brevedad.respuestas(a)))

    def test_la_tabla_y_el_codigo_cuentan(self):
        """**A propósito.** Ocupan pantalla igual, y lo que se mide es cuánto
        hay que leer — no cuánta prosa hay."""
        largo = brevedad.respuestas(self.archivo(
            transcripcion(u"| a | b |\n|---|---|\n| 1 | 2 |"))[1])[0][1]
        self.assertGreater(largo, 10)


class ElResumen(Base):

    def test_la_mediana_de_tres(self):
        _r, a = self.archivo(transcripcion(u"a" * 10, u"b" * 100, u"c" * 1000))
        self.assertEqual(100, brevedad.resumen(a)["mediana"])

    def test_la_mediana_de_dos_promedia(self):
        _r, a = self.archivo(transcripcion(u"a" * 10, u"b" * 20))
        self.assertEqual(15, brevedad.resumen(a)["mediana"])

    def test_la_maxima(self):
        _r, a = self.archivo(transcripcion(u"a" * 10, u"b" * 900))
        self.assertEqual(900, brevedad.resumen(a)["maxima"])

    def test_sin_respuestas_no_revienta(self):
        _r, a = self.archivo(u"# 2026-01-02 — Sesión\n\nsin nada\n")
        self.assertEqual({"cuantas": 0, "mediana": 0, "maxima": 0, "total": 0},
                         brevedad.resumen(a))


class NuncaDetiene(Base):
    """**Es lo que separa esto de un validador.** `ID9` no se puede comprobar;
    lo que se puede es dejar el número a la vista."""

    def test_nunca_hay_una_falla(self):
        raiz, _a = self.archivo(transcripcion(*[u"x" * 9000] * 10))
        self.assertEqual([], [h for h in brevedad.validar(raiz)
                              if h.severidad == FALLA])

    def test_la_sesion_larga_avisa(self):
        raiz, _a = self.archivo(transcripcion(*[u"x" * 9000] * 10))
        self.assertEqual(1, len(brevedad.validar(raiz)))

    def test_la_sesion_corta_calla(self):
        raiz, _a = self.archivo(transcripcion(*[u"corto"] * 10))
        self.assertEqual([], brevedad.validar(raiz))

    def test_una_sesion_de_pocos_turnos_no_avisa(self):
        """**Con cuatro respuestas la mediana no dice nada.** Una sesión que
        arrancó con un informe pedido no es una sesión que contesta largo."""
        raiz, _a = self.archivo(transcripcion(*[u"x" * 9000] * 4))
        self.assertEqual([], brevedad.validar(raiz))

    def test_se_mira_la_mediana_no_la_maxima(self):
        """Nueve cortas y una larguísima **no** es un problema de `ID9`."""
        raiz, _a = self.archivo(transcripcion(*([u"corto"] * 9 + [u"x" * 90000])))
        self.assertEqual([], brevedad.validar(raiz))


class Bordes(Base):

    def test_sin_historico_no_dice_nada(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.assertEqual([], brevedad.transcripciones(tmp.name))
        self.assertEqual([], brevedad.validar(tmp.name))

    def test_lo_que_no_es_transcripcion_se_ignora(self):
        """`historico-chat/` lleva `README.md`, `memory/` y `resumenes/`."""
        raiz, _a = self.archivo(transcripcion(u"algo"))
        with io.open(os.path.join(raiz, "historico-chat", "README.md"),
                     "w", encoding="utf-8") as f:
            f.write(u"# Cómo se usa\n")
        self.assertEqual(1, len(brevedad.transcripciones(raiz)))

    def test_el_texto_sale_con_una_linea_por_sesion(self):
        raiz, _a = self.archivo(transcripcion(u"algo"))
        self.assertIn(u"2026-01-02-sesion", brevedad.como_texto(raiz))

    def test_sin_nada_el_texto_es_vacio(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.assertEqual("", brevedad.como_texto(tmp.name))

    def test_no_es_punto_de_entrada(self):
        with io.open(os.path.join(VALIDADORES, "brevedad.py"),
                     encoding="utf-8") as f:
            self.assertIn(u"no_es_punto_de_entrada", f.read())


if __name__ == "__main__":
    unittest.main(verbosity=2)
