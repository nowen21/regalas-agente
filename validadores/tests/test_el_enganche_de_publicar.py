# -*- coding: utf-8 -*-
"""`09·08` · La batería corre antes de publicar, no en cada commit.

**Publicar es lo que no se deshace.** Un commit se revierte; lo publicado ya lo
tiene otro. Por eso la batería completa va en `pre-push` y no en `pre-commit`:
ahí sería insoportable —minutos por cada commit— y a la semana alguien lo apaga.

**Y no todo detiene.** Lo que sale del trabajo de hoy —enlaces rotos, algo sin
versionar— rechaza el push. El cuerpo de reglas contra su propio molde
**informa**: hay deuda conocida, y un estándar endeudado consigo mismo no puede
impedir publicar cualquier otra cosa. Eso convertiría el enganche en un
obstáculo permanente, que es como se termina en `--no-verify` para todo.
"""
import io
import os
import sys
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import instalar    # noqa: E402
from comun import RAIZ      # noqa: E402

GANCHO = os.path.join(RAIZ, ".githooks", "pre-push")


class ElEngancheEstaYSeInstala(unittest.TestCase):

    def test_esta_en_la_lista_del_instalador(self):
        self.assertIn("pre-push", [n for n, _p, _d in instalar.HOOKS])

    def test_el_archivo_existe(self):
        self.assertTrue(os.path.isfile(GANCHO))

    def test_lleva_la_marca_del_estandar(self):
        with io.open(GANCHO, encoding="utf-8") as f:
            self.assertIn(instalar.MARCA, f.read())


class QueDetieneYQueNo(unittest.TestCase):
    """**Es la distinción que decide si el enganche sobrevive.**"""

    def _texto(self):
        with io.open(GANCHO, encoding="utf-8") as f:
            return f.read()

    def test_estandar_y_versionado_detienen(self):
        t = self._texto()
        self.assertIn("for SUB in estandar versionado", t)

    def test_metareglas_informa_y_no_detiene(self):
        """Si `metareglas` entrara al bucle que marca fallo, **hoy ningún push
        pasaría**: hay reglas publicadas que no cumplen su checklist, y son
        deuda conocida del pendiente 19 — no defectos de este trabajo."""
        t = self._texto()
        self.assertIn("no detiene", t)
        self.assertNotIn("for SUB in estandar metareglas", t)

    def test_dice_como_saltarlo_a_proposito(self):
        """**Un enganche sin salida se salta a escondidas.** Decir cómo saltarlo
        es lo que hace que saltarlo sea una decisión y no una maña."""
        self.assertIn("--no-verify", self._texto())

    def test_no_corre_lo_que_necesita_un_proyecto_real(self):
        """El linter, la suite y el audit fallarían en cualquier repositorio que
        no los tenga instalados — y un enganche que falla siempre se salta."""
        t = self._texto()
        for sub in ("linter", "suite", "audit"):
            self.assertNotIn(' "%s"' % sub, t)


if __name__ == "__main__":
    unittest.main(verbosity=2)
