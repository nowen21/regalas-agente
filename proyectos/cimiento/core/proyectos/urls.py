from django.urls import path

from . import views

app_name = "proyectos"

urlpatterns = [
    path("", views.Lista.as_view(), name="lista"),
    path("registrar/", views.Registrar.as_view(), name="registrar"),
    path("<int:pk>/editar/", views.Editar.as_view(), name="editar"),
]
