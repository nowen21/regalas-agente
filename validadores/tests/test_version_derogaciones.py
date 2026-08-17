"""Con una derogación sin adoptar, el proyecto no avanza de fase (`02·F22`).

Fase `A-EP-004-HU-015-retrodocumentar-la-comprobacion-de-la-f22`, casos CP-001 a
CP-004.

**Qué se comprueba.** El código de `derogaciones`, `sin_adoptar` y
`validar_fase` se escribió el 2026-08-16 sin fase, sin plan y sin una sola
prueba: la única evidencia de que funcionaba era el relato de la sesión que lo
escribió. Esta suite es la evidencia que faltaba, y por eso corre contra las
derogaciones **reales** del estándar en vez de contra un dato inventado — si
mañana cambia la marca del encabezado, el caso lo dice en vez de pasar.

La excepción es el CP-002, que sí usa datos inventados: lo que prueba es la
aritmética del rango de versiones, y con datos reales cambiaría de significado
cada vez que se derogue una regla.

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

import flujo  # noqa: E402
import version  # noqa: E402

# Anterior a la primera derogación del estándar, que es de la 3.1.0.
ATRASADA = "3.0.0"


def _f22(hallazgos):
    """Los hallazgos que hablan de derogaciones sin adoptar, y solo esos."""
    return [h for h in hallazgos if "F22" in str(h)]


class ProyectoDeMentira(unittest.TestCase):

    def setUp(self):
        self.temporal = tempfile.mkdtemp(prefix="cimiento-f22-")
        self.proyecto = os.path.join(self.temporal, "proyecto")
        self.fase = os.path.join(
            self.proyecto, "documentacion", "epicas", "EP-001-una-epica",
            "HU-001-una-historia", "A-EP-001-HU-001-una-fase")
        os.makedirs(self.fase)

        epica = os.path.dirname(os.path.dirname(self.fase))
        self._escribir(os.path.join(epica, "epica.md"), "# EP-001\n")
        self._escribir(os.path.join(os.path.dirname(self.fase),
                                    "HU-001-una-historia.md"), "# HU-001\n")
        self._escribir(os.path.join(self.fase, "plan_trabajo.md"),
                       "# Plan de trabajo\n")
        self._declarar(ATRASADA)

    def tearDown(self):
        shutil.rmtree(self.temporal, ignore_errors=True)

    def _escribir(self, ruta, texto):
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)

    def _declarar(self, adoptada):
        """Deja el `CLAUDE.md` del proyecto declarando esa versión."""
        texto = "# Proyecto de prueba\n"
        if adoptada:
            texto += f"\nVersión del estándar adoptada: {adoptada}\n"
        self._escribir(os.path.join(self.proyecto, "CLAUDE.md"), texto)

    def test_cp_001_el_proyecto_atrasado_con_fases_falla(self):
        """CP-001 · la falla sale y nombra cada regla jubilada."""
        derogadas = version.derogaciones()
        self.assertTrue(
            derogadas,
            "el estándar no tiene ninguna regla derogada con su marca: sin ese "
            "dato el caso pasaría sin comprobar nada")

        hallazgos = _f22(version.validar_fase(self.proyecto))
        self.assertEqual(len(hallazgos), 1,
                         "el proyecto atrasado con fases no produjo la falla")

        texto = str(hallazgos[0])
        primera = derogadas[0]
        self.assertIn(primera[1], texto, "la falla no nombra la regla jubilada")
        self.assertIn(primera[0], texto, "la falla no dice en qué versión se jubiló")
        self.assertIn(primera[2].split(" y ")[0], texto,
                      "la falla no dice qué la reemplazó")

        # Y al día, calla.
        self._declarar(version.version_estandar())
        self.assertEqual(_f22(version.validar_fase(self.proyecto)), [],
                         "siguió fallando con la versión vigente declarada")

    def test_cp_002_lo_ya_adoptado_no_se_cuenta(self):
        """CP-002 · el filtro del rango, con datos inventados a propósito."""
        inventadas = [("2.0.0", "X1", "X9"),
                      ("5.0.0", "X2", "X8"),
                      ("7.0.0", "X3", "X7")]

        self.assertEqual(len(version.sin_adoptar("1.0.0", "7.0.0", inventadas)), 3,
                         "desde antes de todas, tienen que salir las tres")
        self.assertEqual([d[1] for d in version.sin_adoptar("2.0.0", "7.0.0", inventadas)],
                         ["X2", "X3"],
                         "la derogación ya adoptada se siguió contando")
        self.assertEqual(version.sin_adoptar("7.0.0", "7.0.0", inventadas), [],
                         "al día y todavía reporta")
        self.assertEqual(version.sin_adoptar(None, "7.0.0", inventadas), [],
                         "sin versión declarada no se puede decidir, y decidió")

    def test_cp_003_sin_fases_no_se_cobra(self):
        """CP-003 · la comprobación se cobra donde hay fases, y solo ahí."""
        con_fase = _f22(flujo.validar(self.proyecto))
        self.assertEqual(len(con_fase), 1,
                         "con fase, la falla tiene que salir por el recorrido de flujo")

        shutil.rmtree(self.fase)
        self.assertEqual(_f22(flujo.validar(self.proyecto)), [],
                         "sin fases se cobró igual, y F0 exceptúa ese trabajo")

    def test_cp_004_los_limites_callan_en_vez_de_romper(self):
        """CP-004 · sin CLAUDE.md y sin versión declarada: silencio, no error."""
        antes = sorted(os.listdir(self.proyecto))

        os.remove(os.path.join(self.proyecto, "CLAUDE.md"))
        self.assertEqual(version.validar_fase(self.proyecto), [],
                         "sin CLAUDE.md tendría que callar")

        self._declarar(None)
        self.assertEqual(_f22(version.validar_fase(self.proyecto)), [],
                         "sin versión declarada tendría que callar")

        self.assertEqual(sorted(os.listdir(self.proyecto)), antes,
                         "comprobar modificó el proyecto")


if __name__ == "__main__":
    unittest.main()
