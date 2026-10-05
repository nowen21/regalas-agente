# -*- coding: utf-8 -*-
"""Cualquier pantalla que no alcance la base dice qué hacer, en vez de una traza.

Va en el middleware y no en cada vista: las pantallas que lleguen después lo
heredan sin escribir nada. Responde 503, que es «el servicio no está», no 500,
que es «el programa falló».

**Se revisa antes que la entrada** (`EP-025·HU-002`). Saber si alguien entró
ya lee la sesión de la base, y el error de ese momento no llega a
`process_exception`: Django lo convierte en una página 500. Por eso
`process_view` prueba la conexión primero, y la página de base apagada se ve
sin haber entrado.
"""
from django.db import OperationalError, connection
from django.shortcuts import render

from .base_de_datos import BaseDeDatos


class BaseApagada:

    def __init__(self, siguiente):
        self.siguiente = siguiente

    def __call__(self, peticion):
        return self.siguiente(peticion)

    @staticmethod
    def responder(peticion, error):
        base = BaseDeDatos()
        return render(peticion, "inicio/base_apagada.html",
                      {"mensaje": base.explicar(error), "base": base}, status=503)

    def process_view(self, peticion, vista, args, kwargs):
        try:
            connection.ensure_connection()
        except OperationalError as error:
            return self.responder(peticion, error)
        return None

    def process_exception(self, peticion, error):
        if not isinstance(error, OperationalError):
            return None
        return self.responder(peticion, error)
