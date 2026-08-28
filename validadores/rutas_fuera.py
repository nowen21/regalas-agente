# -*- coding: utf-8 -*-
"""`EP-005·HU-018` · Avisa cuando el agente escribe fuera del proyecto.

**La regla ya existía y se incumplió cuatro días seguidos.** [`04·S9`](../base/04-seguridad.md)
dice que el agente escribe solo dentro de la carpeta del proyecto. El usuario lo
precisó el 2026-08-22 —*«nada se debe escribir por fuera, todo debe quedar en
historico-chat»*— y **se dejó de cumplir el 24**: 38 guiones en la carpeta
temporal del sistema, más dos clones enteros de la plataforma (`S-057`).

**Lo que fallaba no era la regla: era que nada la hacía cumplir.** Y hay algo
peor que el olvido — la herramienta ofrece una carpeta temporal en cada sesión y
la nombra como el sitio recomendado, así que **el camino cómodo apunta al lado
contrario de la regla**.

## Por qué se compara por partes y no por prefijo

`.../agente` es prefijo de `.../agente-viejo`. Un `startswith` sobre la ruta da
la carpeta hermana por dentro del proyecto, y ahí el aviso **calla justo donde
debía hablar**. Se comparan los tramos de la ruta, que es lo que no se engaña.

## Por qué ante la duda no se acusa

Si la ruta no se puede resolver, se calla. Es `04·R4`: no se afirma sobre lo
que no se pudo leer. **Un aviso falso vale menos que uno que falta**: el agente
escribe decenas de archivos del proyecto por sesión, y un solo falso positivo
por sesión convierte esto en ruido — que se apaga, y con él lo que sí avisaba.

**Avisa, no mueve ni borra** (`EP-004 §10.2`). Mover un archivo que el agente
acaba de escribir rompe lo que estaba haciendo, y esconde el incumplimiento en
vez de mostrarlo.
"""
import os

# Dónde van los guiones de apoyo. Se nombra en el aviso porque un aviso que
# no dice qué hacer se aprende a ignorar.
DESTINO = "historico-chat/scripts/AAAA-MM-DD/"


def _partes(ruta):
    """Los tramos de una ruta, normalizados para comparar.

    `normcase` es lo que hace que en Windows `C:\\Ing` y `c:\\ing` sean la
    misma carpeta, y en Linux no.
    """
    normal = os.path.normcase(os.path.normpath(ruta))
    return [tramo for tramo in normal.replace("\\", "/").split("/") if tramo]


def dentro_del_proyecto(ruta, proyecto):
    """`True` si `ruta` cae dentro de `proyecto` — **o si no se pudo saber**.

    La duda se resuelve callando: ver `04·R4` y el porqué del módulo.
    """
    # `strip()` y no solo `not ruta`: una ruta de puros espacios no es una
    # ruta, y sin esto se acusaba de estar fuera. Lo cazó su propia prueba.
    if not (ruta or "").strip() or not (proyecto or "").strip():
        return True
    try:
        suya = _partes(os.path.realpath(os.path.abspath(ruta)))
        casa = _partes(os.path.realpath(os.path.abspath(proyecto)))
    except (OSError, ValueError, TypeError):
        return True
    if not casa:
        return True
    return suya[:len(casa)] == casa


def aviso(ruta, proyecto):
    """El texto que se muestra, o `""` si la ruta está donde debe.

    Dice **la ruta escrita y dónde debía ir**, que son las dos mitades: sin la
    primera no se sabe qué archivo, y sin la segunda hay que ir a buscarlo.
    """
    if dentro_del_proyecto(ruta, proyecto):
        return ""
    return (
        "[AVISO] se escribió fuera del proyecto: %s — los guiones de apoyo van "
        "en `%s`, y se quedan ahí versionados (`04·S9`, EP-005·HU-018). "
        "Leer fuera sí vale; escribir, no." % (ruta, DESTINO))
