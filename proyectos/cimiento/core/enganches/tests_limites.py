# -*- coding: utf-8 -*-
"""`EP-025·HU-009`: con cada mensaje se avisa el enganche o el archivo del turno
anterior que pasó el límite de su proyecto, una sola vez.

Sin Django: corren con `python -m unittest core.enganches.tests_limites` desde
`proyectos/cimiento/`. Las transcripciones son muestras con la forma verificada
el 2026-10-05.
"""
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

from ..consumo.lector import CARACTERES_POR_TOKEN, LectorDeClaudeCode, estimar_tokens
from .niveles import BaseSinRespuesta, LimitesDelProyecto
from .presupuesto import Presupuesto

ESTANDAR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))))
ENGANCHE = os.path.join(ESTANDAR, "adaptadores", "claude-code", "hook_presupuesto.py")


def caracteres(tokens):
    return "x" * int(tokens * CARACTERES_POR_TOKEN)


def pedido(texto):
    return {"type": "user", "sessionId": "s", "message": {"content": [{"type": "text", "text": texto}]}}


def contexto(uuid, nombre, tokens):
    return [{"type": "attachment", "sessionId": "s", "uuid": uuid + "-ok",
             "attachment": {"type": "hook_success", "hookName": "UserPromptSubmit", "toolUseID": uuid,
                            "command": nombre,
                            "stdout": json.dumps({"hookSpecificOutput": {"additionalContext": caracteres(tokens)}})}},
            {"type": "attachment", "sessionId": "s", "uuid": uuid,
             "attachment": {"type": "hook_additional_context", "hookName": "UserPromptSubmit", "toolUseID": uuid,
                            "hookEvent": "UserPromptSubmit", "content": [caracteres(tokens)]}}]


def lectura(identificador, ruta, tokens):
    return [{"type": "assistant", "sessionId": "s", "message": {
                "id": "m-" + identificador, "model": "m", "usage": {"input_tokens": 1, "output_tokens": 1},
                "content": [{"type": "tool_use", "id": identificador, "name": "Read", "input": {"file_path": ruta}}]}},
            {"type": "user", "sessionId": "s", "message": {"content": [
                {"type": "tool_result", "tool_use_id": identificador, "content": caracteres(tokens)}]}}]


def respuesta():
    return {"type": "assistant", "sessionId": "s",
            "message": {"id": "fin", "model": "m", "usage": {"input_tokens": 1, "output_tokens": 1},
                        "content": [{"type": "text", "text": "listo"}]}}


class ConTranscripcion(unittest.TestCase):

    def setUp(self):
        carpeta = tempfile.TemporaryDirectory()
        self.addCleanup(carpeta.cleanup)
        self.ruta = os.path.join(carpeta.name, "s.jsonl")

    def escribir(self, *grupos):
        with io.open(self.ruta, "a", encoding="utf-8", newline="\n") as archivo:
            for grupo in grupos:
                for dato in (grupo if isinstance(grupo, list) else [grupo]):
                    archivo.write(json.dumps(dato) + "\n")

    def primer_turno(self):
        """Primer mensaje: un enganche de 150 tokens y uno de 50; un archivo de
        1500 y uno de exactamente 1000."""
        self.escribir(pedido("hágalo"), contexto("e-1", "Revisando las reglas...", 150),
                      contexto("e-2", "Marcando...", 50), lectura("t-1", "C:/p/grande.md", 1500),
                      lectura("t-2", "C:/p/justo.md", 1000), respuesta())

    def aviso(self, limites=(100, 1000)):
        turno = LectorDeClaudeCode(self.ruta).turno_anterior()
        enganches = Presupuesto.pasados_del_limite(
            ((e.nombre, estimar_tokens(e.caracteres)) for e in turno.enganches), limites[0])
        archivos = Presupuesto.pasados_del_limite(
            ((a.ruta, estimar_tokens(a.caracteres)) for a in turno.archivos), limites[1])
        return Presupuesto.aviso_de_limites(enganches, archivos, *limites)


class LoQuePasaElLimiteSeAvisa(ConTranscripcion):
    """CP-001."""

    def test_con_el_mensaje_siguiente_ya_escrito(self):
        self.primer_turno()
        self.escribir(pedido("continúe"))
        turno = LectorDeClaudeCode(self.ruta).turno_anterior()
        self.assertEqual((2, 2), (len(turno.enganches), len(turno.archivos)))

    def test_sin_que_el_mensaje_siguiente_este_escrito(self):
        self.primer_turno()
        turno = LectorDeClaudeCode(self.ruta).turno_anterior()
        self.assertEqual((2, 2), (len(turno.enganches), len(turno.archivos)))

    def test_solo_lo_que_pasa_y_justo_en_el_limite_no(self):
        self.primer_turno()
        self.escribir(pedido("continúe"))
        texto = self.aviso()
        self.assertIn("El enganche «Revisando las reglas...» agregó unos 150 tokens", texto)
        self.assertIn("Leer «C:/p/grande.md» ocupó unos 1.500 tokens", texto)
        self.assertNotIn("Marcando", texto)
        self.assertNotIn("justo.md", texto)

    def test_el_mismo_enganche_dos_veces_sale_una(self):
        self.escribir(pedido("hágalo"), contexto("e-1", "Reglas", 150), contexto("e-2", "Reglas", 300), respuesta())
        texto = self.aviso()
        self.assertEqual(1, texto.count("«Reglas»"))
        self.assertIn("unos 300 tokens (2 veces)", texto)

    def test_el_enganche_entero_avisa_y_sale_con_cero(self):
        """Sin base (un puerto donde no hay nada), con los límites por defecto: 2000 y 10 000."""
        self.escribir(pedido("hágalo"), contexto("e-1", "Revisando las reglas...", 2500),
                      lectura("t-1", "C:/p/grande.md", 1500), respuesta(), pedido("continúe"))
        entrada = json.dumps({"transcript_path": self.ruta})
        with mock.patch.dict(os.environ, {"DB_PUERTO": "1"}):
            corrida = subprocess.run([sys.executable, ENGANCHE, "--modo", "aviso", "--raiz", tempfile.gettempdir()],
                                     input=entrada, capture_output=True, text=True, encoding="utf-8", timeout=60)
        self.assertEqual(0, corrida.returncode, corrida.stderr)
        self.assertIn("«Revisando las reglas...» agregó unos 2.500 tokens; el límite del proyecto es 2.000",
                      corrida.stdout)
        self.assertNotIn("grande.md", corrida.stdout)

    def test_sin_transcripcion_sale_con_cero_y_callado(self):
        corrida = subprocess.run([sys.executable, ENGANCHE, "--modo", "aviso"], input="{}",
                                 capture_output=True, text=True, encoding="utf-8", timeout=60)
        self.assertEqual((0, ""), (corrida.returncode, corrida.stdout))


class ElLectorVeTodosLosEnganches(ConTranscripcion):
    """Visto al probar el CP-003 con la sesión real: dos formas de enganche que el lector no nombraba o no contaba."""

    def test_el_texto_plano_de_un_mensaje_llega_al_modelo_y_cuenta(self):
        senal = {"type": "attachment", "sessionId": "s", "uuid": "u-s",
                 "attachment": {"type": "hook_success", "hookName": "UserPromptSubmit", "hookEvent": "UserPromptSubmit",
                                "toolUseID": "x", "command": "Revisando las señales...", "stdout": caracteres(200)}}
        al_cerrar = dict(senal, uuid="u-c", attachment=dict(senal["attachment"], hookEvent="Stop", hookName="Stop"))
        self.escribir(pedido("hágalo"), senal, al_cerrar, respuesta())
        enganches = LectorDeClaudeCode(self.ruta).turno_anterior().enganches
        self.assertEqual([("Revisando las señales...", 200)], [(e.nombre, estimar_tokens(e.caracteres)) for e in enganches])

    def test_sin_hermano_se_nombra_por_su_titulo(self):
        regla = {"type": "attachment", "sessionId": "s", "uuid": "u-r",
                 "attachment": {"type": "hook_additional_context", "hookName": "UserPromptSubmit", "toolUseID": "hook-1",
                                "hookEvent": "UserPromptSubmit", "content": ["[LAS REGLAS DE CADA TURNO]\nlo demás"]}}
        self.escribir(pedido("hágalo"), regla, respuesta())
        self.assertEqual(["LAS REGLAS DE CADA TURNO"],
                         [e.nombre for e in LectorDeClaudeCode(self.ruta).turno_anterior().enganches])


class CadaExcesoSeAvisaUnaVez(ConTranscripcion):
    """CP-002."""

    def test_el_turno_siguiente_sin_excesos_no_avisa(self):
        self.primer_turno()
        self.escribir(pedido("continúe"), contexto("e-3", "Revisando las reglas...", 20), respuesta(),
                      pedido("otra cosa"))
        self.assertEqual("", self.aviso())


class LosLimitesSonLosDelProyecto(unittest.TestCase):
    """CP-003."""

    def limites(self, filas=None, error=None):
        limites = LimitesDelProyecto("C:/p", "C:/estandar", ajustes={"HOST": "h", "PORT": "1"})
        with mock.patch.object(LimitesDelProyecto, "consultar", side_effect=error, return_value=filas):
            return limites.limites()

    def test_los_del_registro(self):
        self.assertEqual((100, 500), self.limites(filas=((100, 500),)))

    def test_sin_registro_los_de_por_defecto(self):
        self.assertEqual((2000, 10000), self.limites(filas=()))

    def test_sin_base_los_de_por_defecto(self):
        self.assertEqual((2000, 10000), self.limites(error=BaseSinRespuesta("MariaDB no responde")))
