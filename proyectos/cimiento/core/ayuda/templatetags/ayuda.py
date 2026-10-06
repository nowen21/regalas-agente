"""Etiquetas de la ayuda en cada campo y en cada pantalla (`EP-025·HU-018`, de scilit EP-014 HU-005).

Uso en una plantilla:
    {% load ayuda %}
    {% campo_con_ayuda form.nombre "configuracion.rutas_en_avisos" %}   campo completo con su «?»
    <label class="form-label">Nombre</label>{% ayuda_campo "suspension.motivo" %}
    <button class="btn" {% ayuda_corta "Termina la suspensión ya" %}>Levantar</button>
    {% ayuda_pantalla "suspensiones" %}
"""
from django import template
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from ..textos import CAMPOS, PANTALLAS

register = template.Library()

BOTONES = [
    ("para_que", "¿Para qué sirve?"),
    ("donde_mas", "¿En qué otras pantallas se usa?"),
    ("como_encaja", "Cómo encaja en el sistema"),
]


def _mapa(pasos):
    """Numera los pasos y les da su turno en la animación: cada elemento aparece después del anterior."""
    turno, salida = 0, []
    for n, paso in enumerate(pasos, 1):
        etiqueta = "Paso %d, aquí está" % n if paso["tipo"] == "aqui" else "Paso %d" % n
        bloque = {**paso, "etiqueta": etiqueta, "turno": turno, "subpasos": []}
        turno += 1
        for m, texto in enumerate(paso["pasos"], 1):
            bloque["subpasos"].append({"texto": texto, "num": "%d.%d" % (n, m), "turno": turno})
            turno += 1
        bloque["flecha"] = turno if n < len(pasos) else None
        turno += 1
        salida.append(bloque)
    return salida


def _datos_del_campo(clave):
    texto = CAMPOS.get(clave)
    if not texto:
        # En desarrollo, un «?» rojo avisa que la clave no tiene texto; en producción no se pinta nada.
        return {"texto": None, "falta": settings.DEBUG and bool(clave), "clave": clave}
    secciones = [{"encabezado": e, "lista" if isinstance(c, (list, tuple)) else "parrafo": c}
                 for e, c in texto["secciones"]]
    contenido = render_to_string("ayuda/tooltip_contenido.html", {"secciones": secciones,
                                                                   "consejo": texto.get("consejo")})
    return {"texto": texto, "clave": clave, "contenido": contenido.strip()}


@register.inclusion_tag("ayuda/tooltip.html")
def ayuda_campo(clave):
    """El «?» junto a una etiqueta, con su globo."""
    return _datos_del_campo(clave)


@register.inclusion_tag("ayuda/campo.html")
def campo_con_ayuda(campo, clave="", clase=""):
    """Un campo de formulario completo: etiqueta, «?», casilla, texto de apoyo y error."""
    ayuda = render_to_string("ayuda/tooltip.html", _datos_del_campo(clave)) if clave else ""
    return {"campo": campo, "ayuda": mark_safe(ayuda.strip()), "clase": clase}


@register.inclusion_tag("ayuda/ayuda_corta.html")
def ayuda_corta(texto):
    """Atributos de un texto emergente corto, para poner dentro de un botón o una etiqueta."""
    return {"texto": texto}


@register.inclusion_tag("ayuda/ayuda_pantalla.html")
def ayuda_pantalla(clave):
    """Los botones de ayuda debajo del título de una pantalla, con sus ventanas."""
    pantalla = PANTALLAS.get(clave, {})
    botones = []
    for parte, titulo in BOTONES:
        if parte in pantalla:
            datos = dict(pantalla[parte])
            if "mapa" in datos:
                datos["mapa"] = _mapa(datos["mapa"])
            botones.append({"id": "ayuda-%s-%s" % (clave, parte), "titulo": titulo, **datos})
    return {"botones": botones, "clave": clave}
