# -*- coding: utf-8 -*-
"""`09·16` · Marca pares de señales sospechosamente parecidas, para que alguien mire.

**Una memoria con dos señales opuestas activas es peor que una memoria vacía**:
da respuestas seguras y contradictorias según cuál se encuentre primero.

## Se llama «parecidas», no «contradicciones», y es a propósito

**Decidir si dos señales se contradicen o se complementan es criterio, no
cálculo.** Dos decisiones sobre el mismo tema pueden ser la misma dicha de dos
formas, una que reemplazó a la otra, o dos caras de un acuerdo más grande.

**Lo que un programa puede hacer es encontrar el par y ponerlo delante.**
Llamarlo «detección de contradicciones» prometería más de lo que puede dar — y
un aviso que promete de más se termina apagando, que es el defecto más caro de
este repositorio.

## Por qué el mismo tipo y el mismo alcance

Dos señales solo pueden chocar si hablan de lo mismo **para el mismo sitio**. Un
acuerdo de la organización y uno de un proyecto que dicen cosas distintas no se
contradicen: el segundo **ajusta** al primero, que es como está diseñado el
alcance.

## Umbral alto, y salida en aviso

Un umbral bajo llena la salida de pares que no tienen nada que ver, y entonces
nadie mira ninguno. Se prefiere **perder pares dudosos antes que sepultar los
buenos**.
"""
import os
import sqlite3
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

# Tan parecidas que casi seguro hablan de lo mismo. No es «se contradicen»:
# es «alguien tiene que mirar si se contradicen».
#
# **Medido el 2026-08-18 sobre 114 señales que deciden.** El corte es abrupto:
# 0.86 devuelve seis pares y 0.90 devuelve cero. Los seis de 0.86 son señales
# **relacionadas** —dos módulos rotos por la misma fase anterior— y ninguna
# contradice a la otra.
#
# **Se eligió el umbral que hoy no devuelve nada**, y es la decisión correcta:
# seis pares que hay que descartar a mano enseñan a no mirar la lista, y
# entonces el día que haya uno de verdad tampoco se mira.
UMBRAL = 0.90

# Los tipos donde una contradicción hace daño de verdad: los que **deciden**.
# Un `gotcha` o una `pregunta-abierta` repetidos son ruido, no una trampa.
TIPOS_QUE_DECIDEN = ("decision", "patron", "restriccion", "supuesto")


def activas(con, tipos=None):
    """`[(id, tipo, scope, titulo, why)]` de las señales vigentes."""
    tipos = tipos or TIPOS_QUE_DECIDEN
    marcas = ",".join("?" * len(tipos))
    filas = con.execute(
        "SELECT id, tipo, scope, titulo, COALESCE(why,'') FROM senales "
        "WHERE estado = 'activa' AND tipo IN (%s) ORDER BY id" % marcas,
        tuple(tipos)).fetchall()
    return [tuple(f) for f in filas]


def _vectores(textos):
    """Los vectores del módulo semántico, o `None` si no está disponible."""
    import semantica
    if not semantica.disponible():
        return None
    return semantica.embed(textos)


def _coseno(a, b):
    import math
    num = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    return num / (na * nb) if na and nb else 0.0


def pares(con, umbral=UMBRAL, tipos=None):
    """`[(a, b, parecido)]` de las que conviene mirar. Vacío si no hay semántica.

    **Sin el módulo semántico no adivina**: devuelve `[]` y quien llama lo dice.
    Comparar por palabras sueltas daría pares por casualidad, y un par por
    casualidad enseña a ignorar la lista entera.
    """
    señales = activas(con, tipos)
    if len(señales) < 2:
        return []
    # **Se compara el porqué, no el título.** Los títulos de esta casa siguen un
    # molde —«Módulo X cerrado con Fase Y»— y dos señales de temas distintos
    # salen parecidísimas por la **forma** de la frase. Medido: comparando
    # títulos, los once pares que salían eran todos de esa clase.
    #
    # El porqué es donde está la sustancia, y dos porqués parecidos sí son dos
    # señales que hablan de lo mismo.
    vecs = _vectores([s[4] or s[3] for s in señales])
    if vecs is None:
        return []

    salida = []
    for i in range(len(señales)):
        for j in range(i + 1, len(señales)):
            a, b = señales[i], señales[j]
            if a[1] != b[1] or a[2] != b[2]:
                continue                # distinto tipo o distinto alcance
            p = _coseno(vecs[i], vecs[j])
            if p >= umbral:
                salida.append((a, b, p))
    return sorted(salida, key=lambda x: -x[2])


def informe(db=None, umbral=UMBRAL):
    """El texto para leer. Dice **también** cuando no pudo mirar."""
    db = db or os.path.join(AQUI, "senales.db")
    if not os.path.isfile(db):
        return "no hay memoria que revisar: falta %s" % db
    con = sqlite3.connect(db)
    try:
        import semantica
        if not semantica.disponible():
            return ("el módulo semántico no está disponible, así que **no se "
                    "revisó nada**. No se compara por palabras sueltas: daría "
                    "pares por casualidad, y un par por casualidad enseña a "
                    "ignorar la lista entera")
        encontrados = pares(con, umbral)
    finally:
        con.close()

    if not encontrados:
        return "ningún par de señales activas se parece lo suficiente (umbral %.2f)" % umbral

    lineas = ["%d par(es) para mirar — **parecidos, no necesariamente opuestos**:"
              % len(encontrados)]
    for a, b, p in encontrados:
        lineas.append("  %s ~ %s  (%.2f · %s · %s)" % (a[0], b[0], p, a[1], a[2]))
        lineas.append("      %s" % a[3][:70])
        lineas.append("      %s" % b[3][:70])
    lineas.append("")
    lineas.append("Si dos dicen lo contrario, una se marca como reemplazada. "
                  "Si se complementan, no hay nada que hacer — **eso lo decide "
                  "quien lee**.")
    return "\n".join(lineas)


def main():
    import argparse
    p = argparse.ArgumentParser(
        description="Marca pares de señales activas sospechosamente parecidas. "
                    "No dice que se contradigan: dice que alguien mire.")
    p.add_argument("--db", default=os.path.join(AQUI, "senales.db"))
    p.add_argument("--umbral", type=float, default=UMBRAL)
    a = p.parse_args()
    print(informe(a.db, a.umbral))
    return 0


if __name__ == "__main__":
    sys.exit(main())
