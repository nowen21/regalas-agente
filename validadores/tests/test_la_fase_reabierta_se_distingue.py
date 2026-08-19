# -*- coding: utf-8 -*-
"""`09·10` · Una fase reabierta no se parece a una fase nueva.

**Hoy no se distinguían**, así que la medida de retrabajo no existía. Y el
retrabajo es la señal más directa de que una especificación salió incompleta —
no para calificar a nadie, sino para ver **qué parte del flujo lo produce**.

**Se deriva de la historia, no de las palabras.** Las reaperturas se escriben en
prosa y cada una con las suyas: «reabierta», «se reabrió», «vuelta a cerrar».
Buscar la palabra encuentra unas, se pierde otras, y cuenta las que solo
*hablan* de reabrir — hay cinco archivos que la mencionan y solo dos fases se
reabrieron de verdad.

**Lo que no se puede escribir de dos formas es una casilla que estaba marcada y
dejó de estarlo.**
"""
import io
import os
import subprocess
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import reaperturas    # noqa: E402
from comun import FALLA, RAIZ      # noqa: E402


def tabla(estaciones):
    """Una tabla de estaciones con las casillas que se le den."""
    filas = "\n".join("| %d | Etapa | puerta | %s |" % (n, "☑" if v else "☐")
                      for n, v in sorted(estaciones.items()))
    return u"# Estado de fase\n\n| # | Etapa | Puerta | Estado |\n|---|---|---|---|\n%s\n" % filas


def repo(*versiones):
    """Un repositorio con una fase cuyo estado cambia en cada commit."""
    tmp = tempfile.TemporaryDirectory()
    r = tmp.name
    subprocess.run(["git", "init", "-q", r], capture_output=True)
    subprocess.run(["git", "-C", r, "config", "user.email", "p@p"], capture_output=True)
    subprocess.run(["git", "-C", r, "config", "user.name", "p"], capture_output=True)
    d = os.path.join(r, "documentacion", "epicas", "EP-001", "HU-001", "A-fase")
    os.makedirs(d)
    for i, estaciones in enumerate(versiones):
        with io.open(os.path.join(d, "estado-fase.md"), "w", encoding="utf-8") as f:
            f.write(tabla(estaciones))
        subprocess.run(["git", "-C", r, "add", "-A"], capture_output=True)
        subprocess.run(["git", "-C", r, "commit", "-qm", "v%d" % i], capture_output=True)
    return tmp


class LaVueltaAtrasSeDetecta(unittest.TestCase):

    def test_cerrar_y_volver_atras_es_reapertura(self):
        """Estación 7 marcada, y en un guardado posterior desmarcada."""
        tmp = repo({7: True, 8: True}, {7: False, 8: True})
        self.addCleanup(tmp.cleanup)
        self.assertEqual(1, len(reaperturas.reaperturas(tmp.name)))

    def test_dos_vueltas_se_cuentan_dos(self):
        tmp = repo({7: True}, {7: False}, {7: True}, {7: False})
        self.addCleanup(tmp.cleanup)
        _ruta, vueltas = reaperturas.reaperturas(tmp.name)[0]
        self.assertEqual(2, len(vueltas))

    def test_avanzar_no_es_reapertura(self):
        """**Es la mitad que importa.** Marcar estaciones es el trabajo normal."""
        tmp = repo({7: False, 8: False}, {7: True, 8: False}, {7: True, 8: True})
        self.addCleanup(tmp.cleanup)
        self.assertEqual([], reaperturas.reaperturas(tmp.name))

    def test_volver_atras_antes_de_cerrar_no_cuenta(self):
        """Corregir la estación 3 no es reabrir: no se había cerrado nada."""
        tmp = repo({3: True, 7: False}, {3: False, 7: False})
        self.addCleanup(tmp.cleanup)
        self.assertEqual([], reaperturas.reaperturas(tmp.name))

    def test_una_fase_recien_creada_no_es_reapertura(self):
        tmp = repo({7: False})
        self.addCleanup(tmp.cleanup)
        self.assertEqual([], reaperturas.reaperturas(tmp.name))


class SobreElRepositorioDeVerdad(unittest.TestCase):

    def test_encuentra_las_dos_que_se_reabrieron(self):
        """`A-EP-005-HU-008` —el enganche del resumen— y `A-EP-007-HU-006`."""
        rutas = [r for r, _v in reaperturas.reaperturas(RAIZ)]
        self.assertEqual(2, len(rutas))
        juntas = " ".join(rutas)
        self.assertIn("A-EP-005-HU-008", juntas)
        self.assertIn("A-EP-007-HU-006", juntas)

    def test_no_cuenta_las_que_solo_hablan_de_reabrir(self):
        """**Cinco archivos mencionan la palabra y solo dos se reabrieron.**
        Buscar el texto habría dado más del doble."""
        self.assertEqual(2, len(reaperturas.reaperturas(RAIZ)))

    def test_nunca_es_una_falla(self):
        """**Reabrir es lo correcto** cuando lo que falla es ese trabajo y su
        documentación decía que estaba hecho. Lo que se mide no es un
        incumplimiento: es de dónde sale el retrabajo."""
        self.assertEqual([], [h for h in reaperturas.validar(RAIZ)
                              if h.severidad == FALLA])


class Bordes(unittest.TestCase):

    def test_sin_epicas_no_revienta(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.assertEqual([], reaperturas.reaperturas(tmp.name))

    def test_el_resumen_va_aunque_no_haya_ninguna(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.assertIn("Fases reabiertas: 0", reaperturas.linea_resumen(tmp.name))

    def test_no_es_punto_de_entrada(self):
        with io.open(os.path.join(VALIDADORES, "reaperturas.py"),
                     encoding="utf-8") as f:
            self.assertIn("no_es_punto_de_entrada", f.read())


if __name__ == "__main__":
    unittest.main(verbosity=2)
