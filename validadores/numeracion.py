# -*- coding: utf-8 -*-
"""`EP-002 · HU-006` · Una sola numeración, aunque haya dos sesiones.

**El caso está medido.** El 2026-08-14 dos sesiones abiertas sobre el mismo
repositorio dejaron dos numeraciones vivas: una escribió la `10.0.0` mientras
la otra subía la `9.0.0`, la `9.1.0` y la `9.2.0`. Nadie avisó, y al final del
día había entradas del registro escritas por las dos.

**La decisión fue la salida 1 del [pendiente 22](../pendientes/22-dos-sesiones-versionando-a-la-vez.md):
el número lo pone quien guarda, no quien edita.** Editar `VERSION` en medio de
una sesión larga es apostar a que nadie más guarde antes.

**Lo que esto comprueba, en el momento de guardar:**

1. Que el número que trae `VERSION` **avanza** desde el que está guardado. Si
   otra sesión guardó primero, el de esta ya quedó viejo y se ve.
2. Que ese número **tiene su entrada** en el registro.
3. Que **no repite** un número que el registro ya usó.

**No mira el reloj ni quién escribió**, porque no hay forma fiable de saberlo:
mira los números, que es lo que se rompe.
"""
import os
import re
import subprocess

import comun
from comun import AVISO, FALLA, Hallazgo, RAIZ, leer, relativo

_VERSION = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")
_ENTRADA = re.compile(r"(?m)^## (\d+\.\d+\.\d+)\b(.*)$")
_RECONOCIDO = u"número repetido"


def _tupla(v):
    m = _VERSION.match((v or "").strip())
    return tuple(int(x) for x in m.groups()) if m else None


def guardada(raiz, revision="HEAD"):
    """El número que hay en `VERSION` **en lo ya guardado**, o `None`.

    Sin control de versiones no hay con qué comparar, y eso no es un fallo:
    devuelve `None` y quien llama decide.
    """
    try:
        r = subprocess.run(["git", "-C", raiz, "show", "%s:VERSION" % revision],
                           capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=30)
    except (OSError, subprocess.SubprocessError):
        return None
    return r.stdout.strip() if r.returncode == 0 else None


def validar(raiz=None):
    """Los tres hallazgos de la numeración."""
    raiz = raiz or RAIZ
    hallazgos = []
    archivo = os.path.join(raiz, "VERSION")
    registro = os.path.join(raiz, "CHANGELOG.md")

    try:
        ahora = leer(archivo).strip()
        cambios = leer(registro)
    except OSError:
        return []                       # sin los dos archivos no hay nada que decir

    t_ahora = _tupla(ahora)
    if not t_ahora:
        return [Hallazgo(FALLA, archivo, 1,
                         "`VERSION` no tiene la forma `MAYOR.MENOR.PARCHE`")]

    filas = _ENTRADA.findall(cambios)
    entradas = [v for v, _ in filas]
    # Un duplicado que el registro ya reconoce con «número repetido» en su
    # propio título no se renumera: alguien pudo haber adoptado ese número, y
    # cambiárselo ahora le movería el piso. Queda como aviso — sigue a la vista,
    # deja de detener.
    reconocidas = {v for v, resto in filas if _RECONOCIDO in resto}

    # 1 · No se quedó atrás de lo guardado.
    #
    # **Igual no es falla:** recién commiteado, `VERSION` y lo guardado
    # coinciden, y eso es lo normal. La falla es quedar **por debajo**, que solo
    # pasa si otra sesión guardó un número mayor mientras esta editaba.
    antes = guardada(raiz)
    t_antes = _tupla(antes)
    if t_antes and t_ahora < t_antes:
        hallazgos.append(Hallazgo(
            FALLA, archivo, 1,
            f"`VERSION` dice {ahora} y lo guardado ya está en {antes} — otra "
            f"sesión guardó primero y este número quedó viejo. El número lo pone "
            f"quien guarda"))

    # 2 · Tiene su entrada.
    if ahora not in entradas:
        hallazgos.append(Hallazgo(
            FALLA, registro, 0,
            f"`VERSION` dice {ahora} y el registro no tiene su entrada"))

    # 3 · No repite.
    repetidas = sorted({v for v in entradas if entradas.count(v) > 1})
    for v in repetidas:
        conocida = v in reconocidas
        hallazgos.append(Hallazgo(
            AVISO if conocida else FALLA, registro, 0,
            f"el registro tiene {entradas.count(v)} entradas para la {v} — dos "
            f"sesiones numeraron a la vez"
            + (" (ya reconocido en el registro; no se renumera)" if conocida else "")))

    # Y un aviso: hueco en la numeración. No es falla —una versión puede
    # saltarse a propósito— pero casi siempre es la marca de dos sesiones.
    numeros = sorted({_tupla(v) for v in entradas if _tupla(v)})
    for a, b in zip(numeros, numeros[1:]):
        if b[0] == a[0] and b[1] == a[1] and b[2] > a[2] + 1:
            hallazgos.append(Hallazgo(
                AVISO, registro, 0,
                f"hueco entre la {'.'.join(map(str, a))} y la "
                f"{'.'.join(map(str, b))} — puede ser a propósito, o dos "
                f"sesiones numerando"))
    return hallazgos


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("versionado")
