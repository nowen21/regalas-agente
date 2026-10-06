# -*- coding: utf-8 -*-
"""`manage.py registrar`: la puerta por la que el instalador da de alta un proyecto.

    python manage.py registrar --nombre agro-system --ruta C:\\proyectos\\agro-system
    python manage.py registrar --ruta C:\\proyectos\\agro-system --baja

Repetirla con la misma carpeta no cambia nada, salvo que estuviera dada de baja:
entonces la vuelve a activar. `--baja` es su contraria (`EP-025·HU-021`): la
usa la desinstalación, y el proyecto no se borra.
"""
from django.core.management.base import BaseCommand, CommandError

from core.proyectos.models import Proyecto
from core.proyectos.registro import dar_de_baja, reactivar, registrar


class Command(BaseCommand):
    help = "Registra un proyecto en Cimiento si su carpeta no lo está; con --baja, lo desactiva."

    def add_arguments(self, parser):
        parser.add_argument("--nombre", default="")
        parser.add_argument("--ruta", required=True)
        parser.add_argument("--scope", default="", help="Se acepta y no se guarda.")
        parser.add_argument("--baja", action="store_true", help="desactiva el proyecto; no lo borra")

    def handle(self, *args, **opciones):
        if opciones["baja"]:
            hecho = dar_de_baja(Proyecto, opciones["ruta"])
            self.stdout.write("dado de baja" if hecho else "no estaba activo")
            return
        if not opciones["nombre"]:
            raise CommandError("registrar pide --nombre")
        if registrar(Proyecto, opciones["nombre"], opciones["ruta"]):
            self.stdout.write("registrado")
        elif reactivar(Proyecto, opciones["ruta"]):
            self.stdout.write("reactivado")
        else:
            self.stdout.write("ya estaba registrado")
