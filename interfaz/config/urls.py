from django.urls import path
from cimiento.proyectos import views as proyectos_views
from cimiento.visor import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doc/', views.doc, name='doc'),
    path('panel/', views.panel, name='panel'),
    path('memoria/', views.memoria, name='memoria'),
    path('memoria/senal/', views.senal_detalle, name='senal_detalle'),
    path('memoria/crear/', views.crear_senal, name='crear_senal'),
    path('memoria/export/', views.export_senales, name='export_senales'),
    path('proyectos/', proyectos_views.lista, name='proyectos'),
    path('proyectos/nuevo/', proyectos_views.editar, name='proyecto_nuevo'),
    path('proyectos/<int:pk>/editar/', proyectos_views.editar, name='proyecto_editar'),
    path('proyectos/<int:pk>/baja/', proyectos_views.baja, name='proyecto_baja'),
    path('proyectos/<int:pk>/medir/', proyectos_views.medir, name='proyecto_medir'),
    path('proyectos/importar/', proyectos_views.importar, name='proyectos_importar'),
    path('proyectos/exportar/', proyectos_views.exportar, name='proyectos_exportar'),
]
