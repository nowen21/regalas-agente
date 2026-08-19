#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganches de Claude Code que sostienen el resumen de la sesión.

Se conectan en `.claude/settings.json`:

    SessionStart      -> python hook_resumen.py --modo inicio --raiz <proyecto>
    UserPromptSubmit  -> python hook_resumen.py --modo aviso  --raiz <proyecto>

Los dos aseguran el archivo del resumen con el modelo puesto y muestran lo que
sigue abierto del propósito de la sesión; el segundo avisa además qué le falta,
una vez por cada cosa que falte.

**El archivo nace en el primer mensaje del usuario, no al abrir.** Al abrir, la
transcripción de la sesión todavía no existe, y de su nombre sale el nombre del
resumen. Por eso los dos modos crean: la sesión que se retoma lo tiene desde el
arranque, y la nueva lo tiene en el primer turno.

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

# **Vive en el adaptador, no en `validadores/`.** Por eso tiene que decir
# dónde están los módulos que usa: el trabajo es agnóstico y sigue allá;
# acá sólo está lo que habla con esta herramienta.
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "validadores"))
import historico                        # noqa: E402
import resumen as R                     # noqa: E402
from comun import preparar_salida       # noqa: E402


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


def _asegurar(raiz, sesion, estandar):
    """El resumen de esta sesión, creándolo si falta. Devuelve (ruta, si nació).

    Se llama desde los **dos** modos, y no solo al abrir, porque al abrir la
    transcripción todavía no existe: la escribe `hook_historico.py` en el primer
    mensaje del usuario. Colgar la creación solo de `SessionStart` era pedirle el
    archivo a un programa que no tenía todavía de dónde sacarle el nombre.

    Los enganches de un mismo evento pueden correr a la vez, así que el orden no
    se da por hecho: si en este turno la transcripción no está, el turno
    siguiente lo crea.
    """
    transcripcion = _sesion_y_transcripcion(raiz, sesion)
    if not transcripcion:
        return "", False
    antes = R.ruta_de(raiz, transcripcion)
    existia = bool(antes) and os.path.isfile(antes)
    ruta = R.crear(raiz, transcripcion, estandar)
    return ruta, bool(ruta) and not existia


def inicio(raiz, sesion, estandar):
    """Crea el resumen y devuelve lo que hay que mostrarle al agente."""
    ruta, _ = _asegurar(raiz, sesion, estandar)
    if not ruta:
        return ""
    return _arranque(raiz, ruta)


def _arranque(raiz, ruta):
    """El mensaje de cuando el archivo ya está: dónde vive y qué sigue abierto."""
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


def aviso(raiz, sesion, estandar=""):
    """Lo que hay que avisar sobre el resumen en este turno, o "".

    Asegura el archivo antes de mirarlo: este es el primer momento de la sesión
    en que la transcripción ya existe, así que acá es donde el resumen nace de
    verdad. El turno en que nace muestra el mensaje de arranque, no el aviso: lo
    que falta se dice desde el turno siguiente.
    """
    ruta, nacio = _asegurar(raiz, sesion, estandar)
    if not ruta:
        return ""
    if nacio:
        return _arranque(raiz, ruta)
    if not _produjo_algo(raiz):
        return ""                       # todavía no hay nada que anotar

    pendientes = R.falta(ruta)
    if not pendientes:
        return ""

    rel = os.path.relpath(ruta, raiz).replace("\\", "/")
    for clave in pendientes:
        R.marcar_avisado(ruta, clave)
    if "molde" in pendientes:
        fuera = R.hallazgos_fuera_del_molde(ruta)
        return ("[LOS HALLAZGOS DE ESTE RESUMEN NO SE LEEN]\n"
                f"`{rel}` tiene {len(fuera)} hallazgo(s) escritos como `### N ·` "
                "y el molde pide `### H-N ·` (`plantillas/sesion.md`). Escritos "
                "así **el programa no ve ninguno**: se cuentan como resumen "
                "vacío, y la comprobación del cierre no llega a correr. "
                "Renumerarlos, que ya están escritos.")
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
    # Su texto lleva acentos y comillas angulares. Sin esto sale en la página de
    # códigos de la consola y quien lo lea recibe mojibake — o, si la salida va a
    # una tubería, no se puede ni decodificar. Era el único enganche que no lo
    # hacía; es el mismo descuido que cerró el pendiente 45 en el instalador.
    preparar_salida()
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
    # **Tres niveles, no dos**: este archivo vive en
    # `adaptadores/claude-code/`, no en `validadores/`. Contar mal los
    # niveles no revienta — apunta a una carpeta que existe y el
    # enganche deja de escribir en silencio, que es peor.
    estandar = args.estandar or os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))

    try:
        texto = (inicio(raiz, sesion, estandar) if args.modo == "inicio"
                 else aviso(raiz, sesion, estandar))
    except Exception as e:                                  # noqa: BLE001
        texto = f"[el enganche del resumen no pudo correr: {e}]"
    if texto:
        print(texto)
    sys.exit(0)


if __name__ == "__main__":
    main()
