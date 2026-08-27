# -*- coding: utf-8 -*-
"""Pasa a cerrada la estación de las fases que están cerradas de hecho.

**Qué se toca y qué no.** Solo `estado-fase.md`, que es el documento que dice
«abierta» cuando no lo está. El `funcionalidad_implementada.md` **no se toca**:
esos cierres son de un molde más viejo que no tenía fila de commit, así que no
mienten, simplemente no registran ese dato. Agregarles una fila sería reescribir
un documento cerrado para meterle algo que su molde no pedía.

**El hash no se inventa: sale de `git log`** sobre el propio documento de
cierre. Si un cierre no está en git, esa fase no se toca y se dice por qué.
"""
import io
import os
import re
import subprocess
import sys

RAIZ = "documentacion"
EST = re.compile(r"\*\*Estación actual:\*\*\s*([^\n]*)")
COMMIT_EN_CIERRE = re.compile(r"\*\*Commit\*\*\s*\|\s*`?([0-9a-f]{7,})")
# `| 9 | Commit único | 👤 pendiente de autorización | ☐ |`
FILA_9 = re.compile(r"^\|\s*9\s*\|([^|]*)\|([^|]*)\|\s*☐\s*\|\s*$",
                    re.MULTILINE)

solo_mirar = "--aplicar" not in sys.argv


def hash_de(archivo):
    salida = subprocess.run(["git", "log", "-1", "--format=%h", "--", archivo],
                            capture_output=True, text=True)
    return salida.stdout.strip()


candidatas = []
for r, _, a in os.walk(RAIZ):
    if "estado-fase.md" not in a:
        continue
    ruta_estado = os.path.join(r, "estado-fase.md")
    t = io.open(ruta_estado, encoding="utf-8", errors="replace").read()
    m = EST.search(t)
    if not m:
        continue
    n = re.match(r"^\s*(\d+)", m.group(1).strip())
    if not n or int(n.group(1)) != 8:
        continue
    cierre = os.path.join(r, "funcionalidad_implementada.md")
    if not os.path.isfile(cierre):
        continue
    if COMMIT_EN_CIERRE.search(
            io.open(cierre, encoding="utf-8", errors="replace").read()):
        continue          # ya tiene su hash anotado: no es de estas
    candidatas.append((r, ruta_estado, cierre))

print("Fases en estación 8 con su cierre escrito y sin hash: %d"
      % len(candidatas))
print()

tocadas, saltadas = 0, []
for carpeta, ruta_estado, cierre in candidatas:
    commit = hash_de(cierre)
    nombre = os.path.basename(carpeta)
    if not commit:
        saltadas.append((nombre, "su cierre no está en git"))
        continue

    e = io.open(ruta_estado, encoding="utf-8", errors="replace").read()
    nuevo = EST.sub(
        "**Estación actual:** cerrada. **Última puerta pasada:** 9, el commit "
        "`%s`.\n\n> **La estación se corrigió el 2026-08-25**, leyendo el "
        "historial: el trabajo de esta fase estaba guardado desde hacía "
        "tiempo, y lo que faltaba era la marca. El hash sale de `git log` "
        "sobre su documento de cierre, no de una suposición." % commit,
        e, count=1)
    nuevo, marcadas = FILA_9.subn(
        lambda m: "| 9 |%s| 👤 Commit `%s`, verificado en el historial | ☑ |"
                  % (m.group(1), commit), nuevo, count=1)
    # Algunas de estas fases no tienen tabla de estaciones: solo la linea.
    # Se corrige igual, porque la linea es lo que dice "abierta".
    sin_tabla = "" if marcadas else "   (no tiene tabla de estaciones)"

    if solo_mirar:
        print("  %s  ->  %s%s" % (commit, nombre[:52], sin_tabla))
    else:
        io.open(ruta_estado, "w", encoding="utf-8", newline="\n").write(nuevo)
    tocadas += 1

print()
print("Fases %s: %d" % ("que se tocarían" if solo_mirar else "corregidas",
                        tocadas))
if saltadas:
    print()
    print("NO se tocaron, y por qué:")
    for nombre, porque in saltadas:
        print("   %-56s %s" % (nombre[:56], porque))
if solo_mirar:
    print()
    print("(esto fue solo mirar. Con --aplicar se escribe)")
