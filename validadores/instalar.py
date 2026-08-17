#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deja instalado y operativo el agente en un proyecto que usa el estándar.

    python validadores/instalar.py                    # muestra el registro
    python validadores/instalar.py C:/ruta/proyecto   # simula (no toca nada)
    python validadores/instalar.py C:/ruta --aplicar  # instala de verdad
    python validadores/instalar.py --todos --aplicar  # en todos los del registro

**Una sola línea instala todo.** El proceso no le pide al usuario guardar, copiar
ni crear nada a mano: lee el estado del proyecto, calcula qué falta y lo deja
puesto — la estructura base, el `CLAUDE.md` con las rutas de esta máquina, el
`.gitignore`, los archivos de `.agente/`, el histórico, la memoria, los enganches
de git y de Claude Code, el registro central y el registro de versión. Al final
comprueba el resultado y dice si algo quedó fuera.

**Es idempotente.** Lo que ya está al día no se toca, no se duplica y no se pisa:
los documentos que llena el proyecto (`CLAUDE.md`, los 4 de `.agente/`, el índice
de la memoria) solo se crean si faltan; después, solo se les agrega lo que el
estándar sumó. Correrlo dos veces da el mismo resultado que correrlo una.

**No pregunta.** Lo que ya está decidido —por `CLAUDE.md`, por las reglas de
`base/` o por la estructura estándar— se aplica sin consultar. Lo único que se
reporta como pendiente es lo que de verdad exige una decisión del usuario, y se
dice cuál es y por qué.

**Por defecto solo simula.** Instalar cambia el comportamiento de un repositorio
ajeno — a partir de ahí un commit con mal mensaje se rechaza allí también — así
que hay que pedirlo explícitamente con `--aplicar`.

Las reglas y los validadores **no se copian**: los enganches los llaman en su
sitio, por ruta absoluta. Una sola copia del estándar sirve a todos los
proyectos, y al cambiar una regla aquí cambia en todos a la vez. Dentro del
proyecto solo se crea lo que el proyecto necesita tener para funcionar.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import unicodedata
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from comun import RAIZ, leer, preparar_salida           # noqa: E402

REGISTRO = os.path.join(RAIZ, "plantillas", "proyectos.md")

# Fila del registro: | Nombre | `ruta` | scope | stack |
_FILA = re.compile(r"^\|([^|]+)\|([^|]+)\|")

MARCA = "# generado por validadores/instalar.py del estándar del agente"

# Preámbulo común: localizar el intérprete y el estándar, o fallar diciendo por
# qué. Un enganche que calla cuando no puede correr es peor que no tenerlo.
_PREAMBULO = """#!/bin/sh
{marca}
# {descripcion}
#
# Se activa con:    git config core.hooksPath .githooks
# Se desactiva con: git config --unset core.hooksPath

ESTANDAR="{estandar}"

if command -v python > /dev/null 2>&1; then
    PY=python
elif command -v python3 > /dev/null 2>&1; then
    PY=python3
else
    echo "{nombre}: no se encontró Python; no se pudo revisar." >&2
    echo "Instala Python o desactiva: git config --unset core.hooksPath" >&2
    exit 1
fi

if [ ! -f "$ESTANDAR/validadores/validar.py" ]; then
    echo "{nombre}: no se encontró el estándar en $ESTANDAR" >&2
    echo "Reinstala el enganche o desactiva: git config --unset core.hooksPath" >&2
    exit 1
fi
"""

PLANTILLA_COMMIT_MSG = _PREAMBULO + """
"$PY" "$ESTANDAR/validadores/validar.py" commit --archivo "$1" || {{
    echo "" >&2
    echo "Commit rechazado: corrige el mensaje y vuelve a intentar." >&2
    exit 1
}}
"""

PLANTILLA_PRE_COMMIT = _PREAMBULO + """
# Solo lo que entra en ESTE commit — no el repositorio entero. Ver G3.
"$PY" "$ESTANDAR/validadores/validar.py" versionado --raiz "$(pwd)" --preparados || {{
    echo "" >&2
    echo "Commit rechazado: saca del commit lo que no debe versionarse." >&2
    exit 1
}}
"""

HOOKS = [
    ("commit-msg", PLANTILLA_COMMIT_MSG,
     "Revisa el mensaje del commit antes de aceptarlo (09-git.md · G2, G8)."),
    ("pre-commit", PLANTILLA_PRE_COMMIT,
     "Revisa que no entren secretos ni artefactos (09-git.md · G3)."),
]


def proyectos_registrados():
    """Lee `plantillas/proyectos.md` y devuelve [(nombre, ruta), ...]."""
    if not os.path.isfile(REGISTRO):
        return []

    salida = []
    for linea in leer(REGISTRO).splitlines():
        m = _FILA.match(linea.strip())
        if not m:
            continue
        nombre, ruta = m.group(1).strip(), m.group(2).strip()
        # Se saltan el encabezado y la línea de guiones de la tabla.
        if not ruta.startswith("`") or nombre.lower() == "proyecto":
            continue
        salida.append((nombre, ruta.strip("`").strip()))
    return salida


def _mandar_git(ruta, *args):
    return subprocess.run(["git", "-C", ruta, *args],
                          capture_output=True, text=True, encoding="utf-8")


def cumple_f13(ruta):
    """El arranque de `02·F13`: ¿existe la carpeta `proyectos/`?

    Es la precondición de todo lo demás. Ya no es un muro: si falta, el
    instalador la crea vacía (`instalar_estructura`). Lo que sigue siendo del
    usuario es **qué va adentro** — el agente no mueve ni reorganiza código.
    """
    return os.path.isdir(os.path.join(ruta, "proyectos"))


def es_el_estandar(ruta):
    """¿`ruta` es la carpeta del propio estándar?

    No es un proyecto que use el agente: es donde viven las reglas. No tiene
    `proyectos/`, y su `CLAUDE.md` sí se versiona — meterlo al `.gitignore`
    borraría del repositorio el instructivo del estándar.
    """
    return os.path.normcase(os.path.abspath(ruta)) == os.path.normcase(RAIZ)


def es_repositorio_git(ruta):
    """¿`ruta` es la raíz de un repositorio (no una subcarpeta de otro)?"""
    return os.path.isdir(os.path.join(ruta, ".git"))


def repositorios_git(ruta):
    """Todos los repositorios de un espacio de trabajo.

    Según `02·F13`, el código vive en `proyectos/` y puede ser **uno o varios**
    repositorios independientes (ej. RNI: `proyectos/rni-back/` +
    `proyectos/rni-front/`). El espacio del agente (`documentacion/`, `.agente/`)
    va al lado, y puede o no estar versionado él mismo.

    Por eso se mira en dos sitios: la raíz, y cada carpeta de `proyectos/`.
    """
    encontrados = []
    if es_repositorio_git(ruta):
        encontrados.append(ruta)

    proyectos = os.path.join(ruta, "proyectos")
    if os.path.isdir(proyectos):
        for nombre in sorted(os.listdir(proyectos)):
            sub = os.path.join(proyectos, nombre)
            if os.path.isdir(sub) and es_repositorio_git(sub):
                encontrados.append(sub)

    return encontrados


# Enganches de Claude Code: (evento, matcher, guion, mensaje, argumentos).
# `matcher` en None = el evento no filtra por herramienta (SessionStart).
# `argumentos` deja que un mismo guion sirva a dos eventos con papeles distintos,
# como el histórico: uno anota al usuario y el otro al agente.
HOOKS_CLAUDE = [
    ("PostToolUse", "Write|Edit", "hook_md.py",
     "Revisando los enlaces del proyecto...", ""),
    ("SessionStart", None, "hook_sesion.py",
     "Revisando el estándar...", ""),
    ("UserPromptSubmit", None, "hook_historico.py",
     "Anotando en el histórico...", "--modo usuario"),
    ("Stop", None, "hook_historico.py",
     "Anotando en el histórico...", "--modo agente"),
    ("UserPromptSubmit", None, "hook_checklist.py",
     "Revisando la instalación del agente...", ""),
    ("SessionStart", None, "hook_recuerdos.py",
     "Recogiendo la memoria del agente...", ""),
    ("PostToolUse", "Write|Edit", "hook_recuerdos.py",
     "Recogiendo la memoria del agente...", ""),
    ("SessionStart", None, "hook_resumen.py",
     "Preparando el resumen de la sesión...", "--modo inicio"),
    ("UserPromptSubmit", None, "hook_resumen.py",
     "Revisando el resumen de la sesión...", "--modo aviso"),
]


def _hook_claude(estandar, proyecto, guion, mensaje, argumentos=""):
    extra = f"{argumentos} " if argumentos else ""
    return {
        "type": "command",
        "command": (f'python "{estandar}/validadores/{guion}" '
                    f'{extra}--raiz "{proyecto}"'),
        "statusMessage": mensaje,
    }


def instalar_git(ruta, estandar, aplicar):
    """Escribe los enganches en .githooks/ y apunta core.hooksPath ahí."""
    pasos = []
    carpeta = os.path.join(ruta, ".githooks")

    actual = _mandar_git(ruta, "config", "--get", "core.hooksPath").stdout.strip()
    if actual and actual != ".githooks":
        return [f"OMITIDO: core.hooksPath ya apunta a «{actual}» — "
                f"no se pisa; revísalo a mano"]

    for nombre, plantilla, descripcion in HOOKS:
        archivo = os.path.join(carpeta, nombre)
        contenido = plantilla.format(marca=MARCA, estandar=estandar,
                                     nombre=nombre, descripcion=descripcion)
        if os.path.isfile(archivo) and leer(archivo) == contenido:
            pasos.append(f"{nombre} ya estaba al día")
            continue
        pasos.append(f"escribir {os.path.join('.githooks', nombre)}")
        if aplicar:
            os.makedirs(carpeta, exist_ok=True)
            with open(archivo, "w", encoding="utf-8", newline="\n") as f:
                f.write(contenido)
            os.chmod(archivo, 0o755)

    if actual == ".githooks":
        pasos.append("core.hooksPath ya estaba puesto")
    else:
        pasos.append("git config core.hooksPath .githooks")
        if aplicar:
            _mandar_git(ruta, "config", "core.hooksPath", ".githooks")

    return pasos


def instalar_claude(ruta, estandar, aplicar):
    """Agrega los enganches de Claude Code al .claude/settings.json."""
    pasos = []
    carpeta = os.path.join(ruta, ".claude")
    archivo = os.path.join(carpeta, "settings.json")
    destino = os.path.join(".claude", "settings.json")

    datos = {}
    if os.path.isfile(archivo):
        try:
            datos = json.loads(leer(archivo))
        except (json.JSONDecodeError, ValueError):
            return ["OMITIDO: .claude/settings.json tiene JSON inválido — "
                    "no se toca; arréglalo a mano"]

    cambios = False
    for evento, matcher, guion, mensaje, argumentos in HOOKS_CLAUDE:
        nuevo = _hook_claude(estandar, ruta.replace("\\", "/"),
                             guion, mensaje, argumentos)

        # Se respeta lo que ya hubiera; solo se toca el grupo propio.
        ganchos = datos.setdefault("hooks", {}).setdefault(evento, [])
        grupo = next((g for g in ganchos if g.get("matcher") == matcher), None)
        if grupo is None:
            grupo = {"hooks": []}
            if matcher:
                grupo["matcher"] = matcher
            ganchos.append(grupo)

        # Se reconoce un enganche propio por el guion al que llama, no por el
        # comando exacto: así una versión anterior se REEMPLAZA en vez de
        # quedar duplicada corriendo en paralelo.
        propios = [i for i, h in enumerate(grupo["hooks"])
                   if guion in (h.get("command") or "")]

        if len(propios) == 1 and grupo["hooks"][propios[0]] == nuevo:
            pasos.append(f"enganche {evento} ya estaba puesto")
            continue

        if propios:
            for i in reversed(propios):
                grupo["hooks"].pop(i)
            pasos.append(f"reemplazar el enganche {evento} en {destino}")
        else:
            pasos.append(f"agregar enganche {evento} a {destino}")
        grupo["hooks"].append(nuevo)
        cambios = True

    if cambios and aplicar:
        os.makedirs(carpeta, exist_ok=True)
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)
            f.write("\n")
    return pasos


PLANTILLA_HISTORICO = os.path.join(RAIZ, "plantillas", "historico-chat.md")
PLANTILLA_MEMORIA = os.path.join(RAIZ, "plantillas", "memoria.md")


def instalar_stack(ruta, aplicar):
    """Copia el stack de instalación a `.agente/`, sellado con su huella.

    Esta copia **sí** se pisa, al revés que los 4 archivos de configuración: no
    la llena nadie, es el retrato de lo que el estándar exige hoy. Comparar su
    huella con la del original es lo que delata que hay componentes nuevos.
    """
    # Se importa aquí y no arriba: `checklist` usa a `instalar` para saber qué
    # enganches y repositorios espera, así que a nivel de módulo sería un ciclo.
    import checklist

    original = checklist.ruta_plantilla(RAIZ)
    if not os.path.isfile(original):
        return ["OMITIDO: falta plantillas/stack-instalacion.md en el estándar"]

    destino = os.path.join(ruta, ".agente", "stack-instalacion.md")

    if checklist.huella_instalada(ruta) == checklist.huella(RAIZ):
        # "Al día" es contra la plantilla, y una copia puede estar al día y mal
        # escrita a la vez: es lo que pasó con la 21.1.0.
        return (_reparar_marcadores(destino, ruta, aplicar,
                                    ".agente/stack-instalacion.md")
                or ["stack de instalación ya estaba al día"])

    if aplicar:
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        cuerpo = _rellenar(leer(original), _rellenos(ruta))
        with open(destino, "w", encoding="utf-8", newline="\n") as f:
            f.write(cuerpo + checklist.sello(RAIZ))
    return ["copiar .agente/stack-instalacion.md"]


def instalar_historico(ruta, aplicar):
    """Crea `historico-chat/` con su README, desde la plantilla del estándar.

    Va aquí y no en el enganche: un hook que crea carpetas por su cuenta en
    cualquier proyecto donde corra sorprende al usuario. El instalador se corre
    a propósito y avisa qué hace.

    Si el README ya existe **no se pisa** —puede haberlo editado el proyecto—,
    pero sí se le refresca el sello: quedar viejo tiene que poder detectarse
    aunque el texto local difiera del original.
    """
    import versiones

    comp = versiones.POR_ID["historico"]
    carpeta = os.path.join(ruta, "historico-chat")
    archivo = os.path.join(carpeta, "README.md")

    if not os.path.isfile(PLANTILLA_HISTORICO):
        return ["OMITIDO: falta plantillas/historico-chat.md en el estándar"]

    if not os.path.isfile(archivo):
        if aplicar:
            os.makedirs(carpeta, exist_ok=True)
            _escribir_sellado(archivo, leer(PLANTILLA_HISTORICO), comp, ruta)
        return ["crear historico-chat/README.md"] + _instalar_resumenes(ruta, aplicar)

    return _refrescar_sello(archivo, comp, ruta, aplicar,
                            "historico-chat/README.md") + _instalar_resumenes(ruta, aplicar)


def _instalar_resumenes(ruta, aplicar):
    """Deja puesta `historico-chat/resumenes/` con su índice.

    El enganche del resumen no crea nada si esta carpeta falta, y sin ella queda
    mudo: el proyecto recibe los dos enganches en su configuración y ninguno
    escribe. Dejarlo como paso a mano era exigir configuración que nadie
    documentó. Como el README del histórico, si ya existe no se pisa.
    """
    carpeta = os.path.join(ruta, "historico-chat", "resumenes")
    archivo = os.path.join(carpeta, "README.md")
    if os.path.isfile(archivo):
        return []
    if aplicar:
        os.makedirs(carpeta, exist_ok=True)
        with open(archivo, "w", encoding="utf-8", newline="\n") as f:
            f.write(TEXTO_RESUMENES)
    return ["crear historico-chat/resumenes/README.md"]


TEXTO_RESUMENES = """# Lo que dejó cada sesión

Una carpeta por día y un archivo por sesión: `AAAA-MM-DD/«tema».md`. Las crea el
enganche del resumen en el primer mensaje de la sesión, con el modelo del
estándar puesto.

**Se arranca por acá, no por la transcripción.** La transcripción de
`historico-chat/` guarda lo que se dijo, y es larga. Acá queda lo que la sesión
**dejó**: los hallazgos, qué se decidió en cada uno y qué quedó abierto.

Llenarlo es del agente: reconocer un hallazgo es criterio, y el programa solo
deja el hueco a la vista.
"""


def instalar_recuerdos(ruta, aplicar):
    """Crea `historico-chat/memory/` y vacía ahí la memoria de la herramienta.

    Dos cosas que van juntas y por eso viven en la misma función: no sirve
    declarar dónde va la memoria si lo que ya está escrito se queda donde no
    debe. El índice se crea sellado y **no se pisa** —lo llena el proyecto—,
    igual que el README del histórico.

    Mover es del instalador y del enganche, nunca del agente: la herramienta
    escribe su memoria donde ella decide, no donde el agente se acuerde.

    **Lo que ya está instalado no se vuelve a tocar.** Si el índice existe y el
    almacén está enlazado a esta carpeta, aquí no se escribe una línea: la
    memoria de un proyecto no es sitio para que una reinstalación pruebe nada.
    """
    import recuerdos
    import versiones

    comp = versiones.POR_ID["recuerdos"]
    archivo = recuerdos.ruta_indice(ruta)

    if not os.path.isfile(PLANTILLA_MEMORIA):
        return ["OMITIDO: falta plantillas/memoria.md en el estándar"]

    etiqueta = f"{recuerdos.CARPETA.replace(os.sep, '/')}/{recuerdos.INDICE}"

    if recuerdos.enlazada(ruta) and recuerdos.indice_presente(ruta):
        # "No se toca" es no escribir memoria; rellenar un marcador que se coló
        # al copiar el índice no es escribir memoria, es terminar la copia.
        return (_reparar_marcadores(archivo, ruta, aplicar, etiqueta)
                + ["memoria enlazada a `historico-chat/memory/`: ya cumple, "
                   "no se toca"])

    if not recuerdos.indice_presente(ruta):
        pasos = [f"crear {etiqueta}"]
        if aplicar:
            os.makedirs(os.path.dirname(archivo), exist_ok=True)
            _escribir_sellado(
                archivo, _rellenar(leer(PLANTILLA_MEMORIA), _rellenos(ruta)),
                comp, ruta)
    else:
        pasos = _refrescar_sello(archivo, comp, ruta, aplicar, etiqueta)

    return pasos + recuerdos.pasos(recuerdos.migrar(ruta, aplicar))


def _escribir_sellado(archivo, texto, componente, proyecto):
    """Escribe `texto` en `archivo` con el sello de su plantilla al día."""
    import version
    import versiones

    sellado = versiones.poner_sello(
        texto, versiones.huella_central(componente, RAIZ),
        version.version_estandar())
    with open(archivo, "w", encoding="utf-8", newline="\n") as f:
        f.write(sellado)


def _refrescar_sello(archivo, componente, proyecto, aplicar, etiqueta):
    """Pone al día solo el sello de un archivo que el proyecto llena.

    No toca una línea del contenido: el `CLAUDE.md` y el README del histórico
    son del proyecto. Lo único que el estándar escribe ahí es la marca de contra
    qué plantilla se sincronizaron, que es lo que permite decir después si
    quedaron viejos.
    """
    import version
    import versiones

    pasos = _reparar_marcadores(archivo, proyecto, aplicar, etiqueta)

    actual = versiones.huella_central(componente, RAIZ)
    sellada, ver = versiones.leer_sello(archivo)
    if sellada == actual and ver == (version.version_estandar() or "?"):
        return pasos or [f"{etiqueta} ya estaba sellado al día"]

    if aplicar:
        texto = versiones.poner_sello(leer(archivo), actual,
                                      version.version_estandar())
        with open(archivo, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
    return pasos + [f"sellar {etiqueta} contra la plantilla "
                    f"({sellada or 'sin sello'} → {actual})"]


# ── El `CLAUDE.md`: el setup del agente en el proyecto ────────────────────

# Lo que la plantilla deja marcado para que lo llene el instalador. Nada de esto
# es una decisión del usuario: sale de esta máquina, de la carpeta del proyecto
# y del `VERSION` del estándar. Preguntarlo sería preguntar lo que ya se sabe.
_MARCADOR = re.compile(r"«(?!…»)[^»\n]+»")


def _slug(texto):
    """`Proyecto de grado` -> `proyecto-de-grado`. Sin tildes ni espacios."""
    plano = unicodedata.normalize("NFKD", texto)
    plano = plano.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", plano.lower()).strip("-") or "proyecto"


def _rellenos(ruta):
    """Qué valor le corresponde a cada marcador de la plantilla."""
    import version

    nombre = os.path.basename(os.path.abspath(ruta).rstrip("\\/")) or "proyecto"
    slug = _slug(nombre)
    estandar = RAIZ.replace("\\", "/")
    proyecto = os.path.abspath(ruta).replace("\\", "/")
    ver = version.version_estandar() or "?"
    hoy = datetime.now().strftime("%Y-%m-%d")

    return {
        "«NOMBRE-PROYECTO»": nombre,
        "«SLUG-PROYECTO»": slug,
        "«RUTA-ESTANDAR»": estandar,
        "«RUTA-PROYECTO»": proyecto,
        "«VERSION-ESTANDAR»": ver,
        "«FECHA»": hoy,
        # Marcadores de plantillas anteriores. Se traducen igual, para que un
        # proyecto viejo converja al correr el instalador en vez de quedarse
        # con huecos que reprueban el checklist para siempre.
        "«NOMBRE DEL PROYECTO»": nombre,
        "«slug-proyecto»": slug,
        "«slug»": slug,
        "«ruta-al-estandar»": estandar,
        "«ruta-de-este-proyecto»": proyecto,
        "«X.Y.Z»": ver,
        "«YYYY-MM-DD»": hoy,
        "«español»": "español",
        "«sí / no»": "no",
        "«Otro ajuste: número de regla (01–19) + qué cambia + por qué»": "ninguno",
        "«ninguna por ahora / ver ./.agente/reglas-proyecto.md»":
            "ninguna por ahora",
    }


def _rellenar(texto, rellenos):
    for marcador, valor in rellenos.items():
        texto = texto.replace(marcador, valor)
    return texto


def _reparar_marcadores(archivo, ruta, aplicar, etiqueta):
    """Rellena en sitio los marcadores que quedaron crudos en una copia vieja.

    Arreglar el punto de copia solo alcanza a lo que se instale **desde ahora**:
    un proyecto que ya tenía la copia mala se queda con ella, porque la huella
    sale de la plantilla central y esa no cambió. Por eso toda copia que ya
    existe pasa por aquí.

    **No reescribe el archivo: sustituye marcadores.** `_rellenar` solo conoce
    los de `_rellenos`, que son los que el instalador sabe calcular. Un hueco que
    llena el proyecto —`«motor»`, `«manual / pipeline»`— no está en ese
    diccionario y sale intacto. Si no hay nada que sustituir, no se escribe ni se
    reporta paso: repetir la instalación no tiene por qué tocar la fecha de un
    archivo que está bien.
    """
    if not os.path.isfile(archivo):
        return []

    original = leer(archivo)
    reparado = _rellenar(original, _rellenos(ruta))
    if reparado == original:
        return []

    if aplicar:
        with open(archivo, "w", encoding="utf-8", newline="\n") as f:
            f.write(reparado)
    return [f"rellenar los marcadores que quedaron crudos en {etiqueta}"]


def _secciones(texto):
    """[(título, líneas)] por cada encabezado `##` o menor. Ignora el H1.

    El H1 lleva el nombre del proyecto, así que nunca coincide entre la
    plantilla y el archivo local — compararlo solo daría falsos faltantes.
    """
    salida = []
    dentro_de_codigo = False
    for linea in texto.splitlines():
        if linea.lstrip().startswith("```"):
            dentro_de_codigo = not dentro_de_codigo
        m = None if dentro_de_codigo else re.match(r"^(#{2,6})\s+(.*)$", linea)
        if m:
            salida.append((m.group(2).strip(), [linea]))
        elif salida:
            salida[-1][1].append(linea)
    return salida


def _completar_secciones(local, plantilla):
    """Agrega al final las secciones que la plantilla tiene y el local no.

    `01·C18` es aditiva: nunca se pisa, se reordena ni se borra lo escrito. Se
    agrega la sección **con su texto**, no vacía — el punto es que la
    instalación quede operativa sin que nadie tenga que ir a copiarla.
    """
    presentes = {t for t, _ in _secciones(local)}
    faltan = [(t, cuerpo) for t, cuerpo in _secciones(plantilla)
              if t not in presentes]
    if not faltan:
        return local, []

    partes = [local.rstrip("\n")]
    for _, cuerpo in faltan:
        partes.append("\n".join(cuerpo).rstrip("\n"))
    return "\n\n".join(partes) + "\n", [t for t, _ in faltan]


def instalar_claude_md(ruta, aplicar):
    """Deja el `CLAUDE.md` del proyecto puesto, lleno y sellado.

    Tres casos, y ninguno le pide nada al usuario:

      - **no existe** -> se genera desde la plantilla central con las rutas de
        esta máquina, el nombre y el slug del proyecto y la versión del
        estándar. Antes había que copiarlo y llenarlo a mano, que es justo lo
        que dejaba a medio instalar a casi todos los proyectos.
      - **existe con marcadores sin llenar** -> se llenan los que el instalador
        sabe calcular, incluidos los de plantillas anteriores.
      - **existe y la plantilla ganó secciones** -> se agregan al final, sin
        tocar una línea de lo que el proyecto escribió.

    El sello **no** es la huella del `CLAUDE.md`: es la de la plantilla contra
    la que se sincronizó. Tiene que ser así porque cada proyecto lo llena con lo
    suyo, así que su contenido nunca coincide con el original — y aun así hay
    que poder decir si quedó viejo.
    """
    import versiones

    comp = versiones.POR_ID["claude-md"]
    plantilla = comp.ruta_plantilla(RAIZ)
    archivo = os.path.join(ruta, "CLAUDE.md")

    if not os.path.isfile(plantilla):
        return ["OMITIDO: falta plantillas/CLAUDE.md.plantilla en el estándar"]

    rellenos = _rellenos(ruta)
    molde = _rellenar(leer(plantilla), rellenos)

    if not os.path.isfile(archivo):
        if aplicar:
            _escribir_sellado(archivo, molde, comp, ruta)
        return ["crear CLAUDE.md desde la plantilla, con las rutas y la "
                "versión de esta máquina"]

    original = leer(archivo)
    cuerpo = versiones.quitar_sello(_rellenar(original, rellenos))

    pasos = []
    if _MARCADOR.search(original) and not _MARCADOR.search(cuerpo):
        pasos.append("llenar en CLAUDE.md los marcadores que quedaban sin valor")
    cuerpo, agregadas = _completar_secciones(cuerpo, versiones.quitar_sello(molde))
    if agregadas:
        pasos.append("agregar a CLAUDE.md lo que la plantilla sumó: "
                     + ", ".join(agregadas))

    if not pasos:
        return _refrescar_sello(archivo, comp, ruta, aplicar, "CLAUDE.md")

    if aplicar:
        _escribir_sellado(archivo, cuerpo, comp, ruta)
    return pasos + ["sellar CLAUDE.md contra la plantilla"]


# ── Lo que el proyecto necesita tener para que el agente funcione ─────────

# `02·F13`: el código del usuario en `proyectos/`, y al lado el espacio del
# agente. Se crean vacías: qué va adentro de `proyectos/` lo decide el usuario.
CARPETAS_BASE = ["proyectos", "documentacion", "prompts"]

# Los 4 archivos de configuración del proyecto. La lista vive aquí porque es el
# instalador quien los pone; `checklist.py` la lee de acá (`20·M2`).
CONFIG_AGENTE = ["stack.md", "dominio.md", "mapeo-nombres.md",
                 "marco-normativo.md"]

# Configuración local de la máquina: no es del repositorio.
IGNORADOS = ["CLAUDE.md", ".agente/"]


def instalar_estructura(ruta, aplicar):
    """Crea la estructura base de `02·F13`.

    La carpeta se crea; el contenido no se inventa. Que `proyectos/` exista es
    una condición de la norma, no una decisión: exigirle al usuario que la
    creara a mano dejaba la instalación parada en el primer paso. Dónde va cada
    fuente **sí** es decisión suya, y por eso el agente nunca mueve ni
    reorganiza lo que ya esté ahí.
    """
    pasos = []
    for nombre in CARPETAS_BASE:
        destino = os.path.join(ruta, nombre)
        if os.path.isdir(destino):
            continue
        pasos.append(f"crear {nombre}/")
        if aplicar:
            os.makedirs(destino, exist_ok=True)
    return pasos or ["la estructura base ya estaba"]


def instalar_gitignore(ruta, aplicar):
    """Agrega al `.gitignore` lo que no es del repositorio.

    Solo agrega, nunca reescribe ni reordena: el `.gitignore` es del proyecto.
    """
    archivo = os.path.join(ruta, ".gitignore")
    texto = leer(archivo) if os.path.isfile(archivo) else ""
    puestas = {l.strip() for l in texto.splitlines()}
    faltan = [x for x in IGNORADOS if x not in puestas]
    if not faltan:
        return ["el .gitignore ya ignoraba la configuración local"]

    if aplicar:
        if texto and not texto.endswith("\n"):
            texto += "\n"
        bloque = ("\n# Configuración local del agente — no es del repositorio.\n"
                  + "\n".join(faltan) + "\n")
        with open(archivo, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto + bloque)
    return [f"agregar al .gitignore: {', '.join(faltan)}"]


def instalar_agente_config(ruta, aplicar):
    """Pone los 4 archivos de `.agente/` desde las plantillas centrales.

    Se crean solo si faltan: los llena el proyecto con sus datos y pisarlos
    sería borrar lo único que el estándar no sabe. Llenarlos es del agente al
    abrir sesión — deduce lo que se ve en el proyecto y deja marcado lo que no.
    """
    pasos = []
    carpeta = os.path.join(ruta, ".agente")
    rellenos = _rellenos(ruta)
    for nombre in CONFIG_AGENTE:
        destino = os.path.join(carpeta, nombre)
        if os.path.isfile(destino):
            # No se pisa, pero sí se le rellenan los marcadores que el
            # instalador sabe llenar: un enlace muerto no es contenido del
            # proyecto, es un hueco que se escapó al copiarlo.
            pasos += _reparar_marcadores(destino, ruta, aplicar,
                                         f".agente/{nombre}")
            continue
        origen = os.path.join(RAIZ, "plantillas", nombre)
        if not os.path.isfile(origen):
            pasos.append(f"OMITIDO: falta plantillas/{nombre} en el estándar")
            continue
        pasos.append(f"crear .agente/{nombre} desde su plantilla")
        if aplicar:
            os.makedirs(carpeta, exist_ok=True)
            with open(destino, "w", encoding="utf-8", newline="\n") as f:
                f.write(_rellenar(leer(origen), rellenos))
    return pasos or ["los 4 archivos de .agente/ ya estaban"]


def instalar_registro(ruta, aplicar):
    """Anota el proyecto en `plantillas/proyectos.md`, la lista única.

    El stack queda «por detectar»: es un dato, no una decisión, y lo completa el
    agente cuando llene `.agente/stack.md`. Dejar la fila sin escribir hasta
    entonces era peor — el proyecto no figuraba en ningún lado.
    """
    if not os.path.isfile(REGISTRO):
        return ["OMITIDO: falta plantillas/proyectos.md en el estándar"]

    esperado = os.path.normcase(os.path.abspath(ruta))
    for _, registrada in proyectos_registrados():
        if os.path.normcase(os.path.abspath(registrada)) == esperado:
            return ["el proyecto ya estaba en el registro central"]

    nombre = os.path.basename(os.path.abspath(ruta).rstrip("\\/"))
    fila = (f"| {nombre} | `{os.path.abspath(ruta)}` | "
            f"`proyecto:{_slug(nombre)}` | por detectar |\n")
    if aplicar:
        texto = leer(REGISTRO)
        if not texto.endswith("\n"):
            texto += "\n"
        with open(REGISTRO, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto + fila)
    return [f"anotar «{nombre}» en plantillas/proyectos.md"]


def instalar(nombre, ruta, aplicar):
    # Prepara su propia salida. Imprime tildes y flechas, y la consola de
    # Windows tal como arranca no las admite: sin esto el programa se muere al
    # escribir en pantalla, no instalando. Dependía de que lo hiciera `main()`,
    # así que quien llamara a `instalar()` como biblioteca tenía que conocer un
    # detalle que no es suyo — y una prueba se lo encontró de frente.
    preparar_salida()

    print(f"\n— {nombre}\n  {ruta}")

    # Se normaliza para que la ruta escrita en el hook no dependa de cómo llegó
    # (`.` vs absoluta, `c:` vs `C:`); si no, cada corrida la reescribiría.
    # `abspath` no toca la letra de la unidad en Windows, así que se fuerza.
    unidad, resto = os.path.splitdrive(os.path.abspath(ruta))
    ruta = unidad.upper() + resto

    if not os.path.isdir(ruta):
        # Único bloqueo que queda: una ruta que no existe suele ser un error de
        # tecleo, y crear una carpeta ahí sería adivinar dónde vive el proyecto.
        print("  BLOQUEADO: la carpeta no existe — revisá la ruta")
        return False

    estandar = RAIZ.replace("\\", "/")
    marca = "·" if aplicar else "(simulado)"

    # Huellas y versión ANTES de tocar nada: es la única forma de decir después
    # qué cambió de verdad, y no repetir el inventario entero en cada registro.
    # La versión hay que leerla aquí: en cuanto se sella, los sellos ya dicen la
    # nueva y una instalación desde cero declararía venir de sí misma.
    antes = _huellas(ruta)
    anterior = _version_anterior(ruta)

    # El propio estándar queda exento de las dos primeras: no es un proyecto que
    # use el agente, es donde viven las reglas. No tiene `proyectos/`, y su
    # `CLAUDE.md` se versiona — ignorarlo borraría el instructivo del estándar.
    propio = es_el_estandar(ruta)
    if propio:
        print("  · es la carpeta del propio estándar: se ponen los enganches, "
              "el histórico y la memoria; nada de configuración de proyecto")
    else:
        for paso in instalar_estructura(ruta, aplicar):
            print(f"  {marca} {paso}")
        for paso in instalar_gitignore(ruta, aplicar):
            print(f"  {marca} {paso}")

    # Los dos enganches son independientes y tienen alcance distinto:
    #   - el de commits va en CADA repositorio (pueden ser varios);
    #   - el de edición va UNA vez, en la raíz del espacio de trabajo, porque
    #     la documentación que revisa vive ahí y no dentro del código.
    repos = repositorios_git(ruta)
    if not repos:
        print("  · commit-msg: OMITIDO — no hay repositorios git aquí")
    for repo in repos:
        etiqueta = os.path.relpath(repo, ruta).replace("\\", "/")
        if etiqueta != ".":
            print(f"  repositorio {etiqueta}/")
        for paso in instalar_git(repo, estandar, aplicar):
            print(f"  {marca} {paso}")

    for paso in instalar_claude(ruta, estandar, aplicar):
        print(f"  {marca} {paso}")

    # El histórico y la memoria sí valen para el propio estándar: ahí también se
    # transcribe cada sesión y se guarda lo que el usuario pide recordar.
    pasos = []
    for instalador in (instalar_historico, instalar_recuerdos):
        pasos += instalador(ruta, aplicar)
    if not propio:
        for instalador in (instalar_stack, instalar_agente_config,
                           instalar_claude_md, instalar_registro):
            pasos += instalador(ruta, aplicar)

    for paso in pasos:
        print(f"  {marca} {paso}")

    for paso in registrar_version(ruta, antes, pasos, aplicar, anterior):
        print(f"  {marca} {paso}")

    comprobar(ruta, aplicar, propio)
    return True


def comprobar(ruta, aplicar, propio=False):
    """La comprobación final: ¿quedó completo? Y si no, qué falta y por qué.

    Instalar y decir "listo" sin mirar es prometer, no entregar. Aquí se recorre
    el mismo stack que revisa el enganche de cada mensaje, y lo que siga
    faltando después de haber instalado todo es, por definición, algo que exige
    una decisión del usuario.
    """
    import checklist

    if propio:
        # El stack de instalación describe un proyecto que **usa** el agente.
        # Medir con esa vara la carpeta donde viven las reglas daría siempre
        # once faltantes que no son faltantes.
        return
    if not aplicar:
        print("  (simulado) la comprobación final corre al aplicar")
        return

    puntos = checklist.revisar(ruta, RAIZ)
    print(f"\n  {checklist.resumen(ruta, puntos)}")

    faltan = checklist.pendientes(puntos)
    if not faltan:
        return
    print("\n  Esto no se pudo resolver solo — necesita una decisión tuya:\n")
    for linea in checklist.detalle(puntos).splitlines():
        print(f"  {linea}")


def _huellas(ruta):
    """{id: huella sellada} de cada documento heredado, ahora mismo."""
    import versiones
    return {e.id: e.sellada for e in versiones.estado(ruta, RAIZ)}


def _version_anterior(ruta):
    """Con qué versión venía el proyecto: "" si es la primera instalación."""
    import versiones
    return versiones.version_registrada(ruta) or versiones.version_sellada(ruta)


def _pendientes(ruta):
    """Lo que quedó sin resolver después de instalar todo.

    Ya no se filtra por una lista de "componentes manuales": el instalador pone
    todos. Lo que aparezca aquí es lo que de verdad exige una decisión del
    usuario, o una falla que hay que mirar — en los dos casos, va al registro.
    """
    import checklist
    if es_el_estandar(ruta):
        return []
    return [f"**{p.id}** — {p.detalle or p.componente}"
            for p in checklist.pendientes(checklist.revisar(ruta, RAIZ))]


def registrar_version(ruta, antes, pasos, aplicar, anterior=""):
    """Deja constancia en `documentacion/versiones/` de la actualización aplicada.

    Se registra por dos motivos, y basta con uno:

      - **cambió alguna huella**: al proyecto le bajó una plantilla nueva;
      - **subió la versión del estándar**, aunque ninguna plantilla del proyecto
        cambiara. La carpeta promete decir *desde cuándo* el proyecto usa cada
        versión, y sin este caso el registro se queda atrás para siempre: el
        instalador decía "nada que registrar" y el checklist "falta el
        registro", sin más salida que editar a mano un archivo que dice que no
        se edita a mano.

    Sin ninguno de los dos no se escribe nada: un registro por corrida
    convertiría la carpeta en ruido y taparía las actualizaciones de verdad.
    """
    import version
    import versiones

    # El estándar no hereda de sí mismo: lleva su `CHANGELOG`, su `versiones` ni
    # siquiera se revisa, y un registro por publicación sería ruido puro.
    if es_el_estandar(ruta):
        return []

    actual = version.version_estandar() or "?"
    despues = _huellas(ruta)
    cambios = [id for id in despues if antes.get(id, "") != despues.get(id, "")]
    subio = bool(anterior) and anterior != actual

    if not cambios and not subio:
        return ["versiones: ni las plantillas ni la versión cambiaron, "
                "no hay actualización que registrar"]

    if not aplicar:
        detalle = ", ".join(sorted(cambios)) if cambios else f"{anterior} → {actual}"
        return [f"registrar la actualización en {versiones.CARPETA} ({detalle})"]

    archivo = versiones.registrar(
        ruta, actual, antes, despues, pasos,
        pendientes=_pendientes(ruta), estandar=RAIZ, anterior=anterior)
    return [f"registrar {os.path.relpath(archivo, ruta)}"]


def main():
    preparar_salida()

    p = argparse.ArgumentParser(
        description="Instala los enganches del estándar en un proyecto.")
    p.add_argument("ruta", nargs="?", help="carpeta del proyecto")
    p.add_argument("--todos", action="store_true",
                   help="todos los proyectos de plantillas/proyectos.md")
    p.add_argument("--aplicar", action="store_true",
                   help="instalar de verdad (sin esto solo simula)")
    a = p.parse_args()

    registrados = proyectos_registrados()

    if a.todos:
        objetivos = registrados
    elif a.ruta:
        ruta = os.path.abspath(a.ruta)
        nombre = next((n for n, r in registrados
                       if os.path.abspath(r) == ruta), "(fuera del registro)")
        objetivos = [(nombre, ruta)]
    else:
        print("Proyectos registrados en plantillas/proyectos.md:\n")
        for nombre, ruta in registrados:
            estado = "" if os.path.isdir(ruta) else "   (no existe)"
            print(f"  {nombre}{estado}\n    {ruta}")
        print("\nIndica una ruta, o --todos. Agrega --aplicar para instalar.")
        return 0

    if not a.aplicar:
        print("MODO SIMULACIÓN — no se modifica nada. Agrega --aplicar.")

    hechos = sum(1 for nombre, ruta in objetivos
                 if instalar(nombre, ruta, a.aplicar))

    print(f"\n{hechos} de {len(objetivos)} proyecto(s) "
          f"{'procesados' if a.aplicar else 'simulados'}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
