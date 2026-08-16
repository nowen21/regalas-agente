"""El marcador se resuelve contra el estándar, no contra la raíz que se valida.

Fase `A-EP-004-HU-005-el-marcador-se-resuelve-contra-el-estandar`, casos CP-001
a CP-004.

**Qué se comprueba.** Un `.md` que cita una regla con `«RUTA-ESTANDAR»/base/…`
tiene que dar el mismo veredicto se corra desde donde se corra. Los enganches
llaman a este programa desde la carpeta del estándar y le pasan el proyecto
como `--raiz`, así que la raíz que se valida **no** es el estándar: si el
marcador se resolviera contra ella, buscaría `<proyecto>/base/…`, que nunca
existe — el instalador no copia `base/` a ningún proyecto, lo engancha por ruta
absoluta.

El resultado esperado no sale de correr el programa: sale de mirar si el
archivo citado existe en disco, que es una fuente independiente.

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

import enlaces  # noqa: E402

# Una regla que existe de verdad, y una que no. La primera se comprueba contra
# el disco en cada caso: si algún día se renombra, la prueba lo dice en vez de
# pasar por casualidad.
REGLA_QUE_EXISTE = "base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md"
REGLA_INVENTADA = "base/02-flujo-de-trabajo/reglas/F99-esta-regla-no-existe.md"


class MarcadorResuelveIgualDesdeCualquierRaiz(unittest.TestCase):

    nombre_carpeta = "proyecto de prueba"

    def setUp(self):
        self.temporal = tempfile.mkdtemp(prefix="cimiento-enlaces-")
        self.proyecto = os.path.join(self.temporal, self.nombre_carpeta)
        os.makedirs(self.proyecto)

    def tearDown(self):
        shutil.rmtree(self.temporal, ignore_errors=True)

    def _escribir(self, destino):
        """Deja un .md en el proyecto de prueba citando `destino`."""
        archivo = os.path.join(self.proyecto, "cita.md")
        with io.open(archivo, "w", encoding="utf-8", newline="\n") as f:
            f.write("# Cita de prueba\n\n"
                    f"Ver [la regla]({enlaces.MARCADOR_RAIZ}/{destino}).\n")
        return archivo

    def _rotos(self, raiz):
        return [h for h in enlaces.validar_enlaces(raiz) if "cita.md" in str(h)]

    def test_cp_001_el_mismo_enlace_da_el_mismo_veredicto(self):
        """CP-001 · una cita que resuelve no se reporta desde ninguna raíz."""
        # El resultado esperado sale del disco, no del programa que se prueba.
        self.assertTrue(
            os.path.isfile(os.path.join(enlaces.ESTANDAR, REGLA_QUE_EXISTE)),
            f"la regla de referencia ya no está en {REGLA_QUE_EXISTE}")

        self._escribir(REGLA_QUE_EXISTE)

        desde_el_proyecto = self._rotos(self.proyecto)
        self.assertEqual(
            desde_el_proyecto, [],
            "se reportó como roto un enlace que resuelve: "
            f"{[str(h) for h in desde_el_proyecto]}")

    def test_cp_002_el_marcador_que_no_resuelve_se_reporta(self):
        """CP-002 · el arreglo no puede volverse una excusa para callar."""
        self.assertFalse(
            os.path.isfile(os.path.join(enlaces.ESTANDAR, REGLA_INVENTADA)),
            "la regla inventada existe; hay que cambiarla en la prueba")

        self._escribir(REGLA_INVENTADA)

        self.assertEqual(
            len(self._rotos(self.proyecto)), 1,
            "no se reportó el enlace que no resuelve")

    def test_cp_003_la_raiz_validada_no_cambia_el_veredicto(self):
        """CP-003 · la misma cita, comprobada desde dos raíces distintas.

        Es el caso que falla con el código anterior: desde el proyecto se
        buscaba `<proyecto>/base/…` y el enlace bueno salía roto.
        """
        self._escribir(REGLA_QUE_EXISTE)

        # La segunda raíz es la carpeta de arriba: contiene el mismo .md y no
        # es el estándar, igual que un proyecto cualquiera.
        desde_el_proyecto = self._rotos(self.proyecto)
        desde_mas_arriba = self._rotos(self.temporal)

        self.assertEqual([str(h) for h in desde_el_proyecto],
                         [str(h) for h in desde_mas_arriba],
                         "el veredicto cambió según desde dónde se corrió")
        self.assertEqual(desde_el_proyecto, [])


class MarcadorEnRutaConTildes(MarcadorResuelveIgualDesdeCualquierRaiz):
    """CP-004 · lo mismo, con espacios y tilde en el nombre de la carpeta."""

    nombre_carpeta = "proyecto de prueba ñ"


if __name__ == "__main__":
    unittest.main()
