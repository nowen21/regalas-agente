# -*- coding: utf-8 -*-
"""Suma al análisis 8 lo acordado sobre las recomendaciones (turnos 156 y 157)."""
import os

RUTA = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")),
                    "documentacion", "epicas", "EP-023-lo-que-se-construye-es-lo-que-se-analizo",
                    "103-cada-documento-de-la-cadena-sale-del-anterior", "analisis-8.md")
H1 = ("../HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes/"
      "HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md")
H6 = "../HU-006-lo-aprendido-incluye-las-lecciones/HU-006-lo-aprendido-incluye-las-lecciones.md"

CAMBIOS = [
    ("| Respuesta que entra tarde al análisis |",
     "| Recomendación repetida o sin origen | Cualquier proyecto que acumule análisis | Dos recomendaciones dicen distinto lo mismo, o nadie sabe de dónde salió una | El validador busca repetidas y exige el análisis de origen |\n"
     "| Respuesta que entra tarde al análisis |"),
    ("\nSiguen abiertas: ninguna.",
     "| 9 | Las recomendaciones del análisis | Viven en un solo archivo, `plantillas/recomendaciones-del-analisis.md`, y la plantilla abre con una sección que lo enlaza y dice cuáles aplican. Hay dos niveles: las de Cimiento, que viajan con el estándar y llevan versión, y las de cada proyecto, en su archivo; la del proyecto que sirva a todos sube a Cimiento. Cada una dice qué se hace, por qué y de qué análisis sale. Antes de crear una se busca si ya existe (`20·M12`). Si se vuelve exigible, sube a regla. El validador revisa el origen, que no haya repetidas y que cada análisis aprobado diga cuáles consultó. Arranca con las que dejaron las lecciones de los análisis 1 a 8, y el recuerdo «El análisis cubre todos los casos» pasa a ser la R-1 | Turnos 156 y 157 |\n"
     "| 10 | Cómo se alimentan | De las lecciones de cada análisis: su tabla suma una columna que dice si la lección complementa una recomendación, crea una nueva o no aplica. Es de la HU-006, que trata de las lecciones, y por eso la HU-006 depende de la fase D de la HU-001 | Turnos 156 y 157 |\n"
     "\nSiguen abiertas: ninguna."),
    ("| 3 | HU-006 | HU-001 | No depende de las demás; cada análisis suma lecciones que hoy no tienen dónde quedar |",
     "| 3 | HU-006 | HU-001, fase D | Las lecciones alimentan las recomendaciones que crea la fase D; cada análisis suma lecciones que hoy no tienen dónde quedar |"),
    ("| 4 | Reescribir la hoja de ruta de EP-023 con el orden de este análisis | 8 | EP-023, [épica](../epica.md) |",
     "| 4 | Reescribir la hoja de ruta de EP-023 con el orden de este análisis | 8, 10 | EP-023, [épica](../epica.md) |\n"
     "| 5 | Sumar a la HU-001 el criterio de las recomendaciones: el archivo con su forma y sus dos niveles, la sección que lo enlaza al inicio de la plantilla, el validador, y las recomendaciones de arranque | 9 | EP-023, [HU-001](" + H1 + "), fase D |\n"
     "| 6 | Sumar a la HU-006 el criterio de alimentar las recomendaciones desde las lecciones, con la columna nueva en su tabla | 10 | EP-023, [HU-006](" + H6 + ") |"),
]


def main():
    with open(RUTA, encoding="utf-8") as f:
        texto = f.read()
    for viejo, nuevo in CAMBIOS:
        assert texto.count(viejo) == 1, viejo[:60]
        texto = texto.replace(viejo, nuevo)
    with open(RUTA, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


if __name__ == "__main__":
    main()
