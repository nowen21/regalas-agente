# -*- coding: utf-8 -*-
"""Acuerdo 8 del análisis 1 del pendiente 110: el freno deja instalar paquetes en
el entorno que está dentro del proyecto (pendiente 115, reportado por scilit)."""
import glob
import io
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
A = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "HU-003-*", "pendientes", "110-*", "analisis-1.md"))[0]
P115 = glob.glob(os.path.join(RAIZ, "historico-chat", "resumenes", "*", "pendientes", "115-*"))[0]
rel115 = os.path.relpath(P115, RAIZ).replace("\\", "/")

# 1 · el acuerdo y la fila
t = io.open(A, encoding="utf-8").read()
ancla = "Reemplaza el acuerdo 4 del análisis 13 del pendiente 103 (turnos 625 a 627).\n"
if "8. El freno deja instalar" not in t:
    assert t.count(ancla) == 1
    t = t.replace(ancla, ancla + (
        "8. El pendiente 115, que scilit reportó mientras se trabajaba este análisis, tiene la misma causa 2: el freno detiene toda instalación de paquetes, "
        "aun la que va al entorno `venv/` del proyecto. El freno deja pasar la instalación que corre con el intérprete o el instalador de un entorno que está "
        "dentro del proyecto, y sigue deteniendo la global; se prueba en una copia de scilit con la orden exacta, y el 115 se reúne en el 110 (turnos 628 y 629).\n"))
    r = "| 9 | Que el aviso salga solo con la prueba"
    i = t.index(r); j = t.index("\n", i) + 1
    t = t[:j] + ("| 10 | Que el freno deje instalar paquetes en el entorno del proyecto, con su prueba, y que el 115 se reúna aquí con su prueba en el proyecto | 8 | "
                 "Este análisis, de una y sin fase: `validadores/freno.py`, `validadores/tests/test_el_reporte_de_un_proyecto_se_corrige_para_todos.py`, "
                 "`%s/pendiente.md`, `%s/prueba-en-el-proyecto.md`, `CHANGELOG.md` |\n" % (rel115, rel115)) + t[j:]
    io.open(A, "w", encoding="utf-8", newline="\n").write(t)

# 2 · el freno
F = os.path.join(RAIZ, "validadores", "freno.py")
t = io.open(F, encoding="utf-8").read()
viejo = '''def nunca(orden, en_segundo_plano=False):
    """Por qué esa orden no se deja nunca, o `None`."""
    if en_segundo_plano:
        return "corre en segundo plano y deja su salida fuera del proyecto (04·S9)"
    for patron, porque in _NUNCA:
        if patron.search(orden or ""):
            return porque
    return None
'''
nuevo = '''_INSTALA = re.compile(r"(?:\\bpip3?(?:\\.exe)?|-m\\s+pip)\\s+install\\b", re.I)
_OTROS_INSTALADORES = re.compile(r"\\b(?:npm|apt|apt-get|brew|choco|winget|gem)\\b", re.I)


def _instala_en_el_proyecto(orden, proyecto, cwd):
    """Si cada instalación de paquetes de la orden corre con el intérprete o el
    instalador de un entorno que está dentro del proyecto (`venv/`, `.venv/`):
    instala ahí, no fuera (pendiente 115; análisis 1 del pendiente 110, acuerdo 8)."""
    if not proyecto or _OTROS_INSTALADORES.search(orden or ""):
        return False
    hay = False
    for parte in _partes(orden or ""):
        if not _INSTALA.search(parte):
            continue
        hay = True
        palabras = _palabras(parte)
        if not palabras:
            return False
        programa = ruta_real(palabras[0], cwd or proyecto)
        if relativa(proyecto, programa) is None:
            return False
        if not set(programa.replace("\\\\", "/").lower().split("/")) & {"venv", ".venv", "env", ".env"}:
            return False
    return hay


def nunca(orden, en_segundo_plano=False, proyecto=None, cwd=None):
    """Por qué esa orden no se deja nunca, o `None`."""
    if en_segundo_plano:
        return "corre en segundo plano y deja su salida fuera del proyecto (04·S9)"
    for patron, porque in _NUNCA:
        if patron.search(orden or ""):
            if porque.startswith("instala paquetes") and _instala_en_el_proyecto(orden, proyecto, cwd):
                continue
            return porque
    return None
'''
if "_instala_en_el_proyecto" not in t:
    assert t.count(viejo) == 1
    t = t.replace(viejo, nuevo)
    a = '        porque = nunca(orden, bool(entrada.get("run_in_background")))'
    assert t.count(a) == 1
    t = t.replace(a, '        porque = nunca(orden, bool(entrada.get("run_in_background")), proyecto, cwd)')
    io.open(F, "w", encoding="utf-8", newline="\n").write(t)

# 3 · el 115 se reúne en el 110
p = os.path.join(P115, "pendiente.md")
t = io.open(p, encoding="utf-8").read()
if "Se resuelve en el" not in t:
    rel = os.path.relpath(A, P115).replace("\\", "/")
    i = t.index("\n\n") + 2
    t = t[:i] + ("Se resuelve en el [análisis 1 del pendiente 110: lo que un proyecto reporta es un defecto de Cimiento en todos los proyectos](%s), "
                 "que reúne los reportes de scilit.\n\n" % rel) + t[i:]
    io.open(p, "w", encoding="utf-8", newline="\n").write(t)
print("listo")
