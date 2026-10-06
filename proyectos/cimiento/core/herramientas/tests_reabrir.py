# -*- coding: utf-8 -*-
"""Un pendiente cerrado se puede reabrir (`EP-025·HU-022`).

Sin Django: corren con `python -m unittest core.herramientas.tests_reabrir`
desde `proyectos/cimiento/`.
"""
import io
import os
import tempfile
import unittest

from ..validadores.enlaces import EnlacesRotos
from .cerrar import CerradorDePendientes

INDICE = "# Pendientes\n\n| # | P | Pendiente | Qué |\n|---|---|---|---|\n| 07 | **P2** | [Algo](07-algo.md) | x |\n"


def _escribir(raiz, rel, texto):
    ruta = os.path.join(raiz, *rel.split("/"))
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def _leer(raiz, rel):
    with io.open(os.path.join(raiz, *rel.split("/")), encoding="utf-8") as f:
        return f.read()


class UnPendienteCerradoSePuedeReabrir(unittest.TestCase):

    def setUp(self):
        carpeta = tempfile.TemporaryDirectory()
        self.addCleanup(carpeta.cleanup)
        self.raiz = carpeta.name
        _escribir(self.raiz, "pendientes/07-algo.md", "# Algo\n\n**Estado:** abierto. Ver [x](../base/x.md).\n")
        _escribir(self.raiz, "pendientes/README.md", INDICE)
        _escribir(self.raiz, "base/x.md", "# X\n")
        _escribir(self.raiz, "notas/n.md", "Ver [el 07](../pendientes/07-algo.md).\n")
        CerradorDePendientes(self.raiz).cerrar("07", "algo-resuelto", escribir=True)

    def reabrir(self, numero="07", motivo="volvió a fallar", escribir=True):
        return CerradorDePendientes(self.raiz).reabrir(numero, motivo, "2026-10-05", escribir=escribir)

    # CP-001 · Reabrir
    def test_vuelve_con_sus_enlaces_y_su_fila(self):
        self.assertIn("~~07~~", _leer(self.raiz, "pendientes/README.md"))
        self.reabrir()
        self.assertTrue(os.path.isfile(os.path.join(self.raiz, "pendientes", "07-algo-resuelto.md")))
        self.assertFalse(os.path.exists(os.path.join(self.raiz, "pendientes", "hecho", "algo-resuelto.md")))
        self.assertIn("../pendientes/07-algo-resuelto.md", _leer(self.raiz, "notas/n.md"))
        self.assertIn("| 07 | — | [Algo](07-algo-resuelto.md) | x |", _leer(self.raiz, "pendientes/README.md"))
        texto = _leer(self.raiz, "pendientes/07-algo-resuelto.md")
        self.assertIn("> **Reabierto** el 2026-10-05: volvió a fallar.", texto)
        self.assertIn("](../base/x.md)", texto)
        self.assertEqual([], EnlacesRotos(self.raiz).validar())

    def test_el_estado_hecho_pasa_a_reabierto(self):
        ruta = "pendientes/hecho/algo-resuelto.md"
        _escribir(self.raiz, ruta, _leer(self.raiz, ruta).replace("**Estado:** abierto", "**Estado:** hecho"))
        self.reabrir()
        self.assertIn("**Estado:** reabierto", _leer(self.raiz, "pendientes/07-algo-resuelto.md"))

    # CP-002 · Rechazos y simulación
    def test_un_numero_que_no_esta_cerrado_se_rechaza(self):
        with self.assertRaises(SystemExit):
            self.reabrir("08")
        self.assertTrue(os.path.isfile(os.path.join(self.raiz, "pendientes", "hecho", "algo-resuelto.md")))

    def test_sin_motivo_se_rechaza(self):
        with self.assertRaises(SystemExit):
            self.reabrir(motivo=" ")

    def test_sin_aplicar_no_toca_nada(self):
        indice = _leer(self.raiz, "pendientes/README.md")
        _o, destino, tocados = self.reabrir(escribir=False)
        self.assertTrue(tocados)
        self.assertFalse(os.path.exists(destino))
        self.assertEqual(indice, _leer(self.raiz, "pendientes/README.md"))


if __name__ == "__main__":
    unittest.main()
