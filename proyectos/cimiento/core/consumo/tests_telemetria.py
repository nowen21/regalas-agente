"""`EP-025·HU-007`: la telemetría de Claude Code llega a Cimiento y se guarda
sin duplicar lo que trae el `.jsonl`. Los envíos son muestras armadas acá,
con los nombres de la documentación de Claude Code, verificados el 2026-10-05."""
import gzip
import io
import json
import os
import shutil
import tempfile
from unittest import mock

from django.core.management import call_command
from django.test import SimpleTestCase, TestCase

from core.consumo.models import GastoDeArchivo, Llamada
from core.consumo.telemetria import EnvioInvalido, EventosDeTelemetria
from core.consumo.tests import SESION, escribir_jsonl, llamada
from core.proyectos.models import Proyecto

SOLICITUD = "req_1"


def atributo(clave, valor):
    if isinstance(valor, bool):
        return {"key": clave, "value": {"boolValue": valor}}
    if isinstance(valor, int):
        return {"key": clave, "value": {"intValue": str(valor)}}
    if isinstance(valor, float):
        return {"key": clave, "value": {"doubleValue": valor}}
    return {"key": clave, "value": {"stringValue": valor}}


def envio(*eventos, sesion=SESION):
    """Un envío OTLP JSON con `session.id` en el recurso, como lo arma Claude Code."""
    registros = [{"timeUnixNano": "1791194400000000000",
                  "attributes": [atributo(k, v) for k, v in evento.items()]} for evento in eventos]
    return json.dumps({"resourceLogs": [{
        "resource": {"attributes": [atributo("session.id", sesion), atributo("service.name", "claude-code")]},
        "scopeLogs": [{"logRecords": registros}]}]})


def pedido(solicitud=SOLICITUD, entrada=10):
    return {"event.name": "claude_code.api_request", "event.timestamp": "2026-10-05T10:00:00.000Z",
            "request_id": solicitud, "model": "claude-opus-5-5", "input_tokens": entrada, "output_tokens": 5,
            "cache_read_tokens": 100.0, "cache_creation_tokens": 2, "cost_usd": 0.01}


def lectura(identificador="t-9"):
    return {"event.name": "claude_code.tool_result", "tool_name": "Read", "tool_use_id": identificador,
            "success": True, "tool_result_size_bytes": 300,
            "tool_parameters": json.dumps({"file_path": "C:/p/b.md", "limit": 5})}


class ElEnvioSeLee(SimpleTestCase):
    """CP-001, paso 1."""

    def test_saca_la_llamada_y_el_archivo(self):
        llamadas, archivos = EventosDeTelemetria(envio(pedido(), lectura())).leer()
        self.assertEqual(1, len(llamadas))
        una = llamadas[0]
        self.assertEqual((SESION, SOLICITUD, SOLICITUD, "claude-opus-5-5", 10, 2, 100, 5),
                         (una.sesion, una.mensaje, una.solicitud, una.modelo, una.entrada,
                          una.cache_creada, una.cache_leida, una.salida))
        self.assertEqual(2026, una.fecha.year)
        self.assertEqual([("t-9", "C:/p/b.md", 300)], [(a.identificador, a.ruta, a.caracteres) for a in archivos])

    def test_lo_que_no_entiende_lo_salta(self):
        otra_herramienta = dict(lectura(), tool_name="Bash", tool_parameters=json.dumps({"command": "ls"}))
        llamadas, archivos = EventosDeTelemetria(envio({"event.name": "claude_code.user_prompt"},
                                                       otra_herramienta)).leer()
        self.assertEqual(([], []), (llamadas, archivos))

    def test_un_json_roto_es_invalido(self):
        with self.assertRaises(EnvioInvalido):
            EventosDeTelemetria(b"{roto")


class ConProyecto(TestCase):

    def setUp(self):
        self.base = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.base, True)
        self.ruta_proyecto = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.ruta_proyecto, True)
        self.proyecto = Proyecto.objects.create(nombre="uno", ruta=self.ruta_proyecto)
        os.makedirs(os.path.join(self.base, self.proyecto.carpeta_claude))
        self.jsonl = os.path.join(self.base, self.proyecto.carpeta_claude, SESION + ".jsonl")
        open(self.jsonl, "w").close()
        parche = mock.patch("core.consumo.guardar.proyectos_de_claude", return_value=self.base)
        parche.start()
        self.addCleanup(parche.stop)

    def mandar(self, cuerpo, desde="127.0.0.1", **cabeceras):
        return self.client.post("/v1/logs", data=cuerpo, content_type="application/json",
                                REMOTE_ADDR=desde, **cabeceras)

    def leer_jsonl(self):
        call_command("leer_consumo", stdout=io.StringIO())


class UnaLlamadaLlegaYQuedaGuardada(ConProyecto):
    """CP-001, paso 2."""

    def test_sin_cuenta_queda_en_la_base_con_su_proyecto(self):
        respuesta = self.mandar(envio(pedido(), lectura()))
        self.assertEqual((200, {}), (respuesta.status_code, respuesta.json()))
        una = Llamada.objects.get()
        self.assertEqual((self.proyecto, SESION, SOLICITUD, 117), (una.proyecto, una.sesion, una.solicitud, una.total))
        archivo = GastoDeArchivo.objects.get()
        self.assertEqual((self.proyecto, "C:/p/b.md", 300), (archivo.proyecto, archivo.ruta, archivo.caracteres))

    def test_comprimido_con_gzip_tambien(self):
        respuesta = self.mandar(gzip.compress(envio(pedido()).encode()), HTTP_CONTENT_ENCODING="gzip")
        self.assertEqual(200, respuesta.status_code)
        self.assertEqual(1, Llamada.objects.count())

    def test_no_guarda_texto(self):
        self.mandar(envio(pedido(), lectura()))
        guardado = json.dumps(list(GastoDeArchivo.objects.values()), default=str)
        self.assertNotIn("limit", guardado)


class LoQueNoValeNoSeGuarda(ConProyecto):
    """CP-002."""

    def test_otra_maquina_recibe_403(self):
        self.assertEqual(403, self.mandar(envio(pedido()), desde="192.168.1.20").status_code)
        self.assertFalse(Llamada.objects.exists())

    def test_json_roto_recibe_400(self):
        self.assertEqual(400, self.mandar("{roto").status_code)
        self.assertFalse(Llamada.objects.exists())

    def test_sesion_sin_proyecto_se_descarta(self):
        respuesta = self.mandar(envio(pedido(), lectura(), sesion="otra-sesion"))
        self.assertEqual(200, respuesta.status_code)
        self.assertEqual((0, 0), (Llamada.objects.count(), GastoDeArchivo.objects.count()))

    def test_una_sesion_con_ruta_no_sale_de_la_carpeta(self):
        self.mandar(envio(pedido(), sesion="../" + SESION))
        self.assertFalse(Llamada.objects.exists())

    def test_get_no_se_acepta(self):
        self.assertEqual(405, self.client.get("/v1/logs", REMOTE_ADDR="127.0.0.1").status_code)


class LaMismaLlamadaCuentaUnaVez(ConProyecto):
    """CP-003."""

    def jsonl_con_la_misma(self):
        linea = llamada("m-1")
        linea["requestId"] = SOLICITUD
        escribir_jsonl(self.jsonl, [linea])

    def test_telemetria_y_despues_jsonl(self):
        self.mandar(envio(pedido()))
        self.jsonl_con_la_misma()
        self.leer_jsonl()
        una = Llamada.objects.get()
        self.assertEqual(("m-1", SOLICITUD), (una.mensaje, una.solicitud))

    def test_jsonl_y_despues_telemetria(self):
        self.jsonl_con_la_misma()
        self.leer_jsonl()
        self.mandar(envio(pedido(entrada=999)))
        una = Llamada.objects.get()
        self.assertEqual(("m-1", 10), (una.mensaje, una.entrada))

    def test_el_mismo_envio_dos_veces(self):
        self.mandar(envio(pedido(), lectura()))
        self.mandar(envio(pedido(), lectura()))
        self.assertEqual((1, 1), (Llamada.objects.count(), GastoDeArchivo.objects.count()))

    def test_el_jsonl_deja_el_archivo_en_caracteres(self):
        self.mandar(envio(lectura("t-1")))
        lectura_jsonl = {"type": "tool_use", "id": "t-1", "name": "Read", "input": {"file_path": "C:/p/b.md"}}
        escribir_jsonl(self.jsonl, [llamada("m-5", contenido=[lectura_jsonl]),
                                    {"type": "user", "sessionId": SESION, "timestamp": "2026-10-05T10:00:01Z",
                                     "message": {"content": [{"type": "tool_result", "tool_use_id": "t-1",
                                                              "content": "x" * 70}]}}])
        self.leer_jsonl()
        self.assertEqual(70, GastoDeArchivo.objects.get().caracteres)
