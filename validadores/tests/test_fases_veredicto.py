"""Una fase no puede tener dos veredictos distintos.

Fase `A-EP-004-HU-014-comparar-los-dos-veredictos`, casos CP-001 a CP-004.

**Qué se comprueba.** El veredicto de una fase se escribe dos veces a mano: en
el §6 del `resultado_pruebas` y en el `estado-fase`. El segundo es el que se
mira para pasar la puerta de verificación, así que si dice «cumple» la fase pasa
sin que nadie abra el primero — que es donde está la verdad. Ya pasó una vez, en
`A-EP-003-HU-010`: el resultado decía **No cumple** y el estado-fase seguía
diciendo «aprobada con una prueba pendiente».

El caso original ya se corrigió, así que la contradicción se reconstruye de
mentira: una prueba no puede depender de que alguien vuelva a romper algo.

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

import fases  # noqa: E402


def _resultado(concepto="Cumple", cumplidos=3, total=3, rnf="Sí"):
    return f"""# Resultado de Pruebas — fase de mentira

## 5. Veredicto por criterio

| Exigencia | Casos | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Salió bien | Sí |
| RNF-01 | CP-002 | Lo que haya salido | {rnf} |

## 6. Veredicto de la fase

| Campo | Valor |
|---|---|
| **Concepto** | **{concepto}** |
| **CA cumplidos** | {cumplidos} de {total} |
"""


def _estado(concepto="Cumple", cumplidos=3, total=3):
    return f"""# Estado de fase — fase de mentira

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **{concepto}** |
| **CA cumplidos** | {cumplidos} de {total} |
"""


class UnSoloVeredictoPorFase(unittest.TestCase):

    def setUp(self):
        self.temporal = tempfile.mkdtemp(prefix="cimiento-veredicto-")
        self.fase = os.path.join(self.temporal, "A-EP-001-HU-001-una-fase")
        os.makedirs(self.fase)

    def tearDown(self):
        shutil.rmtree(self.temporal, ignore_errors=True)

    def _escribir(self, resultado=None, estado=None):
        if resultado is not None:
            self._archivo("resultado_pruebas.md", resultado)
        if estado is not None:
            self._archivo("estado-fase.md", estado)

    def _archivo(self, nombre, texto):
        with io.open(os.path.join(self.fase, nombre), "w",
                     encoding="utf-8", newline="\n") as f:
            f.write(texto)

    def _hallazgos(self):
        return fases.veredicto(self.fase, "fase de prueba")

    def test_cp_001_dos_veredictos_distintos_se_reportan(self):
        """CP-001 · el caso que destapó el pendiente 28."""
        self._escribir(_resultado(), _estado())
        self.assertEqual(self._hallazgos(), [], "reportó una fase coherente")

        self._escribir(resultado=_resultado(concepto="No cumple"))
        hallazgos = [h for h in self._hallazgos() if "no coinciden" in str(h)]
        self.assertEqual(len(hallazgos), 1, "no reportó la contradicción")

        texto = str(hallazgos[0])
        self.assertIn("no cumple", texto, "no dice qué dice el resultado")
        self.assertIn("estado-fase", texto, "no nombra los dos documentos")

        self._escribir(estado=_estado(concepto="No cumple"))
        self.assertEqual([h for h in self._hallazgos() if "no coinciden" in str(h)],
                         [], "siguió reportando con los dos ya iguales")

    def test_cp_002_criterio_en_no_con_la_fase_dada_por_cumplida(self):
        """CP-002 · la puerta no se pasa con una exigencia en No."""
        self._escribir(_resultado(rnf="No"), _estado())

        hallazgos = [h for h in self._hallazgos() if "en No" in str(h)]
        self.assertEqual(len(hallazgos), 1, "dejó pasar un requisito en No")
        self.assertIn("RNF-01", str(hallazgos[0]), "no nombra la exigencia")

        self._escribir(resultado=_resultado(rnf="Sí"))
        self.assertEqual([h for h in self._hallazgos() if "en No" in str(h)], [])

    def test_cp_003_el_conteo_que_no_cuadra(self):
        """CP-003 · los dos documentos no pueden contar cosas distintas."""
        self._escribir(_resultado(cumplidos=3), _estado(cumplidos=2))

        hallazgos = [h for h in self._hallazgos() if "conteo" in str(h)]
        self.assertEqual(len(hallazgos), 1, "no reportó el conteo distinto")
        self.assertIn("3 de 3", str(hallazgos[0]))
        self.assertIn("2 de 3", str(hallazgos[0]))

        self._escribir(estado=_estado(cumplidos=3))
        self.assertEqual([h for h in self._hallazgos() if "conteo" in str(h)], [])

    def test_cp_004_lo_que_no_hay_que_reportar(self):
        """CP-004 · los límites y el riesgo B-01, los falsos positivos."""
        # 1 · la salvedad al lado del concepto no es otro veredicto.
        self._escribir(_resultado(concepto="Cumple, con una salvedad"), _estado())
        self.assertEqual(self._hallazgos(), [],
                         "confundió una salvedad con una contradicción")

        # 2 y 3 · falta uno de los dos documentos.
        os.remove(os.path.join(self.fase, "resultado_pruebas.md"))
        self.assertEqual(self._hallazgos(), [], "se cobró sin resultado_pruebas")

        self._escribir(resultado=_resultado())
        os.remove(os.path.join(self.fase, "estado-fase.md"))
        self.assertEqual(self._hallazgos(), [], "se cobró sin estado-fase")

        # 4 · la forma vieja de escribir el concepto se reconoce igual.
        self._escribir(
            resultado=_resultado().replace("| **Concepto** | **Cumple** |",
                                           "**Concepto: Cumple.**"),
            estado=_estado())
        self.assertEqual(self._hallazgos(), [],
                         "no reconoció la forma vieja y reportó de más")

        # 5 · comprobar no modifica nada.
        antes = {n: os.path.getsize(os.path.join(self.fase, n))
                 for n in os.listdir(self.fase)}
        self._hallazgos()
        despues = {n: os.path.getsize(os.path.join(self.fase, n))
                   for n in os.listdir(self.fase)}
        self.assertEqual(antes, despues, "comprobar modificó algún documento")


if __name__ == "__main__":
    unittest.main()
