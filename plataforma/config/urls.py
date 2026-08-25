# -*- coding: utf-8 -*-
"""Las rutas de la plataforma.

`proyectos-lista` es `P-01` y `proyectos-uno` es `P-02`, del diseño aprobado.
`esta-viva` queda de la fase A: sirve para saber si la plataforma responde sin
depender de que haya proyectos conectados.
"""
from django.urls import path

from nucleo.almacen import views
from nucleo.proyectos import views as proyectos

urlpatterns = [
    path("", proyectos.lista, name="proyectos-lista"),
    path("conectar/", proyectos.conectar, name="proyectos-conectar"),
    path("proyecto/<str:identificador>/", proyectos.uno, name="proyectos-uno"),
    path("proyecto/<str:identificador>/<str:que>/", proyectos.cambiar,
         name="proyectos-cambiar"),
    path("esta-viva/", views.esta_viva, name="esta-viva"),
]
