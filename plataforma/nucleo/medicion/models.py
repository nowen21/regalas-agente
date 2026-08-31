# -*- coding: utf-8 -*-
"""El índice de lo conversado. **No es la fuente**: se borra entero y se rehace.

La fuente son los archivos de `historico-chat/` del proyecto, que el enganche
del estándar ya escribió y que el propio proyecto versiona. Acá no hay ningún
dato que no esté también en ese texto: si algún día aparece uno, la decisión
`DA-01` dejó de cumplirse y hay que mirarla de nuevo.

**Por qué el texto del mensaje sí se guarda acá.** El `CA-01` pide ver **en qué
mensaje** se dijo lo que se busca, y abrir el archivo por cada resultado leería
el disco entero para responder una búsqueda. Sigue siendo reconstruible: sale de
volver a leer los mismos archivos.
"""
from django.db import models


class Sesion(models.Model):
    """Un tramo de trabajo con el agente. Uno por archivo del histórico."""

    USUARIO = "usuario"
    AGENTE = "agente"

    proyecto = models.ForeignKey("proyectos.Proyecto", on_delete=models.CASCADE,
                                 related_name="sesiones")
    # Relativo a la raíz del proyecto: la ruta absoluta cambia de máquina, y
    # lo que identifica a la sesión es dónde vive dentro de su proyecto.
    archivo = models.CharField(max_length=500)
    fecha = models.CharField(max_length=10)
    tema = models.CharField(max_length=300, blank=True)
    huella = models.CharField(max_length=64)

    class Meta:
        ordering = ["-fecha", "archivo"]
        unique_together = [("proyecto", "archivo")]

    def __str__(self):
        return self.tema or self.archivo


class Mensaje(models.Model):
    """Un turno de la conversación, tal como quedó escrito."""

    sesion = models.ForeignKey(Sesion, on_delete=models.CASCADE,
                               related_name="mensajes")
    orden = models.IntegerField()
    quien = models.CharField(max_length=10)
    cuando = models.CharField(max_length=40)
    texto = models.TextField()

    class Meta:
        ordering = ["sesion", "orden"]
        unique_together = [("sesion", "orden")]

    def __str__(self):
        return "%s · %s" % (self.quien, self.texto[:40])
