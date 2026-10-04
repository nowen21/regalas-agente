# -*- coding: utf-8 -*-
"""El freno no frena el registro de git (sesión del 2026-10-04, análisis 1 del pendiente 116, fila 15).

Dos defectos hacían que todo commit con archivos nuevos se detuviera:
- leía la ruta vieja de un renombrado como un archivo más, sin sus tres
  primeras letras («taforma/…»);
- revisaba `git add` y `git commit` como si escribieran contenido, cuando solo
  registran lo que ya cambió, y eso ya lo revisa el `pre-commit`.
"""
import os
import subprocess
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import freno  # noqa: E402


def _git(repo, *args):
    subprocess.run(["git", "-C", repo, *args], check=True, capture_output=True)


class ElRenombradoSeLeeBien(unittest.TestCase):

    def test_la_ruta_vieja_no_aparece_como_archivo(self):
        with tempfile.TemporaryDirectory() as repo:
            _git(repo, "init", "-q")
            _git(repo, "config", "user.email", "prueba@ejemplo.co")
            _git(repo, "config", "user.name", "Prueba")
            os.makedirs(os.path.join(repo, "plataforma"))
            with open(os.path.join(repo, "plataforma", "a.py"), "w") as f:
                f.write("x = 1\n" * 20)
            _git(repo, "add", "-A")
            _git(repo, "commit", "-q", "-m", "inicio")
            os.makedirs(os.path.join(repo, "nueva"))
            os.replace(os.path.join(repo, "plataforma", "a.py"), os.path.join(repo, "nueva", "a.py"))
            _git(repo, "add", "-A")
            self.assertEqual(sorted(freno._cambiados(repo)), ["nueva/a.py"])


class ElRegistroDeGitNoSeRevisa(unittest.TestCase):

    def test_las_ordenes_que_solo_registran(self):
        for orden in ("git add -A", "git commit -m 'x; y'", 'git -C "C:/a b" commit -F m.txt',
                      "cd /c/repo && git add . && git commit -m x && git push",
                      "git commit -F - <<'EOF'\nmensaje; con punto y coma\nEOF"):
            self.assertTrue(freno.solo_registra(orden), orden)

    def test_las_que_escriben_si_se_revisan(self):
        for orden in ("git add -A && rm -rf x", "git checkout -- a.py", "python guion.py", "", "git rm x"):
            self.assertFalse(freno.solo_registra(orden), orden)

    def test_despues_de_registrar_no_hay_hallazgos(self):
        self.assertEqual(freno.despues(tempfile.gettempdir(), "git commit -m x"), [])


if __name__ == "__main__":
    unittest.main()
