# -*- coding: utf-8 -*-
"""Crea una cuenta de la plataforma y la mete en su grupo.

    python manage.py crear_cuenta jose --grupo usuario
    python manage.py crear_cuenta el-agente --grupo agente

**La contraseña se pide sin mostrarla y no se recibe como argumento.** Una
contraseña escrita en la línea de órdenes queda en el historial de la consola,
que es un archivo de texto que nadie borra (`00·N6`).
"""
import getpass

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

from nucleo.acceso import grupos


class Command(BaseCommand):
    help = "Crea una cuenta de la plataforma y la pone en su grupo"

    def add_arguments(self, parser):
        parser.add_argument("nombre")
        parser.add_argument("--grupo", default=grupos.USUARIO,
                            choices=[grupos.USUARIO, grupos.AGENTE])
        parser.add_argument("--cambiar-clave", action="store_true",
                            help="solo cambiar la contraseña de una que ya está")

    def handle(self, *args, **opciones):
        grupos.poner_al_dia()
        Cuenta = get_user_model()
        nombre = opciones["nombre"]
        ya_estaba = Cuenta.objects.filter(username=nombre).first()

        if ya_estaba and not opciones["cambiar_clave"]:
            self.stdout.write(
                "Ya hay una cuenta llamada «%s». No se toca: para cambiarle la "
                "contraseña, agregue --cambiar-clave." % nombre)
            return

        clave = getpass.getpass("Contraseña para «%s»: " % nombre)
        otra_vez = getpass.getpass("Otra vez, para comprobar: ")
        if clave != otra_vez:
            self.stdout.write("No coinciden. No se hizo nada.")
            return
        if len(clave) < 8:
            self.stdout.write("Muy corta: mínimo ocho. No se hizo nada.")
            return

        if ya_estaba:
            ya_estaba.set_password(clave)
            ya_estaba.save()
            self.stdout.write("Contraseña cambiada para «%s»." % nombre)
            return

        cuenta = Cuenta.objects.create_user(username=nombre, password=clave)
        cuenta.groups.add(Group.objects.get(name=opciones["grupo"]))
        self.stdout.write(
            "Cuenta «%s» creada, en el grupo «%s»." % (nombre, opciones["grupo"]))
        if opciones["grupo"] == grupos.AGENTE:
            self.stdout.write(
                "Ese grupo NO puede aprobar, publicar versiones, derogar "
                "reglas ni administrar cuentas.")
