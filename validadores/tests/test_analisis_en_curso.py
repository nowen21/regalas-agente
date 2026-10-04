# -*- coding: utf-8 -*-
"""`EP-023 · HU-001 · fase B` · La conversación pasa sola al análisis prendido.

Los casos CP-001 a CP-006 del plan de pruebas de la fase, sobre una carpeta
temporal con una transcripción y pendientes de prueba.
"""
import io
import json
import os
import re
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

    def test_los_puntos_suspensivos_pasan_a_tres_puntos(self):
        self.assertEqual(curso._limpiar("### 1 · Usuario — hora\n> Analicemos: …\n"),
                         "### 1 · Usuario, hora\n> Analicemos: ...\n")

    def llenar(self, ruta, turno_acordado):
        """Lo mínimo para que el análisis salido de la plantilla pase la revisión de origen."""
        curso.pasar(self.raiz)
        texto = self.leer(ruta).replace("1. «tema»: «lo que se decidió» (turno «N»).",
                                        "1. Algo: se hace (turno %d)." % turno_acordado)
        texto = re.sub(r"^\| 1 \| Pasar el pendiente.*\n", "", texto, flags=re.M)
        self.escribir(ruta, texto.replace("| «número» |", "| 1 |"))


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
                          "## Lo acordado\n\nNota del usuario.\n")
        curso._guardar_estado(self.raiz, {"analisis": a1, "transcripcion": self.trans,
                                          "desde": 1, "pausa": None, "pausas": []})
        self.agregar(turno(1, "uno"))
        curso.pasar(self.raiz)
        self.agregar(turno(2, "dos"))
        curso.pasar(self.raiz)
        texto = self.leer(a1)
        self.assertIn("### 2 · Usuario", texto)
        self.assertTrue(texto.endswith("## Lo acordado\n\nNota del usuario.\n"))


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
        self.llenar(a1, 6)
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

    def test_h6_se_apaga_aunque_la_respuesta_llegue_tarde(self):
        """H-6: al cerrar el turno que aprobó, la respuesta aún no está escrita."""
        self.agregar(turno(1, "Analicemos: el pendiente 7"))
        curso.prender(self.raiz, 7, self.trans, 1)
        a1 = os.path.join(self.p7, "analisis-1.md")
        self.agregar("### 2 · Usuario — 2026-10-02 10:02:00\n> Apruebo el análisis\n\n")
        self.llenar(a1, 1)
        self.assertTrue(curso.aprobar(self.raiz, 2, "2026-10-02"))
        curso.pasar(self.raiz)
        self.assertIsNotNone(curso.leer_estado(self.raiz))
        self.agregar("**Agente** — 2026-10-02 10:02:30\n\nAprobado.\n\n" + turno(3, "Escriba"))
        curso.pasar(self.raiz)
        self.assertIsNone(curso.leer_estado(self.raiz))
        texto = self.leer(a1)
        self.assertIn("Aprobado.", texto)
        self.assertNotIn("### 3 · Usuario", texto)

    def test_h9_la_respuesta_pasa_apenas_se_escribe(self):
        """H-9: la respuesta la pasa el histórico después de escribirla, no un enganche paralelo."""
        adaptador = os.path.join(os.path.dirname(HOOK), "hook_historico.py")
        with open(adaptador, encoding="utf-8") as f:
            texto = f.read()
        self.assertLess(texto.index("historico.anotar_agente("), texto.index("analisis_en_curso.pasar(raiz)"))
        import instalar
        self.assertFalse([h for h in instalar.HOOKS_CLAUDE if h[0] == "Stop" and h[2] == "hook_analisis.py"])
        # Lo que hace el histórico al cerrar: anota la respuesta y pasa; la respuesta queda.
        self.agregar(turno(1, "Analicemos: el pendiente 7").split("**Agente**")[0])
        curso.prender(self.raiz, 7, self.trans, 1)
        self.agregar("**Agente** — 2026-10-02 10:01:30\n\nLa respuesta.\n\n")
        curso.pasar(self.raiz)
        self.assertIn("La respuesta.", self.leer(os.path.join(self.p7, "analisis-1.md")))

    def test_el_enlace_a_lo_que_se_movio_pasa_como_texto(self):
        self.agregar(turno(1, "Analicemos: el pendiente 7", "Quedó en [el archivo](otro/movido.md)."))
        curso.prender(self.raiz, 7, self.trans, 1)
        curso.pasar(self.raiz)
        texto = self.leer(os.path.join(self.p7, "analisis-1.md"))
        self.assertIn("el archivo (`otro/movido.md`, ya no está ahí)", texto)
        self.assertNotIn("](", texto.split("## Conversación")[1].split("acá termina")[0])

    def test_h6_lo_que_entro_despues_de_aprobar_sale(self):
        self.agregar(turno(1, "Analicemos: el pendiente 7"))
        curso.prender(self.raiz, 7, self.trans, 1)
        a1 = os.path.join(self.p7, "analisis-1.md")
        self.agregar(turno(2, "Apruebo el análisis"))
        estado = curso.leer_estado(self.raiz)
        self.agregar(turno(3, "Escriba"))
        curso.pasar(self.raiz)
        self.assertIn("### 3 · Usuario", self.leer(a1))
        self.llenar(a1, 1)
        self.assertTrue(curso.aprobar(self.raiz, 2, "2026-10-02"))
        curso._guardar_estado(self.raiz, estado)
        curso.pasar(self.raiz)
        texto = self.leer(a1)
        self.assertIn("### 2 · Usuario", texto)
        self.assertNotIn("### 3 · Usuario", texto)
        self.assertIsNone(curso.leer_estado(self.raiz))


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

    def test_cp010_el_aviso_dice_por_que_no_se_aprobo(self):
        a1 = os.path.join(self.p7, "analisis-1.md")
        self.escribir(a1, ANALISIS.replace(FILA, ""))
        curso._guardar_estado(self.raiz, {"analisis": a1, "transcripcion": self.trans,
                                          "desde": 1, "pausa": None, "pausas": []})
        _, texto = self.correr("Apruebo el análisis")
        self.assertIn("No se aprobó: falta al menos una fila", texto)
        self.assertNotIn("**Aprobado**", self.leer(a1))


# ── Fase D: aprobar revisa, marca la versión y pasa lo que suma ─────────────

FILA = "| 1 | Hacer algo | 1 | EP-009, HU-001 |\n"
APORTA = ("## Lo que aporta al análisis principal\n\n**Resultado:** Ratifica.\n\n"
          "**Lo que suma al análisis principal:** La clase tiene suma.\n")
ANALISIS = ("# Análisis 1: algo\n\n## Conversación\n\n### 1 · Usuario, 2026-10-02 10:00:00\n> Algo\n\n"
            "> acá termina la conversación\n\n## Lo acordado\n\n1. Algo: se hace (turno 1).\n\n"
            "## Lo que se tiene que hacer\n\n| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |\n"
            "|---|---|---|---|\n" + FILA + "\n" + APORTA)
PRINCIPAL = ("# Análisis principal\n\n## Qué es\n\nCimiento es algo.\n\n"
             "## Lista de análisis\n\n| Fecha | Resultado | Análisis |\n|---|---|---|\n")


class AprobarRevisaYPasaAlPrincipal(Base):

    def preparar(self, texto, carpeta=None):
        carpeta = carpeta or self.p7
        ruta = os.path.join(carpeta, "analisis-1.md")
        self.escribir(ruta, texto)
        curso._guardar_estado(self.raiz, {"analisis": ruta, "transcripcion": self.trans,
                                          "desde": 1, "pausa": None, "pausas": []})
        return ruta

    def test_cp006_la_marca_dice_la_version(self):
        a1 = self.preparar(ANALISIS)
        self.assertTrue(curso.aprobar(self.raiz, 7, "2026-10-02"))
        self.assertIn(", con la versión %s." % curso.version(), self.leer(a1))
        self.assertTrue(curso.aprobado(a1))
        self.assertEqual(curso.turno_aprobado(a1), 7)

    def test_cp009_lo_que_suma_pasa_tal_cual_al_principal(self):
        principal = os.path.join(self.raiz, "analisis", "proyecto-analisis-principal.md")
        self.escribir(principal, PRINCIPAL)
        a1 = self.preparar(ANALISIS)
        self.assertTrue(curso.aprobar(self.raiz, 7, "2026-10-02"))
        texto = self.leer(principal)
        self.assertIn("Cimiento es algo. La clase tiene suma.\n\n## Lista de análisis", texto)
        self.assertTrue(texto.endswith(
            "| 2026-10-02 | Ratifica | [Análisis 1 del pendiente 7](../documentacion/7-algo-que-falla/analisis-1.md) |\n"))
        import analisis
        self.assertEqual(analisis.copias(self.raiz), [])
        self.assertEqual(analisis.fuera_de_la_lista(self.raiz), [])
        self.assertTrue(os.path.isfile(a1))

    def test_cp009_el_modulo_con_principal_propio_lo_usa(self):
        del_proyecto = os.path.join(self.raiz, "analisis", "proyecto-analisis-principal.md")
        del_modulo = os.path.join(self.raiz, "ventas", "analisis", "ventas-analisis-principal.md")
        self.escribir(del_proyecto, PRINCIPAL)
        self.escribir(del_modulo, PRINCIPAL)
        self.preparar(ANALISIS, os.path.join(self.raiz, "ventas", "documentacion", "8-otra-cosa"))
        self.assertTrue(curso.aprobar(self.raiz, 7, "2026-10-02"))
        self.assertIn("La clase tiene suma.", self.leer(del_modulo))
        self.assertNotIn("La clase tiene suma.", self.leer(del_proyecto))

    def test_cp010_sin_filas_no_se_aprueba(self):
        a1 = self.preparar(ANALISIS.replace(FILA, ""))
        self.assertEqual(curso.por_que_no_se_aprueba(self.raiz), ["falta al menos una fila en «Lo que se tiene que hacer»"])
        self.assertFalse(curso.aprobar(self.raiz, 7, "2026-10-02"))
        self.assertFalse(curso.aprobado(a1))

    def test_cp011_sin_lo_que_aporta_no_se_aprueba(self):
        a1 = self.preparar(ANALISIS.replace(APORTA, ""))
        self.assertFalse(curso.aprobar(self.raiz, 7, "2026-10-02"))
        self.assertFalse(curso.aprobado(a1))
        self.assertIn("Lo que aporta al análisis principal", curso.por_que_no_se_aprueba(self.raiz)[0])

    def test_cp011_sin_lo_que_suma_no_se_aprueba(self):
        a1 = self.preparar(ANALISIS.replace("**Lo que suma al análisis principal:** La clase tiene suma.\n", ""))
        self.assertFalse(curso.aprobar(self.raiz, 7, "2026-10-02"))
        self.assertFalse(curso.aprobado(a1))

    def test_con_una_falla_de_origen_no_se_aprueba(self):
        a1 = self.preparar(ANALISIS.replace(FILA, "| 1 | Hacer algo | 2 | EP-009, HU-001 |\n"))
        self.assertIn("cita el punto 2 de «Lo acordado», que no existe", curso.por_que_no_se_aprueba(self.raiz)[0])
        self.assertFalse(curso.aprobar(self.raiz, 7, "2026-10-02"))
        self.assertFalse(curso.aprobado(a1))

    def test_la_fila_puede_citar_el_acuerdo_de_otro_analisis(self):
        self.escribir(os.path.join(self.p7, "analisis-1.md"), "# Análisis 1\n\n## Lo acordado\n\n5. Otro: algo (turno 1).\n")
        self.escribir(os.path.join(self.p7, "pendiente.md"),
                      "# Pendiente: algo que falla\n\n| | |\n|---|---|\n| **De dónde sale** | H-1 |\n")
        a2 = os.path.join(self.p7, "analisis-2.md")
        self.escribir(a2, ANALISIS.replace("# Análisis 1: algo\n", "# Análisis 2: algo\n\n## Hallazgo\n\n### H-1 · Algo\n").replace(
            FILA, FILA + "| 2 | Pasar el pendiente | Análisis 1, acuerdo 5 | Este análisis, de una |\n"))
        curso._guardar_estado(self.raiz, {"analisis": a2, "transcripcion": self.trans,
                                          "desde": 1, "pausa": None, "pausas": []})
        self.assertEqual(curso.por_que_no_se_aprueba(self.raiz), [])
        self.escribir(a2, self.leer(a2).replace("acuerdo 5", "acuerdo 6"))
        self.assertIn("cita el acuerdo 6 del análisis 1, que no existe", curso.por_que_no_se_aprueba(self.raiz)[0])

    def test_la_plantilla_trae_lo_que_pide_aprobar(self):
        with open(os.path.join(curso.comun.RAIZ, curso.PLANTILLA), encoding="utf-8") as f:
            self.assertEqual(curso.faltantes(f.read()), [])


if __name__ == "__main__":
    unittest.main()
