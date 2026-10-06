from django.urls import path

from . import views

app_name = "proyectos"

urlpatterns = [
    path("", views.Lista.as_view(), name="lista"),
    path("registrar/", views.Registrar.as_view(), name="registrar"),
    path("configuracion/", views.Configuracion.as_view(), name="configuracion"),
    path("<int:pk>/editar/", views.Editar.as_view(), name="editar"),
    path("<int:pk>/suspensiones/", views.Suspensiones.as_view(), name="suspensiones"),
    path("<int:pk>/suspensiones/<int:suspension>/levantar/", views.Levantar.as_view(), name="levantar"),
]
