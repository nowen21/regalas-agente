# -*- coding: utf-8 -*-
"""`EP-026·HU-005` · Las pantallas del estándar, de la memoria y de las propuestas.

Toda cuenta mira; solo el grupo administrador cambia, quita o aprueba (RNF-01).
Cada envío que cambia algo trae las dos preguntas: el middleware fija con ellas
el tipo de la versión, y la historia guarda el cambio (HU-001, HU-002).
"""
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.safestring import mark_safe
from django.views import View

from core.cuentas.permisos import es_administrador
from core.historia.models import ESTANDAR
from core.historia.versiones import actual
from core.proyectos.models import Proyecto

from . import cambios
from .models import PENDIENTE, Documento, Propuesta, Recuerdo
from .presentar import Ficha, Estandar


def _sin_permiso(peticion):
    return render(peticion, "cuentas/sin_permiso.html", status=403)


class Lista(View):
    """`EP-027·HU-004` · El estándar por capítulo, con el código y el nombre de cada regla."""

    def get(self, peticion):
        buscar = peticion.GET.get("q", "").strip()
        estandar = Estandar(Documento.objects.all())
        capitulos = estandar.capitulos()
        if buscar:
            hallados = set(Documento.objects.filter(contenido__icontains=buscar).values_list("pk", flat=True))
            for c in capitulos:
                c["renglones"] = [r for r in c["renglones"] if r["pk"] in hallados]
            capitulos = [c for c in capitulos if c["renglones"]]
        return render(peticion, "estandar/lista.html", {
            "capitulos": capitulos, "buscar": buscar, "version": actual(ESTANDAR),
            "pendientes": Propuesta.objects.filter(estado=PENDIENTE).count(),
            "proyectos": Proyecto.objects.filter(activo=True),
            "puede_cambiar": es_administrador(peticion.user)})


class VerDocumento(View):
    """`EP-027·HU-004` · El documento como página, con sus relaciones; quien
    administra cambia el texto en su propia pestaña."""

    def get(self, peticion, pk):
        documento = get_object_or_404(Documento, pk=pk)
        estandar = Estandar(Documento.objects.all())
        ficha = estandar.por_pk[documento.pk]
        return render(peticion, "estandar/documento.html", {
            "documento": documento, "ficha": ficha, "pagina": mark_safe(estandar.html(ficha)),
            "relaciones": estandar.relaciones(ficha), "capitulo": estandar.capitulo_de(ficha),
            "puede_cambiar": es_administrador(peticion.user), "nuevo": False})

    def post(self, peticion, pk):
        if not es_administrador(peticion.user):
            return _sin_permiso(peticion)
        documento = get_object_or_404(Documento, pk=pk)
        cambios.guardar_documento(documento.ruta, peticion.POST.get("contenido", ""))
        messages.success(peticion, "Documento guardado; el estándar va en la %s." % actual(ESTANDAR))
        return redirect("estandar:documento", pk=pk)


class NuevoDocumento(View):

    def get(self, peticion):
        if not es_administrador(peticion.user):
            return _sin_permiso(peticion)
        return render(peticion, "estandar/documento.html", {"documento": None, "puede_cambiar": True, "nuevo": True})

    def post(self, peticion):
        if not es_administrador(peticion.user):
            return _sin_permiso(peticion)
        try:
            documento = cambios.guardar_documento(peticion.POST.get("ruta", ""), peticion.POST.get("contenido", ""))
        except cambios.CambioInvalido as razon:
            messages.error(peticion, "No se creó: %s." % razon)
            return redirect("estandar:nuevo")
        messages.success(peticion, "Documento creado.")
        return redirect("estandar:documento", pk=documento.pk)


class QuitarDocumento(View):

    def post(self, peticion, pk):
        if not es_administrador(peticion.user):
            return _sin_permiso(peticion)
        documento = get_object_or_404(Documento, pk=pk)
        titulo = Ficha(documento).titulo
        cambios.quitar_documento(documento)
        messages.success(peticion, "Se quitó «%s»; queda en la historia." % titulo)
        return redirect("estandar:lista")


class Memoria(View):

    def get(self, peticion, proyecto):
        proyecto = get_object_or_404(Proyecto, pk=proyecto)
        return render(peticion, "estandar/recuerdos.html", {
            "proyecto": proyecto, "recuerdos": proyecto.recuerdos.all(),
            "version": actual("proyecto", proyecto.pk), "puede_cambiar": es_administrador(peticion.user)})


class VerRecuerdo(View):

    def get(self, peticion, proyecto, pk=None):
        proyecto = get_object_or_404(Proyecto, pk=proyecto)
        recuerdo = get_object_or_404(Recuerdo, pk=pk, proyecto=proyecto) if pk else None
        if recuerdo is None and not es_administrador(peticion.user):
            return _sin_permiso(peticion)
        return render(peticion, "estandar/recuerdo.html", {
            "proyecto": proyecto, "recuerdo": recuerdo, "puede_cambiar": es_administrador(peticion.user)})

    def post(self, peticion, proyecto, pk=None):
        if not es_administrador(peticion.user):
            return _sin_permiso(peticion)
        proyecto = get_object_or_404(Proyecto, pk=proyecto)
        if pk and peticion.POST.get("quitar"):
            get_object_or_404(Recuerdo, pk=pk, proyecto=proyecto).delete()
            messages.success(peticion, "Recuerdo quitado; queda en la historia.")
            return redirect("estandar:memoria", proyecto=proyecto.pk)
        nombre = get_object_or_404(Recuerdo, pk=pk, proyecto=proyecto).nombre if pk else peticion.POST.get("nombre", "")
        try:
            recuerdo = cambios.guardar_recuerdo(proyecto, nombre, peticion.POST.get("contenido", ""))
        except cambios.CambioInvalido as razon:
            messages.error(peticion, "No se guardó: %s." % razon)
            return redirect("estandar:memoria", proyecto=proyecto.pk)
        messages.success(peticion, "Recuerdo guardado.")
        return redirect("estandar:recuerdo", proyecto=proyecto.pk, pk=recuerdo.pk)


class Propuestas(View):

    def get(self, peticion):
        # `EP-028·HU-004` · Cada pendiente con lo que cambia (guía de diseño de pantallas, §11).
        pendientes = list(Propuesta.objects.filter(estado=PENDIENTE).select_related("proyecto"))
        for propuesta in pendientes:
            propuesta.cambia = cambios.que_cambia(propuesta)
        return render(peticion, "estandar/propuestas.html", {
            "pendientes": pendientes,
            "resueltas": Propuesta.objects.exclude(estado=PENDIENTE).select_related("proyecto", "resuelta_por")[:50],
            "puede_cambiar": es_administrador(peticion.user)})


class Resolver(View):
    aprobar = True

    def post(self, peticion, pk):
        if not es_administrador(peticion.user):
            return _sin_permiso(peticion)
        propuesta = get_object_or_404(Propuesta, pk=pk)
        try:
            if self.aprobar:
                cambios.aplicar(propuesta, peticion.user)
            else:
                motivo = peticion.POST.get("motivo_rechazo", "").strip()
                if not motivo:
                    messages.error(peticion, "Para rechazar la propuesta %d hay que escribir por qué." % propuesta.pk)
                    return redirect("estandar:propuestas")
                cambios.rechazar(propuesta, peticion.user, motivo)
        except cambios.CambioInvalido as razon:
            messages.error(peticion, "No se resolvió: %s." % razon)
        else:
            messages.success(peticion, "Propuesta %d %s." % (propuesta.pk, "aprobada" if self.aprobar else "rechazada"))
        return redirect("estandar:propuestas")


def raiz_del_repositorio():
    """`EP-026·HU-007` · El repositorio donde vive Cimiento. Las pruebas lo cambian."""
    from core.comun import Proyecto as Carpeta

    return Carpeta.estandar()


class SubirAGit(View):
    """`EP-026·HU-007` · Lo que cambió cada sesión, y el botón que hace su commit."""

    def get(self, peticion):
        from core.herramientas.cambios import CambiosPorSesion

        try:
            propios, compartidos, sin_sesion = CambiosPorSesion(raiz_del_repositorio()).repartir()
        except ValueError as error:
            messages.error(peticion, str(error))
            propios, compartidos, sin_sesion = {}, [], []
        return render(peticion, "estandar/git.html", {
            "propios": sorted(propios.items()), "compartidos": compartidos, "sin_sesion": sin_sesion,
            "puede_cambiar": es_administrador(peticion.user)})

    def post(self, peticion):
        from .subir import SinSubir, guardar

        if not es_administrador(peticion.user):
            return _sin_permiso(peticion)
        p = peticion.POST
        try:
            hash_, subido = guardar(raiz_del_repositorio(), p.get("sesion", ""), p.get("asunto", ""),
                                    p.get("idea", ""), p.get("hecho", ""), subir=bool(p.get("subir")))
        except SinSubir as razon:
            messages.error(peticion, "Sin subir: %s" % razon)
        else:
            messages.success(peticion, "Commit %s hecho%s." % (hash_, " y subido" if subido else ""))
        return redirect("estandar:git")


class Reportes(View):
    """`EP-026·HU-008` · Lo que reportan los proyectos, y cómo quedó."""

    def get(self, peticion):
        from core.historia.models import Version

        from .models import ABIERTO, Reporte

        return render(peticion, "estandar/reportes.html", {
            "abiertos": Reporte.objects.filter(estado=ABIERTO).select_related("proyecto"),
            "resueltos": Reporte.objects.exclude(estado=ABIERTO).select_related(
                "proyecto", "corregido_en", "resuelto_por")[:50],
            "versiones": Version.objects.filter(ambito=ESTANDAR).order_by("-id")[:30],
            "proyectos": Proyecto.objects.filter(activo=True),
            "puede_cambiar": es_administrador(peticion.user)})

    def post(self, peticion):
        from .models import Reporte

        if not es_administrador(peticion.user):
            return _sin_permiso(peticion)
        proyecto = get_object_or_404(Proyecto, pk=peticion.POST.get("proyecto") or 0)
        titulo = peticion.POST.get("titulo", "").strip()
        if not titulo:
            messages.error(peticion, "El reporte necesita su título.")
            return redirect("estandar:reportes")
        Reporte.objects.create(proyecto=proyecto, titulo=titulo, texto=peticion.POST.get("texto", ""),
                               regla=peticion.POST.get("regla", "").strip(), quien=peticion.user.get_username())
        messages.success(peticion, "Reporte guardado.")
        return redirect("estandar:reportes")


class ResolverReporte(View):
    """`EP-026·HU-008` · Corregido, con la versión del estándar que lo corrigió, o descartado con su motivo."""

    def post(self, peticion, pk):
        from django.utils import timezone

        from core.historia.models import Version

        from .models import ABIERTO, CORREGIDO, DESCARTADO, Reporte

        if not es_administrador(peticion.user):
            return _sin_permiso(peticion)
        reporte = get_object_or_404(Reporte, pk=pk)
        if reporte.estado != ABIERTO:
            messages.error(peticion, "Ese reporte ya está %s." % reporte.get_estado_display().lower())
            return redirect("estandar:reportes")
        if peticion.POST.get("descartar"):
            motivo = peticion.POST.get("motivo", "").strip()
            if not motivo:
                messages.error(peticion, "Descartar pide el motivo.")
                return redirect("estandar:reportes")
            reporte.estado, reporte.motivo = DESCARTADO, motivo
        else:
            version = get_object_or_404(Version, pk=peticion.POST.get("version") or 0, ambito=ESTANDAR)
            if version.fecha < reporte.fecha:
                messages.error(peticion, "La versión que corrige es posterior al reporte.")
                return redirect("estandar:reportes")
            reporte.estado, reporte.corregido_en = CORREGIDO, version
        reporte.resuelto_por, reporte.resuelto = peticion.user, timezone.now()
        reporte.save()
        messages.success(peticion, "Reporte %d %s." % (reporte.pk, reporte.get_estado_display().lower()))
        return redirect("estandar:reportes")


class VistaPrevia(View):
    """`EP-026·HU-009` · Qué reglas le llegarían al agente con un mensaje, en un
    proyecto. Solo muestra: no guarda nada ni deja historia (acuerdo 21)."""

    def get(self, peticion):
        from core.herramientas.recuperar import RecuperadorDeReglas
        from core.proyectos.ajustes import CAPITULOS_OPT_IN, SI, clave_opt_in

        proyectos = Proyecto.objects.filter(activo=True).order_by("nombre")
        proyecto = proyectos.filter(pk=peticion.GET.get("proyecto") or 0).first()
        mensaje = peticion.GET.get("mensaje", "")
        bloque, opt_in = None, []
        if proyecto:
            ajustes = proyecto.ajustes()
            opt_in = [(c, tema, ajustes[clave_opt_in(c)][0] == SI) for c, tema in CAPITULOS_OPT_IN.items()]
            if mensaje.strip():
                bloque = RecuperadorDeReglas().como_texto(mensaje, proyecto=proyecto.ruta) or \
                    "Con este mensaje no llega ninguna regla."
        return render(peticion, "estandar/vista_previa.html", {
            "proyectos": proyectos, "proyecto": proyecto, "mensaje": mensaje, "bloque": bloque,
            "opt_in": opt_in})
