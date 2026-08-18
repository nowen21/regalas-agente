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

Ese renombre es lo tercero que hay acá. El archivo nace `AAAA-MM-DD-sesion.md`
porque al abrir el chat nadie sabe de qué va a tratar; cuando ya hubo una
respuesta, el tema está claro y `aviso_de_nombre` le recuerda al agente que le
ponga uno. `renombrar` hace el cambio: mueve el archivo y corrige la línea del
índice, que es lo único por lo que la próxima sesión encuentra a esta.
"""
import json
import os
import re
import unicodedata
from datetime import datetime

import enmascarar

CARPETA = "historico-chat"
INDICE = "README.md"

# Cuántas sesiones se listan al arrancar. Las viejas siguen en el índice del
# README; lo que se recorta es el bloque que se le inyecta al agente.
LIMITE = 40

_NUMERO = re.compile(r"^### (\d+) · ", re.MULTILINE)

# Una línea del índice, con su resumen de sesión al final si ya lo tiene:
# `- [nombre.md](nombre.md) — de qué se trató. · [resumenes/AAAA-MM-DD/tema.md](…)`
_LINEA = re.compile(
    r"^- \[[^\]]*\]\(([^)#\s]+\.md)\)\s*(?:—\s*(.*?))?"
    r"\s*(?:·\s*\[[^\]]*\]\([^)]+\))?\s*$")

# Dónde vive el resumen de una sesión, relativo a la carpeta del histórico.
RESUMENES = "resumenes"

# Cómo se sube desde el resumen (`resumenes/AAAA-MM-DD/tema.md`) hasta la
# transcripción, que vive en la raíz de la carpeta del histórico.
HACIA_HISTORICO = "../../"

# La fecha con la que empieza el nombre del archivo de una sesión.
_FECHA = re.compile(r"^(\d{4}-\d{2}-\d{2})")

# El nombre que pone el enganche mientras no se sabe el tema: `2026-08-09-sesion.md`.
_GENERICO = re.compile(r"^\d{4}-\d{2}-\d{2}-sesion(?:-\d+)?\.md$", re.IGNORECASE)

# Queda en el archivo cuando ya se pidió el nombre, para no pedirlo otra vez.
MARCA_NOMBRE = "<!-- nombre: preguntado -->"


def anotar_usuario(raiz, sesion, mensaje):
    """Agrega el mensaje del usuario. Devuelve la ruta escrita, o "" si no aplica."""
    if not (mensaje or "").strip():
        return ""
    ruta = _archivo(raiz, sesion, crear=True)
    if not ruta:
        return ""

    texto = _leer(ruta)
    numero = _siguiente_numero(texto)
    # `EP-005·HU-002`: la clave se tapa **antes** de escribirse. Una vez en el
    # archivo ya no se borra — la transcripción se versiona.
    mensaje, _tapadas = enmascarar.enmascarar(mensaje)
    cita = "\n".join(f"> {l}" if l.strip() else ">"
                     for l in mensaje.rstrip().splitlines())
    _anotar(ruta, f"\n### {numero} · Usuario — {_ahora()}\n{cita}\n")

    # En cada mensaje, no solo al crear el archivo: la línea del índice es lo
    # único por lo que la próxima sesión encuentra a esta. Si al crearlo no
    # había README —o alguien lo rehízo—, la sesión quedaría invisible. Es
    # idempotente: si la línea ya está, no hace nada.
    carpeta = os.path.dirname(ruta)
    nombre = os.path.basename(ruta)
    _indexar(carpeta, nombre, _fecha_de(nombre))
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
    respuesta, _tapadas = enmascarar.enmascarar(respuesta)
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


def _fecha_de(nombre):
    """La fecha del nombre del archivo (`AAAA-MM-DD-tema.md`), o la de hoy."""
    m = _FECHA.match(nombre)
    return m.group(1) if m else datetime.now().strftime("%Y-%m-%d")


# ── Ponerle el tema al nombre ─────────────────────────────────────────────

def aviso_de_nombre(ruta):
    """Lo que hay que recordarle al agente para que nombre la sesión, o "".

    Se pide **una sola vez** y no en el primer mensaje: al abrir el chat ni el
    usuario ni el agente saben todavía de qué va a tratar, así que preguntar
    ahí solo gasta un turno. Se pide cuando ya hubo una respuesta —ahí el tema
    está claro— y queda la marca en el archivo para no volver a pedirlo.

    No renombra nada por su cuenta: el nombre lo aprueba el usuario.
    """
    if not ruta:
        return ""
    nombre = os.path.basename(ruta)
    if not _GENERICO.match(nombre):
        return ""                       # ya tiene tema
    texto = _leer(ruta)
    if MARCA_NOMBRE in texto or "\n**Agente**" not in texto:
        return ""                       # ya se pidió, o todavía no hay tema

    _marcar(ruta)
    orden = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "historico.py").replace(os.sep, "/")
    return "\n".join([
        "[HISTÓRICO — ESTA SESIÓN TODAVÍA NO TIENE NOMBRE]",
        f"Se está guardando en `{CARPETA}/{nombre}`, que no dice de qué trata. "
        "Ese nombre y su línea en el índice son lo único que la próxima sesión "
        "va a ver de esta.",
        "Antes de seguir, proponer en una línea el nombre y el resumen — por "
        "ejemplo: «esta sesión la guardo como "
        f"{_fecha_de(nombre)}-<tema>.md — <de qué se trató>, ¿va?».",
        "Si el usuario aprueba, correr esto, que renombra el archivo y corrige "
        "la línea del índice (las dos cosas, o el índice apunta a un archivo "
        "que ya no está):",
        f'    python "{orden}" --renombrar "{os.path.abspath(ruta).replace(os.sep, "/")}" '
        '--tema "<tema-en-guiones>" --resumen "<de qué se trató>"',
        "Y pedirle que pegue esta línea, que le pone el mismo nombre a la "
        "sesión de Claude Code —lo que se ve en la pestaña, en la barra del "
        "prompt y en `/resume`—. Es un comando del usuario: el agente no puede "
        "escribirlo por él.",
        "    /rename <tema-en-guiones>",
        "Si no quiere ponerle nombre, se deja como está. Esto se pide una sola "
        "vez en la sesión.",
    ])


def renombrar(archivo, tema, resumen=""):
    """Le pone el tema al nombre del archivo y corrige el índice. Ruta nueva.

    Las dos cosas van juntas a propósito: renombrar sin tocar el índice deja
    una línea apuntando a un archivo que ya no existe, y esa línea es por donde
    la próxima sesión llega a esta.

    La fecha no se toca — sale del nombre viejo, no del reloj: una sesión que
    se nombra al otro día sigue siendo la del día que ocurrió.
    """
    archivo = os.path.abspath(archivo)
    if not os.path.isfile(archivo):
        raise FileNotFoundError(f"no existe el archivo de sesión: {archivo}")
    if not _slug(tema):
        raise ValueError("el tema queda vacío al pasarlo a nombre de archivo")

    carpeta = os.path.dirname(archivo)
    viejo = os.path.basename(archivo)
    nuevo = _libre(carpeta, f"{_fecha_de(viejo)}-{_slug(tema)}.md", viejo)

    _titular(archivo, _fecha_de(viejo), tema)
    _mover_resumen(carpeta, viejo, nuevo)
    if nuevo != viejo:
        os.rename(archivo, os.path.join(carpeta, nuevo))
    _reindexar(carpeta, viejo, nuevo, resumen)
    return os.path.join(carpeta, nuevo)


def _mover_resumen(carpeta, viejo, nuevo):
    """Le pone el nombre nuevo al resumen de esa sesión, si ya existe.

    Va **antes** de mover la transcripción y de tocar el índice: si algo falla,
    lo que queda mal es el resumen, que se puede volver a mover, y no el índice,
    que es por donde la próxima sesión llega a esta.

    El resumen se llama igual que la transcripción sin la fecha, así que los dos
    nombres tienen que moverse juntos: renombrar solo uno deja el enlace del
    índice apuntando a un archivo que no está.
    """
    fecha = _fecha_de(viejo)
    dia = os.path.join(carpeta, RESUMENES, fecha)
    origen = os.path.join(dia, os.path.basename(viejo)[len(fecha) + 1:])
    destino = os.path.join(dia, os.path.basename(nuevo)[len(fecha) + 1:])
    if origen == destino or not os.path.isfile(origen) or os.path.exists(destino):
        return
    try:
        os.rename(origen, destino)
    except OSError:
        return                          # no poder moverlo no detiene el renombrado
    _reindexar_dia(dia, os.path.basename(origen), os.path.basename(destino))
    _reenlazar(destino, carpeta, os.path.basename(viejo), os.path.basename(nuevo))


def _reenlazar(resumen, carpeta, viejo, nuevo):
    """Deja con el nombre nuevo el enlace que el resumen le hace a su sesión.

    Mover el archivo no basta: adentro, la primera línea nombra la
    transcripción con un enlace, y ese enlace se queda apuntando al nombre que
    ya no existe. Se cambian **las dos partes** —el texto que se ve y el
    destino—, porque `13·DOC14` pide que el texto diga dónde vive el archivo:
    un enlace que abre pero se anuncia con el nombre viejo también miente.

    Se reemplaza el par exacto, no toda aparición del nombre viejo: un resumen
    puede nombrar otras sesiones, y a esas no hay que tocarles nada.
    """
    texto = _leer(resumen)
    if not texto:
        return
    hist = os.path.basename(carpeta.rstrip(os.sep + "/"))
    nuevo_texto = texto.replace(
        f"[{hist}/{viejo}]({HACIA_HISTORICO}{viejo})",
        f"[{hist}/{nuevo}]({HACIA_HISTORICO}{nuevo})")
    # Y el que lleve otro texto, que igual apunta a la misma sesión.
    nuevo_texto = nuevo_texto.replace(f"]({HACIA_HISTORICO}{viejo})",
                                      f"]({HACIA_HISTORICO}{nuevo})")
    if nuevo_texto == texto:
        return
    try:
        with open(resumen, "w", encoding="utf-8", newline="\n") as f:
            f.write(nuevo_texto)
    except OSError:
        return                          # tampoco esto detiene el renombrado


def _reindexar_dia(dia, viejo, nuevo):
    """Deja la línea del índice del día apuntando al nombre nuevo."""
    ruta = os.path.join(dia, INDICE)
    if not os.path.isfile(ruta):
        return
    texto = _leer(ruta)
    if f"({viejo})" not in texto:
        return
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto.replace(f"[{viejo}]({viejo})", f"[{nuevo}]({nuevo})"))


def _marcar(ruta):
    """Deja `MARCA_NOMBRE` bajo la marca de sesión, en la cabecera del archivo."""
    lineas = _leer(ruta).split("\n")
    lineas.insert(1 if lineas and lineas[0].startswith("<!-- sesion:") else 0,
                  MARCA_NOMBRE)
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lineas))


def _titular(ruta, fecha, tema):
    """Cambia el título `# AAAA-MM-DD — Sesión` por el tema real."""
    texto = _leer(ruta)
    nuevo = re.sub(rf"^# {re.escape(fecha)} — .*$",
                   f"# {fecha} — {_legible(tema)}", texto, count=1,
                   flags=re.MULTILINE)
    if nuevo != texto:
        with open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(nuevo)


def _reindexar(carpeta, viejo, nuevo, resumen):
    """Deja la línea del índice apuntando al nombre nuevo, con el resumen."""
    ruta = os.path.join(carpeta, INDICE)
    if not os.path.isfile(ruta):
        return
    resumen = (resumen or "").strip() or f"sesión del {_fecha_de(nuevo)}"
    if not resumen.endswith((".", "!", "?")):
        resumen += "."
    linea = f"- [{nuevo}]({nuevo}) — {resumen}{_enlace_al_resumen(carpeta, nuevo)}"

    salida, puesta = [], False
    for cruda in _leer(ruta).splitlines():
        m = _LINEA.match(cruda.strip())
        if m and m.group(1) == viejo:
            salida.append(linea)
            puesta = True
        else:
            salida.append(cruda)
    texto = "\n".join(salida).rstrip("\n") + "\n"
    if not puesta:
        texto += f"{linea}\n"           # no estaba indexada: se agrega ahora
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def _enlace_al_resumen(carpeta, nombre):
    """` · [ruta](ruta)` al resumen de esa sesión, o "" si todavía no existe.

    El resumen se llama igual que la transcripción, sin la fecha, y vive en la
    carpeta del día: `resumenes/AAAA-MM-DD/<tema>.md`. Se enlaza por sesión y
    no por día porque cada sesión resuelve un tema, y quien busca qué quedó
    busca el de una sesión concreta.

    Si el archivo no está, no se inventa el enlace: un enlace roto en el índice
    es peor que no tenerlo. La próxima vez que se renombre, se pone.
    """
    fecha = _fecha_de(nombre)
    tema = os.path.basename(nombre)[len(fecha) + 1:]
    if not tema:
        return ""
    rel = f"{RESUMENES}/{fecha}/{tema}"
    if not os.path.isfile(os.path.join(carpeta, RESUMENES, fecha, tema)):
        return ""
    return f" · [{rel}]({rel})"


def _libre(carpeta, nombre, actual):
    """`nombre`, o con sufijo `-2`, `-3` si ese ya está ocupado por otro."""
    if nombre == actual or not os.path.exists(os.path.join(carpeta, nombre)):
        return nombre
    raiz, ext = os.path.splitext(nombre)
    n = 2
    while os.path.exists(os.path.join(carpeta, f"{raiz}-{n}{ext}")):
        n += 1
    return f"{raiz}-{n}{ext}"


def _slug(tema):
    """El tema como parte de un nombre de archivo: minúsculas y guiones.

    Se quitan las tildes y la eñe pasa a `n`: el nombre viaja en enlaces, rutas
    y URLs, donde un carácter fuera del inglés se escribe distinto según quién
    lo lea. El texto con tildes se conserva en el título y en el índice.
    """
    plano = unicodedata.normalize("NFKD", str(tema or ""))
    plano = "".join(c for c in plano if not unicodedata.combining(c))
    return re.sub(r"-{2,}", "-", re.sub(r"[^a-z0-9]+", "-", plano.lower())).strip("-")


def _legible(tema):
    """El tema para el título: guiones a espacios y la primera en mayúscula."""
    texto = str(tema or "").replace("-", " ").replace("_", " ").strip()
    return texto[:1].upper() + texto[1:] if texto else "Sesión"


def sesiones(raiz):
    """Las sesiones registradas: `[(archivo, de qué se trató)]`, en orden.

    Se leen del índice y no de la carpeta: el índice es lo que dice **de qué
    trató** cada sesión, y un listado de nombres de archivo no serviría para
    decidir cuál abrir.
    """
    salida = []
    for linea in _leer(os.path.join(raiz, CARPETA, INDICE)).splitlines():
        m = _LINEA.match(linea.strip())
        if m and m.group(1).lower() != INDICE.lower():
            salida.append((m.group(1), (m.group(2) or "").strip()))
    return salida


def contexto(raiz, limite=LIMITE):
    """El índice de sesiones que se le inyecta al agente al abrir la sesión.

    Va el índice, **no** las transcripciones: son la conversación entera y
    llenarían la ventana con lo que casi nunca hace falta. El agente abre la que
    le sirve — pero para eso tiene que saber que existe, y el chat nuevo arranca
    sin memoria de los anteriores.
    """
    hechas = sesiones(raiz)
    if not hechas:
        return ""

    recorte = hechas[-limite:]
    cabeza = [
        "[HISTÓRICO DE SESIONES — NO ESTÁ CARGADO, SOLO EL ÍNDICE]",
        "Cada sesión con este proyecto quedó transcrita literal. Antes de "
        "retomar un tema, leer con Read la sesión que lo trató: ahí está qué se "
        "decidió y por qué. No suponer qué dice una sesión por su título.",
    ]
    if len(hechas) > len(recorte):
        cabeza.append(f"Se listan las últimas {len(recorte)} de {len(hechas)}; "
                      f"el resto, en {CARPETA}/{INDICE}.")

    cuerpo = [f"  {CARPETA}/{archivo}" + (f" — {tema}" if tema else "")
              for archivo, tema in recorte]
    return "\n".join(cabeza + [""] + cuerpo)


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


def main(argv=None):
    """`--renombrar <archivo> --tema <tema> [--resumen <texto>]`.

    Es lo que corre el agente cuando el usuario aprueba el nombre. Va por
    comando y no a mano para que el archivo y el índice cambien juntos.
    """
    import argparse
    import sys

    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from comun import preparar_salida
    preparar_salida()

    p = argparse.ArgumentParser(description="Le pone el tema al nombre de una "
                                            "sesión del histórico.")
    p.add_argument("--renombrar", metavar="ARCHIVO", required=True,
                   help="el archivo de la sesión, tal como está hoy")
    p.add_argument("--tema", required=True,
                   help="de qué trató, en pocas palabras")
    p.add_argument("--resumen", default="",
                   help="la línea del índice; si falta, queda la fecha")
    a = p.parse_args(argv)

    try:
        ruta = renombrar(a.renombrar, a.tema, a.resumen)
    except (OSError, ValueError) as e:
        print(f"No se pudo renombrar: {e}", file=sys.stderr)
        return 1
    print(f"Sesión guardada como {os.path.basename(ruta)}; índice al día.")
    return 0


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


if __name__ == "__main__":
    import sys
    sys.exit(main())
