# -*- coding: utf-8 -*-
"""El andamio crea la historia con el número que le dio el análisis.

Análisis 3 del pendiente 119, acuerdo 4. Sin Django: corren con
`python -m unittest core.herramientas.tests_andamio` desde `proyectos/cimiento/`.
"""
import io
import os
import tempfile
import unittest

from .andamio import Andamio

EPICA = "EP-001-algo"


class LaHistoriaTomaElNumeroPedido(unittest.TestCase):

    def setUp(self):
        carpeta = tempfile.TemporaryDirectory()
        self.addCleanup(carpeta.cleanup)
        self.raiz = carpeta.name
        self.epica = os.path.join(self.raiz, "documentacion", "epicas", EPICA)
        os.makedirs(os.path.join(self.epica, "HU-001-primera"))
        with io.open(os.path.join(self.epica, "epica.md"), "w", encoding="utf-8") as f:
            f.write("# EP-001 · Algo\n\n## 9. Historias\n\n| a |\n|---|\n")

    def test_con_numero_toma_ese(self):
        destino, _ = Andamio(self.raiz).crear_hu(EPICA, "la-quinta", escribir=True, numero=5)
        self.assertEqual("HU-005-la-quinta", os.path.basename(destino))
        self.assertIn("HU-005", io.open(os.path.join(self.epica, "epica.md"), encoding="utf-8").read())

    def test_sin_numero_sigue_tomando_el_siguiente(self):
        destino, _ = Andamio(self.raiz).crear_hu(EPICA, "la-otra", escribir=True)
        self.assertEqual("HU-002-la-otra", os.path.basename(destino))

    def test_un_numero_que_ya_existe_se_rechaza_sin_escribir(self):
        with self.assertRaises(ValueError):
            Andamio(self.raiz).crear_hu(EPICA, "repetida", escribir=True, numero=1)
        self.assertEqual(["HU-001-primera", "epica.md"], sorted(os.listdir(self.epica)))


def _leer(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return f.read()


def _escribir(ruta, texto):
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


class LoQueCreaElAndamioSePuedeQuitar(unittest.TestCase):
    """`EP-025·HU-020` · Lo que se crea junto se quita junto."""

    def setUp(self):
        carpeta = tempfile.TemporaryDirectory()
        self.addCleanup(carpeta.cleanup)
        self.raiz = carpeta.name
        self.epica = os.path.join(self.raiz, "documentacion", "epicas", EPICA)
        os.makedirs(self.epica)
        _escribir(os.path.join(self.epica, "epica.md"), "# EP-001 · Algo\n\n## 9. Historias\n\n| a |\n|---|\n")
        _escribir(os.path.join(self.epica, "README.md"), "# EP-001\n\n| Qué | De qué |\n|---|---|\n| x | y |\n")
        self.antes = {n: _leer(os.path.join(self.epica, n)) for n in ("epica.md", "README.md")}
        self.andamio = Andamio(self.raiz)

    def _hu(self, descripcion="una"):
        return self.andamio.crear_hu(EPICA, descripcion, escribir=True)[0]

    # CP-001 · Borrar plantilla
    def test_la_hu_sin_cambios_se_borra_con_sus_filas(self):
        hu = self._hu()
        accion, _ = self.andamio.quitar(hu, escribir=True)
        self.assertIn("borrada", accion)
        self.assertFalse(os.path.exists(hu))
        self.assertEqual(self.antes, {n: _leer(os.path.join(self.epica, n)) for n in self.antes})

    def test_la_fase_sin_cambios_se_borra(self):
        hu = self._hu()
        fase, _ = self.andamio.crear(EPICA, os.path.basename(hu), "algo", escribir=True)
        self.assertIn("borrada", self.andamio.quitar(fase, escribir=True)[0])
        self.assertFalse(os.path.exists(fase))
        self.assertTrue(os.path.isdir(hu))

    def test_el_pendiente_sin_cambios_se_borra(self):
        ruta, _ = self.andamio.crear_pendiente("algo-falta", escribir=True)
        carpeta = os.path.dirname(ruta)
        self.assertIn("borrada", self.andamio.quitar(carpeta, escribir=True)[0])
        self.assertFalse(os.path.exists(carpeta))

    # CP-002 · Archivar
    def test_la_hu_con_trabajo_se_archiva_y_su_numero_no_se_reusa(self):
        hu = self._hu()
        nombre = os.path.basename(hu)
        md = os.path.join(hu, nombre + ".md")
        _escribir(md, _leer(md) + "\nTrabajo escrito.\n")
        accion, _ = self.andamio.quitar(hu, escribir=True)
        self.assertIn("archivada", accion)
        archivada = os.path.join(self.epica, "_archivo", nombre)
        self.assertIn("Trabajo escrito.", _leer(os.path.join(archivada, nombre + ".md")))
        self.assertIn("](../../epica.md)", _leer(os.path.join(archivada, nombre + ".md")))
        self.assertIn("](_archivo/%s/%s.md) (archivada)" % (nombre, nombre),
                      _leer(os.path.join(self.epica, "epica.md")))
        self.assertIn("](_archivo/%s/) (archivada)" % nombre, _leer(os.path.join(self.epica, "README.md")))
        self.assertTrue(os.path.basename(self._hu("otra")).startswith("HU-002-"))
        with self.assertRaises(ValueError):
            self.andamio.crear_hu(EPICA, "repetida", escribir=True, numero=1)

    # CP-003 · Rechazos y simulación
    def test_la_hu_con_fases_no_se_quita(self):
        hu = self._hu()
        self.andamio.crear(EPICA, os.path.basename(hu), "algo", escribir=True)
        with self.assertRaises(ValueError):
            self.andamio.quitar(hu, escribir=True)
        self.assertTrue(os.path.isdir(hu))

    def test_una_carpeta_que_no_es_del_andamio_no_se_quita(self):
        ajena = os.path.join(self.raiz, "otra-cosa")
        os.makedirs(ajena)
        with self.assertRaises(ValueError):
            self.andamio.quitar(ajena, escribir=True)
        self.assertTrue(os.path.isdir(ajena))

    def test_sin_aplicar_no_toca_nada(self):
        hu = self._hu()
        epica = _leer(os.path.join(self.epica, "epica.md"))
        accion, tocados = self.andamio.quitar(hu)
        self.assertIn("borrada", accion)
        self.assertIn(os.path.join(self.epica, "epica.md"), tocados)
        self.assertTrue(os.path.isdir(hu))
        self.assertEqual(epica, _leer(os.path.join(self.epica, "epica.md")))


if __name__ == "__main__":
    unittest.main()
