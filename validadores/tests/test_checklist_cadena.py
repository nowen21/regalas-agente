"""La revisión de la instalación ve la cadena de `02·F0`.

Fase `A-EP-007-HU-007-la-revision-ve-la-cadena`, casos CP-001 a CP-003.

**Qué se comprueba.** Un proyecto puede tener los trece componentes puestos,
código commiteado, `prompts/` sin un solo planteamiento, ninguna épica y
ninguna historia — y la revisión decía «13 de 13, instalación completa». Pasó
en `shopnest-mesa`, y lo notó el usuario preguntando, no el estándar.

Lo que se mira no es una función suelta sino el conjunto: lo que falló fue el
**resumen**, no una comprobación.

Todo corre sobre proyectos de mentira en carpetas temporales (`00·N4`).

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

import checklist  # noqa: E402

PUNTO = "cadena"


class LaRevisionVeLaCadena(unittest.TestCase):

    def setUp(self):
        self.temporal = tempfile.mkdtemp(prefix="cimiento-cadena-")
        self.proyecto = os.path.join(self.temporal, "proyecto")
        for carpeta in ("prompts", "proyectos",
                        os.path.join("documentacion", "epicas")):
            os.makedirs(os.path.join(self.proyecto, *carpeta.split(os.sep)))

    def tearDown(self):
        shutil.rmtree(self.temporal, ignore_errors=True)

    def _con_codigo(self):
        ruta = os.path.join(self.proyecto, "proyectos", "app.py")
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write("# código que ya se commiteó\n")

    def _con_planteamiento(self):
        ruta = os.path.join(self.proyecto, "prompts", "mesas-planteamiento.md")
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write("# Planteamiento\n\nLo que el negocio quiere resolver.\n")

    def _con_epica(self):
        os.makedirs(os.path.join(self.proyecto, "documentacion", "epicas",
                                 "EP-001-una-epica"))

    def _punto(self):
        """El punto de la cadena dentro de la revisión completa."""
        for p in checklist.revisar(self.proyecto):
            if p.id == PUNTO:
                return p
        return None

    def test_cp_001_la_cadena_vacia_se_nombra(self):
        """CP-001 · sale como faltante, con el detalle y el arreglo."""
        self._con_codigo()

        punto = self._punto()
        self.assertIsNotNone(
            punto, "el punto de la cadena no está en la lista de componentes")
        self.assertFalse(punto.cumple,
                         "un proyecto con código y sin planteamiento pasó en verde")
        self.assertIn("planteamiento", punto.detalle,
                      "el detalle no dice qué falta")
        self.assertIn("instalador", punto.arreglo,
                      "no dice que este punto no lo pone el instalador")

        # Lo que de verdad falló en shopnest-mesa: el resumen.
        #
        # No se busca «completa» a secas: «incompleta» la contiene, y el caso
        # daba rojo contra un resumen correcto. Se busca la frase entera.
        resumen = checklist.resumen(self.proyecto, checklist.revisar(self.proyecto))
        self.assertNotIn("instalación completa", resumen.lower(),
                         f"el resumen sigue diciendo que está completa: {resumen}")
        self.assertIn("de 14", resumen,
                      f"el punto nuevo no entró en la cuenta: {resumen}")

    def test_cp_002_el_punto_se_apaga_al_escribir_el_planteamiento(self):
        """CP-002 · el silencio significa que la cadena arrancó."""
        self._con_codigo()
        self.assertFalse(self._punto().cumple)

        self._con_planteamiento()
        self._con_epica()

        self.assertTrue(self._punto().cumple,
                        f"siguió reportando: {self._punto().detalle}")

    def test_cp_003_la_epica_solo_se_exige_si_hay_codigo(self):
        """CP-003 · no se le pide épica a un proyecto que no ha construido nada."""
        self._con_planteamiento()

        self.assertTrue(
            self._punto().cumple,
            "le pidió la épica a un proyecto recién instalado, sin código")

        self._con_codigo()
        punto = self._punto()
        self.assertFalse(punto.cumple, "con código y sin épica tendría que reportar")
        self.assertIn("épica", punto.detalle)


if __name__ == "__main__":
    unittest.main()
