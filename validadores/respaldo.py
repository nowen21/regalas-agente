# -*- coding: utf-8 -*-
"""`09·15` · Hace el respaldo antes de correr lo que no se puede deshacer.

**[`00·N7`](../base/00-nucleo-blindado.md) exige comprobar que hay de dónde
volver antes de una operación irreversible sobre datos reales.** Hoy eso lo
cumple el agente acordándose, y **una regla del núcleo no debería depender de
que alguien se acuerde**.

## El límite, dicho antes que nada

**«Operación irreversible» en general no se puede detectar sin criterio.** Un
borrado escrito a mano, un guion de limpieza propio, una llamada a una interfaz
que borra del otro lado — nada de eso lo va a ver este programa.

**Lo que cubre es el subconjunto nombrado**: los comandos que el proyecto
declara como destructivos en su `.agente/stack.md`. Y por eso lo dice cada vez
que corre.

> **Un respaldo automático parcial que se anuncia como total es peor que no
> tenerlo**, porque genera confianza donde no la hay.

## Por qué no adivina el comando

Sin `Respaldo de datos` declarado, **no corre nada y lo dice**. Adivinar cómo se
respalda una base ajena es exactamente la clase de error que este repositorio no
puede permitirse: se equivocaría **justo antes** de lo irreversible.

## Por qué invocarlo es la autorización

`00·N4` pide autorización para esa operación concreta. **Escribir el comando
destructivo dentro de este envoltorio es esa autorización**: nadie lo teclea sin
querer. Lo que el envoltorio agrega no es permiso — es la red.
"""
import os
import re
import subprocess

import comun
from comun import leer

STACK = os.path.join(".agente", "stack.md")

# Fila de la tabla de comandos: `| Acción | `comando` |`
_FILA = re.compile(r"(?m)^\|\s*\**(.+?)\**\s*\|\s*`(.+?)`\s*\|")

# Lo que se toma como marcador de «sin llenar» en las plantillas.
_SIN_LLENAR = ("«", "…")


def comandos(raiz=None):
    """`{acción en minúsculas: comando}` de lo que el proyecto declaró."""
    raiz = raiz or comun.RAIZ
    archivo = os.path.join(raiz, *STACK.split(os.sep))
    if not os.path.isfile(archivo):
        return {}
    salida = {}
    for m in _FILA.finditer(leer(archivo)):
        accion, cmd = m.group(1).strip().lower(), m.group(2).strip()
        if any(x in cmd for x in _SIN_LLENAR):
            continue                    # marcador sin llenar: no es un comando
        salida[accion] = cmd
    return salida


def comando_de_respaldo(raiz=None):
    """El comando declarado para respaldar, o `""` si no lo hay."""
    return comandos(raiz).get("respaldo de datos", "")


def _nombre_del_archivo(fecha):
    return "respaldo-%s.txt" % fecha


def respaldar(raiz, fecha, escribir=False):
    """Corre el respaldo declarado. `(ok, mensaje)`.

    **No inventa el comando**: sin declaración devuelve `(False, …)` y quien
    llama decide — que en este programa siempre es *no seguir*.
    """
    cmd = comando_de_respaldo(raiz)
    if not cmd:
        return False, (
            "el proyecto no declara «Respaldo de datos» en `%s`: no se hace el "
            "respaldo y **no se corre la operación**. Declararlo es de quien "
            "conoce el almacén, no de este programa" % STACK.replace(os.sep, "/"))
    if not escribir:
        return True, "se correría: %s" % cmd
    r = subprocess.run(cmd, shell=True, cwd=raiz, capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        return False, ("el respaldo falló (%s) — **no se corre la operación**: "
                       "%s" % (cmd, (r.stderr or r.stdout).strip()[:200]))
    return True, "respaldo hecho con: %s" % cmd


def main():
    """Se pide a mano. Correrlo **es** la autorización de `00·N4`."""
    import argparse
    import datetime
    p = argparse.ArgumentParser(
        description="Respalda y después corre la operación que se le pase. "
                    "Sin respaldo declarado no corre nada.")
    p.add_argument("operacion", nargs=argparse.REMAINDER,
                   help="el comando destructivo, tal cual se escribiría")
    p.add_argument("--raiz", default=os.getcwd())
    p.add_argument("--aplicar", action="store_true",
                   help="corre de verdad; sin esto solo dice qué haría")
    a = p.parse_args()

    if not a.operacion:
        print("respaldo: falta la operación que se va a correr.")
        print("Uso: python validadores/respaldo.py --aplicar -- <comando>")
        return 2

    print("Cubre solo lo que se le pase por aquí. **Un borrado escrito a mano, "
          "un guion propio o un borrado por interfaz no los ve nadie** — eso "
          "sigue siendo criterio del agente (`00·N7`).\n")

    ok, mensaje = respaldar(a.raiz, datetime.datetime.now().strftime("%Y-%m-%d"),
                            a.aplicar)
    print("  respaldo: %s" % mensaje)
    if not ok:
        return 1

    cmd = " ".join(x for x in a.operacion if x != "--")
    if not a.aplicar:
        print("  operación: se correría: %s  (simulado; agrega --aplicar)" % cmd)
        return 0

    print("  operación: %s" % cmd)
    r = subprocess.run(cmd, shell=True, cwd=a.raiz)
    return r.returncode


if __name__ == "__main__":
    import sys
    sys.exit(main())
