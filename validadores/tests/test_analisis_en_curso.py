# -*- coding: utf-8 -*-
"""`EP-023 · HU-001 · fase B` · La conversación pasa sola al análisis prendido.

Los casos CP-001 a CP-006 del plan de pruebas de la fase, sobre una carpeta
temporal con una transcripción y pendientes de prueba.
"""
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import analisis_en_curso as curso   # noqa: E402
import marcas                       # noqa: E402

HOOK = os.path.join(os.path.dirname(VALIDADORES), "adaptadores", "claude-code", "hook_analisis.py")


def turno(n, usuario, agente="Respuesta."):
    return (f"### {n} · Usuario — 2026-10-02 10:0{n % 10}:00\n> {usuario}\n\n"
            f"**Agente** — 2026-10-02 10:0{n % 10}:30\n\n{agente}\n\n")


class Base(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.raiz = self.tmp.name
        os.makedirs(os.path.join(self.raiz, "historico-chat"))
        self.trans = os.path.join(self.raiz, "historico-chat", "2026-10-02-sesion.md")
        self.escribir(self.trans, "# Sesión\n\n")
        self.p7 = os.path.join(self.raiz, "documentacion", "7-algo-que-falla")
        self.escribir(os.path.join(self.p7, "pendiente.md"), "# Pendiente: algo que falla\n")

    def tearDown(self):
        self.tmp.cleanup()

    def escribir(self, ruta, texto):
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(texto)

    def leer(self, ruta):
        with open(ruta, encoding="utf-8") as f:
            return f.read()

    def agregar(self, texto):
        with open(self.trans, "a", encoding="utf-8") as f:
            f.write(texto)


class LaHerramientaLeeElEstado(Base):

    def test_cp001_escribe_en_el_analisis_del_estado(self):
        a1 = os.path.join(self.p7, "analisis-1.md")
        a2 = os.path.join(self.p7, "analisis-2.md")
        modelo = "# Análisis\n\n## Conversación\n\n> La escribe el enganche.\n\n> acá termina la conversación\n"
        self.escribir(a1, modelo)
        self.escribir(a2, modelo)
        self.agregar(turno(1, "hola") + turno(2, "sigue") + turno(3, "fin"))
        curso._guardar_estado(self.raiz, {"analisis": a2, "transcripcion": self.trans,
                                          "desde": 2, "pausa": None, "pausas": []})
        curso.pasar(self.raiz)
        self.assertIn("### 2 · Usuario", self.leer(a2))
        self.assertNotIn("### 1 · Usuario", self.leer(a2))
        self.assertEqual(self.leer(a1), modelo)
        self.assertTrue(os.path.isfile(HOOK))
        with open(os.path.join(VALIDADORES, "analisis_en_curso.py"), encoding="utf-8") as f:
            self.assertNotIn("analisis-1.md", f.read())

    def test_cp002_lo_agregado_a_mano_no_se_toca(self):
        a1 = os.path.join(self.p7, "analisis-1.md")
        self.escribir(a1, "# Análisis\n\n## Conversación\n\n> Nota.\n\n> acá termina la conversación\n\n"
                          "## Conclusiones\n\nNota del usuario.\n")
        curso._guardar_estado(self.raiz, {"analisis": a1, "transcripcion": self.trans,
                                          "desde": 1, "pausa": None, "pausas": []})
        self.agregar(turno(1, "uno"))
        curso.pasar(self.raiz)
        self.agregar(turno(2, "dos"))
        curso.pasar(self.raiz)
        texto = self.leer(a1)
        self.assertIn("### 2 · Usuario", texto)
        self.assertTrue(texto.endswith("## Conclusiones\n\nNota del usuario.\n"))


class SinMarcasNiEtiquetas(Base):

    def test_cp003(self):
        a1 = os.path.join(self.p7, "analisis-1.md")
        self.escribir(a1, "# Análisis\n\n## Conversación\n\n> Nota.\n\n> acá termina la conversación\n")
        self.agregar("### 1 · Usuario — 2026-10-02 10:00:00\n"
                     "> <ide_opened_file>The user opened x.md</ide_opened_file>\n"
                     "> <pasted_content id=\"1\">\n> texto pegado\n> </pasted_content id=\"1\">\n\n"
                     "**Agente** — 2026-10-02 10:00:30\n\nListo.\n\n")
        curso._guardar_estado(self.raiz, {"analisis": a1, "transcripcion": self.trans,
                                          "desde": 1, "pausa": None, "pausas": []})
        curso.pasar(self.raiz)
        texto = self.leer(a1)
        self.assertIn("### 1 · Usuario, 2026", texto)
        self.assertIn("**Agente**, 2026", texto)
        self.assertNotIn("pasted_content", texto)
        self.assertNotIn("ide_opened_file", texto)
        self.assertIn("texto pegado", texto)
        cuenta = sum(len(marcas.marcas_de_linea(l)) for l in texto.splitlines())
        self.assertEqual(cuenta, 0)


class PrenderPausarApagar(Base):

    def test_cp004(self):
        self.agregar(turno(1, "hola") + turno(2, "Analicemos: el pendiente 7"))
        self.assertEqual(curso.pendiente_pedido("Analicemos: el pendiente 7"), 7)
        prendido, _ = curso.prender(self.raiz, 7, self.trans, 2)
        self.assertTrue(prendido)
        a1 = os.path.join(self.p7, "analisis-1.md")
        self.assertTrue(os.path.isfile(a1))
        self.assertEqual(curso.leer_estado(self.raiz)["desde"], 2)

        self.agregar(turno(3, "tres") + turno(4, "Pare") + turno(5, "otra cosa"))
        self.assertTrue(curso.pausar(self.raiz, 4))
        self.agregar(turno(6, "Analicemos: el pendiente 7"))
        curso.prender(self.raiz, 7, self.trans, 6)
        curso.pasar(self.raiz)
        texto = self.leer(a1)
        self.assertIn("Turnos 4 a 5 en pausa", texto)
        self.assertNotIn("### 5 · Usuario", texto)
        self.assertIn("### 6 · Usuario", texto)

        self.agregar("### 7 · Usuario — 2026-10-02 10:07:00\n> Apruebo el análisis\n\n")
        self.assertTrue(curso.aprobar(self.raiz, 7, "2026-10-02"))
        self.assertIn("> **Aprobado** por el usuario el 2026-10-02, en el turno 7", self.leer(a1))
        curso.pasar(self.raiz)
        self.assertIsNotNone(curso.leer_estado(self.raiz))
        self.agregar("**Agente** — 2026-10-02 10:07:30\n\nAprobado.\n\n")
        curso.pasar(self.raiz)
        self.assertIsNone(curso.leer_estado(self.raiz))
        self.agregar(turno(8, "otra cosa"))
        curso.pasar(self.raiz)
        self.assertNotIn("### 8 · Usuario", self.leer(a1))

        self.assertIsNone(curso.pendiente_pedido("Analicemos por qué falla esto"))


class UnSoloAnalisisAbierto(Base):

    def test_cp005(self):
        hu = os.path.join(self.raiz, "documentacion", "epicas", "EP-009-x", "HU-002-y", "HU-002-y.md")
        self.escribir(hu, "| **Estado** | Lista |\n")
        self.escribir(os.path.join(self.p7, "analisis-1.md"),
                      "# Análisis 1\n\n> **Aprobado** por el usuario el 2026-10-01, en el turno 3.\n\n"
                      "## Lo que se tiene que hacer\n\n| # | Qué | Sale de | Pasó a |\n|---|---|---|---|\n"
                      "| 1 | Algo | 1 | EP-009, HU-002 |\n")
        p8 = os.path.join(self.raiz, "documentacion", "8-otra-cosa")
        self.escribir(os.path.join(p8, "pendiente.md"), "# Pendiente: otra cosa\n")
        self.agregar(turno(1, "Analicemos: el pendiente 8"))

        prendido, nota = curso.prender(self.raiz, 8, self.trans, 1)
        self.assertFalse(prendido)
        self.assertIn("analisis-1.md", nota)

        prendido, _ = curso.prender(self.raiz, 7, self.trans, 1)
        self.assertTrue(prendido)
        self.assertTrue(os.path.isfile(os.path.join(self.p7, "analisis-2.md")))

        os.remove(os.path.join(self.raiz, curso.ESTADO))
        os.remove(os.path.join(self.p7, "analisis-2.md"))
        self.escribir(hu, "| **Estado** | Terminada el 2026-10-02 |\n")
        prendido, _ = curso.prender(self.raiz, 8, self.trans, 1)
        self.assertTrue(prendido)


class ElAvisoDeCadaTurno(Base):

    def correr(self, mensaje):
        entrada = json.dumps({"prompt": mensaje, "session_id": "s1", "cwd": self.raiz})
        r = subprocess.run([sys.executable, HOOK, "--modo", "mensaje", "--raiz", self.raiz],
                           input=entrada.encode("utf-8"), capture_output=True, timeout=30)
        return r.returncode, json.loads(r.stdout.decode("utf-8"))["hookSpecificOutput"]["additionalContext"]

    def test_cp006(self):
        codigo, texto = self.correr("Pregunta: cómo va")
        self.assertEqual(codigo, 0)
        self.assertIn("Ningún análisis está prendido", texto)
        a1 = os.path.join(self.p7, "analisis-1.md")
        self.escribir(a1, "# Análisis\n\n## Conversación\n\n> Nota.\n\n> acá termina la conversación\n")
        curso._guardar_estado(self.raiz, {"analisis": a1, "transcripcion": self.trans,
                                          "desde": 1, "pausa": None, "pausas": []})
        codigo, texto = self.correr("Pregunta: cómo va")
        self.assertEqual(codigo, 0)
        self.assertIn("analisis-1.md", texto)


if __name__ == "__main__":
    unittest.main()
