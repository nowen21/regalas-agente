# -*- coding: utf-8 -*-
"""`EP-025·HU-014` · Lo que revisa el enganche después de editar un archivo.

Vivía en `adaptadores/claude-code/hook_md.py`, que usaba las copias viejas de
`validadores/` (análisis 2 del pendiente 119, punto 8). Acá queda la lógica; el
adaptador solo lee la entrada de la herramienta y llama a `revisar`.

- Anota que la sesión tocó el archivo, sea cual sea su extensión, para que un
  commit de otra sesión no se lo lleve sin darse cuenta (pendiente 80).
- Si es un `.md` del proyecto, revisa enlaces e índices, y mide las marcas de
  redacción de **lo que se acaba de escribir** (`00·ID8`, `EP-004·HU-012·CA-05`):
  el archivo trae marcas viejas, y repetirlas en cada edición es ruido.

Devuelve `(código, para el agente, para el error)`: 2 si hay enlaces rotos,
que la herramienta le devuelve al agente para que los corrija; 0 si no.
"""
import os

from .. import validadores  # noqa: F401  Primero el paquete: así cierra la carga de los validadores.
from ..comun import FALLA, Proyecto
from ..comun.consola import archivo_editado
from ..validadores.enlaces import EnlacesRotos, IndicesDeCarpetas
from ..validadores.marcas import Marcas
from ..validadores.sesiones import Sesiones

# Hasta cuántas marcas se nombran una por una. Más que eso tapa el aviso.
TOPE_MARCAS = 15


def texto_escrito(datos):
    """Lo que se acaba de escribir: el `content` de `Write`, o los `new_string`
    de `Edit` y de `MultiEdit`."""
    entrada = (datos or {}).get("tool_input") or {}
    if entrada.get("content") is not None:
        return entrada.get("content") or ""
    partes = [entrada.get("new_string") or ""]
    partes += [e.get("new_string") or "" for e in entrada.get("edits") or []]
    return "\n".join(p for p in partes if p)


def aviso_de_marcas(ruta, texto):
    """El aviso de las marcas de lo recién escrito, o `""` si no hay."""
    halladas = Marcas.medir(texto)
    if not halladas:
        return ""
    lineas = ["[REDACCIÓN: LO QUE SE ACABA DE ESCRIBIR TIENE %d MARCA(S) DE `00·ID8`] %s"
              % (len(halladas), os.path.basename(ruta)),
              "Corregirlas ahora, antes de entregar. La línea cuenta desde el comienzo de lo escrito."]
    for n, _clave, nombre, lugar in halladas[:TOPE_MARCAS]:
        lineas.append("  línea %d: %s; en su lugar, %s" % (n, nombre, lugar))
    if len(halladas) > TOPE_MARCAS:
        lineas.append("  y %d más" % (len(halladas) - TOPE_MARCAS))
    return "\n".join(lineas)


def es_md_de(ruta, raiz):
    if not ruta.lower().endswith(".md"):
        return False
    try:
        return os.path.commonpath([os.path.abspath(ruta), os.path.abspath(raiz)]) == os.path.abspath(raiz)
    except ValueError:      # otra unidad en Windows
        return False


def revisar(raiz, datos):
    """`(código, para el agente, para el error)` de la edición que describe `datos`."""
    editado = archivo_editado(datos)
    # Se anota todo lo que se edita, no solo los `.md`: lo que una sesión se
    # llevó por delante la vez que pasó fue un `.py` a medio corregir. Anotar no
    # puede tumbar el enganche.
    try:
        Sesiones(raiz).anotar((datos or {}).get("session_id") or "", editado)
    except OSError:
        pass
    if not editado or not es_md_de(editado, raiz):
        return 0, "", ""
    try:
        aviso = aviso_de_marcas(editado, texto_escrito(datos))
    except Exception:       # noqa: BLE001  Medir no puede tumbar el enganche.
        aviso = ""
    proyecto = Proyecto(raiz)
    fallas = [h for h in EnlacesRotos(proyecto).validar() + IndicesDeCarpetas(proyecto).validar()
              if h.severidad == FALLA]
    if not fallas:
        return 0, aviso, ""
    error = "La edición dejó enlaces rotos:\n" + "\n".join("  %s" % h for h in fallas)
    if aviso:
        error += "\n\n" + aviso
    return 2, "", error
