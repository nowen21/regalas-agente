# -*- coding: utf-8 -*-
"""Cuantas historias arrastran un rojo que una fase posterior podria reemplazar.

Es la linea base de la HU que hace que el conteo sepa leer una correccion.
Se mide ANTES de crear su carpeta, porque abrirla mueve el numero.

**No decide nada**: solo dice cuantas hay y cuales, para que el plan se escriba
sobre datos y no sobre una intuicion.
"""
import os
import sys

RAIZ = r"c:\Ing. Jose\ia\agente"
sys.path.insert(0, os.path.join(RAIZ, "validadores"))
import fases as F

raiz = os.path.join(RAIZ, *F.CARPETA.split("/"))
de_cada_uno = F.marcadores_de_los_moldes(RAIZ)

con_rojo = []
for ep in F._subcarpetas(raiz):
    if not F._EPICA.match(ep):
        continue
    rep = os.path.join(raiz, ep)
    for hu in F._subcarpetas(rep):
        if not F._HU.match(hu):
            continue
        rhu = os.path.join(rep, hu)
        fs = [n for n in F._subcarpetas(rhu) if F._FASE.match(n)]
        if not F._historia_terminada(rhu, de_cada_uno):
            continue
        dichos = [(f, F.veredicto_de(os.path.join(rhu, f))) for f in sorted(fs)]
        rojas = [f for f, v in dichos if v == "No cumple"]
        if not rojas:
            continue
        # Hay fase posterior a la ultima roja?
        orden = [f for f, _ in dichos]
        ultima_roja = max(orden.index(f) for f in rojas)
        posteriores = orden[ultima_roja + 1:]
        con_rojo.append((ep, hu, rojas, posteriores,
                         [v for f, v in dichos if f in posteriores]))

print("HISTORIAS TERMINADAS CON ALGUNA FASE EN ROJO: %d" % len(con_rojo))
print()
con = [x for x in con_rojo if x[3]]
sin = [x for x in con_rojo if not x[3]]
print("  con una fase POSTERIOR a la ultima roja: %d" % len(con))
print("  sin ninguna fase posterior:              %d" % len(sin))
print()
print("LAS QUE TIENEN FASE POSTERIOR (candidatas a declarar el reemplazo):")
for ep, hu, rojas, post, veredictos in sorted(con):
    print("  %s" % hu)
    for r in rojas:
        print("      roja:      %s" % r)
    for p, v in zip(post, veredictos):
        print("      posterior: %-62s %s" % (p, v))
print()
print("LAS QUE NO TIENEN NINGUNA FASE DESPUES (el rojo sigue vivo de verdad):")
for ep, hu, rojas, _, _ in sorted(sin):
    print("  %-56s (%d roja/s)" % (hu, len(rojas)))
