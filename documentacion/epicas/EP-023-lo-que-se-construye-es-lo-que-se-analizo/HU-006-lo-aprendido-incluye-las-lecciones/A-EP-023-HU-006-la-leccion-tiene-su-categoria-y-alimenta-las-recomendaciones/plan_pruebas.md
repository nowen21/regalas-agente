# Plan de Pruebas · Fase `A-EP-023-HU-006-la-leccion-tiene-su-categoria-y-alimenta-las-recomendaciones`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP023-HU006-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-006: CA-01 y CA-02 |
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
| Unitario | El tipo nuevo y las comprobaciones de la tabla de lecciones | Claude | Carpeta temporal | Sí |
| Aceptación | Que la plantilla diga lo que piden los criterios | Ing. José Dúmar Jiménez Ruíz | Lectura | No |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01 y CA-02 |
| Compatibilidad | ☑ | Los análisis aprobados antes siguen pasando |

### 3.3 Técnicas de diseño de casos

- Partición: lección con señal y sin ella; recomendación que existe y que no; aprobado antes y desde 46.0.0.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01 y CA-02 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Las pruebas de la fase: `memoria/pruebas.py` y `validadores/tests/test_analisis.py`; `validar.py estandar`, `analisis` y `flujo`, y `marcas.py` sobre los archivos de la fase.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-006 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-006 | CA-02 | CP-002 | Funcional | Alta | Parcial | ☑ |
| HU-006 | CA-01, CA-02 | CP-003 | Compatibilidad | Alta | Sí | ☑ |
| HU-006 | RNF-06 | CP-004 | Trazabilidad | Media | Parcial | ☑ |

**Cobertura:** 2 de 2 criterios y el RNF-06.

## 6. Casos de prueba

### CP-001 · La lección tiene su categoría y el análisis la enlaza

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-01 |
| **Precondiciones** | T-01 a T-03 terminadas |
| **Datos de entrada** | Una base de señales y análisis de prueba |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir una señal de tipo `leccion` | Queda con ese tipo |
| 2 | Validar un análisis aprobado con 46.0.0 cuya lección enlaza esa señal | Ninguna falla |
| 3 | Validar uno cuya lección no enlaza señal, o enlaza una de otro tipo | Una falla que nombra la lección |

### CP-002 · Las lecciones alimentan las recomendaciones

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-02 |
| **Precondiciones** | T-04 y T-05 terminadas |
| **Datos de entrada** | Análisis y recomendaciones de prueba |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer la tabla de lecciones de la plantilla | Trae la columna «Recomendación» y la nota de buscar antes de crear |
| 2 | Validar una lección que complementa una R-n que existe | Ninguna falla |
| 3 | Validar una con la columna vacía, y otra que nombra una R-n que no existe | Una falla por cada una |

### CP-003 · Lo aprobado antes no se reabre

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-01 y CA-02 |
| **Precondiciones** | T-03 y T-05 terminadas |
| **Datos de entrada** | Un análisis aprobado con 45.0.0 y el repositorio |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Validar el aprobado con 45.0.0 con lecciones «Por escribir» | Ninguna falla |
| 2 | Correr `validar.py analisis` sobre el repositorio | Sin fallas |

### CP-004 · Cada tarea cita su criterio

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / RNF-06 |
| **Precondiciones** | Fase terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar.py flujo` y leer el plan | Ninguna tarea sin su criterio |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Un análisis ya aprobado falla, o uno nuevo sin señal pasa | Antes de cerrar la fase |
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
