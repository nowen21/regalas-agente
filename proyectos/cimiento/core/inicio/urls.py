from django.urls import path

from .views import Inicio

app_name = "inicio"

urlpatterns = [
    path("", Inicio.as_view(), name="inicio"),
]
