# Plan de Pruebas · Fase A-EP-001-HU-041, las reglas nombran la base de datos del agente   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Ningún criterio de aceptación queda sin al menos un caso. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar: lo que pasó va en el `resultado_pruebas.md` de la misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP001-HU041-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-041](../HU-041-las-reglas-reconocen-la-base-de-cimiento-como-fuente-del-estandar.md) |
| **Fecha** | 2026-10-06 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 132](../../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Sistema | Las reglas cambiadas pasan los validadores del estándar | El agente | Local | Sí |
| Aceptación | El texto dice lo que pide la HU | El usuario | Local | No |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Criterios de aceptación de la HU |

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Se corren `python validadores/validar.py metareglas` y `python validadores/validar.py estandar`. No se corre ninguna suite de Cimiento: la fase no toca código.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-041 | CA-01 | [CP-001](#cp-001--m10-dice-versión-y-registro-en-la-base) | Funcional | Crítica | No | ☐ |
| HU-041 | CA-02 | [CP-002](#cp-002--nada-dice-que-la-fuente-es-el-texto) | Funcional | Alta | No | ☐ |
| HU-041 | CA-03 | [CP-003](#cp-003--los-validadores-del-estándar-pasan), [CP-004](#cp-004--la-versión-sube-a-5600) | Funcional | Alta | Sí | ☐ |
| HU-041 | RNF-01 | [CP-001](#cp-001--m10-dice-versión-y-registro-en-la-base) | Trazabilidad | Media | No | ☐ |

**Cobertura:** 4 de 4 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · `M10` dice versión y registro en la base

| Campo | Valor |
|---|---|
| **HU / CA** | HU-041 / CA-01, RNF-01 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | T-01, T-02 y T-06 hechas |
| **Datos de entrada** | `M10-…md`, `base/20-meta-reglas/base.md` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `M10` | El título no cambió |
| 2 | Leer el cuerpo | Dice que todo cambio, del estándar o de un proyecto, sube su versión y queda registrado en la base de datos del agente, y que mientras no la tenga siguen `CHANGELOG.md` y `VERSION` |
| 3 | Leer la sección «M10» de `base.md` | Trae las dos preguntas que fijan el tipo |
| 4 | Leer el checklist | Está en CUMPLE contra 56.0.0 y cita el análisis 1 del pendiente 132 |

### CP-002 · Nada dice que la fuente es el texto

| Campo | Valor |
|---|---|
| **HU / CA** | HU-041 / CA-02 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | T-03 a T-05 hechas |
| **Datos de entrada** | `C19`, la nota, EP-016, `CLAUDE.md` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `C19` | La memoria vive en la base de datos del agente cuando la tiene |
| 2 | Abrir la nota de la fuente de las reglas | Marcada como derogada, con el enlace al análisis |
| 3 | Abrir EP-016, secciones 7, 10 y 13 | La restricción derogada, con el enlace |
| 4 | Leer `CLAUDE.md`, secciones 2 y 4 | Versionar y hacer commit se hacen desde la pantalla cuando exista |

### CP-003 · Los validadores del estándar pasan

| Campo | Valor |
|---|---|
| **HU / CA** | HU-041 / CA-03 |
| **Tipo** | Funcional, regresión |
| **Prioridad** | Alta |
| **Precondiciones** | T-01 a T-08 hechas |
| **Datos de entrada** | El repositorio |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `python validadores/validar.py metareglas` | Sin fallas |
| 2 | Correr `python validadores/validar.py estandar` | Sin fallas nuevas por esta fase |

### CP-004 · La versión sube a 56.0.0

| Campo | Valor |
|---|---|
| **HU / CA** | HU-041 / CA-03 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | T-08 hecha |
| **Datos de entrada** | `CHANGELOG.md`, `VERSION` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `VERSION` | Dice 56.0.0 |
| 2 | Abrir `CHANGELOG.md` | La primera entrada es 56.0.0, MAYOR, y nombra `20·M10` y `01·C19` |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4, con el paso que falló; si obliga a tocar un archivo que el plan no declara, es hallazgo y se detiene la fase.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre los 4 diseñados, en `resultado_pruebas.md`.
