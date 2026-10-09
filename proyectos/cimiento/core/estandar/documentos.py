# -*- coding: utf-8 -*-
"""`EP-030·HU-001` · Un solo camino para leer y escribir los documentos de Cimiento.

**Cada tipo se registra una vez** con su modelo, los campos que lo identifican y
el campo con su texto. Todo programa que lea o escriba un documento pasa por
aquí: `listar`, `ver` y `proponer`. Cada HU de la EP-030 que pase un tipo a la
base lo registra en `TIPOS`, y el comando `manage.py documento` lo sirve sin
escribir un guion nuevo.

**Escribir es proponer** (análisis 1 del pendiente 142, acuerdo 5). Crear,
editar o quitar deja una `Propuesta`; nada cambia hasta que se aprueba en
«Estándar → Propuestas», y al aprobarse la historia guarda el antes y el
después en `Cambio`.
"""
import os

from core.historia.registro import quien_y_por_que

from .cambios import CambioInvalido, accion_para, ruta_valida
from .models import DOCUMENTO, QUITAR, RECUERDO, Documento, Propuesta, Recuerdo

CREAR, EDITAR, QUITAR_ = "crear", "editar", "quitar"


class TipoDesconocido(CambioInvalido):
    pass


class Tipo:
    """Un tipo de documento: cómo se busca, cómo se lista y cómo se propone."""

    nombre = ""
    descripcion = ""
    objeto = ""          # el de la `Propuesta`
    pide_proyecto = False

    def consulta(self, proyecto=None):
        raise NotImplementedError

    def buscar(self, clave, proyecto=None):
        raise NotImplementedError

    def clave_de(self, fila):
        raise NotImplementedError

    def texto_de(self, fila):
        return fila.contenido

    def datos_de_propuesta(self, clave, proyecto=None):
        raise NotImplementedError

    # `EP-030·HU-002` · La pantalla de propuestas le pregunta al tipo: así
    # muestra y aprueba cualquier tipo registrado sin código aparte.

    def actual(self, propuesta):
        """El texto que hay hoy donde la propuesta cambia; "" si es nuevo."""
        raise NotImplementedError

    def aplicar(self, propuesta, raiz=None):
        """Hace lo que la propuesta pide. Lo llama `cambios.aplicar`, ya aprobada."""
        raise NotImplementedError


class DelEstandar(Tipo):
    nombre = "estandar"
    descripcion = "documento del estándar (base/…)"
    objeto = DOCUMENTO

    def consulta(self, proyecto=None):
        return Documento.objects.all()

    def filtrar(self, consulta, inicio):
        return consulta.filter(ruta__startswith=inicio) if inicio else consulta

    def buscar(self, clave, proyecto=None):
        return Documento.objects.filter(ruta=_ruta(clave)).first()

    def clave_de(self, fila):
        return fila.ruta

    def datos_de_propuesta(self, clave, proyecto=None):
        return {"ruta": ruta_valida(_ruta(clave))}

    def actual(self, propuesta):
        fila = Documento.objects.filter(ruta=propuesta.ruta).only("contenido").first()
        return fila.contenido if fila else ""

    def aplicar(self, propuesta, raiz=None):
        from .cambios import guardar_documento, quitar_documento

        if propuesta.accion == QUITAR:
            documento = Documento.objects.filter(ruta=propuesta.ruta).first()
            if documento is None:
                raise CambioInvalido("el documento ya no existe")
            quitar_documento(documento, raiz)
        else:
            guardar_documento(propuesta.ruta, propuesta.contenido, raiz)


class DeLaMemoria(Tipo):
    nombre = "recuerdo"
    descripcion = "recuerdo de la memoria de un proyecto"
    objeto = RECUERDO
    pide_proyecto = True

    def consulta(self, proyecto=None):
        return Recuerdo.objects.filter(proyecto=proyecto)

    def filtrar(self, consulta, inicio):
        return consulta.filter(nombre__startswith=inicio) if inicio else consulta

    def buscar(self, clave, proyecto=None):
        return Recuerdo.objects.filter(proyecto=proyecto, nombre=clave).first()

    def clave_de(self, fila):
        return fila.nombre

    def datos_de_propuesta(self, clave, proyecto=None):
        return {"proyecto": proyecto, "nombre": clave}

    def actual(self, propuesta):
        fila = Recuerdo.objects.filter(proyecto=propuesta.proyecto, nombre=propuesta.nombre).only("contenido").first()
        return fila.contenido if fila else ""

    def aplicar(self, propuesta, raiz=None):
        from .cambios import guardar_recuerdo

        if propuesta.accion == QUITAR:
            Recuerdo.objects.filter(proyecto=propuesta.proyecto, nombre=propuesta.nombre).delete()
        else:
            guardar_recuerdo(propuesta.proyecto, propuesta.nombre, propuesta.contenido)


TIPOS = {t.nombre: t for t in (DelEstandar(), DeLaMemoria())}


def de_la_propuesta(propuesta):
    """El tipo que atiende la propuesta, por su `objeto`."""
    for t in TIPOS.values():
        if t.objeto == propuesta.objeto:
            return t
    raise TipoDesconocido("ningún tipo atiende las propuestas de «%s»" % propuesta.objeto)


def _ruta(clave):
    return (clave or "").replace("\\", "/").strip()


def tipo(nombre):
    if nombre not in TIPOS:
        raise TipoDesconocido("no hay un tipo «%s»; los que hay: %s" % (nombre, ", ".join(sorted(TIPOS))))
    return TIPOS[nombre]


def proyecto_de(ruta):
    """El proyecto registrado en esa carpeta, o error."""
    from core.proyectos.models import Proyecto

    registrado = Proyecto.objects.filter(ruta__iexact=os.path.abspath(ruta or "")).first()
    if registrado is None:
        raise CambioInvalido("el proyecto %s no está registrado en Cimiento" % ruta)
    return registrado


def listar(nombre, inicio="", proyecto=None):
    """Las claves de los documentos de ese tipo que empiezan por `inicio`."""
    t = tipo(nombre)
    return [t.clave_de(f) for f in t.filtrar(t.consulta(proyecto), inicio)]


def ver(nombre, clave, proyecto=None):
    """El texto del documento, o error si no está."""
    t = tipo(nombre)
    fila = t.buscar(clave, proyecto)
    if fila is None:
        raise CambioInvalido("%s no está en %s" % (clave, t.descripcion))
    return t.texto_de(fila)


def proponer(nombre, accion, clave, contenido="", motivo="", quien="agente", proyecto=None):
    """Deja la propuesta de crear, editar o quitar un documento. Devuelve la `Propuesta`.

    Con `accion=None` decide sola entre crear y editar, según exista: es lo que
    hacía `manage.py proponer`, que sigue igual para quien ya lo usa.
    """
    t = tipo(nombre)
    if not (motivo or "").strip():
        raise CambioInvalido("falta el motivo")
    existe = t.buscar(clave, proyecto) is not None
    if accion == CREAR and existe:
        raise CambioInvalido("%s ya existe: se edita" % clave)
    if accion == EDITAR and not existe:
        raise CambioInvalido("%s no existe: se crea" % clave)
    if accion == QUITAR_ and not existe:
        raise CambioInvalido("no hay qué quitar")
    datos = t.datos_de_propuesta(clave, proyecto)
    datos.update(objeto=t.objeto, accion=accion_para(t.objeto, existe, accion == QUITAR_),
                 contenido="" if accion == QUITAR_ else contenido, motivo=motivo, quien=quien)
    with quien_y_por_que(quien=quien, motivo=motivo):
        return Propuesta.objects.create(**datos)
