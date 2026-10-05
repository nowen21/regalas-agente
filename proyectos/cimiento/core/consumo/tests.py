"""`EP-025·HU-006`: el lector del formato de Claude Code, el guardado sin
duplicar, las líneas rotas y la orden `leer_consumo`. Los `.jsonl` son
muestras armadas acá, con la forma verificada el 2026-10-05."""
import io
import json
import os
import shutil
import sys
import tempfile
from unittest import mock

from django.core.management import call_command
from django.test import SimpleTestCase, TestCase

from core.consumo.guardar import GuardadoDeConsumo
from core.consumo.lector import CARACTERES_POR_TOKEN, LectorDeClaudeCode, estimar_tokens
from core.consumo.models import AvanceDeLectura, GastoDeArchivo, GastoDeEnganche, Llamada
from core.proyectos.models import Proyecto

SESION = "s-1"
CONTEXTO = "[REGLAS] lo que llega con cada mensaje"


def llamada(mensaje, entrada=10, salida=5, cache=100, creada=2, contenido=None):
    return {"type": "assistant", "sessionId": SESION, "timestamp": "2026-10-05T10:00:00Z",
            "message": {"id": mensaje, "model": "claude-opus-5-5", "content": contenido or [],
                        "usage": {"input_tokens": entrada, "output_tokens": salida,
                                  "cache_read_input_tokens": cache, "cache_creation_input_tokens": creada}}}


def muestra():
    """Dos llamadas (una partida en dos líneas), un enganche con nombre, un
    bloqueo y un archivo leído."""
    lectura = {"type": "tool_use", "id": "t-1", "name": "Read", "input": {"file_path": "C:/p/a.md"}}
    return [
        {"type": "attachment", "sessionId": SESION, "uuid": "u-1", "timestamp": "2026-10-05T09:59:00Z",
         "attachment": {"type": "hook_success", "hookName": "UserPromptSubmit", "toolUseID": "x",
                        "command": "Revisando las reglas...",
                        "stdout": json.dumps({"hookSpecificOutput": {"additionalContext": CONTEXTO}})}},
        {"type": "attachment", "sessionId": SESION, "uuid": "u-2", "timestamp": "2026-10-05T09:59:00Z",
         "attachment": {"type": "hook_additional_context", "hookName": "UserPromptSubmit", "toolUseID": "x",
                        "hookEvent": "UserPromptSubmit", "content": [CONTEXTO]}},
        llamada("m-1", contenido=[lectura]),
        llamada("m-1", contenido=[{"type": "text", "text": "sigue"}]),
        {"type": "user", "sessionId": SESION, "timestamp": "2026-10-05T10:00:01Z",
         "message": {"content": [{"type": "tool_result", "tool_use_id": "t-1", "content": "x" * 70}]}},
        {"type": "attachment", "sessionId": SESION, "uuid": "u-3", "timestamp": "2026-10-05T10:00:02Z",
         "attachment": {"type": "hook_blocking_error", "hookName": "PostToolUse:Bash", "hookEvent": "PostToolUse",
                        "blockingError": {"blockingError": "y" * 35, "command": "Comparando con el plan..."}}},
        llamada("m-2", entrada=1, salida=1, cache=0, creada=0),
    ]


def escribir_jsonl(ruta, datos, crudo_al_final=""):
    with open(ruta, "a", encoding="utf-8", newline="\n") as archivo:
        for dato in datos:
            archivo.write(json.dumps(dato) + "\n")
        archivo.write(crudo_al_final)


class ElLector(SimpleTestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.ruta = os.path.join(self.tmp, SESION + ".jsonl")

    def test_saca_llamadas_enganches_y_archivos(self):
        escribir_jsonl(self.ruta, muestra())
        lectura = LectorDeClaudeCode(self.ruta).leer()
        self.assertEqual(["m-1", "m-2"], [l.mensaje for l in lectura.llamadas])
        primera = lectura.llamadas[0]
        self.assertEqual((10, 2, 100, 5, "claude-opus-5-5"),
                         (primera.entrada, primera.cache_creada, primera.cache_leida, primera.salida, primera.modelo))
        self.assertEqual([("Revisando las reglas...", len(CONTEXTO)), ("Comparando con el plan...", 35)],
                         [(e.nombre, e.caracteres) for e in lectura.enganches])
        self.assertEqual([("C:/p/a.md", 70)], [(a.ruta, a.caracteres) for a in lectura.archivos])

    def test_la_estimacion_usa_una_sola_constante(self):
        self.assertEqual(estimar_tokens(70), round(70 / CARACTERES_POR_TOKEN))

    def test_una_linea_ilegible_se_salta(self):
        escribir_jsonl(self.ruta, muestra()[:3], crudo_al_final="{esto no es json\n")
        escribir_jsonl(self.ruta, [llamada("m-3")])
        self.assertEqual(["m-1", "m-3"], [l.mensaje for l in LectorDeClaudeCode(self.ruta).leer().llamadas])

    def test_la_ultima_linea_sin_salto_queda_para_despues(self):
        escribir_jsonl(self.ruta, [llamada("m-1")], crudo_al_final=json.dumps(llamada("m-2"))[:30])
        lectura = LectorDeClaudeCode(self.ruta).leer()
        self.assertEqual(["m-1"], [l.mensaje for l in lectura.llamadas])
        self.assertLess(lectura.hasta, os.path.getsize(self.ruta))

    def test_no_guarda_texto(self):
        escribir_jsonl(self.ruta, muestra())
        lectura = LectorDeClaudeCode(self.ruta).leer()
        for evento in lectura.llamadas + lectura.enganches + lectura.archivos:
            self.assertNotIn(CONTEXTO, json.dumps(evento.__dict__, default=str))

    def test_la_suma_de_la_sesion_cuenta_una_vez_la_llamada_partida(self):
        escribir_jsonl(self.ruta, muestra())
        raiz = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.abspath(__file__))))))
        sys.path.insert(0, os.path.join(raiz, "adaptadores", "claude-code"))
        self.addCleanup(sys.path.remove, os.path.join(raiz, "adaptadores", "claude-code"))
        import hook_presupuesto
        consumos = hook_presupuesto.consumos_de_transcripcion(self.ruta)
        self.assertEqual([{"entrada": 12, "salida": 5, "cache": 100}, {"entrada": 1, "salida": 1, "cache": 0}],
                         consumos)


class LaOrdenGuardaSinDuplicar(TestCase):

    def setUp(self):
        self.base = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.base, True)
        self.ruta_proyecto = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.ruta_proyecto, True)
        self.proyecto = Proyecto.objects.create(nombre="uno", ruta=self.ruta_proyecto)
        os.makedirs(os.path.join(self.base, self.proyecto.carpeta_claude))
        self.jsonl = os.path.join(self.base, self.proyecto.carpeta_claude, SESION + ".jsonl")
        escribir_jsonl(self.jsonl, muestra())

    def correr(self):
        salida = io.StringIO()
        with mock.patch("core.consumo.guardar.proyectos_de_claude", return_value=self.base):
            call_command("leer_consumo", stdout=salida)
        return salida.getvalue()

    def cantidades(self):
        return (Llamada.objects.count(), GastoDeEnganche.objects.count(), GastoDeArchivo.objects.count())

    def test_guarda_lo_de_la_muestra(self):
        texto = self.correr()
        self.assertEqual((2, 2, 1), self.cantidades())
        self.assertIn("2 llamada(s), 2 enganche(s) y 1 archivo(s) leído(s) nuevos", texto)
        llamada_1 = Llamada.objects.get(mensaje="m-1")
        self.assertEqual((self.proyecto, SESION, 117), (llamada_1.proyecto, llamada_1.sesion, llamada_1.total))

    def test_dos_veces_no_duplica_y_no_vuelve_a_abrir(self):
        self.correr()
        with mock.patch("core.consumo.guardar.LectorDeClaudeCode") as lector:
            self.correr()
        lector.assert_not_called()
        self.assertEqual((2, 2, 1), self.cantidades())

    def test_lo_nuevo_se_suma(self):
        self.correr()
        escribir_jsonl(self.jsonl, [llamada("m-3")])
        self.assertIn("1 llamada(s)", self.correr())
        self.assertEqual(3, Llamada.objects.count())

    def test_la_linea_completada_despues_se_guarda(self):
        os.remove(self.jsonl)
        AvanceDeLectura.objects.all().delete()
        partida = json.dumps(llamada("m-9"))
        escribir_jsonl(self.jsonl, [llamada("m-1")], crudo_al_final=partida[:40])
        self.correr()
        self.assertEqual(1, Llamada.objects.count())
        with open(self.jsonl, "a", encoding="utf-8", newline="\n") as archivo:
            archivo.write(partida[40:] + "\n")
        self.correr()
        self.assertTrue(Llamada.objects.filter(mensaje="m-9").exists())

    def test_un_proyecto_inactivo_no_se_lee(self):
        self.proyecto.activo = False
        self.proyecto.save()
        self.assertIn("No hay proyectos activos", self.correr())
        self.assertEqual((0, 0, 0), self.cantidades())

    def test_tambien_los_de_los_agentes_auxiliares(self):
        """Hasta la HU-010 solo se leía la primera altura; desde ella, también `subagents/`."""
        auxiliar = os.path.join(self.base, self.proyecto.carpeta_claude, SESION, "subagents")
        os.makedirs(auxiliar)
        escribir_jsonl(os.path.join(auxiliar, "agent-1.jsonl"), [llamada("m-aux")])
        self.assertEqual([self.jsonl, os.path.join(auxiliar, "agent-1.jsonl")],
                         GuardadoDeConsumo(self.proyecto, self.base).archivos())
