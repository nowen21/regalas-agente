# -*- coding: utf-8 -*-
"""`{% load gasto %}` · `{{ numero|miles }}` en las plantillas del tablero."""
from django import template

from core.consumo import formato

register = template.Library()
register.filter("miles", formato.miles)
