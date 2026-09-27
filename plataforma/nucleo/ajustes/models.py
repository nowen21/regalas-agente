# -*- coding: utf-8 -*-
"""Lo que se puede cambiar sin abrir el código.

**Por qué esto sí va en la base, si `DA-01` dice que el texto manda.** Esa
decisión habla de **los documentos del proyecto**: lo que un proyecto tiene
escrito no se copia a una tabla, se lee. Un ajuste de la plataforma no es un
documento de ningún proyecto — es un hecho de esta instalación, como las cuentas
y las aprobaciones. No hay ningún texto de dónde leerlo.

**Y la razón de fondo:** si para cambiar una frase hay que abrir el código, la
plataforma no sirve para lo que existe. Quien la administra tiene que poder
cambiarla desde ella.

**Nada se pierde si la tabla se borra.** Cada ajuste tiene su valor de fábrica
escrito al lado, y `poner_al_dia()` los vuelve a sembrar. Lo que se pierde son
los cambios que alguien haya hecho, y eso se dice en el manual.
"""
from django.db import models


class Ajuste(models.Model):
    """Un texto o un número que la plataforma usa y que se puede cambiar."""

    TEXTO = "texto"
    NUMERO = "numero"
    DE_QUE_TIPO = ((TEXTO, "Texto"), (NUMERO, "Número"))

    clave = models.CharField(
        max_length=80, unique=True, verbose_name="Clave",
        help_text="El nombre con que el programa lo pide. No se cambia.")
    valor = models.TextField(
        verbose_name="Valor",
        help_text="Lo que se muestra o se usa. Esto es lo que se cambia.")
    tipo = models.CharField(max_length=10, choices=DE_QUE_TIPO, default=TEXTO)
    para_que = models.CharField(
        max_length=300, verbose_name="Para qué sirve",
        help_text="Dónde se ve y qué pasa si se cambia.")
    de_fabrica = models.TextField(
        blank=True, verbose_name="Valor de fábrica",
        help_text="Con lo que vino. Sirve para volver atrás.")

    class Meta:
        ordering = ["clave"]
        verbose_name = "Ajuste"
        verbose_name_plural = "Ajustes de la plataforma"

    def __str__(self):
        return self.clave

    @property
    def fue_cambiado(self):
        """¿Alguien lo cambió respecto de como vino?"""
        return self.valor != self.de_fabrica


class EtapaDelCiclo(models.Model):
    """Una de las etapas por las que pasa un proyecto.

    **Son siete hoy, y podrían no serlo.** Tenerlas en el código obligaba a
    editarlo para cambiarle el nombre a una, o para explicarla mejor. La carpeta
    sí está atada a cómo se reconocen los documentos; lo demás es texto que se
    lee en pantalla y se cambia acá.
    """

    orden = models.IntegerField(
        verbose_name="Orden",
        help_text="El del ciclo, de planear a mantener. No es alfabético a "
                  "propósito: el orden enseña por dónde va un proyecto.")
    carpeta = models.CharField(
        max_length=60, unique=True, verbose_name="Carpeta",
        help_text="Dentro de `cvds/`. Con esto se reconocen sus documentos: "
                  "cambiarla hace que dejen de encontrarse.")
    nombre = models.CharField(
        max_length=60, verbose_name="Nombre en claro",
        help_text="Como se lee en la pantalla. «Planear», no «planificacion».")
    pregunta = models.CharField(
        max_length=200, verbose_name="Qué se responde en esta etapa")
    queda = models.CharField(
        max_length=300, verbose_name="Qué queda escrito en ella")

    class Meta:
        ordering = ["orden"]
        verbose_name = "Etapa del ciclo"
        verbose_name_plural = "Etapas del ciclo de vida"

    def __str__(self):
        return "%d. %s" % (self.orden, self.nombre)
