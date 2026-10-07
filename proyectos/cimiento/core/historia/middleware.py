# -*- coding: utf-8 -*-
"""`EP-026·HU-001` · Lo que se guarda en una petición queda a nombre de su cuenta.

`EP-026·HU-002` · Si el formulario trae las dos preguntas, su respuesta fija el
tipo de la versión que sube el envío; el motivo va en `version_motivo`, o en
`motivo` si el formulario ya trae uno.
"""
from .registro import quien_y_por_que
from .versiones import tipo_de

OBLIGA, AGREGA = "version_obliga", "version_agrega"


class CuentaDeLaPeticion:

    def __init__(self, siguiente):
        self.siguiente = siguiente

    def __call__(self, peticion):
        cuenta = getattr(peticion, "user", None)
        if cuenta is None or not cuenta.is_authenticated:
            return self.siguiente(peticion)
        motivo, tipo = "", None
        if peticion.method == "POST":
            motivo = peticion.POST.get("version_motivo") or peticion.POST.get("motivo", "")
            if OBLIGA in peticion.POST or AGREGA in peticion.POST:
                tipo = tipo_de(peticion.POST.get(OBLIGA), peticion.POST.get(AGREGA))
        with quien_y_por_que(cuenta=cuenta, motivo=motivo, tipo=tipo):
            return self.siguiente(peticion)
