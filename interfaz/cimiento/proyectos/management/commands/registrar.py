# -*- coding: utf-8 -*-
"""`manage.py registrar`: la puerta por la que el instalador da de alta un proyecto.

Antes el instalador anotaba la fila en `plantillas/proyectos.md` a mano; desde
el pendiente 76 el alta entra al registro de Cimiento y el `.md` se regenera.
"""
from django.core.management.base import BaseCommand

from cimiento.proyectos import core


class Command(BaseCommand):
    help = "Registra (o actualiza la ruta de) un proyecto y regenera proyectos.md"

    def add_arguments(self, parser):
        parser.add_argument("--nombre", required=True)
        parser.add_argument("--ruta", required=True)
        parser.add_argument("--scope", default="")
        parser.add_argument("--stack", default="por detectar")

    def handle(self, *args, **opts):
        creado = core.registrar(opts["nombre"], opts["ruta"], opts["scope"],
                                opts["stack"])
        self.stdout.write("registrado" if creado else "ya estaba; ruta al día")
