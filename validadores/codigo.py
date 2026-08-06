#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recorrer el código versionado de un proyecto.

Base común de los validadores que escanean **contenido** (errores, rendimiento,
esquema…): entrega, por cada archivo de código versionado, su ruta mostrada y su
texto. Se apoya en `git ls-files` (lo registrado, no lo que hay suelto en disco)
y salta lo que es de terceros o generado.

No opina sobre nada: solo recorre. La regla la aplica cada validador.
"""
import os
import re

import instalar
import versionado
from comun import leer

# Extensiones de código/config que vale la pena abrir. Deja fuera binarios,
# imágenes, lockfiles y documentación.
EXTENSIONES = {
    ".php", ".py", ".js", ".ts", ".jsx", ".tsx", ".mjs", ".cjs", ".vue",
    ".rb", ".go", ".java", ".kt", ".cs", ".rs", ".swift", ".scala", ".sql",
}

# Se salta lo de terceros y lo generado. Incluye las raíces web de assets
# construidos/vendorizados (`public/`, `static/`, `staticfiles/`): el código
# fuente vive en `app/`, `resources/`, `src/`…, no ahí. Un secreto en `public/`
# sí importa, pero de eso se ocupa `secretos.py` (que no usa este filtro); acá
# se buscan olores de código, y esos árboles son salida, no fuente.
_SALTAR = re.compile(
    r"(^|/)(vendor|node_modules|dist|build|\.git|public|static|staticfiles)/|"
    r"\.min\.(js|css)$")


def linea_de(texto, pos):
    """Número de línea (1-based) del carácter en `pos`. Para reportar un
    hallazgo detectado escaneando el texto entero, no línea por línea."""
    return texto.count("\n", 0, pos) + 1


def archivos(raiz, extensiones=None):
    """Genera `(ruta_mostrada, texto)` por cada archivo de código versionado."""
    exts = extensiones or EXTENSIONES
    raiz = os.path.abspath(raiz)
    for repo in instalar.repositorios_git(raiz):
        etiqueta = os.path.relpath(repo, raiz).replace("\\", "/")
        prefijo = "" if etiqueta == "." else f"{etiqueta}/"
        for a in versionado.archivos_versionados(repo):
            if _SALTAR.search(a):
                continue
            if os.path.splitext(a)[1].lower() not in exts:
                continue
            try:
                texto = leer(os.path.join(repo, a))
            except OSError:
                continue
            yield f"{prefijo}{a}", texto
