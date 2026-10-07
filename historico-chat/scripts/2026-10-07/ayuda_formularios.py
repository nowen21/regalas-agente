# -*- coding: utf-8 -*-
"""EP-028·HU-005 · Pone el «?» de cada campo y la ayuda de cada pantalla en los
formularios de Cimiento. Se corre desde `proyectos/cimiento/`. Si una plantilla ya
tiene su ayuda de pantalla, no la repite; los reemplazos fallan si el texto no está."""
import io

CARGA = "{% load ayuda %}"


def cambiar(ruta, pares, pantalla=None, despues_de="{% block contenido %}"):
    t = io.open(ruta, encoding="utf-8").read()
    if CARGA not in t:
        i = t.index("\n") + 1 if t.startswith("{% extends") else 0
        t = t[:i] + CARGA + "\n" + t[i:]
    if pantalla and "ayuda_pantalla" not in t:
        assert despues_de in t, (ruta, despues_de)
        t = t.replace(despues_de, despues_de + '\n{% ayuda_pantalla "' + pantalla + '" %}', 1)
    for a, b in pares:
        assert a in t, (ruta, a)
        t = t.replace(a, b, 1)
    io.open(ruta, "w", encoding="utf-8").write(t)


def ayuda(clave):
    return '{% ayuda_campo "' + clave + '" %}'


def etiqueta(para, texto, clave, extra=""):
    """La etiqueta de un campo con su «?» al lado."""
    return ('<div class="d-flex align-items-center gap-1 mb-1"><label class="form-label mb-0%s" for="%s">%s</label>'
            % (extra, para, texto)) + ayuda(clave) + '</div>'


T = "core/%s/templates/%s/%s.html"

cambiar("core/cuentas/templates/cuentas/entrar.html", [
    ('<label class="form-label" for="id_username">Usuario</label>', etiqueta("id_username", "Usuario", "entrar.usuario")),
    ('<label class="form-label" for="id_password">Contraseña</label>', etiqueta("id_password", "Contraseña", "entrar.clave")),
])

SELECT_PROYECTO = '<select class="form-select" name="proyecto" aria-label="Proyecto" onchange="this.form.submit()">'
SELECT_DIAS = '<select class="form-select" name="dias" aria-label="Período" onchange="this.form.submit()">'
FIN = "{% endfor %}\n    </select>\n  </div>"
cambiar(T % ("consumo", "consumo", "tablero"), [
    (SELECT_PROYECTO, '<div class="d-flex align-items-center gap-1">' + SELECT_PROYECTO),
    (FIN, "{% endfor %}\n    </select>" + ayuda("gasto.proyecto") + "</div>\n  </div>"),
    (SELECT_DIAS, '<div class="d-flex align-items-center gap-1">' + SELECT_DIAS),
    (FIN, "{% endfor %}\n    </select>" + ayuda("gasto.dias") + "</div>\n  </div>"),
], pantalla="gasto")

cambiar(T % ("estandar", "estandar", "documento"), [
    ('<label class="form-label" for="ruta">Ruta</label>', etiqueta("ruta", "Ruta", "documento.ruta")),
    ('<label class="form-label" for="contenido">Texto</label>', etiqueta("contenido", "Texto", "documento.texto")),
], pantalla="documento")

cambiar(T % ("estandar", "estandar", "git"), [
    ('<label class="form-label" for="asunto-{{ forloop.counter }}">Asunto</label>',
     etiqueta("asunto-{{ forloop.counter }}", "Asunto", "git.asunto")),
    ('<label class="form-label" for="idea-{{ forloop.counter }}">La idea del usuario</label>',
     etiqueta("idea-{{ forloop.counter }}", "La idea del usuario", "git.idea")),
    ('<label class="form-label" for="hecho-{{ forloop.counter }}">Lo que hizo el agente</label>',
     etiqueta("hecho-{{ forloop.counter }}", "Lo que hizo el agente", "git.hecho")),
    ('name="subir" value="1"> Subir también</label>', 'name="subir" value="1"> Subir también ' + ayuda("git.subir") + '</label>'),
], pantalla="git")

cambiar(T % ("estandar", "estandar", "lista"), [
    ('placeholder="Buscar en el estándar">', 'placeholder="Buscar en el estándar">' + ayuda("estandar.buscar")),
], pantalla="estandar")

cambiar(T % ("estandar", "estandar", "recuerdo"), [
    ('<label class="form-label" for="nombre">Nombre</label>', etiqueta("nombre", "Nombre", "recuerdo.nombre")),
    ('<label class="form-label" for="contenido">Texto</label>', etiqueta("contenido", "Texto", "recuerdo.texto")),
], pantalla="recuerdo")

cambiar(T % ("estandar", "estandar", "reportes"), [
    ('<select class="form-select form-select-sm w-auto" name="version" required>',
     ayuda("reporte.version") + '<select class="form-select form-select-sm w-auto" name="version" required>'),
    ('name="motivo" placeholder="Por qué se descarta" required>',
     'name="motivo" placeholder="Por qué se descarta" required>' + ayuda("reporte.motivo")),
    ('<label class="form-label" for="proyecto">Proyecto</label>', etiqueta("proyecto", "Proyecto", "reporte.proyecto")),
    ('<label class="form-label" for="titulo">Qué pasa</label>', etiqueta("titulo", "Qué pasa", "reporte.titulo")),
    ('<label class="form-label" for="regla">La regla que toca, si hay una</label>',
     etiqueta("regla", "La regla que toca, si hay una", "reporte.regla")),
    ('<label class="form-label" for="texto">Detalle</label>', etiqueta("texto", "Detalle", "reporte.texto")),
], pantalla="reportes")

cambiar(T % ("estandar", "estandar", "vista_previa"), [
    ('<label class="form-label" for="proyecto">Proyecto</label>', etiqueta("proyecto", "Proyecto", "vista_previa.proyecto")),
    ('<label class="form-label" for="mensaje">Mensaje</label>', etiqueta("mensaje", "Mensaje", "vista_previa.mensaje")),
], pantalla="vista_previa")

cambiar(T % ("estandar", "estandar", "propuestas"), [
    ('<label class="form-label required" for="rechazo-{{ p.pk }}">Si no se aprueba, por qué</label>',
     etiqueta("rechazo-{{ p.pk }}", "Si no se aprueba, por qué", "propuesta.rechazo", " required")),
], pantalla="propuestas")

cambiar(T % ("historia", "historia", "lista"), [
    ('<select class="form-select form-select-sm w-auto" name="tabla">',
     ayuda("historia.tabla") + '<select class="form-select form-select-sm w-auto" name="tabla">'),
    ('<select class="form-select form-select-sm w-auto" name="accion">',
     ayuda("historia.accion") + '<select class="form-select form-select-sm w-auto" name="accion">'),
], pantalla="historia")

cambiar(T % ("historia", "historia", "versiones"), [
    ('<select class="form-select form-select-sm w-auto" name="proyecto">',
     ayuda("versiones.proyecto") + '<select class="form-select form-select-sm w-auto" name="proyecto">'),
], pantalla="versiones")

cambiar(T % ("niveles", "niveles", "reglas"), [
    ('<div class="card-header"><h3 class="card-title">Capítulo {{ capitulo }}</h3></div>',
     '<div class="card-header"><h3 class="card-title">Capítulo {{ capitulo }}</h3>'
     '<span class="ms-auto d-flex align-items-center gap-1 text-secondary">Nivel ' + ayuda("nivel.regla") + '</span></div>'),
], pantalla="reglas")

INCLUIR = '{% include "proyectos/_ayuda_del_campo.html" %}'
ETIQUETA = '<label class="form-label" for="{{ campo.id_for_label }}">{{ campo.label|capfirst }}</label>'
CON_AYUDA = ('<div class="d-flex align-items-center gap-1 mb-1"><label class="form-label mb-0" '
             'for="{{ campo.id_for_label }}">{{ campo.label|capfirst }}</label>' + INCLUIR + '</div>')
cambiar("core/proyectos/templates/proyectos/formulario.html", [
    (ETIQUETA + "\n      <select", CON_AYUDA + "\n      <select"),
    (ETIQUETA + "\n      <input", CON_AYUDA + "\n      <input"),
    ('<span class="form-check-label">{{ campo.label }}</span>', '<span class="form-check-label">{{ campo.label }}</span> ' + INCLUIR),
], pantalla="proyecto")
print("listo")
