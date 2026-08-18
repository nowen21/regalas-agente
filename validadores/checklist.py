#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El stack de instalación del agente: qué le falta a un proyecto.

Mientras falte un componente, la instalación está **incompleta** y el agente
tiene que decirlo. Es la diferencia entre "el estándar está instalado" como
promesa y como hecho comprobable.

**La lista no vive aquí.** Vive en `plantillas/stack-instalacion.md` y se lee de
ahí: id, qué es cada componente y cómo se instala. Este módulo solo aporta,
para cada `id`, la comprobación que dice sí o no. Así el texto se corrige en la
plantilla —que es la que se copia a cada proyecto— sin tocar código, y no hay
dos listas que puedan terminar diciendo cosas distintas.

Tres cosas se reportan por separado, porque se arreglan distinto:

  - falta un componente          -> instalarlo;
  - el stack de instalación cambió -> reinstalar, hay componentes nuevos;
  - el estándar subió de versión -> decisión del usuario, no se aplica sola.
"""
import json
import os
import re
from datetime import datetime

import instalar
import recuerdos
import sesion
import version
import versiones
import comun
from comun import FALLA, RAIZ, leer

PLANTILLA = "plantillas/stack-instalacion.md"
COPIA = os.path.join(".agente", "stack-instalacion.md")
MARCA = os.path.join(".agente", "INSTALACION-INCOMPLETA.md")

# La lista vive en `instalar.py`, que es quien pone esos archivos. Dos listas
# que declaren lo mismo terminan diciendo cosas distintas (`20·M2`).
CONFIG_AGENTE = instalar.CONFIG_AGENTE

# Fila de la tabla de componentes: | `id` | Componente | Cómo se instala |
_FILA = re.compile(r"^\|\s*`([a-z0-9-]+)`\s*\|([^|]+)\|([^|]+)\|")


class Punto:
    """Un componente del stack y cómo quedó al comprobarlo."""

    def __init__(self, id, componente, arreglo, cumple, detalle=""):
        self.id = id
        self.componente = componente
        self.arreglo = arreglo
        self.cumple = cumple
        self.detalle = detalle

    def __str__(self):
        marca = "ok" if self.cumple else "FALTA"
        return f"[{marca}] {self.id} — {self.detalle or self.componente}"


def ruta_plantilla(estandar=None):
    return os.path.join(estandar or RAIZ, *PLANTILLA.split("/"))


def componentes(estandar=None):
    """La lista, leída de la plantilla: [(id, componente, cómo se instala)]."""
    archivo = ruta_plantilla(estandar)
    if not os.path.isfile(archivo):
        return []
    salida = []
    for linea in leer(archivo).splitlines():
        m = _FILA.match(linea.strip())
        if m:
            salida.append((m.group(1), m.group(2).strip(), m.group(3).strip()))
    return salida


# El sello lo define `versiones.py`, que es el dueño del tema: una sola forma
# de sellar para todos los documentos heredados. Aquí solo se usa (`M2`).
_STACK = versiones.POR_ID["stack-instalacion"]


def huella(estandar=None):
    """Huella del stack central. Cambia cuando cambia la lista."""
    return versiones.huella_central(_STACK, estandar)


def huella_instalada(proyecto):
    """La huella que quedó sellada en la copia del proyecto, o ""."""
    return versiones.huella_sellada(proyecto, _STACK)


def sello(estandar=None):
    """La línea que se le agrega a la copia para poder comparar después."""
    return ("\n" + versiones.texto_sello(huella(estandar),
                                         version.version_estandar()) + "\n")


# ── Las comprobaciones, una por `id` de la plantilla ──────────────────────

def _f13(proyecto, estandar):
    return (instalar.cumple_f13(proyecto),
            "falta la carpeta `proyectos/` — el proyecto no está instalado")


def _claude_md(proyecto, estandar):
    """Existe, está lleno **y** está sincronizado con la plantilla central.

    Lo tercero es lo que antes se escapaba: `revisar_claude_md` detecta las
    secciones que faltan y la diferencia de fechas, pero las reporta como AVISO
    —y aquí solo cuentan las FALLA—, así que un `CLAUDE.md` viejo figuraba como
    instalación completa. Peor: un cambio *dentro* de una sección que ya existía
    no lo veía ninguno de los dos, y la fecha del archivo miente en cuanto
    alguien clona el repositorio o edita el archivo por cualquier motivo.

    El sello no depende de nada de eso: compara la huella de la plantilla contra
    la que este `CLAUDE.md` declara haber seguido.
    """
    fallas = [h for h in sesion.revisar_claude_md(proyecto, estandar)
              if h.severidad == FALLA]
    if fallas:
        return False, fallas[0].mensaje

    est = versiones.estado_de(proyecto, "claude-md", estandar)
    if est and not est.al_dia:
        return False, est.mensaje()
    return True, ""


def _gitignore(proyecto, estandar):
    archivo = os.path.join(proyecto, ".gitignore")
    if not os.path.isfile(archivo):
        return False, "no hay .gitignore"
    lineas = {l.strip() for l in leer(archivo).splitlines()}
    faltan = [x for x in ("CLAUDE.md", ".agente/") if x not in lineas]
    return not faltan, f"al .gitignore le faltan: {', '.join(faltan)}"


def _agente_config(proyecto, estandar):
    carpeta = os.path.join(proyecto, ".agente")
    faltan = [n for n in CONFIG_AGENTE
              if not os.path.isfile(os.path.join(carpeta, n))]
    return not faltan, f"faltan en .agente/: {', '.join(faltan)}"


def _stack_instalacion(proyecto, estandar):
    instalada = huella_instalada(proyecto)
    if not instalada:
        return False, "el proyecto no tiene copia del stack de instalación"
    actual = huella(estandar)
    if instalada != actual:
        return False, ("el stack de instalación cambió en el estándar "
                       f"({instalada} → {actual}): hay componentes nuevos")
    return True, ""


def _documentacion(proyecto, estandar):
    return (os.path.isdir(os.path.join(proyecto, "documentacion")),
            "falta la carpeta `documentacion/`")


def _historico(proyecto, estandar):
    if not os.path.isfile(os.path.join(proyecto, "historico-chat", "README.md")):
        return False, "falta `historico-chat/` con su README"
    est = versiones.estado_de(proyecto, "historico", estandar)
    if est and not est.al_dia:
        return False, est.mensaje()
    return True, ""


def _recuerdos(proyecto, estandar):
    """La memoria del agente: existe en el repositorio y **solo** ahí (`01·C19`).

    Las dos mitades son la misma exigencia. Tener la carpeta y dejar los
    recuerdos en el almacén de la herramienta es no tener memoria: lo que manda
    sigue siendo lo que no se puede revisar ni viaja al repositorio.
    """
    if not recuerdos.indice_presente(proyecto):
        return False, (f"falta `{recuerdos.CARPETA.replace(os.sep, '/')}/` "
                       f"con su índice")

    est = versiones.estado_de(proyecto, "recuerdos", estandar)
    if est and not est.al_dia:
        return False, est.mensaje()
    return recuerdos.revisar(proyecto)


def _versiones(proyecto, estandar):
    return versiones.revisar_registro(proyecto, estandar)


def _enganches_git(proyecto, estandar):
    if not instalar.repositorios_git(proyecto):
        return True, ""             # sin repos no hay enganche que poner
    hallazgos = sesion.revisar_enganches(proyecto, estandar)
    return not hallazgos, (hallazgos[0].mensaje if hallazgos else "")


def _enganches_claude(proyecto, estandar):
    archivo = os.path.join(proyecto, ".claude", "settings.json")
    if not os.path.isfile(archivo):
        return False, "no hay .claude/settings.json"
    try:
        datos = json.loads(leer(archivo))
    except (json.JSONDecodeError, ValueError):
        return False, ".claude/settings.json tiene JSON inválido"

    puestos = {(evento, h.get("command") or "")
               for evento, grupos in (datos.get("hooks") or {}).items()
               for g in grupos for h in g.get("hooks", [])}

    faltan = []
    for evento, _, guion, mensaje, args in instalar.HOOKS_CLAUDE:
        esperado = instalar._hook_claude(
            estandar.replace("\\", "/"), proyecto.replace("\\", "/"),
            guion, mensaje, args)["command"]
        if (evento, esperado) not in puestos:
            faltan.append(f"{evento}/{guion}")
    return not faltan, f"enganches de Claude Code sin poner o vencidos: {', '.join(faltan)}"


def _registro(proyecto, estandar):
    esperado = os.path.normcase(os.path.abspath(proyecto))
    for _, ruta in instalar.proyectos_registrados():
        if os.path.normcase(os.path.abspath(ruta)) == esperado:
            return True, ""
    return False, "el proyecto no está en plantillas/proyectos.md del estándar"


def _version(proyecto, estandar):
    """Que el proyecto **declare** qué versión sigue. El número en sí no reprueba.

    Antes cualquier subida del estándar dejaba al proyecto en rojo, incluso un
    PARCHE que solo corrige una redacción y no le pide nada. Eso es ruido, y el
    ruido enseña a ignorar la alerta.

    Al proyecto le importa lo que **tiene que aplicar**, no el número: de eso se
    encargan los sellos, que solo se quejan cuando cambió algo que el proyecto
    usa de verdad. Aquí solo se exige que la versión adoptada esté declarada —
    sin ella no hay contra qué comparar ni con qué sellar las fases cerradas.
    """
    claude = os.path.join(proyecto, "CLAUDE.md")
    if not os.path.isfile(claude):
        return False, "no se encontró CLAUDE.md; no se puede leer la versión adoptada"
    if not version.extraer_adoptada(leer(claude)):
        return False, ("el proyecto no declara qué versión del estándar sigue "
                       "— fijarla en su CLAUDE.md")
    return True, ""


def _cadena(proyecto, estandar):
    """`02·F0` — el proyecto arrancó la cadena, o todavía no empezó por donde va.

    **El único punto de la lista que el instalador no instala.** No mira si
    falta un archivo del andamiaje: mira si hay por dónde empezar. Un proyecto
    puede tener los trece componentes puestos, código commiteado y `prompts/`
    sin un solo planteamiento — y eso fue exactamente lo que pasó, con la
    revisión diciendo «13 de 13, instalación completa».

    La épica se exige **solo si ya hay código**: pedírsela a un proyecto recién
    instalado es ruido, y el ruido se deja de leer.
    """
    prompts = os.path.join(proyecto, "prompts")
    hay_planteamiento = any(
        n.lower().endswith("planteamiento.md")
        for n in (os.listdir(prompts) if os.path.isdir(prompts) else []))
    if not hay_planteamiento:
        return (False, "no hay ningún planteamiento en `prompts/` — la cadena "
                       "de `02·F0` arranca ahí, y lo escribe el agente con lo "
                       "que el usuario quiere, no el instalador")

    codigo = os.path.join(proyecto, "proyectos")
    hay_codigo = bool(os.path.isdir(codigo) and os.listdir(codigo))
    epicas = os.path.join(proyecto, "documentacion", "epicas")
    hay_epica = any(
        os.path.isdir(os.path.join(epicas, n))
        for n in (os.listdir(epicas) if os.path.isdir(epicas) else []))
    if hay_codigo and not hay_epica:
        return (False, "hay código en `proyectos/` y ninguna épica en "
                       "`documentacion/epicas/` — se construyó saltando la "
                       "cadena (`02·F0`)")
    return True, ""


COMPROBACIONES = {
    "f13": _f13,
    "claude-md": _claude_md,
    "gitignore": _gitignore,
    "agente-config": _agente_config,
    "stack-instalacion": _stack_instalacion,
    "documentacion": _documentacion,
    "historico": _historico,
    "recuerdos": _recuerdos,
    "enganches-git": _enganches_git,
    "enganches-claude": _enganches_claude,
    "registro": _registro,
    "version": _version,
    "versiones": _versiones,
    "cadena": _cadena,
}


def revisar(proyecto, estandar=None):
    """Comprueba todo el stack. Devuelve un `Punto` por componente, en orden."""
    proyecto = os.path.abspath(proyecto)
    estandar = os.path.abspath(estandar or RAIZ)

    puntos = []
    for id, componente, arreglo in componentes(estandar):
        comprobar = COMPROBACIONES.get(id)
        if comprobar is None:
            # La plantilla nombra un componente que este validador no sabe
            # comprobar: se dice, no se calla. Suele significar que el estándar
            # de esta máquina quedó viejo.
            puntos.append(Punto(id, componente, arreglo, False,
                                f"el validador no sabe comprobar «{id}» "
                                f"— actualizar el estándar"))
            continue
        try:
            cumple, detalle = comprobar(proyecto, estandar)
        except Exception as e:      # noqa: BLE001 — un componente roto no tumba el resto
            cumple, detalle = False, f"no se pudo comprobar: {e}"
        puntos.append(Punto(id, componente, arreglo, cumple,
                            "" if cumple else detalle))
    return puntos


def pendientes(puntos):
    return [p for p in puntos if not p.cumple]


def resumen(proyecto, puntos):
    """Una línea para la pantalla del usuario."""
    nombre = os.path.basename(os.path.abspath(proyecto))
    faltan = pendientes(puntos)
    if not puntos:
        return f"Instalación del agente · {nombre} · no se pudo leer el stack"
    if not faltan:
        return (f"Instalación del agente completa · {nombre} · "
                f"{len(puntos)} de {len(puntos)}")
    ids = ", ".join(p.id for p in faltan[:4])
    if len(faltan) > 4:
        ids += f" y {len(faltan) - 4} más"
    return (f"INSTALACIÓN INCOMPLETA · {nombre} · "
            f"{len(puntos) - len(faltan)} de {len(puntos)} · falta: {ids}")


def detalle(puntos):
    """El desglose que lee el agente: qué falta y cómo se arregla."""
    faltan = pendientes(puntos)
    if not faltan:
        return ""
    lineas = []
    for p in faltan:
        lineas.append(f"- **{p.id}** — {p.detalle or p.componente}")
        lineas.append(f"  Se arregla así: {p.arreglo}")
    return "\n".join(lineas)


def escribir_marca(proyecto, puntos):
    """Escribe (o borra) `.agente/INSTALACION-INCOMPLETA.md`.

    La ausencia del archivo **es** la señal de instalación completa: si el
    último componente se resuelve, la marca desaparece sola. Una marca que hay
    que borrar a mano termina mintiendo.

    Devuelve la ruta escrita, o "" si no había nada que marcar.
    """
    proyecto = os.path.abspath(proyecto)
    archivo = os.path.join(proyecto, MARCA)
    faltan = pendientes(puntos)

    if not faltan:
        if os.path.isfile(archivo):
            os.remove(archivo)
        return ""

    cuerpo = (
        "# Instalación del agente incompleta\n\n"
        f"Comprobado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} · "
        f"faltan {len(faltan)} de {len(puntos)} componentes.\n\n"
        "Mientras exista este archivo, el agente **no está completo** y lo avisa "
        "en cada mensaje. Lo escribe y lo borra el enganche; no se edita a mano.\n\n"
        "## Qué falta\n\n"
        f"{detalle(puntos)}\n\n"
        "## Se resuelve con una línea\n\n"
        "```sh\n"
        f'python "{RAIZ.replace(os.sep, "/")}/validadores/instalar.py" '
        f'"{proyecto.replace(os.sep, "/")}" --aplicar\n'
        "```\n\n"
        "El instalador pone todo lo de la lista y comprueba el resultado. Si "
        "después de correrlo algo sigue apareciendo aquí, es porque exige una "
        "decisión del usuario: qué código va en `proyectos/`, o subir la "
        "versión adoptada del estándar.\n\n"
        "> La lista completa de componentes está en `.agente/stack-instalacion.md`.\n")

    os.makedirs(os.path.dirname(archivo), exist_ok=True)
    with open(archivo, "w", encoding="utf-8", newline="\n") as f:
        f.write(cuerpo)
    return archivo


if __name__ == "__main__":
    # `53` · Un modulo que se ejecuta solo y no imprime nada dice, con su
    # silencio, lo mismo que diria si hubiera comprobado y estuviera todo bien.
    comun.no_es_punto_de_entrada("checklist")
