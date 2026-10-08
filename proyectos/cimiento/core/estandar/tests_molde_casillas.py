# -*- coding: utf-8 -*-
"""`EP-027·HU-001` · CP-002: cada regla del estándar se lee en casillas y se vuelve a armar igual."""
from collections import Counter

from django.test import SimpleTestCase, TestCase

from core.comun import Proyecto as Carpeta

from . import molde
from .importar import importar
from .models import Documento

# Las que el molde ordena distinto (F8 traía la excepción después del ejemplo) o
# que traían la raya repetida (D5, G5, G7): mismo contenido, en el orden del molde.
REORDENADAS = {"F8", "D5", "G5", "G7"}


def _renglones(texto):
    return [l for l in texto.replace("\r\n", "\n").split("\n") if l.strip()]


class TodasLasReglasVanYVuelven(TestCase):

    @classmethod
    def setUpTestData(cls):
        importar(Carpeta.estandar())

    def test_todas_dan_el_mismo_texto(self):
        vistas, distintas = 0, []
        for d in Documento.objects.filter(ruta__startswith="base/").exclude(ruta__startswith="base/reglas-por-tarea/"):
            texto = d.contenido.replace("\r\n", "\n")
            for inicio, fin, codigo in molde.partir(texto):
                vistas += 1
                antes, despues = _renglones(texto[inicio:fin]), _renglones(molde.normalizar(texto[inicio:fin]))
                if codigo in REORDENADAS:
                    sin_raya = lambda r: Counter(l for l in r if l.strip() != "---")
                    if sin_raya(antes) != sin_raya(despues):
                        distintas.append(codigo)
                elif antes != despues:
                    distintas.append(codigo)
        self.assertGreaterEqual(vistas, 269)
        self.assertEqual([], distintas)


F8 = """## F8 · Edita solo los archivos que el plan aprobado declara

Durante la ejecución, toca solo los archivos que el plan aprobado nombra (depende de [`02·F4`](F4-x.md)).

**Excepción** — una herramienta que bloquea se corrige sin análisis (condición); solo esa herramienta (límite); lo autoriza el usuario con «corrija» (autoriza).

```
INCORRECTO: tocar un archivo que el plan no nombra
CORRECTO:   parar y proponer
            el archivo
```

**Quién la hace cumplir:** `validadores/freno.py`, que detiene la escritura.

**Aplica a:** cambiar-codigo, escribir-documento

**Autoriza escribir:** `historico-chat/*.md`

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist](x.md) contra **v2.5.0**, el **2026-08-07**.

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — fila 16.

**Corregida el 2026-08-22.**

> Vale mientras el texto de arriba no cambie."""


class CadaParteEnSuCasilla(SimpleTestCase):
    """CP-002, paso 2."""

    def setUp(self):
        self.c = molde.leer(F8)

    def test_las_casillas(self):
        self.assertEqual("F8", self.c["codigo"])
        self.assertEqual("Edita solo los archivos que el plan aprobado declara", self.c["titulo"])
        self.assertTrue(self.c["exigencia"].startswith("Durante la ejecución"))
        self.assertTrue(self.c["excepcion"].startswith("**Excepción**"))
        self.assertIn("freno.py", self.c["quien_cumple"])
        self.assertEqual("cambiar-codigo, escribir-documento", self.c["aplica_a"])
        self.assertIn("historico-chat", self.c["autoriza_escribir"])
        self.assertTrue(self.c["sello"].startswith("### Checklist"))
        self.assertEqual(F8, molde.armar(self.c))

    def test_las_partes_menores(self):
        self.assertEqual(("tocar un archivo que el plan no nombra", "parar y proponer\nel archivo"),
                         molde.par_del_ejemplo(self.c["ejemplo"]))
        self.assertEqual(("una herramienta que bloquea se corrige sin análisis", "solo esa herramienta",
                          "lo autoriza el usuario con «corrija»"), molde.partes_de_la_excepcion(self.c["excepcion"]))
        resultado, version, fecha, observacion = molde.sello_de(self.c["sello"])
        self.assertEqual(("CUMPLE", "2.5.0", "2026-08-07"), (resultado, version, fecha))
        self.assertIn("Corregida el 2026-08-22", observacion)
        self.assertEqual([(molde.DEPENDE, "02", "F4")], molde.dependencias(self.c["exigencia"]))
        self.assertEqual(["cambiar-codigo", "escribir-documento"], molde.tareas(self.c["aplica_a"]))

    def test_la_marca(self):
        c = molde.leer("## N1 · No toques nada `[BLINDADA]`\n\nNada.")
        self.assertEqual((molde.BLINDADA, "No toques nada"), (c["marca"], c["titulo"]))
        c = molde.leer("## S7 · Vieja  ·  `[DEROGADA en 23.17.0 → ver 10·DEP3]`\n\nYa no.")
        self.assertEqual(molde.DEROGADA, c["marca"])
        self.assertEqual("## S7 · Vieja  ·  `[DEROGADA en 23.17.0 → ver 10·DEP3]`\n\nYa no.", molde.armar(c))
