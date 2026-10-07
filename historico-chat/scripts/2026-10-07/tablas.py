# -*- coding: utf-8 -*-
"""EP-028·HU-006 · Convierte las tablas de historia, versiones, reportes y propuestas
al patrón de tabla avanzada de Tabler. Se corre desde `proyectos/cimiento/core/`;
cada reemplazo falla si el texto de origen no está tal cual."""
import io


def rep(p, pares):
    t = io.open(p, encoding="utf-8").read()
    for a, b in pares:
        assert a in t, (p, a[:60])
        t = t.replace(a, b, 1)
    io.open(p, "w", encoding="utf-8").write(t)


def orden(campo, titulo):
    return '<th><button type="button" class="table-sort" data-sort="%s">%s</button></th>' % (campo, titulo)


def filtro(campo, que):
    return ('<th><input type="search" class="form-control form-control-sm" placeholder="Filtrar" '
            'aria-label="Filtrar por %s" data-filtro="%s"></th>' % (que, campo))


def lista(campo, que, todos="Todos"):
    return ('<th><select class="form-select form-select-sm" aria-label="Filtrar por %s" data-filtro="%s" data-exacto>'
            '<option value="">%s</option></select></th>' % (que, campo, todos))


VACIA = "<th></th>"
NOTA = '{% comment %}`EP-028·HU-006` · Ordena y filtra lo que se ve; la base ya pagina (guía §6).{% endcomment %}'

rep("historia/templates/historia/lista.html", [
    ('<div class="card">\n  <table class="table card-table table-vcenter">\n    <thead>\n      <tr><th>#</th><th>Fecha</th><th>Quién</th>'
     '<th>Tabla</th><th>Fila</th><th>Acción</th><th>Antes</th><th>Después</th><th>Por qué</th><th>Versión</th><th></th></tr>\n'
     '    </thead>\n    <tbody>',
     '<div class="card">\n  ' + NOTA + '\n  <div id="tabla-historia" data-tabla-avanzada data-por-pagina="0">\n'
     '  <div class="table-responsive">\n  <table class="table card-table table-vcenter">\n    <thead>\n      <tr>'
     + orden("t-numero", "#") + orden("t-fecha", "Fecha") + orden("t-quien", "Quién") + orden("t-tabla", "Tabla")
     + orden("t-fila", "Fila") + orden("t-accion", "Acción") + "<th>Antes</th><th>Después</th>"
     + orden("t-motivo", "Por qué") + orden("t-version", "Versión") + VACIA + "</tr>\n      <tr>"
     + VACIA * 2 + filtro("t-quien", "quién") + VACIA * 5 + filtro("t-motivo", "motivo") + VACIA * 2
     + '</tr>\n    </thead>\n    <tbody class="table-tbody">'),
    ('        <td>{{ cambio.pk }}</td>\n        <td>{{ cambio.fecha|date:"Y-m-d H:i" }}</td>\n'
     '        <td>{{ cambio.quien_lo_hizo }}</td>\n        <td><code>{{ cambio.tabla }}</code></td>\n'
     '        <td>{{ cambio.fila }}</td>\n        <td>{{ cambio.get_accion_display }}</td>',
     '        <td class="t-numero">{{ cambio.pk }}</td>\n        <td class="t-fecha">{{ cambio.fecha|date:"Y-m-d H:i" }}</td>\n'
     '        <td class="t-quien">{{ cambio.quien_lo_hizo }}</td>\n        <td class="t-tabla"><code>{{ cambio.tabla }}</code></td>\n'
     '        <td class="t-fila">{{ cambio.fila }}</td>\n        <td class="t-accion">{{ cambio.get_accion_display }}</td>'),
    ('        <td>{{ cambio.motivo }}{% if cambio.deshace %}', '        <td class="t-motivo">{{ cambio.motivo }}{% if cambio.deshace %}'),
    ('        <td>{% if cambio.version %}{{ cambio.version }}{% endif %}</td>',
     '        <td class="t-version">{% if cambio.version %}{{ cambio.version }}{% endif %}</td>'),
    ('      {% empty %}\n      <tr><td colspan="11" class="text-secondary">Todavía no hay cambios.</td></tr>\n'
     '      {% endfor %}\n    </tbody>\n  </table>\n</div>',
     '      {% endfor %}\n    </tbody>\n  </table>\n  </div>\n'
     '  {% if not pagina %}<div class="empty py-4"><p class="empty-title">Todavía no hay cambios</p></div>{% endif %}\n'
     '  <div class="card-body text-secondary" data-sin-coincidencias hidden>Ningún cambio de esta página coincide con los filtros.</div>\n'
     '  </div>\n</div>'),
])

rep("historia/templates/historia/versiones.html", [
    ('<div class="card">\n  <table class="table card-table table-vcenter">\n    <thead><tr><th>De</th><th>Versión</th><th>Tipo</th>'
     '<th>Fecha</th><th>Quién</th><th>Por qué</th><th>Cambios</th></tr></thead>\n    <tbody>',
     '<div class="card">\n  ' + NOTA + '\n  <div id="tabla-versiones" data-tabla-avanzada data-por-pagina="0">\n'
     '  <div class="table-responsive">\n  <table class="table card-table table-vcenter">\n    <thead><tr>'
     + orden("t-de", "De") + orden("t-numero", "Versión") + orden("t-tipo", "Tipo") + orden("t-fecha", "Fecha")
     + orden("t-quien", "Quién") + orden("t-motivo", "Por qué") + "<th>Cambios</th></tr>\n      <tr>"
     + VACIA * 2 + lista("t-tipo", "tipo") + VACIA * 2 + filtro("t-motivo", "motivo") + VACIA
     + '</tr></thead>\n    <tbody class="table-tbody">'),
    ('        <td>{% if version.proyecto %}{{ version.proyecto }}{% else %}Estándar{% endif %}</td>\n'
     '        <td><strong>{{ version.numero }}</strong></td>\n        <td>{{ version.get_tipo_display }}</td>\n'
     '        <td>{{ version.fecha|date:"Y-m-d H:i" }}</td>\n        <td>{% if version.cuenta %}',
     '        <td class="t-de">{% if version.proyecto %}{{ version.proyecto }}{% else %}Estándar{% endif %}</td>\n'
     '        <td class="t-numero"><strong>{{ version.numero }}</strong></td>\n        <td class="t-tipo">{{ version.get_tipo_display }}</td>\n'
     '        <td class="t-fecha">{{ version.fecha|date:"Y-m-d H:i" }}</td>\n        <td class="t-quien">{% if version.cuenta %}'),
    ('        <td>{{ version.resumen }}</td>', '        <td class="t-motivo">{{ version.resumen }}</td>'),
    ('      {% empty %}\n      <tr><td colspan="7" class="text-secondary">Todavía no hay versiones guardadas.</td></tr>\n'
     '      {% endfor %}\n    </tbody>\n  </table>\n</div>',
     '      {% endfor %}\n    </tbody>\n  </table>\n  </div>\n'
     '  {% if not pagina %}<div class="empty py-4"><p class="empty-title">Todavía no hay versiones guardadas</p></div>{% endif %}\n'
     '  <div class="card-body text-secondary" data-sin-coincidencias hidden>Ninguna versión de esta página coincide con los filtros.</div>\n'
     '  </div>\n</div>'),
])

rep("estandar/templates/estandar/reportes.html", [
    ('<div class="card"><table class="table card-table">\n  <thead><tr><th>#</th><th>Proyecto</th><th>Qué</th><th>Cómo quedó</th>'
     '<th>Quién</th><th>Avisado</th></tr></thead>\n  <tbody>{% for r in resueltos %}<tr><td>{{ r.pk }}</td><td>{{ r.proyecto }}</td>'
     '<td>{{ r.titulo }}</td>\n    <td>{% if r.corregido_en %}',
     '<div class="card" id="tabla-reportes" data-tabla-avanzada data-por-pagina="10"><div class="table-responsive">'
     '<table class="table card-table table-vcenter">\n  <thead><tr>'
     + orden("t-proyecto", "Proyecto") + orden("t-que", "Qué") + orden("t-como", "Cómo quedó") + orden("t-quien", "Quién")
     + orden("t-avisado", "Avisado") + "</tr>\n  <tr>" + lista("t-proyecto", "proyecto") + filtro("t-que", "lo reportado")
     + VACIA * 3 + '</tr></thead>\n  <tbody class="table-tbody">{% for r in resueltos %}<tr><td class="t-proyecto">{{ r.proyecto }}</td>'
     '<td class="t-que">{{ r.titulo }}</td>\n    <td class="t-como">{% if r.corregido_en %}'),
    ('    <td>{{ r.resuelto_por.get_username|default:"" }}</td><td>{% if r.avisado %}Sí{% else %}No{% endif %}</td></tr>{% endfor %}</tbody>\n'
     '</table></div>',
     '    <td class="t-quien">{{ r.resuelto_por.get_username|default:"" }}</td><td class="t-avisado">{% if r.avisado %}Sí{% else %}No{% endif %}</td></tr>'
     '{% endfor %}</tbody>\n</table></div>\n<div class="card-body text-secondary" data-sin-coincidencias hidden>Ningún reporte coincide con los filtros.</div>\n'
     '{% include "includes/tabla_pie.html" with tabla="tabla-reportes" %}</div>'),
])

rep("estandar/templates/estandar/propuestas.html", [
    ('<div class="card"><div class="table-responsive"><table class="table table-vcenter card-table">\n'
     '  <thead><tr><th>Qué</th><th>Quién propuso</th><th>Cómo quedó</th><th>Quién resolvió</th><th>Cuándo</th></tr></thead>\n'
     '  <tbody>{% for p in resueltas %}<tr>\n    <td>{{ p.get_accion_display }}: {{ p.destino }}</td><td>{{ p.quien }}</td>\n'
     '    <td><span class="badge ',
     '<div class="card" id="tabla-propuestas" data-tabla-avanzada data-por-pagina="10"><div class="table-responsive">'
     '<table class="table table-vcenter card-table">\n  <thead><tr>'
     + orden("t-que", "Qué") + orden("t-quien", "Quién propuso") + orden("t-estado", "Cómo quedó")
     + orden("t-resolvio", "Quién resolvió") + orden("t-cuando", "Cuándo") + "</tr>\n  <tr>"
     + filtro("t-que", "lo propuesto") + VACIA + lista("t-estado", "cómo quedó", "Todas") + VACIA * 2
     + '</tr></thead>\n  <tbody class="table-tbody">{% for p in resueltas %}<tr>\n'
     '    <td class="t-que">{{ p.get_accion_display }}: {{ p.destino }}</td><td class="t-quien">{{ p.quien }}</td>\n'
     '    <td><span class="badge t-estado '),
    ('    <td>{{ p.resuelta_por.get_username|default:"" }}</td><td>{{ p.resuelta|date:"Y-m-d H:i" }}</td>\n'
     '  </tr>{% endfor %}</tbody>\n</table></div></div>',
     '    <td class="t-resolvio">{{ p.resuelta_por.get_username|default:"" }}</td><td class="t-cuando">{{ p.resuelta|date:"Y-m-d H:i" }}</td>\n'
     '  </tr>{% endfor %}</tbody>\n</table></div>\n'
     '<div class="card-body text-secondary" data-sin-coincidencias hidden>Ninguna propuesta coincide con los filtros.</div>\n'
     '{% include "includes/tabla_pie.html" with tabla="tabla-propuestas" %}</div>'),
])
print("listo")
