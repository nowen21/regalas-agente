from django.urls import path

from . import views

app_name = "pruebas"

urlpatterns = [
    path("", views.Lista.as_view(), name="lista"),
    path("<int:pk>/", views.Detalle.as_view(), name="detalle"),
    path("<int:pk>/revisar/", views.Revisar.as_view(), name="revisar"),
    path("revision/<int:pk>/borrar/", views.Borrar.as_view(), name="borrar"),
]
