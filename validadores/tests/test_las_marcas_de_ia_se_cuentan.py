# -*- coding: utf-8 -*-
"""Pendiente 11 · Contar las marcas de `00·ID8` antes de tocar nada.

El pendiente pide **contar antes de limpiar**: sin el recuento no se sabe si
el trabajo son dos horas o dos días. Y decía que hacerlo a mano sobre 200
archivos es lo que lo volvía inabordable.

**Lo que estas pruebas fijan es dónde está la frontera.** El anexo tiene ocho
secciones y casi todas piden criterio —si la raya aparece «muy seguido», si el
paralelismo es «perfecto»—. Un programa que opinara de eso llenaría de ruido lo
que hoy nadie mira. Acá se cuenta lo que el propio anexo llama *«las únicas que
un script cuenta sin equivocarse»*, y lo demás **no se toca a propósito**.
"""
import io
import os
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import marcas   # noqa: E402


def claves(linea):
    return sorted(c for c, _ in marcas.marcas_de_linea(linea))


class LoQueSeCuenta(unittest.TestCase):

    def test_las_invisibles(self):
        """Sobreviven a cualquier reescritura y no se ven leyendo."""
        for caracter in (u" ", u"​", u"﻿", u"­",
                         u"…", u"–"):
            with self.subTest(caracter=repr(caracter)):
                self.assertEqual(1, len(marcas.marcas_de_linea(
                    u"palabra%spalabra" % caracter)))

    def test_la_raya_larga(self):
        self.assertEqual(["raya"], claves(u"la solución — que es buena — sirve")[:1])
        self.assertEqual(2, claves(u"a — b — c").count("raya"))

    def test_la_vineta_con_negrita_y_dos_puntos(self):
        self.assertIn("vineta", claves(u"- **Algo:** lo que sea"))
        self.assertNotIn("vineta", claves(u"- algo que no abre con negrita"))

    def test_el_encabezado_que_termina_en_dos_puntos(self):
        self.assertIn("encabezado", claves(u"## Qué falta:"))
        self.assertNotIn("encabezado", claves(u"## Qué falta"))

    def test_la_flecha_como_vineta(self):
        self.assertIn("flecha", claves(u"→ eso lleva a lo otro"))
        self.assertNotIn("flecha", claves(u"de A → B dentro de la frase"))

    def test_el_semaforo(self):
        self.assertIn("semaforo", claves(u"estado 🔴 detenido"))


class LoQueNoSeCuenta(unittest.TestCase):
    """Cada exclusión con su motivo, para que no se borre por parecer de más."""

    def test_la_cita_del_estandar_no_es_punto_medio(self):
        """`NN·ID` es notación definida por `20·M4`, y el anexo la exceptúa."""
        self.assertNotIn("punto-medio", claves(u"lo dice 20·M4 y también 02·F0"))

    def test_el_punto_medio_suelto_si_se_cuenta(self):
        """Adornar un título con `·` es lo que el anexo llama marca."""
        self.assertIn("punto-medio", claves(u"Fase A · el título"))

    def test_lo_que_pide_criterio_no_se_cuenta(self):
        """El paralelismo, la regla de tres y el español de otro lado.

        **No es que no importen: es que un programa no los puede juzgar.**
        Contarlos por aproximación llenaría la salida de ruido y el día que
        alguien la mire va a dejar de mirarla.
        """
        self.assertEqual([], claves(u"Tres razones, tres ejemplos, tres viñetas."))
        self.assertEqual([], claves(u"En tal sentido, es importante destacar."))


class ElConteo(unittest.TestCase):

    def repo(self, archivos):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        for rel, contenido in archivos.items():
            ruta = os.path.join(tmp.name, *rel.split("/"))
            if not os.path.isdir(os.path.dirname(ruta)):
                os.makedirs(os.path.dirname(ruta))
            with io.open(ruta, "w", encoding="utf-8") as f:
                f.write(contenido)
        return tmp.name

    def test_reparte_por_marca_y_por_archivo(self):
        """Dos repartos: por marca dice qué pesa, por archivo dónde empezar."""
        raiz = self.repo({
            "base/a.md": u"uno — dos — tres\n",
            "notas/b.md": u"cuatro — cinco\n",
        })
        por_marca, por_archivo, _ = marcas.contar(raiz)
        self.assertEqual(3, por_marca["raya"])
        self.assertEqual(2, len(por_archivo))

    def test_el_historico_se_cuenta_aparte(self):
        """Es transcripción literal: no se reescribe, así que no es deuda."""
        raiz = self.repo({
            "base/a.md": u"uno — dos\n",
            "historico-chat/c.md": u"tres — cuatro — cinco\n",
        })
        self.assertEqual(1, sum(marcas.contar(raiz)[0].values()))
        self.assertEqual(3, sum(marcas.contar(raiz, incluir_historico=True)[0].values()))

    def test_el_ejemplo_dentro_de_un_bloque_no_cuenta(self):
        """En un bloque cercado la marca es el ejemplo de lo que no se hace."""
        raiz = self.repo({"base/a.md": u"bien\n\n```\nmal — mal\n```\n"})
        self.assertEqual({}, marcas.contar(raiz)[0])

    def test_el_catalogo_no_se_cuenta_a_si_mismo(self):
        """Un catálogo de marcas está lleno de marcas por definición."""
        raiz = self.repo({
            "base/00-identidad-y-rol/marcadores-de-ia.md": u"la raya — así\n",
        })
        self.assertEqual({}, marcas.contar(raiz)[0])


class SoloSeReportaLoQueSeHereda(ElConteo):
    """`validar` mira `base/` y `plantillas/`, que es lo que viaja al proyecto.

    Reportar hoy `notas/` y `analisis/` sepultaría lo que sí hay que arreglar
    — y una salida sepultada se deja de leer.
    """

    def test_notas_y_analisis_no_se_reportan(self):
        raiz = self.repo({
            "base/a.md": u"uno — dos\n",
            "notas/b.md": u"tres — cuatro\n",
            "analisis/c.md": u"cinco — seis\n",
        })
        archivos = {os.path.basename(h.archivo) for h in marcas.validar(raiz)}
        self.assertEqual({"a.md"}, archivos)

    def test_una_vez_por_linea_y_por_marca(self):
        """El conteo va en `contar`; acá lo que importa es dónde mirar."""
        raiz = self.repo({"base/a.md": u"uno — dos — tres — cuatro\n"})
        self.assertEqual(1, len(marcas.validar(raiz)))


if __name__ == "__main__":
    unittest.main()


class ElSeparadorDeEncabezadoEsNotacion(unittest.TestCase):
    """`00·ID8` · El `·` que separa el número del capítulo de su nombre.

    **Decidido el 2026-08-18.** Hasta entonces se contaban los 1 599 separadores
    de título como marca de generación automática — con lo que el propio índice
    del anexo, `## 2 · Puntuación y tipografía`, era una marca.

    **El código ya lo tenía decidido y no lo había implementado.** Su comentario
    decía *«ni de un `A · B` de encabezado: los dos son notación definida»*, y la
    expresión solo cubría la cita `NN·ID`.
    """

    def _puntos(self, linea):
        return [q for _c, q in marcas.marcas_de_linea(linea) if "punto medio" in q]

    def test_el_separador_del_titulo_no_cuenta(self):
        self.assertEqual([], self._puntos(u"## 09 · Control de versiones"))

    def test_tampoco_en_el_titulo_de_una_fase(self):
        self.assertEqual([], self._puntos(u"# Fase A · lo que hace"))

    def test_ni_con_varios_separadores(self):
        self.assertEqual([], self._puntos(u"### 2 · Puntuación · y tipografía"))

    def test_en_prosa_sigue_contando(self):
        """**El límite.** Fuera de un encabezado, el punto medio entre frases
        sigue siendo lo que el anexo llama adorno."""
        self.assertEqual(1, len(self._puntos(u"Se hace esto · y después lo otro.")))

    def test_la_cita_sigue_sin_contar_en_prosa(self):
        self.assertEqual([], self._puntos(u"Lo dice `20·M4` y no se discute."))

    def test_un_punto_medio_de_adorno_en_un_encabezado_no_se_salva(self):
        """Se exime **el separador**, no el carácter: pegado, sin espacios, no
        es la notación de la casa."""
        self.assertEqual(1, len(self._puntos(u"## Algo·pegado")))


class LaNotacionNoEsAdorno(unittest.TestCase):
    """`CA-03` · Lo que el anexo nunca llamó marca, y el programa contaba igual.

    **Cada caso va con su pareja.** La misma forma en su versión de notación y
    en su versión de prosa. Sin la pareja, una expresión que se pasa de ancha
    deja de contar adorno de verdad y nadie se entera: la regla queda escrita y
    sin quien la haga cumplir.
    """

    def _cuantas(self, linea, clase):
        return len([c for c, _ in marcas.marcas_de_linea(linea) if c == clase])

    # ── el título y el nombre de una sección no son un inciso ────────────

    def test_cp001_el_titulo_con_raya_no_cuenta(self):
        self.assertEqual(0, self._cuantas(u"# EP-000 — «Título de la épica»", "raya"))
        self.assertEqual(0, self._cuantas(u"## 1. Necesidad — en una frase", "raya"))

    def test_cp005_el_inciso_en_prosa_sigue_contando(self):
        self.assertEqual(2, self._cuantas(
            u"El plan —que ya estaba— se aprobó ayer.", "raya"))

    # ── el identificador y lo que enuncia ────────────────────────────────

    def test_cp002_el_identificador_con_su_enunciado_no_cuenta(self):
        self.assertEqual(0, self._cuantas(
            u"- [ ] **CAE-01** — «Resultado observable a nivel de negocio»", "raya"))

    def test_cp006_una_negrita_seguida_de_un_inciso_sigue_contando(self):
        """Se descuenta **una** raya, la del enunciado. Las demás son incisos.

        La línea trae tres: la que separa el identificador de lo que enuncia, y
        las dos del inciso. Quedan dos.
        """
        self.assertEqual(2, self._cuantas(
            u"**CAE-01** — el resultado —que ya se midió— queda acá", "raya"))

    # ── una celda de tabla es un dato, no un párrafo ─────────────────────

    def test_cp003_la_celda_de_tabla_no_cuenta(self):
        self.assertEqual(0, self._cuantas(u"| Fase 1 — MVP | HU-001 |", "raya"))
        self.assertEqual(0, self._cuantas(u"| enlace · cuando se ejecute | x |",
                                          "punto-medio"))

    def test_cp007_el_punto_medio_entre_frases_sigue_contando(self):
        self.assertEqual(1, self._cuantas(u"Se hace esto · y después lo otro.",
                                          "punto-medio"))

    # ── el rótulo de un campo no es una viñeta de prosa ──────────────────

    def test_cp004_el_campo_con_su_hueco_no_cuenta(self):
        self.assertEqual(0, self._cuantas(
            u"- **Objetivo:** «qué se logra cuando esto esté hecho»", "vineta"))

    def test_cp004b_el_campo_cuyo_valor_iba_en_codigo_tampoco(self):
        """`- **Slug:** `«x»`` llega acá sin el código, con el valor vacío."""
        self.assertEqual(0, self._cuantas(u"- **Slug del módulo:** ", "vineta"))

    def test_cp008_la_misma_vineta_con_prosa_sigue_contando(self):
        self.assertEqual(1, self._cuantas(
            u"- **Objetivo:** dejar el módulo andando antes del viernes", "vineta"))
