# -*- coding: utf-8 -*-
"""Quién puede cambiar algo en Cimiento.

**El grupo consulta solo mira.** Lo que cambia niveles, límites o proyectos lo
hace el grupo administrador, o un superusuario, que es como nace la primera
cuenta (`createsuperuser` no le pone grupo).

**Sin permiso es 403, no la entrada.** La cuenta ya entró; mandarla a entrar
otra vez no le dice qué pasa. La página no muestra nada de lo que protege.
"""
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render

ADMINISTRADOR = "administrador"
CONSULTA = "consulta"
GRUPOS = (ADMINISTRADOR, CONSULTA)


def es_administrador(cuenta):
    if not cuenta.is_authenticated:
        return False
    return cuenta.is_superuser or cuenta.groups.filter(name=ADMINISTRADOR).exists()


class SoloAdministrador(UserPassesTestMixin):
    """Para las vistas que cambian algo: el grupo consulta recibe 403."""

    def test_func(self):
        return es_administrador(self.request.user)

    def handle_no_permission(self):
        return render(self.request, "cuentas/sin_permiso.html", status=403)
