"""Las pantallas de «Proyectos» y «Configuración».

`EP-025·HU-013` · Los ajustes van en tres capas: la base de Cimiento en
«Configuración», los del proyecto en su formulario, y las suspensiones en la
pantalla de cada proyecto. Las ve cualquier cuenta; las cambia el administrador.
Cada cambio vuelve a escribir la copia `.agente/configuracion.md`.
"""
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView

from core.cuentas.permisos import SoloAdministrador, es_administrador

from . import ajustes as catalogo
from . import copia
from .forms import ConfiguracionForm, ProyectoForm, SuspensionForm
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


class ConCopia:
    """Después de guardar el proyecto y sus ajustes, su copia."""

    def form_valid(self, form):
        respuesta = super().form_valid(form)
        copia.escribir(self.object)
        return respuesta


class Registrar(SoloAdministrador, ConCopia, CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = "proyectos/formulario.html"
    success_url = reverse_lazy("proyectos:lista")
    extra_context = {"titulo": "Registrar un proyecto"}


class Editar(SoloAdministrador, ConCopia, UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = "proyectos/formulario.html"
    success_url = reverse_lazy("proyectos:lista")
    extra_context = {"titulo": "Editar el proyecto"}


class Configuracion(View):
    """Capa 1: el valor común de cada ajuste."""

    def get(self, peticion):
        return render(peticion, "proyectos/configuracion.html", {
            "form": ConfiguracionForm(), "puede_cambiar": es_administrador(peticion.user)})

    def post(self, peticion):
        if not es_administrador(peticion.user):
            return render(peticion, "cuentas/sin_permiso.html", status=403)
        form = ConfiguracionForm(peticion.POST)
        if not form.is_valid():
            return render(peticion, "proyectos/configuracion.html", {"form": form, "puede_cambiar": True})
        form.guardar()
        escritas = copia.escribir_todas()
        messages.success(peticion, "Configuración guardada; %d copia(s) de proyectos al día." % len(escritas))
        return redirect("proyectos:configuracion")


class Suspensiones(View):
    """Capa 3: lo suspendido de un proyecto, y suspender."""

    def contexto(self, peticion, proyecto, form):
        return {"proyecto": proyecto, "form": form, "puede_cambiar": es_administrador(peticion.user),
                "suspensiones": proyecto.suspensiones.select_related("creada_por", "levantada_por"),
                "ahora": timezone.now(), "dias": catalogo.DIAS_MAXIMOS}

    def get(self, peticion, pk):
        proyecto = get_object_or_404(Proyecto, pk=pk)
        return render(peticion, "proyectos/suspensiones.html", self.contexto(peticion, proyecto, SuspensionForm()))

    def post(self, peticion, pk):
        if not es_administrador(peticion.user):
            return render(peticion, "cuentas/sin_permiso.html", status=403)
        proyecto = get_object_or_404(Proyecto, pk=pk)
        form = SuspensionForm(peticion.POST)
        if not form.is_valid():
            return render(peticion, "proyectos/suspensiones.html", self.contexto(peticion, proyecto, form))
        suspension = form.save(commit=False)
        suspension.proyecto, suspension.creada_por = proyecto, peticion.user
        suspension.save()
        copia.escribir(proyecto)
        messages.success(peticion, "Suspendido hasta el %s." % timezone.localtime(suspension.vence).strftime("%Y-%m-%d %H:%M"))
        return redirect("proyectos:suspensiones", pk=pk)


class Levantar(View):
    """La contraria de suspender (`02·F30`): la suspensión deja de valer y queda quién la levantó."""

    def post(self, peticion, pk, suspension):
        if not es_administrador(peticion.user):
            return render(peticion, "cuentas/sin_permiso.html", status=403)
        proyecto = get_object_or_404(Proyecto, pk=pk)
        objetivo = get_object_or_404(proyecto.suspensiones, pk=suspension)
        if objetivo.levantada is None:
            objetivo.levantada, objetivo.levantada_por = timezone.now(), peticion.user
            objetivo.save(update_fields=["levantada", "levantada_por"])
            copia.escribir(proyecto)
            messages.success(peticion, "Suspensión levantada.")
        return redirect("proyectos:suspensiones", pk=pk)
