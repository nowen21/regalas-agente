# -*- coding: utf-8 -*-
"""Los casos del plan de pruebas de la fase `A-EP-011-HU-002`.

**El caso que decide es el `CA-03`**, y es real: en la conversación de este
repositorio se pidió *español colombiano* de tres maneras distintas. Tienen que
salir como una fila, no como tres.

**Y el que más protege es el `CA-04`**: sin nada repetido se dice, en vez de
rellenar el reporte con lo que solo se dijo una vez. Un reporte que siempre
tiene filas deja de leerse.
"""
from django.test import TestCase

from nucleo.proyectos.models import Proyecto
from . import repeticion
from .models import Mensaje, Sesion


class Base(TestCase):

    def sesion(self, archivo="historico-chat/2026-01-02-una.md",
               fecha="2026-01-02"):
        proyecto, _ = Proyecto.objects.get_or_create(
            identificador="de-prueba",
            defaults={"nombre": "De prueba", "ruta_codigo": "/no/importa",
                      "ruta_normalizada": "/no/importa",
                      "conectado": "2026-01-02"})
        return Sesion.objects.create(proyecto=proyecto, archivo=archivo,
                                     fecha=fecha, tema="", huella="x")

    def dice(self, sesion, *textos):
        for orden, texto in enumerate(textos, 1):
            Mensaje.objects.create(sesion=sesion, orden=orden, quien="usuario",
                                   cuando="10:00", texto=texto)


class QueCuentaComoCorreccion(TestCase):
    """`RN-6`, decidida con el usuario: todo menos las confirmaciones."""

    def test_una_confirmacion_no_es_correccion(self):
        for palabra in ("si", "Sí", "hágale", "listo", "OK", "siga"):
            self.assertFalse(repeticion.es_correccion(palabra), palabra)

    def test_un_pedido_si_lo_es(self):
        self.assertTrue(repeticion.es_correccion(
            "recuerde que todo va en español colombiano"))

    def test_lo_muy_corto_no_cuenta(self):
        """No alcanza para agrupar, y se deja fuera diciéndolo."""
        self.assertFalse(repeticion.es_correccion("no eso"))

    def test_lo_que_pego_la_herramienta_no_cuenta_como_dicho(self):
        """**Lo que el editor agrega no lo escribió una persona.** Antes de
        sacarlo, el reporte lo encabezaban frases como «this may», 139 veces."""
        pegado = ("<ide_opened_file>The user opened the file Untitled-1 in the "
                  "IDE. This may or may not be related to the current task."
                  "</ide_opened_file>\nlevante el servidor")
        self.assertEqual("levante el servidor",
                         repeticion.sin_lo_de_la_maquina(pegado).strip())

    def test_un_mensaje_que_es_solo_ruido_de_la_herramienta_no_cuenta(self):
        solo_ruido = ("<system-reminder>algo largo que agrega la herramienta"
                      "</system-reminder>")
        self.assertFalse(repeticion.es_correccion(solo_ruido))


class LoMismoDichoDistintoCuentaComoUno(Base):
    """`CA-03` — el caso real de este repositorio."""

    def setUp(self):
        una = self.sesion("historico-chat/2026-01-02-una.md", "2026-01-02")
        otra = self.sesion("historico-chat/2026-01-03-otra.md", "2026-01-03")
        self.dice(una, "adapte la plantilla al español colombiano",
                       "recuerde el español colombiano")
        self.dice(otra, "pero español colombiano cómo sería")

    def _fila(self, frase):
        for r in repeticion.correcciones(limite=50):
            if r["frase"] == frase:
                return r
        return None

    def test_las_tres_formas_salen_como_una(self):
        fila = self._fila("espanol colombiano")
        self.assertIsNotNone(fila)
        self.assertEqual(3, fila["veces"])

    def test_dice_en_que_sesiones(self):
        """`CA-02` — cuántas veces y dónde."""
        fila = self._fila("espanol colombiano")
        self.assertEqual(2, len(fila["sesiones"]))
        self.assertIn("historico-chat/2026-01-02-una.md", fila["sesiones"])

    def test_no_se_agrupa_en_cadena(self):
        """Si A se parece a B y B a C, juntar las tres terminaría diciendo que
        todo es lo mismo. Cada frase repetida es su propia fila."""
        otra = self.sesion("historico-chat/2026-01-04-tres.md", "2026-01-04")
        self.dice(otra, "el manual de instalación quedó incompleto",
                        "el manual de instalación va aparte")
        frases = [r["frase"] for r in repeticion.correcciones(limite=50)]
        self.assertIn("espanol colombiano", frases)
        self.assertIn("manual instalacion", frases)


class ElReporteSaleOrdenadoYPorPeriodo(Base):
    """`CA-01` — de lo más repetido a lo menos, y por período."""

    def setUp(self):
        vieja = self.sesion("historico-chat/2026-01-02-vieja.md", "2026-01-02")
        nueva = self.sesion("historico-chat/2026-02-10-nueva.md", "2026-02-10")
        self.dice(vieja, "revise el plan de trabajo otra vez",
                         "el plan de trabajo va antes",
                         "el plan de trabajo se aprueba")
        self.dice(nueva, "escriba la señal cuando aparece",
                         "la señal cuando aparece, no al cerrar")

    def test_sale_lo_mas_repetido_primero(self):
        self.assertEqual("plan trabajo",
                         repeticion.correcciones(limite=5)[0]["frase"])

    def test_el_periodo_recorta(self):
        frases = [r["frase"] for r in
                  repeticion.correcciones(desde="2026-02-01", limite=50)]
        self.assertIn("senal aparece", frases)
        self.assertNotIn("plan trabajo", frases)

    def test_dos_corridas_dan_la_misma_lista(self):
        """Un reporte que cambia de orden entre corridas no se puede revisar."""
        self.assertEqual([r["frase"] for r in repeticion.correcciones()],
                         [r["frase"] for r in repeticion.correcciones()])


class SinNadaRepetidoSeDice(Base):
    """`CA-04` — no se rellena con lo que solo se dijo una vez."""

    def test_lo_dicho_una_sola_vez_no_entra(self):
        una = self.sesion()
        self.dice(una, "esto se dijo una sola vez y no se repite")
        self.assertEqual([], repeticion.correcciones())

    def test_pero_hubo_correcciones_que_mirar(self):
        """**Los dos silencios se distinguen.** «Nada se repitió» y «no había
        nada que mirar» devuelven la misma lista vacía."""
        una = self.sesion()
        self.dice(una, "esto se dijo una sola vez y no se repite")
        self.assertEqual([], repeticion.correcciones())
        self.assertEqual(1, repeticion.cuantas_correcciones())

    def test_sin_nada_indexado_la_cuenta_es_cero(self):
        self.assertEqual([], repeticion.correcciones())
        self.assertEqual(0, repeticion.cuantas_correcciones())

    def test_una_sesion_de_puras_confirmaciones_no_deja_nada(self):
        una = self.sesion()
        self.dice(una, "si", "si", "hágale", "listo", "siga")
        self.assertEqual(0, repeticion.cuantas_correcciones())
        self.assertEqual([], repeticion.correcciones())


class LoQueDiceElAgenteNoSeCuenta(Base):
    """Se mide lo que el usuario tuvo que repetir, no lo que el agente contestó."""

    def test_solo_cuentan_los_mensajes_del_usuario(self):
        una = self.sesion()
        for orden in (1, 2):
            Mensaje.objects.create(sesion=una, orden=orden, quien="agente",
                                   cuando="10:00",
                                   texto="el plan de trabajo quedó escrito")
        self.assertEqual([], repeticion.correcciones())
