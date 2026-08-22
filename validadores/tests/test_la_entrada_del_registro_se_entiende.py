# -*- coding: utf-8 -*-
"""`20·M17` · La entrada del registro abre en castellano llano.

**Nace de una prueba que salió mal.** El `CA-03` de EP-002 · HU-002 exige que
una entrada del registro se entienda sin haber seguido el trabajo. Se le mostró
al usuario la entrada de la `15.2.0` y contestó **«no entendí nada»**.

Al medir las 83, **ninguna** se salvaba: 74 citan una ruta de archivo, 43 un
identificador de regla, y la que menos jerga tiene todavía trae tres palabras
que solo significan algo adentro.

**Lo que se comprueba no es que se entienda** —eso lo decide quien lee— sino
lo que la volvía ilegible: que el primer párrafo no abra con un identificador,
una ruta o las palabras de la casa.

**Y solo la entrada de la versión vigente.** `20·M10` dice que un cambio de
norma no reabre lo cerrado; reportar las 83 viejas sepultaría la única que
todavía se puede arreglar.
"""
import io
import os
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import metareglas   # noqa: E402

CABEZA = u"# Cambios del estándar\n\n"


class Registro(unittest.TestCase):

    def repo(self, version, entrada, anteriores=u""):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        with io.open(os.path.join(tmp.name, "VERSION"), "w", encoding="utf-8") as f:
            f.write(version + u"\n")
        with io.open(os.path.join(tmp.name, "CHANGELOG.md"), "w", encoding="utf-8") as f:
            f.write(CABEZA + u"## %s — 2026-08-18\n\n%s\n\n%s" % (version, entrada, anteriores))
        return tmp.name

    def hallazgos(self, *a, **k):
        return metareglas._fila_m17_entrada_llana(self.repo(*a, **k))


class LoQueSeReporta(Registro):

    def test_abrir_con_un_identificador_de_regla(self):
        h = self.hallazgos(u"1.0.0", u"**MENOR** — la fila 12 de `20·M5` pide ejemplo.")
        self.assertEqual(1, len(h))
        self.assertIn("identificador de regla", h[0].mensaje)

    def test_abrir_con_una_ruta_de_archivo(self):
        h = self.hallazgos(u"1.0.0", u"**MENOR** — columna nueva en `plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md`.")
        self.assertEqual(1, len(h))
        self.assertIn("ruta de archivo", h[0].mensaje)

    def test_abrir_con_las_palabras_de_la_casa(self):
        h = self.hallazgos(u"1.0.0", u"**MENOR** — el checklist de la fase pasa a exigirlo.")
        self.assertEqual(1, len(h))
        self.assertIn("palabras de la casa", h[0].mensaje)

    def test_el_mensaje_junta_los_motivos(self):
        """Quien lo lee tiene que saber qué sacar, no solo que algo sobra."""
        h = self.hallazgos(u"1.0.0", u"**MENOR** — `20·M5` y `plantillas/x.md`.")
        self.assertIn(" y ", h[0].mensaje)


class LoQueNoSeReporta(Registro):

    def test_la_entrada_llana_pasa(self):
        h = self.hallazgos(
            u"1.0.0",
            u"**MENOR** — al anotar que una prueba pasó ahora hay que decir con qué se probó.\n\n"
            u"Antes se anotaba solo «aprobado», y así nadie podía repetirla.")
        self.assertEqual([], h)

    def test_el_detalle_debajo_no_cuenta(self):
        """El identificador y la ruta siguen siendo bienvenidos: más abajo."""
        h = self.hallazgos(
            u"1.0.0",
            u"**MENOR** — al anotar que una prueba pasó hay que decir con qué se probó.\n\n"
            u"Antes se anotaba solo «aprobado».\n\n"
            u"**El detalle.** Lo pide `20·M5`, en `plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md`.")
        self.assertEqual([], h)

    def test_la_fecha_no_cuenta_como_parrafo(self):
        """Queda pegada al encabezado y no dice nada; contarla desplazaría la
        ventana y dejaría el primer párrafo de verdad sin mirar."""
        h = self.hallazgos(u"1.0.0", u"2026-08-18\n\n**MENOR** — `20·M5` lo pide.")
        self.assertEqual(1, len(h))

    def test_las_entradas_viejas_no_se_reportan(self):
        """`20·M10`: un cambio de norma no reabre lo cerrado. Y reportar 83
        entradas sepultaría la única que todavía se puede arreglar."""
        h = self.hallazgos(
            u"1.0.0",
            u"**MENOR** — al anotar que una prueba pasó hay que decir con qué se probó.",
            anteriores=u"## 0.9.0 — 2026-08-01\n\n**MENOR** — `20·M5` en `base/x.md`.\n")
        self.assertEqual([], h)

    def test_sin_entrada_para_la_version_no_dice_nada(self):
        """De eso ya se queja la fila 19, y dos hallazgos por lo mismo es ruido."""
        tmp = self.repo(u"1.0.0", u"llano y claro")
        with io.open(os.path.join(tmp, "VERSION"), "w", encoding="utf-8") as f:
            f.write(u"2.0.0\n")
        self.assertEqual([], metareglas._fila_m17_entrada_llana(tmp))


class ElRegistroDeEsteRepositorio(unittest.TestCase):
    """La entrada vigente, sobre el archivo de verdad.

    Se cae cuando alguien escriba la próxima empezando por una ruta — que es
    exactamente lo que se hizo en las 83 anteriores.
    """

    def test_la_entrada_vigente_abre_en_llano(self):
        h = metareglas._fila_m17_entrada_llana(metareglas.RAIZ)
        self.assertEqual([], [x.mensaje for x in h])


if __name__ == "__main__":
    unittest.main()
