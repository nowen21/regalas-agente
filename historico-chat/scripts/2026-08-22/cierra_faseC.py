# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, r"C:/Users/user/AppData/Local/Temp/claude/c--Ing--Jose-ia-agente/563dc2f9-c782-46f9-af82-c9bc948b3566/scratchpad")
import p19lib as L
os.chdir(r"c:\Ing. Jose\ia\agente")
H = "documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/"

# la HU registra la fase y el CA-06 en su tabla
p = H + "HU-007-regla-de-las-reglas.md"
s = L.leer(p)
a = "| [B-EP-001-HU-007-primero-que-el-proceso-sirva](B-EP-001-HU-007-primero-que-el-proceso-sirva/README.md) | CA-05 |"
i = s.find(a)
fin = s.find("\n", i)
s = s[:fin + 1] + "| [C-EP-001-HU-007-el-barrido-de-candidatas-tiene-molde-y-disparador](C-EP-001-HU-007-el-barrido-de-candidatas-tiene-molde-y-disparador/README.md) | CA-06 | **Cerrada 2026-08-22 — Cumple** (5 de 5; v31.0.0). Nace `20·M20` y el molde del barrido, desde el punto 2 del [pendiente 33](../../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md) |\n" + s[fin + 1:]
L.escribir(p, s)

# README de la HU
p = H + "README.md"
s = L.leer(p)
if "C-EP-001-HU-007" not in s:
    a2 = "B-EP-001-HU-007-primero-que-el-proceso-sirva"
    i = s.rfind(a2)
    fin = s.find("\n", i)
    s = s[:fin + 1] + "| [C-EP-001-HU-007-el-barrido-de-candidatas-tiene-molde-y-disparador](C-EP-001-HU-007-el-barrido-de-candidatas-tiene-molde-y-disparador/README.md) | El barrido de lo que se pidió dos veces gana molde y disparador: nace `20·M20` (2026-08-22) |\n" + s[fin + 1:]
    L.escribir(p, s)

# versión y registro
assert L.leer("VERSION").strip() == "30.9.1"
L.escribir("VERSION", "31.0.0\n")
c = L.leer("CHANGELOG.md")
e = """## 31.0.0 — 2026-08-22

**MAYOR** ⚠ obliga a migrar (antes de publicar una versión hay que releer el tramo y anotar lo que se pidió dos veces).

**Lo que alguien pide dos veces deja de perderse entre sesiones.** Hasta hoy, un criterio que el usuario repetía en sesiones distintas solo se convertía en regla si alguien lo notaba en el momento; si no, se repetía la corrección tres o cuatro veces más. Desde esta versión, antes de publicar se relee el tramo que se cierra y lo repetido se escribe en un documento con su salida: ya está cubierto, merece regla nueva, hay que afinar una existente, o no es regla del estándar. Decidir cuáles se escriben sigue siendo del usuario.

**Qué hay que hacer para adoptarla.** Al cerrar la próxima versión, escribir el barrido con el molde nuevo, [plantillas/candidatas-a-regla.md](plantillas/candidatas-a-regla.md). No hay que barrer hacia atrás: rige del tramo en curso en adelante.

**El detalle.** Nace [`20·M20`](base/20-meta-reglas/reglas/M20-antes-de-publicar-una-version-se-barre-lo-que-se-pidio-dos-veces.md), que extiende a `01·C10` (esa atrapa el patrón en el momento; esta relee lo que en el momento no se notó), y el criterio `CA-06` de EP-001 · HU-007, en la fase [`C`](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/C-EP-001-HU-007-el-barrido-de-candidatas-tiene-molde-y-disparador/README.md). Sale del punto 2 del pendiente [33](pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md), abierto desde el 2026-08-06, donde el defecto estaba dicho así: «sin disparador, se hace cuando el usuario lo pida es un favor, no una norma». El barrido se había hecho una sola vez, el 2026-08-13, con 27 fichas; las cuatro salidas del molde las cubren todas.

"""
L.escribir("CHANGELOG.md", c.replace("## 30.9.1 — 2026-08-22", e + "## 30.9.1 — 2026-08-22", 1))
print("ok")
