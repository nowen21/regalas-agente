# -*- coding: utf-8 -*-
"""`EP-026·HU-001` · Quién cambia qué y por qué, y el registro de cada cambio.

**Quién y por qué viajan con el hilo.** El middleware pone la cuenta de cada
petición; un programa usa `quien_y_por_que`. Sin nada de eso, el cambio queda a
nombre del programa que corre (`manage.py <orden>`).

**Las señales cubren toda tabla**, menos las de `FUERA`: las de Django que no
son datos, el gasto que se trae de Claude Code y la historia misma.

**Nada sale en claro** (`00·N6`): la contraseña queda como «cambiada» y todo
texto pasa por el tapado de claves antes de guardarse.
"""
import json
import os
import sys
import threading
from contextlib import contextmanager

from django.core.serializers.json import DjangoJSONEncoder
from django.db import models, transaction
from django.db.models.signals import m2m_changed, post_delete, post_save, pre_save

from core.enganches.enmascarar import Enmascarador

from . import versiones
from .models import BORRAR, CAMBIAR, CREAR, Cambio

# Lo que no entra a la historia: tablas de Django que no son datos, el gasto
# (cada fila ya es su historia y nunca se edita) y la historia misma.
FUERA_APPS = {"historia", "consumo", "sessions", "contenttypes", "admin", "migrations"}
FUERA_TABLAS = {"auth.permission"}
CAMBIADA = "«cambiada»"
_SECRETOS = {"password"}

_hilo = threading.local()


def _programa():
    args = [os.path.basename(a) for a in sys.argv[:2]]
    return " ".join(args) or "programa"


def actual():
    """`(cuenta, quien, motivo)` de lo que corre ahora."""
    return (getattr(_hilo, "cuenta", None), getattr(_hilo, "quien", None) or _programa(),
            getattr(_hilo, "motivo", ""))


@contextmanager
def quien_y_por_que(cuenta=None, quien=None, motivo="", tipo=None):
    """Lo que se guarde adentro queda a nombre de `cuenta` (o de `quien`) y con
    `motivo`. Lo que lleve versión sube una sola por ámbito, del `tipo` dado
    (`EP-026·HU-002`)."""
    previo = (getattr(_hilo, "cuenta", None), getattr(_hilo, "quien", None), getattr(_hilo, "motivo", ""),
              getattr(_hilo, "tipo", None), getattr(_hilo, "versiones", None))
    _hilo.cuenta = cuenta if cuenta is not None and getattr(cuenta, "is_authenticated", False) else None
    _hilo.quien = quien or ("cuenta" if _hilo.cuenta else previo[1])
    _hilo.motivo = motivo or previo[2]
    _hilo.tipo = tipo or previo[3]
    _hilo.versiones = {}
    try:
        yield
    finally:
        _hilo.cuenta, _hilo.quien, _hilo.motivo, _hilo.tipo, _hilo.versiones = previo


@contextmanager
def en_version(version):
    """`EP-026·HU-003` · Lo que se guarde adentro, del ámbito de `version`, va a
    esa versión y no sube otra. Va dentro de `quien_y_por_que`."""
    abiertas = getattr(_hilo, "versiones", None)
    if abiertas is None:
        raise RuntimeError("en_version va dentro de quien_y_por_que")
    clave = (version.ambito, version.proyecto_id)
    previa = abiertas.get(clave)
    abiertas[clave] = version
    try:
        yield
    finally:
        if previa is None:
            abiertas.pop(clave, None)
        else:
            abiertas[clave] = previa


def etiqueta(modelo):
    return "%s.%s" % (modelo._meta.app_label, modelo._meta.model_name)


def se_registra(modelo):
    return modelo._meta.app_label not in FUERA_APPS and etiqueta(modelo) not in FUERA_TABLAS


def _automaticos(modelo):
    """Los campos que se llenan solos al guardar: no son un cambio."""
    return {f.attname for f in modelo._meta.concrete_fields
            if getattr(f, "auto_now", False) or getattr(f, "auto_now_add", False)}


def _limpio(campo, valor):
    if campo in _SECRETOS:
        return CAMBIADA
    valor = json.loads(json.dumps(valor, cls=DjangoJSONEncoder))
    if isinstance(valor, str):
        return Enmascarador.enmascarar(valor)[0]
    return valor


def foto(instancia):
    """`{campo: valor}` de los campos de la fila, sin los automáticos."""
    modelo = type(instancia)
    fuera = _automaticos(modelo)
    return {f.attname: getattr(instancia, f.attname) for f in modelo._meta.concrete_fields
            if f.attname not in fuera}


_lista = False


def _tabla_lista():
    """¿Ya existe la tabla de la historia? Las migraciones de datos de otros
    módulos corren antes que la de la historia y no tienen dónde anotar."""
    global _lista
    if not _lista:
        from django.db import connection

        _lista = Cambio._meta.db_table in connection.introspection.table_names()
    return _lista


def anotar(tabla, fila, accion, antes=None, despues=None, deshace=None, completa=None):
    """Escribe un cambio con quién y por qué de lo que corre ahora. `completa` es
    la fila entera, de donde sale a qué proyecto pertenece (`EP-026·HU-002`)."""
    if not _tabla_lista():
        return None
    cuenta, quien, motivo = actual()
    datos = completa if completa is not None else (despues if despues is not None else antes)
    version = _version(tabla, fila, datos, cuenta, quien, motivo)
    return Cambio.objects.create(version=version,
        cuenta=cuenta, quien=quien, tabla=tabla, fila=str(fila), accion=accion,
        antes={k: _limpio(k, v) for k, v in antes.items()} if antes is not None else None,
        despues={k: _limpio(k, v) for k, v in despues.items()} if despues is not None else None,
        motivo=Enmascarador.enmascarar(motivo or "")[0], deshace=deshace)


def _version(tabla, fila, datos, cuenta, quien, motivo):
    """`EP-026·HU-002` · La versión que sube este cambio, o None si no lleva."""
    ambito = versiones.ambito_de(tabla, fila, datos)
    if ambito is None:
        return None
    abiertas = getattr(_hilo, "versiones", None)
    if abiertas is not None and ambito in abiertas:
        return abiertas[ambito]
    tipo = getattr(_hilo, "tipo", None) or versiones.PARCHE
    version = versiones.nueva(ambito[0], ambito[1], tipo, Enmascarador.enmascarar(motivo or "")[0], cuenta, quien)
    if abiertas is not None:
        abiertas[ambito] = version
    return version


# ── las señales ───────────────────────────────────────────────────────────

def _antes_de_guardar(sender, instance, raw=False, **_):
    if raw or not se_registra(sender) or instance.pk is None:
        instance._historia_antes = None
        return
    previa = sender._base_manager.filter(pk=instance.pk).first()
    instance._historia_antes = foto(previa) if previa else None


def _despues_de_guardar(sender, instance, created, raw=False, **_):
    if raw or not se_registra(sender):
        return
    ahora = foto(instance)
    antes = getattr(instance, "_historia_antes", None)
    if created or antes is None:
        anotar(etiqueta(sender), instance.pk, CREAR, despues=ahora)
        return
    cambiados = sorted(k for k in ahora if ahora[k] != antes.get(k))
    if not cambiados:
        return
    anotar(etiqueta(sender), instance.pk, CAMBIAR,
           antes={k: antes.get(k) for k in cambiados}, despues={k: ahora[k] for k in cambiados}, completa=ahora)


def _despues_de_borrar(sender, instance, **_):
    if se_registra(sender):
        anotar(etiqueta(sender), instance.pk, BORRAR, antes=foto(instance))


def _relacion(sender, instance, action, model, pk_set, reverse=False, **_):
    """Agregar o quitar en una relación de muchos a muchos (una cuenta en un grupo)."""
    if action not in ("post_add", "post_remove", "post_clear") or not se_registra(type(instance)):
        return
    campo = [f.name for f in type(instance)._meta.many_to_many if f.remote_field.through is sender]
    nombre = campo[0] if campo else etiqueta(model)
    ids = sorted(pk_set or [])
    if action == "post_add":
        anotar(etiqueta(type(instance)), instance.pk, CAMBIAR, despues={nombre + "+": ids}, completa=foto(instance))
    else:
        anotar(etiqueta(type(instance)), instance.pk, CAMBIAR, antes={nombre + "-": ids or "todos"},
               completa=foto(instance))


def conectar():
    pre_save.connect(_antes_de_guardar, dispatch_uid="historia_antes")
    post_save.connect(_despues_de_guardar, dispatch_uid="historia_despues")
    post_delete.connect(_despues_de_borrar, dispatch_uid="historia_borrar")
    m2m_changed.connect(_relacion, dispatch_uid="historia_relacion")


# ── deshacer ──────────────────────────────────────────────────────────────

class NoSeDeshace(Exception):
    """El cambio no se puede deshacer; el mensaje dice por qué."""


def _modelo(tabla):
    from django.apps import apps

    app, nombre = tabla.split(".")
    return apps.get_model(app, nombre)


def deshacer(cambio, cuenta, motivo=""):
    """Devuelve la fila a como estaba antes de `cambio`. Deja un cambio nuevo."""
    if cambio.deshecho_por.exists():
        raise NoSeDeshace("ese cambio ya se deshizo")
    if any(k.endswith(("+", "-")) for k in list((cambio.antes or {})) + list((cambio.despues or {}))):
        raise NoSeDeshace("los cambios de pertenencia a un grupo se deshacen en la cuenta")
    if CAMBIADA in (cambio.antes or {}).values():
        raise NoSeDeshace("una contraseña no se devuelve: se cambia otra vez")
    modelo = _modelo(cambio.tabla)
    texto = "deshace el cambio %d" % cambio.pk + (": %s" % motivo if motivo else "")
    with transaction.atomic(), quien_y_por_que(cuenta=cuenta, motivo=texto):
        if cambio.accion == CREAR:
            fila = modelo._base_manager.filter(pk=cambio.fila).first()
            if fila is None:
                raise NoSeDeshace("la fila ya no existe")
            fila.delete()
        elif cambio.accion == CAMBIAR:
            fila = modelo._base_manager.filter(pk=cambio.fila).first()
            if fila is None:
                raise NoSeDeshace("la fila ya no existe")
            for campo, valor in (cambio.antes or {}).items():
                setattr(fila, campo, _a_python(modelo, campo, valor))
            fila.save()
        else:
            datos = {campo: _a_python(modelo, campo, valor) for campo, valor in (cambio.antes or {}).items()}
            modelo._base_manager.create(**datos)
        nuevo = Cambio.objects.filter(tabla=cambio.tabla, fila=str(cambio.fila)).order_by("-id").first()
        if nuevo and nuevo.pk > cambio.pk and nuevo.deshace_id is None:
            nuevo.deshace = cambio
            Cambio.objects.filter(pk=nuevo.pk).update(deshace=cambio)
        return nuevo


def _a_python(modelo, campo, valor):
    for f in modelo._meta.concrete_fields:
        if f.attname == campo:
            return f.to_python(valor) if not isinstance(f, models.ForeignKey) else valor
    return valor
