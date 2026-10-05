from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from core.cuentas.permisos import SoloAdministrador, es_administrador

from .forms import ProyectoForm
from .models import Proyecto


class Lista(ListView):
    """La ve cualquier cuenta; los botones de cambiar, solo el administrador."""

    model = Proyecto
    template_name = "proyectos/lista.html"
    context_object_name = "proyectos"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["puede_cambiar"] = es_administrador(self.request.user)
        return contexto


class Registrar(SoloAdministrador, CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = "proyectos/formulario.html"
    success_url = reverse_lazy("proyectos:lista")
    extra_context = {"titulo": "Registrar un proyecto"}


class Editar(SoloAdministrador, UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = "proyectos/formulario.html"
    success_url = reverse_lazy("proyectos:lista")
    extra_context = {"titulo": "Editar el proyecto"}
