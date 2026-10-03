# Plan de Pruebas · Fase `A-EP-023-HU-004-el-hallazgo-detiene-y-vuelve-al-analisis`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP023-HU004-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-004: CA-01 a CA-07 |
| **Fecha** | 2026-10-02 |
| **Elaborado por** | Claude |
| **Revisado por** | Ing. José Dúmar Jiménez Ruíz |
| **Aprobado por** | Ing. José Dúmar Jiménez Ruíz, el 2026-10-02 |
| **Estado** | Aprobado |

Para una fase, la plantilla pide las secciones 3, 5, 6, 9 y 12; las demás son opcionales y no se usan.

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Unitario | Que la fase y la HU no cierren con el análisis del hallazgo abierto | Claude | Carpeta temporal | Sí |
| Aceptación | Que las reglas y las plantillas digan lo que piden los criterios | Ing. José Dúmar Jiménez Ruíz | Lectura | No |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01 a CA-07 |
| Compatibilidad | ☑ | Las fases del repositorio siguen pasando |

### 3.3 Técnicas de diseño de casos

- Partición: fase con el análisis del hallazgo abierto y aprobado; fase en curso y cerrada.
- Inspección: lectura de las reglas y de las plantillas.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-02, CA-04 y CA-05 | 100% |
| Media | CA-01, CA-03, CA-06 y CA-07 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Las pruebas de la fase: `validadores/tests/test_hallazgo_detiene_la_fase.py`; `validar.py estandar`, `fases` y `flujo`, y `marcas.py` sobre los archivos de la fase.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-004 | CA-01 | CP-001 | Funcional | Media | No | ☑ |
| HU-004 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |
| HU-004 | CA-03 | CP-003 | Funcional | Media | No | ☑ |
| HU-004 | CA-04 | CP-004 | Funcional | Alta | No | ☑ |
| HU-004 | CA-05 | CP-005 | Funcional | Alta | No | ☑ |
| HU-004 | CA-06 | CP-006 | Funcional | Media | No | ☑ |
| HU-004 | CA-07 | CP-007 | Funcional | Media | No | ☑ |
| HU-004 | RNF-06 | CP-008 | Trazabilidad | Media | Parcial | ☑ |

**Cobertura:** 7 de 7 criterios y el RNF-06.

## 6. Casos de prueba

### CP-001 · Versiones en el mismo archivo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-01 |
| **Precondiciones** | T-01 terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `02·F28` | El hallazgo, el pendiente, la HU y el plan cambian en su mismo archivo; el análisis no se reescribe y se numera el siguiente |

### CP-002 · Un hallazgo detiene y nada cierra

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-02 |
| **Precondiciones** | T-02 y T-03 terminadas |
| **Datos de entrada** | Una épica, una HU, una fase y un pendiente de prueba |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer la sección 4 del estado de la fase | Trae el motivo «hallazgo al ejecutar», con el enlace al análisis |
| 2 | Marcar «Cumple» una fase cuyo pendiente tiene un análisis posterior sin aprobar | `fases.py` falla y nombra el análisis abierto |
| 3 | Marcar «Terminada» la HU | `fases.py` falla |
| 4 | Aprobar ese análisis | Ya no falla |
| 5 | Correr `validar.py fases` sobre el repositorio | Sin fallas nuevas |

### CP-003 · El análisis siguiente trata solo lo que falló

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-03 |
| **Precondiciones** | T-04 terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `13·DOC24` | Lo dice |

### CP-004 · `F8` y `F9` detienen y vuelven al análisis

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-04 |
| **Precondiciones** | T-05 terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `02·F8` y `02·F9` | Las dos dicen que la ejecución se detiene y vuelve al análisis |

### CP-005 · El plan pasa de versión y la fase cerrada se reabre

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-05 |
| **Precondiciones** | T-06 terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `02/base.md`, el anexo de `02·F12` y `13·DOC12` | Los tres dicen lo del criterio |

### CP-006 · El plan registra sus hallazgos

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-06 |
| **Precondiciones** | T-07 terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer la sección 13 de la plantilla del plan | Pide cuántos hallazgos salieron y el enlace a cada análisis |

### CP-007 · El análisis decide primero si es parte del plan

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-07 |
| **Precondiciones** | T-08 terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `13·DOC24` y la nota de la plantilla del análisis | Dicen lo del criterio |

### CP-008 · Cada tarea cita su criterio

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / RNF-06 |
| **Precondiciones** | Fase terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar.py flujo` y leer el plan | Ninguna tarea sin su criterio |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Una fase cierra con el análisis del hallazgo abierto, o una fase del repositorio empieza a fallar sin razón | Antes de cerrar la fase |
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
