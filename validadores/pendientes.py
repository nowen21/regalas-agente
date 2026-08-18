#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La numeración de `pendientes/` — EP-004 · HU-018.

Un pendiente se numera por el orden en que conviene ejecutarlo, y su número
**no se reutiliza nunca**: los huecos son historia y los pendientes se citan
entre sí por número. Abrir uno con un número ya tomado rompe esas citas sin
que nadie se entere, porque los dos archivos existen y ninguno se pisa.

Esto comprueba tres cosas:

1. **Cuál es el próximo número libre**, para no tener que mirar la carpeta.
2. **Que ningún número esté repetido**, contando también los cerrados de
   `hecho/`: un número liberado por cerrarse sigue tomado.
3. **Que la carpeta y el índice digan lo mismo**, en los dos sentidos.

    python validadores/validar.py pendientes
"""
import os
import re

import comun
from comun import AVISO, FALLA, Hallazgo

CARPETA = "pendientes"
CERRADOS = "hecho"
INDICE = "README.md"

# `07-persona-no-admite-homonimos.md` → 7. Los ceros a la izquierda no cambian
# el número: `07` y `7` son el mismo, y tenerlos como dos distintos dejaría
# pasar justo el choque que esto busca.
_NUMERADO = re.compile(r"^(\d+)-(.+)\.md$")


def _leer(ruta):
    """El texto del archivo, o "" si no está o no se puede leer.

    No se usa `comun.leer` a propósito: hoy revienta con el archivo ausente o
    mal codificado, y esta comprobación tiene que poder correr sobre una
    carpeta de pendientes que todavía no tiene índice. Es el defecto `D-01` de
    la fase `A-EP-004-HU-003`, que se arregla en su propia fase `B`.
    """
    try:
        with open(ruta, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def _archivos(carpeta):
    if not os.path.isdir(carpeta):
        return []
    return sorted(n for n in os.listdir(carpeta)
                  if n.endswith(".md") and n != INDICE
                  and os.path.isfile(os.path.join(carpeta, n)))


def numerados(proyecto):
    """`{numero: [nombres]}` de los archivos numerados de la carpeta."""
    raiz = os.path.join(os.path.abspath(proyecto), CARPETA)
    encontrados = {}
    for carpeta in (raiz, os.path.join(raiz, CERRADOS)):
        for nombre in _archivos(carpeta):
            m = _NUMERADO.match(nombre)
            if m:
                encontrados.setdefault(int(m.group(1)), []).append(nombre)
    return encontrados


def numeros_del_indice(proyecto):
    """Los números que el índice registra, **incluidos los cerrados**.

    Es la única memoria completa de la numeración. Al cerrar un pendiente su
    archivo se mueve a `hecho/` y **pierde el número** —`02-vigencia…md` pasa a
    `vigencia-y-poda-de-memoria.md`—, así que mirando solo la carpeta el 02
    parece libre. Lo que lo conserva es la fila tachada del índice: `~~02~~`.
    """
    indice = _leer(os.path.join(os.path.abspath(proyecto), CARPETA, INDICE))
    return {int(n) for n in re.findall(r"^\|\s*~*(\d+)~*\s*\|", indice, re.M)}


def tomados(proyecto):
    """Todos los números que **no se pueden reutilizar**: los de la carpeta y
    los que el índice recuerda de los ya cerrados."""
    return set(numerados(proyecto)) | numeros_del_indice(proyecto)


def sin_numero(proyecto):
    """Los `.md` de `pendientes/` que no empiezan por un número."""
    raiz = os.path.join(os.path.abspath(proyecto), CARPETA)
    return [n for n in _archivos(raiz) if not _NUMERADO.match(n)]


def proximo_libre(proyecto):
    """El siguiente número que se puede usar sin pisar a nadie.

    **El siguiente al mayor, no el primer hueco.** El índice dice que «el
    número no se reutiliza ni se renumeran los demás: los huecos son historia»,
    y los pendientes se citan entre sí por número. Entregar un hueco haría que
    «el 02» apuntara a dos cosas distintas según cuándo se leyera.
    """
    ocupados = tomados(proyecto)
    return max(ocupados) + 1 if ocupados else 1


def validar(proyecto):
    proyecto = os.path.abspath(proyecto)
    raiz = os.path.join(proyecto, CARPETA)
    hallazgos = []

    if not os.path.isdir(raiz):
        return [Hallazgo(FALLA, CARPETA, 0,
                         "no existe la carpeta de pendientes (HU-018)")]

    # CA-02 · el número repetido.
    for numero, nombres in sorted(numerados(proyecto).items()):
        if len(nombres) > 1:
            hallazgos.append(Hallazgo(
                FALLA, f"{CARPETA}/", 0,
                f"el número {numero} está tomado por {len(nombres)} pendientes: "
                + ", ".join(f"`{n}`" for n in nombres)
                + " — un número no se reutiliza (HU-018)"))

    # Transversal de errores · el nombre que no se puede interpretar se
    # reporta y **no detiene**: un archivo suelto no puede invalidar la
    # comprobación de los otros cuarenta.
    for nombre in sin_numero(proyecto):
        hallazgos.append(Hallazgo(
            AVISO, f"{CARPETA}/{nombre}", 0,
            "no empieza por un número, así que no entra en la numeración (HU-018)"))

    # CA-03 · la carpeta y el índice, en los dos sentidos.
    indice = _leer(os.path.join(raiz, INDICE))
    if indice:
        enlazados = set(re.findall(r"\]\(([^)]+\.md)\)", indice))
        propios = {e for e in enlazados if "/" not in e and e != INDICE}
        for nombre in _archivos(raiz):
            if nombre not in propios:
                hallazgos.append(Hallazgo(
                    AVISO, f"{CARPETA}/{nombre}", 0,
                    f"no aparece en `{CARPETA}/{INDICE}` (HU-018)"))
        for nombre in sorted(propios - set(_archivos(raiz))):
            hallazgos.append(Hallazgo(
                AVISO, f"{CARPETA}/{INDICE}", 0,
                f"el índice enlaza `{nombre}`, que no está en la carpeta (HU-018)"))

    return hallazgos


def linea_proximo(proyecto):
    """La línea que dice el próximo número libre — CA-01."""
    if not os.path.isdir(os.path.join(os.path.abspath(proyecto), CARPETA)):
        return ""
    ocupados = tomados(proyecto)
    abiertos = len(numerados(proyecto))
    return (f"Pendientes: {abiertos} con archivo · {len(ocupados)} números "
            f"tomados · el próximo libre es el {proximo_libre(proyecto):02d} (HU-018)")


if __name__ == "__main__":
    # `53` · Un modulo que se ejecuta solo y no imprime nada dice, con su
    # silencio, lo mismo que diria si hubiera comprobado y estuviera todo bien.
    comun.no_es_punto_de_entrada("pendientes")
