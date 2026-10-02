# -*- coding: utf-8 -*-
"""Saca del análisis 8 lo de las respuestas cortas, que es otro hallazgo (H-10), y renumera."""
import os
import re

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
RUTA = os.path.join(RAIZ, "documentacion", "epicas", "EP-023-lo-que-se-construye-es-lo-que-se-analizo",
                    "103-cada-documento-de-la-cadena-sale-del-anterior", "analisis-8.md")


def quitar_fila(texto, empieza):
    lineas = texto.split("\n")
    quedan = [l for l in lineas if not l.startswith(empieza)]
    assert len(lineas) - len(quedan) == 1, empieza
    return "\n".join(quedan)


def main():
    with open(RUTA, encoding="utf-8") as f:
        texto = f.read()
    texto = quitar_fila(texto, "| Respuesta corta del usuario a una pregunta del agente |")
    texto = quitar_fila(texto, "| 12 | Las respuestas cortas |")
    texto = quitar_fila(texto, "| 8 | Que el programa reconozca las respuestas cortas")
    # Conclusiones 13 a 15 pasan a 12 a 14.
    for viejo, nuevo in ((13, 12), (14, 13), (15, 14)):
        texto = texto.replace("\n| %d | " % viejo, "\n| %d | " % nuevo, 1)
    # Puntos 9 y 10 de «Lo que se tiene que hacer» pasan a 8 y 9, con sus conclusiones al día.
    i = texto.index("## Lo que se tiene que hacer")
    cuerpo = texto[i:]
    cuerpo = cuerpo.replace("\n| 9 | Sumar a las recomendaciones de arranque", "\n| 8 | Sumar a las recomendaciones de arranque", 1)
    cuerpo = cuerpo.replace("antes de entregarla | 13 |", "antes de entregarla | 12 |", 1)
    cuerpo = cuerpo.replace("\n| 10 | Subir la corrección del H-9", "\n| 9 | Subir la corrección del H-9", 1)
    cuerpo = cuerpo.replace("su versión | 15 |", "su versión | 14 |", 1)
    texto = texto[:i] + cuerpo
    assert "respuestas cortas" not in texto.split("## Lo que aportó cada parte")[1]
    with open(RUTA, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


if __name__ == "__main__":
    main()
