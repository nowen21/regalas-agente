"""`EP-030·HU-001` · El comando fijo para los documentos de Cimiento, de cualquier tipo registrado.

    manage.py documento tipos
    manage.py documento listar estandar base/01-conducta
    manage.py documento ver estandar base/01-conducta.md
    manage.py documento ver recuerdo memory.md --proyecto "C:/Ing. Jose/ia/agente"
    manage.py documento crear recuerdo nuevo.md --proyecto … --archivo texto.md --motivo "…"
    manage.py documento editar estandar base/x.md --archivo texto.md --motivo "…"
    manage.py documento quitar estandar base/x.md --motivo "…"

Crear, editar y quitar dejan una propuesta: nada cambia hasta que se aprueba en
Cimiento → Estándar → Propuestas. Sin `--archivo`, el texto se lee de la entrada estándar.
"""
import io
import sys

from django.core.management.base import BaseCommand, CommandError

from core.estandar import documentos
from core.estandar.cambios import CambioInvalido

ACCIONES = ["tipos", "listar", "ver", documentos.CREAR, documentos.EDITAR, documentos.QUITAR_]


class Command(BaseCommand):
    help = "Lista, muestra, crea, edita o quita un documento de Cimiento; lo que cambia queda como propuesta."

    def add_arguments(self, parser):
        parser.add_argument("accion", choices=ACCIONES)
        parser.add_argument("tipo", nargs="?", default="")
        parser.add_argument("clave", nargs="?", default="", help="la ruta o el nombre; en listar, el comienzo")
        parser.add_argument("--proyecto", help="la carpeta del proyecto, para los tipos que lo piden")
        parser.add_argument("--archivo", help="el texto completo; sin esto, la entrada estándar")
        parser.add_argument("--motivo", default="")
        parser.add_argument("--quien", default="agente")

    def handle(self, *args, accion="", tipo="", clave="", proyecto=None, archivo=None, motivo="", quien="agente",
               **opciones):
        try:
            if accion == "tipos":
                for t in documentos.TIPOS.values():
                    self.stdout.write("%s: %s" % (t.nombre, t.descripcion))
                return
            t = documentos.tipo(tipo)
            registrado = documentos.proyecto_de(proyecto) if t.pide_proyecto else None
            if accion == "listar":
                for c in documentos.listar(tipo, clave, registrado):
                    self.stdout.write(c)
                return
            if not clave:
                raise CommandError("falta la ruta o el nombre del documento")
            if accion == "ver":
                self.stdout.write(documentos.ver(tipo, clave, registrado), ending="")
                return
            contenido = "" if accion == documentos.QUITAR_ else self._texto(archivo)
            propuesta = documentos.proponer(tipo, accion, clave, contenido, motivo, quien, registrado)
        except CambioInvalido as razon:
            raise CommandError(str(razon))
        self.stdout.write("Propuesta %d: %s %s. Se aprueba en Cimiento → Estándar → Propuestas." % (
            propuesta.pk, propuesta.get_accion_display().lower(), propuesta.destino()))

    @staticmethod
    def _texto(archivo):
        if archivo:
            with io.open(archivo, encoding="utf-8", newline="") as f:
                return f.read()
        return sys.stdin.read()
