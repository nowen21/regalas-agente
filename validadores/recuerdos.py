#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Los recuerdos del agente viven en el repositorio, no en la herramienta.

Claude Code guarda lo que el agente debe recordar entre sesiones en una carpeta
propia, **fuera** del proyecto:

    ~/.claude/projects/<ruta-del-proyecto-con-guiones>/memory/

Ahí no sirve: no se ve en `git`, no se puede revisar en un cambio, no se
versiona y no viaja a otra máquina. El día que el proyecto se clona en otro
equipo, la memoria se queda atrás y nadie se entera.

Este módulo hace que esa carpeta quede **vacía**: cada recuerdo se **mueve** a
`historico-chat/memory/` del proyecto, que sí se versiona. Es la norma `01·C19`.

Mover y no copiar es lo que evita la trampa: dos copias del mismo recuerdo
terminan diciendo cosas distintas, y la que manda es la que nadie puede leer.

**Nada se borra.** Un recuerdo que ya existe tiene que seguir existiendo — es la
razón entera de haberlo traído al repositorio. Si el nombre ya está ocupado, el
que llega entra como `<nombre>-local.md` y decide el usuario.

**El almacén puede estar enlazado** a `historico-chat/memory/` con un *junction*
o un enlace simbólico. Ahí la herramienta ya escribe dentro del repositorio: la
norma está cumplida, no hay nada que mover, y hacerlo sería mover cada archivo
sobre sí mismo. Por eso todo lo de aquí pregunta primero si las dos rutas son el
mismo sitio en disco, no si se escriben igual.

No confundir con la memoria por señales (`13·DOC5`, la base de `memoria/`):
aquella guarda lo que el **proyecto** aprendió; esta, cómo quiere el usuario que
el **agente** trabaje.
"""
import comun
import os
import re
import shutil

CARPETA = os.path.join("historico-chat", "memory")
INDICE = "memory.md"

# Claude Code nombra la carpeta del proyecto reemplazando por `-` todo lo que no
# sea letra o dígito ASCII — incluidos los acentos:
#   c:\Ing. Jose\ia\agente  ->  c--Ing--Jose-ia-agente
_NO_ALFANUM = re.compile(r"[^A-Za-z0-9]")

# Sufijo para el recuerdo que llega con un nombre ya ocupado. No se pisa nada:
# lo local puede ser una versión distinta, y decidir cuál manda es del usuario.
_SUFIJO = "-local"


def carpeta_local(proyecto, casa=None):
    """Dónde guarda la herramienta la memoria de este proyecto."""
    slug = _NO_ALFANUM.sub("-", os.path.abspath(proyecto))
    return os.path.join(casa or os.path.expanduser("~"),
                        ".claude", "projects", slug, "memory")


def carpeta_repo(proyecto):
    """Dónde debe vivir: `historico-chat/memory/` del proyecto."""
    return os.path.join(os.path.abspath(proyecto), *CARPETA.split(os.sep))


def ruta_indice(proyecto):
    return os.path.join(carpeta_repo(proyecto), INDICE)


def indice_presente(proyecto):
    """¿Ya hay índice? Sin distinguir mayúsculas, a propósito.

    En Windows `MEMORY.md` —el índice que escribe la herramienta— y `memory.md`
    son el mismo archivo. Preguntar por el nombre exacto haría que el instalador
    creyera que falta y lo escribiera encima.
    """
    carpeta = carpeta_repo(proyecto)
    if not os.path.isdir(carpeta):
        return False
    return INDICE.lower() in {n.lower() for n in os.listdir(carpeta)}


def _es_el_mismo(uno, otro):
    """¿Las dos rutas son el **mismo** archivo o carpeta en disco?

    No basta comparar los textos de las rutas: un *junction* de Windows —o un
    enlace simbólico— hace que dos rutas distintas apunten al mismo sitio.
    """
    try:
        if os.path.exists(uno) and os.path.exists(otro):
            return os.path.samefile(uno, otro)
    except OSError:
        pass
    return (os.path.normcase(os.path.realpath(uno))
            == os.path.normcase(os.path.realpath(otro)))


def enlazada(proyecto, casa=None):
    """¿El almacén de la herramienta **es** la carpeta del repositorio?

    Se resuelve enlazando una a la otra: entonces la herramienta escribe
    directamente dentro del repositorio y `01·C19` ya está cumplido — no hay
    nada que mover, y tratar de moverlo sería mover un archivo sobre sí mismo.
    """
    return _es_el_mismo(carpeta_local(proyecto, casa), carpeta_repo(proyecto))


def sueltos(proyecto, casa=None):
    """Los archivos que quedaron en la carpeta de la herramienta.

    Vacío = no hay nada que mover, que es como tiene que estar siempre. Con el
    almacén enlazado a la carpeta del repositorio también es vacío: esos
    archivos ya están donde deben.
    """
    local = carpeta_local(proyecto, casa)
    if not os.path.isdir(local) or enlazada(proyecto, casa):
        return []
    return [os.path.join(local, n) for n in sorted(os.listdir(local))
            if os.path.isfile(os.path.join(local, n))]


def _libre(carpeta, nombre):
    """Un nombre que no choque con nada de `carpeta`.

    La comparación es sin distinguir mayúsculas a propósito: en Windows
    `MEMORY.md` y `memory.md` son **el mismo archivo**, y mover uno sobre otro
    borraría el índice del proyecto sin decir nada.
    """
    ocupados = {n.lower() for n in os.listdir(carpeta)} \
        if os.path.isdir(carpeta) else set()
    if nombre.lower() not in ocupados:
        return nombre

    base, ext = os.path.splitext(nombre)
    candidato = f"{base}{_SUFIJO}{ext}"
    n = 2
    while candidato.lower() in ocupados:
        candidato = f"{base}{_SUFIJO}-{n}{ext}"
        n += 1
    return candidato


def migrar(proyecto, aplicar=True, casa=None):
    """Vacía la carpeta de la herramienta hacia `historico-chat/memory/`.

    Devuelve `[(nombre_de_origen, nombre_de_destino)]`.

    **Aquí no se borra nada, nunca.** Todo lo que hay en el almacén se mueve;
    si el nombre ya está ocupado, entra como `<nombre>-local.md` y decide el
    usuario cuál manda. Un recuerdo que ya existe tiene que seguir existiendo:
    esa es toda la razón de haberlo traído al repositorio.

    La versión anterior borraba el archivo del almacén cuando era idéntico a
    uno del repositorio —"no se pierde nada, queda el del repo"— y con eso
    destruyó memoria real: si el almacén es un *junction* a la carpeta del
    repositorio, los dos son **el mismo archivo**, compararlos da idéntico
    siempre y el borrado se lleva el único ejemplar.
    """
    pendientes = sueltos(proyecto, casa)
    if not pendientes:
        return []

    destino_carpeta = carpeta_repo(proyecto)
    movidos = []
    for origen in pendientes:
        nombre = os.path.basename(origen)
        # Cinturón, además del de `sueltos`: mover un archivo sobre sí mismo
        # es la forma de perderlo.
        if _es_el_mismo(origen, os.path.join(destino_carpeta, nombre)):
            continue

        nuevo = _libre(destino_carpeta, nombre)
        movidos.append((nombre, nuevo))
        if aplicar:
            os.makedirs(destino_carpeta, exist_ok=True)
            shutil.move(origen, os.path.join(destino_carpeta, nuevo))
    return movidos


def pasos(movidos):
    """Los movimientos, dichos en una línea cada uno."""
    salida = []
    ruta = CARPETA.replace(os.sep, "/")
    for nombre, destino in movidos:
        if destino == nombre:
            salida.append(f"mover `{nombre}` a `{ruta}/`")
        else:
            salida.append(f"mover `{nombre}` a `{ruta}/{destino}` "
                          f"— el nombre ya estaba ocupado; revisar cuál manda")
    return salida


def contexto(proyecto):
    """La memoria del agente, para inyectarla al abrir la sesión.

    Va el índice completo —es corto y dice de qué trata cada recuerdo—, no los
    recuerdos enteros: el agente abre el que le toca.

    Sin esto, la memoria que pasó al repositorio no la vería nadie: la
    herramienta solo carga sola lo que guarda ella, y ahí ya no hay nada.
    """
    archivo = ruta_indice(proyecto)
    if not os.path.isfile(archivo):
        return ""
    try:
        with open(archivo, encoding="utf-8", errors="replace") as f:
            texto = f.read()
    except OSError:
        return ""

    ruta = CARPETA.replace(os.sep, "/")
    return ("[MEMORIA DEL AGENTE — ÍNDICE, OBLIGATORIA]\n"
            "Es cómo pide el usuario que se trabaje en este proyecto, y rige "
            "esta sesión completa. Antes de tocar un tema que aparezca abajo, "
            "leer con Read el archivo del recuerdo: el índice dice de qué "
            "trata, no qué exige.\n"
            f"Un recuerdo nuevo se escribe en `{ruta}/`, nunca en el almacén de "
            "la herramienta (`01·C19`).\n\n"
            f"<<< {ruta}/{INDICE} >>>\n{texto}")


def revisar(proyecto, casa=None):
    """¿La carpeta de la herramienta está vacía? Devuelve `(cumple, detalle)`."""
    quedaron = sueltos(proyecto, casa)
    if not quedaron:
        return True, ""
    nombres = ", ".join(os.path.basename(r) for r in quedaron[:4])
    if len(quedaron) > 4:
        nombres += f" y {len(quedaron) - 4} más"
    local = carpeta_local(proyecto, casa).replace(os.sep, "/")
    return False, (f"quedaron {len(quedaron)} archivo(s) en la memoria local de "
                   f"la herramienta ({nombres}) — `{local}`; la memoria va en "
                   f"`{CARPETA.replace(os.sep, '/')}/` (`01·C19`)")


if __name__ == "__main__":
    # `53` · Un modulo que se ejecuta solo y no imprime nada dice, con su
    # silencio, lo mismo que diria si hubiera comprobado y estuviera todo bien.
    comun.no_es_punto_de_entrada()
