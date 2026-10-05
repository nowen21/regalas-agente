from django.urls import path

from . import views

app_name = "niveles"

urlpatterns = [
    path("<int:pk>/reglas/", views.Reglas.as_view(), name="reglas"),
    path("<int:pk>/reglas/historial/", views.Historial.as_view(), name="historial"),
]
