# -*- coding: utf-8 -*-
"""El checklist de una regla, y si su sello sigue valiendo.

    python manage.py sello_de_regla cimiento-el-estandar M11
"""
import io
import os
import subprocess

from django.core.management.base import BaseCommand

from nucleo.ciclo_de_vida import core as ciclo
from nucleo.proyectos.models import Proyecto
from nucleo.reglas import catalogo, sello


def _tocado_el(raiz, archivo):
    """Cuándo cambió por última vez, según el control de versiones."""
    try:
        corrida = subprocess.run(
            ["git", "log", "-1", "--format=%ad", "--date=short", "--", archivo],
            cwd=raiz, capture_output=True, text=True, encoding="utf-8",
            errors="replace", timeout=60)
    except (OSError, subprocess.SubprocessError):
        return ""
    return (corrida.stdout or "").strip()


class Command(BaseCommand):
    help = "El checklist de una regla, y si su sello sigue valiendo"

    def add_arguments(self, parser):
        parser.add_argument("proyecto")
        parser.add_argument("identificador")
        parser.add_argument("--con-las-filas", action="store_true",
                            dest="con_filas")

    def handle(self, *args, **opciones):
        try:
            proyecto = Proyecto.objects.get(identificador=opciones["proyecto"])
        except Proyecto.DoesNotExist:
            self.stdout.write("No hay un proyecto registrado con ese nombre.")
            return

        raiz = proyecto.ruta_codigo
        buscada = None
        for una in catalogo.todas(raiz):
            if una.id == opciones["identificador"]:
                buscada = una
                break
        if buscada is None:
            self.stdout.write("No hay ninguna regla con ese identificador.")
            return

        with io.open(buscada.archivo, encoding="utf-8",
                     errors="replace") as archivo:
            texto = archivo.read()

        version, cuando = sello.contra_que(texto)
        tocado = _tocado_el(raiz, os.path.relpath(buscada.archivo, raiz))
        vencido = sello.parece_vencido(texto, tocado)

        self.stdout.write("Regla: %s · %s"
                          % (buscada.id, ciclo.para_la_consola(buscada.titulo)))
        if not sello.tiene_sello(texto):
            self.stdout.write("**Sin sello.** Nunca se le aplicó el checklist.")
        else:
            self.stdout.write("Sellada contra v%s, el %s. Tocada el %s."
                              % (version or "sin decir", cuando or "sin fecha",
                                 tocado or "sin saber"))
            self.stdout.write("Sello: %s"
                              % ("**parece anulado por fechas**; el estándar es el que decide"
                                 if vencido else "vale"))

        if opciones["con_filas"]:
            self.stdout.write("")
            self.stdout.write("Las %d filas del checklist:"
                              % len(sello.filas(raiz)))
            for fila in sello.filas(raiz):
                self.stdout.write("  %2d  %s"
                                  % (fila["numero"],
                                     ciclo.para_la_consola(fila["que"])))
            self.stdout.write("")
            self.stdout.write("**Buena parte pide criterio.** La plataforma "
                              "trae las filas y guarda lo respondido; decidir "
                              "es de una persona.")
