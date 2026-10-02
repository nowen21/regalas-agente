# -*- coding: utf-8 -*-
"""Suma al análisis 8 lo acordado en los turnos 158 a 162."""
import os

RUTA = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")),
                    "documentacion", "epicas", "EP-023-lo-que-se-construye-es-lo-que-se-analizo",
                    "103-cada-documento-de-la-cadena-sale-del-anterior", "analisis-8.md")
H1 = ("../HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes/"
      "HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md")
H36 = ("../../EP-001-cuerpo-de-reglas-heredable/HU-036-el-pedido-dice-que-se-espera/"
       "HU-036-el-pedido-dice-que-se-espera.md")

CAMBIOS = [
    ("| Respuesta que entra tarde al análisis |",
     "| Análisis aprobado que no suma su línea al análisis principal | Cualquier proyecto con análisis | Nadie sabe por qué cambió lo que se construye | El validador avisa |\n"
     "| Respuesta corta del usuario a una pregunta del agente | Cualquier herramienta con palabras clave | El agente no avanza o malinterpreta | El programa reconoce la cita de una regla, la opción elegida y el «sí» |\n"
     "| Respuesta del agente más larga de lo que pide `00·ID9` | Cualquier agente | El usuario tiene que pedir que la acorte, una y otra vez | Recomendación: medirla antes de entregarla |\n"
     "| Respuesta que entra tarde al análisis |"),
    ("\nSiguen abiertas: ninguna.",
     "| 11 | El análisis principal al día | Los análisis 6, 7 y 8 suman su línea a la lista de cambios del análisis principal (`13·DOC25`), y el validador avisa cuando un análisis aprobado cambia una HU y no aparece en esa lista | Turnos 158 y 159 |\n"
     "| 12 | Las respuestas cortas | Un mensaje que es solo el número de una regla quiere decir «aplique esa regla a lo que acaba de responder», no «explíquela». Si el último mensaje del agente terminó en una pregunta, la opción que elige el usuario o su «sí» quedan como su decisión. Escribir o cambiar archivos sigue pidiendo su palabra (`01·C28`) | Turnos 159, 160 y 161 |\n"
     "| 13 | El largo de la respuesta | Medir la respuesta contra `00·ID9` antes de entregarla queda como recomendación de arranque | Turnos 159 y 161 |\n"
     "| 14 | Revisar lo que se tiene que hacer | No nace nada nuevo: para eso existe «Lo que aportó cada parte». Lo que falló en el H-5 y el H-7 fue hacer esas partes por encima, sin revisarlas contra cada punto de «Lo que se tiene que hacer»; queda como lección | Turnos 159 y 160 |\n"
     "| 15 | La corrección del H-9 | Cambió `validadores/instalar.py`, que viaja a los proyectos: entra con su línea en el CHANGELOG y su versión (`20·M10`) en el commit que la sube | Turnos 160 y 161 |\n"
     "\nSiguen abiertas: ninguna."),
    ("| 3 | Corregir en el piloto lo que falla del propio enganche evita que falle en los análisis siguientes | Funcionó | Por escribir |",
     "| 3 | Corregir en el piloto lo que falla del propio enganche evita que falle en los análisis siguientes | Funcionó | Por escribir |\n"
     "| 4 | Las cuatro partes de «Lo que aportó cada parte» se hicieron por encima en los análisis 1 a 5, sin revisarlas contra cada punto de «Lo que se tiene que hacer», y por eso salieron el H-5 y el H-7 al escribir los planes | Falló | Por escribir |\n"
     "| 5 | El usuario tuvo que pedir «00 id9» muchas veces en la misma sesión: el largo se medía después de entregar | Falló | Por escribir |"),
    ("| 6 | Sumar a la HU-006 el criterio",
     "| 7 | Sumar las líneas de los análisis 6, 7 y 8 a la lista de cambios del análisis principal, y el criterio de que el validador avise cuando falte la de un análisis aprobado | 11 | EP-023, [HU-001](" + H1 + "), fase D |\n"
     "| 8 | Que el programa reconozca las respuestas cortas: la cita de una regla, la opción elegida y el «sí» después de una pregunta del agente | 12 | EP-001, [HU-036](" + H36 + "), dueña de `01·C28` |\n"
     "| 9 | Sumar a las recomendaciones de arranque medir la respuesta contra `00·ID9` antes de entregarla | 13 | EP-023, [HU-001](" + H1 + "), fase D |\n"
     "| 10 | Subir la corrección del H-9 con su línea en el CHANGELOG y su versión | 15 | Este análisis, en el commit que la sube |\n"
     "| 6 | Sumar a la HU-006 el criterio"),
]


def main():
    with open(RUTA, encoding="utf-8") as f:
        texto = f.read()
    for viejo, nuevo in CAMBIOS:
        assert texto.count(viejo) == 1, viejo[:60]
        texto = texto.replace(viejo, nuevo)
    # Las filas nuevas de «Lo que se tiene que hacer» van en orden, después de la 6.
    i = texto.index("## Lo que se tiene que hacer")
    cuerpo = texto[i:]
    filas = [l for l in cuerpo.split("\n") if l.startswith("| ") and l[2:3].isdigit()]
    ordenadas = sorted(filas, key=lambda l: int(l.split("|")[1]))
    for vieja, nueva in zip(filas, ordenadas):
        cuerpo = cuerpo.replace(vieja, "\0" + str(filas.index(vieja)), 1)
    for k, nueva in enumerate(ordenadas):
        cuerpo = cuerpo.replace("\0" + str(k), nueva, 1)
    with open(RUTA, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto[:i] + cuerpo)


if __name__ == "__main__":
    main()
