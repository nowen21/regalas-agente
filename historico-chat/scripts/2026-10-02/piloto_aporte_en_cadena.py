# -*- coding: utf-8 -*-
"""Análisis 9, turnos 222 a 225: la sección «Lo que aporta al análisis principal» lleva el resultado,
la redacción propia del análisis y la nueva redacción del análisis principal que el agente propone con
lo que el análisis aporta. Se rehace en cadena: cada análisis parte de la redacción que dejó el anterior.
"""
import glob
import os
import re

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
CARPETA = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "103-*"))[0]
VIEJO = os.path.join(RAIZ, "analisis", "base-2026-08-07-cumplimiento-meta-reglas.md")
NOTA = "> Se agregó en el piloto, por el [análisis 9](%s), a partir de las conclusiones de este análisis; no decide nada nuevo."

INICIO = ("Cimiento es el estándar que hace que una IA que programa trabaje siempre igual en cualquier "
          "proyecto: con las mismas reglas, la misma memoria y comprobaciones que no dependen de que alguien se acuerde.")

# (archivo, resultado, redacción propia, lo que suma a la redacción del principal), en el orden en que se aprobaron.
CADENA = [
    (VIEJO, "Aclara",
     "Se aclara cómo estaba el cuerpo de reglas frente a sus meta-reglas: la norma estaba bien definida y se cumplía a medias.",
     " Sus reglas se escriben con el molde que fijan sus propias meta-reglas."),
    (1, "Cambia lo que se construye y modifica la idea",
     "Se requiere que lo que se construye salga de lo que se analizó: antes de repartir el trabajo hay un análisis, cada documento sale del anterior, un hallazgo detiene la ejecución y nada se escribe fuera del plan aprobado.",
     " Lo que construye sale de lo que se analizó: antes de repartir el trabajo hay un análisis, cada documento sale del anterior, un hallazgo detiene la ejecución y nada se escribe fuera del plan aprobado."),
    (2, "Cambia lo que se construye",
     "Se requiere que la conversación del análisis pase sola a su archivo, y que el análisis se prenda, se pause y se apruebe con tres palabras, con uno solo abierto a la vez.",
     " La conversación del análisis pasa sola a su archivo, y el análisis se prende, se pausa y se aprueba con tres palabras, con uno solo abierto a la vez."),
    (3, "Aclara",
     "Se aclara que de un análisis pasan a trabajo su propuesta final y lo que se tiene que hacer, y que la conversación es el contexto.",
     " De un análisis pasan a trabajo su propuesta final y lo que se tiene que hacer; la conversación es el contexto."),
    (4, "Aclara",
     "Se aclara que el contexto de una HU que sale de una épica es la parte del problema que le toca.",
     " El contexto de cada HU que sale de una épica es la parte del problema que le toca."),
    (5, "Modifica la idea",
     "Se requiere que el análisis individual cierre en su mismo archivo y no se reescriba, y que el análisis principal se reescriba con lo que aportan los individuales.",
     " El análisis individual cierra en su mismo archivo y no se reescribe; el principal se reescribe con lo que aportan los individuales."),
    (6, "Modifica la idea",
     "Se define que lo pedido es el criterio de aceptación más lo que exigen las reglas, y que lo que nadie pidió no se agrega: se pregunta en el análisis.",
     " Lo pedido es el criterio de aceptación más lo que exigen las reglas; lo que nadie pidió no se agrega, se pregunta en el análisis."),
    (7, "Cambia lo que se construye",
     "Se requiere que cada criterio de la HU diga, desde su plantilla, de qué punto del análisis sale.",
     " Cada criterio de la HU dice, desde su plantilla, de qué punto del análisis sale."),
    (8, "Cambia lo que se construye y amplía la idea",
     "Se requiere que las reglas se hagan cumplir por cualquier canal y en cualquier herramienta, que el análisis considere todos los casos, ordene las HU por su dependencia y consulte las recomendaciones, y que cada pendiente viva dentro de lo que lo origina.",
     " Las reglas se hacen cumplir por cualquier canal y en cualquier herramienta; el análisis considera todos los casos que pueden pasar en cualquier proyecto, ordena las HU por su dependencia y consulta las recomendaciones; y cada pendiente vive dentro de lo que lo origina."),
    (9, "Modifica la idea",
     "Se define que todo análisis termina en una decisión y se anota en el principal aunque no cambie el sistema, porque también confirma, aclara, amplía o modifica la idea; su aporte pasa tal cual.",
     " Todo análisis termina en una decisión y se anota en el principal aunque no cambie el sistema, porque también confirma, aclara, amplía o modifica la idea. Cada cosa se escribe una sola vez."),
]


def ruta_de(clave):
    return clave if isinstance(clave, str) else os.path.join(CARPETA, "analisis-%d.md" % clave)


def seccion(ruta, resultado, propia, principal, piloto):
    a9 = os.path.relpath(os.path.join(CARPETA, "analisis-9.md"), os.path.dirname(ruta)).replace(os.sep, "/")
    nota = (NOTA % a9 + "\n\n") if piloto else ""
    return ("## Lo que aporta al análisis principal\n\n" + nota
            + "**Resultado:** %s.\n\n**Lo que aporta este análisis:** %s\n\n"
            "**El análisis principal pasa a decir:**\n\n> %s\n" % (resultado.lower().capitalize(), propia, principal))


def main():
    redaccion = INICIO
    for clave, resultado, propia, suma in CADENA:
        redaccion = redaccion + suma
        ruta = ruta_de(clave)
        with open(ruta, encoding="utf-8") as f:
            t = f.read()
        i = t.index("## Lo que aporta al análisis principal")
        t = t[:i] + seccion(ruta, resultado, propia, redaccion, clave != 9)
        with open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(t)


if __name__ == "__main__":
    main()
