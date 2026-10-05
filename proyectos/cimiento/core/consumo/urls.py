"""Las rutas del gasto: la de la telemetría (`EP-025·HU-007`), la que OpenTelemetry
usa para los eventos, y las del tablero (`EP-025·HU-008`)."""
from django.urls import path

from . import views

app_name = "consumo"

urlpatterns = [
    path("v1/logs", views.RecibirEventos.as_view(), name="eventos"),
    path("gasto/", views.Tablero.as_view(), name="tablero"),
    path("gasto/datos/", views.DatosDelTablero.as_view(), name="datos"),
]
