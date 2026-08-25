# -*- coding: utf-8 -*-
"""Las rutas de la plataforma. En la fase A solo hay una: decir que está viva."""
from django.urls import path

from nucleo.almacen import views

urlpatterns = [
    path("", views.esta_viva, name="esta-viva"),
]
