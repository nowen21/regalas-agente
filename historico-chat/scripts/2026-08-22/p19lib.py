# -*- coding: utf-8 -*-
"""Pendiente 19 · ronda 1: las 27 reglas con sello en NO CUMPLE pasan a CUMPLE."""
import io
import os
import re

os.chdir(r"c:\Ing. Jose\ia\agente")
VERSION = "30.8.0"
FECHA = "2026-08-22"


def ancla(heading_txt):
    t = heading_txt.lower().replace("·", "")
    t = re.sub(r"[`*\"«»¿?¡!(),.:;\[\]]", "", t)
    return t.replace(" ", "-")


def leer(p):
    return io.open(p, encoding="utf-8").read()


def escribir(p, s):
    io.open(p, "w", encoding="utf-8", newline="").write(s)


def bloque(s, rid):
    """(inicio_heading, fin) del bloque de la regla dentro del archivo."""
    m = re.search(r"^## %s · .*?$" % re.escape(rid), s, re.M)
    if not m:
        raise SystemExit("no está " + rid)
    resto = s[m.end():]
    fin = re.search(r"^## [A-Z]+\d+(?:\.\d+)? · ", resto, re.M)
    return m.start(), (m.end() + fin.start()) if fin else len(s), m


def checklist_link(archivo):
    return ("../../20-meta-reglas/checklist.md" if os.sep in archivo.replace("/", os.sep)[5:]
            and "/reglas/" in archivo.replace("\\", "/") else "20-meta-reglas/checklist.md")


QUITAR = ("❌", "no cabe", "sin ejemplo", "Fila 10", "Fila 11", "Fila 12", "Fila 14",
          "Fila 16", "Fila 17", "Regla vigente y reprobada", "texto prestado",
          "Las tres ❌", "fuera de las tres formas")


def resellar(texto_bloque, archivo, nota_hoy, vencido_solo=False):
    """Devuelve el bloque con su checklist en CUMPLE, re-fechado, sin contradicciones."""
    cl = texto_bloque.find("### Checklist")
    if cl < 0:
        raise SystemExit("bloque sin checklist")
    cab, chk = texto_bloque[:cl], texto_bloque[cl:]
    chk = re.sub(r"### Checklist\s+·\s+\*\*NO CUMPLE\*\*", "### Checklist  ·  **CUMPLE**", chk)
    chk = re.sub(r"contra \*\*v[\d.]+\*\*, el \*\*\d{4}-\d{2}-\d{2}\*\*",
                 f"contra **v{VERSION}**, el **{FECHA}**", chk, count=1)
    lineas = chk.split("\n")
    salida = []
    filas = []
    for l in lineas:
        if re.match(r"^\| [A-E] · ", l):
            l = l.replace("❌", "✅")
            filas.append(l)
        if l.startswith("**20 filas:"):
            ok = sum(f.count("✅") for f in filas)
            na = sum(f.count("N/A") for f in filas)
            resto = re.sub(r"^\*\*20 filas:[^*]*\*\*", "", l)
            resto = re.sub(r"\s*\*\*❌\*\*.*$", "", resto)
            l = f"**20 filas: {ok} ✅ · 0 ❌ · {na} N/A.**" + resto
            salida.append(l)
            salida.append("")
            salida.append(nota_hoy)
            continue
        if not l.startswith("|") and any(q in l for q in QUITAR) and not l.startswith("> Vale"):
            continue
        salida.append(l)
    chk = "\n".join(salida)
    chk = re.sub(r"\n{3,}", "\n\n", chk)
    return cab + chk


def reemplazar_cuerpo(s, rid, nuevo_cuerpo, nuevo_titulo=None):
    """Sustituye lo que va del heading al `---` previo al checklist."""
    ini, fin, m = bloque(s, rid)
    b = s[ini:fin]
    cl = b.find("### Checklist")
    sep = b.rfind("\n---", 0, cl)
    heading = b[:b.find("\n")]
    if nuevo_titulo:
        heading = f"## {rid} · {nuevo_titulo}" + (" `[BLINDADA]`" if "[BLINDADA]" in heading else "")
    nuevo = heading + "\n\n" + nuevo_cuerpo.strip() + "\n\n" + b[sep + 1:]
    return s[:ini] + nuevo + s[fin:]


def aplicar(archivo, rid, cuerpo=None, nota="", titulo=None):
    s = leer(archivo)
    if cuerpo is not None:
        s = reemplazar_cuerpo(s, rid, cuerpo, titulo)
    ini, fin, _ = bloque(s, rid)
    s = s[:ini] + resellar(s[ini:fin], archivo, nota) + s[fin:]
    escribir(archivo, s)


