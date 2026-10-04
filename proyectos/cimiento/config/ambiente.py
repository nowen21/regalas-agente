# -*- coding: utf-8 -*-
"""Lee el `.env` de esta máquina y lo pone en el ambiente del proceso.

**El archivo existía y nadie lo leía.** `.env.example` decía «copiar a `.env` y
llenar», y los ajustes lo buscaban con `os.environ.get(...)` — que lee el
ambiente del proceso, no el archivo. Quien copiara el ejemplo y lo llenara no
cambiaba nada, y no había forma de notarlo: la clave de desarrollo funciona.

**Sin dependencia nueva.** Leer líneas `CLAVE=valor` son diez líneas; traer una
biblioteca para eso es una dependencia que hay que mantener, auditar y explicar.

**El ambiente gana sobre el archivo, y no al revés.** Poner una variable al
correr una vez es la forma normal de pisar lo de siempre; si el archivo ganara,
esa variable no serviría para nada y costaría media hora entender por qué.

**El `.env` no entra al repositorio** (`00·N6`), y por eso el puerto vive ahí:
es de esta máquina, y en otra el 8015 puede estar ocupado.
"""
import io
import os


def cargar(ruta):
    """Pone en el ambiente lo que el archivo declare. Devuelve qué puso.

    Si el archivo no está, no pasa nada y no falla: correr sin `.env` es el caso
    normal de una máquina recién clonada.
    """
    puestas = {}
    try:
        with io.open(ruta, encoding="utf-8", errors="replace") as abierto:
            lineas = abierto.readlines()
    except OSError:
        return puestas

    for linea in lineas:
        limpia = linea.strip()
        if not limpia or limpia.startswith("#") or "=" not in limpia:
            continue
        clave, valor = limpia.split("=", 1)
        clave = clave.strip()
        valor = valor.strip().strip('"').strip("'")
        if not clave or not valor:
            continue
        # Lo que ya viene del ambiente manda: es como se pisa por una corrida.
        if clave in os.environ:
            continue
        os.environ[clave] = valor
        puestas[clave] = valor
    return puestas
