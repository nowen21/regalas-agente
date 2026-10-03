# -*- coding: utf-8 -*-
"""Plan de pruebas y estado de la fase D en su versión 2, por el análisis 9."""
import glob
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
D = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "HU-001-*", "D-EP-023-*"))[0]

CASOS = """### CP-008 · `DOC25` anota todo análisis aprobado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-23 |
| **Precondiciones** | T-16 terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `13·DOC25` | Pide anotar cada análisis aprobado en el principal de su alcance, aunque no cambie el sistema, con lo que aportó tal cual |
| 2 | Leer su checklist | Cumple, contra 44.0.0 |

### CP-009 · Lo que suma pasa tal cual al principal

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-24 |
| **Precondiciones** | T-10, T-17, T-18 y T-19 terminadas |
| **Datos de entrada** | Un proyecto de prueba con su principal, y otro con un principal de módulo |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer la plantilla del análisis | Termina con «Lo que aporta al análisis principal», con el resultado y lo que suma |
| 2 | Aprobar un análisis de prueba | Lo que suma queda, letra por letra, al final de la redacción del principal, y su fila al final de la «Lista de análisis» |
| 3 | Aprobar uno dentro de un módulo con principal propio | Queda en el principal del módulo y no en el del proyecto |
| 4 | Cambiar una palabra en el principal y correr el validador | Una falla que nombra el análisis |
| 5 | Correr `validar.py analisis` sobre el repositorio | Los diez análisis del piloto pasan |

### CP-010 · Sin filas no se aprueba

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-25 |
| **Precondiciones** | T-20 terminada |
| **Datos de entrada** | Un análisis de prueba con «Lo que se tiene que hacer» vacía |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Aprobarlo | No tiene la marca, y el aviso dice que falta al menos una fila |

### CP-011 · Sin «Lo que aporta» no se aprueba

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-26 |
| **Precondiciones** | T-20 terminada |
| **Datos de entrada** | Un análisis de prueba sin la sección, y otro con la sección sin lo que suma |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Aprobar cada uno | Ninguno tiene la marca, y el aviso dice qué falta |

"""


def una(t, viejo, nuevo):
    assert t.count(viejo) == 1, viejo[:80]
    return t.replace(viejo, nuevo)


def pruebas():
    ruta = os.path.join(D, "plan_pruebas.md")
    with open(ruta, encoding="utf-8") as f:
        t = f.read()
    t = una(t, "| **Versión** | 1.0 |", "| **Versión** | 2.0, por el análisis 9 |")
    t = una(t, "| **Alcance del plan** | HU-001: CA-17 a CA-22 |", "| **Alcance del plan** | HU-001: CA-17 a CA-26 |")
    t = una(t, "| Unitario | Las comprobaciones nuevas de `analisis.py` y la marca con la versión |",
            "| Unitario | Las comprobaciones nuevas de `analisis.py`, la marca con la versión y lo que hace `aprobar()` |")
    t = una(t, "| Aceptación | Que las plantillas, las recomendaciones y el análisis principal digan lo que piden los criterios |",
            "| Aceptación | Que las plantillas, las recomendaciones, `DOC25` y el análisis principal digan lo que piden los criterios |")
    t = una(t, "| Funcional | ☑ | CA-17 a CA-22 |", "| Funcional | ☑ | CA-17 a CA-26 |")
    t = una(t, "aprobado antes y después de 43.0.0.", "aprobado antes y después de 44.0.0.")
    t = una(t, "- Inspección: lectura de las plantillas, del archivo de recomendaciones y del análisis principal.",
            "- Inspección: lectura de las plantillas, del archivo de recomendaciones, de `DOC25` y del análisis principal.")
    t = una(t, "| Alta | CA-17, CA-18, CA-19 y CA-22 | 100% |", "| Alta | CA-17, CA-18, CA-19, CA-22, CA-24, CA-25 y CA-26 | 100% |")
    t = una(t, "| Media | CA-20 y CA-21 | 100% |", "| Media | CA-20, CA-21 y CA-23 | 100% |")
    t = una(t, "la suite completa en primer plano", "la suite completa por partes y en primer plano")
    t = una(t, "| HU-001 | RNF-06 | CP-007 | Trazabilidad | Media | Parcial | ☐ |",
            "| HU-001 | CA-23 | CP-008 | Funcional | Media | No | ☐ |\n"
            "| HU-001 | CA-24 | CP-009 | Funcional | Alta | Parcial | ☐ |\n"
            "| HU-001 | CA-25 | CP-010 | Funcional | Alta | Sí | ☐ |\n"
            "| HU-001 | CA-26 | CP-011 | Funcional | Alta | Sí | ☐ |\n"
            "| HU-001 | RNF-06 | CP-007 | Trazabilidad | Media | Parcial | ☐ |")
    t = una(t, "**Cobertura:** 6 de 6 criterios y el RNF-06.", "**Cobertura:** 10 de 10 criterios y el RNF-06.")
    t = t.replace("aprobados con la versión 43.0.0", "aprobados con la versión 44.0.0")
    t = una(t, "| **Precondiciones** | T-06, T-07, T-08, T-09 y T-12 terminadas |",
            "| **Precondiciones** | T-06, T-07, T-08, T-09, T-12 y T-15 terminadas |")
    t = una(t, "| 4 | Validar un análisis aprobado con 43.0.0 que no dice cuáles consultó | Una falla |",
            "| 4 | Validar un análisis aprobado con 44.0.0 que no dice cuáles consultó | Una falla |\n"
            "| 5 | Leer los análisis 1 a 9 del pendiente 103 | Cada uno tiene «Recomendaciones», con la nota del piloto |")
    t = una(t, "| 5 | Correr `validar.py plantilla` sobre el archivo | Sin fallas |\n"
               "| 6 | Leer el recuerdo | Enlaza la R-1 y conserva que el usuario lo pidió |",
            "| 6 | Correr `validar.py plantilla` sobre el archivo | Sin fallas |\n"
            "| 7 | Leer el recuerdo | Enlaza la R-1 y conserva que el usuario lo pidió |")
    t = una(t, "| 1 | Leer la lista de cambios | Tiene las líneas de los análisis 6, 7 y 8, con su fecha y su enlace |\n"
               "| 2 | Validar con un análisis aprobado que no aparece en la lista | Un aviso, según lo decidido en 2.7 del plan de trabajo |",
            "| 1 | Leer el análisis principal | Su contenido es la redacción que forman los aportes, sin «Qué se construye hoy» |\n"
            "| 2 | Leer la «Lista de análisis» | Tiene los diez análisis, del de la forma anterior al 9, con fecha, resultado y enlace |\n"
            "| 3 | Validar con un análisis aprobado que no aparece en la lista | Un aviso, aunque se haya aprobado antes de 44.0.0 |")
    t = una(t, "| **Datos de entrada** | Los análisis 1 a 8 del repositorio y uno de prueba |",
            "| **Datos de entrada** | Los análisis 1 a 9 del repositorio y uno de prueba |")
    t = una(t, "| 2 | Correr `validar.py analisis` sobre el repositorio | Los análisis 1 a 8 pasan sin las secciones nuevas |",
            "| 2 | Correr `validar.py analisis` sobre el repositorio | Los análisis 1 a 9 pasan sin lo que exige la 44.0.0 |")
    t = una(t, "| 3 | Validar uno aprobado con 43.0.0 sin las secciones | Falla |",
            "| 3 | Validar uno aprobado con 44.0.0 sin las secciones | Falla |")
    t = una(t, "### CP-007 · Cada tarea cita su criterio", CASOS + "### CP-007 · Cada tarea cita su criterio")
    t = una(t, "| **Alta** | Un análisis ya aprobado falla, o uno nuevo sin las secciones pasa |",
            "| **Alta** | Un análisis ya aprobado falla, uno nuevo sin las secciones pasa, o lo que suma no llega tal cual al principal |")
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)


def estado():
    ruta = os.path.join(D, "estado-fase.md")
    with open(ruta, encoding="utf-8") as f:
        t = f.read()
    t = una(t, "| **Módulo** | `plantillas/`, `validadores/` y `analisis/` |",
            "| **Módulo** | `plantillas/`, `validadores/`, `analisis/` y `base/13-documentacion/` |")
    t = una(t, "| 1 | Explorador · análisis | contexto entendido | ☑ Análisis 8 del pendiente 103 |",
            "| 1 | Explorador · análisis | contexto entendido | ☑ Análisis 8 y 9 del pendiente 103 |")
    t = una(t, "| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ El análisis 8, aprobado |",
            "| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ Los análisis 8 y 9, aprobados |")
    t = una(t, "| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ El 2026-10-02 |",
            "| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ El 2026-10-02, con los cambios del análisis 9 |")
    t = una(t, "N/A: la especificación son los CA-17 a CA-22 y las conclusiones del análisis 8",
            "N/A: la especificación son los CA-17 a CA-26")
    t = una(t, "☐ Escritos; esperan la decisión de 2.7 y la aprobación", "☐ Versión 2 escrita; espera la aprobación")
    t = una(t, "**Hechas:** 0 de 14. **Bloqueadas:** todas, hasta que se decida la duda de 2.7.",
            "**Hechas:** 0 de 20. **Bloqueadas:** todas, hasta que se aprueben los planes.")
    t = una(t, "| **CA cumplidos** | 0 de 6 |", "| **CA cumplidos** | 0 de 10 |")
    t = una(t, "- El aviso del CA-20 y el análisis 3 (plan, 2.7).\n", "")
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)


if __name__ == "__main__":
    pruebas()
    estado()
