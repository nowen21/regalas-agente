from django.db import connection
from django.views.generic import TemplateView

from .base_de_datos import BaseDeDatos


class Inicio(TemplateView):
    """La primera página: dice a qué base está conectado Cimiento."""

    template_name = "inicio/inicio.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        # Si la base no responde, esto levanta el error y lo atiende BaseApagada.
        connection.ensure_connection()
        contexto["base"] = BaseDeDatos()
        contexto["version"] = BaseDeDatos.version(connection)
        return contexto
