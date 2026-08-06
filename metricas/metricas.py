#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Métricas del proceso — un lector que agrega y reporta (pendiente 06).

No es telemetría: no instrumenta nada nuevo. Deriva lo que **ya se registra** en
`memoria/senales.db` (y, a futuro, el árbol de fases y `git log`). Solo lee y suma.

    python metricas/metricas.py [--db ...] [--scope proyecto:x] [--meses 6]

> **Para decidir, no para calificar.** Una métrica visible se vuelve objetivo y
> deja de medir: "cero fases reabiertas" se consigue no reabriendo ninguna, no
> haciéndolas mejor. Estos números sirven para **decidir qué reglas cambiar**,
> nunca para puntuar el trabajo de nadie.
"""
import argparse
import os
import sqlite3
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, "..", "memoria"))
import memoria  # noqa: E402  (reutiliza meses_desde y el default de la base)

DEUDA = ("deuda-tecnica", "pregunta-abierta")
MESES_VIGENCIA = 6


def resumen(filas, meses=MESES_VIGENCIA):
    """Núcleo puro: agrega una lista de señales (dicts con tipo/estado/revisada).
    Aislado de la base para poder probarlo con filas sintéticas."""
    m = {"total": len(filas), "por_estado": {}, "por_tipo": {},
         "deuda_abierta": 0, "deuda_cerrada": 0, "sin_verificar": 0}
    for f in filas:
        m["por_estado"][f["estado"]] = m["por_estado"].get(f["estado"], 0) + 1
        m["por_tipo"][f["tipo"]] = m["por_tipo"].get(f["tipo"], 0) + 1
        if f["tipo"] in DEUDA:
            if f["estado"] == "activa":
                m["deuda_abierta"] += 1
            elif f["estado"] == "cerrada":
                m["deuda_cerrada"] += 1
        if f["estado"] == "activa":
            n = memoria.meses_desde(f.get("revisada"))
            if n is not None and n >= meses:
                m["sin_verificar"] += 1
    return m


def _leer(db, scope):
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row
    sql = "SELECT tipo, estado, revisada FROM senales WHERE 1=1 "
    params = []
    if scope:
        sql += "AND scope = ? "; params.append(scope)
    filas = [dict(r) for r in con.execute(sql, params)]
    con.close()
    return filas


def _pct(parte, total):
    return f"{100 * parte // total}%" if total else "—"


def reportar(m, meses):
    lineas = []
    lineas.append("== Métricas del proceso (para decidir qué reglas cambiar, no para calificar) ==")
    lineas.append(f"Señales: {m['total']}")

    total_deuda = m["deuda_abierta"] + m["deuda_cerrada"]
    lineas.append(
        f"Deuda diferida: {m['deuda_abierta']} abierta · {m['deuda_cerrada']} cerrada"
        f" ({_pct(m['deuda_cerrada'], total_deuda)} resuelta)"
        "  — si la abierta solo crece, §Fuera-de-scope se volvió un basurero")

    activas = m["por_estado"].get("activa", 0)
    lineas.append(
        f"Sin verificar (>{meses} meses): {m['sin_verificar']} de {activas} activas"
        f" ({_pct(m['sin_verificar'], activas)})  — vigencia (02)")

    lineas.append("Por estado: " + " · ".join(
        f"{k} {v}" for k, v in sorted(m["por_estado"].items())))
    lineas.append("Por tipo: " + " · ".join(
        f"{k} {v}" for k, v in sorted(m["por_tipo"].items())))
    return "\n".join(lineas)


def main():
    p = argparse.ArgumentParser(description="Métricas del proceso (lector, no telemetría)")
    p.add_argument("--db", default=memoria.DB_DEFAULT)
    p.add_argument("--scope", default=None)
    p.add_argument("--meses", type=int, default=MESES_VIGENCIA)
    a = p.parse_args()
    if not os.path.isfile(a.db):
        sys.exit(f"no existe la base {a.db} (corré memoria/memoria.py init)")
    print(reportar(resumen(_leer(a.db, a.scope), a.meses), a.meses))


if __name__ == "__main__":
    main()
