# -*- coding: utf-8 -*-
"""Los siete casos del plan de pruebas de la fase D.

El que decide es `CP-007`: contar los registros, ejecutar todo lo que la
plataforma sabe hacer, y volver a contar. Si sale uno de menos, hay un camino
que escribe saltándose la auditoría, y los otros seis casos en verde no lo
habrían visto.

**Ninguna clave de estas pruebas es real.** Son inventadas, y eso también es
parte de lo que se está probando (`00·N6`).
"""
import io
import os
import shutil
import tempfile

from django.test import TestCase, override_settings

from nucleo.almacen import core as almacen
from nucleo.constancia import SinConstancia
from . import core
from .models import Registro, SoloSeAgrega


class BaseAuditoria(TestCase):
    """Cada prueba corre sobre una carpeta de datos propia y desechable."""

    def setUp(self):
        self.carpeta = tempfile.mkdtemp(prefix="prueba-auditoria-")
        self.contexto = override_settings(CARPETA_DATOS=self.carpeta)
        self.contexto.enable()

    def tearDown(self):
        self.contexto.disable()
        shutil.rmtree(self.carpeta, ignore_errors=True)

    def _texto_del_registro(self):
        carpeta = os.path.join(self.carpeta, "auditoria")
        salida = ""
        for nombre in sorted(os.listdir(carpeta)):
            with io.open(os.path.join(carpeta, nombre), encoding="utf-8") as f:
                salida += f.read()
        return salida


class RegistrarTests(BaseAuditoria):
    """CP-001 · la acción queda registrada con sus seis datos."""

    def test_la_accion_queda_con_sus_seis_datos(self):
        fila = core.registrar(
            que_se_hizo="conectar un proyecto",
            sobre_que="rni-back",
            quien="el usuario",
            que_cambio="quedó registrado",
            proyecto="rni-back",
            sesion="5f06ce4e")

        for columna in core.COLUMNAS:
            self.assertIn(columna, fila.fila)
        self.assertEqual(fila.fila["quién"], "el usuario")
        self.assertTrue(fila.fila["cuándo"])

        guardado = Registro.objects.get(que_se_hizo="conectar un proyecto")
        self.assertEqual(guardado.proyecto, "rni-back")
        self.assertEqual(guardado.sesion, "5f06ce4e")

    def test_una_accion_sin_proyecto_se_registra_igual(self):
        fila = core.registrar(
            que_se_hizo="publicar una versión de reglas",
            sobre_que="VERSION",
            quien="el agente")

        self.assertEqual(fila.fila["proyecto"], "")
        self.assertEqual(Registro.objects.filter(proyecto="").count(), 1)

    def test_lo_registrado_queda_como_texto_legible(self):
        core.registrar("conectar un proyecto", "rni-back", "el usuario")
        texto = self._texto_del_registro()
        self.assertIn("conectar un proyecto", texto)
        self.assertIn("| cuándo |", texto)

    def test_el_indice_se_rehace_desde_el_texto(self):
        core.registrar("una acción", "algo", "el agente")
        core.registrar("otra acción", "algo", "el agente")
        Registro.objects.todos().delete()
        self.assertEqual(Registro.objects.count(), 0)

        cuantas = core.reconstruir_indice()

        self.assertEqual(cuantas, 2)
        self.assertEqual(Registro.objects.count(), 2)


class IntegridadTests(BaseAuditoria):
    """CP-002 · editar o borrar no se puede, y el intento queda."""

    def test_editar_una_fila_del_indice_no_se_puede(self):
        core.registrar("una acción", "algo", "el agente")
        guardado = Registro.objects.first()
        guardado.que_se_hizo = "otra cosa"

        with self.assertRaises(SoloSeAgrega):
            guardado.save()

        self.assertEqual(Registro.objects.first().que_se_hizo, "una acción")

    def test_borrar_una_fila_del_indice_no_se_puede(self):
        core.registrar("una acción", "algo", "el agente")
        guardado = Registro.objects.first()

        with self.assertRaises(SoloSeAgrega):
            guardado.delete()

        with self.assertRaises(SoloSeAgrega):
            Registro.objects.all().delete()

        self.assertEqual(Registro.objects.count(), 1)

    def test_actualizar_en_bloque_no_se_puede(self):
        core.registrar("una acción", "algo", "el agente")
        with self.assertRaises(SoloSeAgrega):
            Registro.objects.all().update(quien="otro")

    def test_el_intento_de_editar_queda_registrado(self):
        core.registrar("una acción", "algo", "el agente")
        antes = Registro.objects.count()

        with self.assertRaises(core.LoRegistradoNoSeToca):
            core.editar()

        self.assertEqual(Registro.objects.count(), antes + 1)
        self.assertIn("intento de editar", self._texto_del_registro())

    def test_el_intento_de_borrar_queda_registrado(self):
        with self.assertRaises(core.LoRegistradoNoSeToca):
            core.borrar()
        self.assertIn("intento de borrar", self._texto_del_registro())

    def test_lo_ya_escrito_no_se_reescribe_al_agregar(self):
        core.registrar("primera", "algo", "el agente")
        primero = self._texto_del_registro()
        core.registrar("segunda", "algo", "el agente")
        despues = self._texto_del_registro()

        self.assertTrue(despues.startswith(primero))


class SinConstanciaNoHayEfectoTests(BaseAuditoria):
    """CP-003 · con el registro bloqueado, nada cambia."""

    def _bloquear_la_carpeta(self):
        """Deja la carpeta de auditoría sin poder escribirse.

        En Windows quitar el permiso de escritura a una carpeta no impide
        crear archivos dentro, así que se bloquea de la forma que sí funciona
        en los dos sistemas: se pone un **archivo** donde tiene que ir la
        carpeta. Lo que se prueba es el comportamiento ante la falla de
        escritura, no la forma de provocarla.
        """
        ruta = os.path.join(self.carpeta, "auditoria")
        if os.path.isdir(ruta):
            shutil.rmtree(ruta)
        with io.open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write("no soy una carpeta")

    def test_si_no_se_puede_registrar_revienta(self):
        self._bloquear_la_carpeta()
        with self.assertRaises(core.RegistroNoSePudoEscribir):
            core.registrar("una acción", "algo", "el agente")

    def test_la_accion_no_se_ejecuta_si_no_hubo_constancia(self):
        self._bloquear_la_carpeta()
        huella = []

        def accion(comprobante):
            huella.append("se ejecutó")
            return almacen.guardar("cambiado.md", "no debería quedar",
                                   comprobante)

        with self.assertRaises(core.RegistroNoSePudoEscribir):
            core.con_constancia(accion, que_se_hizo="cambiar algo",
                                sobre_que="cambiado.md", quien="el agente")

        self.assertEqual(huella, [], "la acción se ejecutó sin constancia")
        self.assertFalse(os.path.exists(os.path.join(self.carpeta, "cambiado.md")))

    def test_con_constancia_ejecuta_cuando_si_se_pudo_registrar(self):
        resultado = core.con_constancia(
            lambda c: almacen.guardar("cambiado.md", "# Cambiado" + chr(10), c),
            que_se_hizo="cambiar algo", sobre_que="cambiado.md",
            quien="el agente")

        self.assertTrue(resultado)
        self.assertEqual(almacen.leer("cambiado.md"), "# Cambiado\n")
        self.assertEqual(Registro.objects.count(), 1)

    def test_la_constancia_se_escribe_antes_de_ejecutar(self):
        """No basta con que las dos cosas pasen: importa el orden."""
        orden = []

        def accion(_comprobante):
            orden.append("efecto")

        original = core._agregar

        def espiar(nombre, linea):
            orden.append("constancia")
            return original(nombre, linea)

        core._agregar = espiar
        try:
            core.con_constancia(accion, que_se_hizo="cambiar algo",
                                sobre_que="algo", quien="el agente")
        finally:
            core._agregar = original

        self.assertEqual(orden, ["constancia", "efecto"])


class CredencialesTests(BaseAuditoria):
    """CP-004 y CP-005 · la clave se tapa; el molde no."""

    def test_la_clave_entre_comillas_queda_tapada(self):
        core.registrar("conectar", 'password: "inventada123"', "el agente")
        texto = self._texto_del_registro()
        self.assertNotIn("inventada123", texto)
        self.assertIn("password", texto)

    def test_la_clave_sin_comillas_tambien_queda_tapada(self):
        core.registrar("conectar", "API_KEY=inventada456", "el agente")
        texto = self._texto_del_registro()
        self.assertNotIn("inventada456", texto)
        self.assertIn("API_KEY", texto)

    def test_la_clave_en_cualquier_campo_queda_tapada(self):
        core.registrar("conectar", "algo", "el agente",
                       que_cambio="secret=inventada789")
        self.assertNotIn("inventada789", self._texto_del_registro())

    def test_el_molde_no_se_tapa(self):
        core.registrar("documentar", "clave: tu-clave", "el agente",
                       que_cambio="usar changeme mientras tanto")
        texto = self._texto_del_registro()
        self.assertIn("tu-clave", texto)
        self.assertIn("changeme", texto)

    def test_lo_indexado_tampoco_trae_la_clave(self):
        core.registrar("conectar", 'password: "inventada123"', "el agente")
        guardado = Registro.objects.first()
        self.assertNotIn("inventada123", guardado.sobre_que)


class EnlaceConLaSesionTests(BaseAuditoria):
    """CP-006 · el enlace a la sesión está, y aguanta el renombre."""

    def test_la_accion_de_una_sesion_trae_su_enlace(self):
        core.registrar("conectar", "algo", "el agente",
                       sesion="5f06ce4e-64bf-41e5-b58e-87959b32bf62")
        guardado = Registro.objects.first()
        self.assertEqual(guardado.sesion,
                         "5f06ce4e-64bf-41e5-b58e-87959b32bf62")

    def test_una_accion_fuera_de_toda_sesion_lo_trae_vacio(self):
        core.registrar("publicar", "VERSION", "el usuario")
        self.assertEqual(Registro.objects.first().sesion, "")

    def test_el_enlace_aguanta_que_el_archivo_se_renombre(self):
        """Lo que decide el caso.

        El archivo del histórico nace `AAAA-MM-DD-sesion.md` y se renombra
        cuando se le pone el tema. Si el registro hubiera guardado el nombre,
        acá se rompería; guarda el identificador, que no cambia.
        """
        historico = tempfile.mkdtemp(prefix="prueba-historico-")
        try:
            identificador = "5f06ce4e-64bf-41e5-b58e-87959b32bf62"
            viejo = os.path.join(historico, "2026-08-25-sesion.md")
            with io.open(viejo, "w", encoding="utf-8") as archivo:
                archivo.write("<!-- sesion: %s -->\n" % identificador)

            core.registrar("conectar", "algo", "el agente",
                           sesion=identificador)

            nuevo = os.path.join(historico, "2026-08-25-la-auditoria.md")
            os.rename(viejo, nuevo)

            guardado = Registro.objects.first()
            encontrado = [n for n in os.listdir(historico)
                          if identificador in io.open(
                              os.path.join(historico, n),
                              encoding="utf-8").read()]

            self.assertEqual(guardado.sesion, identificador)
            self.assertEqual(encontrado, ["2026-08-25-la-auditoria.md"])
        finally:
            shutil.rmtree(historico, ignore_errors=True)


class NadaCambiaSinRegistroTests(BaseAuditoria):
    """CP-007 · que NO pase: que algo cambie sin quedar registrado.

    Se cuentan los registros, se ejecuta todo lo que la plataforma sabe hacer
    a través del camino correcto, y se vuelve a contar. Es el caso que
    encontraría un camino que escribe saltándose la auditoría.
    """

    def test_cada_accion_deja_exactamente_un_registro(self):
        acciones = [
            ("guardar un documento", "uno.md",
             lambda c: almacen.guardar("uno.md", "# Uno" + chr(10), c)),
            ("guardar otro documento", "dos.md",
             lambda c: almacen.guardar("dos.md", "# Dos" + chr(10), c)),
            ("rehacer el índice", "el índice",
             lambda _c: almacen.reconstruir_indice()),
        ]
        antes = Registro.objects.count()

        for nombre, sobre_que, accion in acciones:
            core.con_constancia(accion, que_se_hizo=nombre,
                                sobre_que=sobre_que, quien="el agente")

        self.assertEqual(Registro.objects.count(), antes + len(acciones))

    def test_la_puerta_de_atras_quedo_cerrada(self):
        """Lo que antes era el hueco de `CP-007`, ahora rechazado.

        Escribir sin haber registrado la acción reventaba en silencio hasta el
        2026-08-25: el archivo cambiaba y no quedaba rastro. Ahora el almacén
        pide el comprobante, así que el descuido se convierte en un error.
        """
        antes = Registro.objects.count()

        with self.assertRaises(SinConstancia):
            almacen.guardar("por-la-puerta-de-atras.md",
                            "# Sin constancia" + chr(10), None)

        self.assertIsNone(almacen.leer("por-la-puerta-de-atras.md"))
        self.assertEqual(Registro.objects.count(), antes)

    def test_una_constancia_no_sirve_para_cambiar_otra_cosa(self):
        """El descuido más probable: reutilizar el comprobante que hay a mano."""
        comprobante = core.registrar("guardar un documento", "uno.md",
                                     "el agente")

        with self.assertRaises(SinConstancia):
            almacen.guardar("otro.md", "# Otro" + chr(10), comprobante)

        self.assertIsNone(almacen.leer("otro.md"))
