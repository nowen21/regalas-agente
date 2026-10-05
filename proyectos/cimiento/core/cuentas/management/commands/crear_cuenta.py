# -*- coding: utf-8 -*-
"""Crea una cuenta de Cimiento en uno de sus dos grupos.

    python manage.py crear_cuenta --usuario ana --grupo consulta

**La contraseña se pide, no se pasa.** Escrita en la orden quedaría en el
historial de la consola (`00·N6`). Se pide dos veces sin mostrarse, y la
revisan los mismos validadores que usa Django para cualquier contraseña.
"""
import getpass

from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from core.comun.consola import preparar_salida
from core.cuentas.permisos import GRUPOS


class Command(BaseCommand):
    help = "Crea una cuenta en el grupo administrador o en el grupo consulta."

    def add_arguments(self, parser):
        parser.add_argument("--usuario", required=True)
        parser.add_argument("--grupo", required=True, help=" o ".join(GRUPOS))

    def pedir_clave(self):
        """Aparte para que las pruebas la sustituyan."""
        return getpass.getpass("Contraseña: "), getpass.getpass("Otra vez: ")

    def handle(self, *args, usuario, grupo, **opciones):
        preparar_salida()
        if grupo not in GRUPOS:
            raise CommandError(f"El grupo «{grupo}» no existe. Los que valen: {', '.join(GRUPOS)}.")
        Cuenta = get_user_model()
        if Cuenta.objects.filter(username=usuario).exists():
            raise CommandError(f"La cuenta «{usuario}» ya existe; no se cambió.")

        clave, otra = self.pedir_clave()
        if clave != otra:
            raise CommandError("Las dos contraseñas no coinciden; no se creó la cuenta.")
        try:
            password_validation.validate_password(clave, Cuenta(username=usuario))
        except ValidationError as error:
            raise CommandError(" ".join(error.messages))

        with transaction.atomic():
            cuenta = Cuenta.objects.create_user(username=usuario, password=clave)
            cuenta.groups.add(Group.objects.get(name=grupo))
        self.stdout.write(f"La cuenta «{usuario}» quedó en el grupo {grupo}.")
