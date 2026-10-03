# -*- coding: utf-8 -*-
"""Análisis 11 del pendiente 103: el título, las recomendaciones, el hallazgo H-14 y el pendiente."""
import glob
import io
import os
import re

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
P = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "pendientes", "103-*"))[0]
A = os.path.join(P, "analisis-11.md")
RESUMEN = os.path.join(RAIZ, "historico-chat", "resumenes", "2026-10-01", "sesion.md")

RECOMENDACIONES = """| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-1 | Se buscan todos los casos en que una regla entra o sale, no solo el de la prueba que falló |
| R-2 | Se revisa lo que ya existe: la línea «Autoriza escribir» en cada regla y la marca de derogada en su título |
| R-6 | Se leen los acuerdos que llegan con cada mensaje y los análisis 1, 8 y 10 antes de proponer |
| R-7 | Lo que nadie pidió se pregunta acá, no se agrega al plan |
| R-14 | Se confirma con el usuario que el hallazgo que abre este análisis es el H-14 |
| R-15 | Se aplicó: la ejecución se detuvo al aparecer el hallazgo, antes de tocar otro archivo |
| R-17 | Cada respuesta se mide contra `00·ID9` antes de entregarla |
| R-3, R-4, R-5, R-8 a R-13, R-16 | No aplican mientras el análisis no cree ni cambie reglas o plantillas; se revisan si eso cambia |"""

PENDIENTE = """### Pendiente. Lo que se construye se aparta de lo aprobado

Reúne los pendientes 103, 104 y 105. Versión 3, del [análisis 2](analisis-2.md).

| Campo | Valor |
|---|---|
| De dónde sale | [H-13 de la sesión del 2026-09-28](../../../../../historico-chat/resumenes/2026-09-28/sesion.md), que reúne H-10, H-11 y H-13, y [H-2 de la sesión del 2026-09-30](../../../../../historico-chat/resumenes/2026-09-30/sesion.md) |
| El problema | No hay un documento que fije el alcance antes de la HU. Nada obliga a que cada documento salga del anterior. Nada detiene al agente cuando trabaja fuera del plan aprobado. La plantilla del plan no permite comprobarlo con un programa. Y lo que pasa la conversación al análisis hay que configurarlo a mano para cada análisis. |
| Por qué importa | Al ejecutar el plan aparecen hallazgos que se podían evitar, y cada uno se vuelve un pendiente más. |"""


def cambiar(t, a, b):
    assert t.count(a) == 1, a[:80]
    return t.replace(a, b)


def hallazgo():
    """El H-14 tal como está en el resumen, sin su fila «Pendiente»."""
    t = io.open(RESUMEN, encoding="utf-8").read()
    m = re.search(r"^### H-14 · .*?(?=^\| Pendiente)", t, re.M | re.S)
    assert m
    return m.group(0).rstrip("\n")


def main():
    t = io.open(A, encoding="utf-8").read()
    t = cambiar(t, "# Análisis 11: «el problema que trata el análisis, en una frase»",
                "# Análisis 11: la prueba de la fase A fija cuántas reglas autorizan escribir")
    i = t.index("> Plantilla del análisis.")
    j = t.index("> Este análisis se redacta aplicando estas reglas.")
    t = t[:i] + t[j:]
    t = t.replace("«RUTA-ESTANDAR»/", "../../../../../")
    a = t.index("> Un análisis aprobado no se reescribe.")
    b = t.index("\n", a)
    t = t[:a] + ("> Viene del [análisis 10](analisis-10.md), aprobado el 2026-10-03. Trata solo lo que falló y sus "
                 "implicaciones sobre lo ya hecho (conclusión 19 del análisis 1).") + t[b:]
    a = t.index("> Antes de analizar se leen")
    b = t.index("| «R-n o RP-n» | «qué se hizo por ella, o por qué no aplica» |") + len("| «R-n o RP-n» | «qué se hizo por ella, o por qué no aplica» |")
    t = t[:a] + RECOMENDACIONES + t[b:]
    a = t.index("> Copia del hallazgo que origina")
    b = t.index("«copia del hallazgo»") + len("«copia del hallazgo»")
    t = t[:a] + hallazgo() + t[b:]
    a = t.index("> Copia del pendiente, tal como")
    b = t.index("«copia del pendiente»") + len("«copia del pendiente»")
    t = t[:a] + PENDIENTE + t[b:]
    io.open(A, "w", encoding="utf-8", newline="\n").write(t)


if __name__ == "__main__":
    main()
