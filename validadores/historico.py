#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escribe la transcripción de la sesión en `historico-chat/`.

Esto no comprueba nada: **escribe**. Es la excepción al principio de que los
validadores solo verifican, y por un motivo concreto — la regla dice que toda
sesión queda registrada, y mientras eso dependa de que el agente se acuerde de
hacerlo, no se cumple siempre. Aquí lo hace el programa.

Dos entradas, una por cada momento del diálogo:

  - `anotar_usuario` — lo escribe el enganche `UserPromptSubmit`, con el mensaje
    tal como lo envió el usuario.
  - `anotar_agente` — lo escribe el enganche `Stop`, leyendo del transcript de
    Claude Code el texto que el agente acaba de responder.

La hora sale del reloj de la máquina en el instante en que ocurre cada cosa, que
es justo lo que un agente no puede garantizar de memoria.

Cómo se sabe a qué archivo va cada sesión: la primera línea del archivo lleva
`<!-- sesion: <id> -->`. Se busca esa marca, no el nombre — así el archivo se
puede renombrar (para ponerle el tema real) sin que la sesión pierda el hilo.
"""
import json
import os
import re
from datetime import datetime

CARPETA = "historico-chat"
INDICE = "README.md"

_NUMERO = re.compile(r"^### (\d+) · ", re.MULTILINE)


def anotar_usuario(raiz, sesion, mensaje):
    """Agrega el mensaje del usuario. Devuelve la ruta escrita, o "" si no aplica."""
    if not (mensaje or "").strip():
        return ""
    ruta = _archivo(raiz, sesion, crear=True)
    if not ruta:
        return ""

    texto = _leer(ruta)
    numero = _siguiente_numero(texto)
    cita = "\n".join(f"> {l}" if l.strip() else ">"
                     for l in mensaje.rstrip().splitlines())
    _anotar(ruta, f"\n### {numero} · Usuario — {_ahora()}\n{cita}\n")
    return ruta


def anotar_agente(raiz, sesion, transcript):
    """Agrega la respuesta del agente leída del transcript. Ruta escrita, o ""."""
    respuesta, marca = ultima_respuesta(transcript)
    if not respuesta:
        return ""
    ruta = _archivo(raiz, sesion, crear=False)
    if not ruta:
        return ""                       # sin mensaje previo no hay dónde escribir

    texto = _leer(ruta)
    if marca and f"<!-- agente: {marca} -->" in texto:
        return ""                       # ya estaba: el enganche puede repetirse
    sello = f"\n<!-- agente: {marca} -->" if marca else ""
    _anotar(ruta, f"\n**Agente** — {_ahora()}{sello}\n\n{respuesta}\n")
    return ruta


def ultima_respuesta(transcript):
    """El texto que el agente respondió en el último turno, y su identificador.

    Se recorre el transcript de atrás hacia adelante y se juntan los bloques de
    texto del agente hasta topar con un mensaje real del usuario. "Real" importa:
    los resultados de herramientas también viajan como mensajes de usuario, y si
    se cortara ahí solo quedaría el último párrafo de una respuesta larga.

    No se guarda el razonamiento ni la salida de herramientas: el histórico es la
    conversación, no la máquina por dentro.
    """
    if not transcript or not os.path.isfile(transcript):
        return "", ""

    entradas = []
    with open(transcript, encoding="utf-8", errors="replace") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            try:
                entradas.append(json.loads(linea))
            except (json.JSONDecodeError, ValueError):
                continue

    partes, marca = [], ""
    for dato in reversed(entradas):
        if dato.get("isSidechain"):
            continue                    # los subagentes no son el diálogo
        if _es_usuario(dato):
            break
        if dato.get("type") != "assistant":
            continue
        textos = [b.get("text", "") for b in _bloques(dato)
                  if b.get("type") == "text" and b.get("text", "").strip()]
        if not textos:
            continue
        if not marca:
            marca = dato.get("uuid") or ""
        partes.insert(0, "\n\n".join(t.strip() for t in textos))

    return "\n\n".join(partes), marca


def _es_usuario(dato):
    """Un mensaje escrito por la persona, no un resultado de herramienta."""
    if dato.get("type") != "user":
        return False
    contenido = (dato.get("message") or {}).get("content")
    if isinstance(contenido, str):
        return True
    if isinstance(contenido, list):
        return any(b.get("type") != "tool_result"
                   for b in contenido if isinstance(b, dict))
    return False


def _bloques(dato):
    contenido = (dato.get("message") or {}).get("content")
    if isinstance(contenido, list):
        return [b for b in contenido if isinstance(b, dict)]
    return []


def _archivo(raiz, sesion, crear):
    """La ruta del archivo de esta sesión; lo crea si hace falta y se permite.

    Si el proyecto no tiene carpeta `historico-chat/`, no se inventa: significa
    que ese proyecto no lleva histórico y el enganche no tiene nada que hacer.
    """
    carpeta = os.path.join(raiz, CARPETA)
    if not os.path.isdir(carpeta):
        return ""

    marca = f"<!-- sesion: {sesion} -->"
    for nombre in sorted(os.listdir(carpeta)):
        if not nombre.lower().endswith(".md") or nombre == INDICE:
            continue
        ruta = os.path.join(carpeta, nombre)
        if marca in _leer(ruta):
            return ruta

    return _crear(carpeta, sesion) if crear and sesion else ""


def _crear(carpeta, sesion):
    fecha = datetime.now().strftime("%Y-%m-%d")
    previas = [n for n in os.listdir(carpeta)
               if n.startswith(f"{fecha}-") and n.lower().endswith(".md")]
    sufijo = "" if not previas else f"-{len(previas) + 1}"
    nombre = f"{fecha}-sesion{sufijo}.md"
    ruta = os.path.join(carpeta, nombre)

    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(f"<!-- sesion: {sesion} -->\n\n"
                f"# {fecha} — Sesión\n\n"
                "## Conversación\n")

    _indexar(carpeta, nombre, fecha)
    return ruta


def _indexar(carpeta, nombre, fecha):
    """Agrega la línea al índice del README. Si no hay índice, no pasa nada."""
    ruta = os.path.join(carpeta, INDICE)
    if not os.path.isfile(ruta):
        return
    texto = _leer(ruta)
    if f"({nombre})" in texto:
        return
    linea = f"- [{nombre}]({nombre}) — sesión del {fecha}.\n"
    _agregar(ruta, linea if texto.endswith("\n") else f"\n{linea}")


def _siguiente_numero(texto):
    numeros = [int(n) for n in _NUMERO.findall(texto)]
    return max(numeros) + 1 if numeros else 1


def _ahora():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def _leer(ruta):
    try:
        with open(ruta, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def _agregar(ruta, texto):
    with open(ruta, "a", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def _anotar(ruta, bloque):
    """Mete el bloque al final de la conversación, no al final del archivo.

    La plantilla cierra con `## Abierto`, y ahí la diferencia importa: pegar al
    final dejaría los mensajes nuevos por debajo de esa sección. Si el archivo
    no la tiene, el final del archivo es el final de la conversación.
    """
    texto = _leer(ruta)
    corte = texto.find("\n## Abierto")
    if corte < 0:
        _agregar(ruta, bloque)
        return
    nuevo = (f"{texto[:corte].rstrip()}\n"
             f"{bloque.rstrip()}\n\n"
             f"{texto[corte:].lstrip()}")
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(nuevo)
