"""`EP-005·HU-025` · Las reglas de cada tarea llegan antes de la acción, una sola vez.

Plan de pruebas: `PP-EP005-HU025-A`. Se leen las reglas del disco, con un
proyecto temporal donde queda lo entregado de cada sesión.
"""
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

from ..comun import Archivos, Proyecto
from .entrega_de_reglas import ESTADO, EntregaDeReglas
from .recuperar import TOPE, RecuperadorDeReglas

RAIZ = Proyecto.estandar()
ADAPTADORES = os.path.join(RAIZ, "adaptadores", "claude-code")
_PIEZA = re.compile(r"^<<< \d{2}·([A-Z]+\d+(?:\.\d+)?)", re.M)


def ids(texto):
    return _PIEZA.findall(texto or "")


class ConUnProyecto(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r = RecuperadorDeReglas(RAIZ, archivos=Archivos())
        cls.acciones = cls.r.mapa.acciones()
        cls.por_tarea = cls.r.mapa.reglas_por_tarea()

    def setUp(self):
        self.proyecto = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.proyecto, True)
        self.e = EntregaDeReglas(self.proyecto, recuperador=self.r)

    def de(self, tarea):
        idx = self.r.indice()
        return {r.id for r in self.por_tarea[tarea] if not idx[r.id].derogada}

    def nucleo(self):
        return {r.id for r in self.r.indice().values() if r.blindada and not r.derogada}

    def hasta_vaciar(self, pedir, veces=20):
        """Pide hasta que no llega nada; devuelve los textos de cada entrega."""
        textos = []
        for _ in range(veces):
            texto = pedir()
            if not texto:
                return textos
            textos.append(texto)
        self.fail("la entrega no se vació en %d pedidos" % veces)


class CP001LaTareaDeCadaAccion(ConUnProyecto):
    def tareas(self, herramienta, entrada):
        return self.e.tareas_de_la_accion(self.acciones, herramienta, entrada)

    def test_escribir_codigo(self):
        self.assertIn("cambiar-codigo", self.tareas("Write", {"file_path": os.path.join(self.proyecto, "x.py")}))

    def test_escribir_un_documento(self):
        tareas = self.tareas("Edit", {"file_path": "notas.md"})
        self.assertIn("escribir-documento", tareas)
        self.assertNotIn("cambiar-codigo", tareas)

    def test_escribir_en_el_estandar(self):
        self.assertIn("cambiar-estandar", self.tareas("Write", {"file_path": "base/01-conducta.md"}))

    def test_un_commit(self):
        tareas = self.tareas("Bash", {"command": "git commit -m 'x'"})
        self.assertIn("correr-comando", tareas)
        self.assertIn("tocar-git", tareas)

    def test_una_orden_que_no_es_git(self):
        self.assertNotIn("tocar-git", self.tareas("Bash", {"command": "python digit.py"}))

    def test_ir_afuera(self):
        self.assertIn("ir-afuera", self.tareas("WebFetch", {"url": "https://x"}))

    def test_leer_no_pide_nada(self):
        self.assertEqual([], self.tareas("Read", {"file_path": "x.py"}))


class CP002ElEngancheNoFrena(unittest.TestCase):
    def test_sale_con_cero_y_sin_decision(self):
        proyecto = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, proyecto, True)
        datos = {"hook_event_name": "PreToolUse", "session_id": "s-cp002", "tool_name": "Write",
                 "tool_input": {"file_path": os.path.join(proyecto, "x.py")}}
        proceso = subprocess.run([sys.executable, os.path.join(ADAPTADORES, "hook_reglas_accion.py"),
                                  "--raiz", proyecto], input=json.dumps(datos).encode("utf-8"),
                                 capture_output=True, timeout=120)
        self.assertEqual(0, proceso.returncode)
        if proceso.stdout.strip():
            salida = json.loads(proceso.stdout.decode("utf-8"))["hookSpecificOutput"]
            self.assertNotIn("permissionDecision", salida)
            self.assertIn("cambiar-codigo", salida["additionalContext"])


class CP003UnaSolaVez(ConUnProyecto):
    def pedir(self, agente=""):
        return self.e.para_la_accion("s-1", agente, "Write", {"file_path": "x.py"})

    def test_cada_regla_llega_una_vez(self):
        textos = self.hasta_vaciar(self.pedir)
        llegadas = [i for t in textos for i in ids(t)]
        self.assertEqual(len(llegadas), len(set(llegadas)), "una regla llegó dos veces")
        self.assertEqual(self.de("cambiar-codigo"), set(llegadas))

    def test_el_subagente_lleva_su_cuenta(self):
        self.hasta_vaciar(self.pedir)
        self.assertTrue(self.pedir("agente-1"))

    def test_otra_sesion_empieza_de_cero(self):
        self.hasta_vaciar(self.pedir)
        self.assertTrue(self.e.para_la_accion("s-2", "", "Write", {"file_path": "x.py"}))

    def test_queda_guardado_en_el_estado_de_la_sesion(self):
        self.pedir()
        self.assertTrue(os.path.isfile(os.path.join(self.proyecto, ESTADO, "s-1.json")))


class CP004PorPartesYSinLeerCuandoYaLlego(ConUnProyecto):
    def pedir(self):
        return self.e.para_la_accion("s-1", "", "Write", {"file_path": "x.py"})

    def test_lo_que_no_cabe_se_nombra_y_llega_despues(self):
        primero = self.pedir()
        self.assertIn("[NO CUPIERON", primero)
        faltan = re.search(r"\[NO CUPIERON[^\n]*\n  ([^\n]+)", primero).group(1)
        siguiente = self.pedir()
        primera_faltante = faltan.split(",")[0].strip().split("·")[1]
        self.assertIn(primera_faltante, ids(siguiente))

    def test_ninguna_entrega_pasa_del_tope(self):
        for texto in self.hasta_vaciar(self.pedir):
            if len(ids(texto)) > 1:
                self.assertLessEqual(len(texto.encode("utf-8")), TOPE)

    def test_si_ya_llego_todo_no_lee_el_estandar(self):
        self.hasta_vaciar(self.pedir)
        with mock.patch.object(self.r, "indice", side_effect=AssertionError("leyó el estándar")):
            self.assertEqual("", self.pedir())


class CP005ElMensajeTraeSoloLoQueFalta(ConUnProyecto):
    def mensaje(self, texto, sesion="s-1"):
        return self.e.para_el_mensaje(sesion, texto)

    def test_una_pregunta_trae_responder_y_no_recibir_pedido(self):
        llegadas = set()
        for texto in self.hasta_vaciar(lambda: self.mensaje("Pregunta qué es esto")):
            llegadas |= set(ids(texto))
        self.assertEqual(self.de("responder") | self.nucleo(), llegadas)

    def test_hagalo_trae_recibir_pedido(self):
        llegadas = set()
        for texto in self.hasta_vaciar(lambda: self.mensaje("Hágalo")):
            llegadas |= set(ids(texto))
        self.assertTrue(self.de("recibir-pedido") <= llegadas)

    def test_nada_se_repite(self):
        textos = self.hasta_vaciar(lambda: self.mensaje("Hágalo"))
        llegadas = [i for t in textos for i in ids(t)]
        self.assertEqual(len(llegadas), len(set(llegadas)))
        self.assertEqual("", self.mensaje("Hágalo otra vez"))

    def test_la_regla_citada_llega_siempre(self):
        self.hasta_vaciar(lambda: self.mensaje("Hágalo"))
        self.assertIn("F24", ids(self.mensaje("Pregunta qué dice 02·F24?")))

    def test_sin_palabra_llega_el_aviso(self):
        self.assertIn("[EL MENSAJE NO ABRE CON UNA PALABRA", self.mensaje("hola"))

    def test_las_de_lectura_no_autorizan_cambiar(self):
        self.assertFalse(self.e.autoriza_cambiar("Revise el archivo"))
        self.assertTrue(self.e.autoriza_cambiar("Corrija el archivo"))


class CP006SinElBloqueDeCadaTurno(unittest.TestCase):
    def test_el_enganche_del_mensaje_no_lo_trae(self):
        proyecto = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, proyecto, True)
        datos = {"hook_event_name": "UserPromptSubmit", "session_id": "s-cp006", "prompt": "Pregunta algo"}
        proceso = subprocess.run([sys.executable, os.path.join(ADAPTADORES, "hook_reglas.py"),
                                  "--raiz", proyecto], input=json.dumps(datos).encode("utf-8"),
                                 capture_output=True, timeout=120)
        self.assertEqual(0, proceso.returncode)
        self.assertNotIn("LAS REGLAS DE CADA TURNO", proceso.stdout.decode("utf-8", "replace"))


class CP007LasSenalesAlAbrir(unittest.TestCase):
    def test_van_al_abrir_y_no_con_el_mensaje(self):
        from ..comun.enganches import HOOKS_CLAUDE
        eventos = {evento for evento, _, guion, _, _ in HOOKS_CLAUDE if guion == "hook_senales.py"}
        self.assertEqual({"SessionStart"}, eventos)

    def test_avisa_una_vez_por_sesion_leida_de_la_entrada(self):
        sys.path.insert(0, ADAPTADORES)
        self.addCleanup(sys.path.remove, ADAPTADORES)
        import hook_senales
        proyecto = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, proyecto, True)
        os.makedirs(os.path.join(proyecto, "documentacion"))
        with io.open(os.path.join(proyecto, "documentacion", "senales.md"), "w", encoding="utf-8") as f:
            f.write("# Señales\n")
        sesion = hook_senales._sesion({"session_id": "s-cp007"})
        self.assertEqual("s-cp007", sesion)
        self.assertTrue(hook_senales.aviso(proyecto, sesion))
        self.assertEqual("", hook_senales.aviso(proyecto, sesion))


# ══ EP-005·HU-027 · el núcleo y lo que vuelve después de un resumen ════════════

class HU027CP001AlAbrirLlegaElNucleo(ConUnProyecto):
    def test_llega_el_nucleo_sin_pasar_del_tope(self):
        texto = self.e.al_abrir("s-1", "startup")
        self.assertTrue(set(ids(texto)) <= self.nucleo())
        self.assertTrue(ids(texto))
        if len(ids(texto)) > 1:
            self.assertLessEqual(len(texto.encode("utf-8")), TOPE)

    def test_lo_que_no_cupo_llega_con_los_mensajes(self):
        llegadas = ids(self.e.al_abrir("s-1", "startup"))
        for texto in self.hasta_vaciar(lambda: self.e.para_el_mensaje("s-1", "Pregunta algo")):
            llegadas += ids(texto)
        self.assertEqual(len(llegadas), len(set(llegadas)))
        self.assertTrue(self.nucleo() <= set(llegadas))


class HU027CP002ElEngancheNoFrena(unittest.TestCase):
    def test_sale_con_cero(self):
        proyecto = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, proyecto, True)
        datos = {"hook_event_name": "SessionStart", "session_id": "s-hu027", "source": "startup"}
        proceso = subprocess.run([sys.executable, os.path.join(ADAPTADORES, "hook_reglas_sesion.py"),
                                  "--raiz", proyecto], input=json.dumps(datos).encode("utf-8"),
                                 capture_output=True, timeout=120)
        self.assertEqual(0, proceso.returncode)
        if proceso.stdout.strip():
            salida = json.loads(proceso.stdout.decode("utf-8"))["hookSpecificOutput"]
            self.assertEqual("SessionStart", salida["hookEventName"])


class HU027CP003DespuesDeUnResumenVuelve(ConUnProyecto):
    def escribir(self, agente=""):
        return self.e.para_la_accion("s-1", agente, "Write", {"file_path": "x.py"})

    def vaciar_todo(self):
        self.hasta_vaciar(lambda: self.e.al_abrir("s-1", "startup"))
        self.hasta_vaciar(lambda: self.e.para_el_mensaje("s-1", "Pregunta algo"))
        self.hasta_vaciar(self.escribir)

    def test_compact_y_clear_vuelven_a_entregar(self):
        for origen in ("compact", "clear"):
            self.vaciar_todo()
            self.assertTrue(set(ids(self.e.al_abrir("s-1", origen))) & self.nucleo(), origen)
            self.assertTrue(self.escribir(), origen)


class HU027CP004RetomarNoVuelveACero(ConUnProyecto):
    def test_resume_no_entrega_de_nuevo(self):
        self.hasta_vaciar(lambda: self.e.al_abrir("s-1", "startup"))
        self.hasta_vaciar(lambda: self.e.para_el_mensaje("s-1", "Pregunta algo"))
        self.assertEqual("", self.e.al_abrir("s-1", "resume"))

    def test_el_subagente_conserva_su_cuenta(self):
        pedir = lambda: self.e.para_la_accion("s-1", "agente-1", "Write", {"file_path": "x.py"})
        self.hasta_vaciar(pedir)
        self.e.al_abrir("s-1", "compact")
        self.assertEqual("", pedir())


# ══ EP-005·HU-026 · las reglas de código por temas ═════════════════════════════

CON_TEMAS = os.path.join(RAIZ, "historico-chat", "scripts", "2026-10-09", "tareas-con-temas.txt")


class ConLaTablaDeTemas(ConUnProyecto):
    def setUp(self):
        super().setUp()
        with io.open(CON_TEMAS, encoding="utf-8") as f:
            self.temas = EntregaDeReglas.leer_temas(f.read())
        acciones = {t: [[c, v] for c, v in specs] for t, specs in self.acciones.items()}
        self.e.guardar("s-1", {"acciones": acciones, "temas": self.temas})

    def capitulos(self, texto):
        return {self.r.capitulo(self.r.indice()[i]) for i in ids(texto)}

    def escribir(self, ruta):
        return lambda: self.e.para_la_accion("s-1", "", "Write", {"file_path": ruta})


class HU026CP001UnaPruebaRecibeSusTemas(ConLaTablaDeTemas):
    def test_la_tabla_se_lee(self):
        self.assertIn("pruebas", [t[0] for t in self.temas])
        self.assertIn("todos", [t[0] for t in self.temas])

    def test_solo_pruebas_y_lo_de_todos(self):
        textos = self.hasta_vaciar(self.escribir("core/tests_x.py"))
        capitulos = set().union(*(self.capitulos(t) for t in textos))
        self.assertIn("08", capitulos)
        self.assertFalse(capitulos & {"17", "18", "03"})

    def test_no_pasa_de_25_kb(self):
        textos = self.hasta_vaciar(self.escribir("core/tests_x.py"))
        reglas = [self.r.indice()[i] for t in textos for i in ids(t)]
        de_codigo = sum(len(self.r.pieza(r, "t").encode("utf-8")) for r in reglas
                        if r.id in self.de("cambiar-codigo"))
        self.assertLessEqual(de_codigo, 25 * 1024)


class HU026CP002OtroArchivoRecibeLosSuyos(ConLaTablaDeTemas):
    def test_una_vista_despues_de_una_prueba(self):
        self.hasta_vaciar(self.escribir("core/tests_x.py"))
        capitulos = set().union(*(self.capitulos(t) for t in self.hasta_vaciar(self.escribir("core/views.py"))))
        self.assertTrue({"04", "05", "06"} <= capitulos)


class HU026CP003SinPatronOSinTablaLleganTodas(ConLaTablaDeTemas):
    def test_un_archivo_que_no_encaja(self):
        self.assertIsNone(EntregaDeReglas.capitulos_del_archivo(self.temas, "algo.xyz"))
        llegadas = {i for t in self.hasta_vaciar(self.escribir("algo.xyz")) for i in ids(t)}
        self.assertTrue(self.de("cambiar-codigo") <= llegadas)

    def test_sin_tabla(self):
        self.assertIsNone(EntregaDeReglas.capitulos_del_archivo([], "core/tests_x.py"))

    def test_la_carpeta_y_el_nombre(self):
        self.assertIn("08", EntregaDeReglas.capitulos_del_archivo(self.temas, "app/tests/algo.py"))
        self.assertIn("17", EntregaDeReglas.capitulos_del_archivo(self.temas, "web/Index.HTML"))


if __name__ == "__main__":
    unittest.main()
