# -*- coding: utf-8 -*-
"""Cómo se escriben los números del gasto, en la orden y en el tablero."""


def miles(numero):
    """`1.756.000`: en Colombia los miles se separan con punto."""
    return f"{int(numero or 0):,}".replace(",", ".")
