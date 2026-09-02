# -*- coding: utf-8 -*-
"""Los casos del plan de pruebas de la fase `R-EP-017-HU-004`.

**El caso que decide es el CP-002:** que sin coincidencias se diga que no hay.
Una lista vacía y una búsqueda que no se pudo hacer se ven igual, y la
diferencia importa.

**Y el CP-003 es el que la vuelve usable:** responder rápido no es un lujo. Una
consulta que tarda se deja de hacer, y una auditoría que nadie consulta es lo
mismo que no tenerla.
"""
from django.test import TestCase

from . import busqueda
from .models import Registro


def _registrar(cuando, proyecto, que_se_hizo, sobre_que="algo"):
    return Registro.objects.create(
        cuando=cuando, quien="el agente", que_se_hizo=que_se_hizo,
        sobre_que=sobre_que, proyecto=proyecto)


class Base(TestCase):

    def setUp(self):
        _registrar("2026-08-01 10:00:00", "uno", "conectar un proyecto")
        _registrar("2026-08-15 11:00:00", "uno", "traer la documentación")
        _registrar("2026-09-01 12:00:00", "uno", "aprobar un documento")
        _registrar("2026-09-01 13:00:00", "otro", "aprobar un documento")


class CP001SeFiltraPorLoQueSePida(Base):

    def test_sin_filtros_salen_todos(self):
        self.assertEqual(busqueda.buscar()["cuantos"], 4)

    def test_por_proyecto(self):
        self.assertEqual(busqueda.buscar(proyecto="uno")["cuantos"], 3)

    def test_por_fecha_desde(self):
        self.assertEqual(busqueda.buscar(desde="2026-09-01")["cuantos"], 2)

    def test_por_fecha_hasta_incluye_el_dia_completo(self):
        """Quien escribe una fecha quiere ese día entero, no su medianoche."""
        self.assertEqual(busqueda.buscar(hasta="2026-09-01")["cuantos"], 4)

    def test_por_tipo_de_accion(self):
        self.assertEqual(busqueda.buscar(accion="aprobar")["cuantos"], 2)

    def test_los_filtros_se_combinan(self):
        self.assertEqual(
            busqueda.buscar(proyecto="uno", accion="aprobar")["cuantos"], 1)

    def test_salen_del_mas_nuevo_al_mas_viejo(self):
        hallados = busqueda.buscar(proyecto="uno")["hallados"]
        self.assertEqual(hallados[0].cuando, "2026-09-01 12:00:00")

    def test_los_tipos_se_derivan_de_lo_que_hay(self):
        """Una lista escrita a mano se queda corta y nadie lo nota."""
        self.assertEqual(len(busqueda.tipos_de_accion()), 3)
        self.assertEqual(len(busqueda.tipos_de_accion(proyecto="otro")), 1)


class CP002SinCoincidenciasSeDice(Base):
    """**El caso que decide.** Vacío y fallido se ven igual."""

    def test_una_busqueda_sin_resultados_lo_dice(self):
        resultado = busqueda.buscar(accion="cocinar una arepa")
        self.assertFalse(resultado["hubo"])
        self.assertEqual(resultado["cuantos"], 0)

    def test_y_la_frase_lo_distingue_de_un_fallo(self):
        resultado = busqueda.buscar(accion="cocinar una arepa")
        self.assertIn("no pasó nada así", busqueda.dicho(resultado))

    def test_con_resultados_la_frase_dice_cuántos(self):
        self.assertIn("4 registro", busqueda.dicho(busqueda.buscar()))


class CP003ResponderRapido(TestCase):
    """Una consulta que tarda se deja de hacer."""

    def test_con_un_ano_de_registros_responde_en_menos_de_un_segundo(self):
        registros = []
        for dia in range(365):
            registros.append(Registro(
                cuando="2026-%02d-%02d 10:00:00" % (dia % 12 + 1, dia % 28 + 1),
                quien="el agente", que_se_hizo="una acción cualquiera",
                sobre_que="algo", proyecto="uno"))
        Registro.objects.bulk_create(registros)

        resultado = busqueda.buscar(proyecto="uno", accion="acción")
        self.assertEqual(resultado["cuantos"], 365)
        self.assertLess(resultado["segundos"], 1.0)

    def test_se_recorta_y_se_dice(self):
        """Recortar en silencio es lo mismo que perder."""
        Registro.objects.bulk_create([
            Registro(cuando="2026-08-%02d 10:00:00" % (uno % 28 + 1),
                     quien="el agente", que_se_hizo="algo", sobre_que="x",
                     proyecto="uno")
            for uno in range(50)])
        resultado = busqueda.buscar(cuantas=10)
        self.assertTrue(resultado["se_recorto"])
        self.assertEqual(len(resultado["hallados"]), 10)
        self.assertIn("más recientes", busqueda.dicho(resultado))
