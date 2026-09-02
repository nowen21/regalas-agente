# -*- coding: utf-8 -*-
"""Los casos del plan de pruebas de la fase `Y-EP-011-HU-003` — `F-032`.

**El caso que decide es el CP-002:** que la línea base salga siempre marcada como
reconstruida. La de verdad debió tomarse antes de empezar y no se tomó; una que
se presente como un antes hace que la mejora parezca mayor de lo que es.

**Y el que evita el número falso es el CP-003:** que un hueco de cuatro horas no
se cuente como cuatro horas de revisión. Contarlo convertiría un almuerzo en el
mejor dato del reporte.
"""
from django.test import TestCase

from nucleo.medicion import revision
from nucleo.medicion.models import Mensaje, Sesion
from nucleo.proyectos.models import Proyecto


class Turno(object):
    """Un mensaje, sin tocar la base: `huecos` solo necesita estos dos campos."""

    def __init__(self, quien, cuando):
        self.quien = quien
        self.cuando = cuando


class LosHuecosSeMiden(TestCase):
    """`CA-2`: medir no obliga al usuario a anotar nada a mano."""

    def test_el_hueco_es_entre_la_respuesta_del_agente_y_lo_que_sigue(self):
        medidos = revision.huecos([
            Turno("usuario", "2026-09-01 10:00:00"),
            Turno("agente", "2026-09-01 10:01:00"),
            Turno("usuario", "2026-09-01 10:03:00"),
        ])
        self.assertEqual([120.0], medidos["segundos"])

    def test_dos_mensajes_seguidos_del_agente_no_son_una_revision(self):
        medidos = revision.huecos([
            Turno("agente", "2026-09-01 10:00:00"),
            Turno("agente", "2026-09-01 10:05:00"),
        ])
        self.assertEqual([], medidos["segundos"])

    def test_un_mensaje_sin_hora_se_cuenta_aparte_y_no_se_inventa(self):
        medidos = revision.huecos([
            Turno("agente", "hora no registrada"),
            Turno("usuario", "2026-09-01 10:03:00"),
        ])
        self.assertEqual([], medidos["segundos"])
        self.assertEqual(1, medidos["descartados_sin_hora"])

    def test_el_si_de_dos_segundos_no_es_una_revision(self):
        medidos = revision.huecos([
            Turno("agente", "2026-09-01 10:00:00"),
            Turno("usuario", "2026-09-01 10:00:01"),
        ])
        self.assertEqual([], medidos["segundos"])


class LasHorasNoSeInventan(TestCase):
    """El CP-003: un hueco larguísimo no es revisión, es que se fue."""

    def test_un_hueco_de_cuatro_horas_se_descarta_y_se_cuenta(self):
        medidos = revision.huecos([
            Turno("agente", "2026-09-01 10:00:00"),
            Turno("usuario", "2026-09-01 14:00:00"),
        ])
        self.assertEqual([], medidos["segundos"])
        self.assertEqual(1, medidos["descartados_largos"])

    def test_uno_de_una_hora_si_cuenta(self):
        medidos = revision.huecos([
            Turno("agente", "2026-09-01 10:00:00"),
            Turno("usuario", "2026-09-01 11:00:00"),
        ])
        self.assertEqual([3600.0], medidos["segundos"])
        self.assertEqual(0, medidos["descartados_largos"])


class Base(TestCase):

    def setUp(self):
        self.proyecto = Proyecto.objects.create(
            identificador="de-prueba", nombre="De prueba",
            ruta_codigo="/x", ruta_normalizada="/x", conectado="conectado")

    def sesion(self, fecha, pares, archivo=None):
        """Una sesión con `pares` revisiones de un minuto cada una."""
        creada = Sesion.objects.create(
            proyecto=self.proyecto, archivo=archivo or ("historico/%s-%d.md"
                                                        % (fecha, pares)),
            fecha=fecha, tema="de mentiras", huella="x")
        orden = 0
        hora = 8
        minuto = 0
        for _ in range(pares):
            Mensaje.objects.create(
                sesion=creada, orden=orden, quien="agente",
                cuando="%s %02d:%02d:00" % (fecha, hora, minuto), texto="a")
            orden += 1
            Mensaje.objects.create(
                sesion=creada, orden=orden, quien="usuario",
                cuando="%s %02d:%02d:00" % (fecha, hora, minuto + 1), texto="u")
            orden += 1
            minuto += 2
            if minuto >= 58:
                minuto = 0
                hora += 1
        return creada


class CP001SeMideMesAMes(Base):

    def test_cada_mes_trae_su_cuenta_su_total_y_su_mediana(self):
        self.sesion("2026-07-01", 12)
        self.sesion("2026-08-01", 15)
        meses = revision.por_mes("de-prueba")
        self.assertEqual(["2026-07", "2026-08"],
                         [uno["mes"] for uno in meses])
        self.assertEqual(12, meses[0]["cuantos"])
        self.assertEqual(60.0, meses[0]["mediana_segundos"])

    def test_sin_nada_indexado_devuelve_lista_vacia(self):
        self.assertEqual([], revision.por_mes("de-prueba"))


class CP002LaLineaBaseSiempreDiceQueEsReconstruida(Base):
    """`CA-1`, y la advertencia que la ficha dejó escrita."""

    def test_la_base_es_el_mes_mas_viejo_con_datos_suficientes(self):
        self.sesion("2026-07-01", 12)
        self.sesion("2026-08-01", 15)
        base = revision.linea_base("de-prueba")
        self.assertEqual("2026-07", base["mes"])
        self.assertTrue(base["reconstruida"])

    def test_un_mes_con_muy_pocas_revisiones_no_sirve_de_base(self):
        self.sesion("2026-07-01", 2)
        self.sesion("2026-08-01", 15)
        self.assertEqual("2026-08", revision.linea_base("de-prueba")["mes"])

    def test_la_comparacion_dice_que_la_base_no_es_un_antes_de_verdad(self):
        self.sesion("2026-07-01", 12)
        self.sesion("2026-08-01", 15)
        escrito = revision.dicho(revision.comparar("de-prueba"))
        self.assertIn("reconstruida, no tomada", escrito)
        self.assertIn("no se tomó", escrito)


class CP004CuandoNoSePuedeCompararSeDice(Base):
    """Lo que salió al correrlo contra el histórico real de este repositorio."""

    def test_con_un_solo_mes_no_se_compara_y_se_explica(self):
        self.sesion("2026-08-01", 20)
        comparada = revision.comparar("de-prueba")
        self.assertFalse(comparada["se_puede_comparar"])
        self.assertIn("un mes", comparada["por_que"])
        self.assertIn("No se puede comparar", revision.dicho(comparada))

    def test_sin_nada_indexado_se_dice_y_no_se_devuelve_cero(self):
        comparada = revision.comparar("de-prueba")
        self.assertFalse(comparada["se_puede_comparar"])
        self.assertIsNone(comparada["cambio_mediana"])
        self.assertIn("ninguna sesión indexada", comparada["por_que"])

    def test_con_dos_meses_se_compara_y_se_dice_hacia_donde(self):
        self.sesion("2026-07-01", 12)
        self.sesion("2026-08-01", 15)
        comparada = revision.comparar("de-prueba")
        self.assertTrue(comparada["se_puede_comparar"])
        self.assertEqual(0.0, comparada["cambio_mediana"])
