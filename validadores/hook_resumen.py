#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganches de Claude Code que sostienen el resumen de la sesión.

Se conectan en `.claude/settings.json`:

    SessionStart      -> python hook_resumen.py --modo inicio --raiz <proyecto>
    UserPromptSubmit  -> python hook_resumen.py --modo aviso  --raiz <proyecto>

El primero crea el archivo del resumen con el modelo puesto y muestra lo que
sigue abierto del propósito de la sesión. El segundo avisa qué le falta al
resumen, una vez por cada cosa que falte.

Es la misma lección de la transcripción: lo que depende de que alguien se
acuerde, no pasa. El enganche **no escribe hallazgos** ni los interpreta: crea,
avisa y muestra. Reconocer un hallazgo es criterio (`13·DOC22`).

Siempre sale con código 0. Un enganche que detiene el trabajo es peor que el
problema que resuelve.
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import historico                        # noqa: E402
import resumen as R                     # noqa: E402


def _sesion_y_transcripcion(raiz, sesion):
    """La ruta de la transcripción de esta sesión, o "" si todavía no hay."""
    carpeta = os.path.join(raiz, historico.CARPETA)
    if not os.path.isdir(carpeta):
        return ""
    marca = f"<!-- sesion: {sesion} -->"
    for nombre in sorted(os.listdir(carpeta)):
        if not nombre.lower().endswith(".md") or nombre == historico.INDICE:
            continue
        ruta = os.path.join(carpeta, nombre)
        try:
            with open(ruta, encoding="utf-8") as f:
                if marca in f.read():
                    return ruta
        except OSError:
            continue
    return ""


def inicio(raiz, sesion, estandar):
    """Crea el resumen y devuelve lo que hay que mostrarle al agente."""
    transcripcion = _sesion_y_transcripcion(raiz, sesion)
    if not transcripcion:
        return ""                       # sin transcripción todavía: nada que hacer
    ruta = R.crear(raiz, transcripcion, estandar)
    if not ruta:
        return ""

    rel = os.path.relpath(ruta, raiz).replace("\\", "/")
    lineas = ["[LO QUE ESTA SESIÓN DEJA SE ESCRIBE EN SU RESUMEN]",
              f"El archivo ya está creado: `{rel}`. Se llena **en el momento en que "
              f"aparece cada hallazgo**, no al cerrar: un chat no tiene final "
              f"(`13·DOC22`)."]

    p = R.proposito(raiz, ruta)
    if p:
        origen, hid, titulo, retoma = p
        rel_o = os.path.relpath(origen, raiz).replace("\\", "/")
        lineas += ["",
                   f"**El propósito de esta sesión sigue abierto:** {hid} · {titulo}.",
                   f"Vive en `{rel_o}` y ahí se actualiza, no se copia acá.",
                   f"Con qué se retoma: {retoma}" if retoma else ""]
    return "\n".join(l for l in lineas if l)


def aviso(raiz, sesion):
    """Lo que hay que avisar sobre el resumen en este turno, o ""."""
    transcripcion = _sesion_y_transcripcion(raiz, sesion)
    if not transcripcion:
        return ""
    ruta = R.ruta_de(raiz, transcripcion)
    if not ruta or not os.path.isfile(ruta):
        return ""
    if not _produjo_algo(raiz):
        return ""                       # todavía no hay nada que anotar

    pendientes = R.falta(ruta)
    if not pendientes:
        return ""

    rel = os.path.relpath(ruta, raiz).replace("\\", "/")
    for clave in pendientes:
        R.marcar_avisado(ruta, clave)
    if "vacio" in pendientes:
        return ("[EL RESUMEN DE ESTA SESIÓN SIGUE VACÍO]\n"
                f"La sesión ya produjo algo y `{rel}` no tiene ni un hallazgo. "
                "Escribir lo que la sesión lleva dejado, con el modelo de "
                "`plantillas/sesion.md`.")
    abiertos = R.sin_resolver(ruta)
    detalle = "; ".join(f"{h} · {t}" for h, t in abiertos) or "ninguno"
    return ("[FALTA DECIR SI ESTA SESIÓN SE PUEDE CERRAR]\n"
            f"`{rel}` tiene hallazgos pero su sección de cierre está sin llenar. "
            f"Siguen abiertos: {detalle}.")


def _produjo_algo(raiz):
    """Si la sesión ya produjo algo, por dos caminos independientes.

    Uno: hay algo escrito sin guardar en `base/` o en `plantillas/`. Otro: hay
    cambios preparados para guardar. Escribir un borrador no cuenta como
    producir, y por eso no se miran los archivos sueltos del disco.
    """
    import subprocess
    try:
        salida = subprocess.run(["git", "status", "--porcelain"], cwd=raiz,
                                capture_output=True, text=True, timeout=5).stdout
    except (OSError, subprocess.SubprocessError):
        return False
    for linea in salida.splitlines():
        ruta = linea[3:].strip().strip('"')
        if ruta.startswith(("base/", "plantillas/")) or linea[:1] in ("A", "M", "D"):
            return True
    return False


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--modo", choices=("inicio", "aviso"), required=True)
    p.add_argument("--raiz", default="")
    p.add_argument("--estandar", default="")
    args = p.parse_args()

    try:
        entrada = json.load(sys.stdin) if not sys.stdin.isatty() else {}
    except (json.JSONDecodeError, ValueError):
        entrada = {}
    raiz = args.raiz or entrada.get("cwd") or os.getcwd()
    sesion = entrada.get("session_id", "")
    estandar = args.estandar or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    try:
        texto = inicio(raiz, sesion, estandar) if args.modo == "inicio" else aviso(raiz, sesion)
    except Exception as e:                                  # noqa: BLE001
        texto = f"[el enganche del resumen no pudo correr: {e}]"
    if texto:
        print(texto)
    sys.exit(0)


if __name__ == "__main__":
    main()
