# -*- coding: utf-8 -*-
"""`manage.py danar_a_proposito`: daña el código a propósito y dice qué daños no detectan las pruebas.

    python manage.py danar_a_proposito --danos danos.json --pruebas "python -m unittest" --raiz «carpeta»

`EP-029·HU-008` · `danos.json` es una lista de objetos `nombre`, `archivo` (relativo
a `--raiz`), `antes` y `despues`. Por cada daño copia el archivo, lo daña, corre
las pruebas y lo devuelve desde la copia; al final comprueba que todo quedó igual.
"""
from django.core.management.base import BaseCommand, CommandError

from core.comun.consola import preparar_salida

from ...danar import NO_DETECTADO, Danar, NoSeDana, leer_danos


class Command(BaseCommand):
    help = "Daña el código a propósito, corre las pruebas con cada daño y dice cuáles no detectan."
    requires_system_checks = []

    def add_arguments(self, parser):
        parser.add_argument("--danos", required=True, help="el JSON con la lista de daños")
        parser.add_argument("--pruebas", required=True, help="la orden que corre las pruebas")
        parser.add_argument("--raiz", default=".", help="la carpeta del proyecto; los archivos van relativos a ella")
        parser.add_argument("--tiempo", type=int, default=600, help="segundos máximos por corrida de las pruebas")

    def handle(self, *args, **o):
        preparar_salida()
        try:
            danar = Danar(o["raiz"], o["pruebas"], o["tiempo"])
            resultados = danar.correr(leer_danos(o["danos"]))
        except NoSeDana as e:
            raise CommandError("No se dañó nada: %s" % e if "no pasan sin daños" in str(e) else str(e))
        ancho = max(len(d.nombre) for d, _r in resultados)
        for dano, resultado in resultados:
            self.stdout.write("  %s  %s" % (dano.nombre.ljust(ancho), resultado))
        sin_detectar = sum(1 for _d, r in resultados if r == NO_DETECTADO)
        self.stdout.write("%d daños, %d sin detectar. Todo quedó como estaba." % (len(resultados), sin_detectar))
        for relativa in danar.borrados:
            self.stdout.write("  borrado, lo había dejado un daño: %s" % relativa)
