"""Las rutas de Cimiento. Cada módulo de `core/` agrega las suyas con `include`."""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
