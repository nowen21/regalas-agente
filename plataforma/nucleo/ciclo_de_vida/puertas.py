# -*- coding: utf-8 -*-
"""No dejar pasar a la estación siguiente sin la puerta cumplida — `F-013`.

**El rechazo dice cuál puerta falta.** «No se puede avanzar» obliga a ir a
buscar; «falta la estación 7, el plan aprobado por el usuario» se arregla de una.

**Una puerta que estorba se termina saltando**, así que acá hay tres y no trece:
las que se comprueban son las que dejan daño cuando se saltan —código sin plan
aprobado, cierre sin veredicto, publicación sin autorización—. Las otras diez se
marcan a mano y esta función no opina sobre ellas.

**Y no es un candado.** Cualquiera puede escribir el archivo a mano; lo que se
logra es que saltarse la puerta sea un acto deliberado en vez de un olvido.
"""
import re

from nucleo.ciclo_de_vida import estaciones

# La estación a la que se quiere entrar, y qué se exige antes de dejar pasar.
# Solo estas tres: las demás se marcan y ya.
LAS_QUE_SE_COMPRUEBAN = {
    8: ("la estación 7 · plan y pruebas aprobados por el usuario",
        "escribir código sin un plan aprobado es construir lo que nadie pidió"),
    12: ("un veredicto de las pruebas que diga Cumple",
         "cerrar sin veredicto deja escrito que algo funciona sin que conste "
         "que se probó"),
    13: ("la estación 12 · el commit autorizado",
         "publicar lo que no está guardado deja fuera del repositorio lo que "
         "salió a producción"),
}

_CONCEPTO = re.compile(
    r"\*\*Concepto\*\*\s*\|\s*\**\s*(Cumple|No cumple|Sin veredicto)", re.I)


def veredicto_de(texto):
    """`Cumple`, `No cumple` o `""` si la fase no lo dice todavía."""
    hallado = _CONCEPTO.search(texto)
    return hallado.group(1).capitalize() if hallado else ""


def _cumplida(fase, numero):
    for una in fase.get("estaciones", []):
        if una["numero"] == numero:
            return una["estado"] in ("cumplida", "no aplica")
    return False


def se_puede_pasar(fase, texto, a_estacion):
    """¿Deja pasar? Devuelve `(sí_o_no, motivo)`.

    El motivo **siempre nombra la puerta**, también cuando deja pasar: quien lee
    un sí tiene que poder comprobarlo sin volver al documento.
    """
    if a_estacion not in LAS_QUE_SE_COMPRUEBAN:
        return True, ("la estación %d no tiene puerta comprobable: se marca a "
                      "mano y esta comprobación no opina" % a_estacion)
    que_exige, por_que = LAS_QUE_SE_COMPRUEBAN[a_estacion]

    if a_estacion == 12:
        concepto = veredicto_de(texto)
        if concepto.lower() != "cumple":
            return False, ("falta %s — %s. Hoy dice: %s" % (
                que_exige, por_que, concepto or "nada"))
        return True, "cumplida: %s" % que_exige

    anterior = a_estacion - 1
    if not _cumplida(fase, anterior):
        return False, "falta %s — %s" % (que_exige, por_que)
    return True, "cumplida: %s" % que_exige


def revisar(fase, texto):
    """Las tres puertas de una fase, con su veredicto. Para verlas de un golpe."""
    return [
        {"estacion": numero,
         "pasa": se_puede_pasar(fase, texto, numero)[0],
         "motivo": se_puede_pasar(fase, texto, numero)[1]}
        for numero in sorted(LAS_QUE_SE_COMPRUEBAN)
    ]


def dicho(revisadas):
    """Las tres líneas para la consola."""
    return "\n".join(
        "  estación %2d: %s — %s" % (
            una["estacion"], "pasa" if una["pasa"] else "NO pasa", una["motivo"])
        for una in revisadas)
