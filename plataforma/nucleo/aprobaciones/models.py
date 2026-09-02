# -*- coding: utf-8 -*-
"""Quién aprobó un documento, cuándo, y **sobre qué texto exacto**.

**Esta sí se guarda, y es la única del módulo que lo hace.** Una aprobación no
se puede derivar del texto: aprobar es un hecho que ocurrió, y si no queda
escrito no ocurrió para nadie más. Es lo contrario del expediente o de los
huecos, que se calculan al pedirlos.

**La huella del texto es lo que la vuelve una aprobación y no una firma en
blanco.** Sin ella, «este documento está aprobado» no dice nada: el documento
pudo haber cambiado tres veces desde entonces. Con ella, se puede responder la
única pregunta que importa: **¿lo aprobado sigue siendo lo que hay?**

**Nada se borra.** Cuando un documento cambia y su aprobación caduca, la
aprobación anterior **se queda**: es la historia de qué se autorizó y cuándo.
Borrarla dejaría el documento como si nunca hubiera pasado por nadie.
"""
from django.db import models


class Aprobacion(models.Model):
    """Una aprobación que ocurrió. **Se agrega; no se edita ni se borra.**"""

    proyecto = models.CharField(max_length=120, db_index=True)
    # La ruta del documento dentro del proyecto. Es lo que lo identifica.
    documento = models.CharField(max_length=500, db_index=True)
    quien = models.CharField(max_length=120)
    cuando = models.CharField(max_length=40)
    # La huella del texto que se aprobó. Sin ella, la aprobación no dice nada.
    huella = models.CharField(max_length=64)
    # Cuántos caracteres tenía, para poder decir cuánto cambió después.
    tamano = models.IntegerField(default=0)

    class Meta:
        ordering = ["proyecto", "documento", "-id"]

    def __str__(self):
        return "%s · %s · %s" % (self.proyecto, self.documento, self.cuando)
