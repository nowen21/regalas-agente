# -*- coding: utf-8 -*-
"""Qué documentos guardados parecen traer credenciales. **No toca ninguno.**

**Por qué contar en vez de tapar.** Lo importado es texto que ya existía en el
proyecto. Taparlo lo alteraría, y tapar no se deshace: es el único daño de esta
lista sin vuelta atrás.

Y no es teórico. Medido el 2026-09-01 sobre los 1 002 documentos guardados de
este repositorio, el tapador cambiaría **7 documentos y 21 fragmentos**. Los 21
son claves inventadas, y viven en los documentos de las fases **que
construyeron el tapador**: son sus casos de prueba escritos.

Es el mismo caso que ya apareció con los espacios por llenar: **un documento
que habla de algo parece contenerlo.** Ahí se podía recontar; acá se habría
perdido el texto.

**Callarlos tampoco sirve.** Un proyecto que trae una clave de verdad tiene que
saberlo, aunque la plataforma no la toque. Por eso se cuenta y se nombra, y la
decisión queda donde corresponde.
"""
from . import claves


def parecen_traer_claves(textos):
    """Cuáles de esos textos cambiarían si se taparan, y cuántos fragmentos.

    `textos` es una lista de `(nombre, texto)`. Devuelve una lista de
    `(nombre, cuantas)`, de más a menos. **Ningún texto se modifica**: se tapa
    una copia para contar, y la copia se descarta.
    """
    encontrados = []
    for nombre, texto in textos:
        if not texto:
            continue
        _, cuantas = claves.tapar(texto)
        if cuantas:
            encontrados.append((nombre, cuantas))
    encontrados.sort(key=lambda uno: (-uno[1], uno[0]))
    return encontrados
