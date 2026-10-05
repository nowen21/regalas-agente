from django.contrib.auth import views
from django.urls import path

app_name = "cuentas"

urlpatterns = [
    path("entrar/", views.LoginView.as_view(template_name="cuentas/entrar.html"), name="entrar"),
    path("salir/", views.LogoutView.as_view(), name="salir"),
]
