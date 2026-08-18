# -*- coding: utf-8 -*-
"""`EP-005 · HU-002` · Tapa la clave antes de que se escriba en el histórico.

**El daño era real y estaba medido.** La fase
[`A-EP-005-HU-001`](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-001-transcripcion-de-la-sesion/A-EP-005-HU-001-retrodocumentar-la-transcripcion-de-la-sesion/resultado_pruebas.md)
comprobó que **una clave pegada en el chat queda escrita en claro en la
transcripción, y la transcripción se versiona**. De ahí no se borra: queda en
el historial del control de versiones para siempre.

**Se reconoce con lo que `secretos.py` ya sabe**, y no con una lista nueva. Ese
módulo lleva ocho formas de secreto de proveedor y el molde de la variable con
pinta de clave; duplicarlas acá dejaría dos listas que se separan.

**La marca es `«enmascarado»`** — la misma que el estándar ya usa para el
espacio por llenar. No se inventa una: se ve que hubo algo, y se distingue del
texto que sí es del mensaje.

**Lo que no se tapa, y es la mitad del trabajo:** el molde (`tu-clave`,
`changeme`, `<...>`), porque taparlo vuelve ilegible un ejemplo; y la línea que
lee del entorno, que es justo la forma correcta.
"""
import re
import sys

import comun
import secretos

MARCA = u"«enmascarado»"

# `password: "loquesea"` — se tapa **solo el valor**, no la variable: quien lea
# la transcripción tiene que poder seguir entendiendo de qué se hablaba.
_ASIGNA = secretos._ASIGNA


def _tapar_asignacion(m):
    if not secretos._valor_sospechoso(m.group("valor")):
        return m.group(0)               # es un molde: taparlo empeora el texto
    entero = m.group(0)
    return entero.replace(m.group("valor"), MARCA, 1)


def enmascarar(texto):
    """Devuelve el texto con las claves tapadas. `(texto, cuántas)`.

    No toca nada más: ni el orden, ni los saltos de línea, ni el resto del
    mensaje. Un enmascarado que reescribe de más deja de ser fiable como
    transcripción, que es lo único que este archivo tiene que ser.
    """
    if not texto:
        return texto, 0

    cuantas = [0]

    def uno(m):
        cuantas[0] += 1
        return MARCA

    salida = []
    for linea in texto.splitlines(keepends=True):
        # 1 · Las formas que delatan un secreto de un proveedor concreto.
        for patron, _motivo in secretos.SEGUROS:
            linea = patron.sub(uno, linea)

        # 2 · La variable con pinta de clave asignada a un texto fijo, salvo
        #     que lea del entorno — ahí no hay secreto que tapar.
        if not secretos._ENTORNO.search(linea):
            def asigna(m):
                nueva = _tapar_asignacion(m)
                if nueva != m.group(0):
                    cuantas[0] += 1
                return nueva
            linea = _ASIGNA.sub(asigna, linea)

        salida.append(linea)
    return "".join(salida), cuantas[0]


def hay_clave(texto):
    """Si el texto trae algo que se taparía. Para avisar sin reescribir."""
    return enmascarar(texto)[1] > 0


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("estandar")
