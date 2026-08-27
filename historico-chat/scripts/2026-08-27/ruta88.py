# -*- coding: utf-8 -*-
import io

f = r"c:\Ing. Jose\ia\agente\pendientes\README.md"
t = io.open(f, encoding="utf-8").read()

viejo = (u"**El [87](87-la-estacion-del-commit-casi-nunca-se-marca.md) tampoco, "
         u"y por otra raz\u00f3n:** es del est\u00e1ndar, y su historia depende de cu\u00e1l "
         u"de las tres salidas se elija. Escribirla antes de esa decisi\u00f3n ser\u00eda "
         u"fijar el c\u00f3mo antes del qu\u00e9.")
assert viejo in t

nuevo = viejo + (
    u"\n\n**El [88](88-el-andamio-crea-una-fase-que-ya-cuenta-como-terminada.md), "
    u"por la misma raz\u00f3n que el 87:** tiene tres salidas y dos de ellas no se "
    u"estorban, pero la tercera cambia c\u00f3mo se abre una fase. La historia se "
    u"escribe cuando el usuario decida cu\u00e1les entran.")

io.open(f, "w", encoding="utf-8", newline="\n").write(t.replace(viejo, nuevo, 1))
print("ruta anotada")
