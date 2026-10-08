"""`EP-027·HU-006` · Las reglas propias de un proyecto pasan a la tabla de reglas.

    manage.py pasar_reglas_proyecto --proyecto "C:/DesarrollosClaude/dp"
    manage.py pasar_reglas_proyecto --todos --borrar

Con `--borrar`, el archivo `.agente/reglas-proyecto.md` queda entero en la
historia del proyecto y se borra: desde ahí las reglas viven en Cimiento. Cada
proyecto sube su propia versión.
"""
import os

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from core.estandar.reglas import (ARCHIVO_DEL_PROYECTO, CodigoRepetido, archivo_a_la_historia,
                                  pasar_reglas_del_proyecto)
from core.historia import versiones
from core.historia.registro import quien_y_por_que
from core.proyectos.models import Proyecto


class Command(BaseCommand):
    help = "Pasa las reglas propias de un proyecto, o de todos, a la tabla de reglas."

    def add_arguments(self, parser):
        parser.add_argument("--proyecto", default="", help="la carpeta del proyecto")
        parser.add_argument("--todos", action="store_true")
        parser.add_argument("--borrar", action="store_true", help="guarda el archivo en la historia y lo borra")

    def handle(self, *args, proyecto="", todos=False, borrar=False, **opciones):
        if todos:
            proyectos = Proyecto.objects.filter(activo=True)
        elif proyecto:
            proyectos = Proyecto.objects.filter(ruta__iexact=os.path.abspath(proyecto))
            if not proyectos.exists():
                raise CommandError("el proyecto %s no está registrado en Cimiento" % proyecto)
        else:
            raise CommandError("falta --proyecto o --todos")
        for registrado in proyectos:
            archivo = os.path.join(registrado.ruta, *ARCHIVO_DEL_PROYECTO.split("/"))
            if not os.path.isfile(archivo):
                continue
            with open(archivo, encoding="utf-8") as f:
                texto = f.read()
            try:
                with transaction.atomic(), quien_y_por_que(
                        quien="pasar_reglas_proyecto", tipo=versiones.MENOR,
                        motivo="EP-027·HU-006: las reglas propias del proyecto pasan a la tabla de Cimiento"):
                    reglas = pasar_reglas_del_proyecto(registrado, texto)
                    if borrar:
                        archivo_a_la_historia(registrado, texto)
            except CodigoRepetido as razon:
                self.stderr.write("NO PASÓ: %s. Su archivo queda como está." % razon)
                continue
            if borrar:
                os.remove(archivo)
            self.stdout.write("%s: %d reglas en la tabla%s." % (registrado.nombre, len(reglas),
                                                                "; el archivo quedó en la historia y se borró"
                                                                if borrar else ""))
