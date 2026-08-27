# -*- coding: utf-8 -*-
import io

f = r"c:\Ing. Jose\ia\agente\historico-chat\resumenes\2026-08-22\sesion-6.md"
t = io.open(f, encoding="utf-8").read()

pares = [
    (u"| Todo hallazgo abierto tiene su pendiente creado | \u2610 \u00b7 **falta el de `H-40`** |",
     u"| Todo hallazgo abierto tiene su pendiente creado | \u2611 \u00b7 el [88](../../../pendientes/88-el-andamio-crea-una-fase-que-ya-cuenta-como-terminada.md) |"),
    (u"**La medida que lo destapa ya existe y funciona:** contar los marcadores del molde sin reemplazar. Treinta y uno es un formulario; cinco son comillas de prosa. **Ese es el pendiente que falta escribir.**",
     u"**La medida que lo destapa ya existe y funciona:** contar los marcadores del molde sin reemplazar. Treinta y uno es un formulario; cinco son comillas de prosa. Qued\u00f3 anotado en el [pendiente 88](../../../pendientes/88-el-andamio-crea-una-fase-que-ya-cuenta-como-terminada.md), con las tres salidas y sin elegir por el usuario cu\u00e1l entra."),
]

for viejo, nuevo in pares:
    assert viejo in t, viejo[:60]
    t = t.replace(viejo, nuevo, 1)

io.open(f, "w", encoding="utf-8", newline="\n").write(t)
print("cierre al dia")
