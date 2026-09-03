# -*- coding: utf-8 -*-
"""Lo que una prueba de pantalla necesita para poder entrar.

**Vive acá y no repetido en cada archivo de pruebas.** Cuando los permisos
cambien —y van a cambiar—, esto se toca en un lugar. Cinco copias de lo mismo se
convierten en cinco cosas distintas sin que nadie lo decida.

**Y no le regala permisos a nadie.** `como_usuario` crea una cuenta del grupo
`usuario` y `como_agente` una del grupo `agente`, con los permisos de verdad: una
prueba que entra con superusuario no comprueba nada sobre permisos.
"""
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from nucleo.acceso import grupos

CLAVE = "de-prueba-no-sirve-afuera"


def _cuenta(nombre, grupo):
    grupos.poner_al_dia()
    Cuenta = get_user_model()
    cuenta = Cuenta.objects.create_user(username=nombre, password=CLAVE)
    cuenta.groups.add(Group.objects.get(name=grupo))
    return cuenta


def como_usuario(cliente, nombre="quien-manda"):
    """Entra con una cuenta del grupo `usuario`. Devuelve la cuenta."""
    cuenta = _cuenta(nombre, grupos.USUARIO)
    cliente.force_login(cuenta)
    return cuenta


def como_agente(cliente, nombre="el-agente"):
    """Entra con una cuenta del grupo `agente`. Devuelve la cuenta."""
    cuenta = _cuenta(nombre, grupos.AGENTE)
    cliente.force_login(cuenta)
    return cuenta
