# -*- coding: utf-8 -*-
"""Los niveles de las reglas de un proyecto, y su historial.

**Todo o nada.** El formulario trae todas las reglas; se guardan las que
cambiaron, en una transacción. Si el envío trae una regla fuera del catálogo
(del núcleo, inventada) o un nivel que no existe, no se guarda ninguna.
"""
from itertools import groupby

from django.contrib import messages
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from core.cuentas.permisos import es_administrador
from core.proyectos.models import Proyecto

from .catalogo import ids_configurables, reglas_configurables
from .models import FRENA, NIVELES, CambioDeNivel, NivelDeRegla

PREFIJO = "nivel-"


class Reglas(View):

    def get(self, peticion, pk):
        proyecto = get_object_or_404(Proyecto, pk=pk)
        guardados = dict(proyecto.niveles.values_list("regla", "nivel"))
        filas = [(regla, guardados.get(regla.id, FRENA)) for regla in reglas_configurables()]
        capitulos = [(capitulo, list(grupo)) for capitulo, grupo
                     in groupby(filas, key=lambda fila: fila[0].capitulo)]
        return render(peticion, "niveles/reglas.html", {
            "proyecto": proyecto, "capitulos": capitulos, "niveles": NIVELES,
            "puede_cambiar": es_administrador(peticion.user)})

    def post(self, peticion, pk):
        if not es_administrador(peticion.user):
            return render(peticion, "cuentas/sin_permiso.html", status=403)
        proyecto = get_object_or_404(Proyecto, pk=pk)
        enviados = {clave[len(PREFIJO):]: valor for clave, valor in peticion.POST.items()
                    if clave.startswith(PREFIJO)}

        validos = {codigo for codigo, _ in NIVELES}
        fuera = sorted(set(enviados) - ids_configurables())
        malos = sorted(regla for regla, nivel in enviados.items() if nivel not in validos)
        if fuera or malos:
            if fuera:
                messages.error(peticion, f"Estas reglas no se pueden cambiar: {', '.join(fuera)}. No se guardó nada.")
            if malos:
                messages.error(peticion, f"Nivel que no existe en: {', '.join(malos)}. No se guardó nada.")
            return redirect("niveles:reglas", pk=pk)

        guardados = dict(proyecto.niveles.values_list("regla", "nivel"))
        cambios = 0
        with transaction.atomic():
            for regla, nuevo in enviados.items():
                anterior = guardados.get(regla, FRENA)
                if nuevo == anterior:
                    continue
                NivelDeRegla.objects.update_or_create(proyecto=proyecto, regla=regla,
                                                      defaults={"nivel": nuevo})
                CambioDeNivel.objects.create(proyecto=proyecto, regla=regla, anterior=anterior,
                                             nuevo=nuevo, cuenta=peticion.user)
                cambios += 1
        messages.success(peticion, f"{cambios} nivel(es) cambiado(s)." if cambios else "No había cambios.")
        return redirect("niveles:reglas", pk=pk)


class Historial(View):

    def get(self, peticion, pk):
        proyecto = get_object_or_404(Proyecto, pk=pk)
        return render(peticion, "niveles/historial.html", {
            "proyecto": proyecto,
            "cambios": proyecto.cambios_de_nivel.select_related("cuenta")})
