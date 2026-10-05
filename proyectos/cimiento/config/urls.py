"""Las rutas de Cimiento. Cada módulo de `core/` agrega las suyas con `include`."""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.cuentas.urls")),
    path("", include("core.inicio.urls")),
    path("proyectos/", include("core.proyectos.urls")),
    path("proyectos/", include("core.niveles.urls")),
    path("", include("core.consumo.urls")),
]
