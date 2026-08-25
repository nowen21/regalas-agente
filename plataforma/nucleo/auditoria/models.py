# -*- coding: utf-8 -*-
"""El índice del registro. La fuente es el texto de `datos/auditoria/`.

**Este modelo no deja modificar ni borrar.** No es una precaución de más: es
`DA-08`. Un registro editable no demuestra nada, y la forma de que no se edite
por error es que la operación no exista, no que alguien se acuerde de no
llamarla.

Para las tareas que sí tienen que limpiar el índice —rehacerlo desde el
texto— está `Registro.objects.todos()`, que es el único camino que puede
borrar filas.
"""
from django.db import models


class SoloSeAgrega(Exception):
    """Se intentó cambiar o borrar una fila del índice de auditoría."""


class RegistroQuerySet(models.QuerySet):
    """El conjunto normal: no borra ni actualiza."""

    def delete(self, *_args, **_opciones):
        raise SoloSeAgrega("Lo registrado no se borra.")

    def update(self, *_args, **_opciones):
        raise SoloSeAgrega("Lo registrado no se edita.")


class RegistroManager(models.Manager):
    """El acceso normal. Lo único que sabe hacer de más es crear."""

    def get_queryset(self):
        return RegistroQuerySet(self.model, using=self._db)

    def crear_desde_texto(self, datos):
        """Crea la fila del índice a partir de una línea ya escrita en el texto."""
        return super(RegistroManager, self).get_queryset().create(
            cuando=datos["cuándo"],
            quien=datos["quién"],
            que_se_hizo=datos["qué se hizo"],
            sobre_que=datos["sobre qué"],
            que_cambio=datos["qué cambió"],
            proyecto=datos["proyecto"],
            sesion=datos["sesión"])

    def todos(self):
        """El conjunto sin la protección, para rehacer el índice desde el texto.

        Es el único camino que puede borrar filas, y existe porque el índice se
        reconstruye. Borrar acá no pierde nada: la fuente sigue en el texto.
        """
        return super(RegistroManager, self).get_queryset()


class Registro(models.Model):
    """Una acción registrada. Los seis datos, más la sesión."""

    cuando = models.CharField(max_length=40)
    quien = models.CharField(max_length=100)
    que_se_hizo = models.CharField(max_length=300)
    sobre_que = models.CharField(max_length=300)
    que_cambio = models.TextField(blank=True)
    proyecto = models.CharField(max_length=200, blank=True)
    sesion = models.CharField(max_length=100, blank=True)

    objects = RegistroManager()

    class Meta:
        ordering = ["cuando"]

    def __str__(self):
        return "%s · %s · %s" % (self.cuando, self.quien, self.que_se_hizo)

    def save(self, *args, **opciones):
        """Solo deja la primera escritura. Cambiar una fila ya guardada, nunca."""
        if self.pk is not None:
            raise SoloSeAgrega("Lo registrado no se edita.")
        return super(Registro, self).save(*args, **opciones)

    def delete(self, *_args, **_opciones):
        raise SoloSeAgrega("Lo registrado no se borra.")
