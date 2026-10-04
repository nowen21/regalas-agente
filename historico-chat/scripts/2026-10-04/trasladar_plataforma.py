# -*- coding: utf-8 -*-
"""Traslado de `plataforma/` a `proyectos/plataforma/` (análisis 1 del pendiente 116, acuerdo 7).

    python trasladar_plataforma.py fila      # escribe la fila 9 del análisis con las rutas exactas
    python trasladar_plataforma.py enlaces   # los enlaces a plataforma/ pasan a proyectos/plataforma/

Las rutas se calculan con `git grep`: escribirlas a mano dejaría por fuera alguna
de las 51, y el freno solo deja pasar las que la fila nombra.
"""
import os
import re
import subprocess
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
ANALISIS = os.path.join(RAIZ, "historico-chat", "resumenes", "2026-10-04", "pendientes",
                        "116-el-codigo-de-cimiento-se-repite-en-vez-de-reusarse", "analisis-1.md")
ENLACE = re.compile(r"(\]\((?:\.\./|\./)*)plataforma/")
FIJAS = [".gitignore", "validadores/comun.py", "validadores/corredor.py", "plataforma",
         "proyectos/plataforma", "proyectos/plataforma/config/settings/base.py",
         "proyectos/plataforma/nucleo/ciclo_de_vida/core.py"]


def documentos():
    salida = subprocess.run(
        ["git", "-C", RAIZ, "grep", "-l", "-E", r"\]\(([./]*)plataforma/", "--", "*.md",
         ":!plataforma", ":!historico-chat"],
        capture_output=True, text=True, encoding="utf-8").stdout
    return [l.strip() for l in salida.splitlines() if l.strip()]


def fila():
    with open(ANALISIS, encoding="utf-8") as f:
        texto = f.read()
    if "\n| 9 |" in texto:
        print("la fila 9 ya está")
        return
    rutas = ", ".join("`%s`" % r for r in FIJAS + documentos())
    nueva = ("| 9 | Trasladar `plataforma/` a `proyectos/plataforma/` con su historia: Cimiento la "
             "ignora, la plataforma busca el estándar subiendo de carpeta y los enlaces de los "
             "documentos pasan a la ruta nueva | 7 | Este análisis, de una y sin fase: %s, hecho el "
             "2026-10-04 |" % rutas)
    ancla = re.search(r"^\| 8 \|.*$", texto, re.M)
    texto = texto[:ancla.end()] + "\n" + nueva + texto[ancla.end():]
    with open(ANALISIS, "w", encoding="utf-8") as f:
        f.write(texto)
    print("fila 9 escrita con %d rutas" % (len(FIJAS) + len(documentos())))


def enlaces():
    cambiados = 0
    for rel in documentos():
        ruta = os.path.join(RAIZ, rel)
        with open(ruta, encoding="utf-8") as f:
            texto = f.read()
        nuevo = ENLACE.sub(lambda m: m.group(1) + "proyectos/plataforma/", texto)
        if nuevo != texto:
            with open(ruta, "w", encoding="utf-8", newline="") as f:
                f.write(nuevo)
            cambiados += 1
    print("%d documentos con enlaces nuevos" % cambiados)


if __name__ == "__main__":
    if sys.argv[1] in ("fila", "enlaces"):
        {"fila": fila, "enlaces": enlaces}[sys.argv[1]]()


# ── acuerdos 8 a 10: Cimiento es la aplicación Django y parte de una base limpia ──

BASE = "proyectos/cimiento/"
LIMPIEZA = ["nucleo", "datos", "terceros", "templates", "templates/.gitkeep", "static",
            "static/.gitkeep", "proyectos", "descargar_estaticos.py", "indice.sqlite3",
            "config/ambiente.py", "config/settings/base.py", "config/settings/local.py",
            "config/urls.py", "README.md", ".env.example", ".gitignore", "requirements/base.txt",
            "requirements/local.txt", "requirements/lock.txt", "core", "core/__init__.py",
            ".agente/mapeo-nombres.md"]


def _enlazan_a(carpeta):
    salida = subprocess.run(
        ["git", "-C", RAIZ, "grep", "-l", "-E", r"\]\(([./]*)%s/" % carpeta, "--", "*.md",
         ":!historico-chat"], capture_output=True, text=True, encoding="utf-8").stdout
    return [l.strip() for l in salida.splitlines() if l.strip()]


def _epicas():
    carpeta = os.path.join(RAIZ, "documentacion", "epicas")
    return ["documentacion/epicas/%s/epica.md" % e for e in sorted(os.listdir(carpeta))
            if re.match(r"EP-0(0[89]|1\d|2[012])-", e)]


def filas_base():
    with open(ANALISIS, encoding="utf-8") as f:
        texto = f.read()
    if "\n| 10 |" in texto:
        print("las filas 10 a 12 ya están")
        return
    lista = lambda rutas: ", ".join("`%s`" % r for r in rutas)
    nuevas = [
        "| 10 | La carpeta pasa a llamarse `proyectos/cimiento/`: corregir la ruta de las pruebas "
        "y los enlaces de los documentos | 8 | Este análisis, de una y sin fase: %s, hecho el 2026-10-04 |"
        % lista(["validadores/corredor.py"] + _enlazan_a("proyectos/plataforma")),
        "| 11 | Dejar en `proyectos/cimiento/` solo la base Django de la plantilla, con el paquete "
        "`core/`, y probar que arranca | 9 | Este análisis, de una y sin fase: %s, hecho el 2026-10-04 |"
        % lista(BASE + r for r in LIMPIEZA),
        "| 12 | Marcar como retiradas las épicas `EP-008` a `EP-022`, con fecha y enlace a este "
        "análisis | 10 | Este análisis, de una y sin fase: %s, hecho el 2026-10-04 |" % lista(_epicas()),
    ]
    import re as _re
    ancla = _re.search(r"^\| 9 \|.*$", texto, _re.M)
    texto = texto[:ancla.end()] + "\n" + "\n".join(nuevas) + texto[ancla.end():]
    with open(ANALISIS, "w", encoding="utf-8") as f:
        f.write(texto)
    print("filas 10 a 12 escritas")


def enlaces_cimiento():
    cambiados = 0
    for rel in _enlazan_a("proyectos/plataforma"):
        ruta = os.path.join(RAIZ, rel)
        with open(ruta, encoding="utf-8") as f:
            texto = f.read()
        nuevo = texto.replace("proyectos/plataforma/", "proyectos/cimiento/")
        if nuevo != texto:
            with open(ruta, "w", encoding="utf-8", newline="") as f:
                f.write(nuevo)
            cambiados += 1
    print("%d documentos apuntan a proyectos/cimiento/" % cambiados)


if __name__ == "__main__" and sys.argv[1] in ("filas_base", "enlaces_cimiento"):
    {"filas_base": filas_base, "enlaces_cimiento": enlaces_cimiento}[sys.argv[1]]()
