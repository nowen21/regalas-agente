"""`EP-027·HU-002` · Pasa las reglas del estándar a sus tablas, en una sola versión."""
import os

from django.core.management.base import BaseCommand

from core.comun import Proyecto as Carpeta
from core.estandar import cambios
from core.estandar.reglas import pasar_todo
from core.historia import versiones
from core.historia.registro import quien_y_por_que


class Command(BaseCommand):
    help = "Pasa cada regla del texto a sus tablas, mueve las notas con fecha del sello a la historia y arma el texto."

    def handle(self, *args, **opciones):
        raiz = os.path.abspath(Carpeta.estandar())
        with quien_y_por_que(quien="pasar_reglas", tipo=versiones.MENOR,
                             motivo="EP-027·HU-002: las reglas pasan a sus tablas; las notas con fecha del sello, "
                                    "a la historia"):
            total, cambiados = pasar_todo(raiz)
            cambios.rearmar_mapa(raiz)
        self.stdout.write("%d reglas en las tablas; %d documentos armados de nuevo desde ellas." % (total,
                                                                                                    len(cambiados)))
