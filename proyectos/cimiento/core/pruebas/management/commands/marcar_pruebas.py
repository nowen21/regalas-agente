# -*- coding: utf-8 -*-
"""`manage.py marcar_pruebas`: anota si un proyecto tiene la parte que revisa sus pruebas.

    python manage.py marcar_pruebas --ruta «carpeta» --tiene [--puesta]
    python manage.py marcar_pruebas --ruta «carpeta» --no-tiene
    python manage.py marcar_pruebas --ruta «carpeta» --quitar

`EP-029·HU-003` · La llaman el instalador y el desinstalador, que corren sin
Django. `--puesta` dice que la herramienta la instaló Cimiento. `--quitar` es la
contraria (`02·F30`): imprime `puesta=1` o `puesta=0` antes de borrar la
anotación, para que el desinstalador sepa si le toca quitar la herramienta.
"""
import os

from django.core.management.base import BaseCommand, CommandError

from core.proyectos.models import Proyecto

from ...models import PruebasDelProyecto


class Command(BaseCommand):
    help = "Anota si un proyecto tiene la parte que revisa sus pruebas."

    def add_arguments(self, parser):
        parser.add_argument("--ruta", required=True)
        grupo = parser.add_mutually_exclusive_group(required=True)
        grupo.add_argument("--tiene", action="store_true")
        grupo.add_argument("--no-tiene", action="store_true")
        grupo.add_argument("--quitar", action="store_true")
        parser.add_argument("--puesta", action="store_true", help="La herramienta la instaló Cimiento.")

    def handle(self, *args, **o):
        ruta = os.path.normcase(os.path.abspath(o["ruta"]))
        proyecto = next((p for p in Proyecto.objects.all()
                         if os.path.normcase(os.path.abspath(p.ruta)) == ruta), None)
        if proyecto is None:
            raise CommandError("No hay ningún proyecto registrado en «%s»." % o["ruta"])
        estado = PruebasDelProyecto.de(proyecto)
        if o["quitar"]:
            self.stdout.write("puesta=%d" % int(estado.instalada_por_cimiento))
            estado.delete()
            return
        estado.tiene_parte = o["tiene"]
        # Si la herramienta ya la había puesto Cimiento, sigue siendo suya aunque esta vez ya estuviera.
        estado.instalada_por_cimiento = estado.instalada_por_cimiento or (o["tiene"] and o["puesta"])
        estado.save()
        self.stdout.write("tiene=%d puesta=%d" % (int(estado.tiene_parte), int(estado.instalada_por_cimiento)))
