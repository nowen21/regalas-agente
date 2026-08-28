# -*- coding: utf-8 -*-
"""T-06: con el registro nuevo, en cuantos commits avisaria la comprobacion.

Es el caso que puede tumbar la fase. Un arreglo que cambia un silencio inutil
por un ruido inutil es PEOR que no hacerlo: el ruido apaga tambien lo que
servia.

El diseno descartado avisaba en 7 de 12. Este tiene que avisar en menos, y la
diferencia es de fondo: alli se avisaba por «no tengo registro», que es el caso
normal; aca se avisa solo cuando DOS sesiones anotaron el mismo archivo, que es
lo que de verdad hay que ver.
"""
import os
import subprocess
import sys

RAIZ = r"c:\Ing. Jose\ia\agente"
sys.path.insert(0, os.path.join(RAIZ, "validadores"))
import sesiones                                          # noqa: E402


def git(*args):
    return subprocess.run(["git"] + list(args), cwd=RAIZ, capture_output=True,
                          text=True, encoding="utf-8", errors="replace").stdout


# Con el registro nuevo, cada sesion anota lo que cambio en su turno. Para
# medirlo sobre el historial se simula: los archivos de un commit se reparten
# entre las sesiones que estaban vivas. La pregunta es cuantas veces DOS
# sesiones distintas coincidirian en el mismo archivo.
vivas = sesiones.registros(RAIZ)
print("Sesiones vivas ahora: %d" % len(vivas))
for s, archivos in vivas.items():
    print("   %s : %d archivos" % (s[:8], len(archivos)))
print()

print("En cuantos de los ultimos commits DOS sesiones coincidirian:")
print()
print("%-10s %-6s %s" % ("COMMIT", "ARCH", "SESIONES QUE COINCIDEN"))
avisaria = 0
total = 0
for linea in git("log", "--format=%h", "-12").splitlines():
    h = linea.strip()
    if not h:
        continue
    archivos = set(l.strip() for l in
                   git("show", "--name-only", "--pretty=format:", h).splitlines()
                   if l.strip())
    if not archivos:
        continue
    total += 1
    coinciden = {s: archivos & suyos for s, suyos in vivas.items()
                 if archivos & suyos}
    if len(coinciden) >= 2:
        avisaria += 1
        detalle = " · ".join("%s:%d" % (s[:8], len(a))
                             for s, a in sorted(coinciden.items()))
    else:
        detalle = "no (%d sesion/es)" % len(coinciden)
    print("%-10s %-6d %s" % (h, len(archivos), detalle))

print()
print("AVISARIA en %d de %d commits." % (avisaria, total))
print()
print("El diseno descartado avisaba en 7 de 12, por «no tengo registro».")
print("Este avisa solo cuando dos sesiones anotaron el mismo archivo.")
print()
print("LIMITE de esta medicion, dicho para que no se lea de mas: hoy hay una")
print("sola sesion viva, asi que el numero real de coincidencias no se puede")
print("observar en el historial. Lo que si se comprueba es que NO avisa por")
print("falta de registro, que era el defecto del diseno descartado.")
