"""`EP-025·HU-033` · El comando fijo para guardar el texto de una sección de un análisis.

    manage.py analisis seccion «ruta del analisis-N.md» "Lo acordado" --archivo texto.md

Sin `--archivo`, el texto se lee de la entrada estándar. Reemplaza lo que había
en la sección y lo muestra, para volver a ponerlo con el mismo comando si hace
falta. Reemplaza los guiones sueltos que llenaban cada análisis.
"""
import io
import os
import sys

from django.core.management.base import BaseCommand, CommandError

from core.enganches.llenar_analisis import SeccionInexistente, poner_seccion


class Command(BaseCommand):
    help = "Guarda en un análisis el texto de una sección."

    def add_arguments(self, parser):
        parser.add_argument("accion", choices=["seccion"])
        parser.add_argument("analisis", help="la ruta del analisis-N.md")
        parser.add_argument("seccion", help="el título de la sección, o su comienzo")
        parser.add_argument("--archivo", default="", help="el texto; sin esto, la entrada estándar")

    def handle(self, *args, **o):
        ruta = os.path.abspath(o["analisis"])
        if not os.path.isfile(ruta):
            raise CommandError("no existe el análisis %s" % ruta)
        if o["archivo"]:
            with io.open(o["archivo"], encoding="utf-8") as f:
                cuerpo = f.read()
        else:
            cuerpo = sys.stdin.read()
        with io.open(ruta, encoding="utf-8") as f:
            texto = f.read()
        try:
            nuevo, anterior = poner_seccion(texto, o["seccion"], cuerpo)
        except SeccionInexistente as error:
            raise CommandError(str(error))
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(nuevo)
        self.stdout.write("Sección «%s» guardada. Lo que tenía antes:\n%s" % (o["seccion"], anterior))
