# -*- coding: utf-8 -*-
"""Los seis casos del plan de pruebas de la fase A.

Buena parte comprueba **lo que NO debe pasar**: escribir fuera de la carpeta de
datos, o perder información al borrar el índice. Una comprobación que solo mira
el camino feliz aprueba cualquier cosa.
"""
import io
import os
import shutil
import tempfile

from django.test import TestCase, override_settings

from . import core
from .models import Anotado


class AlmacenTests(TestCase):
    """Guardar, leer, reconstruir, y no salirse de la carpeta."""

    def setUp(self):
        self.carpeta = tempfile.mkdtemp(prefix="prueba-plataforma-")
        self.contexto = override_settings(CARPETA_DATOS=self.carpeta)
        self.contexto.enable()

    def tearDown(self):
        self.contexto.disable()
        shutil.rmtree(self.carpeta, ignore_errors=True)

    # CP-002 · lo guardado sobrevive
    def test_lo_guardado_se_lee_despues(self):
        core.guardar("proyectos/uno.md", "# Uno\n")
        self.assertEqual(core.leer("proyectos/uno.md"), "# Uno\n")

    # CP-004 · la fuente es texto legible sin la plataforma
    def test_lo_guardado_queda_como_texto_en_disco(self):
        core.guardar("proyectos/dos.md", "# Dos\n")
        completa = os.path.join(self.carpeta, "proyectos", "dos.md")
        with io.open(completa, encoding="utf-8") as archivo:
            self.assertEqual(archivo.read(), "# Dos\n")

    def test_leer_algo_que_no_esta_no_inventa(self):
        self.assertIsNone(core.leer("no-existe.md"))

    # CP-003 · el índice se reconstruye
    def test_borrar_el_indice_no_pierde_informacion(self):
        core.guardar("uno.md", "# Uno\n")
        core.guardar("dos.md", "# Dos\n")
        Anotado.objects.all().delete()
        self.assertEqual(Anotado.objects.count(), 0)

        cuantos = core.reconstruir_indice()

        self.assertEqual(cuantos, 2)
        self.assertEqual(Anotado.objects.count(), 2)
        self.assertEqual(core.leer("uno.md"), "# Uno\n")

    def test_el_indice_guarda_la_huella_del_texto(self):
        core.guardar("tres.md", "# Tres\n")
        anotado = Anotado.objects.get(nombre="tres.md")
        self.assertEqual(anotado.huella, core.huella("# Tres\n"))

    def test_la_huella_cambia_cuando_el_texto_cambia(self):
        primera = core.guardar("cuatro.md", "# Cuatro\n")
        segunda = core.guardar("cuatro.md", "# Cuatro corregido\n")
        self.assertNotEqual(primera, segunda)

    # CP-006 · que NO pase: escribir fuera de la carpeta de datos
    def test_no_se_escribe_fuera_de_la_carpeta(self):
        with self.assertRaises(core.RutaFueraDeLaPlataforma):
            core.guardar("../afuera.md", "no debería quedar")
        self.assertFalse(
            os.path.exists(os.path.join(os.path.dirname(self.carpeta), "afuera.md")))

    def test_no_se_lee_fuera_de_la_carpeta(self):
        with self.assertRaises(core.RutaFueraDeLaPlataforma):
            core.leer("../../algo.md")


class EstaVivaTests(TestCase):
    """CP-001 · la plataforma responde, sin salir a la red."""

    def test_responde_que_esta_viva(self):
        respuesta = self.client.get("/")
        self.assertEqual(respuesta.status_code, 200)
        self.assertIn("está viva", respuesta.content.decode("utf-8"))


class SinRedTests(TestCase):
    """CP-001 · con la salida a la red tapada, la plataforma sigue sirviendo.

    Desconectar la máquina de verdad lo hace una persona. Lo que esta prueba
    deja automático es lo que esa desconexión buscaba encontrar: que nada de la
    plataforma dependa de una conexión que salga afuera.
    """

    def setUp(self):
        import socket
        self.conectar = socket.socket.connect
        adentro = ("127.0.0.1", "localhost", "::1")

        def sin_red(elmismo, direccion):
            if isinstance(direccion, tuple) and direccion[0] not in adentro:
                raise OSError("salió a la red: %s" % (direccion,))
            return self.conectar(elmismo, direccion)

        socket.socket.connect = sin_red

    def tearDown(self):
        import socket
        socket.socket.connect = self.conectar

    def test_responde_y_guarda_con_la_red_tapada(self):
        carpeta = tempfile.mkdtemp(prefix="prueba-sin-red-")
        try:
            self.assertEqual(self.client.get("/").status_code, 200)
            with override_settings(CARPETA_DATOS=carpeta):
                core.guardar("uno.md", "# Uno\n")
                self.assertEqual(core.leer("uno.md"), "# Uno\n")
        finally:
            shutil.rmtree(carpeta, ignore_errors=True)
