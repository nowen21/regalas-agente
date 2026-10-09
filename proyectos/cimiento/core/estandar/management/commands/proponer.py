"""`EP-026·HU-005` · El agente propone un cambio del estándar o de la memoria; se aprueba en la pantalla.

    manage.py proponer --ruta base/x.md --archivo texto-nuevo.md --motivo "…"
    manage.py proponer --ruta base/x.md --quitar --motivo "…"
    manage.py proponer --proyecto C:/ruta --recuerdo nombre.md --archivo texto.md --motivo "…"

Sin `--archivo`, el texto se lee de la entrada estándar. Nada cambia hasta que
el administrador aprueba la propuesta en «Estándar» → «Propuestas» (acuerdo 3).
"""
import io
import sys

from django.core.management.base import BaseCommand, CommandError

from core.estandar import documentos
from core.estandar.cambios import CambioInvalido


class Command(BaseCommand):
    help = "Deja una propuesta de cambio del estándar o de la memoria, para aprobarla en la pantalla."

    def add_arguments(self, parser):
        parser.add_argument("--ruta", help="el documento del estándar: base/…")
        parser.add_argument("--proyecto", help="la carpeta del proyecto, para un recuerdo")
        parser.add_argument("--recuerdo", help="el nombre del recuerdo")
        parser.add_argument("--archivo", help="el texto completo que se propone; sin esto, la entrada estándar")
        parser.add_argument("--quitar", action="store_true")
        parser.add_argument("--motivo", required=True)
        parser.add_argument("--quien", default="agente")

    def handle(self, *args, ruta=None, proyecto=None, recuerdo=None, archivo=None, quitar=False, motivo="",
               quien="agente", **opciones):
        contenido = ""
        if not quitar:
            if archivo:
                with io.open(archivo, encoding="utf-8", newline="") as f:
                    contenido = f.read()
            else:
                contenido = sys.stdin.read()
        # `EP-030·HU-001` · Propone por el camino único de los documentos.
        accion = documentos.QUITAR_ if quitar else None
        try:
            if ruta:
                propuesta = documentos.proponer("estandar", accion, ruta, contenido, motivo, quien)
            elif proyecto and recuerdo:
                registrado = documentos.proyecto_de(proyecto)
                propuesta = documentos.proponer("recuerdo", accion, recuerdo, contenido, motivo, quien, registrado)
            else:
                raise CommandError("falta --ruta, o --proyecto con --recuerdo")
        except CambioInvalido as razon:
            raise CommandError(str(razon))
        self.stdout.write("Propuesta %d: %s %s. Se aprueba en Cimiento → Estándar → Propuestas." % (
            propuesta.pk, propuesta.get_accion_display().lower(), propuesta.destino()))
