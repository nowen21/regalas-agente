#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Memoria por señales (SQLite + FTS5) — backend central del estándar.

Uso:
  python memoria.py init
  python memoria.py add --tipo decision --titulo "..." --why "..." [--scope organizacion] [...]
  python memoria.py search "facturacion iva" [--scope proyecto:tienda] [--tipo gotcha] [--limit 5]
  python memoria.py supersede S-003 --by S-012
  python memoria.py list [--scope ...] [--tipo ...]

La base por defecto es memoria/senales.db (junto a este script); se puede
cambiar con --db o la variable de entorno MEMORIA_DB.
"""
import argparse, os, sqlite3, sys, datetime

AQUI = os.path.dirname(os.path.abspath(__file__))
DB_DEFAULT = os.environ.get("MEMORIA_DB", os.path.join(AQUI, "senales.db"))
ESQUEMA = os.path.join(AQUI, "esquema.sql")

TIPOS = {"decision","error-resuelto","patron","aprendizaje","alternativa-descartada",
         "supuesto","restriccion","pregunta-abierta","gotcha","deuda-tecnica"}


def conectar(db):
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys=ON")
    return con


def cmd_init(a):
    con = conectar(a.db)
    with open(ESQUEMA, encoding="utf-8") as f:
        con.executescript(f.read())
    con.commit(); con.close()
    print(f"OK: base creada/verificada en {a.db}")


def siguiente_id(con):
    r = con.execute("SELECT id FROM senales ORDER BY rowid DESC LIMIT 1").fetchone()
    n = (int(r["id"].split("-")[1]) + 1) if r else 1
    return f"S-{n:03d}"


def cmd_add(a):
    if a.tipo not in TIPOS:
        sys.exit(f"tipo invalido. Validos: {', '.join(sorted(TIPOS))}")
    con = conectar(a.db)
    sid = siguiente_id(con)
    hoy = datetime.date.today().isoformat()
    con.execute(
        "INSERT INTO senales(id,tipo,titulo,what,why,where_,learned,scope,estado,reemplaza,creada,autor)"
        " VALUES(?,?,?,?,?,?,?,?, 'activa', ?, ?, ?)",
        (sid, a.tipo, a.titulo, a.what, a.why, getattr(a, "where"), a.learned,
         a.scope, a.reemplaza, hoy, a.autor))
    if a.reemplaza:
        con.execute("UPDATE senales SET estado='reemplazada' WHERE id=?", (a.reemplaza,))
    con.commit(); con.close()
    print(f"OK: {sid} registrada ({a.tipo}, scope={a.scope})")


def cmd_search(a):
    con = conectar(a.db)
    sql = ("SELECT s.id, s.tipo, s.titulo, s.scope, s.estado "
           "FROM senales_fts f JOIN senales s ON s.rowid=f.rowid "
           "WHERE senales_fts MATCH ? AND s.estado='activa' ")
    params = [a.query]
    if a.scope:
        sql += "AND s.scope LIKE ? "; params.append(a.scope + "%")
    if a.tipo:
        sql += "AND s.tipo=? "; params.append(a.tipo)
    sql += "ORDER BY bm25(senales_fts) LIMIT ?"; params.append(a.limit)
    filas = con.execute(sql, params).fetchall()
    con.close()
    if not filas:
        print("(sin señales relevantes)"); return
    for r in filas:
        print(f"{r['id']} · {r['tipo']} · [{r['scope']}] {r['titulo']}")


def cmd_supersede(a):
    con = conectar(a.db)
    n = con.execute("UPDATE senales SET estado='reemplazada' WHERE id=?", (a.id,)).rowcount
    con.commit(); con.close()
    print(f"OK: {a.id} marcada reemplazada por {a.by}" if n else f"no existe {a.id}")


def cmd_list(a):
    con = conectar(a.db)
    sql = "SELECT id,tipo,scope,estado,titulo FROM senales WHERE 1=1 "
    params = []
    if a.scope: sql += "AND scope LIKE ? "; params.append(a.scope + "%")
    if a.tipo:  sql += "AND tipo=? "; params.append(a.tipo)
    sql += "ORDER BY rowid"
    for r in con.execute(sql, params):
        print(f"{r['id']} · {r['tipo']} · [{r['scope']}] · {r['estado']} · {r['titulo']}")
    con.close()


def main():
    p = argparse.ArgumentParser(description="Memoria por señales (SQLite+FTS5)")
    p.add_argument("--db", default=DB_DEFAULT)
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init").set_defaults(fn=cmd_init)

    ad = sub.add_parser("add")
    ad.add_argument("--tipo", required=True)
    ad.add_argument("--titulo", required=True)
    ad.add_argument("--what", default=""); ad.add_argument("--why", default="")
    ad.add_argument("--where", default=""); ad.add_argument("--learned", default="")
    ad.add_argument("--scope", default="proyecto")
    ad.add_argument("--reemplaza", default=None); ad.add_argument("--autor", default="")
    ad.set_defaults(fn=cmd_add)

    se = sub.add_parser("search")
    se.add_argument("query")
    se.add_argument("--scope", default=None); se.add_argument("--tipo", default=None)
    se.add_argument("--limit", type=int, default=5)
    se.set_defaults(fn=cmd_search)

    su = sub.add_parser("supersede")
    su.add_argument("id"); su.add_argument("--by", required=True)
    su.set_defaults(fn=cmd_supersede)

    li = sub.add_parser("list")
    li.add_argument("--scope", default=None); li.add_argument("--tipo", default=None)
    li.set_defaults(fn=cmd_list)

    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
