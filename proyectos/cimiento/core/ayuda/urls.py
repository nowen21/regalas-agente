from django.urls import path

from . import views

app_name = "ayuda"

urlpatterns = [
    path("", views.manual, name="manual"),
    path("pantalla/", views.pantalla, name="pantalla"),
    path("<slug:seccion>/", views.panel, name="panel"),
]
