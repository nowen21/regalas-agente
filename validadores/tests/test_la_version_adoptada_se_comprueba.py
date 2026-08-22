# -*- coding: utf-8 -*-
"""`82` · La versión que un proyecto declara se comprueba contra algo.

Antes no se comprobaba contra nada. Un proyecto podía escribir cualquier número
en su `CLAUDE.md`, y **si era mayor que la vigente, el programa concluía que
estaba al día y dejaba de avisar del desfase**. La comprobación se apagaba sola
con un número inventado, y el que la apagaba no se enteraba.

Y había un segundo hueco: el instalador deja constancia de cada actualización en
`documentacion/versiones/`, y nadie comparaba esa constancia con lo declarado.
Cuando se buscó, la contradicción ya estaba: un proyecto real declaraba `27.2.0`
y su historial decía `28.0.0`, los dos del mismo día.

**La mitad de estas pruebas son de lo que NO debe fallar.** Una comprobación de
versión que reprueba a un proyecto bien declarado se apaga a la semana.
"""
import io
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import version                     # noqa: E402
from comun import AVISO, FALLA     # noqa: E402


class LaVersionAdoptadaSeComprueba(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self._publicadas = version.versiones_publicadas
        self._estandar = version.version_estandar
        version.versiones_publicadas = lambda raiz=None: {"1.0.0", "2.0.0", "3.0.0"}
        version.version_estandar = lambda: "3.0.0"

    def tearDown(self):
        version.versiones_publicadas = self._publicadas
        version.version_estandar = self._estandar
        shutil.rmtree(self.tmp, ignore_errors=True)

    def proyecto(self, adoptada, adopciones=()):
        with io.open(os.path.join(self.tmp, "CLAUDE.md"), "w",
                     encoding="utf-8", newline="\n") as f:
            f.write(u"# Proyecto\n\n- **Versión del estándar adoptada:** "
                    u"`%s` · sellada `2026-08-20`.\n" % adoptada)
        if adopciones:
            carpeta = os.path.join(self.tmp, "documentacion", "versiones")
            os.makedirs(carpeta)
            for v in adopciones:
                with io.open(os.path.join(carpeta, "2026-08-20-%s.md" % v), "w",
                             encoding="utf-8", newline="\n") as f:
                    f.write(u"# Actualización a %s\n" % v)
        return version.validar(self.tmp)

    def fallas(self, hallazgos):
        return [h for h in hallazgos if h.severidad == FALLA]

    # ── lo que sí tiene que fallar ───────────────────────────────────────

    def test_una_version_que_no_existe_falla(self):
        h = self.fallas(self.proyecto("99.9.9"))
        self.assertEqual(1, len(h))
        self.assertIn(u"no existe en el registro", h[0].mensaje)

    def test_la_version_inventada_ya_no_apaga_el_aviso(self):
        """El corazón del defecto: `99.9.9` es mayor que la vigente, así que
        el desfase callaba. Ahora hay una falla, aunque el aviso siga callado."""
        hallazgos = self.proyecto("99.9.9")
        self.assertTrue(self.fallas(hallazgos),
                        "un número inventado no puede pasar en silencio")

    def test_declarada_y_ultimo_registro_que_difieren_falla(self):
        h = self.fallas(self.proyecto("1.0.0", adopciones=["1.0.0", "2.0.0"]))
        self.assertEqual(1, len(h))
        self.assertIn(u"1.0.0", h[0].mensaje)
        self.assertIn(u"2.0.0", h[0].mensaje,
                      "el mensaje nombra las dos, porque no se sabe cuál está mal")

    # ── lo que NO tiene que fallar ───────────────────────────────────────

    def test_un_proyecto_al_dia_no_falla(self):
        self.assertEqual([], self.fallas(self.proyecto("3.0.0")))

    def test_un_proyecto_atrasado_avisa_y_no_falla(self):
        hallazgos = self.proyecto("2.0.0")
        self.assertEqual([], self.fallas(hallazgos))
        self.assertEqual(1, len(hallazgos))
        self.assertEqual(AVISO, hallazgos[0].severidad,
                         "quedarse atrás avisa; es decisión del usuario subir")

    def test_declarada_y_registro_que_coinciden_no_falla(self):
        self.assertEqual([], self.fallas(
            self.proyecto("2.0.0", adopciones=["1.0.0", "2.0.0"])))

    def test_sin_historial_de_adopciones_no_se_inventa_nada(self):
        """Un proyecto recién instalado no tiene la carpeta, y eso no es falla."""
        self.assertEqual([], self.fallas(self.proyecto("3.0.0")))

    def test_sin_registro_de_cambios_no_se_afirma_nada(self):
        """Si no se puede leer qué versiones existen, no se acusa a nadie.

        Es la lección de esta casa: una comprobación que no pudo leer su
        archivo y reporta igual afirma sobre lo que no vio.
        """
        version.versiones_publicadas = lambda raiz=None: set()
        self.assertEqual([], self.fallas(self.proyecto("99.9.9")))

    def test_un_proyecto_que_no_declara_version_avisa_como_antes(self):
        with io.open(os.path.join(self.tmp, "CLAUDE.md"), "w",
                     encoding="utf-8", newline="\n") as f:
            f.write(u"# Proyecto sin versión declarada\n")
        hallazgos = version.validar(self.tmp)
        self.assertEqual([], self.fallas(hallazgos))
        self.assertEqual(1, len(hallazgos))

    # ── el orden de lo que se lee ────────────────────────────────────────

    def test_el_ultimo_registro_es_el_mayor_y_no_el_ultimo_alfabetico(self):
        version.versiones_publicadas = lambda raiz=None: {"9.0.0", "10.0.0"}
        version.version_estandar = lambda: "10.0.0"
        h = self.fallas(self.proyecto("9.0.0", adopciones=["9.0.0", "10.0.0"]))
        self.assertEqual(1, len(h))
        self.assertIn(u"10.0.0", h[0].mensaje,
                      "por orden de texto, «9» va después de «10»")


if __name__ == "__main__":
    unittest.main()
