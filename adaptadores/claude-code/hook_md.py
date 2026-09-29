#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganche para Claude Code: revisa los enlaces tras editar un `.md`.

Se conecta como hook `PostToolUse` sobre `Write|Edit` en `.claude/settings.json`.
Lee por la entrada estándar el JSON que envía Claude Code y:

  - anota que esta sesión tocó ese archivo, sea cual sea su extensión, para
    que un commit de otra sesión no se lo lleve sin darse cuenta (`80`);
  - si el archivo editado NO es un `.md` del proyecto -> no hace nada más;
  - si lo es -> comprueba enlaces e índices de ese proyecto, y mide las
    marcas de redacción de **lo que se acaba de escribir** (`00·ID8`).

**Las marcas se miden en el momento de escribir** (`EP-004·HU-012·CA-05`).
Antes solo las contaba el `pre-commit`, cuando el documento ya se había
entregado. Se mide el texto escrito (`content` de `Write`, `new_string` de
`Edit`) y no el archivo entero: el archivo trae marcas viejas, y repetirlas
en cada edición es ruido que se deja de leer. Son aviso, no falla: le llegan
al agente por su contexto y no detienen nada.

    python hook_md.py [--raiz <carpeta del proyecto>]

Sin `--raiz` revisa el repositorio del estándar. Con `--raiz` revisa el proyecto
indicado — así el mismo archivo sirve para todos los proyectos sin copiarse.

Sin dependencias externas: en esta máquina no hay `jq`, y de todos modos hacerlo
en Python evita depender de qué trae instalado cada equipo.

Códigos de salida:
  0 — todo bien, no aplicaba, o solo hay marcas: esas van por el contexto.
  2 — hay enlaces rotos; Claude Code se lo devuelve al modelo para que los
      corrija, y si hay marcas se nombran en el mismo mensaje.
"""
import json
import os
import sys

# **Vive en el adaptador, no en `validadores/`.** Por eso tiene que decir
# dónde están los módulos que usa: el trabajo es agnóstico y sigue allá;
# acá sólo está lo que habla con esta herramienta.
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "validadores"))

import enlaces
import marcas                                           # noqa: E402
import sesiones                                          # noqa: E402
from comun import FALLA, RAIZ, preparar_salida          # noqa: E402


def raiz_pedida(argv):
    """La carpeta a revisar: `--raiz X`, o el estándar si no se indica."""
    if "--raiz" in argv:
        i = argv.index("--raiz")
        if i + 1 < len(argv):
            return os.path.abspath(argv[i + 1])
    return RAIZ


def archivo_editado(datos):
    """La ruta del archivo, mirando primero la entrada y luego la respuesta."""
    entrada = datos.get("tool_input") or {}
    respuesta = datos.get("tool_response") or {}
    return (entrada.get("file_path")
            or respuesta.get("filePath")
            or respuesta.get("file_path")
            or "")


def texto_escrito(datos):
    """Lo que se acaba de escribir: el `content` de `Write`, o los `new_string`
    de `Edit` y de `MultiEdit`."""
    entrada = datos.get("tool_input") or {}
    if entrada.get("content") is not None:
        return entrada.get("content") or ""
    partes = [entrada.get("new_string") or ""]
    partes += [e.get("new_string") or "" for e in entrada.get("edits") or []]
    return "\n".join(p for p in partes if p)


# Hasta cuántas marcas se nombran una por una. Más que eso tapa el aviso.
TOPE_MARCAS = 15


def aviso_de_marcas(ruta, texto):
    """El aviso de las marcas de lo recién escrito, o `""` si no hay."""
    halladas = marcas.medir_texto(texto)
    if not halladas:
        return ""
    lineas = [f"[REDACCIÓN: LO QUE SE ACABA DE ESCRIBIR TIENE {len(halladas)} "
              f"MARCA(S) DE `00·ID8`] {os.path.basename(ruta)}",
              "Corregirlas ahora, antes de entregar. La línea cuenta desde el "
              "comienzo de lo escrito."]
    for n, _clave, nombre, lugar in halladas[:TOPE_MARCAS]:
        lineas.append(f"  línea {n}: {nombre}; en su lugar, {lugar}")
    if len(halladas) > TOPE_MARCAS:
        lineas.append(f"  y {len(halladas) - TOPE_MARCAS} más")
    return "\n".join(lineas)


def es_md_de(ruta, raiz):
    if not ruta.lower().endswith(".md"):
        return False
    try:
        return os.path.commonpath([os.path.abspath(ruta), raiz]) == raiz
    except ValueError:      # otra unidad en Windows
        return False


def main():
    preparar_salida()
    raiz = raiz_pedida(sys.argv[1:])

    try:
        datos = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0            # sin JSON válido no hay nada que revisar

    editado = archivo_editado(datos)

    # **Se anota todo lo que se edita, no solo los `.md`.** Lo que una sesión
    # se llevó por delante la vez que pasó fue un `.py` a medio corregir. La
    # anotación no puede tumbar el enganche: si falla, el trabajo del agente
    # sigue igual y lo único que se pierde es el aviso del commit.
    try:
        sesiones.anotar(raiz, datos.get("session_id") or "", editado)
    except OSError:
        pass

    if not es_md_de(editado, raiz):
        return 0

    try:
        aviso = aviso_de_marcas(editado, texto_escrito(datos))
    except Exception:       # noqa: BLE001 — medir no puede tumbar el enganche
        aviso = ""

    hallazgos = enlaces.validar_enlaces(raiz) + enlaces.validar_indices(raiz)
    fallas = [h for h in hallazgos if h.severidad == FALLA]
    if not fallas:
        if aviso:
            print(json.dumps({"hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": aviso}}, ensure_ascii=False))
        return 0

    print("La edición dejó enlaces rotos:", file=sys.stderr)
    for h in fallas:
        print(f"  {h}", file=sys.stderr)
    if aviso:
        print(f"\n{aviso}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
