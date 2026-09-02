# -*- coding: utf-8 -*-
"""Cuánto tiempo se gasta revisando lo entregado — `F-032`.

**Medir no obliga al usuario a anotar nada.** El tiempo sale de las horas que el
enganche del estándar ya escribe en cada mensaje del histórico: entre la
respuesta del agente y el mensaje siguiente del usuario hay un hueco, y ese hueco
es lo que se tardó en leer y contestar. Pedirle al usuario que cronometre sería
cobrarle la medición, y la ficha lo prohíbe: *medir no puede costar más que lo
que ahorra*.

**La medición inicial no se tomó antes de empezar, y eso no se arregla acá.** Lo
dice la propia ficha de `F-032`. Lo que hay es la reconstruida: el tramo más
viejo del histórico. **No es un antes: es el comienzo de lo que quedó grabado**,
y para entonces el proyecto ya llevaba camino andado. Sale escrito en cada
comparación, porque una línea base que se presenta como si fuera un antes de
verdad hace que la mejora parezca mayor de lo que es.

**Un hueco muy largo no es revisión: es que se fue.** Se descartan los mayores
al tope, y se dice cuántos se descartaron. Contarlos como revisión convertiría un
almuerzo en cuatro horas de lectura.
"""
import datetime

# Formato de la hora que escribe el enganche del estándar.
RELOJ = "%Y-%m-%d %H:%M:%S"

# Por encima de esto no se cuenta: nadie revisa una respuesta dos horas seguidas
# sin escribir nada. Se descarta y se dice cuántos.
TOPE_SEGUNDOS = 2 * 60 * 60

# Debajo de esto tampoco: es un «si» o un «siga», no una revisión.
PISO_SEGUNDOS = 3

MINIMO_PARA_COMPARAR = 10


def _cuando(texto):
    """La hora del mensaje, o `None` si no la tiene.

    De 3720 mensajes indexados en este repositorio, **55 no tienen hora**: unos
    dicen «hora no registrada» y otros «reconstruido a mano». No se inventan.
    """
    try:
        return datetime.datetime.strptime(texto, RELOJ)
    except (ValueError, TypeError):
        return None


def huecos(mensajes):
    """Los segundos entre cada respuesta del agente y el mensaje siguiente.

    Devuelve `{"segundos", "descartados_largos", "descartados_sin_hora"}`.
    """
    segundos = []
    largos = 0
    sin_hora = 0
    anterior = None
    for uno in mensajes:
        cuando = _cuando(uno.cuando)
        if cuando is None:
            sin_hora += 1
            anterior = None
            continue
        if (anterior is not None and anterior[1] == "agente"
                and uno.quien == "usuario"):
            paso = (cuando - anterior[0]).total_seconds()
            if paso > TOPE_SEGUNDOS:
                largos += 1
            elif paso >= PISO_SEGUNDOS:
                segundos.append(paso)
        anterior = (cuando, uno.quien)
    return {"segundos": segundos, "descartados_largos": largos,
            "descartados_sin_hora": sin_hora}


def _resumir(medidos):
    if not medidos["segundos"]:
        return None
    ordenados = sorted(medidos["segundos"])
    mitad = len(ordenados) // 2
    mediana = (ordenados[mitad] if len(ordenados) % 2
               else (ordenados[mitad - 1] + ordenados[mitad]) / 2.0)
    return {
        "cuantos": len(ordenados),
        "total_minutos": round(sum(ordenados) / 60.0, 1),
        # La mediana y no el promedio: un solo hueco largo mueve el promedio y
        # no mueve la mediana, y acá los huecos largos son lo normal.
        "mediana_segundos": round(mediana, 1),
        "descartados_largos": medidos["descartados_largos"],
        "descartados_sin_hora": medidos["descartados_sin_hora"],
    }


def por_mes(proyecto=None):
    """Lo revisado mes a mes, del más viejo al más nuevo. `[]` si no hay nada."""
    from nucleo.medicion.models import Mensaje, Sesion
    sesiones = Sesion.objects.all().order_by("fecha", "archivo")
    if proyecto:
        sesiones = sesiones.filter(proyecto__identificador=proyecto)

    juntados = {}
    for sesion in sesiones:
        mes = (sesion.fecha or "")[:7]
        if len(mes) != 7:
            continue
        medidos = huecos(Mensaje.objects.filter(sesion=sesion).order_by("orden"))
        acumulado = juntados.setdefault(
            mes, {"segundos": [], "descartados_largos": 0,
                  "descartados_sin_hora": 0})
        acumulado["segundos"].extend(medidos["segundos"])
        acumulado["descartados_largos"] += medidos["descartados_largos"]
        acumulado["descartados_sin_hora"] += medidos["descartados_sin_hora"]

    salida = []
    for mes in sorted(juntados):
        resumido = _resumir(juntados[mes])
        if resumido:
            resumido["mes"] = mes
            salida.append(resumido)
    return salida


def linea_base(proyecto=None):
    """El tramo más viejo con datos suficientes, o `None`.

    **Siempre viene marcada como reconstruida.** No hay otra: la de verdad
    debió tomarse antes de empezar, y no se tomó.
    """
    meses = por_mes(proyecto)
    for uno in meses:
        if uno["cuantos"] >= MINIMO_PARA_COMPARAR:
            copia = dict(uno)
            copia["reconstruida"] = True
            return copia
    return None


def comparar(proyecto=None):
    """La línea base contra el último mes con datos.

    Devuelve `{"base", "ultimo", "cambio_mediana", "se_puede_comparar", "por_que"}`.
    """
    meses = por_mes(proyecto)
    base = linea_base(proyecto)
    ultimo = meses[-1] if meses else None

    if not meses:
        return {"base": None, "ultimo": None, "cambio_mediana": None,
                "se_puede_comparar": False,
                "por_que": "no hay ninguna sesión indexada con hora de reloj"}
    if not base:
        return {"base": None, "ultimo": ultimo, "cambio_mediana": None,
                "se_puede_comparar": False,
                "por_que": ("ningún mes llega a %d revisiones medidas: es muy "
                            "poco para comparar contra nada"
                            % MINIMO_PARA_COMPARAR)}
    if base["mes"] == ultimo["mes"]:
        return {"base": base, "ultimo": ultimo, "cambio_mediana": None,
                "se_puede_comparar": False,
                "por_que": ("solo hay un mes con datos: la línea base y el "
                            "último son el mismo")}

    cambio = ultimo["mediana_segundos"] - base["mediana_segundos"]
    return {"base": base, "ultimo": ultimo, "cambio_mediana": round(cambio, 1),
            "se_puede_comparar": True, "por_que": ""}


def dicho(comparacion):
    """Lo comparado, con la advertencia de qué es esa línea base."""
    if not comparacion["se_puede_comparar"]:
        return "No se puede comparar todavía: %s." % comparacion["por_que"]
    base = comparacion["base"]
    ultimo = comparacion["ultimo"]
    cambio = comparacion["cambio_mediana"]
    hacia = "menos" if cambio < 0 else "más"
    return (
        "Línea base %s: %d revisiones, mediana de %.0f s.\n"
        "Último mes %s: %d revisiones, mediana de %.0f s.\n"
        "Son %.0f s %s por revisión.\n"
        "\n"
        "**Esa línea base es reconstruida, no tomada.** Es el tramo más viejo "
        "que quedó grabado, y para entonces el proyecto ya llevaba camino "
        "andado. La medición inicial de verdad debió tomarse antes de empezar "
        "y no se tomó: sin ella, esta comparación dice menos de lo que parece."
        % (base["mes"], base["cuantos"], base["mediana_segundos"],
           ultimo["mes"], ultimo["cuantos"], ultimo["mediana_segundos"],
           abs(cambio), hacia))
