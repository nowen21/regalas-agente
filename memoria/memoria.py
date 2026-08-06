#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Memoria por señales (SQLite + FTS5) — backend central del estándar.

Uso:
  python memoria.py init
  python memoria.py add --tipo decision --titulo "..." --why "..." [--scope organizacion] [...]
  python memoria.py search "facturacion iva" [--scope proyecto:tienda] [--tipo gotcha] [--limit 5] [--meses 6]
  python memoria.py supersede S-003 --by S-012
  python memoria.py revisar S-003                      # marca revisada hoy
  python memoria.py revisar --viejas --scope proyecto:x # ritual: lista las más viejas
  python memoria.py archivar S-003                     # poda: fuera de search, se conserva
  python memoria.py pendientes [--scope modulo:facturacion]  # deuda/preguntas sin cerrar
  python memoria.py cerrar S-014 --ref "F3 / commit abc1234" # cierra deuda resuelta
  python memoria.py list [--scope ...] [--tipo ...]

La base por defecto es memoria/senales.db (junto a este script); se puede
cambiar con --db o la variable de entorno MEMORIA_DB.
"""
import argparse, os, re, sqlite3, sys, datetime

AQUI = os.path.dirname(os.path.abspath(__file__))
DB_DEFAULT = os.environ.get("MEMORIA_DB", os.path.join(AQUI, "senales.db"))
ESQUEMA = os.path.join(AQUI, "esquema.sql")

TIPOS = {"decision","error-resuelto","patron","aprendizaje","alternativa-descartada",
         "supuesto","restriccion","pregunta-abierta","gotcha","deuda-tecnica"}

MESES_VIGENCIA = 6      # sin revisar más que esto -> se muestra "sin verificar"


def conectar(db):
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys=ON")
    return con


def migrar(con):
    """Cambios de esquema sobre una base ya existente. Idempotente.

    `CREATE TABLE IF NOT EXISTS` no agrega columnas nuevas a una tabla que ya
    está, así que la columna `revisada` se suma aquí con ALTER y se rellena con
    `creada` (una señal vieja se considera revisada por última vez al crearse).
    """
    cols = [r[1] for r in con.execute("PRAGMA table_info(senales)")]
    if not cols:
        return
    if "revisada" not in cols:
        con.execute("ALTER TABLE senales ADD COLUMN revisada TEXT")
        con.execute("UPDATE senales SET revisada = creada WHERE revisada IS NULL")
    if "cerrada_en" not in cols:                 # ciclo de vida de la deuda (03)
        con.execute("ALTER TABLE senales ADD COLUMN cerrada_en TEXT")
    if "cierra_ref" not in cols:
        con.execute("ALTER TABLE senales ADD COLUMN cierra_ref TEXT")


def cmd_init(a):
    con = conectar(a.db)
    with open(ESQUEMA, encoding="utf-8") as f:
        con.executescript(f.read())
    migrar(con)
    con.commit(); con.close()
    print(f"OK: base creada/verificada en {a.db}")


def meses_desde(fecha_iso):
    """Meses transcurridos desde una fecha ISO, o None si no se puede leer."""
    try:
        d = datetime.date.fromisoformat(fecha_iso)
    except (ValueError, TypeError):
        return None
    hoy = datetime.date.today()
    return (hoy.year - d.year) * 12 + (hoy.month - d.month)


def marca_vigencia(revisada, meses):
    """Sufijo '⚠ sin verificar hace Nm' si la señal está vieja, o ''."""
    n = meses_desde(revisada)
    return f"  ⚠ sin verificar hace {n}m" if n is not None and n >= meses else ""


def siguiente_id(con):
    r = con.execute("SELECT id FROM senales ORDER BY rowid DESC LIMIT 1").fetchone()
    n = (int(r["id"].split("-")[1]) + 1) if r else 1
    return f"S-{n:03d}"


def cmd_add(a):
    if a.tipo not in TIPOS:
        sys.exit(f"tipo invalido. Validos: {', '.join(sorted(TIPOS))}")
    con = conectar(a.db)
    migrar(con)
    sid = siguiente_id(con)
    hoy = datetime.date.today().isoformat()
    con.execute(
        "INSERT INTO senales(id,tipo,titulo,what,why,where_,learned,scope,estado,reemplaza,creada,revisada,autor)"
        " VALUES(?,?,?,?,?,?,?,?, 'activa', ?, ?, ?, ?)",
        (sid, a.tipo, a.titulo, a.what, a.why, getattr(a, "where"), a.learned,
         a.scope, a.reemplaza, hoy, hoy, a.autor))
    if a.reemplaza:
        con.execute("UPDATE senales SET estado='reemplazada' WHERE id=?", (a.reemplaza,))
    con.commit(); con.close()
    print(f"OK: {sid} registrada ({a.tipo}, scope={a.scope})")


def _fts(q):
    """Términos FTS5 seguros: solo palabras (ignora - + " que rompen la sintaxis)."""
    toks = re.findall(r'\w+', q, re.UNICODE)
    return ' '.join('"%s"*' % t.lower() for t in toks) if toks else None


def cmd_search(a):
    fts = _fts(a.query)
    if not fts:
        print("(término de búsqueda vacío)"); return
    con = conectar(a.db)
    migrar(con)
    # Solo señales 'activa' (deja fuera archivada/reemplazada/revertida).
    # Orden: relevancia léxica y, a igualdad, la revisada más reciente primero,
    # para que lo viejo no tape lo nuevo (F1 · recencia + relevancia).
    sql = ("SELECT s.id, s.tipo, s.titulo, s.scope, s.revisada "
           "FROM senales_fts f JOIN senales s ON s.rowid=f.rowid "
           "WHERE senales_fts MATCH ? AND s.estado='activa' ")
    params = [fts]
    if a.scope:
        sql += "AND s.scope = ? "; params.append(a.scope)
    if a.tipo:
        sql += "AND s.tipo=? "; params.append(a.tipo)
    sql += "ORDER BY bm25(senales_fts), s.revisada DESC LIMIT ?"; params.append(a.limit)
    filas = con.execute(sql, params).fetchall()
    con.close()
    if not filas:
        print("(sin señales relevantes)"); return
    for r in filas:
        print(f"{r['id']} · {r['tipo']} · [{r['scope']}] {r['titulo']}"
              + marca_vigencia(r["revisada"], a.meses))


def cmd_supersede(a):
    con = conectar(a.db)
    n = con.execute("UPDATE senales SET estado='reemplazada' WHERE id=?", (a.id,)).rowcount
    con.commit(); con.close()
    print(f"OK: {a.id} marcada reemplazada por {a.by}" if n else f"no existe {a.id}")


def cmd_revisar(a):
    con = conectar(a.db)
    migrar(con)
    if a.viejas:
        # Ritual: las señales activas más viejas de un scope, para confirmar,
        # reemplazar o archivar. Las más desactualizadas primero.
        sql = ("SELECT id,tipo,scope,revisada,titulo FROM senales "
               "WHERE estado='activa' ")
        params = []
        if a.scope:
            sql += "AND scope = ? "; params.append(a.scope)
        sql += "ORDER BY revisada ASC, rowid ASC LIMIT ?"; params.append(a.limit)
        filas = con.execute(sql, params).fetchall()
        con.close()
        if not filas:
            print("(sin señales activas en ese scope)"); return
        for r in filas:
            print(f"{r['id']} · {r['tipo']} · [{r['scope']}] {r['titulo']}"
                  + marca_vigencia(r["revisada"], a.meses))
        return
    if not a.id:
        sys.exit("indica una señal (`revisar S-003`) o usa `--viejas`")
    hoy = datetime.date.today().isoformat()
    n = con.execute("UPDATE senales SET revisada=? WHERE id=?", (hoy, a.id)).rowcount
    con.commit(); con.close()
    print(f"OK: {a.id} revisada al {hoy}" if n else f"no existe {a.id}")


def cmd_archivar(a):
    con = conectar(a.db)
    migrar(con)
    fila = con.execute("SELECT tipo,estado FROM senales WHERE id=?", (a.id,)).fetchone()
    if not fila:
        con.close(); print(f"no existe {a.id}"); return
    con.execute("UPDATE senales SET estado='archivada' WHERE id=?", (a.id,))
    con.commit(); con.close()
    aviso = ("  (es historia — se conserva; sale de search pero no se borra)"
             if fila["tipo"] in ("decision", "restriccion") else "")
    print(f"OK: {a.id} archivada (fuera de search){aviso}")


DEUDA = ("deuda-tecnica", "pregunta-abierta")


def cmd_pendientes(a):
    """Lo que el agente difirió y sigue abierto: deuda técnica y preguntas."""
    con = conectar(a.db)
    migrar(con)
    sql = ("SELECT id,tipo,scope,revisada,titulo FROM senales "
           "WHERE estado='activa' AND tipo IN (?,?) ")
    params = list(DEUDA)
    if a.scope:
        sql += "AND scope = ? "; params.append(a.scope)
    sql += "ORDER BY revisada ASC, rowid ASC"
    filas = con.execute(sql, params).fetchall()
    con.close()
    if not filas:
        print("(sin deuda abierta en ese scope)"); return
    for r in filas:
        print(f"{r['id']} · {r['tipo']} · [{r['scope']}] {r['titulo']}"
              + marca_vigencia(r["revisada"], MESES_VIGENCIA))


def cmd_cerrar(a):
    """Cierra una deuda/pregunta resuelta: fuera de search, con fecha y referencia."""
    con = conectar(a.db)
    migrar(con)
    hoy = datetime.date.today().isoformat()
    n = con.execute(
        "UPDATE senales SET estado='cerrada', cerrada_en=?, cierra_ref=? WHERE id=?",
        (hoy, a.ref, a.id)).rowcount
    con.commit(); con.close()
    print(f"OK: {a.id} cerrada ({hoy}) — {a.ref}" if n else f"no existe {a.id}")


def cmd_list(a):
    con = conectar(a.db)
    migrar(con)
    sql = "SELECT id,tipo,scope,estado,revisada,titulo FROM senales WHERE 1=1 "
    params = []
    if a.scope: sql += "AND scope LIKE ? "; params.append(a.scope + "%")
    if a.tipo:  sql += "AND tipo=? "; params.append(a.tipo)
    sql += "ORDER BY rowid"
    for r in con.execute(sql, params):
        print(f"{r['id']} · {r['tipo']} · [{r['scope']}] · {r['estado']} · {r['titulo']}"
              + marca_vigencia(r["revisada"], MESES_VIGENCIA))
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
    se.add_argument("--meses", type=int, default=MESES_VIGENCIA,
                    help="marca 'sin verificar' pasados N meses (por defecto 6)")
    se.set_defaults(fn=cmd_search)

    su = sub.add_parser("supersede")
    su.add_argument("id"); su.add_argument("--by", required=True)
    su.set_defaults(fn=cmd_supersede)

    re_ = sub.add_parser("revisar", help="marca una señal como revisada hoy, o lista las viejas")
    re_.add_argument("id", nargs="?", default=None)
    re_.add_argument("--viejas", action="store_true", help="lista las señales activas más viejas")
    re_.add_argument("--scope", default=None)
    re_.add_argument("--limit", type=int, default=10)
    re_.add_argument("--meses", type=int, default=MESES_VIGENCIA)
    re_.set_defaults(fn=cmd_revisar)

    ar = sub.add_parser("archivar", help="poda: saca la señal de search (se conserva)")
    ar.add_argument("id")
    ar.set_defaults(fn=cmd_archivar)

    pe = sub.add_parser("pendientes", help="deuda técnica y preguntas abiertas sin cerrar")
    pe.add_argument("--scope", default=None)
    pe.set_defaults(fn=cmd_pendientes)

    ce = sub.add_parser("cerrar", help="cierra una deuda/pregunta resuelta, con referencia")
    ce.add_argument("id")
    ce.add_argument("--ref", required=True, help="commit / fase / HU que la cerró")
    ce.set_defaults(fn=cmd_cerrar)

    li = sub.add_parser("list")
    li.add_argument("--scope", default=None); li.add_argument("--tipo", default=None)
    li.set_defaults(fn=cmd_list)

    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
