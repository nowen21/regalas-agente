from django.urls import path

from . import views

app_name = "historia"

urlpatterns = [
    path("", views.Lista.as_view(), name="lista"),
    path("<int:pk>/deshacer/", views.Deshacer.as_view(), name="deshacer"),
    path("versiones/", views.Versiones.as_view(), name="versiones"),
]
