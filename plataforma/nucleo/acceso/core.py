# -*- coding: utf-8 -*-
"""Quién entra, y qué se le responde a quien no puede — `F-036` y `F-037`.

**Una cuenta que no existe se rechaza.** Antes de esto, `aprobar --quien
"cualquier cosa"` guardaba ese texto tal cual: una aprobación decía quién la dio
y no lo probaba. Ahora el nombre tiene que ser una cuenta de la plataforma.

**Las órdenes de consola no piden contraseña**, y es una decisión, no un olvido:
quien alcanza la consola de la máquina ya tiene la máquina. Lo que sí se exige es
que la cuenta **exista** y que **tenga el permiso**.
"""
from django.contrib.auth import get_user_model

from nucleo.acceso import grupos


class NoPuede(Exception):
    """La cuenta no existe, o existe y no tiene ese permiso."""


def cuenta(nombre):
    """La cuenta con ese nombre. Levanta `NoPuede` si no existe.

    **No se crea sola.** Aceptar un nombre desconocido creando la cuenta sería
    volver a tener un campo de texto libre, con más pasos.
    """
    Cuenta = get_user_model()
    try:
        return Cuenta.objects.get(username=nombre)
    except Cuenta.DoesNotExist:
        raise NoPuede(
            "no hay ninguna cuenta llamada «%s» en la plataforma. Las cuentas "
            "se crean con `python manage.py crear_cuenta`, y el nombre que se "
            "declara tiene que ser una de ellas: si no, la constancia diría "
            "quién lo hizo sin probarlo." % nombre)


def puede(quien, clave):
    """¿Esa cuenta tiene ese permiso? El superusuario siempre puede."""
    return quien.is_superuser or quien.has_perm(grupos.con_prefijo(clave))


def exigir(nombre, clave):
    """La cuenta, si existe y tiene el permiso. Si no, `NoPuede` con el porqué.

    **El rechazo dice qué permiso falta y por qué existe.** «No autorizado»
    obliga a ir a preguntar; «falta aprobar_documento, porque aprobar es de una
    persona» se entiende sin salir de la pantalla.
    """
    quien = cuenta(nombre)
    if puede(quien, clave):
        return quien
    porque = grupos.por_que_no(clave)
    raise NoPuede(
        "la cuenta «%s» no tiene el permiso «%s»%s. Lo tiene el grupo «%s»."
        % (nombre, clave, (" — " + porque) if porque else "", grupos.USUARIO))


def como_se_llama(quien):
    """El nombre que se guarda en la constancia de una acción."""
    return getattr(quien, "username", "") or str(quien)
