"""`EP-025·HU-032`, fase B · Los enganches leen lo suspendido: CP-003 y CP-004 del plan de pruebas.

Sin Django: corren con `python -m unittest core.enganches.tests_suspendidos` desde `proyectos/cimiento/`.
"""
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import unittest

from .suspendidos import Suspendidos, clave_del_mensaje, salir_si_esta_suspendido

CIMIENTO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ADAPTADORES = os.path.join(os.path.dirname(os.path.dirname(CIMIENTO)), "adaptadores", "claude-code")
MANANA = time.time() + 86400


class Contador:
    """Una consulta a la base de mentira, que cuenta cuántas veces se hizo y tarda un poco."""

    def __init__(self, lista):
        self.lista, self.veces, self._candado = lista, 0, threading.Lock()

    def __call__(self):
        with self._candado:
            self.veces += 1
        time.sleep(0.2)
        return self.lista


class ConUnProyecto(unittest.TestCase):
    def setUp(self):
        self.raiz = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.raiz, True)


class UnaSolaConsultaPorMensaje(ConUnProyecto):
    """CP-003."""

    def test_ocho_a_la_vez_consultan_una_vez_y_ven_lo_mismo(self):
        consulta = Contador([["senales", MANANA, "estorba"]])
        clave = clave_del_mensaje("UserPromptSubmit", {"prompt": "hola"})
        vistas = []

        def enganche():
            vistas.append(Suspendidos(self.raiz, "s-1", consultar=consulta).esta("senales", clave))

        hilos = [threading.Thread(target=enganche) for _ in range(8)]
        for hilo in hilos:
            hilo.start()
        for hilo in hilos:
            hilo.join(5)
        self.assertEqual(1, consulta.veces)
        self.assertEqual([True] * 8, vistas)

    def test_sin_mensaje_propio_usa_la_lista_del_mensaje_y_otro_mensaje_consulta_otra_vez(self):
        consulta = Contador([])
        Suspendidos(self.raiz, "s-1", consultar=consulta).lista(clave_del_mensaje("UserPromptSubmit", {"prompt": "uno"}))
        Suspendidos(self.raiz, "s-1", consultar=consulta).lista(clave_del_mensaje("PreToolUse", {}))
        self.assertEqual(1, consulta.veces)
        Suspendidos(self.raiz, "s-1", consultar=consulta).lista(clave_del_mensaje("UserPromptSubmit", {"prompt": "dos"}))
        self.assertEqual(2, consulta.veces)

    def test_un_turno_caido_no_deja_esperando_para_siempre(self):
        os.makedirs(os.path.join(self.raiz, ".agente"))
        suspendidos = Suspendidos(self.raiz, "s-1", consultar=Contador([]), ahora=lambda: time.time() + 60)
        turno = suspendidos._ganar_el_turno("x")
        self.assertTrue(turno)
        # Pasado el tiempo de un turno viejo, el siguiente lo toma y consulta.
        self.assertEqual([], suspendidos.lista("x"))


class ElSuspendidoSale(ConUnProyecto):
    """CP-004."""

    def correr(self, datos, lista=None, falla=False):
        """`(salió, lo que quedó en la entrada)` de `salir_si_esta_suspendido` con `datos` por la entrada."""
        def consultar():
            if falla:
                raise RuntimeError("sin base")
            return lista or []
        viejo = sys.stdin
        sys.stdin = io.TextIOWrapper(io.BytesIO(json.dumps(datos).encode("utf-8")), encoding="utf-8")
        try:
            try:
                salir_si_esta_suspendido("hook_senales.py", ["--raiz", self.raiz], consultar=consultar)
                salio = False
            except SystemExit as fin:
                self.assertEqual(0, fin.code)
                salio = True
            return salio, sys.stdin.buffer.read()
        finally:
            sys.stdin = viejo

    def datos(self, prompt="hola"):
        return {"hook_event_name": "UserPromptSubmit", "session_id": "s-1", "prompt": prompt}

    def test_suspendido_sale_con_cero(self):
        self.assertTrue(self.correr(self.datos(), [["senales", MANANA, "estorba"]])[0])

    def test_vencido_o_sin_base_corre(self):
        self.assertFalse(self.correr(self.datos("a"), [["senales", time.time() - 10, "ya venció"]])[0])
        self.assertFalse(self.correr(self.datos("b"), falla=True)[0])

    def test_sin_suspension_el_programa_lee_la_misma_entrada(self):
        salio, entrada = self.correr(self.datos(), [["otro", MANANA, "x"]])
        self.assertFalse(salio)
        self.assertEqual(self.datos(), json.loads(entrada.decode("utf-8")))

    def test_el_adaptador_suspendido_no_escribe_nada(self):
        os.makedirs(os.path.join(self.raiz, ".agente"))
        with io.open(os.path.join(self.raiz, ".agente", "suspendidos.%s.json" % __import__("hashlib").sha1(
                b"s-1").hexdigest()[:16]), "w", encoding="utf-8") as f:
            json.dump({"clave": None, "lista": [["reglas-relacionadas", MANANA, "estorba"]]}, f)
        # Un evento sin mensaje propio usa la lista guardada: no hace falta base.
        datos = {"hook_event_name": "PostToolUse", "session_id": "s-1"}
        proceso = subprocess.run([sys.executable, os.path.join(ADAPTADORES, "hook_relacionadas.py"), "--raiz", self.raiz],
                                 input=json.dumps(datos).encode("utf-8"), capture_output=True, timeout=60)
        self.assertEqual(0, proceso.returncode)
        self.assertEqual(b"", proceso.stdout)


class SoloFrenoApagaElFreno(unittest.TestCase):
    """CP-005."""

    def niveles(self, suspendidas):
        from unittest import mock
        from .niveles import TODAS, NivelesDelProyecto
        with mock.patch.object(NivelesDelProyecto, "consultar_juntas", return_value=([], suspendidas)):
            return TODAS, NivelesDelProyecto(tempfile.gettempdir()).todos()

    def test_suspender_el_historico_no_apaga_el_freno(self):
        todas, niveles = self.niveles([("enganche", "historico-del-usuario")])
        self.assertNotIn(todas, niveles)

    def test_suspender_freno_lo_apaga_como_antes(self):
        todas, niveles = self.niveles([("enganche", "freno"), ("regla", "02·F8")])
        self.assertEqual("apagada", niveles[todas])
        self.assertEqual("apagada", niveles["02·F8"])


if __name__ == "__main__":
    unittest.main()
