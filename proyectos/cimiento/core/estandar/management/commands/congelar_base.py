"""`EP-026·HU-006` · Congela `base/`, `VERSION` y `CHANGELOG.md`; con `--deshacer`, los suelta.

Congelar pone primero la base al día con git y alinea su versión con la de
`VERSION`, para que el número siga en la base sin retroceder. Se niega si esos
archivos tienen cambios sin guardar: quedarían fuera.
"""
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from core.comun import Git
from core.comun import Proyecto as Carpeta
from core.estandar import congelado
from core.estandar.importar import sincronizar
from core.historia import versiones
from core.historia.models import ESTANDAR, PARCHE
from core.historia.registro import quien_y_por_que
from core.proyectos.models import AjusteBase


class Command(BaseCommand):
    help = "Congela base/, VERSION y CHANGELOG.md: desde ahí el estándar se cambia solo en la base."

    def add_arguments(self, parser):
        parser.add_argument("--deshacer", action="store_true", help="quita la marca")
        parser.add_argument("--motivo", default="")

    def handle(self, *args, deshacer=False, motivo="", **opciones):
        raiz = Carpeta.estandar()
        if deshacer:
            with quien_y_por_que(quien="congelar_base", motivo=motivo or "Se suelta base/ (EP-026·HU-006)",
                                 tipo=PARCHE):
                AjusteBase.objects.filter(clave=congelado.CLAVE).delete()
            congelado.olvidar()
            self.stdout.write("base/, VERSION y CHANGELOG.md vuelven a poder cambiarse.")
            return
        sucios = [l for l in Git(raiz).lineas("status", "--porcelain", "--", "base", *congelado.QUIETOS)]
        if sucios:
            raise CommandError("hay cambios sin guardar en lo que se congela: %s" % ", ".join(s[3:] for s in sucios))
        with transaction.atomic():
            sincronizar(raiz, tipo=PARCHE, motivo="La base toma lo guardado en git antes de congelar (EP-026·HU-006)")
            archivo = versiones.del_archivo()
            if versiones.ultima(ESTANDAR) < archivo:
                versiones.de_partida(archivo, "La base toma la versión %d.%d.%d de VERSION al congelar" % archivo,
                                     "congelar_base")
            with quien_y_por_que(quien="congelar_base", tipo=PARCHE,
                                 motivo=motivo or "Se congelan base/, VERSION y CHANGELOG.md (EP-026·HU-006)"):
                AjusteBase.objects.update_or_create(clave=congelado.CLAVE, defaults={"valor": congelado.SI})
        congelado.olvidar()
        self.stdout.write("Congelado: el estándar va en la %s y se cambia solo en la base." % versiones.actual(ESTANDAR))
