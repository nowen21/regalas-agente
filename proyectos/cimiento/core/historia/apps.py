from django.apps import AppConfig


class HistoriaConfig(AppConfig):
    name = "core.historia"
    label = "historia"
    verbose_name = "Historia de los cambios"

    def ready(self):
        from . import registro

        registro.conectar()
