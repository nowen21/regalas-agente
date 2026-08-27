# -*- coding: utf-8 -*-
import io

f = r"c:\Ing. Jose\ia\agente\pendientes\README.md"
t = io.open(f, encoding="utf-8").read()

marca = u"### Sin agrupar todav\u00eda"
assert marca in t

seccion = u"""### Lo que dej\u00f3 hacer honesto el n\u00famero que dice cu\u00e1nto falta (88)

| # | P | Pendiente | Qu\u00e9 resuelve |
|---|---|---|---|
| 88 | **P1** | [El andamio crea una fase que ya cuenta como terminada](88-el-andamio-crea-una-fase-que-ya-cuenta-como-terminada.md) | El inventario cuenta una fase terminada cuando **existen** sus cinco documentos, y el andamio los crea vac\u00edos de entrada: una fase reci\u00e9n abierta ya cuenta como hecha. Cobr\u00f3 tres veces el 2026-08-27, la \u00faltima moviendo la base de una medici\u00f3n en curso. La medida que lo destapa ya se prob\u00f3 \u2014 contar los marcadores del molde sin reemplazar \u2014 y separa sin falsos positivos. Falta decidir d\u00f3nde entra. Sale de `S-053`. |

---

"""

t = t.replace(marca, seccion + marca, 1)
io.open(f, "w", encoding="utf-8", newline="\n").write(t)
print("indice actualizado")
