# -*- coding: utf-8 -*-
"""Las pantallas del registro: listar, registrar, editar, dar de baja y medir."""
import os

from django.shortcuts import get_object_or_404, redirect, render

from cimiento.visor.core import md_to_html

from . import core
from .forms import ProyectoForm
from .models import Proyecto


def _exportar_o_avisar(mensaje_ok):
    """Exporta el .md; si el registro quedó vacío y el archivo tenía filas, avisa en vez de borrar."""
    try:
        core.exportar()
        return mensaje_ok
    except core.RegistroVacio as e:
        return f"Guardado. El .md no se regeneró: {e}"


def lista(request):
    proyectos = list(Proyecto.objects.all())
    for p in proyectos:
        p.ruta_existe = os.path.isdir(p.ruta)
    return render(request, "proyectos/lista.html", {
        "proyectos": proyectos,
        "titulo": "Proyectos",
        "mensaje": request.GET.get("m", ""),
    })


def editar(request, pk=None):
    proyecto = get_object_or_404(Proyecto, pk=pk) if pk else None
    form = ProyectoForm(request.POST or None, instance=proyecto)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("/proyectos/?m=" + _exportar_o_avisar("Guardado y exportado al registro .md"))
    return render(request, "proyectos/editar.html", {
        "form": form, "proyecto": proyecto,
        "titulo": "Editar proyecto" if proyecto else "Registrar proyecto",
    })


def baja(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == "POST":
        proyecto.activo = not proyecto.activo
        proyecto.save()
        return redirect("/proyectos/?m=" + _exportar_o_avisar("Estado cambiado y registro .md regenerado"))
    return redirect("/proyectos/")


def importar(request):
    if request.method == "POST":
        nuevas = core.importar()
        return redirect(f"/proyectos/?m=Importados {nuevas} proyecto(s) del .md")
    return redirect("/proyectos/")


def exportar(request):
    if request.method == "POST":
        try:
            filas = core.exportar()
        except core.RegistroVacio as e:
            return redirect(f"/proyectos/?m=No se exportó: {e}")
        return redirect(f"/proyectos/?m=Registro .md regenerado con {filas} activo(s)")
    return redirect("/proyectos/")


def medir(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    existe, lineas = core.medir(proyecto)
    return render(request, "proyectos/medir.html", {
        "proyecto": proyecto,
        "existe": existe,
        "reporte": md_to_html("\n".join(lineas)),
        "titulo": f"Expediente · {proyecto.nombre}",
    })
