# -*- coding: utf-8 -*-
"""El comprobante de que una acción ya quedó registrada.

Vive acá, y no dentro de la auditoría ni del almacén, porque los dos lo
necesitan y ninguno debe depender del otro: **la auditoría la emite, el
almacén la exige**.

**Qué barrera es y qué barrera no es.** La constancia dice sobre qué archivo se
dejó el registro, y el almacén rechaza escribir en otro. Eso convierte el
descuido más probable —reutilizar una constancia vieja para otra cosa— en un
rechazo, no en un archivo cambiado a escondidas.

Lo que **no** es: una barrera contra alguien que quiera saltársela a propósito.
En este lenguaje siempre se puede construir el objeto a mano. Lo que se logra
es que escribir sin constancia sea un acto deliberado y visible en el código,
en vez de un olvido que nadie nota. Esa es la promesa, y no una más grande.
"""


class SinConstancia(Exception):
    """Se intentó cambiar algo sin haber dejado el registro antes."""


class Constancia(object):
    """Dice que la acción sobre `sobre_que` ya quedó registrada."""

    def __init__(self, sobre_que, fila):
        self.sobre_que = sobre_que
        self.fila = fila

    def autoriza(self, nombre):
        """Solo autoriza el archivo sobre el que se registró la acción."""
        return self.sobre_que == nombre

    def __repr__(self):
        return "<Constancia sobre %r>" % self.sobre_que
