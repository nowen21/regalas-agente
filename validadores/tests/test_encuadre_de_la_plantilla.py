# -*- coding: utf-8 -*-
"""`EP-004 · HU-004 · CA-05` · El texto fijo de la plantilla sobrevive al llenado.

Una plantilla trae dos cosas antes de su primer separador, y son distintas. El
recuadro de citas `>` dice **cómo llenarla** y se borra. Lo que queda debajo, en
prosa, dice **cómo se usa** el documento ya llenado, y se conserva. En el molde
del planteamiento eso es el encuadre que le recuerda al agente que el documento
es insumo y no una orden de entregar código.

**Ya se perdió una vez.** El planteamiento de este repositorio se escribió con
una nota de procedencia en ese lugar, con fecha, fuentes y el número del
pendiente que cerraba, y nadie lo notó hasta que el usuario preguntó qué
aportaba ese párrafo.

**La mitad de estas pruebas son de lo que NO tiene que reprobar**, que es la que
falta siempre acá. Un validador que reprueba lo que está bien enseña a ignorar
todos los veredictos, y desde ahí ninguno sirve.
"""
import io
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import plantillas                  # noqa: E402
from comun import FALLA            # noqa: E402

# Una plantilla con las dos cosas: el recuadro que se borra y el bloque fijo que
# se conserva. El bloque cita reglas, como el del molde del planteamiento.
PLANTILLA_CON_ENCUADRE = (
    u"# Planteamiento — «Nombre»\n\n"
    u"> **Qué es este archivo.** El planteamiento de entrada.\n"
    u"> **Cómo usarlo.** Reemplazar los «…» y borrar este recuadro.\n\n"
    u"**Encuadre para el agente:** este documento dice qué se necesita. "
    u"El agente sigue el flujo `02·F1` → `02·F2` → `02·F4`. "
    u"No generar código hasta que el plan esté aprobado.\n\n"
    u"---\n\n"
    u"## 0. Identificación\n\nTexto.\n")

# Una plantilla con bloque fijo que NO cita ninguna regla. Es el caso del plan
# de trabajo, y sirve para comprobar que la exigencia sale de la plantilla.
PLANTILLA_SIN_CITAS = (
    u"# Plan de Trabajo — Fase «X»\n\n"
    u"> Plantilla del plan. Borrar esta caja.\n\n"
    u"**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, "
    u"en qué orden y sobre qué archivos.\n\n"
    u"---\n\n"
    u"## 0. Identificación\n\nTexto.\n")

# Una plantilla que no tiene bloque fijo: del título salta al separador.
PLANTILLA_SIN_ENCUADRE = (
    u"# Catálogo de módulos\n\n"
    u"> Plantilla. Borrar esta caja.\n\n"
    u"---\n\n"
    u"## 0. Identificación\n\nTexto.\n")


class EncuadreDeLaPlantilla(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def escribir(self, nombre, texto):
        ruta = os.path.join(self.tmp, nombre)
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
        return ruta

    def fallas_de_encuadre(self, documento, plantilla):
        """Solo las fallas que trae esta comprobación, no las otras cuatro."""
        doc = self.escribir("documento.md", documento)
        pla = self.escribir("plantilla.md", plantilla)
        return [h for h in plantillas.validar(doc, pla)
                if h.severidad == FALLA
                and ("texto que la plantilla fija" in h.mensaje
                     or "no cita ninguna regla" in h.mensaje)]

    # ── CP-001 · el encuadre borrado se reprueba ─────────────────────────

    def test_cp001_el_encuadre_borrado_se_reprueba(self):
        documento = (u"# Planteamiento — Cimiento\n\n"
                     u"---\n\n"
                     u"## 0. Identificación\n\nLleno.\n")
        h = self.fallas_de_encuadre(documento, PLANTILLA_CON_ENCUADRE)
        self.assertEqual(1, len(h), "borrar el encuadre tiene que reprobar")
        self.assertIn(u"Encuadre para el agente", h[0].mensaje,
                      "el mensaje dice qué había ahí, o no se sabe qué reponer")

    # ── CP-002 · el encuadre adaptado NO se reprueba ─────────────────────

    def test_cp002_el_encuadre_reescrito_mas_corto_pasa(self):
        documento = (u"# Planteamiento — Cimiento\n\n"
                     u"**Para el agente:** este documento dice qué se necesita "
                     u"y qué no se negocia. La cadena de `02·F0` no salta "
                     u"eslabones.\n\n"
                     u"---\n\n"
                     u"## 0. Identificación\n\nLleno.\n")
        self.assertEqual([], self.fallas_de_encuadre(documento,
                                                     PLANTILLA_CON_ENCUADRE),
                         "adaptar la redacción del encuadre es legal")

    # ── CP-003 · el encuadre reemplazado por procedencia se reprueba ─────

    def test_cp003_la_nota_de_procedencia_en_el_lugar_del_encuadre_se_reprueba(self):
        documento = (u"# Planteamiento — Cimiento\n\n"
                     u"**Encuadre.** Este es el planteamiento de Cimiento "
                     u"mismo. Se escribió el 2026-08-22 con lo que el proyecto "
                     u"ya tenía dicho. Cierra el pendiente 56.\n\n"
                     u"---\n\n"
                     u"## 0. Identificación\n\nLleno.\n")
        h = self.fallas_de_encuadre(documento, PLANTILLA_CON_ENCUADRE)
        self.assertEqual(1, len(h), "es el caso que ya ocurrió y no se detectó")
        self.assertIn(u"no cita ninguna regla", h[0].mensaje)

    # ── CP-004 · plantilla sin bloque fijo no exige ninguno ──────────────

    def test_cp004_plantilla_sin_encuadre_no_exige_encuadre(self):
        documento = (u"# Catálogo de módulos\n\n"
                     u"---\n\n"
                     u"## 0. Identificación\n\nLleno.\n")
        self.assertEqual([], self.fallas_de_encuadre(documento,
                                                     PLANTILLA_SIN_ENCUADRE),
                         "no se pide lo que la plantilla no pone")

    # ── CP-005 · plantilla sin citas no le exige citas al documento ──────

    def test_cp005_plantilla_sin_citas_no_exige_citas(self):
        documento = (u"# Plan de Trabajo — Fase B-EP-004-HU-004\n\n"
                     u"**Para qué sirve este documento.** Dice qué se va a "
                     u"hacer en esta fase y sobre qué archivos.\n\n"
                     u"---\n\n"
                     u"## 0. Identificación\n\nLleno.\n")
        self.assertEqual([], self.fallas_de_encuadre(documento,
                                                     PLANTILLA_SIN_CITAS),
                         "la exigencia de citar sale de la plantilla, no del programa")

    # ── lo que sostiene el diseño: se identifica por posición ────────────

    def test_el_recuadro_de_instrucciones_no_es_el_bloque_fijo(self):
        fijo = plantillas.bloque_fijo(PLANTILLA_CON_ENCUADRE)
        self.assertEqual(1, len(fijo), "las líneas `>` son el recuadro que se borra")
        self.assertIn(u"Encuadre para el agente", fijo[0][1])

    def test_el_bloque_fijo_termina_en_el_primer_encabezado_si_no_hay_separador(self):
        texto = (u"# Título\n\n"
                 u"**Para el agente:** instrucción con `02·F0`.\n\n"
                 u"## 0. Identificación\n\n"
                 u"Esto ya es cuerpo del documento y no encuadre.\n")
        fijo = plantillas.bloque_fijo(texto)
        self.assertEqual(1, len(fijo),
                         "sin separador, la cabecera termina en el primer `##`")


if __name__ == "__main__":
    unittest.main()
