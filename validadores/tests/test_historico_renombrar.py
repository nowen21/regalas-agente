"""Renombrar una sesión deja coherente el resumen que arrastra.

Fase `B-EP-005-HU-008-renombrar-deja-el-resumen-coherente`, casos CP-001 a
CP-003.

**Qué se comprueba.** `historico.py --renombrar` mueve la transcripción, la
titula, corrige el índice y arrastra el resumen. Lo que no hacía: corregir el
enlace que ese resumen le hace de vuelta a la transcripción, que quedaba
apuntando al nombre viejo. El resultado esperado no sale de leer un texto: sale
de comprobar contra el disco que el archivo enlazado existe.

Todo corre sobre un histórico de mentira en una carpeta temporal. Nunca sobre
`historico-chat/` real (`00·N4`): renombrar mueve archivos, y esos archivos son
el registro del proyecto.

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

import historico  # noqa: E402

FECHA = "2026-01-02"
VIEJO = f"{FECHA}-sesion.md"
TEMA = "el-tema-real"
NUEVO = f"{FECHA}-{TEMA}.md"

# Otra sesión, nombrada dentro del mismo resumen. Su enlace no se toca.
AJENA = "2026-01-01-otra.md"


class RenombrarConResumen(unittest.TestCase):

    def setUp(self):
        self.temporal = tempfile.mkdtemp(prefix="cimiento-historico-")
        self.carpeta = os.path.join(self.temporal, "historico-chat")
        self.dia = os.path.join(self.carpeta, historico.RESUMENES, FECHA)
        os.makedirs(self.dia)

        self._escribir(os.path.join(self.carpeta, VIEJO),
                       f"# {FECHA} — Sesión\n\nLo que se conversó.\n")
        self._escribir(os.path.join(self.carpeta, historico.INDICE),
                       f"# Histórico\n\n- [{VIEJO}]({VIEJO}) — sesión del {FECHA}.\n")

    def tearDown(self):
        shutil.rmtree(self.temporal, ignore_errors=True)

    def _escribir(self, ruta, texto):
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)

    def _resumen(self, nombre_transcripcion, con_ajena=False):
        """Deja el resumen del día, enlazando de vuelta a la transcripción."""
        ruta = os.path.join(self.dia, nombre_transcripcion[len(FECHA) + 1:])
        texto = (f"# {FECHA} · lo que quedó\n\n"
                 f"Hallazgos de la sesión transcrita en "
                 f"[historico-chat/{nombre_transcripcion}]"
                 f"(../../{nombre_transcripcion}).\n")
        if con_ajena:
            texto += (f"\nViene de [historico-chat/{AJENA}](../../{AJENA}).\n")
        self._escribir(ruta, texto)
        return ruta

    def _leer(self, ruta):
        with io.open(ruta, encoding="utf-8") as f:
            return f.read()

    def test_cp_001_el_resumen_arrastrado_apunta_al_nombre_nuevo(self):
        """CP-001 · el enlace de vuelta queda al día, y abre."""
        viejo_resumen = self._resumen(VIEJO)
        self.assertIn(f"(../../{VIEJO})", self._leer(viejo_resumen),
                      "el resumen de partida no trae el enlace que se va a probar")

        historico.renombrar(os.path.join(self.carpeta, VIEJO), TEMA)

        nuevo_resumen = os.path.join(self.dia, f"{TEMA}.md")
        self.assertTrue(os.path.isfile(nuevo_resumen), "el resumen no se arrastró")
        self.assertFalse(os.path.exists(viejo_resumen),
                         "quedó el resumen con el nombre viejo")

        texto = self._leer(nuevo_resumen)
        self.assertIn(f"[historico-chat/{NUEVO}](../../{NUEVO})", texto,
                      "el enlace de vuelta no quedó con el nombre nuevo")
        self.assertNotIn(VIEJO, texto,
                         "quedó una mención al nombre viejo de la sesión")

        # Lo que se pide no es que el texto cambie: es que el enlace abra.
        destino = os.path.normpath(os.path.join(self.dia, "../..", NUEVO))
        self.assertTrue(os.path.isfile(destino),
                        f"el enlace apunta a algo que no está: {destino}")

    def test_cp_002_el_enlace_a_otra_sesion_no_se_toca(self):
        """CP-002 · se corrige un enlace, no todo lo que se le parezca."""
        self._resumen(VIEJO, con_ajena=True)

        historico.renombrar(os.path.join(self.carpeta, VIEJO), TEMA)

        texto = self._leer(os.path.join(self.dia, f"{TEMA}.md"))
        self.assertIn(f"[historico-chat/{NUEVO}](../../{NUEVO})", texto)
        self.assertIn(f"[historico-chat/{AJENA}](../../{AJENA})", texto,
                      "se le cambió el enlace a una sesión que no era")

    def test_cp_003_renombrar_sin_resumen_no_revienta(self):
        """CP-003 · el camino sin resumen sigue funcionando igual."""
        shutil.rmtree(os.path.join(self.carpeta, historico.RESUMENES))

        ruta = historico.renombrar(os.path.join(self.carpeta, VIEJO), TEMA)

        self.assertTrue(os.path.isfile(ruta), "no se renombró la transcripción")
        self.assertIn(f"[{NUEVO}]({NUEVO})",
                      self._leer(os.path.join(self.carpeta, historico.INDICE)),
                      "el índice no quedó apuntando al nombre nuevo")


if __name__ == "__main__":
    unittest.main()
