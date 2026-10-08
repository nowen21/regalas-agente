# -*- coding: utf-8 -*-
"""`EP-027·HU-006` · CP-001 de la fase A: la regla del proyecto versiona su proyecto."""
from django.test import TestCase

from core.estandar.models import Regla, ReglaTarea, Tarea
from core.historia.models import ESTANDAR, PROYECTO, Cambio, Version
from core.historia.registro import quien_y_por_que
from core.proyectos.models import Proyecto


class LaReglaVersionaSuAmbito(TestCase):

    def setUp(self):
        self.proyecto = Proyecto.objects.create(nombre="Prueba", ruta="C:/prueba")

    def cuantas(self):
        return (Version.objects.filter(ambito=ESTANDAR).count(),
                Version.objects.filter(ambito=PROYECTO, proyecto=self.proyecto).count())

    def test_la_del_proyecto_sube_la_del_proyecto(self):
        antes = self.cuantas()
        with quien_y_por_que(quien="prueba", motivo="prueba"):
            regla = Regla.objects.create(proyecto=self.proyecto, codigo="P1", titulo="Algo", exigencia="Algo.")
            ReglaTarea.objects.create(regla=regla, tarea=Tarea.objects.create(nombre="cambiar-codigo"))
        despues = self.cuantas()
        # La tarea nueva es del estándar: las tareas son de todos. La regla y su tarea, del proyecto.
        self.assertEqual((antes[0] + 1, antes[1] + 1), despues)
        relacion = regla.aplica.first()
        version = Cambio.objects.get(tabla="estandar.reglatarea", fila=str(relacion.pk)).version
        self.assertEqual((PROYECTO, self.proyecto.pk), (version.ambito, version.proyecto_id))

    def test_la_del_estandar_sube_la_del_estandar(self):
        antes = self.cuantas()
        with quien_y_por_que(quien="prueba", motivo="prueba"):
            Regla.objects.create(codigo="ZZ1", titulo="Algo", exigencia="Algo.")
        despues = self.cuantas()
        self.assertEqual(antes[0] + 1, despues[0])
        self.assertEqual(antes[1], despues[1])
