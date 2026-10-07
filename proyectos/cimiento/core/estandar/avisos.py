# -*- coding: utf-8 -*-
"""`EP-026·HU-008` · Lo que se le avisa a un proyecto de los reportes que hizo.

**Sin Django**: lo pide el arranque de sesión. Cada reporte resuelto se avisa
una sola vez: después de decirlo, queda marcado como avisado. Sin base o sin
registro, no se dice nada: el arranque no se puede caer por esto.
"""
from ..enganches.estado_en_base import EstadoEnBase
from ..enganches.niveles import BaseSinRespuesta, NivelesDelProyecto

_RESUELTOS = ("SELECT r.id, r.titulo, r.estado, v.mayor, v.menor, v.parche, r.motivo "
              "FROM estandar_reporte r JOIN proyectos_proyecto p ON p.id = r.proyecto_id "
              "LEFT JOIN historia_version v ON v.id = r.corregido_en_id "
              "WHERE p.activo = 1 AND LOWER(p.ruta) = LOWER(%s) AND r.estado <> 'abierto' AND r.avisado = 0")


def de_los_reportes(raiz, ajustes=None):
    """El texto del aviso, o "" si no hay nada que avisar. Marca lo avisado."""
    niveles = NivelesDelProyecto(raiz, ajustes=ajustes)
    try:
        filas = niveles.consultar(_RESUELTOS)
    except BaseSinRespuesta:
        return ""
    if not filas:
        return ""
    lineas = []
    for id_, titulo, estado, mayor, menor, parche, motivo in filas:
        if estado == "corregido":
            lineas.append("- El reporte %d, «%s», quedó corregido en la versión %s.%s.%s del estándar."
                          % (id_, titulo, mayor, menor, parche))
        else:
            lineas.append("- El reporte %d, «%s», se descartó: %s" % (id_, titulo, motivo or "sin motivo"))
    # El cambio de la marca también queda en la historia (`EP-026·HU-001`).
    base = EstadoEnBase(raiz, ajustes=ajustes)
    try:
        for f in filas:
            base.ejecutar("UPDATE estandar_reporte SET avisado = 1 WHERE id = %s", [f[0]], escribir=True)
            base.ejecutar("INSERT INTO historia_cambio (fecha, quien, tabla, fila, accion, antes, despues, motivo) "
                          "VALUES (UTC_TIMESTAMP(6), 'arranque', 'estandar.reporte', %s, 'cambiar', %s, %s, %s)",
                          [str(f[0]), '{"avisado": false}', '{"avisado": true}',
                           "El proyecto se enteró al abrir su sesión"], escribir=True)
    except BaseSinRespuesta:
        pass
    return "[REPORTES DE ESTE PROYECTO AL ESTÁNDAR]\n" + "\n".join(lineas)
