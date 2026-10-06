# -*- coding: utf-8 -*-
"""`EP-025·HU-014 · CP-002`: el enganche de los `.md`, en `core/`.

Sin Django: corren con `python -m unittest core.enganches.tests_md` desde
`proyectos/cimiento/`.
"""
import io
import os
import shutil
import tempfile
import unittest

from .md import revisar

ADAPTADOR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))), "adaptadores", "claude-code", "hook_md.py")


def _escribir(ruta, texto):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


class ElEngancheDeLosMd(unittest.TestCase):

    def setUp(self):
        self.raiz = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.raiz, True)
        self.md = os.path.join(self.raiz, "notas", "a.md")
        _escribir(self.md, "# A\n\nVer [b](b.md).\n")

    def datos(self, ruta=None, texto="nada raro", sesion=""):
        return {"tool_input": {"file_path": ruta or self.md, "new_string": texto}, "session_id": sesion}

    def test_un_enlace_roto_da_codigo_2(self):
        codigo, _agente, error = revisar(self.raiz, self.datos())
        self.assertEqual(2, codigo)
        self.assertIn("b.md", error)

    def test_las_marcas_de_lo_escrito_se_avisan(self):
        _escribir(os.path.join(self.raiz, "notas", "b.md"), "# B\n")
        codigo, agente, error = revisar(self.raiz, self.datos(texto="uno — dos"))
        self.assertEqual((0, ""), (codigo, error))
        self.assertIn("línea 1: raya larga", agente)

    def test_lo_que_no_es_md_o_es_de_afuera_no_se_revisa_pero_se_anota(self):
        codigo, agente, error = revisar(self.raiz, self.datos(os.path.join(self.raiz, "x.py"), sesion="s-1"))
        self.assertEqual((0, "", ""), (codigo, agente, error))
        with open(os.path.join(self.raiz, "historico-chat", ".tocado", "s-1.txt"), encoding="utf-8") as f:
            self.assertIn("x.py", f.read())
        with tempfile.TemporaryDirectory() as afuera:
            self.assertEqual(0, revisar(self.raiz, self.datos(os.path.join(afuera, "c.md")))[0])

    def test_el_adaptador_no_usa_validadores(self):
        with io.open(ADAPTADOR, encoding="utf-8") as f:
            texto = f.read()
        self.assertNotIn('"validadores"', texto)
        self.assertIn("from core.enganches.md import revisar", texto)


if __name__ == "__main__":
    unittest.main()
