# -*- coding: utf-8 -*-
"""Análisis 10 del pendiente 103: el título, las recomendaciones, el hallazgo y el pendiente."""
import glob
import io
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
P = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "pendientes", "103-*"))[0]
A = os.path.join(P, "analisis-10.md")

RECOMENDACIONES = """| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-1 | Se busca en qué otros documentos de la cadena puede pasar lo mismo, no solo en el plan |
| R-2 | Se revisa qué existe hoy para que el plan lea el análisis: la R-6 y el ORIGEN del plan |
| R-5 | Se revisan las cuatro partes contra cada punto de «Lo que se tiene que hacer» |
| R-6 | Se leen completos los análisis 1 a 9 antes de proponer |
| R-7 | Lo que nadie pidió se pregunta acá, no se agrega al plan |
| R-14 | Se confirma con el usuario que el hallazgo que abre este análisis es el H-13 |
| R-15 | No aplica: el hallazgo salió al escribir los planes, y esas fases ya cerraron |
| R-17 | Cada respuesta se mide contra `00·ID9` antes de entregarla |
| R-3, R-4, R-8 a R-13, R-16 | No aplican mientras el análisis no cree ni cambie reglas o plantillas; se revisan si eso cambia |"""

HALLAZGO = """### H-13 · Los planes se escriben sin leer lo que el análisis decidió

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-02, al escribir los planes de las HU-003 y HU-004, el agente trabajó con los criterios de la HU y no leyó las conclusiones del análisis de las que salen. Preguntó tres veces lo que el análisis ya había decidido: dónde vive el 103, dónde va el índice de pendientes, y si se ajustan el anexo de fases y la frase «el plan aprobado no se modifica» (análisis 1 del pendiente 103, conclusiones 24, 33 y 41 y punto 18). Además, en el análisis 8 había agregado un traslado que ninguna conclusión decía. |
| Por qué importa | El análisis es lo que el usuario ya decidió. Un plan que no lo lee vuelve a abrir decisiones cerradas, gasta la atención del usuario y mete lo que nadie pidió. La recomendación R-6 ya lo pedía, y no bastó con que estuviera escrita: nada comprueba que el plan la siguió. |"""

PENDIENTE = """### Pendiente. Lo que se construye se aparta de lo aprobado

Reúne los pendientes 103, 104 y 105. Versión 3, del [análisis 2](analisis-2.md).

| Campo | Valor |
|---|---|
| De dónde sale | [H-13 de la sesión del 2026-09-28](../../../../../historico-chat/resumenes/2026-09-28/sesion.md), que reúne H-10, H-11 y H-13, y [H-2 de la sesión del 2026-09-30](../../../../../historico-chat/resumenes/2026-09-30/sesion.md) |
| El problema | No hay un documento que fije el alcance antes de la HU. Nada obliga a que cada documento salga del anterior. Nada detiene al agente cuando trabaja fuera del plan aprobado. La plantilla del plan no permite comprobarlo con un programa. Y lo que pasa la conversación al análisis hay que configurarlo a mano para cada análisis. |
| Por qué importa | Al ejecutar el plan aparecen hallazgos que se podían evitar, y cada uno se vuelve un pendiente más. |"""


def cambiar(t, a, b):
    assert t.count(a) == 1, a[:60]
    return t.replace(a, b)


def main():
    t = io.open(A, encoding="utf-8").read()
    t = cambiar(t, "# Análisis 10: «el problema que trata el análisis, en una frase»",
                "# Análisis 10: los planes se escriben sin leer lo que el análisis decidió")
    i = t.index("> Plantilla del análisis.")
    j = t.index("> Este análisis se redacta aplicando estas reglas.")
    t = t[:i] + t[j:]
    t = t.replace("«RUTA-ESTANDAR»/", "../../../../../")
    a = t.index("> Un análisis aprobado no se reescribe.")
    b = t.index("\n", a)
    t = t[:a] + "> Viene del [análisis 9](analisis-9.md), aprobado el 2026-10-02. Trata solo lo que falló y sus implicaciones sobre lo ya hecho (conclusión 19 del análisis 1)." + t[b:]
    a = t.index("> Antes de analizar se leen")
    b = t.index("| «R-n o RP-n» | «qué se hizo por ella, o por qué no aplica» |") + len("| «R-n o RP-n» | «qué se hizo por ella, o por qué no aplica» |")
    t = t[:a] + RECOMENDACIONES + t[b:]
    a = t.index("> Copia del hallazgo que origina")
    b = t.index("«copia del hallazgo»") + len("«copia del hallazgo»")
    t = t[:a] + HALLAZGO + t[b:]
    a = t.index("> Copia del pendiente, tal como")
    b = t.index("«copia del pendiente»") + len("«copia del pendiente»")
    t = t[:a] + PENDIENTE + t[b:]
    io.open(A, "w", encoding="utf-8", newline="\n").write(t)


if __name__ == "__main__":
    main()
