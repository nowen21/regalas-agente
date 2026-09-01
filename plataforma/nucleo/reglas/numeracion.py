# -*- coding: utf-8 -*-
"""El identificador de una regla: el siguiente libre, y ninguno se reutiliza.

**Por qué importa tanto un número.** Una especificación escrita hace un año, un
commit, una fase cerrada: todos citan reglas por su identificador. Si un número
se le da a otra regla, todas esas citas empiezan a apuntar a algo que dice otra
cosa, **y no hay forma de notarlo leyendo**. La cita sigue viéndose bien.

**Por eso el número de una regla derogada tampoco se libera.** Derogar no borra:
la regla se queda escrita, marcada, y su número ocupado para siempre.

**Y por eso el siguiente es el que sigue al mayor, no el primer hueco.** Un
hueco puede ser una regla que se derogó y se movió de archivo, o una que nunca
existió; desde acá no se distinguen. Rellenar huecos es la única forma de
reutilizar un número sin darse cuenta, así que no se rellenan.
"""
import re

from . import catalogo

# El número de un identificador: `F26` da 26, y `F12.1` da 12. Las reglas con
# punto son partes de otra, y no consumen un número propio.
_NUMERO = re.compile(u"^([A-Za-z]+)(\\d+)")


class IdentificadorYaUsado(Exception):
    """Ese identificador ya lo tiene otra regla, viva o derogada."""


def _numero_de(identificador):
    encontrado = _NUMERO.match(identificador or "")
    return int(encontrado.group(2)) if encontrado else 0


def usados(raiz, prefijo):
    """Los números que ese prefijo ya tiene, **contando las derogadas**."""
    agrupadas = catalogo.por_prefijo(raiz)
    return sorted(set(_numero_de(una.id) for una in agrupadas.get(prefijo, [])))


def esta_usado(raiz, identificador):
    """Si ese identificador ya existe, viva la regla o esté derogada."""
    return any(una.id == identificador for una in catalogo.todas(raiz))


def siguiente_libre(raiz, prefijo):
    """El identificador que le toca a la próxima regla de ese capítulo.

    **Es el que sigue al mayor**, no el primer hueco: rellenar un hueco es la
    única forma de reutilizar un número sin darse cuenta.
    """
    numeros = usados(raiz, prefijo)
    return "%s%d" % (prefijo, (max(numeros) + 1) if numeros else 1)


def comprobar_libre(raiz, identificador):
    """Levanta `IdentificadorYaUsado` si ese número ya está ocupado.

    Se llama **antes** de guardar. Después de guardar ya hay dos reglas con el
    mismo número, y la que se lea primero gana.
    """
    if esta_usado(raiz, identificador):
        raise IdentificadorYaUsado(
            "El identificador «%s» ya lo tiene otra regla. **No se reutiliza "
            "ninguno**, ni siquiera el de una derogada: las citas escritas "
            "apuntarían a otra cosa sin que nadie lo note." % identificador)


def huecos(raiz, prefijo):
    """Los números que ese prefijo se saltó, **para mirarlos, no para usarlos**.

    Sirve para revisar el cuerpo de reglas, no para asignar: lo que devuelve
    esta función es justamente lo que `siguiente_libre` no va a entregar nunca.
    """
    numeros = usados(raiz, prefijo)
    if not numeros:
        return []
    return [n for n in range(1, max(numeros)) if n not in numeros]
