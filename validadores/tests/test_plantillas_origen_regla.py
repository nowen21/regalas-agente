"""Una regla de negocio sin procedencia se reporta.

Fase `A-EP-004-HU-004-la-regla-de-negocio-declara-su-origen`, casos CP-001 a
CP-003.

**Qué se comprueba.** Desde la v22.0.0 el §4 del modelo de especificación pide
de dónde baja cada regla de negocio, no solo por qué existe. Esta suite
comprueba que una regla sin ese dato se reporte.

Los datos son el caso real que lo destapó, en `shopnest-mesa`: dos reglas que
dicen casi lo mismo, y solo una baja de algún lado. La que no bajaba de nada
llegó hasta un criterio de aceptación y tardó un día en verse, solo porque
alguien preguntó de dónde salía.

Cómo se corre:

    python -m unittest discover -s validadores/tests
"""

import io
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import plantillas  # noqa: E402

CON_ORIGEN = ("«Un problema registra causa raíz y solución definitiva — RF-13 — "
              "para que quien lo lea después sepa por qué pasaba.»")
SIN_ORIGEN = ("«Un problema no se cierra sin causa raíz ni solución definitiva — "
              "porque cerrar es afirmar que ya no vuelve.»")


def _spec(reglas):
    """Una especificación de mentira con ese §4."""
    cuerpo = "\n".join(f"{i}. {r}" for i, r in enumerate(reglas, 1))
    return ("# Especificación del módulo Problemas\n\n"
            "## 3. Alcance\n\nLo que hace el módulo.\n\n"
            "## 4. Reglas de negocio\n\n"
            f"{cuerpo}\n\n"
            "## 5. Modelo de datos\n\nLas tablas.\n")


class ReglaDeNegocioSinOrigen(unittest.TestCase):

    def setUp(self):
        self.temporal = tempfile.mkdtemp(prefix="cimiento-origen-")
        self.plantilla = plantillas._ruta(plantillas.SPEC_MODULO)

    def tearDown(self):
        shutil.rmtree(self.temporal, ignore_errors=True)

    def _archivo(self, nombre, texto):
        ruta = os.path.join(self.temporal, nombre)
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
        return ruta

    def _fallas(self, texto, nombre="spec.md"):
        ruta = self._archivo(nombre, texto)
        return [h for h in plantillas.validar(ruta, self.plantilla)
                if "de dónde baja" in str(h)]

    def test_cp_001_la_regla_sin_origen_se_reporta(self):
        """CP-001 · sale una falla, y por la regla que es."""
        fallas = self._fallas(_spec([CON_ORIGEN, SIN_ORIGEN]))
        self.assertEqual(len(fallas), 1,
                         f"se esperaba una sola falla: {[str(h) for h in fallas]}")

        texto = str(fallas[0])
        self.assertIn("no se cierra", texto, "señaló la regla que no era")
        self.assertIn("se sube a la historia", texto,
                      "la falla no dice qué hacer con la regla")

        # Con origen, calla.
        arreglada = SIN_ORIGEN.replace("— porque", "— D-22 — porque")
        self.assertEqual(self._fallas(_spec([CON_ORIGEN, arreglada])), [],
                         "siguió reportando una regla que ya dice de dónde baja")

    def test_cp_002_lo_que_no_hay_que_reportar(self):
        """CP-002 · los cuatro casos donde tiene que callar."""
        molde = "«Regla — de dónde baja (el identificador del requisito, la historia o la decisión) — por qué existe.»"
        self.assertEqual(self._fallas(_spec([molde, "«…»"])), [],
                         "reportó el molde sin llenar, que ya reporta otra comprobación")

        self.assertEqual(self._fallas(_spec([])), [],
                         "reportó una sección sin ninguna regla")

        con_codigo = ("«El estado del problema usa el catálogo ESTADOS-PROB — RF-13 — "
                      "para no quemarlo en código.»")
        self.assertEqual(self._fallas(_spec([con_codigo])), [],
                         "se confundió con un código dentro del texto de la regla")

        # Un documento que no es especificación, con una sección así.
        otro = self._archivo("dominio.md", _spec([SIN_ORIGEN]))
        otra_plantilla = plantillas._ruta("plantillas/dominio.md")
        fallas = [h for h in plantillas.validar(otro, otra_plantilla)
                  if "de dónde baja" in str(h)]
        self.assertEqual(fallas, [],
                         "miró las reglas de un documento que no es una especificación")

    def test_cp_003_una_especificacion_se_compara_contra_su_plantilla(self):
        """CP-003 · sin esto, la comprobación no se dispararía nunca."""
        ruta = self._archivo("spec.md", _spec([SIN_ORIGEN]))
        deducida = plantillas.deducir_plantilla(ruta, _spec([SIN_ORIGEN]))

        self.assertIsNotNone(deducida, "un spec.md no se reconoce como especificación")
        self.assertEqual(os.path.normpath(deducida), self.plantilla)
        self.assertTrue(os.path.isfile(deducida),
                        f"la plantilla de especificación no está en {deducida}")


if __name__ == "__main__":
    unittest.main()
