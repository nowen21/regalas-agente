"""`EP-025·HU-005 · CP-001`: el lector del freno trae de la base los niveles que
guarda la pantalla, por proyecto.

Va con `TransactionTestCase`: el lector abre su propia conexión con PyMySQL, y
desde ella no se ve lo que una prueba deja sin confirmar dentro de su
transacción.
"""
import tempfile

from django.db import connection
from django.test import TransactionTestCase

from core.enganches.niveles import NivelesDelProyecto
from core.niveles.models import NivelDeRegla
from core.proyectos.models import Proyecto


class ElFrenoLeeLosNivelesGuardados(TransactionTestCase):
    serialized_rollback = True

    def setUp(self):
        carpetas = [tempfile.TemporaryDirectory() for _ in range(3)]
        for carpeta in carpetas:
            self.addCleanup(carpeta.cleanup)
        self.uno = Proyecto.objects.create(nombre="uno", ruta=carpetas[0].name)
        self.otro = Proyecto.objects.create(nombre="otro", ruta=carpetas[1].name)
        self.quieto = Proyecto.objects.create(nombre="quieto", ruta=carpetas[2].name, activo=False)
        NivelDeRegla.objects.create(proyecto=self.uno, regla="02·F8", nivel="avisa")
        NivelDeRegla.objects.create(proyecto=self.quieto, regla="02·F8", nivel="apagada")

    def leer(self, ruta):
        d = connection.settings_dict
        ajustes = {"NAME": d["NAME"], "USER": d["USER"], "PASSWORD": d["PASSWORD"],
                   "HOST": d["HOST"], "PORT": d["PORT"]}
        return NivelesDelProyecto(ruta, ajustes=ajustes).todos()

    def test_trae_el_nivel_del_proyecto(self):
        self.assertEqual({"02·F8": "avisa"}, self.leer(self.uno.ruta))

    def test_la_ruta_se_compara_sin_mayusculas(self):
        self.assertEqual({"02·F8": "avisa"}, self.leer(self.uno.ruta.upper()))

    def test_otro_proyecto_no_tiene_ese_nivel(self):
        self.assertEqual({}, self.leer(self.otro.ruta))

    def test_un_proyecto_inactivo_no_tiene_niveles(self):
        self.assertEqual({}, self.leer(self.quieto.ruta))

    def test_un_proyecto_sin_registrar_no_tiene_niveles(self):
        with tempfile.TemporaryDirectory() as suelta:
            self.assertEqual({}, self.leer(suelta))
