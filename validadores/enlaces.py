#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Coherencia interna del estándar: enlaces rotos e índices desactualizados.

Este validador corre sobre ESTE repositorio (el estándar), no sobre un proyecto
que lo use. Es el único que puede correr sin nada más.
"""
import os

from comun import (AVISO, FALLA, Hallazgo, RAIZ, enlaces, leer, recorrer_md,
                   relativo)

# Carpetas cuyo README.md debe listar todos sus .md.
CON_INDICE = ["pendientes", "notas"]

# Carpeta de transcripciones: se escribe sola y copia el diálogo literal.
HISTORICO = "historico-chat"

EXTERNOS = ("http://", "https://", "mailto:", "ftp://", "//")


def _es_interno(destino):
    return not (destino.startswith(EXTERNOS) or destino.startswith("#"))


def _comprobable(texto, destino):
    """¿Este enlace se puede comprobar contra el disco?

    Se descartan dos cosas, y por razones distintas:

    - Los que llevan `<...>` en el texto o el destino: son ejemplos de formato
      dentro de la documentación (`[<ruta legible>](<path-relativo>.md)`),
      no enlaces a nada.
    - Los que no apuntan a un `.md` ni a una carpeta: apuntan a código de un
      proyecto (`app/PagoService.php`), que por diseño no vive en este
      repositorio. Comprobarlos sería exigir que el estándar contenga los
      proyectos que lo usan.
    """
    if "<" in texto or ">" in texto or "<" in destino or ">" in destino:
        return False
    ruta = destino.split("#", 1)[0]
    return ruta.lower().endswith(".md") or ruta.endswith("/")


def _es_transcripcion(archivo):
    """¿Es una sesión de `historico-chat/`, y no su índice?

    Esos archivos los escribe el enganche del histórico copiando el diálogo
    **literal**, y en el chat los enlaces se escriben relativos a la raíz del
    proyecto (`validadores/README.md`), no a la carpeta donde termina la copia.
    Se rompen por definición.

    La alternativa sería reescribirlos al copiar, y eso ya no sería literal: el
    histórico dejaría de ser prueba de lo que se dijo. Se prefiere no comprobar.
    El `README.md` de la carpeta sí se comprueba — ese lo escribe una persona.
    """
    return (os.path.basename(os.path.dirname(archivo)) == HISTORICO
            and os.path.basename(archivo).lower() != "readme.md")


def validar_enlaces(raiz=None):
    """Todo enlace comprobable de un .md apunta a algo que existe."""
    raiz = raiz or RAIZ
    hallazgos = []

    for archivo in recorrer_md(raiz):
        if _es_transcripcion(archivo):
            continue
        carpeta = os.path.dirname(archivo)
        for n, texto, destino in enlaces(leer(archivo)):
            if not _es_interno(destino) or not _comprobable(texto, destino):
                continue
            # El ancla (#seccion) no se comprueba, solo el archivo.
            ruta = destino.split("#", 1)[0]
            if not ruta:
                continue
            objetivo = os.path.normpath(os.path.join(carpeta, ruta))
            if not os.path.exists(objetivo):
                hallazgos.append(Hallazgo(
                    FALLA, archivo, n, f"enlace roto: {destino}"))

    return hallazgos


def validar_indices(raiz=None, carpetas=None):
    """Cada .md de una carpeta con índice está enlazado desde su README."""
    raiz = raiz or RAIZ
    hallazgos = []

    for nombre in (carpetas or CON_INDICE):
        carpeta = os.path.join(raiz, nombre)
        indice = os.path.join(carpeta, "README.md")
        if not os.path.isfile(indice):
            continue

        texto = leer(indice)
        enlazados = {
            os.path.normpath(os.path.join(carpeta, d.split("#", 1)[0]))
            for _, _, d in enlaces(texto) if _es_interno(d)
        }

        for archivo in sorted(os.listdir(carpeta)):
            if not archivo.lower().endswith(".md") or archivo == "README.md":
                continue
            ruta = os.path.normpath(os.path.join(carpeta, archivo))
            if ruta not in enlazados:
                hallazgos.append(Hallazgo(
                    FALLA, indice, 0,
                    f"el índice no menciona {relativo(ruta)}"))

        # Y al revés: el índice no apunta a archivos que ya no existen.
        # (los enlaces rotos ya los detecta validar_enlaces; aquí solo se
        #  avisa de huérfanos dentro de la propia carpeta)
        for ruta in sorted(enlazados):
            if (os.path.dirname(ruta) == os.path.normpath(carpeta)
                    and not os.path.exists(ruta)):
                hallazgos.append(Hallazgo(
                    AVISO, indice, 0,
                    f"el índice menciona {relativo(ruta)}, que ya no existe"))

    return hallazgos
