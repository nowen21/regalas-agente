# -*- coding: utf-8 -*-
"""Lo que el análisis 9 manda a la HU-001: el CA-20 en su versión siguiente y los CA-23 a CA-26.
Los puntos 1, 2, 3, 5, 8 y 9 de su «Lo que se tiene que hacer» pasan a criterios; el 6 lo cumple el
plan de la fase D en su versión 2."""
import glob
import os
import re

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
HU = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "HU-001-*", "HU-001-*.md"))[0]

CA20 = """### CA-20 · El análisis principal al día

**Sale de:** análisis 8, punto 7, y análisis 9, punto 3.

```gherkin
Dado el análisis principal
Entonces su contenido es la redacción que forman los aportes de los análisis, sin «Lo que está definido» ni «Qué se construye hoy»
Y su «Lista de análisis» tiene una fila por cada análisis aprobado, del de la forma anterior al 9, con fecha, resultado y enlace
Y el validador avisa cuando un análisis aprobado no aparece en esa lista
```

**Cómo validarlo:**
1. Leer el análisis principal y su «Lista de análisis».
2. Correr el validador con un análisis aprobado que no aparece en ella.

**Aprobado cuando:** la redacción y las diez filas están, y el validador avisa en el paso 2.

"""

NUEVOS = """### CA-23 · Todo análisis aprobado se anota en el principal

**Sale de:** análisis 9, punto 1.

```gherkin
Dada la regla 13·DOC25
Entonces pide anotar cada análisis aprobado en el análisis principal de su alcance, aunque no cambie el sistema
Y lo que aportó pasa tal cual, sin redactarlo de nuevo
```

**Cómo validarlo:**
1. Leer `13·DOC25` y aplicarle el checklist del estándar.

**Aprobado cuando:** la regla lo pide y el checklist cumple.

### CA-24 · La sección «Lo que aporta al análisis principal»

**Sale de:** análisis 9, punto 2.

```gherkin
Dada la plantilla del análisis
Entonces trae la sección «Lo que aporta al análisis principal», con el resultado y lo que suma al principal
Cuando el usuario escribe «Apruebo el análisis»
Entonces el enganche pasa lo que suma, tal cual, al análisis principal
Y el validador avisa si las dos copias no coinciden
```

**Cómo validarlo:**
1. Abrir la plantilla del análisis.
2. Aprobar un análisis de prueba y comparar lo que suma con lo que quedó en el principal.
3. Cambiar una palabra en el principal y correr el validador.

**Aprobado cuando:** la sección está, el texto del paso 2 es idéntico y el validador avisa en el paso 3.

### CA-25 · Sin una fila en «Lo que se tiene que hacer» no se aprueba

**Sale de:** análisis 9, punto 5.

```gherkin
Dado un análisis sin filas en «Lo que se tiene que hacer»
Cuando el usuario escribe «Apruebo el análisis»
Entonces no queda aprobado y el aviso dice que falta al menos una fila
```

**Cómo validarlo:**
1. Aprobar un análisis de prueba con la tabla vacía.

**Aprobado cuando:** no tiene la marca y el aviso lo dice.

### CA-26 · Sin «Lo que aporta» no se aprueba

**Sale de:** análisis 9, punto 8.

```gherkin
Dado un análisis sin la sección «Lo que aporta al análisis principal»
Cuando el usuario escribe «Apruebo el análisis»
Entonces no queda aprobado y el aviso dice qué falta
```

**Cómo validarlo:**
1. Aprobar un análisis de prueba sin la sección.

**Aprobado cuando:** no tiene la marca y el aviso lo dice.

"""


def una(t, viejo, nuevo):
    assert t.count(viejo) == 1, viejo[:80]
    return t.replace(viejo, nuevo)


def main():
    with open(HU, encoding="utf-8") as f:
        t = f.read()
    t = una(t, "y del [análisis 8](../103-cada-documento-de-la-cadena-sale-del-anterior/analisis-8.md) (puntos 2, 3, 5, 7 y 8).",
            "y del [análisis 8](../103-cada-documento-de-la-cadena-sale-del-anterior/analisis-8.md) (puntos 2, 3, 5, 7 y 8) "
            "y del [análisis 9](../103-cada-documento-de-la-cadena-sale-del-anterior/analisis-9.md) (puntos 1, 2, 3, 5, 8 y 9; "
            "el 6 lo cumple el plan de la fase D).")
    t = una(t, "| **Estado** | Lista: aprobada el 2026-10-02 |", "| **Estado** | En revisión: cambió por el análisis 9 |")
    m = re.search(r"^### CA-20 .*?(?=^### CA-21)", t, re.M | re.S)
    t = t[:m.start()] + CA20 + t[m.end():]
    t = una(t, "**Sale de:** análisis 8, punto 5.", "**Sale de:** análisis 8, punto 5, y análisis 9, punto 9.")
    t = una(t, "Y el archivo arranca con las que dejaron las lecciones de los análisis 1 a 8\n",
            "Y el archivo arranca con las que dejaron las lecciones de los análisis 1 a 8\n"
            "Y los análisis 1 a 9 dicen qué recomendaciones consultaron\n")
    t = una(t, "**Sale de:** análisis 8, punto 11.", "**Sale de:** análisis 8, punto 11, y análisis 9, punto 8.")
    i = t.index("---\n\n## 5. Requisitos no funcionales")
    t = t[:i] + NUEVOS + t[i:]
    t = una(t, "| CA-17 a CA-22 | CA-02, CA-06, CA-08 |", "| CA-17 a CA-26 | CA-02, CA-06, CA-08 |")
    t = una(t, "| Tiene 16 criterios: puede pedir más de una fase |", "| Tiene 26 criterios: puede pedir más de una fase |")
    t = t.rstrip("\n") + ("\n| 2026-10-02 | Claude, por pedido de Ing. José Dúmar Jiménez Ruíz | El CA-20 pasa a su versión "
                          "siguiente, los CA-19 y CA-22 suman su origen y nacen los CA-23 a CA-26, según el análisis 9. "
                          "La aprobación queda sin efecto hasta que se revise |\n")
    with open(HU, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)


if __name__ == "__main__":
    main()
