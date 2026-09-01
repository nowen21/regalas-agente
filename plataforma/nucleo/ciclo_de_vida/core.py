# -*- coding: utf-8 -*-
"""Qué le falta a un documento del ciclo. **Solo lee; no escribe nada.**

Se calcula al pedirlo, leyendo el archivo. Guardar la lista crearía una segunda
verdad que envejece en cuanto alguien edite el documento por fuera, que es lo
que `DA-01` viene a evitar.

**Escribir es de la otra historia.** Acá se cuenta y se ubica; llenar el hueco
llega con la `HU-002`. Se separaron porque fallan distinto: contar mal da un
número equivocado, escribir mal daña un documento.
"""
import io
import os

from django.conf import settings

from nucleo.importacion.models import Traido
from . import huecos, moldes


def _carpeta_de_plantillas():
    """Dónde vive `plantillas/` del estándar."""
    declarada = getattr(settings, "CARPETA_PLANTILLAS", None)
    if declarada:
        return str(declarada)
    return os.path.join(str(settings.RAIZ.parent), "plantillas")


def _texto_de(traido):
    """El texto guardado de un documento, o `""` si no se puede leer."""
    ruta = os.path.join(str(settings.CARPETA_DATOS),
                        traido.guardado_en.replace("/", os.sep))
    try:
        with io.open(ruta, encoding="utf-8", errors="replace") as abierto:
            return abierto.read()
    except OSError:
        return ""


def que_le_falta(proyecto, origen):
    """Qué molde sigue un documento y qué huecos le faltan.

    Devuelve `None` si ese documento no está traído. Si está, devuelve siempre
    las tres listas, aunque estén vacías: un documento sin huecos **lo dice**,
    en vez de responder con una lista vacía que no se sabe interpretar.
    """
    try:
        traido = Traido.objects.get(proyecto=proyecto, origen=origen)
    except Traido.DoesNotExist:
        return None
    return de_un_texto(_texto_de(traido), traido.tipo, traido.origen)


def de_un_texto(texto, tipo, relativa=""):
    """Lo mismo, sobre un texto que ya se tiene. Es lo que se puede probar.

    Se parte en dos para que la comprobación no necesite base de datos ni
    archivos: lo que decide es el texto y el tipo, no de dónde salieron.
    """
    sin_tipo = not tipo
    porque_no = moldes.por_que_no_tiene_molde(tipo)
    ruta_molde = moldes.molde_de(tipo, relativa)

    del_molde = ()
    if ruta_molde:
        del_molde = huecos.marcas_del_molde(
            moldes.texto_del_molde(_carpeta_de_plantillas(), tipo, relativa))

    hallados = huecos.encontrar(texto, del_molde)
    ciertos = huecos.por_clase(hallados, huecos.CIERTO)
    posibles = huecos.por_clase(hallados, huecos.POSIBLE)
    instalacion = huecos.por_clase(hallados, huecos.INSTALACION)

    return {
        "tipo": tipo,
        "molde": ruta_molde,
        # Las tres razones por las que puede no haber molde, separadas. Un tipo
        # desconocido se arregla enseñándoselo a Importación; un tipo sin molde,
        # escribiendo el molde. Confundirlos esconde el que sí tiene arreglo.
        "sin_tipo": sin_tipo,
        "sin_molde": porque_no,
        "molde_perdido": bool(ruta_molde) and not del_molde and not sin_tipo,
        "ciertos": ciertos,
        "posibles": posibles,
        "instalacion": instalacion,
        # La cuenta que manda. Es la del usuario, y es la misma que da el módulo
        # Expediente: las dos cuentan `«…»`.
        "cuantos": len(ciertos),
        "completo": not ciertos,
    }


def de_un_proyecto(proyecto):
    """Lo que le falta a cada documento de un proyecto, de más a menos.

    Los que no tienen ningún hueco cierto no salen: la lista es de trabajo por
    hacer, y un documento completo no es trabajo.
    """
    salida = []
    for traido in Traido.objects.filter(proyecto=proyecto):
        falta = de_un_texto(_texto_de(traido), traido.tipo, traido.origen)
        if falta["cuantos"]:
            falta["origen"] = traido.origen
            salida.append(falta)
    salida.sort(key=lambda uno: (-uno["cuantos"], uno["origen"]))
    return salida
