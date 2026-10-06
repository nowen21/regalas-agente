"""Declara en la fila 22 del análisis 1 del pendiente 116 las rutas que toca el
retiro de los cuatro módulos viejos de validadores/ (acuerdo 15)."""
import io
import subprocess
import sys

ANALISIS = "historico-chat/resumenes/2026-10-04/pendientes/116-el-codigo-de-cimiento-se-repite-en-vez-de-reusarse/analisis-1.md"
MODULOS = ["validadores/comun.py", "validadores/enlaces.py", "validadores/marcas.py", "validadores/sesiones.py"]
OTRAS = [
    "base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md",
    "plantillas/CLAUDE.md.plantilla",
    "plantillas/prompts/prompt-base-usuario.md",
    "anatomia/que-esta-amarrado-a-la-herramienta.md",
    "historico-chat/scripts/2026-10-05/declarar_retiro_fila_22.py",
    "historico-chat/scripts/README.md",
]

salida = subprocess.run([sys.executable, "validadores/retirar.py"] + MODULOS, capture_output=True, text=True, encoding="utf-8").stdout
documentos = [l.split(": ")[0] for l in salida.splitlines() if " enlace(s) a texto" in l]
with io.open(ANALISIS, encoding="utf-8") as f:
    lineas = f.read().split("\n")
for i, l in enumerate(lineas):
    if l.startswith("| 22 |") and "Este análisis, de una y sin fase" in l:
        nuevas = [r for r in MODULOS + documentos + OTRAS if "`%s`" % r not in l]
        lineas[i] = l.rstrip()[:-1].rstrip() + "".join(", `%s`" % r for r in nuevas) + " |"
        print("%d ruta(s) nuevas en la fila 22" % len(nuevas))
        break
with io.open(ANALISIS, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(lineas))
