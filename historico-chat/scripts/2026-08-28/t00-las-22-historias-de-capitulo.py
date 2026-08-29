# -*- coding: utf-8 -*-
"""Las 22 historias de EP-001 que son «un capitulo de base/ cada una».

Cada una pide dos cosas:
  CA-01 · el capitulo nombra su historia duena, en su cabecera y enlazada.
  CA-02 · un cambio del capitulo tiene donde bajarse (la historia existe).

Antes de escribir 22 fases hay que saber en que estado estan las 22. Si el
CA-01 ya se cumple en todas, la fase de cada una es una comprobacion escrita,
no una construccion; si falla en algunas, esas son trabajo de verdad.

**Se corre, no se cita** ---la leccion de la HU-021: una medicion vieja no es
una medicion.
"""
import io
import os
import re

RAIZ = r"c:\Ing. Jose\ia\agente"
EPICA = os.path.join(RAIZ, "documentacion", "epicas",
                     "EP-001-cuerpo-de-reglas-heredable")

# El nombre de la carpeta dice que capitulo le toca: HU-0NN-el-capitulo-NN-...
DE_CAPITULO = re.compile(r"^HU-\d+-el-capitulo-(\d+)-")


def capitulo_de(numero):
    """La ruta del capitulo NN: puede ser archivo suelto o carpeta con base.md."""
    base = os.path.join(RAIZ, "base")
    for n in sorted(os.listdir(base)):
        if not n.startswith(numero + "-"):
            continue
        ruta = os.path.join(base, n)
        if os.path.isdir(ruta):
            interno = os.path.join(ruta, "base.md")
            return interno if os.path.isfile(interno) else None
        if n.endswith(".md"):
            return ruta
    return None


historias = sorted(n for n in os.listdir(EPICA) if DE_CAPITULO.match(n))
# HU-013 no sigue el patron del nombre pero es del mismo grupo: se mira aparte.
otras = ["HU-013-capitulos-opt-in-de-dominio"]

print("%-62s %-9s %s" % ("HISTORIA", "CAPITULO", "CA-01: la cabecera la nombra"))
cumplen = fallan = sin_capitulo = 0
for h in historias:
    numero = DE_CAPITULO.match(h).group(1)
    cap = capitulo_de(numero)
    if cap is None:
        print("%-62s %-9s NO SE ENCUENTRA EL CAPITULO" % (h[:60], numero))
        sin_capitulo += 1
        continue
    cabecera = io.open(cap, encoding="utf-8").read()[:1500]
    nombrada = h.split("-el-capitulo-")[0] in cabecera or h in cabecera
    print("%-62s %-9s %s" % (h[:60], numero, "si" if nombrada else "NO"))
    if nombrada:
        cumplen += 1
    else:
        fallan += 1

print("")
for h in otras:
    existe = os.path.isdir(os.path.join(EPICA, h))
    print("%-62s %s" % (h[:60], "existe, se mira aparte" if existe else "no esta"))

print("")
print("De %d historias de capitulo: %d con el CA-01 cumplido, %d sin cumplir, "
      "%d sin capitulo." % (len(historias), cumplen, fallan, sin_capitulo))
print("")
print("Si el CA-01 ya se cumple, la fase de cada historia es una comprobacion")
print("escrita ---retrodocumentacion, `13.DOC6`--- y no una construccion.")
