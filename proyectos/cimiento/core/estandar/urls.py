from django.urls import path

from . import views

app_name = "estandar"

urlpatterns = [
    path("", views.Lista.as_view(), name="lista"),
    path("nuevo/", views.NuevoDocumento.as_view(), name="nuevo"),
    path("documento/<int:pk>/", views.VerDocumento.as_view(), name="documento"),
    path("documento/<int:pk>/quitar/", views.QuitarDocumento.as_view(), name="quitar"),
    path("memoria/<int:proyecto>/", views.Memoria.as_view(), name="memoria"),
    path("memoria/<int:proyecto>/nuevo/", views.VerRecuerdo.as_view(), name="recuerdo_nuevo"),
    path("memoria/<int:proyecto>/<int:pk>/", views.VerRecuerdo.as_view(), name="recuerdo"),
    path("propuestas/", views.Propuestas.as_view(), name="propuestas"),
    path("git/", views.SubirAGit.as_view(), name="git"),
    path("vista-previa/", views.VistaPrevia.as_view(), name="vista_previa"),
    path("reportes/", views.Reportes.as_view(), name="reportes"),
    path("reportes/<int:pk>/resolver/", views.ResolverReporte.as_view(), name="resolver_reporte"),
    path("propuestas/<int:pk>/aprobar/", views.Resolver.as_view(aprobar=True), name="aprobar"),
    path("propuestas/<int:pk>/rechazar/", views.Resolver.as_view(aprobar=False), name="rechazar"),
]
