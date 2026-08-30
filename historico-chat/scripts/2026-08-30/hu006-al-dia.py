# -*- coding: utf-8 -*-
import io

R = (r"c:\Ing. Jose\ia\agente\documentacion\epicas"
     r"\EP-001-cuerpo-de-reglas-heredable\HU-006-capa-propia-del-proyecto"
     r"\HU-006-capa-propia-del-proyecto.md")
F = "B-EP-001-HU-006-el-ajuste-que-afloja-el-nucleo-se-reprueba"

with io.open(R, encoding="utf-8") as f:
    t = f.read()

viejo = u"| **Estado** | Pendiente |"
nuevo = (u"| **Estado** | Terminada \u2014 el CA-03 se provoc\u00f3 por primera vez "
         u"en la fase `B`, fall\u00f3, y la comprobaci\u00f3n que faltaba qued\u00f3 "
         u"construida |")
if viejo in t:
    t = t.replace(viejo, nuevo, 1)
    print("estado al dia")

sep = u"| Fase | Qu\u00e9 CA cubre | Estado |\n|---|---|---|\n"
fila = (u"| [%s](%s/estado-fase.md) | CA-03 | **Ejecutada el 2026-08-30.** "
        u"Veredicto: [**Cumple**](%s/resultado_pruebas.md#2-veredicto-de-la-fase) "
        u"\u2014 el ajuste que declara aflojar una `[BLINDADA]` ahora se reprueba, "
        u"y el que la endurece sigue pasando. Declara reemplazar el veredicto de "
        u"la fase `A` |\n" % (F, F, F))
if sep in t:
    t = t.replace(sep, sep + fila, 1)
    print("fila puesta")

with io.open(R, "w", encoding="utf-8", newline="\n") as f:
    f.write(t)
