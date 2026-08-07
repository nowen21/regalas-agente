#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Instala los enganches automáticos en un proyecto que usa el estándar.

    python validadores/instalar.py                    # muestra el registro
    python validadores/instalar.py C:/ruta/proyecto   # simula (no toca nada)
    python validadores/instalar.py C:/ruta --aplicar  # instala de verdad
    python validadores/instalar.py --todos --aplicar  # en todos los del registro

**Por defecto solo simula.** Instalar cambia el comportamiento de un repositorio
ajeno — a partir de ahí un commit con mal mensaje se rechaza allí también — así
que hay que pedirlo explícitamente con `--aplicar`.

Nada se copia: los enganches llaman a los validadores **en su sitio**, por ruta
absoluta. Una sola copia del estándar sirve a todos los proyectos, y al cambiar
una regla aquí cambia en todos a la vez.

Lo único que sí se crea dentro del proyecto es lo que el proyecto necesita tener
para que un enganche funcione — hoy, `historico-chat/` y su `memory/`. Sin ellas,
los enganches del histórico y de la memoria no tendrían dónde escribir.
"""
import argparse
import json
import os
import re
import subprocess
import sys

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


MENSAJE_F13 = """    No existe la carpeta `proyectos/`, donde debe vivir el código fuente.

    Para continuar, creá:
        proyectos/
        └── <tu-proyecto>/     ← coloca aquí tu código (uno o varios proyectos)

    Vos decidís la organización y los nombres."""


def cumple_f13(ruta):
    """El gate de arranque de `02·F13`: ¿existe la carpeta `proyectos/`?

    Es la precondición de todo lo demás. Si el espacio de trabajo no está
    armado según la norma, instalar enganches sería poner el techo antes que
    las paredes: se estaría vigilando una estructura que aún no existe.
    """
    return os.path.isdir(os.path.join(ruta, "proyectos"))


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

    if checklist.huella_instalada(ruta) == checklist.huella(RAIZ):
        return ["stack de instalación ya estaba al día"]

    if aplicar:
        destino = os.path.join(ruta, ".agente", "stack-instalacion.md")
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        with open(destino, "w", encoding="utf-8", newline="\n") as f:
            f.write(leer(original) + checklist.sello(RAIZ))
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
        return ["crear historico-chat/README.md"]

    return _refrescar_sello(archivo, comp, ruta, aplicar,
                            "historico-chat/README.md")


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

    if recuerdos.enlazada(ruta) and recuerdos.indice_presente(ruta):
        return ["memoria enlazada a `historico-chat/memory/`: ya cumple, "
                "no se toca"]

    if not recuerdos.indice_presente(ruta):
        pasos = [f"crear {recuerdos.CARPETA.replace(os.sep, '/')}/"
                 f"{recuerdos.INDICE}"]
        if aplicar:
            os.makedirs(os.path.dirname(archivo), exist_ok=True)
            _escribir_sellado(archivo, leer(PLANTILLA_MEMORIA), comp, ruta)
    else:
        pasos = _refrescar_sello(
            archivo, comp, ruta, aplicar,
            f"{recuerdos.CARPETA.replace(os.sep, '/')}/{recuerdos.INDICE}")

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

    actual = versiones.huella_central(componente, RAIZ)
    sellada, ver = versiones.leer_sello(archivo)
    if sellada == actual and ver == (version.version_estandar() or "?"):
        return [f"{etiqueta} ya estaba sellado al día"]

    if aplicar:
        texto = versiones.poner_sello(leer(archivo), actual,
                                      version.version_estandar())
        with open(archivo, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
    return [f"sellar {etiqueta} contra la plantilla ({sellada or 'sin sello'} → {actual})"]


def sellar_claude_md(ruta, aplicar):
    """Sella el `CLAUDE.md` del proyecto contra la plantilla central.

    El sello **no** es la huella del `CLAUDE.md`: es la de la plantilla contra la
    que se sincronizó. Tiene que ser así porque cada proyecto lo llena con lo
    suyo, así que su contenido nunca coincide con el original — y aun así hay
    que poder decir si quedó viejo.

    Antes esto se detectaba comparando títulos de sección y fechas de archivo.
    Los dos fallan: un paso nuevo dentro de una sección que ya existía no cambia
    ningún título, y la fecha miente en cuanto alguien clona el repositorio o
    edita el archivo por cualquier motivo.
    """
    import versiones

    comp = versiones.POR_ID["claude-md"]
    archivo = os.path.join(ruta, "CLAUDE.md")
    if not os.path.isfile(archivo):
        return ["OMITIDO: el proyecto todavía no tiene CLAUDE.md"]
    if not os.path.isfile(comp.ruta_plantilla(RAIZ)):
        return ["OMITIDO: falta plantillas/CLAUDE.md.plantilla en el estándar"]
    return _refrescar_sello(archivo, comp, ruta, aplicar, "CLAUDE.md")


def instalar(nombre, ruta, aplicar):
    print(f"\n— {nombre}\n  {ruta}")

    # Se normaliza para que la ruta escrita en el hook no dependa de cómo llegó
    # (`.` vs absoluta, `c:` vs `C:`); si no, cada corrida la reescribiría.
    # `abspath` no toca la letra de la unidad en Windows, así que se fuerza.
    unidad, resto = os.path.splitdrive(os.path.abspath(ruta))
    ruta = unidad.upper() + resto

    if not os.path.isdir(ruta):
        print("  OMITIDO: la carpeta no existe")
        return False

    # Gate de F13. El propio estándar queda exento: no es un proyecto que use
    # el agente, es donde viven las reglas.
    if os.path.normcase(ruta) != os.path.normcase(RAIZ) and not cumple_f13(ruta):
        print("  BLOQUEADO: no cumple 02·F13 — falta la estructura base.\n")
        print(MENSAJE_F13)
        print("\n  Cuando `proyectos/` exista, volvé a correr el instalador.")
        return False

    estandar = RAIZ.replace("\\", "/")
    marca = "·" if aplicar else "(simulado)"

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

    # Huellas y versión ANTES de tocar nada: es la única forma de decir después
    # qué cambió de verdad, y no repetir el inventario entero en cada registro.
    # La versión hay que leerla aquí: en cuanto se sella, los sellos ya dicen la
    # nueva y una instalación desde cero declararía venir de sí misma.
    antes = _huellas(ruta)
    anterior = _version_anterior(ruta)

    pasos = []
    for instalador in (instalar_historico, instalar_recuerdos, instalar_stack):
        pasos += instalador(ruta, aplicar)
    pasos += sellar_claude_md(ruta, aplicar)

    for paso in pasos:
        print(f"  {marca} {paso}")

    for paso in registrar_version(ruta, antes, pasos, aplicar, anterior):
        print(f"  {marca} {paso}")
    return True


def _huellas(ruta):
    """{id: huella sellada} de cada documento heredado, ahora mismo."""
    import versiones
    return {e.id: e.sellada for e in versiones.estado(ruta, RAIZ)}


def _version_anterior(ruta):
    """Con qué versión venía el proyecto: "" si es la primera instalación."""
    import versiones
    return versiones.version_registrada(ruta) or versiones.version_sellada(ruta)


def _pendientes(ruta):
    """Lo que el instalador no puede aplicar: es decisión del usuario."""
    import checklist
    manuales = {"f13", "claude-md", "gitignore", "agente-config",
                "documentacion", "registro", "version"}
    return [f"**{p.id}** — {p.detalle or p.componente}"
            for p in checklist.pendientes(checklist.revisar(ruta, RAIZ))
            if p.id in manuales]


def registrar_version(ruta, antes, pasos, aplicar, anterior=""):
    """Deja constancia en `documentacion/versiones/` de la actualización aplicada.

    Solo cuando algo cambió de huella. Un registro por corrida —aunque no
    hubiera nada que hacer— convertiría la carpeta en ruido y taparía las
    actualizaciones de verdad.
    """
    import version
    import versiones

    despues = _huellas(ruta)
    cambios = [id for id in despues if antes.get(id, "") != despues.get(id, "")]
    if not cambios:
        return ["versiones: nada cambió, no hay actualización que registrar"]

    if not aplicar:
        return [f"registrar la actualización en {versiones.CARPETA} "
                f"({', '.join(sorted(cambios))})"]

    archivo = versiones.registrar(
        ruta, version.version_estandar() or "?", antes, despues, pasos,
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
