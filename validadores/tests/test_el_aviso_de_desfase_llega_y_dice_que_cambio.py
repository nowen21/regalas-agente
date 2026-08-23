# -*- coding: utf-8 -*-
"""`83` · El aviso de quedarse atrás llega al abrir, y dice qué cambió.

**Existía y no llegaba.** El aviso estaba construido desde hacía tiempo como
subcomando, y había que pedirlo a mano: el arranque de sesión no lo miraba. La
funcionalidad central de su historia se veía funcionar todos los días **en el
repositorio del estándar**, donde el agente corre las comprobaciones de a una,
y no aparecía nunca en un proyecto instalado, que es donde tiene que llegar.

**Y decía a medias.** Nombraba las dos versiones y no qué las separa, así que
no daba con qué decidir si vale la pena subir.
"""
import io
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import sesion                      # noqa: E402
import version                     # noqa: E402
from comun import AVISO            # noqa: E402

REGISTRO = u"""# Cambios del estándar

## 3.0.0 — 2026-08-20

**MAYOR** ⚠ obliga a migrar.

**Los planes ahora declaran su origen.** Antes no se sabía de dónde salía cada fase.

## 2.1.0 — 2026-08-19

**MENOR** (algo aditivo).

**Se puede saber qué reglas nadie revisó.** Una orden las ordena por antigüedad.

## 2.0.0 — 2026-08-18

**MAYOR** ⚠ obliga a migrar.

**El registro se escribe para quien no siguió el cambio.** Antes abría con jerga.
"""


class ElTramoDelRegistro(unittest.TestCase):
    """Qué versiones separan a las dos, y cómo se cuenta."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        with io.open(os.path.join(self.tmp, "CHANGELOG.md"), "w",
                     encoding="utf-8", newline="\n") as f:
            f.write(REGISTRO)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_el_tramo_son_las_de_en_medio_y_la_de_llegada(self):
        t = version.tramo("2.0.0", "3.0.0", self.tmp)
        self.assertEqual(["2.1.0", "3.0.0"], sorted(v for v, _, _ in t))

    def test_la_version_adoptada_no_entra_en_su_propio_tramo(self):
        """Ya la tiene: contarla haría creer que le falta algo que ya hizo."""
        self.assertNotIn("2.0.0", [v for v, _, _ in version.tramo("2.0.0", "3.0.0", self.tmp)])

    def test_un_proyecto_al_dia_tiene_tramo_vacio(self):
        self.assertEqual([], version.tramo("3.0.0", "3.0.0", self.tmp))

    def test_cada_entrada_trae_su_tipo_y_su_titulo(self):
        t = version.tramo("2.0.0", "3.0.0", self.tmp)
        versiones = {v: (tipo, titulo) for v, tipo, titulo in t}
        self.assertEqual("MAYOR", versiones["3.0.0"][0])
        self.assertIn(u"declaran su origen", versiones["3.0.0"][1])

    def test_sin_registro_no_se_inventa_un_tramo(self):
        self.assertEqual([], version.tramo("1.0.0", "3.0.0", tempfile.mkdtemp()))

    # ── cómo se resume ───────────────────────────────────────────────────

    def test_lo_que_obliga_a_migrar_va_primero(self):
        """Es lo único del aviso que cambia qué hacer."""
        linea = version._resumen_del_tramo(version.tramo("2.0.0", "3.0.0", self.tmp))
        self.assertIn(u"obliga a migrar", linea)
        self.assertLess(linea.index(u"obliga a migrar"), linea.index(u"Lo último"))

    def test_sin_mayores_no_se_habla_de_migrar(self):
        linea = version._resumen_del_tramo(version.tramo("2.1.0", "2.1.0", self.tmp))
        self.assertEqual(u"", linea, "sin tramo no hay nada que resumir")


class ElAvisoLlegaAlAbrir(unittest.TestCase):
    """Lo que de verdad faltaba: que el arranque lo entregue."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.tmp, "proyectos"))
        with io.open(os.path.join(self.tmp, "CLAUDE.md"), "w",
                     encoding="utf-8", newline="\n") as f:
            f.write(u"# Proyecto\n\n- **Versión del estándar adoptada:** "
                    u"`2.0.0` · sellada `2026-08-20`.\n")
        self._validar = version.validar

    def tearDown(self):
        version.validar = self._validar
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_el_arranque_pregunta_por_la_version(self):
        """Antes no lo hacía, y por eso el aviso no llegaba nunca."""
        llamadas = []
        version.validar = lambda raiz: llamadas.append(raiz) or []
        sesion.revisar(self.tmp, os.path.dirname(os.path.dirname(
            os.path.abspath(sesion.__file__))))
        self.assertEqual(1, len(llamadas),
                         "el arranque tiene que mirar la versión del proyecto")

    def test_lo_que_devuelve_la_version_llega_al_arranque(self):
        marca = object()
        version.validar = lambda raiz: [marca]
        salida = sesion.revisar(self.tmp, os.path.dirname(os.path.dirname(
            os.path.abspath(sesion.__file__))))
        self.assertIn(marca, salida, "el hallazgo se pierde por el camino")


if __name__ == "__main__":
    unittest.main()
