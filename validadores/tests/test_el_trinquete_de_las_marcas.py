# -*- coding: utf-8 -*-
"""Pendiente 11 · El trinquete de `00·ID8`: la deuda no crece.

**Limpiar 15 000 marcas primero es hacer el trabajo dos veces.** Medido sobre
este repositorio, el 58 % de las marcas nació *después* de escribirse la regla:
mientras la llave siga abierta, lo limpiado se vuelve a llenar.

**Y bloquear todas las marcas no es una opción.** Los seis commits anteriores a
escribir esto agregaban 425 de estilo: un enganche que rechaza cada commit se
apaga en una tarde, que es el defecto más caro de esta casa.

Lo que estas pruebas fijan es el reparto que sí se sostiene: **las invisibles en
todas partes, todas las marcas en lo que se hereda, y nada más**. Y sobre todo
la prueba que suele faltar — que cuando no hay marca nueva, el programa se calla.
"""
import io
import os
import subprocess
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import marcas          # noqa: E402
from comun import FALLA, AVISO   # noqa: E402

DURO = u" "          # espacio duro: invisible, nunca a propósito
RAYA = u"—"          # raya larga: de estilo


def _git(raiz, *args):
    return subprocess.run(("git", "-C", raiz) + args, capture_output=True,
                          text=True, encoding="utf-8", errors="replace")


class Trinquete(unittest.TestCase):
    """Cada prueba arma un repositorio de verdad: el trinquete lee `git`."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        _git(self.tmp, "init", "-q")
        _git(self.tmp, "config", "user.email", "prueba@ejemplo")
        _git(self.tmp, "config", "user.name", "Prueba")

    def escribir(self, rel, texto):
        ruta = os.path.join(self.tmp, *rel.split("/"))
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)

    def commitear(self, rel, texto):
        self.escribir(rel, texto)
        _git(self.tmp, "add", rel)
        _git(self.tmp, "commit", "-q", "-m", "base", "--no-verify")

    def preparar(self, rel, texto):
        self.escribir(rel, texto)
        _git(self.tmp, "add", rel)

    def veredicto(self):
        h = marcas.validar_preparados(self.tmp)
        return [x.severidad for x in h], h

    # ── lo que bloquea ────────────────────────────────────────────────────

    def test_una_invisible_nueva_bloquea_en_cualquier_carpeta(self):
        """No se teclean a propósito y se quitan en segundos."""
        self.preparar("notas/algo.md", u"Una frase con espacio%sduro." % DURO)
        niveles, _h = self.veredicto()
        self.assertIn(FALLA, niveles)

    def test_crecer_en_lo_que_se_hereda_bloquea(self):
        """`base/` y `plantillas/` son lo que viaja a los proyectos."""
        self.commitear("base/01-algo.md", u"Un texto liso.\n")
        self.preparar("base/01-algo.md",
                      u"Un texto %s con inciso %s liso.\n" % (RAYA, RAYA))
        niveles, _h = self.veredicto()
        self.assertIn(FALLA, niveles)

    # ── lo que NO bloquea: la prueba que suele faltar ─────────────────────

    def test_la_marca_que_ya_estaba_no_bloquea(self):
        """Es un trinquete, no una limpieza: castiga crecer, no existir."""
        viejo = u"Una frase con espacio%sduro.\n" % DURO
        self.commitear("base/01-algo.md", viejo)
        self.preparar("base/01-algo.md", viejo + u"Un renglón limpio más.\n")
        niveles, hallazgos = self.veredicto()
        self.assertEqual([], niveles, "\n".join(x.mensaje for x in hallazgos))

    def test_quitar_marcas_no_bloquea(self):
        """Limpiar tiene que poder guardarse."""
        self.commitear("base/01-algo.md", u"Con espacio%sduro.\n" % DURO)
        self.preparar("base/01-algo.md", u"Con espacio duro.\n")
        niveles, _h = self.veredicto()
        self.assertEqual([], niveles)

    def test_el_estilo_fuera_de_lo_heredado_avisa_pero_deja_pasar(self):
        """425 marcas de estilo en seis commits: bloquear ahí apaga el enganche."""
        self.commitear("notas/algo.md", u"Un texto liso.\n")
        self.preparar("notas/algo.md",
                      u"Un texto %s con inciso %s liso.\n" % (RAYA, RAYA))
        niveles, _h = self.veredicto()
        self.assertEqual([AVISO], niveles)

    def test_dentro_de_un_bloque_cercado_no_cuenta(self):
        """Ahí las marcas son el ejemplo de lo que no hay que hacer."""
        self.commitear("base/01-algo.md", u"Un texto liso.\n")
        self.preparar("base/01-algo.md",
                      u"Un texto liso.\n\n```\nasi%sno %s se escribe\n```\n"
                      % (DURO, RAYA))
        niveles, hallazgos = self.veredicto()
        self.assertEqual([], niveles, "\n".join(x.mensaje for x in hallazgos))

    def test_el_historico_esta_exento(self):
        """Es transcripción literal: no se reescribe, así que no es deuda."""
        self.preparar("historico-chat/2026-08-19/algo.md",
                      u"Dijo: espacio%sduro %s así.\n" % (DURO, RAYA))
        niveles, _h = self.veredicto()
        self.assertEqual([], niveles)

    def test_sin_nada_preparado_no_dice_nada(self):
        """Un enganche que habla cuando no hay nada enseña a no leerlo."""
        self.commitear("base/01-algo.md", u"Un texto liso.\n")
        niveles, _h = self.veredicto()
        self.assertEqual([], niveles)

    def test_renombrar_no_cuenta_las_marcas_viejas(self):
        """Un `git mv` no agrega marcas: la línea base sigue al archivo.

        Pasó el 2026-08-21: mover 11 moldes a su carpeta hizo que el trinquete
        les pusiera línea base cero y contara como nuevas todas sus rayas.
        """
        self.commitear("plantillas/algo.md",
                       u"Un texto %s con inciso %s viejo.\n" % (RAYA, RAYA))
        _git(self.tmp, "mv", "plantillas/algo.md", "plantillas/ciclo/algo.md")
        niveles, hallazgos = self.veredicto()
        self.assertEqual([], niveles,
                         "\n".join(x.mensaje for x in hallazgos))

    def test_renombrar_y_agregar_marca_si_cuenta(self):
        """Lo que el trinquete mira es el crecimiento, también tras un `mv`."""
        self.commitear("plantillas/algo.md", u"Un texto %s viejo.\n" % RAYA)
        _git(self.tmp, "mv", "plantillas/algo.md", "plantillas/ciclo/algo.md")
        self.preparar("plantillas/ciclo/algo.md",
                      u"Un texto %s viejo %s y una raya nueva.\n"
                      % (RAYA, RAYA))
        niveles, _h = self.veredicto()
        self.assertEqual([FALLA], niveles)


if __name__ == "__main__":
    unittest.main()
