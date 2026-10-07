"""`EP-026·HU-005` · El agente propone un cambio del estándar o de la memoria; se aprueba en la pantalla.

    manage.py proponer --ruta base/x.md --archivo texto-nuevo.md --motivo "…"
    manage.py proponer --ruta base/x.md --quitar --motivo "…"
    manage.py proponer --proyecto C:/ruta --recuerdo nombre.md --archivo texto.md --motivo "…"

Sin `--archivo`, el texto se lee de la entrada estándar. Nada cambia hasta que
el administrador aprueba la propuesta en «Estándar» → «Propuestas» (acuerdo 3).
"""
import io
import os
import sys

from django.core.management.base import BaseCommand, CommandError

from core.estandar.cambios import CambioInvalido, accion_para, ruta_valida
from core.estandar.models import DOCUMENTO, QUITAR, RECUERDO, Documento, Propuesta, Recuerdo
from core.historia.registro import quien_y_por_que
from core.proyectos.models import Proyecto


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
        datos = {"motivo": motivo, "quien": quien, "contenido": contenido}
        if ruta:
            try:
                datos["ruta"] = ruta_valida(ruta)
            except CambioInvalido as razon:
                raise CommandError(str(razon))
            datos.update(objeto=DOCUMENTO,
                         accion=accion_para(DOCUMENTO, Documento.objects.filter(ruta=datos["ruta"]).exists(), quitar))
        elif proyecto and recuerdo:
            registrado = Proyecto.objects.filter(ruta__iexact=os.path.abspath(proyecto)).first()
            if registrado is None:
                raise CommandError("el proyecto %s no está registrado en Cimiento" % proyecto)
            existe = Recuerdo.objects.filter(proyecto=registrado, nombre=recuerdo).exists()
            datos.update(objeto=RECUERDO, proyecto=registrado, nombre=recuerdo,
                         accion=accion_para(RECUERDO, existe, quitar))
        else:
            raise CommandError("falta --ruta, o --proyecto con --recuerdo")
        if datos["accion"] == QUITAR and not (ruta and Documento.objects.filter(ruta=datos["ruta"]).exists()
                                              or recuerdo and datos.get("nombre")):
            raise CommandError("no hay qué quitar")
        with quien_y_por_que(quien=quien, motivo=motivo):
            propuesta = Propuesta.objects.create(**datos)
        self.stdout.write("Propuesta %d: %s %s. Se aprueba en Cimiento → Estándar → Propuestas." % (
            propuesta.pk, propuesta.get_accion_display().lower(), propuesta.destino()))
