"""`EP-025·HU-028`: el trabajo de cada mensaje sale del análisis prendido, de lo que
tocó su turno (también las órdenes de consola y las fases de cualquier letra) o
de su conversación."""
import io

from django.core.management import call_command
from django.test import SimpleTestCase

from core.consumo.models import LineaDeSesion, Pedido
from core.consumo.tests import escribir_jsonl
from core.consumo.tests_segunda_tanda import SESION, ConProyecto
from core.consumo.trabajo import trabajo_de_la_ruta, trabajo_del_aviso

FASE_B = "C:/p/documentacion/epicas/EP-028-x/HU-007-y/B-EP-028-HU-007-pestanas/plan_trabajo.md"
PRENDIDO = ("[ANÁLISIS EN CURSO] La conversación entra al análisis "
            "historico-chat/resumenes/2026-10-04/pendientes/119-se-puede/analisis-2.md.")
APAGADO = "[ANÁLISIS EN CURSO] Ningún análisis está prendido: la conversación no entra a ninguno."


def mensaje(identificador, minuto, texto="pregunta: algo", sesion=SESION):
    return {"type": "user", "sessionId": sesion, "promptId": identificador,
            "timestamp": "2026-10-08T10:%02d:00Z" % minuto, "message": {"content": [{"type": "text", "text": texto}]}}


def aviso(texto, minuto, sesion=SESION):
    return {"type": "attachment", "sessionId": sesion, "uuid": "a-%d" % minuto,
            "timestamp": "2026-10-08T10:%02d:01Z" % minuto,
            "attachment": {"type": "hook_additional_context", "hookName": "UserPromptSubmit",
                           "hookEvent": "UserPromptSubmit", "toolUseID": "x", "content": [texto]}}


def respuesta(identificador, minuto, herramienta=None, entrada=None, sesion=SESION):
    contenido = [{"type": "tool_use", "id": "t-" + identificador, "name": herramienta, "input": entrada}] \
        if herramienta else []
    return {"type": "assistant", "sessionId": sesion, "timestamp": "2026-10-08T10:%02d:30Z" % minuto,
            "message": {"id": "m-" + identificador, "model": "m", "content": contenido,
                        "usage": {"input_tokens": 1, "output_tokens": 1}}}


def trabajos():
    return {p.identificador: (p.trabajo, p.origen) for p in Pedido.objects.all()}


class LaDeduccion(SimpleTestCase):
    """CP-001 y CP-002, sin base."""

    def test_reconoce_las_fases_de_cualquier_letra(self):
        self.assertEqual("B-EP-028-HU-007-pestanas", trabajo_de_la_ruta(FASE_B))
        self.assertEqual("C-EP-001-HU-002", trabajo_de_la_ruta('cerrar_fase "x/C-EP-001-HU-002/"'))
        self.assertEqual("", trabajo_de_la_ruta("PP-EP028-HU007-B"))

    def test_el_aviso_dice_el_analisis_prendido(self):
        self.assertEqual("análisis 2 del pendiente 119", trabajo_del_aviso(PRENDIDO))
        self.assertEqual("", trabajo_del_aviso(APAGADO))
        self.assertEqual("", trabajo_del_aviso("[ANÁLISIS EN CURSO] El análisis x/analisis-2.md está en pausa desde el turno 3."))


class ElTrabajoDeCadaMensaje(ConProyecto):

    def test_el_analisis_prendido_manda(self):
        """CP-001."""
        escribir_jsonl(self.jsonl, [mensaje("p-1", 1), aviso(PRENDIDO, 1),
                                    respuesta("1", 1, "Edit", {"file_path": FASE_B})])
        self.leer()
        self.assertEqual({"p-1": ("análisis 2 del pendiente 119", "analisis")}, trabajos())

    def test_el_aviso_apagado_no_da_trabajo(self):
        """CP-001."""
        escribir_jsonl(self.jsonl, [mensaje("p-1", 1), aviso(APAGADO, 1), respuesta("1", 1)])
        self.leer()
        self.assertEqual({"p-1": ("Conversación s-2", "titulo")}, trabajos())

    def test_la_orden_de_consola_dice_la_fase(self):
        """CP-002."""
        orden = {"command": 'python manage.py cerrar_fase "documentacion/x/B-EP-028-HU-007-pestanas" --aplicar'}
        escribir_jsonl(self.jsonl, [mensaje("p-1", 1), respuesta("1", 1, "Bash", orden)])
        self.leer()
        self.assertEqual({"p-1": ("B-EP-028-HU-007-pestanas", "archivos")}, trabajos())

    def test_el_mensaje_sin_rastro_sigue_la_conversacion(self):
        """CP-003, pasos 1 y 2."""
        escribir_jsonl(self.jsonl, [mensaje("p-1", 1, "hágalo"), respuesta("1", 1, "Edit", {"file_path": FASE_B}),
                                    mensaje("p-2", 2, "apruebo")])
        self.leer()
        self.assertEqual(("B-EP-028-HU-007-pestanas", "sesion"), trabajos()["p-2"])
        otra = "C:/p/documentacion/epicas/EP-025-x/HU-028-y/A-EP-025-HU-028-el-trabajo-abierto/plan_trabajo.md"
        escribir_jsonl(self.jsonl, [respuesta("2", 2, "Edit", {"file_path": otra})])
        self.leer()
        self.assertEqual(("A-EP-025-HU-028-el-trabajo-abierto", "archivos"), trabajos()["p-2"])

    def test_otra_conversacion_no_hereda(self):
        """CP-003, paso 3: queda en su propia conversación (fase B)."""
        escribir_jsonl(self.jsonl, [mensaje("p-1", 1), respuesta("1", 1, "Edit", {"file_path": FASE_B}),
                                    mensaje("p-9", 2, sesion="otra")])
        self.leer()
        self.assertEqual(("Conversación otra", "titulo"), trabajos()["p-9"])


class LoGuardadoSeRecalcula(ConProyecto):
    """CP-004."""

    def test_recalcula_desde_las_lineas_y_da_lo_mismo_la_segunda_vez(self):
        escribir_jsonl(self.jsonl, [mensaje("p-1", 1), aviso(PRENDIDO, 1), respuesta("1", 1),
                                    mensaje("p-2", 2), respuesta("2", 2, "Edit", {"file_path": FASE_B}),
                                    mensaje("p-3", 3, "apruebo")])
        self.leer()
        self.assertTrue(LineaDeSesion.objects.exists())
        Pedido.objects.update(trabajo="", origen="")          # como quedaron antes de la HU-028
        esperado = {"p-1": ("análisis 2 del pendiente 119", "analisis"),
                    "p-2": ("B-EP-028-HU-007-pestanas", "archivos"),
                    "p-3": ("B-EP-028-HU-007-pestanas", "sesion")}
        salida = io.StringIO()
        call_command("recalcular_trabajo", stdout=salida)
        self.assertEqual(esperado, trabajos())
        self.assertIn("Sin trabajo: 3 antes, 0 ahora", salida.getvalue())
        call_command("recalcular_trabajo", stdout=io.StringIO())
        self.assertEqual(esperado, trabajos())


def titulo(texto, sesion=SESION):
    return {"type": "ai-title", "aiTitle": texto, "sessionId": sesion}


class NingunMensajeSinTrabajo(ConProyecto):
    """`EP-025·HU-028`, fase B · CP-005."""

    def test_sin_fase_ni_analisis_queda_en_su_conversacion_por_el_titulo(self):
        escribir_jsonl(self.jsonl, [mensaje("p-1", 1, "buenos días"), respuesta("1", 1), titulo("Buenos días"),
                                    mensaje("p-2", 2, "levante el servidor"), respuesta("2", 2, "Bash", {"command": "ls"})])
        self.leer()
        self.assertEqual({"p-1": ("Conversación «Buenos días»", "titulo"),
                          "p-2": ("Conversación «Buenos días»", "titulo")}, trabajos())

    def test_el_titulo_que_llega_despues_reemplaza_el_codigo(self):
        escribir_jsonl(self.jsonl, [mensaje("p-1", 1, "hola"), respuesta("1", 1)])
        self.leer()
        self.assertEqual(("Conversación s-2", "titulo"), trabajos()["p-1"])
        escribir_jsonl(self.jsonl, [titulo("Levante localhub")])
        self.leer()
        self.assertEqual(("Conversación «Levante localhub»", "titulo"), trabajos()["p-1"])

    def test_la_fase_que_aparece_despues_manda_desde_ahi(self):
        escribir_jsonl(self.jsonl, [mensaje("p-1", 1, "hola"), respuesta("1", 1), titulo("Arreglo"),
                                    mensaje("p-2", 2, "hágalo"), respuesta("2", 2, "Edit", {"file_path": FASE_B}),
                                    mensaje("p-3", 3, "apruebo")])
        self.leer()
        self.assertEqual({"p-1": ("Conversación «Arreglo»", "titulo"),
                          "p-2": ("B-EP-028-HU-007-pestanas", "archivos"),
                          "p-3": ("B-EP-028-HU-007-pestanas", "sesion")}, trabajos())

    def test_recalcular_no_deja_ninguno_sin_trabajo(self):
        escribir_jsonl(self.jsonl, [mensaje("p-1", 1), respuesta("1", 1), titulo("Gatos")])
        self.leer()
        huerfano = Pedido.objects.create(proyecto=self.proyecto, sesion="borrada-123", identificador="x",
                                         fecha=None)
        Pedido.objects.update(trabajo="", origen="")
        call_command("recalcular_trabajo", stdout=io.StringIO())
        self.assertFalse(Pedido.objects.filter(trabajo="").exists())
        self.assertEqual("Conversación «Gatos»", Pedido.objects.get(identificador="p-1").trabajo)
        self.assertEqual("Conversación borrada-", Pedido.objects.get(pk=huerfano.pk).trabajo)
