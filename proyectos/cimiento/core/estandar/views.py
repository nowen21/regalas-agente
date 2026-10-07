# -*- coding: utf-8 -*-
"""`EP-026·HU-005` · Las pantallas del estándar, de la memoria y de las propuestas.

Toda cuenta mira; solo el grupo administrador cambia, quita o aprueba (RNF-01).
Cada envío que cambia algo trae las dos preguntas: el middleware fija con ellas
el tipo de la versión, y la historia guarda el cambio (HU-001, HU-002).
"""
from collections import OrderedDict

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from core.cuentas.permisos import es_administrador
from core.historia.models import ESTANDAR
from core.historia.versiones import actual
from core.proyectos.models import Proyecto

from . import cambios
from .models import PENDIENTE, Documento, Propuesta, Recuerdo


def _sin_permiso(peticion):
    return render(peticion, "cuentas/sin_permiso.html", status=403)


class Lista(View):

    def get(self, peticion):
        buscar = peticion.GET.get("q", "").strip()
        documentos = Documento.objects.only("id", "ruta", "actualizado")
        if buscar:
            documentos = documentos.filter(contenido__icontains=buscar) | Documento.objects.filter(
                ruta__icontains=buscar).only("id", "ruta", "actualizado")
        grupos = OrderedDict()
        for d in documentos.order_by("ruta"):
            partes = d.ruta.split("/")
            grupos.setdefault("/".join(partes[:2]) if len(partes) > 2 else partes[0], []).append(d)
        return render(peticion, "estandar/lista.html", {
            "grupos": grupos, "buscar": buscar, "version": actual(ESTANDAR),
            "pendientes": Propuesta.objects.filter(estado=PENDIENTE).count(),
            "proyectos": Proyecto.objects.filter(activo=True),
            "puede_cambiar": es_administrador(peticion.user)})


class VerDocumento(View):

    def get(self, peticion, pk):
        documento = get_object_or_404(Documento, pk=pk)
        return render(peticion, "estandar/documento.html", {
            "documento": documento, "puede_cambiar": es_administrador(peticion.user), "nuevo": False})

    def post(self, peticion, pk):
        if not es_administrador(peticion.user):
            return _sin_permiso(peticion)
        documento = get_object_or_404(Documento, pk=pk)
        cambios.guardar_documento(documento.ruta, peticion.POST.get("contenido", ""))
        messages.success(peticion, "Documento guardado; el estándar va en la %s." % actual(ESTANDAR))
        return redirect("estandar:documento", pk=pk)


class NuevoDocumento(View):

    def get(self, peticion):
        if not es_administrador(peticion.user):
            return _sin_permiso(peticion)
        return render(peticion, "estandar/documento.html", {"documento": None, "puede_cambiar": True, "nuevo": True})

    def post(self, peticion):
        if not es_administrador(peticion.user):
            return _sin_permiso(peticion)
        try:
            documento = cambios.guardar_documento(peticion.POST.get("ruta", ""), peticion.POST.get("contenido", ""))
        except cambios.CambioInvalido as razon:
            messages.error(peticion, "No se creó: %s." % razon)
            return redirect("estandar:nuevo")
        messages.success(peticion, "Documento creado.")
        return redirect("estandar:documento", pk=documento.pk)


class QuitarDocumento(View):

    def post(self, peticion, pk):
        if not es_administrador(peticion.user):
            return _sin_permiso(peticion)
        documento = get_object_or_404(Documento, pk=pk)
        ruta = documento.ruta
        cambios.quitar_documento(documento)
        messages.success(peticion, "Se quitó %s; queda en la historia." % ruta)
        return redirect("estandar:lista")


class Memoria(View):

    def get(self, peticion, proyecto):
        proyecto = get_object_or_404(Proyecto, pk=proyecto)
        return render(peticion, "estandar/recuerdos.html", {
            "proyecto": proyecto, "recuerdos": proyecto.recuerdos.all(),
            "version": actual("proyecto", proyecto.pk), "puede_cambiar": es_administrador(peticion.user)})


class VerRecuerdo(View):

    def get(self, peticion, proyecto, pk=None):
        proyecto = get_object_or_404(Proyecto, pk=proyecto)
        recuerdo = get_object_or_404(Recuerdo, pk=pk, proyecto=proyecto) if pk else None
        if recuerdo is None and not es_administrador(peticion.user):
            return _sin_permiso(peticion)
        return render(peticion, "estandar/recuerdo.html", {
            "proyecto": proyecto, "recuerdo": recuerdo, "puede_cambiar": es_administrador(peticion.user)})

    def post(self, peticion, proyecto, pk=None):
        if not es_administrador(peticion.user):
            return _sin_permiso(peticion)
        proyecto = get_object_or_404(Proyecto, pk=proyecto)
        if pk and peticion.POST.get("quitar"):
            get_object_or_404(Recuerdo, pk=pk, proyecto=proyecto).delete()
            messages.success(peticion, "Recuerdo quitado; queda en la historia.")
            return redirect("estandar:memoria", proyecto=proyecto.pk)
        nombre = get_object_or_404(Recuerdo, pk=pk, proyecto=proyecto).nombre if pk else peticion.POST.get("nombre", "")
        try:
            recuerdo = cambios.guardar_recuerdo(proyecto, nombre, peticion.POST.get("contenido", ""))
        except cambios.CambioInvalido as razon:
            messages.error(peticion, "No se guardó: %s." % razon)
            return redirect("estandar:memoria", proyecto=proyecto.pk)
        messages.success(peticion, "Recuerdo guardado.")
        return redirect("estandar:recuerdo", proyecto=proyecto.pk, pk=recuerdo.pk)


class Propuestas(View):

    def get(self, peticion):
        return render(peticion, "estandar/propuestas.html", {
            "pendientes": Propuesta.objects.filter(estado=PENDIENTE).select_related("proyecto"),
            "resueltas": Propuesta.objects.exclude(estado=PENDIENTE).select_related("proyecto", "resuelta_por")[:50],
            "puede_cambiar": es_administrador(peticion.user)})


class Resolver(View):
    aprobar = True

    def post(self, peticion, pk):
        if not es_administrador(peticion.user):
            return _sin_permiso(peticion)
        propuesta = get_object_or_404(Propuesta, pk=pk)
        try:
            if self.aprobar:
                cambios.aplicar(propuesta, peticion.user)
            else:
                cambios.rechazar(propuesta, peticion.user)
        except cambios.CambioInvalido as razon:
            messages.error(peticion, "No se resolvió: %s." % razon)
        else:
            messages.success(peticion, "Propuesta %d %s." % (propuesta.pk, "aprobada" if self.aprobar else "rechazada"))
        return redirect("estandar:propuestas")
