# -*- coding: utf-8 -*-
"""El tablero del gasto de tokens (`EP-025·HU-008`, rehecho en la `HU-026`).

Solo consulta la base: lo nuevo de los `.jsonl` lo guarda el vigilante
(`EP-025·HU-011`). **La pantalla va en partes** (`EP-025·HU-026`): la franja de
arriba y cada pestaña tienen su ruta, y htmx pide solo la que se ve. Nada se pide
cada cierto tiempo (análisis 1 del pendiente 124, acuerdo 4): se actualiza con el
botón y con cada aviso del vigilante, que llega por SSE (`EP-025·HU-027`).
"""
from django.contrib.auth.decorators import login_not_required
from django.http import Http404, HttpResponse, HttpResponseForbidden, StreamingHttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from django.views.generic import TemplateView

from core.proyectos.models import Proyecto

from .avisos import Avisos, eventos
from .tablero import PERIODO_POR_DEFECTO, PERIODOS, GastoDelPeriodo

LOCALES = {"127.0.0.1", "::1"}


class ConFiltros(TemplateView):
    """Lee el proyecto y el período de la dirección; lo que no existe se ignora."""

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
        self.gasto = self.filtros()
        consulta = "dias=%d" % self.gasto.dias + ("&proyecto=%d" % self.gasto.proyecto.pk if self.gasto.proyecto else "")
        contexto.update({"dias": self.gasto.dias, "proyecto": self.gasto.proyecto, "periodos": PERIODOS,
                         "consulta": consulta, "actualizado": timezone.localtime()})
        return contexto


class Franja(ConFiltros):
    """La franja de arriba: total, variación, llamadas, % de caché releída y contexto máximo."""

    template_name = "consumo/_franja.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["franja"] = self.gasto.franja()
        return contexto


class Pestana(ConFiltros):
    """Una de las cinco pestañas. Un nombre que no existe da 404."""

    def get_template_names(self):
        return ["consumo/_%s.html" % self.kwargs["nombre"]]

    def get_context_data(self, **kwargs):
        if self.kwargs["nombre"] not in GastoDelPeriodo.PESTANAS:
            raise Http404("no hay esa pestaña")
        contexto = super().get_context_data(**kwargs)
        contexto.update(self.gasto.pestana(self.kwargs["nombre"], self.request.GET.get("agrupar", "proyecto")))
        return contexto


class Tablero(ConFiltros):
    """La página: filtros, franja y la barra de pestañas; la pestaña abierta se recuerda en `?pestana=`."""

    template_name = "consumo/tablero.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        pestana = self.request.GET.get("pestana", "resumen")
        contexto.update({
            "todos_los_proyectos": Proyecto.objects.filter(activo=True),
            "pestana": pestana if pestana in GastoDelPeriodo.PESTANAS else "resumen",
            "pestanas": [("resumen", "Resumen"), ("donde", "Dónde se gasta"), ("contexto", "Contexto"),
                         ("ahorro", "Ahorro"), ("actividad", "Actividad")],
            "franja": self.gasto.franja(),
        })
        return contexto


# ── `EP-025·HU-027` · La pantalla se entera en el momento ─────────────────

@login_not_required
@csrf_exempt
@require_POST
def aviso(peticion):
    """Lo llama el vigilante al guardar algo nuevo. Solo desde la misma máquina."""
    if peticion.META.get("REMOTE_ADDR") not in LOCALES:
        return HttpResponseForbidden("el aviso solo se acepta desde esta máquina")
    Avisos.avisar()
    return HttpResponse(status=204)


@require_GET
def flujo_de_eventos(peticion):
    """SSE: un evento `gasto` por cada aviso, para la pantalla abierta."""
    respuesta = StreamingHttpResponse(eventos(), content_type="text/event-stream")
    respuesta["Cache-Control"] = "no-cache"
    respuesta["X-Accel-Buffering"] = "no"
    return respuesta

