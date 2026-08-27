# -*- coding: utf-8 -*-
"""T-05 - Normaliza el campo Estado de las historias.

**Se cambia la palabra, no la frase.** Varias traen texto util detras —la
fecha, los criterios verificados— y eso se conserva entero. Es lo que `CP-002`
paso 5 comprueba.

Sin `--aplicar` solo dice que haria.
"""
import io
import os
import re
import sys

os.chdir(r"c:\Ing. Jose\ia\agente")

# El mapa completo, declarado en el plan §2.1. Se ordena de mas largo a mas
# corto para que `En implementación` gane sobre un hipotetico `En`.
MAPA = [
    ("En implementación", "En curso"),
    ("Backlog", "Pendiente"),
    ("Cumplida", "Terminada"),
    ("Terminada", "Terminada"),
    ("Cerrada", "Terminada"),
    ("Hecha", "Terminada"),
    ("Done", "Terminada"),
    ("Aprobada", "Lista"),
    ("Escrita", "Pendiente"),
    ("Ready", "Lista"),
    ("En curso", "En curso"),
    ("En QA", "En prueba"),
]

EST = re.compile(r"^(\|\s*\*\*Estado\*\*\s*\|\s*)(.+?)(\s*\|)\s*$", re.M)
# La palabra puede venir en negrita: `**Cumplida.**`
PALABRA = re.compile(r"^(\**)([A-Za-zÁÉÍÓÚáéíóúÑñ]+(?: [A-Za-zÁÉÍÓÚáéíóúÑñ]+)?)")

aplicar = "--aplicar" in sys.argv
cambios, sin_mapa, iguales = [], [], 0

for base, _d, arch in os.walk("documentacion/epicas"):
    for a in sorted(arch):
        if not re.match(r"^HU-\d+-.*\.md$", a):
            continue
        ruta = os.path.join(base, a).replace(os.sep, "/")
        t = io.open(ruta, encoding="utf-8").read()
        m = EST.search(t)
        if not m:
            continue
        valor = m.group(2)

        destino = None
        for de, a_ in MAPA:
            # se compara sobre el valor sin marcado de negrita
            limpio = valor.lstrip("*")
            if limpio.startswith(de):
                destino, origen = a_, de
                break
        if destino is None:
            sin_mapa.append((ruta, valor))
            continue

        # Se reemplaza SOLO la palabra, conservando lo que sigue y quitando
        # el marcado de negrita, que no aporta y estorba a la comprobacion.
        venia_en_negrita = valor.startswith("*")
        limpio = valor.lstrip("*")
        resto = limpio[len(origen):]
        if venia_en_negrita:
            # `**Cumplida.** Los tres...` deja `.** Los tres...`. El `**` que
            # cierra la negrita queda **en medio**, no al final: quitarlo con
            # `rstrip` no funciona y deja `Terminada** Los tres...`.
            # Se quita la primera aparicion, y el punto se conserva porque es
            # de la frase: queda `Terminada. Los tres...`.
            resto = resto.replace("**", "", 1)
        # **El punto NO se quita si no venia en negrita.** `En implementación.
        # CA-01 cerrado...` lo necesita: sin el quedaria `En curso CA-01
        # cerrado`. Lo destapo el ensayo, no la lectura.
        nuevo_valor = (destino + resto).strip()

        if nuevo_valor == valor:
            iguales += 1
            continue
        cambios.append((ruta, valor, nuevo_valor))
        if aplicar:
            io.open(ruta, "w", encoding="utf-8", newline="\n").write(
                t[:m.start()] + m.group(1) + nuevo_valor + m.group(3) +
                t[m.end():])

print("Historias que ya estaban bien: %d" % iguales)
print("Historias %s: %d" % ("cambiadas" if aplicar else "por cambiar",
                            len(cambios)))
print("Sin mapa: %d" % len(sin_mapa))
for r, v in sin_mapa:
    print("   %-56s %s" % (r[-56:], v[:40]))
print()
print("Muestra de los cambios:")
for r, v, n in cambios[:6]:
    print("   %-40s" % os.path.basename(r)[:40])
    print("      antes:   %s" % v[:74])
    print("      despues: %s" % n[:74])
if not aplicar:
    print()
    print("(esto fue solo mirar. Con --aplicar se escribe)")
