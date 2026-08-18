#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Qué versión del estándar usa un proyecto, y desde cuándo.

Nada de lo que un proyecto hereda del estándar puede quedarse viejo. Tres
piezas resuelven eso, y cada una hace **una** cosa:

  1. **El sello.** Cada documento que el proyecto copió del estándar lleva al
     final la huella de la plantilla de la que salió. Comparar esa huella con
     la actual delata cualquier cambio —por dentro o por fuera del documento—
     sin depender de la fecha del archivo, que un `clone` reinicia y que una
     edición local cualquiera deja "más nueva" para siempre.
  2. **La comprobación.** `checklist.py` lee los sellos: el componente cuya
     huella no coincide **reprueba**. Estar viejo deja de ser un aviso que se
     puede ignorar y pasa a ser instalación incompleta.
  3. **El registro.** Cada actualización deja un `.md` en `.agente/versiones/`
     con desde cuándo el proyecto usa esa versión, qué componentes se
     actualizaron y qué cambió de huella.

**No hay archivo de estado.** El estado se lee de los sellos y la historia de
los registros. Dos sitios que declaren lo mismo terminan diciendo cosas
distintas el día que alguien actualiza uno solo.

El sello de un documento **no** es la huella de ese documento: es la de la
plantilla contra la que se sincronizó. Tiene que ser así porque el `CLAUDE.md`
lo llena cada proyecto — su contenido siempre difiere del original, y aun así
hay que poder decir si quedó viejo.
"""
import hashlib
import os
import re
from datetime import datetime

import comun
from comun import RAIZ, leer

# Va en `documentacion/` y no en `.agente/`: `.agente/` está en el `.gitignore`
# —es configuración local de la máquina— y este historial tiene que viajar con
# el repositorio. Saber con qué versión de las reglas se cerró cada fase es
# conocimiento del proyecto, no ajuste de una máquina.
CARPETA = os.path.join("documentacion", "versiones")

# El sello, tal como quedó escrito desde la primera versión. No se cambia de
# forma: cambiarla dejaría "desactualizado" a todo proyecto ya instalado por un
# detalle de sintaxis, no por un cambio real del estándar. Por lo mismo, la
# versión es opcional al LEER —un sello viejo sin ella se sigue entendiendo—
# aunque al escribir siempre se ponga.
_SELLO = re.compile(
    r"^<!--\s*huella:\s*([0-9a-f]+)\s*(?:·\s*estandar\s*(\S+?)\s*)?-->\s*$",
    re.MULTILINE)

# Nombre de un registro: 2026-08-07-1.4.0.md  ·  con sufijo si hay dos el mismo día.
_REGISTRO = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+?)(?:-(\d+))?\.md$")


class Componente:
    """Un documento que el proyecto hereda del estándar y que puede quedar viejo.

    `plantilla` es la fuente en el estándar; `destino`, dónde vive la copia
    dentro del proyecto. `se_pisa` distingue las dos clases que hay: la copia
    literal, que el instalador reescribe, y la que llena el proyecto, donde
    solo se refresca el sello.
    """

    def __init__(self, id, descripcion, plantilla, destino, se_pisa):
        self.id = id
        self.descripcion = descripcion
        self.plantilla = plantilla
        self.destino = destino
        self.se_pisa = se_pisa

    def ruta_plantilla(self, estandar=None):
        return os.path.join(estandar or RAIZ, *self.plantilla.split("/"))

    def ruta_destino(self, proyecto):
        return os.path.join(proyecto, *self.destino.split("/"))


COMPONENTES = [
    Componente(
        "claude-md",
        "El `CLAUDE.md` del proyecto, sincronizado con la plantilla central",
        "plantillas/CLAUDE.md.plantilla", "CLAUDE.md", se_pisa=False),
    Componente(
        "stack-instalacion",
        "La lista de lo que el proyecto debe tener",
        "plantillas/stack-instalacion.md", ".agente/stack-instalacion.md",
        se_pisa=True),
    Componente(
        "historico",
        "El `README.md` de `historico-chat/`",
        "plantillas/historico-chat.md", "historico-chat/README.md",
        se_pisa=False),
    Componente(
        "recuerdos",
        "El índice de `historico-chat/memory/`, la memoria del agente",
        "plantillas/memoria.md", "historico-chat/memory/memory.md",
        se_pisa=False),
]

POR_ID = {c.id: c for c in COMPONENTES}


# ── Huellas y sellos ──────────────────────────────────────────────────────

def huella_texto(texto):
    """La huella de un contenido. Corta a propósito: se lee a simple vista."""
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()[:12]


def huella_central(componente, estandar=None):
    """Huella de la plantilla en el estándar, o "" si la plantilla no está."""
    archivo = componente.ruta_plantilla(estandar)
    if not os.path.isfile(archivo):
        return ""
    return huella_texto(leer(archivo))


def leer_sello(archivo):
    """El sello de un archivo: (huella, versión del estándar). ("", "") si no hay."""
    if not os.path.isfile(archivo):
        return "", ""
    m = None
    for m in _SELLO.finditer(leer(archivo)):
        pass                        # el último sello es el vigente
    return (m.group(1), m.group(2) or "") if m else ("", "")


def huella_sellada(proyecto, componente):
    return leer_sello(componente.ruta_destino(proyecto))[0]


def texto_sello(huella, version_estandar):
    return f"<!-- huella: {huella} · estandar {version_estandar or '?'} -->"


def quitar_sello(texto):
    """`texto` sin su sello, para poder agregarle contenido al final.

    El sello va último: si se le anexa una sección después, deja de estar al
    final y el archivo queda con la marca en medio. Se quita, se escribe, y
    `poner_sello` lo vuelve a dejar donde corresponde.
    """
    return _SELLO.sub("", texto).rstrip("\n") + "\n"


def poner_sello(texto, huella, version_estandar):
    """Devuelve `texto` con su sello al día.

    Si ya tenía uno, se reemplaza en su sitio; si no, se agrega al final. Nunca
    quedan dos: un archivo con dos sellos no se sabe cuál declara.
    """
    nuevo = texto_sello(huella, version_estandar)
    if _SELLO.search(texto):
        return _SELLO.sub(lambda _: nuevo, texto)
    if texto and not texto.endswith("\n"):
        texto += "\n"
    return f"{texto}\n{nuevo}\n"


# ── Estado: qué está al día y qué no ──────────────────────────────────────

AL_DIA = "al-dia"
VIEJO = "viejo"
SIN_SELLO = "sin-sello"
FALTA = "falta"


class Estado:
    """Cómo quedó un componente al compararlo con el estándar."""

    def __init__(self, componente, situacion, sellada, actual):
        self.componente = componente
        self.situacion = situacion
        self.sellada = sellada
        self.actual = actual

    @property
    def id(self):
        return self.componente.id

    @property
    def al_dia(self):
        return self.situacion == AL_DIA

    def mensaje(self):
        if self.situacion == FALTA:
            return f"falta `{self.componente.destino}`"
        if self.situacion == SIN_SELLO:
            return (f"`{self.componente.destino}` no declara contra qué versión "
                    f"se sincronizó — reinstalar para sellarlo")
        if self.situacion == VIEJO:
            return (f"`{self.componente.destino}` quedó viejo: la plantilla "
                    f"cambió en el estándar ({self.sellada} → {self.actual})")
        return ""


def estado(proyecto, estandar=None):
    """Un `Estado` por componente heredado, en el orden de `COMPONENTES`."""
    proyecto = os.path.abspath(proyecto)
    salida = []
    for c in COMPONENTES:
        actual = huella_central(c, estandar)
        destino = c.ruta_destino(proyecto)
        if not os.path.isfile(destino):
            salida.append(Estado(c, FALTA, "", actual))
            continue
        sellada = huella_sellada(proyecto, c)
        if not sellada:
            salida.append(Estado(c, SIN_SELLO, "", actual))
        elif sellada != actual:
            salida.append(Estado(c, VIEJO, sellada, actual))
        else:
            salida.append(Estado(c, AL_DIA, sellada, actual))
    return salida


def viejos(proyecto, estandar=None):
    """Los componentes que no están al día. Vacío = nada viejo."""
    return [e for e in estado(proyecto, estandar) if not e.al_dia]


def estado_de(proyecto, id, estandar=None):
    """El estado de un solo componente, por su `id`."""
    return next((e for e in estado(proyecto, estandar) if e.id == id), None)


# ── El registro: `.agente/versiones/` ─────────────────────────────────────

def carpeta_registros(proyecto):
    return os.path.join(os.path.abspath(proyecto), *CARPETA.split(os.sep))


def registros(proyecto):
    """Los registros del proyecto, del más viejo al más nuevo.

    Devuelve [(nombre_archivo, fecha, version)]. El orden sale del nombre, que
    empieza por la fecha; a igual fecha manda el sufijo.
    """
    carpeta = carpeta_registros(proyecto)
    if not os.path.isdir(carpeta):
        return []
    salida = []
    for nombre in os.listdir(carpeta):
        m = _REGISTRO.match(nombre)
        if m:
            salida.append((nombre, m.group(1), m.group(2), int(m.group(3) or 1)))
    salida.sort(key=lambda r: (r[1], r[3]))
    return [(n, f, v) for n, f, v, _ in salida]


def version_registrada(proyecto):
    """La versión del último registro, o "" si el proyecto no tiene ninguno."""
    hechos = registros(proyecto)
    return hechos[-1][2] if hechos else ""


def version_sellada(proyecto):
    """La versión que declaran los sellos ya puestos, o ""."""
    for c in COMPONENTES:
        _, ver = leer_sello(c.ruta_destino(os.path.abspath(proyecto)))
        if ver and ver != "?":
            return ver
    return ""


def _nombre_libre(carpeta, fecha, version):
    base = f"{fecha}-{version}"
    if not os.path.exists(os.path.join(carpeta, f"{base}.md")):
        return f"{base}.md"
    n = 2
    while os.path.exists(os.path.join(carpeta, f"{base}-{n}.md")):
        n += 1
    return f"{base}-{n}.md"


_CABECERA_INDICE = """# Versiones del estándar en este proyecto

Un archivo por actualización. Cada uno dice **desde cuándo** este proyecto usa
esa versión del estándar, qué componentes se actualizaron y qué cambió.

Los escribe `validadores/instalar.py`; no se editan a mano. Sirven para saber con
qué reglas se trabajó en cada momento: un cambio de norma no reabre lo que ya se
cerró bajo la anterior, y para saber bajo cuál cerró hay que poder mirarlo.

**Se versiona.** Va en `documentacion/` y no en `.agente/` justamente por eso:
`.agente/` está en el `.gitignore` y se queda en una sola máquina.

| Fecha | Versión | Registro |
|---|---|---|
"""


def escribir_indice(proyecto):
    """Reescribe el `README.md` de la carpeta con la lista de registros."""
    carpeta = carpeta_registros(proyecto)
    filas = "".join(f"| {fecha} | `{version}` | [{nombre}]({nombre}) |\n"
                    for nombre, fecha, version in registros(proyecto))
    archivo = os.path.join(carpeta, "README.md")
    with open(archivo, "w", encoding="utf-8", newline="\n") as f:
        f.write(_CABECERA_INDICE + (filas or "| — | — | (todavía ninguno) |\n"))
    return archivo


def registrar(proyecto, version_nueva, antes, despues, pasos,
              pendientes=(), estandar=None, anterior=None):
    """Escribe el registro de una actualización y devuelve su ruta.

    `antes` y `despues` son {id: huella} tomados antes y después de instalar.
    Solo se listan los componentes cuya huella cambió: un registro que repite
    todo en cada corrida deja de servir para ver qué pasó.

    `anterior` se recibe, no se calcula: para cuando esto corre, los sellos ya
    dicen la versión nueva, y preguntárselo aquí haría que una instalación
    desde cero declarase venir de la misma versión que acaba de instalar.
    """
    proyecto = os.path.abspath(proyecto)
    carpeta = carpeta_registros(proyecto)
    os.makedirs(carpeta, exist_ok=True)

    ahora = datetime.now()
    fecha = ahora.strftime("%Y-%m-%d")
    momento = ahora.strftime("%Y-%m-%d %H:%M:%S")
    if anterior is None:
        anterior = version_registrada(proyecto)

    cambiados = [(id, antes.get(id, ""), despues.get(id, ""))
                 for id in despues if antes.get(id, "") != despues.get(id, "")]

    lineas = [
        f"# Actualización a {version_nueva} — {fecha}",
        "",
        f"Desde **{momento}** este proyecto usa la versión **{version_nueva}** "
        f"del estándar.",
        "",
        "| | |",
        "|---|---|",
        f"| Versión anterior | {anterior or '(primera instalación)'} |",
        f"| Versión instalada | **{version_nueva}** |",
        f"| Fecha y hora | {momento} |",
        f"| Estándar | `{(estandar or RAIZ).replace(os.sep, '/')}` |",
        "",
        "## Componentes actualizados",
        "",
    ]

    if cambiados:
        lineas += ["| Componente | Qué es | Huella antes | Huella después |",
                   "|---|---|---|---|"]
        for id, viejo, nuevo in cambiados:
            que = POR_ID[id].descripcion if id in POR_ID else id
            lineas.append(f"| `{id}` | {que} | `{viejo or '—'}` | `{nuevo or '—'}` |")
    else:
        lineas.append("Ninguno cambió de huella: solo se refrescó la instalación.")

    lineas += ["", "## Qué se aplicó", ""]
    lineas += [f"- {p}" for p in pasos] or ["- (nada: ya estaba todo al día)"]

    if pendientes:
        lineas += ["", "## Qué quedó pendiente", "",
                   "Esto no lo aplica el instalador — es decisión del usuario:", ""]
        lineas += [f"- {p}" for p in pendientes]

    lineas += ["", "---", "",
               "> Lo escribió `validadores/instalar.py`. No se edita a mano.", ""]

    nombre = _nombre_libre(carpeta, fecha, version_nueva)
    archivo = os.path.join(carpeta, nombre)
    with open(archivo, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lineas))
    escribir_indice(proyecto)
    return archivo


def revisar_registro(proyecto, estandar=None):
    """¿La carpeta de versiones refleja lo que hoy está instalado?

    Devuelve `(cumple, detalle)`, con la forma que espera `checklist.py`.
    """
    proyecto = os.path.abspath(proyecto)
    if not os.path.isdir(carpeta_registros(proyecto)):
        return False, f"falta `{CARPETA.replace(os.sep, '/')}/` con el registro de versiones"

    ultima = version_registrada(proyecto)
    if not ultima:
        return False, "la carpeta de versiones está vacía: ninguna actualización quedó registrada"

    sellada = version_sellada(proyecto)
    if sellada and sellada != ultima:
        return False, (f"lo instalado dice `{sellada}` y el último registro dice "
                       f"`{ultima}`: falta registrar la actualización")
    return True, ""


if __name__ == "__main__":
    # `53` · Un modulo que se ejecuta solo y no imprime nada dice, con su
    # silencio, lo mismo que diria si hubiera comprobado y estuviera todo bien.
    comun.no_es_punto_de_entrada("versiones")
