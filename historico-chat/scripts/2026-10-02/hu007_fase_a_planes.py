# -*- coding: utf-8 -*-
"""Fase A de la HU-007: plan de pruebas, estado de la fase y su fila en la HU."""
import glob
import os
import re

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
HU_DIR = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "HU-007-*"))[0]
FASE = "A-EP-023-HU-007-el-plan-dice-que-se-toca-y-el-commit-lo-cumple"
D = os.path.join(HU_DIR, FASE)

CPS = [
    ("CP-001", "CA-01", "Alta", "Sí", "El plan dice qué toca y quién lo aprobó", "T-01 y T-02 terminadas",
     "Planes de prueba aprobados con 48.0.0",
     [("Leer la plantilla del plan", "La sección 0 pide la aprobación con quién, cuándo y versión; la 2.1 pide rutas exactas"),
      ("Validar un plan con una fila que es una carpeta, un comodín o una descripción", "Una falla por fila"),
      ("Validar un plan sin quién o sin fecha en la aprobación", "Una falla"),
      ("Validar un plan aprobado con 47.0.0 con esas filas", "Ninguna falla")]),
    ("CP-002", "CA-03", "Alta", "Sí", "El commit con un archivo no declarado se rechaza", "T-05 a T-07 terminadas",
     "Un repositorio de git de prueba con una fase y su plan",
     [("Preparar un archivo que el plan declara y correr `validar.py plan --preparados`", "Pasa"),
      ("Preparar uno que el plan no declara ni ninguna regla autoriza", "Falla y nombra el archivo"),
      ("Preparar un documento de la propia fase y el resumen de la sesión", "Pasan"),
      ("Leer el `pre-commit` que escribe el instalador", "Corre `validar.py plan --preparados`")]),
    ("CP-003", "CA-04", "Alta", "Sí", "Lo que autorizan las reglas, también las del proyecto", "T-03 a T-05 terminadas",
     "Reglas de prueba de `base/` y una regla `P1` en `.agente/reglas-proyecto.md`",
     [("Leer las diez reglas de la línea base", "Cada una trae su línea «Autoriza escribir»"),
      ("Preguntar a `autorizado.py` por un análisis, un guion y la memoria", "Dice la regla que los autoriza"),
      ("Preparar para el commit un archivo que solo autoriza la `P1`", "Pasa")]),
    ("CP-004", "RNF-06", "Media", "Parcial", "Cada tarea cita su criterio", "Fase terminada", "Ninguno",
     [("Correr `validar.py flujo` y leer el plan", "Ninguna tarea sin su criterio")]),
]

CABEZA = """# Plan de Pruebas · Fase `{f}`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP023-HU007-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-007: CA-01, CA-03 y CA-04 |
| **Fecha** | 2026-10-02 |
| **Elaborado por** | Claude |
| **Revisado por** | Ing. José Dúmar Jiménez Ruíz |
| **Aprobado por** | Pendiente |
| **Estado** | Borrador |

Para una fase, la plantilla pide las secciones 3, 5, 6, 9 y 12; las demás son opcionales y no se usan.

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Unitario | El validador del plan, lo autorizado y la comparación del commit | Claude | Repositorio de git temporal | Sí |
| Aceptación | Que la plantilla y las reglas digan lo que piden los criterios | Ing. José Dúmar Jiménez Ruíz | Lectura | No |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01, CA-03 y CA-04 |
| Compatibilidad | ☑ | Los planes aprobados antes no se revisan |

### 3.3 Técnicas de diseño de casos

- Partición: archivo declarado, autorizado por regla, de la fase y ninguno; plan aprobado antes y desde 48.0.0.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01, CA-03 y CA-04 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Las pruebas de la fase: `validadores/tests/test_nada_fuera_del_plan.py`; `validar.py estandar`, `flujo` y `plan --preparados`, y `marcas.py` sobre los archivos de la fase.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
{mat}

**Cobertura:** 3 de 3 criterios de esta fase y el RNF-06.

## 6. Casos de prueba

{casos}

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Un commit con un archivo no autorizado pasa, o uno autorizado se rechaza | Antes de cerrar la fase |
| **Baja** | Una marca de redacción | Antes de cerrar la fase |

### 9.2 Flujo del defecto

Un defecto se anota en el resultado de las pruebas. Si es un error dentro de lo que el plan aprobó, se corrige y se vuelve a correr el caso. Si está fuera del plan, es un hallazgo: se detiene la fase y vuelve al análisis.

### 9.3 Contenido mínimo de un reporte

- Caso y paso donde apareció.
- Resultado esperado frente al obtenido.

### 9.4 Registro

Los defectos van en el `resultado_pruebas.md` de la fase.

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de exigencias | Criterios y RNF con caso / criterios y RNF de la fase | 100% |
| Casos ejecutados | Ejecutados / diseñados | 100% |

### 12.2 Dónde se miden

En el `resultado_pruebas.md` de la fase.
"""


def plan_pruebas():
    filas = []
    for c in CPS:
        tipo = "Trazabilidad" if c[1] == "RNF-06" else "Funcional"
        filas.append("| HU-007 | %s | %s | %s | %s | %s | ☐ |" % (c[1], c[0], tipo, c[2], c[3]))
    casos = []
    for c in CPS:
        pasos = "\n".join("| %d | %s | %s |" % (i, a, b) for i, (a, b) in enumerate(c[7], 1))
        casos.append("### %s · %s\n\n| Campo | Valor |\n|---|---|\n| **HU / CA** | HU-007 / %s |\n"
                     "| **Precondiciones** | %s |\n| **Datos de entrada** | %s |\n\n"
                     "| # | Acción | Resultado esperado |\n|---|---|---|\n%s" % (c[0], c[4], c[1], c[5], c[6], pasos))
    texto = CABEZA.format(f=FASE, mat="\n".join(filas), casos="\n\n".join(casos))
    with open(os.path.join(D, "plan_pruebas.md"), "w", encoding="utf-8", newline="\n") as s:
        s.write(texto)


def estado():
    origen = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "HU-004-*", "A-EP-023-*", "estado-fase.md"))[0]
    with open(origen, encoding="utf-8") as e:
        t = e.read()
    t = t.replace(os.path.basename(os.path.dirname(origen)), FASE)
    t = t.replace("[HU-004](../HU-004-un-hallazgo-detiene-la-ejecucion-y-vuelve-al-analisis.md)",
                  "[HU-007](../HU-007-nada-se-escribe-fuera-del-plan-aprobado.md)")
    pares = [
        ("**Estación actual:** 12, commit. **Última puerta pasada:** 11.", "**Estación actual:** 7, planificador de tareas. **Última puerta pasada:** 6."),
        ("☑ Aprobados el 2026-10-02", "☐ Escritos; esperan la aprobación"),
        ("| 8 | Implementador | implementado + pruebas verdes | ☑ Las 9 tareas; las pruebas de la fase pasan |", "| 8 | Implementador | implementado + pruebas verdes | ☐ |"),
        ("| 9 | Verificador | trazabilidad sin faltantes | ☑ `origen` y `flujo` sin fallas |", "| 9 | Verificador | trazabilidad sin faltantes | ☐ |"),
        ("| 10 | Crítico | sin hallazgos graves | ☑ Ninguno |", "| 10 | Crítico | sin hallazgos graves | ☐ |"),
        ("| 11 | Cierre documental + señales | docs y señales al día | ☑ Resultado de pruebas, HU y registro de cambios |", "| 11 | Cierre documental + señales | docs y señales al día | ☐ |"),
        ("| 12 | Commit | 👤 autorizado | ✅ `cfcc89d` |", "| 12 | Commit | 👤 autorizado | ☐ |"),
        ("**Hechas:** 9 de 9. **Bloqueadas:** ninguna.", "**Hechas:** 0 de 8. **Bloqueadas:** todas, hasta que se aprueben los planes."),
        ("| **Concepto** | Cumple |", "| **Concepto** | Sin ejecutar |"),
        ("| **CA cumplidos** | 7 de 7 |", "| **CA cumplidos** | 0 de 3 |"),
        ("N/A: la especificación son los CA-01 a CA-07", "N/A: la especificación son los CA-01, CA-03 y CA-04"),
        ("☑ Análisis 1 y 2 del pendiente 103", "☑ Análisis 1 y 8 del pendiente 103"),
        ("☑ Los análisis 1 y 2, aprobados", "☑ Los análisis 1 y 8, aprobados"),
        ("## 3. Pendiente / preguntas abiertas\n\nNinguna.\n", "## 3. Pendiente / preguntas abiertas\n\n- Que el usuario apruebe el plan de trabajo y el de pruebas.\n"),
    ]
    for a, b in pares:
        assert t.count(a) == 1, a
        t = t.replace(a, b)
    with open(os.path.join(D, "estado-fase.md"), "w", encoding="utf-8", newline="\n") as s:
        s.write(t)


def fila_en_la_hu():
    h = [x for x in os.listdir(HU_DIR) if x.startswith("HU-007") and x.endswith(".md")][0]
    p = os.path.join(HU_DIR, h)
    with open(p, encoding="utf-8") as e:
        s = e.read()
    m = re.search(r"^\| N/A[^\n]*\|$", s, re.M)
    assert m
    fila = ("| [`%s`](%s/estado-fase.md) | CA-01, CA-03, CA-04 | HU-003, HU-004 | [plan](%s/plan_trabajo.md) | "
            "[pruebas](%s/plan_pruebas.md) | Pendiente | Planes escritos, sin aprobar |" % (FASE, FASE, FASE, FASE))
    with open(p, "w", encoding="utf-8", newline="\n") as e:
        e.write(s[:m.start()] + fila + s[m.end():])


if __name__ == "__main__":
    plan_pruebas()
    estado()
    fila_en_la_hu()
