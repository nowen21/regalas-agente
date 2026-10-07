# -*- coding: utf-8 -*-
"""`EP-026·HU-001` · La pantalla «Historia»: qué cambió, quién, cuándo y por qué.

Toda cuenta que entró la ve; solo el grupo administrador deshace (RNF-01).
"""
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from core.cuentas.permisos import es_administrador

from .models import ACCIONES, ESTANDAR, Cambio, Version
from .versiones import actual
from .registro import NoSeDeshace, deshacer

POR_PAGINA = 50


class Lista(View):

    def get(self, peticion):
        cambios = Cambio.objects.select_related("cuenta", "deshace")
        tabla = peticion.GET.get("tabla", "").strip()
        accion = peticion.GET.get("accion", "").strip()
        if tabla:
            cambios = cambios.filter(tabla=tabla)
        if accion:
            cambios = cambios.filter(accion=accion)
        pagina = Paginator(cambios, POR_PAGINA).get_page(peticion.GET.get("pagina"))
        return render(peticion, "historia/lista.html", {
            "pagina": pagina, "tabla": tabla, "accion": accion, "acciones": ACCIONES,
            "tablas": Cambio.objects.order_by("tabla").values_list("tabla", flat=True).distinct(),
            "puede_deshacer": es_administrador(peticion.user)})


class Deshacer(View):

    def post(self, peticion, pk):
        if not es_administrador(peticion.user):
            return render(peticion, "cuentas/sin_permiso.html", status=403)
        cambio = get_object_or_404(Cambio, pk=pk)
        try:
            deshacer(cambio, peticion.user, peticion.POST.get("motivo", ""))
        except NoSeDeshace as razon:
            messages.error(peticion, "No se deshizo: %s." % razon)
        else:
            messages.success(peticion, "Cambio %d deshecho." % cambio.pk)
        return redirect("historia:lista")


class Versiones(View):
    """`EP-026·HU-002` · Las versiones del estándar y de cada proyecto, con sus cambios."""

    def get(self, peticion):
        versiones = Version.objects.select_related("proyecto", "cuenta").prefetch_related("cambios")
        proyecto = peticion.GET.get("proyecto", "").strip()
        if proyecto == ESTANDAR:
            versiones = versiones.filter(ambito=ESTANDAR)
        elif proyecto.isdigit():
            versiones = versiones.filter(proyecto_id=int(proyecto))
        pagina = Paginator(versiones, POR_PAGINA).get_page(peticion.GET.get("pagina"))
        return render(peticion, "historia/versiones.html", {
            "pagina": pagina, "proyecto": proyecto, "estandar": actual(ESTANDAR)})
