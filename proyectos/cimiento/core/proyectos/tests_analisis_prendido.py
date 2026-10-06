# -*- coding: utf-8 -*-
"""`EP-025·HU-023 · CP-002`: el estado del análisis prendido vive en la base.

Va con `TransactionTestCase`: el estado se escribe con PyMySQL, en otra
conexión, y desde ella no se ve lo que una prueba deja sin confirmar.
"""
import os
import shutil
import tempfile

from django.db import connection
from django.test import TransactionTestCase

from core.enganches.analisis_en_curso import ESTADO, ESTADOS, AnalisisEnCurso
from core.enganches.estado_en_base import EstadoEnBase
from core.proyectos.models import AnalisisPrendido, Proyecto


def _ajustes():
    d = connection.settings_dict
    return {"NAME": d["NAME"], "USER": d["USER"], "PASSWORD": d["PASSWORD"], "HOST": d["HOST"], "PORT": d["PORT"]}


class ElEstadoViveEnLaBase(TransactionTestCase):
    # Sin esto, al vaciar la base se recrean los tipos de contenido y la prueba
    # siguiente que restaura la base los encuentra repetidos.
    serialized_rollback = True

    def setUp(self):
        self.raiz = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.raiz, True)
        carpeta = os.path.join(self.raiz, "pendientes", "7-algo")
        os.makedirs(carpeta)
        with open(os.path.join(carpeta, "pendiente.md"), "w", encoding="utf-8") as f:
            f.write("# Pendiente 7\n")
        os.makedirs(os.path.join(self.raiz, "historico-chat"))
        self.t = os.path.join(self.raiz, "historico-chat", "2026-10-05-sesion.md")
        with open(self.t, "w", encoding="utf-8") as f:
            f.write("### 1 · Usuario, 10:00\n\nhola\n")
        self.proyecto = Proyecto.objects.create(nombre="uno", ruta=self.raiz)

    def curso(self, ajustes=None, transcripcion=None):
        base = EstadoEnBase(self.raiz, ajustes=ajustes or _ajustes())
        return AnalisisEnCurso(self.raiz, self.t if transcripcion is None else transcripcion, base=base)

    def sin_archivos(self):
        carpeta = os.path.join(self.raiz, ESTADOS)
        return not os.path.isfile(os.path.join(self.raiz, ESTADO)) and not (
            os.path.isdir(carpeta) and os.listdir(carpeta))

    def test_prender_escribe_la_fila_y_ningun_archivo(self):
        self.assertTrue(self.curso().prender(7, self.t, 1)[0])
        fila = AnalisisPrendido.objects.get(proyecto=self.proyecto)
        self.assertEqual("historico-chat/2026-10-05-sesion.md", fila.sesion)
        self.assertTrue(fila.analisis.endswith("7-algo/analisis-1.md"))
        self.assertTrue(self.sin_archivos())
        self.assertEqual(1, self.curso().leer_estado()["desde"])

    def test_pausar_y_borrar_cambian_la_fila(self):
        curso = self.curso()
        curso.prender(7, self.t, 1)
        curso.pausar(3)
        self.assertEqual(3, AnalisisPrendido.objects.get(proyecto=self.proyecto).pausa)
        curso.borrar_estado()
        self.assertFalse(AnalisisPrendido.objects.exists())

    def test_sin_sesion_se_lee_la_mas_reciente(self):
        self.curso().prender(7, self.t, 1)
        self.assertIn("7-algo", self.curso(transcripcion="").leer_estado()["analisis"])

    def test_lo_que_estaba_en_archivo_pasa_a_la_base(self):
        AnalisisEnCurso(self.raiz, self.t, base=False).prender(7, self.t, 1)
        self.assertFalse(self.sin_archivos())
        estado = self.curso().leer_estado()
        self.assertIn("7-algo", estado["analisis"])
        self.assertTrue(self.sin_archivos())
        self.assertEqual(1, AnalisisPrendido.objects.count())

    def test_un_proyecto_sin_registro_no_tiene_fila(self):
        with tempfile.TemporaryDirectory() as suelta:
            self.assertIsNone(EstadoEnBase(suelta, ajustes=_ajustes()).proyecto_id())

    def test_sin_base_sigue_en_archivo(self):
        malos = dict(_ajustes(), PORT="1")
        self.assertTrue(self.curso(ajustes=malos).prender(7, self.t, 1)[0])
        self.assertFalse(self.sin_archivos())
        self.assertFalse(AnalisisPrendido.objects.exists())
