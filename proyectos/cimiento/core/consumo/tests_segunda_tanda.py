"""`EP-025·HU-010`: el gasto por mensaje, palabra clave, trabajo, herramienta,
agente auxiliar, modelo, tipo de token y lo que llena el contexto.

Los `.jsonl` son muestras armadas acá, con la forma verificada el 2026-10-05:
las líneas del usuario traen `promptId` y las del agente no.
"""
import json
import os
import shutil
import tempfile
from unittest import mock

from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.utils import timezone

from core.consumo.guardar import GuardadoDeConsumo
from core.consumo.lector import LectorDeClaudeCode
from core.consumo.models import GastoDeHerramienta, Llamada, Pedido
from core.consumo.tablero import GastoDelPeriodo
from core.consumo.tests import escribir_jsonl
from core.consumo.trabajo import trabajo_de, trabajo_de_la_ruta
from core.herramientas.recuperar import RecuperadorDeReglas
from core.proyectos.models import Proyecto

SESION = "s-2"
FASE = "C:/p/documentacion/epicas/EP-025-x/HU-010-y/A-EP-025-HU-010-segunda-tanda/plan_trabajo.md"
ANALISIS = "C:/p/historico-chat/resumenes/2026-10-04/pendientes/119-se-puede/analisis-2.md"


def pedido(identificador, texto):
    return {"type": "user", "sessionId": SESION, "promptId": identificador, "timestamp": "2026-10-05T10:00:00Z",
            "message": {"content": [{"type": "text", "text": texto}]}}


def respuesta(mensaje, usos=(), modelo="claude-opus-5-5", entrada=10):
    contenido = [{"type": "tool_use", "id": i, "name": n, "input": e} for i, n, e in usos]
    return {"type": "assistant", "sessionId": SESION, "requestId": "r-" + mensaje, "timestamp": "2026-10-05T10:00:01Z",
            "message": {"id": mensaje, "model": modelo, "content": contenido,
                        "usage": {"input_tokens": entrada, "output_tokens": 5, "cache_read_input_tokens": 100,
                                  "cache_creation_input_tokens": 2}}}


def resultado(identificador, caracteres, prompt):
    return {"type": "user", "sessionId": SESION, "promptId": prompt, "timestamp": "2026-10-05T10:00:02Z",
            "message": {"content": [{"type": "tool_result", "tool_use_id": identificador, "content": "x" * caracteres}]}}


def primera_parte():
    return [
        pedido("p-1", "<ide_opened_file>algo</ide_opened_file>Hágalo con lo de la fase"),
        respuesta("m-1", [("u-1", "Edit", {"file_path": FASE})]), resultado("u-1", 2, "p-1"),
        respuesta("m-2", [("u-2", "Bash", {"command": "ls"})]), resultado("u-2", 35, "p-1"),
        pedido("p-2", "analicemos: esto"),
        respuesta("m-3", [("u-3", "Read", {"file_path": ANALISIS})]), resultado("u-3", 70, "p-2"),
    ]


def segunda_parte():
    return [respuesta("m-4", modelo="claude-haiku-4-5"), pedido("p-3", "hola"), respuesta("m-5")]


class ElTrabajoSaleDeLasRutas(SimpleTestCase):

    def test_fase_analisis_y_nada(self):
        self.assertEqual("A-EP-025-HU-010-segunda-tanda", trabajo_de_la_ruta(FASE))
        self.assertEqual("análisis 2 del pendiente 119", trabajo_de_la_ruta(ANALISIS.replace("/", "\\")))
        self.assertEqual("", trabajo_de_la_ruta("C:/p/README.md"))

    def test_gana_la_que_mas_aparece(self):
        self.assertEqual("análisis 2 del pendiente 119", trabajo_de([FASE, ANALISIS, ANALISIS, "C:/p/x.md"]))
        self.assertEqual("", trabajo_de([]))


class LaPalabraClaveEsLaDeLaLista(SimpleTestCase):

    def test_la_primera_columna_y_sin_el_editor(self):
        recuperador = RecuperadorDeReglas()
        self.assertEqual("Hágalo", recuperador.palabra_clave("<ide_opened_file>x</ide_opened_file>hagalo ya"))
        self.assertEqual("Hágalo", recuperador.palabra_clave("Aplique el cambio"))
        self.assertEqual("Analicemos", recuperador.palabra_clave("analicemos: esto"))
        self.assertEqual("", recuperador.palabra_clave("hola"))


class ConProyecto(TestCase):

    def setUp(self):
        self.base = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.base, True)
        ruta = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, ruta, True)
        self.proyecto = Proyecto.objects.create(nombre="uno", ruta=ruta)
        self.carpeta = os.path.join(self.base, self.proyecto.carpeta_claude)
        os.makedirs(self.carpeta)
        self.jsonl = os.path.join(self.carpeta, SESION + ".jsonl")
        parche = mock.patch("core.consumo.guardar.proyectos_de_claude", return_value=self.base)
        parche.start()
        self.addCleanup(parche.stop)

    def leer(self):
        return GuardadoDeConsumo(self.proyecto, self.base).leer_todo()


class ElGastoQuedaPorMensajePalabraYTrabajo(ConProyecto):
    """CP-001."""

    def test_cada_llamada_con_su_mensaje_palabra_y_trabajo(self):
        escribir_jsonl(self.jsonl, primera_parte() + segunda_parte())
        self.leer()
        pedidos = {p.identificador: (p.palabra, p.trabajo) for p in Pedido.objects.all()}
        self.assertEqual({"p-1": ("Hágalo", "A-EP-025-HU-010-segunda-tanda"),
                          "p-2": ("Analicemos", "análisis 2 del pendiente 119"), "p-3": ("", "")}, pedidos)
        self.assertEqual({"m-1": "p-1", "m-2": "p-1", "m-3": "p-2", "m-4": "p-2", "m-5": "p-3"},
                         dict(Llamada.objects.values_list("mensaje", "pedido__identificador")))

    def test_no_guarda_el_texto(self):
        escribir_jsonl(self.jsonl, primera_parte())
        self.leer()
        guardado = json.dumps(list(Pedido.objects.values()), default=str)
        self.assertNotIn("con lo de la fase", guardado)
        self.assertNotIn("esto", guardado)

    def test_un_turno_leido_en_dos_veces_sigue_con_su_mensaje(self):
        escribir_jsonl(self.jsonl, primera_parte())
        self.leer()
        escribir_jsonl(self.jsonl, segunda_parte())
        self.leer()
        self.assertEqual("p-2", Llamada.objects.get(mensaje="m-4").pedido.identificador)

    def test_leer_otra_vez_no_duplica(self):
        escribir_jsonl(self.jsonl, primera_parte() + segunda_parte())
        self.leer()
        GuardadoDeConsumo(self.proyecto, self.base).guardar(LectorDeClaudeCode(self.jsonl).leer())
        self.assertEqual((3, 5, 3), (Pedido.objects.count(), Llamada.objects.count(),
                                     GastoDeHerramienta.objects.count()))


class ElGastoQuedaPorHerramientaYAgente(ConProyecto):
    """CP-002."""

    def test_herramientas_con_su_resultado(self):
        escribir_jsonl(self.jsonl, primera_parte())
        self.leer()
        self.assertEqual({"u-1": ("Edit", 2), "u-2": ("Bash", 35), "u-3": ("Read", 70)},
                         {h.identificador: (h.nombre, h.caracteres) for h in GastoDeHerramienta.objects.all()})

    def test_el_auxiliar_con_su_tipo_y_sin_mensaje(self):
        escribir_jsonl(self.jsonl, primera_parte())
        auxiliar = os.path.join(self.carpeta, SESION, "subagents")
        os.makedirs(auxiliar)
        tarea = dict(pedido("p-x", "Busque esto"), isSidechain=True)
        escribir_jsonl(os.path.join(auxiliar, "agent-a1.jsonl"), [tarea, dict(respuesta("m-aux"), isSidechain=True)])
        with open(os.path.join(auxiliar, "agent-a1.meta.json"), "w", encoding="utf-8") as meta:
            json.dump({"agentType": "Explore", "description": "Buscar"}, meta)
        self.leer()
        auxiliar_guardado = Llamada.objects.get(mensaje="m-aux")
        self.assertEqual((True, "Explore", None), (auxiliar_guardado.auxiliar, auxiliar_guardado.agente,
                                                   auxiliar_guardado.pedido))
        self.assertFalse(Pedido.objects.filter(identificador="p-x").exists())


class ElTableroMuestraLosSieteNiveles(ConProyecto):
    """CP-003."""

    def setUp(self):
        super().setUp()
        escribir_jsonl(self.jsonl, primera_parte() + segunda_parte())
        self.leer()
        hoy = timezone.now()
        Llamada.objects.update(fecha=hoy)
        Pedido.objects.update(fecha=hoy)
        GastoDeHerramienta.objects.update(fecha=hoy)

    def test_las_sumas(self):
        todo = GastoDelPeriodo().todo()
        niveles = {titulo: {f["nombre"]: f["llamadas"] for f in filas} for titulo, filas in todo["niveles"]}
        self.assertEqual({"Hágalo": 2, "Analicemos": 2, "(sin palabra clave)": 1}, niveles["Por palabra clave"])
        self.assertEqual({"A-EP-025-HU-010-segunda-tanda": 2, "análisis 2 del pendiente 119": 2,
                          "(sin trabajo)": 1}, niveles["Por trabajo"])
        self.assertEqual({"claude-opus-5-5": 4, "claude-haiku-4-5": 1}, niveles["Por modelo"])
        self.assertEqual({"Entrada nueva": 50, "Escrita en caché": 10, "Releída de caché": 500, "Salida": 25},
                         {t["nombre"]: t["total"] for t in todo["tipos"]})
        self.assertEqual({"Read", "Bash", "Edit"}, {h["nombre"] for h in todo["herramientas"]})
        self.assertEqual(112, todo["contexto"]["maximo"])
        self.assertEqual(20, todo["contexto"]["archivos"])
        self.assertEqual({"Hágalo", "Analicemos", ""}, {m["palabra"] for m in todo["mensajes"]})

    def test_la_pagina_las_muestra(self):
        cuenta = get_user_model().objects.create_user("c")
        self.client.force_login(cuenta)
        respuesta_pagina = self.client.get("/gasto/datos/")
        for texto in ("Por palabra clave", "Por trabajo", "Por modelo", "Por agente auxiliar", "Por tipo de token",
                      "Por herramienta", "Lo que llena el contexto", "Últimos mensajes", "Analicemos"):
            self.assertContains(respuesta_pagina, texto)
