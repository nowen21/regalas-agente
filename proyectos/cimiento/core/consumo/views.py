# -*- coding: utf-8 -*-
"""Las rutas del gasto de tokens: la telemetría y el tablero.

`EP-025·HU-007` · La ruta donde Claude Code manda su telemetría.

**Sin cuenta, pero solo desde esta máquina.** Claude Code no tiene cuenta en
Cimiento ni manda la cookie de CSRF, porque no es un navegador. Por eso la
ruta solo acepta envíos de `127.0.0.1` o `::1`: todo corre en una sola
máquina (análisis 1 del pendiente 119, acuerdo 9).

**Responde `{}` aunque descarte un evento.** Un error haría que Claude Code
reintente lo que nunca va a entrar.
"""
import gzip

from django.contrib.auth.decorators import login_not_required
from django.http import HttpResponseBadRequest, HttpResponseForbidden, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from core.proyectos.models import Proyecto

from .guardar import GuardadoDeTelemetria, leer_lo_nuevo
from .tablero import PERIODO_POR_DEFECTO, PERIODOS, GastoDelPeriodo
from .telemetria import EnvioInvalido, EventosDeTelemetria

LOCALES = {"127.0.0.1", "::1"}


@method_decorator([csrf_exempt, login_not_required], name="dispatch")
class RecibirEventos(View):
    http_method_names = ["post"]

    def post(self, request):
        if request.META.get("REMOTE_ADDR") not in LOCALES:
            return HttpResponseForbidden("Solo se reciben envíos de esta máquina.")
        cuerpo = request.body
        try:
            if request.headers.get("Content-Encoding", "").lower() == "gzip":
                cuerpo = gzip.decompress(cuerpo)
            eventos = EventosDeTelemetria(cuerpo)
            llamadas, archivos = eventos.leer()
        except (EnvioInvalido, OSError, EOFError):
            return HttpResponseBadRequest("El envío no es OTLP en JSON.")
        GuardadoDeTelemetria().guardar(llamadas, archivos, eventos.herramientas())
        return JsonResponse({})


class DatosDelTablero(TemplateView):
    """`EP-025·HU-008` · La parte del tablero que htmx pide cada 10 segundos.

    Solo consulta la base: lo vivo llega por telemetría. Un proyecto o un
    período que no existe se ignora.
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
    """`EP-025·HU-008` · La página entera. Al abrirla lee lo nuevo de los `.jsonl`."""

    template_name = "consumo/tablero.html"

    def get(self, request, *args, **kwargs):
        leer_lo_nuevo()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["todos_los_proyectos"] = Proyecto.objects.filter(activo=True)
        return contexto
