"""Las rutas del tablero del gasto (`EP-025·HU-008`; en partes desde la `HU-026`; en vivo desde la `HU-027`)."""
from django.urls import path

from . import views

app_name = "consumo"

urlpatterns = [
    path("gasto/", views.Tablero.as_view(), name="tablero"),
    path("gasto/franja/", views.Franja.as_view(), name="franja"),
    path("gasto/pestana/<slug:nombre>/", views.Pestana.as_view(), name="pestana"),
    path("gasto/aviso/", views.aviso, name="aviso"),
    path("gasto/eventos/", views.flujo_de_eventos, name="eventos"),
]
