# -*- coding: utf-8 -*-
"""Agrega a pendientes.py las dos comprobaciones de EP-004 · HU-016."""
import io, os
os.chdir(r"c:\Ing. Jose\ia\agente")
p = "validadores/pendientes.py"
s = io.open(p, encoding="utf-8").read()

NUEVO = '''
# `EP-004·HU-016` · La ficha de cabecera de un pendiente, sus dos filas.
#
# **Por qué una fila y no una sección.** Una sección se olvida sin dejar rastro;
# una fila de la ficha se ve vacía. Es la decisión 27 del pendiente 59, tomada
# con el dato a la vista: solo **1 de 35** archivos de `hecho/` la llevaba.
_FILA_HISTORIA = re.compile(r"^\\|\\s*\\*\\*Historia de usuario\\*\\*\\s*\\|(.+?)\\|\\s*$", re.M)
_FILA_FASE = re.compile(r"^\\|\\s*\\*\\*Fase\\*\\*\\s*\\|(.+?)\\|\\s*$", re.M)

# Una fase se nombra `X-EP-NNN-HU-NNN-...` (`02·F12`, punto 6).
_NOMBRE_FASE = re.compile(r"\\b([A-Z]-EP-\\d{3}-HU-\\d{3}-[\\w\\-]+)")

# `EP-004·HU-016` · **Desde cuándo se exige.** Es la decisión 26 del pendiente
# 59: desde el 2026-08-16, que es cuando nació la exigencia. Lo cerrado antes no
# se reabre, igual que `20·M10` hace con cualquier norma nueva.
CORTE = "2026-08-16"

# Lo que se cierra **sin construir nada**: una decisión, una medición que dio en
# cero, un duplicado. No tuvo fase porque no hubo desarrollo, y exigirle una
# obligaría a inventarla.
_SIN_FASE = re.compile(
    r"(?i)cerrad[oa] por decisión|no hubo (?:que )?constru|"
    r"sin fase porque|no fue desarrollo|se cerró sin construir")


def _fecha_de_cierre(texto):
    """La fecha que el propio pendiente declara al cerrarse, o "" si no dice."""
    m = re.search(r"(?i)\\*\\*hecho\\*\\*[^\\n]*?(\\d{4}-\\d{2}-\\d{2})", texto)
    if m:
        return m.group(1)
    m = re.search(r"(?i)cerrad[oa][^\\n]*?(\\d{4}-\\d{2}-\\d{2})", texto)
    return m.group(1) if m else ""


def cerrado_declara_su_fase(raiz):
    """`CA-01` · un pendiente cerrado dice en qué fase se hizo.

    **Aviso, no falla.** Que falte la fila no rompe nada hoy: dice que la
    trazabilidad hacia abajo se cortó. Detener la corrida por un pendiente
    viejo sería un obstáculo permanente, y eso se apaga.
    """
    carpeta = os.path.join(raiz, CARPETA, HECHO)
    if not os.path.isdir(carpeta):
        return []
    hallazgos = []
    for nombre in sorted(os.listdir(carpeta)):
        if not nombre.lower().endswith(".md") or nombre.upper() == "README.MD":
            continue
        ruta = os.path.join(carpeta, nombre)
        texto = _leer(ruta)
        fecha = _fecha_de_cierre(texto)
        if fecha and fecha < CORTE:
            continue                       # lo cerrado antes no se reabre
        if _SIN_FASE.search(texto):
            continue                       # no hubo desarrollo: no hay fase
        fases = _NOMBRE_FASE.findall(texto)
        if not fases:
            hallazgos.append(Hallazgo(
                AVISO, ruta, 0,
                "no dice en qué fase se hizo — un pendiente cerrado sin su fase "
                "corta la trazabilidad hacia abajo (EP-004·HU-016)"))
            continue
        for fase in sorted(set(fases)):
            if not _existe_la_fase(raiz, fase):
                hallazgos.append(Hallazgo(
                    AVISO, ruta, 0,
                    f"nombra la fase `{fase}`, que no existe en "
                    f"`documentacion/epicas/` — o se renombró, o nunca estuvo"))
    return hallazgos


def _existe_la_fase(raiz, nombre):
    epicas = os.path.join(raiz, "documentacion", "epicas")
    for actual, carpetas, _ in os.walk(epicas):
        if nombre in carpetas:
            return True
    return False


def abierto_nombra_su_historia(raiz):
    """`CA-02` · un pendiente abierto dice a qué historia baja.

    **Falla, no aviso.** Un pendiente abierto sin historia no se puede
    ejecutar: `02·F23` manda bajarlo a fase de una historia, y sin ella nadie
    sabe de cuál. El enrutamiento del 2026-08-17 dejó las 33 con la suya, y
    esto es lo que impide que la 34 nazca sin ella.
    """
    carpeta = os.path.join(raiz, CARPETA)
    if not os.path.isdir(carpeta):
        return []
    hallazgos = []
    for nombre in sorted(os.listdir(carpeta)):
        if not re.match(r"^\\d+-.+\\.md$", nombre, re.I):
            continue
        ruta = os.path.join(carpeta, nombre)
        texto = _leer(ruta)
        m = _FILA_HISTORIA.search(texto)
        if not m:
            hallazgos.append(Hallazgo(
                FALLA, ruta, 0,
                "no trae la fila **Historia de usuario** en su ficha — sin ella "
                "nadie sabe a qué historia baja este pendiente (02·F23)"))
            continue
        dicho = m.group(1).strip()
        if not dicho or dicho in ("—", "-"):
            hallazgos.append(Hallazgo(
                FALLA, ruta, 0,
                "la fila **Historia de usuario** está vacía — o nombra la "
                "historia, o dice por qué todavía no tiene"))
    return hallazgos

'''

ancla = "def _archivos(carpeta):"
assert ancla in s
s = s.replace(ancla, NUEVO.lstrip("\n") + "\n" + ancla, 1)

# engancharlas en validar()
import re as _re
m = _re.search(r"def validar\(([^)]*)\):", s)
print("validar firma:", m.group(0) if m else "no está")
io.open(p, "w", encoding="utf-8", newline="").write(s)
print("escrito")
