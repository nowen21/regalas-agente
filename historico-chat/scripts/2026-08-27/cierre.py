# -*- coding: utf-8 -*-
import io

f = r"c:\Ing. Jose\ia\agente\historico-chat\resumenes\2026-08-22\sesion-6.md"
t = io.open(f, encoding="utf-8").read()

marca = u"## \u00bfSe puede cerrar la sesi\u00f3n?"
i = t.index(marca)

nuevo = u"""## \u00bfSe puede cerrar la sesi\u00f3n?

Se cierra cuando **ning\u00fan hallazgo queda a medias**. Un hallazgo est\u00e1 terminado de una de dos formas, y las dos valen igual:

- **Resuelto ac\u00e1**, con lo que se hizo escrito en el campo de d\u00f3nde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "qued\u00f3 pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisi\u00f3n escrita | \u2611 |
| Todo hallazgo abierto tiene su pendiente creado | \u2610 \u00b7 **falta el de `H-40`** |
| Toda historia disparada est\u00e1 escrita en su \u00e9pica | \u2611 |
| Lo que se hizo est\u00e1 aprobado y guardado | \u2610 \u00b7 falta el commit de la fase `B` de la `HU-021` |

**Cuarenta y tres hallazgos, cuarenta y dos cerrados.**

**`H-40` es el que queda abierto**, y es el que m\u00e1s vale de la sesi\u00f3n: **el andamio crea los cinco documentos vac\u00edos, y con eso una fase reci\u00e9n abierta ya cuenta como terminada.** No se resolvi\u00f3 \u2014 se escribieron los cuatro cierres que estaban en blanco, que es tapar los casos, no la causa. **Cobr\u00f3 tres veces el mismo d\u00eda**: en las cuatro fases que figuraban cerradas siendo moldes, en la `HU-021` que contaba como terminada sin una l\u00ednea escrita, y en la fase `B` que se cre\u00f3 para arreglar el conteo y le agreg\u00f3 un caso al conteo.

**La medida que lo destapa ya existe y funciona:** contar los marcadores del molde sin reemplazar. Treinta y uno es un formulario; cinco son comillas de prosa. **Ese es el pendiente que falta escribir.**

**El hilo de la sesi\u00f3n, si hay que decirlo en una l\u00ednea:** el n\u00famero que responde \u00abcu\u00e1nto falta\u00bb minti\u00f3 de tres formas distintas en dos d\u00edas \u2014 copiado a mano, contando archivos presentes, y contando fases cerradas sin mirar su veredicto. **Cada arreglo lo dej\u00f3 m\u00e1s honesto y sigui\u00f3 midiendo la cosa de al lado.** Hoy dice `117 en total \u00b7 32 sin terminar \u00b7 85 terminadas, de las cuales 57 cumplen, 13 no cumplen y 15 no dicen si cumplen`.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripci\u00f3n para encontrarla.
"""

io.open(f, "w", encoding="utf-8", newline="\n").write(t[:i] + nuevo)
print("cierre reescrito")
