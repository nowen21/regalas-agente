#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lo que una sesión deja: crea el resumen, dice qué le falta y qué sigue abierto.

    python resumen.py --raiz "C:/ruta/del/proyecto" --sesion <uuid>

No escribe hallazgos ni los interpreta: reconocer uno es criterio, y el criterio
no lo tiene un programa. Lo que sí puede hacer es que el hueco se vea.

Tres cosas, y ninguna más:

  - **Crear** el archivo del resumen al abrir la sesión, con el modelo puesto.
  - **Decir qué falta**: si no hay ningún hallazgo, o si nadie dijo todavía si
    la sesión se puede cerrar.
  - **Buscar lo que sigue abierto del propósito** de la sesión, para que quien
    la retoma no tenga que ir a buscarlo.

El resumen se llama igual que la transcripción, sin la fecha, y vive en la
carpeta del día: `historico-chat/resumenes/AAAA-MM-DD/«tema».md`. Los dos nombres
se mueven juntos cuando la sesión se renombra; de eso se encarga `historico.py`.

Lo exige `13·DOC22`; el modelo es `plantillas/sesion.md`.
"""
import os
import re

CARPETA = "historico-chat"
RESUMENES = "resumenes"
MODELO = os.path.join("plantillas", "sesion.md")

# `### H-1 · título del hallazgo`
_HALLAZGO = re.compile(r"^### (H-\d+) \u00b7 (.+)$", re.MULTILINE)

# `- **Estado:** resuelto acá.` / `- **Estado:** abierto.`
_ESTADO = re.compile(r"^- \*\*Estado:\*\*\s*(.+?)\s*$", re.MULTILINE)

# La sección de cierre y sus casillas.
_CIERRE = "## ¿Se puede cerrar la sesión?"
_SIN_MARCAR = re.compile(r"^\|.*\u2610", re.MULTILINE)

# Queda dentro del resumen cuando ya se avisó, para no repetir el aviso.
MARCA_VACIO = "<!-- aviso: resumen sin hallazgos -->"
MARCA_CIERRE = "<!-- aviso: falta decir si la sesión se puede cerrar -->"


def _leer(ruta):
    with open(ruta, encoding="utf-8") as f:
        return f.read()


def _escribir(ruta, texto):
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


# ── Dónde vive ────────────────────────────────────────────────────────────

def ruta_de(raiz, transcripcion):
    """La ruta del resumen que le corresponde a esa transcripción, o "".

    De `2026-08-14-tema.md` sale `resumenes/2026-08-14/tema.md`. Si el nombre
    todavía no tiene tema, el resumen se llama igual que la transcripción sin
    la fecha, y se moverá cuando la sesión se nombre.
    """
    nombre = os.path.basename(transcripcion)
    m = re.match(r"^(\d{4}-\d{2}-\d{2})-(.+\.md)$", nombre)
    if not m:
        return ""
    fecha, tema = m.group(1), m.group(2)
    return os.path.join(raiz, CARPETA, RESUMENES, fecha, tema)


def _dia(ruta_resumen):
    return os.path.dirname(ruta_resumen)


# ── Crear ─────────────────────────────────────────────────────────────────

def crear(raiz, transcripcion, estandar=""):
    """Crea el resumen con el modelo puesto. Devuelve su ruta, o "".

    No pisa lo que ya esté escrito: si el archivo existe, se devuelve tal cual.
    Un proyecto sin carpeta de resúmenes no se ve afectado, y eso es a propósito:
    no todos llevan histórico.
    """
    if not os.path.isdir(os.path.join(raiz, CARPETA, RESUMENES)):
        return ""
    ruta = ruta_de(raiz, transcripcion)
    if not ruta:
        return ""
    if os.path.isfile(ruta):
        return ruta

    modelo = os.path.join(estandar or raiz, MODELO)
    if not os.path.isfile(modelo):
        return ""

    try:
        os.makedirs(_dia(ruta), exist_ok=True)
        _escribir(ruta, _desde_modelo(_leer(modelo), os.path.basename(transcripcion)))
    except OSError:
        return ""                       # sin permiso o sin espacio: no detiene
    _indexar_dia(_dia(ruta), os.path.basename(ruta))
    return ruta


def _desde_modelo(modelo, transcripcion):
    """El cuerpo del resumen nuevo: el modelo, sin ejemplos y sin hallazgos.

    Los hallazgos de ejemplo del modelo **no** se copian: uno escrito por el
    programa se contaría como trabajo hecho, y el enganche no escribe hallazgos.
    Lo que sí se copia es la sección de cierre, que es la pregunta que hay que
    responder para poder cerrar la sesión.

    El encabezado **no enlaza `plantillas/sesion.md`**: esa carpeta es del
    estándar y no viaja a los proyectos que lo heredan, así que ahí el enlace
    nacía roto. Se enlaza el índice del histórico, que sí lo deja el instalador
    en todos.
    """
    fecha = transcripcion[:10]
    partes = modelo.split(_CIERRE, 1)
    cola = ("\n\nNada todavía.\n\n---\n\n" + _CIERRE + partes[1]) if len(partes) > 1 else "\n"
    return (f"# {fecha} \u00b7 lo que qued\u00f3\n\n"
            f"Hallazgos de la sesi\u00f3n transcrita en "
            f"[{CARPETA}/{transcripcion}](../../{transcripcion}). C\u00f3mo se llena "
            f"est\u00e1 en [{CARPETA}/README.md](../../README.md). "
            f"La conversaci\u00f3n est\u00e1 all\u00e1; ac\u00e1 queda lo que la sesi\u00f3n dej\u00f3.\n\n"
            f"**Viene de:** \u00ab...\u00bb\n\n---\n\n"
            f"## Hallazgos de esta sesi\u00f3n{cola}")


def _indexar_dia(carpeta, nombre):
    """Agrega la línea al índice del día. Si no hay índice, lo crea."""
    ruta = os.path.join(carpeta, "README.md")
    fecha = os.path.basename(carpeta)
    linea = f"| [{nombre}]({nombre}) | Sin escribir todav\u00eda. |\n"
    if not os.path.isfile(ruta):
        _escribir(ruta, f"# {fecha}\n\nRes\u00famenes de las sesiones de este d\u00eda. "
                        f"Uno por sesi\u00f3n.\n\n| Sesi\u00f3n | Qu\u00e9 dej\u00f3 |\n|---|---|\n" + linea)
        return
    texto = _leer(ruta)
    if f"({nombre})" in texto:
        return
    _escribir(ruta, texto.rstrip("\n") + "\n" + linea)


# ── Qué le falta ──────────────────────────────────────────────────────────

def hallazgos(ruta):
    """Los hallazgos escritos: lista de (id, título, estado)."""
    if not os.path.isfile(ruta):
        return []
    texto = _leer(ruta)
    ids = [(m.group(1), m.group(2), m.start()) for m in _HALLAZGO.finditer(texto)]
    estados = [(m.group(1), m.start()) for m in _ESTADO.finditer(texto)]
    salida = []
    for i, (hid, titulo, pos) in enumerate(ids):
        fin = ids[i + 1][2] if i + 1 < len(ids) else len(texto)
        estado = next((e for e, p in estados if pos < p < fin), "")
        salida.append((hid, titulo, estado.rstrip(".").strip().lower()))
    return salida


def falta(ruta):
    """Qué le falta al resumen: lista de claves entre `vacio` y `cierre`.

    Son dos huecos distintos y se avisan por separado, una vez cada uno. Con el
    aviso único se colaba el caso real: escribir un hallazgo y no decir nunca si
    la sesión se puede cerrar.
    """
    if not os.path.isfile(ruta):
        return []
    texto = _leer(ruta)
    pendientes = []
    if not _HALLAZGO.search(texto):
        if MARCA_VACIO not in texto:
            pendientes.append("vacio")
        return pendientes
    cuerpo = texto.split(_CIERRE, 1)
    sin_cierre = len(cuerpo) < 2 or _SIN_MARCAR.search(cuerpo[1])
    if sin_cierre and MARCA_CIERRE not in texto:
        pendientes.append("cierre")
    return pendientes


def marcar_avisado(ruta, clave):
    """Deja la marca del aviso dentro del propio resumen, para no repetirlo.

    En el archivo y no en un registro aparte: un archivo aparte se desincroniza
    y hay que limpiarlo; la marca vive donde vive el dato.
    """
    marca = MARCA_VACIO if clave == "vacio" else MARCA_CIERRE
    if not os.path.isfile(ruta):
        return
    texto = _leer(ruta)
    if marca in texto:
        return
    try:
        _escribir(ruta, texto.rstrip("\n") + f"\n\n{marca}\n")
    except OSError:
        pass                            # no poder marcarlo no detiene la sesión


def sin_resolver(ruta):
    """Los hallazgos del resumen que siguen abiertos: lista de (id, título)."""
    return [(h, t) for h, t, e in hallazgos(ruta) if e.startswith("abierto")]


# ── Lo abierto del propósito ──────────────────────────────────────────────

def viene_de(ruta):
    """El propósito declarado de la sesión: el texto de su «viene de», o ""."""
    if not os.path.isfile(ruta):
        return ""
    m = re.search(r"^\*\*Viene de:\*\*\s*(.+?)\s*$", _leer(ruta), re.MULTILINE)
    if not m:
        return ""
    crudo = m.group(1).strip()
    return "" if crudo.startswith(("\u00ab", "\u2014")) else crudo


def proposito(raiz, ruta):
    """El hallazgo que la sesión viene a resolver, si sigue abierto.

    Devuelve (ruta del resumen donde vive, id, título, pregunta viva), o None.
    **Solo el del propósito**: una sesión abierta para un tema no tiene por qué
    ver los hallazgos de otro. Eso es ruido, y el ruido se deja de leer.
    """
    declarado = viene_de(ruta)
    if not declarado:
        return None
    m = re.search(r"(\d{4}-\d{2}-\d{2})\s*\u00b7\s*\[?([^\u00b7\]]+?)\s*\u00b7\s*\[?(H-\d+)",
                  declarado)
    if not m:
        return None
    fecha, tema, hid = m.group(1), m.group(2).strip(), m.group(3)
    origen = os.path.join(raiz, CARPETA, RESUMENES, fecha, f"{tema}.md")
    if not os.path.isfile(origen):
        return None
    for h, titulo, estado in hallazgos(origen):
        if h == hid and estado.startswith("abierto"):
            return (origen, h, titulo, _retoma(origen, h))
    return None


def _retoma(ruta, hid):
    """El «con qué se retoma» de ese hallazgo, o "" si no lo tiene."""
    texto = _leer(ruta)
    bloque = re.split(r"^### H-\d+ \u00b7 ", texto, flags=re.MULTILINE)
    for i, m in enumerate(re.finditer(r"^### (H-\d+) \u00b7 ", texto, re.MULTILINE)):
        if m.group(1) == hid and i + 1 < len(bloque):
            r = re.search(r"^- \*\*Con qu\u00e9 se retoma:\*\*\s*(.+?)\s*$",
                          bloque[i + 1], re.MULTILINE)
            return r.group(1) if r else ""
    return ""
