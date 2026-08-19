# -*- coding: utf-8 -*-
"""`00·ID9` · Cuánto ocupa lo que el agente contesta. **Mide, no detiene.**

**Por qué solo mide.** `reglas-validables.md` ya dice que `ID9` no se puede
comprobar con un programa: *«contar renglones es fácil, pero decidir cuál sobra
exige entender qué cambia la decisión del que lee»*. Eso sigue siendo cierto y
esto no lo contradice — **cuenta lo fácil y no opina de lo otro**.

**Por qué medir sirve igual.** El [pendiente 58](../pendientes/58-nada-hace-cumplir-id9.md)
midió el daño: en un proyecto el usuario pidió «menos es más» **siete veces en
tres días**, y cada vez se anotó el caso sin que cambiara nada. Lo que faltaba
no era otro recordatorio: era **un número**. «Me parece que contesta largo» no
se puede revisar; «la mediana subió de 900 a 2 400 caracteres» sí.

**Por qué no rebota la respuesta.** Un enganche que corre al terminar llega
tarde: el texto ya salió. Rebotarlo le costaría al usuario leer la versión
larga primero y la corta después — que es más texto, no menos.

**Lo que no hace.** No dice cuál respuesta estuvo mal. Una respuesta larga
puede ser la correcta: `ID9` prohíbe la palabra que sobra, no la línea que hace
falta.
"""
import os
import re

import comun
from comun import AVISO, Hallazgo, leer

# La transcripción la escribe `hook_historico.py`. Cada respuesta abre con esta
# marca y termina donde empieza el siguiente turno.
_AGENTE = re.compile(r"(?m)^\*\*Agente\*\*\s+—\s+([0-9:\- ]+)$")
_TURNO = re.compile(r"(?m)^(?:### \d+ · Usuario|\*\*Agente\*\*) ")
_HTML = re.compile(r"<!--.*?-->", re.S)


def _limpio(texto):
    """El texto como se lee: sin los comentarios que el enganche deja."""
    return _HTML.sub("", texto).strip()


def respuestas(archivo):
    """`[(fecha, cuántos caracteres)]` de cada respuesta del agente.

    Se mide el texto **como se lee**, sin los comentarios de máquina. No se
    descuentan tablas ni bloques de código a propósito: ocupan pantalla igual, y
    lo que se mide es cuánto hay que leer.
    """
    texto = leer(archivo)
    salida = []
    marcas = list(_AGENTE.finditer(texto))
    for i, m in enumerate(marcas):
        ini = m.end()
        siguiente = _TURNO.search(texto, ini)
        fin = siguiente.start() if siguiente else len(texto)
        cuerpo = _limpio(texto[ini:fin])
        if cuerpo:
            salida.append((m.group(1).strip(), len(cuerpo)))
    return salida


def _mediana(numeros):
    if not numeros:
        return 0
    orden = sorted(numeros)
    medio = len(orden) // 2
    if len(orden) % 2:
        return orden[medio]
    return (orden[medio - 1] + orden[medio]) // 2


def resumen(archivo):
    """`{"cuantas","mediana","maxima","total"}` de una transcripción."""
    largos = [n for _f, n in respuestas(archivo)]
    return {"cuantas": len(largos),
            "mediana": _mediana(largos),
            "maxima": max(largos) if largos else 0,
            "total": sum(largos)}


def transcripciones(raiz=None):
    """Los archivos de sesión, del más viejo al más nuevo."""
    raiz = raiz or comun.RAIZ
    carpeta = os.path.join(raiz, "historico-chat")
    if not os.path.isdir(carpeta):
        return []
    salida = [os.path.join(carpeta, n) for n in sorted(os.listdir(carpeta))
              if re.match(r"^\d{4}-\d{2}-\d{2}.*\.md$", n)]
    return salida


# Cuatro líneas de molde son 320 caracteres (`20·M5`). Una respuesta no es una
# regla, así que el umbral es otro: **seis veces eso**. No sale de una teoría —
# sale de que las respuestas que el usuario paró con «no entiendo» pasaban de
# ahí, y las que aceptó, no.
HOLGADO = 320 * 6


def validar(raiz=None):
    """Un aviso por sesión cuya **mediana** pasa el umbral. Nunca una falla.

    **Se mira la mediana y no el máximo**: una respuesta larga suele estar
    justificada —un informe que se pidió, una tabla que hacía falta—. Lo que
    señala un problema es que la mitad de las respuestas sean largas.
    """
    hallazgos = []
    for archivo in transcripciones(raiz):
        r = resumen(archivo)
        if r["cuantas"] >= 5 and r["mediana"] > HOLGADO:
            hallazgos.append(Hallazgo(
                AVISO, archivo, 0,
                f"la mitad de las {r['cuantas']} respuestas pasa de "
                f"{r['mediana']} caracteres (holgado: {HOLGADO}) — `00·ID9`. "
                f"No es un incumplimiento: es un número para mirar al cerrar"))
    return hallazgos


def como_texto(raiz=None):
    """La serie, para leerla al cerrar la sesión."""
    lineas = []
    for archivo in transcripciones(raiz):
        r = resumen(archivo)
        if not r["cuantas"]:
            continue
        nombre = os.path.basename(archivo)[:-3]      # sin el `.md`
        lineas.append("  %-46s %3d resp · mediana %5d · máxima %6d"
                      % (nombre[:46], r["cuantas"], r["mediana"], r["maxima"]))
    if not lineas:
        return ""
    return ("Cuánto ocupa lo que el agente contesta (`00·ID9` · mide, no detiene)\n"
            + "\n".join(lineas))


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("brevedad")
