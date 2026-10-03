# -*- coding: utf-8 -*-
"""`EP-023 · HU-001 · CA-06` · Un análisis aprobado trae sus cuatro partes.

Los casos del CP-005 de la fase `A`: el análisis aprobado completo pasa; al que
le falta una sección se le nombra; el abierto todavía no se juzga, porque se
está llenando.
"""
import os
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import analisis   # noqa: E402

SECCIONES = {
    "Cimiento": "### Cimiento: las reglas que aplican y las que chocan\n\nAlgo.\n",
    "El proyecto": "### El proyecto: lo que existe, lo que funciona y lo que falta\n\nAlgo.\n",
    "Lo aprendido": "### Lo aprendido: señales, lecciones y análisis anteriores\n\nAlgo.\n",
    "El entorno": "### El entorno: normas, herramientas y proyectos que heredan\n\nAlgo.\n",
}


def documento(aprobado=True, sin=None):
    marca = "> **Aprobado** por el usuario el 2026-10-01, en el turno 9.\n\n" if aprobado else ""
    partes = "".join(t for n, t in SECCIONES.items() if n != sin)
    return f"# Análisis 1: algo\n\n{marca}## Lo que aportó cada parte\n\n{partes}"


class UnAnalisisAprobadoTraeSusCuatroPartes(unittest.TestCase):

    def escribir(self, raiz, texto, nombre="analisis-1.md"):
        carpeta = os.path.join(raiz, "documentacion", "pendiente")
        os.makedirs(carpeta, exist_ok=True)
        with open(os.path.join(carpeta, nombre), "w", encoding="utf-8") as f:
            f.write(texto)

    def test_el_aprobado_completo_pasa(self):
        with tempfile.TemporaryDirectory() as raiz:
            self.escribir(raiz, documento())
            self.assertEqual(analisis.revisar(raiz), [])

    def test_al_aprobado_sin_lo_aprendido_se_le_nombra(self):
        with tempfile.TemporaryDirectory() as raiz:
            self.escribir(raiz, documento(sin="Lo aprendido"))
            fallas = analisis.revisar(raiz)
            self.assertEqual(len(fallas), 1)
            self.assertIn("«Lo aprendido»", fallas[0])

    def test_al_aprobado_sin_el_entorno_se_le_nombra(self):
        with tempfile.TemporaryDirectory() as raiz:
            self.escribir(raiz, documento(sin="El entorno"))
            fallas = analisis.revisar(raiz)
            self.assertEqual(len(fallas), 1)
            self.assertIn("«El entorno»", fallas[0])

    def test_el_abierto_incompleto_todavia_no_se_juzga(self):
        with tempfile.TemporaryDirectory() as raiz:
            self.escribir(raiz, documento(aprobado=False, sin="Cimiento"))
            self.assertEqual(analisis.revisar(raiz), [])

    def test_solo_mira_los_analisis_numerados(self):
        with tempfile.TemporaryDirectory() as raiz:
            self.escribir(raiz, documento(sin="Cimiento"), nombre="base-cierre.md")
            self.assertEqual(analisis.revisar(raiz), [])

    def test_la_falla_llega_a_validar(self):
        with tempfile.TemporaryDirectory() as raiz:
            self.escribir(raiz, documento(sin="El proyecto"))
            hallazgos = analisis.validar(raiz)
            self.assertEqual(len(hallazgos), 1)


# ── Fase D: lo que exige la 44.0.0 ──────────────────────────────────────────

RECOMENDACIONES = "## Recomendaciones\n\n| Recomendación | Cómo |\n|---|---|\n| R-1 | Se listaron los casos |\n\n"
DONDE = ("### Dónde más puede pasar\n\n| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |\n"
         "|---|---|---|---|\n| Otro canal | Otra herramienta | Se escapa | Punto 1 |\n\n")
HU = ("## Propuesta final: hallazgo y pendiente\n\n"
      "| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos |\n"
      "|---|---|---|---|---|---|---|\n"
      "| 1 | 1 | Base | Algo | Ninguna | Las demás se apoyan en ella | 1 |\n"
      "| 2 | 2 | Encima | Algo | 1 | Usa la base | 2 |\n\n")
APORTA = ("## Lo que aporta al análisis principal\n\n**Resultado:** Ratifica.\n\n"
          "**Lo que suma al análisis principal:** La clase tiene suma.\n")


def nuevo(version="44.0.0", recomendaciones=RECOMENDACIONES, donde=DONDE, hu=HU, aporta=APORTA):
    marca = "> **Aprobado** por el usuario el 2026-10-02, en el turno 9, con la versión %s.\n\n" % version
    partes = "".join(SECCIONES.values())
    return (f"# Análisis 1: algo\n\n{marca}{recomendaciones}## Hallazgo\n\nAlgo.\n\n"
            f"## Lo que aportó cada parte\n\n{partes}{donde}{hu}{aporta}")


PRINCIPAL = ("# Análisis principal\n\n## Qué es\n\nCimiento es algo. La clase tiene suma.\n\n"
             "## Lista de análisis\n\n| Fecha | Resultado | Análisis |\n|---|---|---|\n"
             "| 2026-10-02 | Ratifica | [Análisis 1 del pendiente 7](../documentacion/7-algo/analisis-1.md) |\n")


class LoQueExigeLa44(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.raiz = self.tmp.name

    def tearDown(self):
        self.tmp.cleanup()

    def escribir(self, relativa, texto):
        ruta = os.path.join(self.raiz, *relativa.split("/"))
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(texto)

    def fallas(self, texto):
        self.escribir("documentacion/7-algo/analisis-1.md", texto)
        return analisis.revisar(self.raiz)

    def test_cp001_el_completo_pasa(self):
        self.assertEqual(self.fallas(nuevo()), [])

    def test_cp001_sin_donde_mas_falla(self):
        fallas = self.fallas(nuevo(donde=""))
        self.assertEqual(len(fallas), 1)
        self.assertIn("«Dónde más puede pasar»", fallas[0])

    def test_cp001_un_caso_sin_lo_que_lo_cubre_se_nombra(self):
        fallas = self.fallas(nuevo(donde=DONDE.replace("| Punto 1 |", "|  |")))
        self.assertEqual(len(fallas), 1)
        self.assertIn("«Otro canal»", fallas[0])

    def test_cp002_una_hu_antes_de_la_que_depende(self):
        roto = HU.replace("| 1 | 1 | Base |", "| 3 | 1 | Base |")
        fallas = self.fallas(nuevo(hu=roto))
        self.assertEqual(len(fallas), 1)
        self.assertIn("la HU 2 va antes de la HU 1", fallas[0])

    def test_cp002_un_puesto_sin_razon(self):
        fallas = self.fallas(nuevo(hu=HU.replace("| Usa la base |", "|  |")))
        self.assertEqual(len(fallas), 1)
        self.assertIn("la HU 2 no dice por qué", fallas[0])

    def test_cp003_sin_recomendaciones_consultadas(self):
        fallas = self.fallas(nuevo(recomendaciones=""))
        self.assertEqual(len(fallas), 1)
        self.assertIn("recomendaciones", fallas[0])

    def test_cp003_recomendacion_sin_origen_y_repetida(self):
        self.escribir("plantillas/recomendaciones-del-analisis.md",
                      "| # | Qué se hace | Por qué | Sale de |\n|---|---|---|---|\n"
                      "| R-1 | Listar los casos | Para no dejar huecos | Análisis 8, lección 1 |\n"
                      "| R-2 | Listar los casos. | Otra razón | Análisis 2, lección 1 |\n"
                      "| R-3 | Medir la respuesta | Para no alargar | |\n")
        fallas = analisis.revisar(self.raiz)
        self.assertEqual(len(fallas), 2)
        self.assertTrue(any("la R-2 dice lo mismo que la R-1" in f for f in fallas))
        self.assertTrue(any("la R-3 no dice de qué análisis sale" in f for f in fallas))

    def test_cp003_las_de_cimiento_pasan(self):
        self.assertEqual(analisis.recomendaciones(), [])

    def test_cp004_el_que_no_esta_en_la_lista_avisa(self):
        self.escribir("analisis/proyecto-analisis-principal.md", PRINCIPAL.replace("](../documentacion/7-algo/analisis-1.md)", "](otro.md)"))
        self.escribir("documentacion/7-algo/analisis-1.md", documento())
        avisos = analisis.fuera_de_la_lista(self.raiz)
        self.assertEqual(len(avisos), 1)
        self.assertIn("«Lista de análisis»", avisos[0][1])

    def test_cp004_el_que_esta_en_la_lista_no_avisa(self):
        self.escribir("analisis/proyecto-analisis-principal.md", PRINCIPAL)
        self.escribir("documentacion/7-algo/analisis-1.md", documento())
        self.assertEqual(analisis.fuera_de_la_lista(self.raiz), [])

    def test_cp006_aprobado_antes_no_se_le_exige(self):
        self.assertEqual(self.fallas(nuevo(version="43.0.0", recomendaciones="", donde="", hu="")), [])

    def test_cp006_sin_version_en_la_marca_no_se_le_exige(self):
        self.assertEqual(self.fallas(documento()), [])

    def test_cp006_aprobado_con_la_44_sin_las_secciones_falla(self):
        self.assertEqual(len(self.fallas(nuevo(recomendaciones="", donde=""))), 2)

    def test_cp009_la_copia_cambiada_falla(self):
        self.escribir("analisis/proyecto-analisis-principal.md", PRINCIPAL.replace("tiene suma", "tiene resta"))
        fallas = self.fallas(nuevo())
        self.assertEqual(len(fallas), 1)
        self.assertIn("no está tal cual", fallas[0])

    def test_cp009_la_copia_igual_pasa(self):
        self.escribir("analisis/proyecto-analisis-principal.md", PRINCIPAL)
        self.assertEqual(self.fallas(nuevo()), [])

    def test_los_prompts_no_son_analisis(self):
        self.escribir("analisis/proyecto-analisis-principal.md", PRINCIPAL)
        self.escribir("prompts/analisis/un-pedido.md", "# Lo que pidió el usuario\n")
        self.escribir("documentacion/7-algo/analisis-1.md", documento())
        self.assertEqual(analisis.fuera_de_la_lista(self.raiz), [])


if __name__ == "__main__":
    unittest.main()
