# -*- coding: utf-8 -*-
"""El orden del ciclo, tipo por tipo. **Es una lista declarada, no deducida.**

Es lo que la §5.1 de la especificación fija y lo que la `HU-001` pedía declarar
antes de construir nada. Vive en su propio archivo por una razón: es lo que hay
que abrir el día que aparezca un tipo de documento nuevo.

**Por qué no se deduce del disco.** El orden del disco es alfabético; el del
ciclo es el que le sirve a quien lee el expediente. Son dos cosas distintas y
solo una de las dos se puede escribir sola.

**Lo que no encaja en ningún grupo no se acomoda al más parecido**, se lista
aparte. Acomodarlo convierte un dato en una suposición, y quien lee el
expediente no tendría cómo saber que se supuso.
"""

# Los nueve grupos, en el orden en que el ciclo los produce. Cada uno con los
# tipos que Importación reconoce y le corresponden.
GRUPOS = (
    ("Planificación",
     ("etapa del ciclo de vida", "acta de constitución",
      "estudio de factibilidad")),
    ("Análisis de requisitos",
     ("inventario de funcionalidades",)),
    ("Diseño",
     ("modelo de datos", "decisiones de arquitectura", "diseño de interfaz",
      "contrato de la interfaz")),
    ("Especificaciones de módulo",
     ("especificación de módulo",)),
    ("Épicas",
     ("épica",)),
    ("Historias de usuario",
     ("historia de usuario",)),
    ("Fases",
     ("plan de trabajo", "plan de pruebas", "resultado de pruebas",
      "estado de fase", "funcionalidad implementada")),
    ("Registros de versión",
     ("registro de versión",)),
)

# **Los cinco documentos de una fase, y en este orden.** No es alfabético: es
# el orden en que la fase los produce, que es lo que le sirve a quien la lee.
DE_UNA_FASE = ("plan de trabajo", "plan de pruebas", "resultado de pruebas",
               "estado de fase", "funcionalidad implementada")

# **Lo que no entra al expediente, por decisión escrita.** La auditoría y la
# memoria sirven para saber cómo se llegó, no para entregar: es la duda 5 del
# análisis, resuelta con el usuario el 2026-08-31.
#
# **Y el índice tampoco**: es la tabla de contenido de una carpeta, y el
# expediente arma la suya.
FUERA = ("señales", "índice")


def grupo_de(tipo):
    """En qué grupo va ese tipo, o `""` si no encaja en ninguno."""
    for nombre, tipos in GRUPOS:
        if tipo in tipos:
            return nombre
    return ""


def orden_de(tipo):
    """La posición del grupo de ese tipo, para ordenar. `-1` si no encaja."""
    for i, (_nombre, tipos) in enumerate(GRUPOS):
        if tipo in tipos:
            return i
    return -1


def posicion_en_grupo(tipo):
    """Qué lugar ocupa ese tipo **dentro de su grupo**. 99 si no está.

    Hace falta para los cinco documentos de una fase: ordenados por su nombre
    de archivo saldrían el estado y el cierre antes que el plan, que es el
    orden del disco. El del ciclo es el que le sirve a quien lee.
    """
    for _nombre, tipos in GRUPOS:
        if tipo in tipos:
            return tipos.index(tipo)
    return 99


def entra(tipo):
    """Si ese tipo entra al expediente."""
    return bool(tipo) and tipo not in FUERA
