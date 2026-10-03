# -*- coding: utf-8 -*-
"""Lo que el análisis 10 del pendiente 103 pasa a las HU: los CA-04 y CA-05 de la HU-002
(puntos 1 y 2) y la versión siguiente del CA-02 de la HU-007 (puntos 3 y 4)."""
import glob
import io
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
EP = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*"))[0]
HU002 = glob.glob(os.path.join(EP, "HU-002-*", "HU-002-*.md"))[0]
HU007 = glob.glob(os.path.join(EP, "HU-007-*", "HU-007-*.md"))[0]
A10 = "[análisis 10](../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-10.md)"
POR = "Claude, por pedido de Ing. José Dúmar Jiménez Ruíz"

CA_HU002 = """
### CA-04 · El agente recibe los acuerdos de los que sale lo que trabaja

**Sale de:** análisis 10, punto 1.

```gherkin
Dada una fase en curso, desde que se crea su carpeta hasta que se anota su commit
Cuando el usuario envía un mensaje
Entonces el agente recibe los acuerdos que citan los criterios de esa fase, siguiendo su «Sale de»
Y con un análisis prendido recibe los acuerdos de los análisis aprobados del mismo pendiente
Y los que no caben llegan nombrados con su tema y su número
```

**Cómo validarlo:**
1. Con una fase en curso de una HU cuyos criterios salen de un análisis, enviar un mensaje y leer lo que recibe el agente.
2. Prender un análisis de un pendiente que tiene análisis aprobados, enviar un mensaje y leer lo que recibe el agente.

**Aprobado cuando:** en los dos casos llegan los acuerdos, completos o nombrados.

### CA-05 · Lo que el plan decide por su cuenta queda marcado como propuesta del agente

**Sale de:** análisis 10, punto 2.

```gherkin
Dado un plan de trabajo
Cuando una de sus decisiones no sale de un acuerdo del análisis
Entonces va marcada como «propuesta del agente»
Y el validador de origen detiene la decisión que no cita su acuerdo ni lleva esa marca
```

**Cómo validarlo:**
1. Abrir la sección 2.6 de [`07-plan-trabajo.md`](../../../../plantillas/ciclo-vida-proyectos/07-plan-trabajo.md).
2. Correr `validar.py origen` sobre un plan con una decisión que no cita acuerdo ni lleva la marca.

**Aprobado cuando:** la plantilla pide la cita o la marca, y el validador detiene la decisión que no tiene ninguna de las dos.
"""


def cambiar(t, a, b):
    assert t.count(a) == 1, a[:80]
    return t.replace(a, b)


def hu002():
    t = io.open(HU002, encoding="utf-8").read()
    t = cambiar(t, "[análisis 7](../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-7.md), punto 1. Los campos",
                "[análisis 7](../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-7.md), punto 1, y del %s, puntos 1 y 2. Los campos" % A10)
    t = cambiar(t, "| **Módulo / Componente** | `base/02-flujo-de-trabajo/`, `validadores/` |",
                "| **Módulo / Componente** | `base/02-flujo-de-trabajo/`, `plantillas/`, `validadores/`, `adaptadores/claude-code/` |")
    t = cambiar(t, "Lo que no tenga origen se detiene | Análisis 1, conclusión 39 |\n",
                "Lo que no tenga origen se detiene | Análisis 1, conclusión 39 |\n"
                "| RN-06 | El agente recibe los acuerdos de los que sale lo que trabaja, y lo que el plan decide por su cuenta va marcado como propuesta suya | Análisis 10, acuerdos 3 y 4 |\n")
    i = t.index("### CA-03 ·")
    j = t.index("\n---\n\n## 5.", i)
    t = t[:j] + "\n" + CA_HU002 + t[j:]
    t = cambiar(t, "| **S**mall (pequeña) | ✅ | Tres criterios |", "| **S**mall (pequeña) | ✅ | Cinco criterios |")
    t = cambiar(t, "| 2026-10-02 | Ing. José Dúmar Jiménez Ruíz | **Aprobada**, con el CA-03 del análisis 7 |\n",
                "| 2026-10-02 | Ing. José Dúmar Jiménez Ruíz | **Aprobada**, con el CA-03 del análisis 7 |\n"
                "| 2026-10-03 | %s | Nacen los CA-04 y CA-05, según el análisis 10. La aprobación queda sin efecto hasta que se revise |\n" % POR)
    io.open(HU002, "w", encoding="utf-8", newline="\n").write(t)


def hu007():
    t = io.open(HU007, encoding="utf-8").read()
    t = cambiar(t, "[análisis 8](../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-8.md), punto 1. Los campos",
                "[análisis 8](../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-8.md), punto 1, y del %s, puntos 3 y 4. Los campos" % A10)
    t = cambiar(t, "incluye las reglas propias de cada proyecto | Análisis 1, conclusión 47 |\n",
                "incluye las reglas propias de cada proyecto | Análisis 1, conclusión 47 |\n"
                "| RN-05 | La fase activa es la fase en curso. Antes de aprobarse su plan, solo se escriben los documentos de la fase y lo que una regla autoriza; sin fase en curso, solo lo autorizado | Análisis 10, acuerdo 6 |\n"
                "| RN-06 | La revisión de la integración continua se activa sola donde el proyecto la tiene, y de dónde se descarga Cimiento es un dato del proyecto | Análisis 10, acuerdo 5 |\n")
    t = cambiar(t, "**Sale de:** análisis 1, punto 26, y análisis 8, punto 1.",
                "**Sale de:** análisis 1, punto 26; análisis 8, punto 1, y análisis 10, puntos 3 y 4.")
    t = cambiar(t, "Y cada adaptador declara qué capas cubre en su herramienta y por qué no las demás\n```",
                "Y cada adaptador declara qué capas cubre en su herramienta y por qué no las demás\n"
                "Y la fase activa es la fase en curso: antes de aprobarse su plan solo se escriben los documentos de la fase y lo que una regla autoriza, y sin fase en curso, solo lo autorizado\n"
                "Y la revisión de la integración continua se agrega sola si el proyecto la tiene, y de dónde se descarga Cimiento es un dato del proyecto\n```")
    t = cambiar(t, "3. Intentar escribir algo que la lista de lo autorizado incluye.\n",
                "3. Intentar escribir algo que la lista de lo autorizado incluye.\n"
                "4. Con la fase en curso y su plan sin aprobar, intentar escribir un archivo de código.\n"
                "5. Instalar en un proyecto con integración continua y en uno sin ella.\n")
    t = cambiar(t, "y el paso 3 pasa. Las fases que hagan falta las reparte el plan.",
                "y el paso 3 pasa; el paso 4 se detiene; en el paso 5 el primero recibe el paso de revisión y el segundo no. Las fases que hagan falta las reparte el plan.")
    t = cambiar(t, "| 2026-10-02 | Ing. José Dúmar Jiménez Ruíz | **Aprobada**, con los cambios del análisis 8 |\n",
                "| 2026-10-02 | Ing. José Dúmar Jiménez Ruíz | **Aprobada**, con los cambios del análisis 8 |\n"
                "| 2026-10-03 | %s | El CA-02 pasa a su versión siguiente: la fase activa y la integración continua, según el análisis 10. La aprobación queda sin efecto hasta que se revise |\n" % POR)
    io.open(HU007, "w", encoding="utf-8", newline="\n").write(t)


if __name__ == "__main__":
    hu002()
    hu007()
