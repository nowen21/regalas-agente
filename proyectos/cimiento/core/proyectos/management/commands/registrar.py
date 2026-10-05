# -*- coding: utf-8 -*-
"""`manage.py registrar`: la puerta por la que el instalador da de alta un proyecto.

    python manage.py registrar --nombre agro-system --ruta C:\\proyectos\\agro-system

Repetirla con la misma carpeta no cambia nada.
"""
from django.core.management.base import BaseCommand

from core.proyectos.models import Proyecto
from core.proyectos.registro import registrar


class Command(BaseCommand):
    help = "Registra un proyecto en Cimiento si su carpeta no lo está."

    def add_arguments(self, parser):
        parser.add_argument("--nombre", required=True)
        parser.add_argument("--ruta", required=True)
        parser.add_argument("--scope", default="", help="Se acepta y no se guarda.")

    def handle(self, *args, **opciones):
        creado = registrar(Proyecto, opciones["nombre"], opciones["ruta"])
        self.stdout.write("registrado" if creado else "ya estaba registrado")
