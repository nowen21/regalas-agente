# -*- coding: utf-8 -*-
"""Las siete etapas del ciclo, como se muestran en la ficha de un proyecto.

**Ya no están escritas acá.** Vivían en este archivo, y cambiarle el nombre a
una o explicarla mejor obligaba a abrir el código. Ahora son filas de la tabla
`EtapaDelCiclo`, que se editan en `/admin/`.

Lo que queda en este archivo es una sola cosa: **cruzar esa lista con lo que el
proyecto tiene escrito**, para saber cuáles le faltan. Eso es lógica, no texto.
"""
from nucleo.ajustes import core as ajustes


def de_un_proyecto(con_documento):
    """Las etapas, cada una sabiendo si ese proyecto la tiene escrita.

    `con_documento` es la lista de carpetas que sí tienen su documento.
    """
    tiene = set(con_documento or ())
    return [dict(una, escrita=una["carpeta"] in tiene)
            for una in ajustes.las_etapas()]
