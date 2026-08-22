from django import template

register = template.Library()

# Color de badge por tipo de señal (clases de Bootstrap).
_COLORES = {
    'decision': 'text-bg-primary',
    'error-resuelto': 'text-bg-danger',
    'patron': 'text-bg-success',
    'aprendizaje': 'text-bg-info',
    'alternativa-descartada': 'text-bg-secondary',
    'supuesto': 'text-bg-warning',
    'restriccion': 'text-bg-dark',
    'pregunta-abierta': 'text-bg-light border',
    'gotcha': 'text-bg-warning',
    'deuda-tecnica': 'text-bg-secondary',
}


@register.filter
def color_tipo(tipo):
    return _COLORES.get(tipo, 'text-bg-secondary')
