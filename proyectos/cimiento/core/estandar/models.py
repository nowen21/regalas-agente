# -*- coding: utf-8 -*-
"""`EP-026·HU-003` · Un documento del estándar y un recuerdo de un proyecto.

Lo que se guarda en ellos tiene historia (HU-001) y sube la versión del
estándar o la del proyecto (HU-002): la tabla del estándar es de la app
`estandar`, que `historia.versiones` sube como estándar.
"""
from django.db import models


class Documento(models.Model):
    """Un documento de `base/`, con su ruta desde la raíz del estándar y su texto exacto."""

    ruta = models.CharField(max_length=255, unique=True, help_text="base/01-conducta.md")
    contenido = models.TextField(blank=True, default="")
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["ruta"]
        verbose_name = "documento del estándar"
        verbose_name_plural = "documentos del estándar"

    def __str__(self):
        return self.ruta

    def nombre_legible(self):
        """`EP-027·HU-005` · El título del documento, no su ruta."""
        from .presentar import titulo_de_texto
        return titulo_de_texto(self.contenido, self.ruta)


class Recuerdo(models.Model):
    """Un recuerdo de la memoria de un proyecto (`01·C19`)."""

    proyecto = models.ForeignKey("proyectos.Proyecto", on_delete=models.PROTECT, related_name="recuerdos")
    nombre = models.CharField(max_length=200, help_text="como el archivo: aprobar-antes-de-commit.md")
    contenido = models.TextField(blank=True, default="")
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["proyecto", "nombre"]
        constraints = [models.UniqueConstraint(fields=["proyecto", "nombre"], name="un_recuerdo_por_nombre")]
        verbose_name = "recuerdo"

    def __str__(self):
        return "%s · %s" % (self.proyecto, self.nombre)

    def nombre_legible(self):
        """`EP-027·HU-005` · El título del recuerdo, no su nombre de archivo."""
        from .presentar import recuerdo_legible
        return recuerdo_legible(self.nombre, self.contenido)[0]

    def descripcion(self):
        from .presentar import recuerdo_legible
        return recuerdo_legible(self.nombre, self.contenido)[1]


PENDIENTE, APROBADA, RECHAZADA = "pendiente", "aprobada", "rechazada"
ESTADOS = [(PENDIENTE, "Pendiente"), (APROBADA, "Aprobada"), (RECHAZADA, "Rechazada")]
DOCUMENTO, RECUERDO = "documento", "recuerdo"
OBJETOS = [(DOCUMENTO, "Documento del estándar"), (RECUERDO, "Recuerdo de un proyecto")]
CREAR, CAMBIAR, QUITAR = "crear", "cambiar", "quitar"
ACCIONES = [(CREAR, "Crear"), (CAMBIAR, "Cambiar"), (QUITAR, "Quitar")]


class Propuesta(models.Model):
    """`EP-026·HU-005` · Lo que propone el agente o un programa. No cambia nada
    hasta que el administrador la aprueba en la pantalla (acuerdo 3)."""

    objeto = models.CharField(max_length=10, choices=OBJETOS)
    accion = models.CharField(max_length=10, choices=ACCIONES)
    ruta = models.CharField(max_length=255, blank=True, default="", help_text="del documento: base/…")
    proyecto = models.ForeignKey("proyectos.Proyecto", null=True, blank=True, on_delete=models.PROTECT,
                                 related_name="propuestas")
    nombre = models.CharField(max_length=200, blank=True, default="", help_text="del recuerdo")
    contenido = models.TextField(blank=True, default="", help_text="el texto completo que queda")
    motivo = models.TextField(blank=True, default="")
    quien = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default=PENDIENTE)
    resuelta_por = models.ForeignKey("auth.User", null=True, blank=True, on_delete=models.SET_NULL,
                                     related_name="propuestas_resueltas")
    resuelta = models.DateTimeField(null=True, blank=True)
    # `EP-028·HU-004` · Rechazar pide el motivo (guía de diseño de pantallas, §11).
    motivo_rechazo = models.TextField(blank=True, default="")

    class Meta:
        ordering = ["-fecha", "-id"]
        verbose_name = "propuesta"

    def destino(self):
        return self.ruta if self.objeto == DOCUMENTO else "%s · %s" % (self.proyecto, self.nombre)

    def nombre_legible(self):
        """`EP-027·HU-005` · Qué cambia, por su nombre: el título del documento o del recuerdo."""
        from .presentar import recuerdo_legible, titulo_de_texto
        if self.objeto == DOCUMENTO:
            texto = self.contenido
            if self.accion == QUITAR or not texto:
                actual = Documento.objects.filter(ruta=self.ruta).only("contenido").first()
                texto = actual.contenido if actual else ""
            return titulo_de_texto(texto, self.ruta)
        texto = self.contenido
        if self.accion == QUITAR or not texto:
            actual = Recuerdo.objects.filter(proyecto=self.proyecto, nombre=self.nombre).only("contenido").first()
            texto = actual.contenido if actual else ""
        return "%s · %s" % (self.proyecto, recuerdo_legible(self.nombre, texto)[0])

    def __str__(self):
        return "%s %s %s" % (self.get_estado_display(), self.accion, self.destino())


ABIERTO, CORREGIDO, DESCARTADO = "abierto", "corregido", "descartado"
ESTADOS_DEL_REPORTE = [(ABIERTO, "Abierto"), (CORREGIDO, "Corregido"), (DESCARTADO, "Descartado")]


class Reporte(models.Model):
    """`EP-026·HU-008` · Lo que un proyecto encuentra mal en el estándar.

    No sube versión al llegar: la sube la corrección, y el reporte apunta a la
    versión que lo corrigió (análisis 1 del pendiente 132, acuerdo 13).
    """

    proyecto = models.ForeignKey("proyectos.Proyecto", on_delete=models.PROTECT, related_name="reportes")
    titulo = models.CharField(max_length=200)
    texto = models.TextField(blank=True, default="")
    regla = models.CharField(max_length=20, blank=True, default="", help_text="la regla que toca, como 02·F8")
    quien = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADOS_DEL_REPORTE, default=ABIERTO)
    corregido_en = models.ForeignKey("historia.Version", null=True, blank=True, on_delete=models.PROTECT,
                                     related_name="reportes_corregidos")
    motivo = models.TextField(blank=True, default="", help_text="por qué se descartó")
    resuelto_por = models.ForeignKey("auth.User", null=True, blank=True, on_delete=models.SET_NULL,
                                     related_name="reportes_resueltos")
    resuelto = models.DateTimeField(null=True, blank=True)
    avisado = models.BooleanField(default=False, help_text="el proyecto ya se enteró de cómo quedó")

    class Meta:
        ordering = ["-fecha", "-id"]
        verbose_name = "reporte de un proyecto"

    def __str__(self):
        return "%s · %s" % (self.proyecto, self.titulo)

    def nombre_legible(self):
        return str(self)


# --- EP-027·HU-001 · Las reglas en tablas, con las casillas del molde ---------

from .molde import BLINDADA, DEPENDE, DEROGA, DEROGADA, EXTIENDE, OPT_IN, SIN_MARCA  # noqa: E402

MARCAS = [(SIN_MARCA, "Sin marca"), (BLINDADA, "Blindada"), (OPT_IN, "Opt-in"), (DEROGADA, "Derogada")]
TIPOS_DE_DEPENDENCIA = [(EXTIENDE, "Extiende"), (DEPENDE, "Depende de"), (DEROGA, "Deroga")]
SIN_DECLARAR, NO_VALIDABLE, FALTA_EL_PROGRAMA, VALIDABLE = "", "no", "falta", "si"
VALIDABLES = [(SIN_DECLARAR, "Sin declarar"), (NO_VALIDABLE, "No"),
              (FALTA_EL_PROGRAMA, "Sí, falta el programa"), (VALIDABLE, "Sí, con su programa")]


class Capitulo(models.Model):
    """Un capítulo del estándar: `02-flujo-de-trabajo`, con su número, su nombre y sus letras (`20·M4`)."""

    clave = models.CharField(max_length=80, unique=True, help_text="02-flujo-de-trabajo")
    numero = models.CharField(max_length=2)
    nombre = models.CharField(max_length=200)
    prefijo = models.CharField(max_length=10, blank=True, default="", help_text="F, DOC…")
    documento = models.ForeignKey(Documento, null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name="capitulos", help_text="el documento que abre el capítulo")

    class Meta:
        ordering = ["clave"]
        verbose_name = "capítulo"

    def __str__(self):
        return self.nombre or self.clave

    def nombre_legible(self):
        return str(self)


class Tarea(models.Model):
    """Una tarea de `01·C28` a la que aplican reglas: `trabajar-cadena`, `tocar-git`…"""

    nombre = models.CharField(max_length=80, unique=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "tarea"

    def __str__(self):
        return self.nombre

    def nombre_legible(self):
        return self.nombre


class Regla(models.Model):
    """Una regla, con una casilla por parte de su molde (`20·M5`).

    Cada casilla de texto guarda su parte tal cual se escribe; de ellas salen las
    partes menores (incorrecto y correcto, condición, límite y autoriza, y el
    resultado del sello), para mostrarlas y comprobarlas sin leer el texto."""

    proyecto = models.ForeignKey("proyectos.Proyecto", null=True, blank=True, on_delete=models.PROTECT,
                                 related_name="reglas", help_text="vacío: es del estándar")
    capitulo = models.ForeignKey(Capitulo, null=True, blank=True, on_delete=models.PROTECT, related_name="reglas")
    documento = models.ForeignKey(Documento, null=True, blank=True, on_delete=models.PROTECT, related_name="reglas",
                                  help_text="dónde se arma su texto")
    orden = models.PositiveIntegerField(default=0, help_text="su lugar dentro del documento")
    grupo = models.CharField(max_length=200, blank=True, default="",
                             help_text="la sección donde va, en las reglas de un proyecto (EP-027·HU-006)")
    apartada = models.BooleanField(default=False,
                                   help_text="la regla del proyecto que salió de su texto: no se borra (20·M11)")
    codigo = models.CharField(max_length=20, help_text="F8, DOC22…; no cambia nunca (20·M4)")
    titulo = models.CharField(max_length=300)
    marca = models.CharField(max_length=10, choices=MARCAS, blank=True, default=SIN_MARCA)
    marca_texto = models.CharField(max_length=160, blank=True, default="",
                                   help_text="como se escribe la marca al final del título")
    exigencia = models.TextField()
    excepcion = models.TextField(blank=True, default="")
    excepcion_condicion = models.TextField(blank=True, default="")
    excepcion_limite = models.TextField(blank=True, default="")
    excepcion_autoriza = models.TextField(blank=True, default="")
    ejemplo = models.TextField(blank=True, default="")
    ejemplo_incorrecto = models.TextField(blank=True, default="")
    ejemplo_correcto = models.TextField(blank=True, default="")
    notas = models.TextField(blank=True, default="", help_text="lo que va después del ejemplo y no es del molde")
    quien_cumple = models.TextField(blank=True, default="", help_text="solo el capítulo 00")
    validable = models.CharField(max_length=5, choices=VALIDABLES, blank=True, default=SIN_DECLARAR)
    validador = models.CharField(max_length=200, blank=True, default="", help_text="el programa que la comprueba")
    autoriza_escribir = models.TextField(blank=True, default="")
    tareas = models.ManyToManyField(Tarea, through="ReglaTarea", related_name="reglas", blank=True)
    raya = models.BooleanField(default=False, help_text="la raya que separa la regla de su sello")
    sello = models.TextField(blank=True, default="")
    sello_resultado = models.CharField(max_length=10, blank=True, default="")
    sello_version = models.CharField(max_length=20, blank=True, default="")
    sello_fecha = models.DateField(null=True, blank=True)
    sello_observacion = models.TextField(blank=True, default="")
    actualizada = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["capitulo__clave", "documento__ruta", "orden"]
        verbose_name = "regla"

    def __str__(self):
        return "%s · %s" % (self.codigo, self.titulo)

    def nombre_legible(self):
        return str(self)

    def clean(self):
        from django.core.exceptions import ValidationError
        repetida = Regla.objects.filter(codigo=self.codigo, proyecto=self.proyecto).exclude(pk=self.pk)
        if repetida.exists():
            raise ValidationError({"codigo": "El código %s ya es de otra regla (20·M4)." % self.codigo})


class ReglaTarea(models.Model):
    """Una tarea a la que aplica la regla, en el orden de su línea «Aplica a»."""

    regla = models.ForeignKey(Regla, on_delete=models.CASCADE, related_name="aplica")
    tarea = models.ForeignKey(Tarea, on_delete=models.PROTECT)
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["regla", "orden"]
        constraints = [models.UniqueConstraint(fields=["regla", "tarea"], name="una_tarea_por_regla")]
        verbose_name = "tarea de una regla"

    def nombre_legible(self):
        return "%s · %s" % (self.regla.codigo, self.tarea.nombre)


class Dependencia(models.Model):
    """Lo que la regla declara con `20·M7`: extiende, depende de o deroga otra."""

    regla = models.ForeignKey(Regla, on_delete=models.CASCADE, related_name="dependencias")
    tipo = models.CharField(max_length=12, choices=TIPOS_DE_DEPENDENCIA)
    codigo = models.CharField(max_length=20, help_text="el código de la otra regla")
    destino = models.ForeignKey(Regla, null=True, blank=True, on_delete=models.SET_NULL, related_name="dependientes")

    class Meta:
        ordering = ["regla", "tipo", "codigo"]
        constraints = [models.UniqueConstraint(fields=["regla", "tipo", "codigo"], name="una_dependencia_por_tipo")]
        verbose_name = "dependencia entre reglas"

    def __str__(self):
        return "%s %s %s" % (self.regla.codigo, self.tipo, self.codigo)

    def nombre_legible(self):
        return str(self)
