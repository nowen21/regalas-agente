# -*- coding: utf-8 -*-
"""`EP-028·HU-003` · Lo que espera una decisión, en toda pantalla.

El menú y el inicio muestran cuántas propuestas y cuántos reportes esperan a
quien administra (`17·I7`; guía de diseño de pantallas, §4). Una sola fuente
para los dos: un procesador de contexto, con dos consultas por página.

Si la base no responde, no se cuenta nada: de avisarlo se encarga la pantalla
de base apagada, no el menú.
"""
from django.db import DatabaseError


def pendientes(peticion):
    usuario = getattr(peticion, "user", None)
    if usuario is None or not usuario.is_authenticated:
        return {}
    from core.estandar.models import ABIERTO, PENDIENTE, Propuesta, Reporte

    try:
        propuestas = Propuesta.objects.filter(estado=PENDIENTE).count()
        reportes = Reporte.objects.filter(estado=ABIERTO).count()
    except DatabaseError:
        return {}
    from core.cuentas.permisos import es_administrador

    # `EP-028·HU-004` · El menú no ofrece a una cuenta de consulta lo que no puede hacer.
    return {"pendientes": {"propuestas": propuestas, "reportes": reportes, "total": propuestas + reportes},
            "administra": es_administrador(usuario)}
