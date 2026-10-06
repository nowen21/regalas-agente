"""Las rutas del tablero del gasto (`EP-025·HU-008`). La de la telemetría salió con la
HU-012: el gasto llega por el `.jsonl`, que guarda el vigilante (`EP-025·HU-011`)."""
from django.urls import path

from . import views

app_name = "consumo"

urlpatterns = [
    path("gasto/", views.Tablero.as_view(), name="tablero"),
    path("gasto/datos/", views.DatosDelTablero.as_view(), name="datos"),
]
