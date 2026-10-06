# Plan de Pruebas · Fase A-EP-001-HU-040, `01·C29` nombra la base de datos del agente   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que ningún criterio de aceptación quede sin al menos un caso, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y no se modifica al ejecutar: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP001-HU040-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-040](../HU-040-c29-reconoce-la-base-de-cimiento.md) |
| **Fecha** | 2026-10-05 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 124](../../../../../historico-chat/resumenes/2026-10-05/pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Sistema | La regla cambiada pasa los validadores del estándar | El agente | Local | Sí |
| Aceptación | El texto dice lo que pide la HU | El usuario | Local | No |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Criterios de aceptación de la HU |

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Se corren `python validadores/validar.py metareglas` y `python validadores/validar.py estandar`, que son los que leen las reglas de `base/`. No se corre ninguna suite de Cimiento: la fase no toca código.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-040 | [CA-01](../HU-040-c29-reconoce-la-base-de-cimiento.md#ca-01--la-regla-nombra-la-base-de-cimiento) | [CP-001](#cp-001--la-regla-dice-repositorio-o-base-de-datos-del-agente) | Funcional | Crítica | No | ☐ |
| HU-040 | [CA-02](../HU-040-c29-reconoce-la-base-de-cimiento.md#ca-02--la-regla-pasa-sus-comprobaciones) | [CP-002](#cp-002--los-validadores-del-estándar-pasan), [CP-003](#cp-003--la-versión-sube-a-5510) | Funcional | Alta | Sí | ☐ |
| HU-040 | RNF-01 | [CP-001](#cp-001--la-regla-dice-repositorio-o-base-de-datos-del-agente) | Trazabilidad | Media | No | ☐ |

**Cobertura:** 3 de 3 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · La regla dice repositorio o base de datos del agente

| Campo | Valor |
|---|---|
| **HU / CA** | HU-040 / CA-01, RNF-01 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | T-01 a T-03 hechas |
| **Datos de entrada** | `base/01-conducta.md` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `base/01-conducta.md` en `## C29` | El título no cambió |
| 2 | Leer el cuerpo | Dice «en el repositorio o en la base de datos del agente» y que lo que no se corrige en su origen se trae a esa base en cuanto aparece, con las claves tapadas |
| 3 | Leer el ejemplo | Trae un INCORRECTO y un CORRECTO sobre el registro que la herramienta borra |
| 4 | Leer el checklist | Está en CUMPLE contra 55.1.0 y cita el acuerdo 5 del análisis 1 del pendiente 124 |

**Resultado esperado final:** la regla dice lo de RN-01 y RN-02 de la HU.

### CP-002 · Los validadores del estándar pasan

| Campo | Valor |
|---|---|
| **HU / CA** | HU-040 / CA-02 |
| **Tipo** | Funcional, regresión |
| **Prioridad** | Alta |
| **Precondiciones** | T-01 a T-04 hechas |
| **Datos de entrada** | El repositorio |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `python validadores/validar.py metareglas` | Sin fallas |
| 2 | Correr `python validadores/validar.py estandar` | Sin fallas nuevas por esta fase |

**Resultado esperado final:** ningún validador señala `C29` ni sus copias.

### CP-003 · La versión sube a 55.1.0

| Campo | Valor |
|---|---|
| **HU / CA** | HU-040 / CA-02 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | T-04 hecha |
| **Datos de entrada** | `CHANGELOG.md`, `VERSION` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `VERSION` | Dice 55.1.0 |
| 2 | Abrir `CHANGELOG.md` | La primera entrada es 55.1.0, MENOR, y nombra `01·C29` |

**Resultado esperado final:** la versión y su entrada están.

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4, con el paso que falló; si obliga a tocar un archivo que el plan no declara, es hallazgo y se detiene la fase.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre los 3 diseñados, en `resultado_pruebas.md`.
