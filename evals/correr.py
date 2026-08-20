#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Corre el banco de evaluación del estándar.

    python evals/correr.py

Cada caso de `casos.jsonl` afirma algo que el estándar promete: que un guardián
atrapa el error que dice atrapar, que no atrapa lo que está bien (el falso
positivo es lo que hace que un validador se ignore), y que una sesión medible
queda dentro de su umbral. **Sin esto, cada cambio del estándar es una
apuesta**: se cambia una regla o un validador y nadie mide si el conjunto
sigue atrapando lo mismo (`notas/estructura.md` §9).

Código de salida: 0 si todos los casos pasan, 1 si alguno falla.
"""
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "validadores"))

import brevedad         # noqa: E402
import commits          # noqa: E402
import errores          # noqa: E402
import secretos         # noqa: E402
from comun import preparar_salida  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))


def _texto(caso):
    """El texto del caso. Un secreto de mentira va partido en `texto_partes` y
    se une acá: entero en el archivo, el escaneo del remoto bloquea el push
    aunque sea de prueba (ya pasó dos veces)."""
    return caso.get("texto") or "".join(caso["texto_partes"])


def _detecta(caso):
    """True si el guardián del caso encontró algo en el texto dado."""
    tipo = caso["tipo"]
    if tipo == "commit":
        return bool(commits.validar(_texto(caso)))
    if tipo == "codigo-errores":
        return bool(errores.revisar_texto(_texto(caso)))
    if tipo == "codigo-secretos":
        return bool(secretos.revisar_texto(_texto(caso)))
    raise ValueError(f"tipo desconocido: {tipo}")


def _arranque(raiz):
    """Lo que el enganche de apertura le inyecta al agente para `raiz`."""
    entrada = json.dumps({"session_id": "evals", "cwd": raiz,
                          "hook_event_name": "SessionStart"})
    r = subprocess.run(
        [sys.executable, os.path.join(RAIZ, "adaptadores", "claude-code", "hook_sesion.py"),
         "--raiz", raiz],
        input=entrada, capture_output=True, text=True, encoding="utf-8", timeout=120)
    return json.loads(r.stdout)["hookSpecificOutput"]["additionalContext"]


def correr_caso(caso):
    """`(paso, detalle)` de un caso."""
    if caso["tipo"] == "arranque":
        # La primera promesa del estándar: las reglas llegan al abrir. Quince
        # días faltaron en su propia carpeta sin que nadie lo midiera.
        contexto = _arranque(RAIZ if caso["raiz"] == "estandar" else caso["raiz"])
        paso = caso["espera_texto"] in contexto
        return paso, ("trae" if paso else "no trae") + f" «{caso['espera_texto'][:40]}…»"
    if caso["tipo"] == "transcripcion":
        r = brevedad.resumen(os.path.join(AQUI, caso["fixture"]))
        paso = r["mediana"] <= caso["mediana_max"]
        return paso, f"mediana {r['mediana']} (tope {caso['mediana_max']})"
    detecta = _detecta(caso)
    espera = caso["espera_hallazgo"]
    paso = detecta == espera
    return paso, ("detecta" if detecta else "no detecta") + \
        ("" if paso else f" y se esperaba lo contrario")


def main():
    preparar_salida()
    archivo = os.path.join(AQUI, "casos.jsonl")
    casos = [json.loads(l) for l in open(archivo, encoding="utf-8")
             if l.strip() and not l.lstrip().startswith("//")]
    fallas = 0
    for caso in casos:
        try:
            paso, detalle = correr_caso(caso)
        except Exception as e:                    # el caso roto también es falla
            paso, detalle = False, f"error: {e}"
        marca = "OK " if paso else "FALLA"
        print(f"  {marca}  {caso['id']:<22} {caso['regla']:<8} {detalle}")
        fallas += 0 if paso else 1
    total = len(casos)
    print(f"\n{total - fallas} de {total} caso(s) en verde.")
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
