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
        """Agrega turnos a una sesión, **continuando su numeración**.

        Empezar siempre en 1 choca con el orden único cuando la misma sesión
        recibe dos tandas, que es lo que hacen las pruebas de la fase B.
        """
        ya = sesion.mensajes.count()
        for orden, texto in enumerate(textos, ya + 1):
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
        mas = self.sesion("historico-chat/2026-01-05-cuatro.md", "2026-01-05")
        self.dice(otra, "el manual de instalación quedó incompleto")
        self.dice(mas, "el manual de instalación va aparte")
        frases = [r["frase"] for r in repeticion.correcciones(limite=50)]
        self.assertIn("espanol colombiano", frases)
        self.assertIn("manual instalacion", frases)


class ElReporteSaleOrdenadoYPorPeriodo(Base):
    """`CA-01` — de lo más repetido a lo menos, y por período."""

    def setUp(self):
        vieja = self.sesion("historico-chat/2026-01-02-vieja.md", "2026-01-02")
        otra = self.sesion("historico-chat/2026-01-09-otra.md", "2026-01-09")
        nueva = self.sesion("historico-chat/2026-02-10-nueva.md", "2026-02-10")
        despues = self.sesion("historico-chat/2026-02-14-despues.md", "2026-02-14")
        # **Repartidas en días distintos a propósito.** Repetir algo tres veces
        # el mismo día es insistir en una conversación; lo que señala una regla
        # que falta es que vuelva a aparecer otro día.
        self.dice(vieja, "revise el plan de trabajo otra vez",
                         "el plan de trabajo va antes")
        self.dice(otra, "el plan de trabajo se aprueba")
        self.dice(nueva, "escriba la señal cuando aparece")
        self.dice(despues, "la señal cuando aparece, no al cerrar")

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


class LoGenericoNoEncabezaElReporte(Base):
    """Fase B · lo hecho con el vocabulario de todos los días no señala nada.

    **El caso está medido.** El primer reporte sobre datos reales lo encabezaban
    «debe quedar» (22 veces), «debe tener» y «debe estar»: no son correcciones,
    son la forma en que el usuario redacta cualquier exigencia.
    """

    def corpus(self, cuantas=10):
        """Sesiones suficientes para que haya vocabulario que calcular."""
        for i in range(cuantas):
            s = self.sesion("historico-chat/2026-01-%02d-una.md" % (i + 1),
                            "2026-01-%02d" % (i + 1))
            # «debe quedar» en todas: es vocabulario, no tema.
            self.dice(s, "esto debe quedar escrito en alguna parte")
            # En dos de diez: por encima del mínimo de sesiones y por debajo
            # de lo que cuenta como vocabulario. Es la franja donde vive un tema.
            if i < 2:
                self.dice(s, "recuerde el español colombiano otra vez")

    def test_lo_dicho_en_muchas_sesiones_no_es_tema(self):
        self.corpus()
        frases = [r["frase"] for r in repeticion.correcciones(limite=50)]
        self.assertNotIn("debe quedar", frases)

    def test_lo_que_si_es_tema_queda(self):
        self.corpus()
        frases = [r["frase"] for r in repeticion.correcciones(limite=50)]
        self.assertIn("espanol colombiano", frases)

    def test_el_vocabulario_se_calcula_no_se_escribe(self):
        self.corpus()
        de_la_casa = repeticion.vocabulario_de_la_casa(
            list(Mensaje.objects.filter(quien="usuario")))
        self.assertIn("debe", de_la_casa)
        self.assertNotIn("colombiano", de_la_casa)

    def test_con_pocas_sesiones_no_se_filtra(self):
        """**Sobre tres conversaciones no hay vocabulario que calcular.** Si se
        filtrara igual, el reporte saldría vacío y se leería como «no hubo nada»."""
        self.corpus(cuantas=2)
        self.assertEqual(set(), repeticion.vocabulario_de_la_casa(
            list(Mensaje.objects.filter(quien="usuario"))))


class LoQueSePegaNoEsLoQueSeDijo(Base):
    """Una ruta de archivo tampoco es una frase que la persona repita."""

    def test_una_ruta_pegada_no_cuenta(self):
        """«ing jose» encabezaba el reporte con doce sesiones, y sale del nombre
        de una carpeta pegada en el mensaje."""
        limpio = repeticion.sin_lo_de_la_maquina(
            "mire c:/Ing. Jose/ia/agente y arregle")
        self.assertNotIn("Jose", limpio)
        self.assertIn("arregle", limpio)

    def test_lo_demas_del_mensaje_se_conserva(self):
        limpio = repeticion.sin_lo_de_la_maquina(
            "revise historico-chat/2026-01-02.md y me dice")
        self.assertIn("revise", limpio)
        self.assertIn("me dice", limpio)


class RepetirEnUnSoloDiaEsInsistir(Base):
    """Fase B · lo que señala una regla que falta es volver a decirlo otro día."""

    def test_tres_veces_el_mismo_dia_no_entra(self):
        una = self.sesion()
        self.dice(una, "revise el plan de trabajo",
                       "el plan de trabajo va antes",
                       "el plan de trabajo se aprueba")
        self.assertEqual([], repeticion.correcciones())

    def test_dos_dias_distintos_si(self):
        una = self.sesion("historico-chat/2026-01-02-una.md", "2026-01-02")
        otra = self.sesion("historico-chat/2026-01-09-otra.md", "2026-01-09")
        self.dice(una, "revise el plan de trabajo")
        self.dice(otra, "el plan de trabajo va antes")
        self.assertEqual("plan trabajo",
                         repeticion.correcciones()[0]["frase"])

    def test_primero_lo_que_aparece_en_mas_dias(self):
        for i in range(4):
            s = self.sesion("historico-chat/2026-01-%02d-x.md" % (i + 1),
                            "2026-01-%02d" % (i + 1))
            self.dice(s, "recuerde el español colombiano")
        una = self.sesion("historico-chat/2026-02-01-y.md", "2026-02-01")
        otra = self.sesion("historico-chat/2026-02-02-z.md", "2026-02-02")
        # Diez veces, pero en dos días: va después de las cuatro.
        self.dice(una, *(["suba el manual de instalacion"] * 5))
        self.dice(otra, *(["suba el manual de instalacion"] * 5))
        self.assertEqual("espanol colombiano",
                         repeticion.correcciones()[0]["frase"])


class LoQueDiceElAgenteNoSeCuenta(Base):
    """Se mide lo que el usuario tuvo que repetir, no lo que el agente contestó."""

    def test_solo_cuentan_los_mensajes_del_usuario(self):
        una = self.sesion()
        for orden in (1, 2):
            Mensaje.objects.create(sesion=una, orden=orden, quien="agente",
                                   cuando="10:00",
                                   texto="el plan de trabajo quedó escrito")
        self.assertEqual([], repeticion.correcciones())
