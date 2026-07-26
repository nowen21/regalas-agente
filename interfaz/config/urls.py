from django.urls import path
from visor import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doc/', views.doc, name='doc'),
    path('panel/', views.panel, name='panel'),
    path('memoria/', views.memoria, name='memoria'),
    path('memoria/senal/', views.senal_detalle, name='senal_detalle'),
    path('memoria/crear/', views.crear_senal, name='crear_senal'),
]
