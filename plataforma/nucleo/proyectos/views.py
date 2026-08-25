# -*- coding: utf-8 -*-
"""Las dos primeras pantallas: la lista de proyectos, y uno solo.

Son `P-01` y `P-02` del diseño aprobado, en su forma mínima: muestran y dejan
conectar. Lo demás que esas pantallas prometen -entrar a un documento, abrir
una fase, pedir el expediente- llega en las versiones siguientes.

**Una lista vacía dice que está vacía.** Una pantalla en blanco se lee como un
error de la plataforma, y no lo es.
"""
from django.shortcuts import get_object_or_404, redirect, render

from . import core
from .models import Proyecto


def lista(request):
    """`P-01` · todos los proyectos, y desde acá se conecta uno nuevo."""
    return render(request, "proyectos/lista.html", {
        "proyectos": Proyecto.objects.all(),
    })


def conectar(request):
    """Recibe el nombre y la ruta. Rechaza o conecta, y dice cuál de las dos."""
    if request.method != "POST":
        return redirect("proyectos-lista")

    nombre = (request.POST.get("nombre") or "").strip()
    ruta = (request.POST.get("ruta") or "").strip()
    if not nombre or not ruta:
        return render(request, "proyectos/lista.html", {
            "proyectos": Proyecto.objects.all(),
            "error": "Hacen falta el nombre y la ruta.",
            "nombre": nombre, "ruta": ruta,
        })

    try:
        proyecto, avisos = core.conectar(
            nombre, ruta, quien="el usuario",
            sesion=(request.POST.get("sesion") or "").strip())
    except (core.RutaQueNoExiste, core.RutaYaRegistrada,
            core.VersionQueNoExiste) as rechazo:
        return render(request, "proyectos/lista.html", {
            "proyectos": Proyecto.objects.all(),
            "error": str(rechazo),
            "nombre": nombre, "ruta": ruta,
        })

    return render(request, "proyectos/uno.html", {
        "proyecto": proyecto,
        "avisos": avisos,
        "recien_conectado": True,
    })


def uno(request, identificador):
    """`P-02` · un proyecto: su ruta, su versión y qué le falta."""
    proyecto = get_object_or_404(Proyecto, identificador=identificador)
    return render(request, "proyectos/uno.html", {
        "proyecto": proyecto,
        "avisos": core.avisos_de(proyecto.ruta_codigo, proyecto.version_reglas)
        if proyecto.ruta_viva else [
            "La ruta de este proyecto ya no existe. Su documentación sigue acá."],
    })
