# -*- coding: utf-8 -*-
"""`EP-029·HU-002` · «Revisión de pruebas»: todos los proyectos, el detalle de uno, revisar y borrar.

**El botón no espera la revisión** (acuerdo 11 del análisis 1 del pendiente
141): arranca `manage.py revisar_pruebas` en otro proceso y vuelve; la página
dice «Revisando» mientras tanto y se recarga sola.

**La contraria de revisar es borrar la revisión** (`02·F30`). Las dos las hace
solo quien administra; mirar, cualquier cuenta.
"""
import os
import subprocess
import sys

from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views import View

from core.cuentas.permisos import SoloAdministrador, es_administrador
from core.proyectos.models import Proyecto

from .lenguaje import reconocer_todos
from .models import PruebasDelProyecto, Revision, como_va


def lanzar(proyecto):
    """Arranca `revisar_pruebas` del proyecto en otro proceso, sin esperarlo."""
    manage = os.path.join(settings.BASE_DIR, "manage.py")
    banderas = subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0
    subprocess.Popen([sys.executable, manage, "revisar_pruebas", "--proyecto", str(proyecto.pk)],
                     cwd=str(settings.BASE_DIR), stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                     stderr=subprocess.DEVNULL, creationflags=banderas, close_fds=True)


def _fila(proyecto):
    # `EP-029·HU-007` · La fila muestra el programa con menos pruebas de la última vez.
    ultimas = Revision.ultimas(proyecto)
    ultima = Revision.la_de_menos_pruebas(ultimas)
    estado = PruebasDelProyecto.objects.filter(proyecto=proyecto).first()
    nombres = sorted({l.nombre for l in reconocer_todos(proyecto.ruta)})
    return {"proyecto": proyecto, "ultima": ultima, "programas": ultimas,
            "lenguaje": " y ".join(nombres) if nombres else "No reconocido",
            "como_va": como_va(ultima, proyecto.ajuste("dias_revision")),
            "revisando": bool(estado and estado.revisando_desde)}


class Lista(View):
    """Todos los proyectos registrados, uno por fila (acuerdo 5)."""

    def get(self, peticion):
        filas = [_fila(p) for p in Proyecto.objects.all()]
        return render(peticion, "pruebas/lista.html", {
            "filas": filas, "revisando": any(f["revisando"] for f in filas),
            "puede_cambiar": es_administrador(peticion.user)})


class Detalle(View):
    """Un proyecto: su última revisión, con los archivos con menos pruebas primero, y las anteriores."""

    def get(self, peticion, pk):
        proyecto = get_object_or_404(Proyecto, pk=pk)
        return render(peticion, "pruebas/detalle.html", {
            **_fila(proyecto), "revisiones": proyecto.revisiones.all()[:20],
            "puede_cambiar": es_administrador(peticion.user)})


class Revisar(SoloAdministrador, View):

    def post(self, peticion, pk):
        proyecto = get_object_or_404(Proyecto, pk=pk)
        estado = PruebasDelProyecto.de(proyecto)
        if not estado.revisando_desde:
            estado.revisando_desde = timezone.now()
            estado.save()
            lanzar(proyecto)
        messages.success(peticion, "La revisión de «%s» empezó. Puede tardar varios minutos; "
                                   "esta página se actualiza sola." % proyecto.nombre)
        return redirect(peticion.POST.get("volver") or "pruebas:lista")


class Borrar(SoloAdministrador, View):

    def post(self, peticion, pk):
        revision = get_object_or_404(Revision, pk=pk)
        proyecto = revision.proyecto
        revision.delete()
        messages.success(peticion, "Se borró la revisión de «%s»." % proyecto.nombre)
        return redirect("pruebas:detalle", pk=proyecto.pk)
