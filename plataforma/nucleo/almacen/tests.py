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

from nucleo.constancia import Constancia, SinConstancia
from nucleo.acceso import para_probar
from . import core
from .models import Anotado


def constancia(nombre):
    """El comprobante que el almacén exige, para las pruebas del almacén.

    Acá se construye a mano a propósito: estas pruebas son del almacén, no de
    la auditoría, y hacerlas pasar por ella las volvería pruebas de las dos
    cosas a la vez. Que la auditoría emita el comprobante de verdad se prueba
    en `nucleo/auditoria/tests.py`.
    """
    return Constancia(nombre, {})


class AlmacenTests(TestCase):
    """Guardar, leer, reconstruir, y no salirse de la carpeta."""

    def setUp(self):
        # Todas las pantallas exigen haber entrado desde `EP-022`.
        para_probar.como_usuario(self.client)
        self.carpeta = tempfile.mkdtemp(prefix="prueba-plataforma-")
        self.contexto = override_settings(CARPETA_DATOS=self.carpeta)
        self.contexto.enable()

    def tearDown(self):
        self.contexto.disable()
        shutil.rmtree(self.carpeta, ignore_errors=True)

    # CP-002 · lo guardado sobrevive
    def test_lo_guardado_se_lee_despues(self):
        core.guardar("proyectos/uno.md", "# Uno\n", constancia("proyectos/uno.md"))
        self.assertEqual(core.leer("proyectos/uno.md"), "# Uno\n")

    # CP-004 · la fuente es texto legible sin la plataforma
    def test_lo_guardado_queda_como_texto_en_disco(self):
        core.guardar("proyectos/dos.md", "# Dos\n", constancia("proyectos/dos.md"))
        completa = os.path.join(self.carpeta, "proyectos", "dos.md")
        with io.open(completa, encoding="utf-8") as archivo:
            self.assertEqual(archivo.read(), "# Dos\n")

    def test_leer_algo_que_no_esta_no_inventa(self):
        self.assertIsNone(core.leer("no-existe.md"))

    # CP-003 · el índice se reconstruye
    def test_borrar_el_indice_no_pierde_informacion(self):
        core.guardar("uno.md", "# Uno\n", constancia("uno.md"))
        core.guardar("dos.md", "# Dos\n", constancia("dos.md"))
        Anotado.objects.all().delete()
        self.assertEqual(Anotado.objects.count(), 0)

        cuantos = core.reconstruir_indice()

        self.assertEqual(cuantos, 2)
        self.assertEqual(Anotado.objects.count(), 2)
        self.assertEqual(core.leer("uno.md"), "# Uno\n")

    def test_el_indice_guarda_la_huella_del_texto(self):
        core.guardar("tres.md", "# Tres\n", constancia("tres.md"))
        anotado = Anotado.objects.get(nombre="tres.md")
        self.assertEqual(anotado.huella, core.huella("# Tres\n"))

    def test_la_huella_cambia_cuando_el_texto_cambia(self):
        primera = core.guardar("cuatro.md", "# Cuatro\n", constancia("cuatro.md"))
        segunda = core.guardar("cuatro.md", "# Cuatro corregido\n", constancia("cuatro.md"))
        self.assertNotEqual(primera, segunda)

    # Fase D · que NO pase: escribir sin haber registrado la acción
    def test_no_se_escribe_sin_constancia(self):
        with self.assertRaises(SinConstancia):
            core.guardar("cinco.md", "# Cinco" + chr(10), None)
        self.assertIsNone(core.leer("cinco.md"))

    def test_una_constancia_de_otra_cosa_no_sirve(self):
        with self.assertRaises(SinConstancia):
            core.guardar("seis.md", "# Seis" + chr(10), constancia("otra.md"))
        self.assertIsNone(core.leer("seis.md"))

    # CP-006 · que NO pase: escribir fuera de la carpeta de datos
    def test_no_se_escribe_fuera_de_la_carpeta(self):
        with self.assertRaises(core.RutaFueraDeLaPlataforma):
            core.guardar("../afuera.md", "no debería quedar", constancia("../afuera.md"))
        self.assertFalse(
            os.path.exists(os.path.join(os.path.dirname(self.carpeta), "afuera.md")))

    def test_no_se_lee_fuera_de_la_carpeta(self):
        with self.assertRaises(core.RutaFueraDeLaPlataforma):
            core.leer("../../algo.md")


class EstaVivaTests(TestCase):
    """CP-001 de la fase A · la plataforma responde, sin salir a la red.

    La ruta se movió de «/» a «/esta-viva/» en la fase B, cuando la raíz pasó a
    ser la lista de proyectos. **La comprobación sigue haciendo falta**: dice
    si la plataforma responde sin depender de que haya proyectos conectados.

    **Y exige haber entrado, como todo lo demás.** Se pensó dejarla abierta —una
    comprobación de vida que pide contraseña no puede responder «estoy caída»—,
    y se descartó: esta dice **la ruta de la carpeta de datos**, que es
    información. Una comprobación que revela dónde vive algo no responde a
    cualquiera.
    """

    def setUp(self):
        para_probar.como_usuario(self.client)

    def test_responde_que_esta_viva(self):
        respuesta = self.client.get("/esta-viva/")
        self.assertEqual(respuesta.status_code, 200)
        self.assertIn("está viva", respuesta.content.decode("utf-8"))


class SinRedTests(TestCase):
    """CP-001 · con la salida a la red tapada, la plataforma sigue sirviendo.

    Desconectar la máquina de verdad lo hace una persona. Lo que esta prueba
    deja automático es lo que esa desconexión buscaba encontrar: que nada de la
    plataforma dependa de una conexión que salga afuera.
    """

    def setUp(self):
        # Todas las pantallas exigen haber entrado desde `EP-022`.
        para_probar.como_usuario(self.client)
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
            self.assertEqual(self.client.get("/esta-viva/").status_code, 200)
            with override_settings(CARPETA_DATOS=carpeta):
                core.guardar("uno.md", "# Uno\n", constancia("uno.md"))
                self.assertEqual(core.leer("uno.md"), "# Uno\n")
        finally:
            shutil.rmtree(carpeta, ignore_errors=True)
