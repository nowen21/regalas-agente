# -*- coding: utf-8 -*-
"""`EP-007 · HU-003 · CA-04` — la historia y el pendiente nacen con su esqueleto y sus índices (fase B)."""
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ = os.path.dirname(VALIDADORES)
sys.path.insert(0, VALIDADORES)

import andamio      # noqa: E402
import enlaces      # noqa: E402
import pendientes   # noqa: E402
from comun import FALLA, leer   # noqa: E402

EPICA = "EP-005-automatismos-que-no-dependen-de-la-memoria"


def escribir(ruta, texto):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def arbol():
    tmp = tempfile.mkdtemp()
    shutil.copytree(os.path.join(RAIZ, "plantillas"), os.path.join(tmp, "plantillas"))
    shutil.copytree(os.path.join(RAIZ, "base"), os.path.join(tmp, "base"))
    shutil.copytree(os.path.join(RAIZ, "documentacion", "epicas", EPICA),
                    os.path.join(tmp, "documentacion", "epicas", EPICA))
    escribir(os.path.join(tmp, "pendientes", "01-algo.md"), "# Pendiente · algo\n")
    escribir(os.path.join(tmp, "pendientes", "README.md"),
             "# Pendientes\n\n## Abiertos\n\n| # | P | Pendiente | Qué resuelve |\n|---|---|---|---|\n"
             "| 01 | **P2** | [algo](01-algo.md) | x |\n\n---\n\n"
             "## Ningún pendiente vive suelto: en qué historia está cada uno\n\n"
             "| Épica · HU | Pendientes que viven ahí |\n|---|---|\n"
             "| [EP-005 · HU-008](../documentacion/epicas/%s/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md) — Enganche del resumen | 32 |\n"
             % EPICA)
    return tmp


class CA04LaHistoria(unittest.TestCase):

    def setUp(self):
        self.tmp = arbol()
        self.addCleanup(lambda: shutil.rmtree(self.tmp, ignore_errors=True))
        self.epica_dir = os.path.join(self.tmp, "documentacion", "epicas", EPICA)

    def test_cp_001_la_historia_nace_con_sus_indices(self):
        destino, tocados = andamio.crear_hu(self.tmp, EPICA, "prueba-del-andamio", escribir=True)
        nombre = os.path.basename(destino)
        self.assertTrue(nombre.startswith("HU-0"))
        self.assertTrue(os.path.isfile(os.path.join(destino, nombre + ".md")))
        self.assertTrue(os.path.isfile(os.path.join(destino, "README.md")))
        epica = leer(os.path.join(self.epica_dir, "epica.md"))
        fila = [l for l in epica.splitlines() if l.startswith("| [%s](%s/%s.md)" % (nombre[:6], nombre, nombre))]
        self.assertEqual(1, len(fila))
        cabecera = [l for l in epica.splitlines() if l.startswith("| ID | Título")][0]
        self.assertEqual(cabecera.count("|"), fila[0].count("|"))
        readme = leer(os.path.join(self.epica_dir, "README.md"))
        self.assertIn("| [documentacion/epicas/%s/%s/](%s/) |" % (EPICA, nombre, nombre), readme)

    def test_cp_002_el_numero_se_lee_de_lo_que_hay(self):
        e = os.path.join(self.tmp, "documentacion", "epicas", "EP-009-x")
        for hu in ("HU-001-a", "HU-003-c"):
            os.makedirs(os.path.join(e, hu))
        self.assertEqual("HU-004", andamio.siguiente_hu(e))

    def test_cp_004_no_escribe_contenido(self):
        destino, _ = andamio.crear_hu(self.tmp, EPICA, "prueba", escribir=True)
        nombre = os.path.basename(destino)
        # La plantilla se pide **por donde la busca el andamio**. Escrita a
        # mano aqui, la ruta quedo apuntando a un archivo que no existe:
        # `leer()` devolvia vacio y la cuenta comparaba 0 contra 68.
        plantilla = leer(os.path.join(self.tmp, andamio.PLANTILLA_HU))
        creada = leer(os.path.join(destino, nombre + ".md"))
        estructurales = 1 + plantilla.count(andamio.MARCADOR_RAIZ)   # «Épica padre» y la ruta
        self.assertEqual(plantilla.count("«") - estructurales, creada.count("«"))
        self.assertNotIn("HU-000", creada)

    def test_cp_005_los_validadores_no_reclaman_nada(self):
        destino, _ = andamio.crear_hu(self.tmp, EPICA, "prueba", escribir=True)
        rotos = [str(h) for h in enlaces.validar_enlaces(self.tmp)
                 if h.severidad == FALLA and os.path.basename(destino) in str(h)]
        self.assertEqual([], rotos)


class CA04ElPendiente(unittest.TestCase):

    def setUp(self):
        self.tmp = arbol()
        self.addCleanup(lambda: shutil.rmtree(self.tmp, ignore_errors=True))

    def test_cp_003_el_pendiente_nace_con_su_fila_y_su_historia_en_el_mapa(self):
        hu = "%s/HU-008-enganche-del-resumen" % EPICA
        destino, tocados = andamio.crear_pendiente(self.tmp, "prueba", hu, escribir=True)
        self.assertEqual("02-prueba.md", os.path.basename(destino))
        texto = leer(destino)
        self.assertIn("[EP-005 · HU-008 — El enganche que sostiene el resumen de la sesión](../documentacion/epicas/%s/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md)" % EPICA, texto)
        self.assertNotIn("«HISTORIA»", texto)
        indice = leer(os.path.join(self.tmp, "pendientes", "README.md"))
        self.assertIn(andamio.SECCION_SIN_AGRUPAR, indice)
        self.assertIn("| 2 | «P?» | [«qué falta, en una línea»](02-prueba.md) |", indice)
        self.assertIn("— Enganche del resumen | 32, 2 |", indice)
        self.assertEqual(3, pendientes.proximo_libre(self.tmp))

    def test_la_historia_que_no_estaba_en_el_mapa_entra(self):
        hu = "%s/HU-009-lo-que-rige-cada-frase-llega-puesto" % EPICA
        andamio.crear_pendiente(self.tmp, "otra", hu, escribir=True)
        indice = leer(os.path.join(self.tmp, "pendientes", "README.md"))
        self.assertRegex(indice, r"\| \[EP-005 · HU-009\]\([^)]+\) — Lo que gobierna cada frase llega puesto al abrir la sesión \| 2 \|")

    def test_sin_aplicar_no_escribe(self):
        hu = "%s/HU-008-enganche-del-resumen" % EPICA
        antes = leer(os.path.join(self.tmp, "pendientes", "README.md"))
        destino, _ = andamio.crear_pendiente(self.tmp, "prueba", hu, escribir=False)
        self.assertFalse(os.path.exists(destino))
        self.assertEqual(antes, leer(os.path.join(self.tmp, "pendientes", "README.md")))


class CP006ElModoDeFaseSigueIgual(unittest.TestCase):

    def test_la_llamada_de_siempre(self):
        tmp = arbol()
        self.addCleanup(lambda: shutil.rmtree(tmp, ignore_errors=True))
        r = subprocess.run([sys.executable, os.path.join(VALIDADORES, "andamio.py"),
                            EPICA, "HU-008-enganche-del-resumen", "prueba", "--raiz", tmp],
                           capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=60)
        self.assertEqual(0, r.returncode, r.stderr)
        self.assertIn("simulado", r.stdout)
        self.assertIn("plan_trabajo.md", r.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
