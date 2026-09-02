# -*- coding: utf-8 -*-
"""Las rutas de la plataforma.

`proyectos-lista` es `P-01` y `proyectos-uno` es `P-02`, del diseño aprobado.
`esta-viva` queda de la fase A: sirve para saber si la plataforma responde sin
depender de que haya proyectos conectados.
"""
from django.urls import path

from nucleo.almacen import views
from nucleo.aprobaciones import views as aprobaciones
from nucleo.avisos import views as avisos
from nucleo.ciclo_de_vida import views as ciclo_de_vida
from nucleo.comprobaciones import views as comprobaciones
from nucleo.importacion import views as importacion
from nucleo.memoria import views as memoria
from nucleo.proyectos import views as proyectos

urlpatterns = [
    path("", proyectos.lista, name="proyectos-lista"),
    path("conectar/", proyectos.conectar, name="proyectos-conectar"),
    path("proyecto/<str:identificador>/", proyectos.uno, name="proyectos-uno"),
    path("proyecto/<str:identificador>/traer/", importacion.traer,
         name="importacion-traer"),
    path("proyecto/<str:identificador>/reportes/", importacion.reportes,
         name="importacion-reportes"),
    path("proyecto/<str:identificador>/reportes/<str:cuando>/",
         importacion.reporte, name="importacion-reporte"),
    path("tablero/", avisos.tablero, name="avisos-tablero"),
    path("proyecto/<str:identificador>/fases/", ciclo_de_vida.fases,
         name="ciclo-fases"),
    path("proyecto/<str:identificador>/funcionalidades/",
         comprobaciones.funcionalidades, name="comprobaciones-funcionalidades"),
    path("proyecto/<str:identificador>/aprobaciones/",
         aprobaciones.aprobaciones, name="aprobaciones-lista"),
    path("proyecto/<str:identificador>/memoria/", memoria.memoria,
         name="memoria-lista"),
    path("proyecto/<str:identificador>/<str:que>/", proyectos.cambiar,
         name="proyectos-cambiar"),
    path("esta-viva/", views.esta_viva, name="esta-viva"),
]
