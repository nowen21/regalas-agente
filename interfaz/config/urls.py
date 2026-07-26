from django.urls import path
from visor import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doc/', views.doc, name='doc'),
    path('memoria/', views.memoria, name='memoria'),
]
