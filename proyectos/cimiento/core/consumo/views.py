# -*- coding: utf-8 -*-
"""El tablero del gasto de tokens (`EP-025·HU-008`).

Solo consulta la base: lo nuevo de los `.jsonl` lo guarda el vigilante
(`EP-025·HU-011`). La ruta de la telemetría salió con la HU-012.
"""
from django.views.generic import TemplateView

from core.proyectos.models import Proyecto

from .tablero import PERIODO_POR_DEFECTO, PERIODOS, GastoDelPeriodo


class DatosDelTablero(TemplateView):
    """`EP-025·HU-008` · La parte del tablero que htmx pide cada 10 segundos.

    Solo consulta la base: lo vivo lo guarda el vigilante (`EP-025·HU-011`).
    Un proyecto o un período que no existe se ignora.
    """

    template_name = "consumo/_datos.html"

    def filtros(self):
        try:
            dias = int(self.request.GET.get("dias", PERIODO_POR_DEFECTO))
        except ValueError:
            dias = PERIODO_POR_DEFECTO
        proyecto = None
        if self.request.GET.get("proyecto", "").isdigit():
            proyecto = Proyecto.objects.filter(pk=int(self.request.GET["proyecto"])).first()
        return GastoDelPeriodo(dias, proyecto)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        gasto = self.filtros()
        contexto.update(gasto.todo())
        contexto.update({"dias": gasto.dias, "proyecto": gasto.proyecto, "periodos": PERIODOS})
        return contexto


class Tablero(DatosDelTablero):
    """`EP-025·HU-008` · La página entera. Solo consulta la base: lo nuevo de los
    `.jsonl` lo guarda el vigilante en cuanto se escribe (`EP-025·HU-011`)."""

    template_name = "consumo/tablero.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["todos_los_proyectos"] = Proyecto.objects.filter(activo=True)
        return contexto
