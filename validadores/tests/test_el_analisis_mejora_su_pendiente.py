# -*- coding: utf-8 -*-
"""`EP-023 · HU-003 · CA-09` · Cada análisis deja el pendiente en su versión siguiente.

CP-001: sin el hallazgo en el pendiente, no se aprueba; con él, sí; sin número, no.
CP-002: el análisis 1 no se revisa.
CP-003: la plantilla pide el pendiente en su versión siguiente.
"""
import os
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import analisis_en_curso as curso   # noqa: E402

CONVERSACION = ("## Conversación\n\n### 1 · Usuario, 2026-10-03 10:00:00\n> Algo\n\n"
                "> acá termina la conversación\n\n## Lo acordado\n\n1. Algo: se hace (turno 1).\n\n")
RESTO = ("## Lo que se tiene que hacer\n\n| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |\n"
         "|---|---|---|---|\n| 1 | Hacer algo | 1 | EP-009, HU-001 |\n\n"
         "## Lo que aporta al análisis principal\n\n**Resultado:** Ratifica.\n\n"
         "**Lo que suma al análisis principal:** Algo.\n")


def analisis(numero, hallazgo="### H-7 · Algo falla\n"):
    return "# Análisis %d: algo\n\n## Hallazgo\n\n%s\n%s%s" % (numero, hallazgo, CONVERSACION, RESTO)


def pendiente(de_donde_sale):
    return "# Pendiente: algo\n\n| | |\n|---|---|\n| **De dónde sale** | %s |\n" % de_donde_sale


class ElAnalisisMejoraSuPendiente(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.raiz = self.tmp.name
        self.carpeta = os.path.join(self.raiz, "documentacion", "7-algo")
        self.trans = os.path.join(self.raiz, "historico-chat", "sesion.md")
        self.escribir(self.trans, "# Sesión\n")

    def tearDown(self):
        self.tmp.cleanup()

    def escribir(self, ruta, texto):
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(texto)

    def prender(self, numero, texto):
        ruta = os.path.join(self.carpeta, "analisis-%d.md" % numero)
        self.escribir(ruta, texto)
        curso._guardar_estado(self.raiz, {"analisis": ruta, "transcripcion": self.trans,
                                          "desde": 1, "pausa": None, "pausas": []})
        return ruta

    def test_cp001_sin_el_hallazgo_en_el_pendiente_no_se_aprueba(self):
        self.escribir(os.path.join(self.carpeta, "pendiente.md"), pendiente("H-3"))
        ruta = self.prender(2, analisis(2))
        faltan = curso.por_que_no_se_aprueba(self.raiz)
        self.assertEqual(len(faltan), 1)
        self.assertIn("falta el H-7 en «De dónde sale» del pendiente", faltan[0])
        self.assertFalse(curso.aprobar(self.raiz, 1, "2026-10-03"))
        self.assertFalse(curso.aprobado(ruta))

    def test_cp001_con_el_hallazgo_en_el_pendiente_se_aprueba(self):
        self.escribir(os.path.join(self.carpeta, "pendiente.md"), pendiente("H-3 y [H-7](x.md)"))
        ruta = self.prender(2, analisis(2))
        self.assertEqual(curso.por_que_no_se_aprueba(self.raiz), [])
        self.assertTrue(curso.aprobar(self.raiz, 1, "2026-10-03"))
        self.assertTrue(curso.aprobado(ruta))

    def test_cp001_sin_numero_de_hallazgo_no_se_aprueba(self):
        self.escribir(os.path.join(self.carpeta, "pendiente.md"), pendiente("H-7"))
        self.prender(2, analisis(2, hallazgo="Algo falla, sin número.\n"))
        self.assertIn("falta el número del hallazgo", curso.por_que_no_se_aprueba(self.raiz)[0])

    def test_cp001_un_numero_parecido_no_cuenta(self):
        self.escribir(os.path.join(self.carpeta, "pendiente.md"), pendiente("H-70"))
        self.prender(2, analisis(2))
        self.assertIn("falta el H-7", curso.por_que_no_se_aprueba(self.raiz)[0])

    def test_cp002_el_analisis_1_no_se_revisa(self):
        self.escribir(os.path.join(self.carpeta, "pendiente.md"), pendiente("H-3"))
        ruta = self.prender(1, analisis(1))
        self.assertEqual(curso.por_que_no_se_aprueba(self.raiz), [])
        self.assertTrue(curso.aprobar(self.raiz, 1, "2026-10-03"))
        self.assertTrue(curso.aprobado(ruta))

    def test_cp003_la_plantilla_pide_el_pendiente_en_su_version_siguiente(self):
        with open(os.path.join(curso.comun.RAIZ, curso.PLANTILLA), encoding="utf-8") as f:
            texto = f.read()
        propuesta = curso.seccion(texto, "Propuesta final")
        self.assertIn("### Pendiente V«N+1»", propuesta)
        self.assertIn("Antes de aprobar, se pasan a los originales", propuesta)


if __name__ == "__main__":
    unittest.main()
