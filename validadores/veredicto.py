# -*- coding: utf-8 -*-
"""El veredicto de una fase se copia solo a donde el estándar manda repetirlo — `EP-005 · HU-003`, fase C.

**Qué hace.** Lee el §6 del `resultado_pruebas.md` de una fase —con las mismas
expresiones con que `fases.py` lo lee para pasar la puerta— y deja el mismo
veredicto en los tres sitios donde se repetía a mano: la fila de la fase en el
§8 de su historia, el `README.md` de la fase y el de la historia.

**Qué no hace.** No decide ni interpreta el veredicto: copia lo que el §6 dice.
No toca el `estado-fase.md`, que es el checkpoint y lo escribe el agente
(`HU-013`). Y con un resultado a medio escribir —sin concepto— no hace nada:
un borrador no es un veredicto.

**Por qué acá y no en el adaptador.** Leer un resultado y reescribir una celda
es agnóstico; enterarse de que el archivo se escribió es de la herramienta, y
eso vive en el enganche del adaptador.
"""
import os
import re

import comun
import fases
from comun import leer

RESULTADO = "resultado_pruebas.md"
_ESTADO_README = re.compile(r"(?m)^\*\*Estado:\*\*.*$")


def leer_veredicto(resultado):
    """`(concepto, (cumplidos, total) | None)`; concepto es `cumple`, `no cumple` o ""."""
    texto = leer(resultado)
    m = fases._CONTEO.search(texto)
    return fases._concepto(texto), ((m.group(1), m.group(2)) if m else None)


def texto_del_estado(concepto, conteo, fecha):
    """Lo que se escribe en la celda de estado."""
    etiqueta = "Cumple" if concepto == "cumple" else "No cumple"
    cabeza = ("Cerrada el %s" if concepto == "cumple" else "Ejecutada el %s") % fecha
    cola = (", %s de %s CA" % conteo) if conteo else ""
    return "%s: %s%s" % (cabeza, etiqueta, cola)


def _fila_de_la_fase(texto, nombre_fase):
    """La fila de tabla cuya primera celda enlaza la carpeta de la fase, o None."""
    patron = re.compile(r"(?m)^\|\s*\[[^\]]*\]\(" + re.escape(nombre_fase)
                        + r"/?(?:README\.md)?\)\s*\|.*$")
    return patron.search(texto)


def _con_ultima_celda(fila, nueva):
    celdas = fila.strip().strip("|").split("|")
    celdas[-1] = " " + nueva + " "
    return "|" + "|".join(celdas) + "|"


def propagar(resultado, fecha, escribir=True):
    """Copia el veredicto a los tres sitios. Devuelve `(tocados, avisos)`.

    `tocados` son rutas reescritas; `avisos` lo que no se pudo hacer y por qué,
    para que el enganche lo diga en vez de callar.
    """
    resultado = os.path.abspath(resultado)
    fase = os.path.dirname(resultado)
    nombre = os.path.basename(fase)
    if os.path.basename(resultado) != RESULTADO or not fases._FASE.match(nombre):
        return [], []
    if not os.path.isfile(resultado):
        return [], []
    concepto, conteo = leer_veredicto(resultado)
    if concepto not in ("cumple", "no cumple"):
        return [], []                   # un borrador no es un veredicto
    estado = texto_del_estado(concepto, conteo, fecha)
    tocados, avisos = [], []

    carpeta_hu = os.path.dirname(fase)
    hus = [n for n in os.listdir(carpeta_hu)
           if n.startswith("HU-") and n.lower().endswith(".md")]
    if hus:
        hu_md = os.path.join(carpeta_hu, hus[0])
        texto = leer(hu_md)
        m = _fila_de_la_fase(texto, nombre)
        if m:
            nueva = _con_ultima_celda(m.group(0), estado)
            if nueva != m.group(0):
                _guardar(hu_md, texto[:m.start()] + nueva + texto[m.end():], escribir)
                tocados.append(hu_md)
        else:
            avisos.append("la historia %s no tiene fila para la fase %s en su §8"
                          % (hus[0], nombre))
    else:
        avisos.append("no hay documento de historia junto a la fase %s" % nombre)

    readme_fase = os.path.join(fase, "README.md")
    if os.path.isfile(readme_fase):
        texto = leer(readme_fase)
        linea = "**Estado:** %s. Falta el commit, que el usuario autoriza aparte." % estado
        if _ESTADO_README.search(texto):
            nuevo = _ESTADO_README.sub(lambda _: linea, texto, count=1)
        else:
            nuevo = texto.rstrip("\n") + "\n\n" + linea + "\n"
        if nuevo != texto:
            _guardar(readme_fase, nuevo, escribir)
            tocados.append(readme_fase)

    readme_hu = os.path.join(carpeta_hu, "README.md")
    if os.path.isfile(readme_hu):
        texto = leer(readme_hu)
        m = _fila_de_la_fase(texto, nombre)
        if m:
            celdas = m.group(0).strip().strip("|").split("|")
            vieja = celdas[-1].strip()
            prefijo = vieja.split(". ", 1)[0] + ". " if ". " in vieja else ""
            nueva = _con_ultima_celda(m.group(0), prefijo + estado)
            if nueva != m.group(0):
                _guardar(readme_hu, texto[:m.start()] + nueva + texto[m.end():], escribir)
                tocados.append(readme_hu)
    return tocados, avisos


def _guardar(ruta, texto, escribir):
    if not escribir:
        return
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


if __name__ == "__main__":
    comun.no_es_punto_de_entrada()
