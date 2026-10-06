# -*- coding: utf-8 -*-
"""`EP-005·HU-024`, fase A: el histórico firma los avisos internos como «Aviso del sistema»."""
import os
import shutil
import tempfile
import unittest

from core.enganches.historico import Historico, es_aviso_interno


def leer(ruta):
    with open(ruta, encoding="utf-8") as f:
        return f.read()


class ElHistoricoFirmaElAviso(unittest.TestCase):
    """CP-001 y CP-002."""

    def setUp(self):
        self.raiz = tempfile.mkdtemp(prefix="cimiento-avisos-")
        self.addCleanup(shutil.rmtree, self.raiz, True)
        os.makedirs(os.path.join(self.raiz, "historico-chat"))
        self.historico = Historico(self.raiz)

    def test_los_dos_avisos_quedan_como_aviso_del_sistema(self):
        self.historico.anotar_usuario("s1", "<task-notification>\n<task-id>x</task-id>\n</task-notification>")
        ruta = self.historico.anotar_usuario("s1", '<agent-message from="a1">\ninforme\n</agent-message>')
        texto = leer(ruta)
        self.assertIn("### 1 · Aviso del sistema — ", texto)
        self.assertIn("### 2 · Aviso del sistema — ", texto)
        self.assertIn("> informe", texto)
        self.assertNotIn("· Usuario —", texto)

    def test_el_mensaje_del_usuario_sigue_igual(self):
        self.historico.anotar_usuario("s1", "Hágalo")
        ruta = self.historico.anotar_usuario("s1", "pregunta: ¿qué hace <agent-message en el histórico?")
        texto = leer(ruta)
        self.assertIn("### 1 · Usuario — ", texto)
        self.assertIn("### 2 · Usuario — ", texto)
        self.assertNotIn("Aviso del sistema", texto)

    def test_reconoce_solo_lo_que_abre_con_la_marca(self):
        self.assertTrue(es_aviso_interno("  <task-notification>"))
        self.assertTrue(es_aviso_interno('<agent-message from="x">'))
        self.assertFalse(es_aviso_interno("hola <task-notification>"))
        self.assertFalse(es_aviso_interno(None))
