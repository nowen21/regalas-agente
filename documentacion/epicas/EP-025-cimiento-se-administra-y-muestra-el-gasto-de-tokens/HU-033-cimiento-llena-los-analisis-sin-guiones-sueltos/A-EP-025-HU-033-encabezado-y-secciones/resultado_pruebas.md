# Resultado de Pruebas · Fase `A-EP-025-HU-033-encabezado-y-secciones`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-033-encabezado-y-secciones` |
| **HU** | [HU-033](../HU-033-cimiento-llena-los-analisis-sin-guiones-sueltos.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-09 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Pruebas de Django de Cimiento, con proyectos temporales y la plantilla real; versión 59.3.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | Prender el primer análisis de un pendiente con su H-1 enlazado | Sin marcas de rutas ni de copias; trae el pendiente, el H-1 y no el H-2 | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-01 | Crítica | El segundo análisis, y un pendiente sin hallazgo enlazado | Traen el pendiente y las rutas, y dejan la marca del hallazgo | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-02 | Crítica | `manage.py analisis seccion` con «Lo acordado» | La sección trae el texto nuevo; lo de antes y lo de después no cambia | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-02 | Crítica | El comando con «No existe» | Falla nombrando las secciones; el análisis no cambia | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** en la primera corrida, el título de la sección se tragaba el salto de línea siguiente y dejaba una línea vacía de más. Se corrigió.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase y las del análisis en curso | `"C:/Ing. Jose/ia/agente/proyectos/cimiento/.venv/Scripts/python.exe" "C:/Ing. Jose/ia/agente/proyectos/cimiento/manage.py" test core.enganches.tests_llenar_analisis core.enganches.tests_analisis_en_curso core.enganches.tests_analisis_desde` | Ran 18 tests in 1.797s, OK |

## 4. Defectos encontrados

Uno, corregido en el mismo ciclo: la línea vacía de más después del título de la sección.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001, CP-002 | Aprobado | Sí |
| CA-02 | CP-003, CP-004 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §5 | 100% | 2 de 2 | Sí |
| Casos ejecutados | Plan §12 | 100% | 4 de 4 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los 4 casos pasan, y las pruebas del análisis en curso siguen en verde.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/enganches/tests_llenar_analisis.py` y la salida de §3 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-09 | 4 | 0 | Primera ejecución |
