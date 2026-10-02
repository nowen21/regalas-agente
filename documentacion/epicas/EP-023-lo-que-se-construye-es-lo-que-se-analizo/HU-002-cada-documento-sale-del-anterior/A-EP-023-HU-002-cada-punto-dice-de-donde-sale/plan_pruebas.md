# Plan de Pruebas · Fase `A-EP-023-HU-002-cada-punto-dice-de-donde-sale`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP023-HU002-A |
| **Versión** | 2.0, del análisis 7 |
| **Alcance del plan** | HU-002: CA-01 a CA-03 |
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
| Unitario | `origen.revisar` sobre documentos de prueba | Claude | Carpeta temporal | Sí, `test_origen.py` |
| Sistema | El validador sobre el repositorio, y las reglas contra el checklist | Claude | Local | Sí, con `validar.py` |
| Aceptación | Que las reglas y la plantilla digan lo que piden los criterios | Ing. José Dúmar Jiménez Ruíz | Lectura | No |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01 a CA-03 |
| Seguridad | ☐ | No toca accesos |
| Rendimiento | ☐ | El validador lee archivos de texto de unas pocas épicas |
| Usabilidad | ☐ | No hay interfaz |
| Compatibilidad | ☐ | No hay interfaz |
| Accesibilidad | ☐ | No hay interfaz |
| Migración de datos | ☐ | Nada se migra |
| Recuperación | ☐ | Revertir el commit basta |

### 3.3 Técnicas de diseño de casos

- Partición: un documento con todos sus orígenes, uno sin «Sale de» y uno con una cita a un punto que no existe, para cada eslabón.
- Inspección: lectura de las reglas y de la plantilla contra los criterios.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | La regla y el validador del CA-01 | 100% |
| Media | CA-02, CA-03, versión y trazabilidad | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

`test_origen.py`; `validar.py origen`, `estandar`, `metareglas`, `tareas`, `amarre`, `version` y `flujo`; `marcas.py` sobre los archivos de la fase.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-002 | CA-01 | CP-001, CP-002, CP-003 | Funcional | Alta | Parcial | ☐ |
| HU-002 | CA-02 | CP-004 | Funcional | Media | No | ☐ |
| HU-002 | CA-03 | CP-005 | Funcional | Media | No | ☐ |
| HU-002 | CA-01, CA-02 | CP-006 | Funcional | Media | Sí | ☐ |
| HU-002 | RNF-06 | CP-007 | Trazabilidad | Media | Parcial | ☐ |

**Cobertura:** 3 de 3 criterios y el RNF-06.

## 6. Casos de prueba

### CP-001 · `F27` exige «Sale de»

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-01 |
| **Precondiciones** | T-01 terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `F27` | Exige «Sale de» en cada punto, con el punto del documento anterior, y dice que lo que no tiene origen no entra |
| 2 | Leer su dependencia | «extiende `02·F18`»; `F18` no cambió |
| 3 | Correr `validar.py metareglas` | Sin fallas |

### CP-002 · El validador sobre documentos de prueba

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-01 |
| **Precondiciones** | T-02 y T-04 terminadas |
| **Datos de entrada** | Una épica de prueba con un pendiente, su hallazgo, un análisis y una HU |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Todos los puntos con un origen que existe | Ninguna falla |
| 2 | Un criterio de la HU sin «Sale de» | Una falla que nombra el criterio |
| 3 | Un criterio que cita un punto que no está en «Lo que se tiene que hacer» | Una falla que nombra el punto |
| 4 | Una conclusión que cita un turno que no está en la conversación | Una falla |
| 5 | Una fila de «Lo que se tiene que hacer» que cita una conclusión que no existe | Una falla |
| 6 | Un pendiente sin «De dónde sale», y otro que cita un hallazgo que no está en su resumen | Una falla por cada uno |
| 7 | Una épica sin análisis cuyas HU no llevan «Sale de» | Ninguna falla |
| 8 | Correr `python -m unittest validadores.tests.test_origen` | Todos pasan |

### CP-003 · El validador sobre el repositorio

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-01 |
| **Precondiciones** | T-03 terminada |
| **Datos de entrada** | El repositorio del estándar |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar.py origen` | Sin fallas: los documentos de EP-023 citan orígenes que existen |

### CP-004 · `F28` dice que el cambio baja en orden

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-02 |
| **Precondiciones** | T-06 terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `F28` | El cambio se aplica en el documento donde nace, aunque sea el planteamiento, y baja en orden: épica, HU, especificación y plan |
| 2 | Leer su dependencia y su checklist | «extiende `02·F0`»; CUMPLE |

### CP-005 · La plantilla de la HU distingue los dos casos, y cada criterio dice de dónde sale

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-03 |
| **Precondiciones** | T-07 y T-09 terminadas |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer la sección 3 de `04-HU.md` | Si la HU sale de un pendiente, el problema del pendiente; si sale de una épica, la parte del problema de la épica que le toca, con el enlace |
| 2 | Leer los criterios de ejemplo de `04-HU.md` | Cada uno tiene «Sale de» encima del escenario |
| 3 | Correr `validar.py estandar` | Sin fallas |

### CP-006 · Registro, reglas por tarea y versión

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-01, CA-02 |
| **Precondiciones** | T-05 y T-08 terminadas |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar.py tareas`, `amarre` y `version` | Sin fallas; `VERSION` dice 42.0.0 |
| 2 | Leer `reglas-validables.md` | `F27` validable con `origen.py`; `F28` no validable |
| 3 | Medir con `marcas.py` los archivos tocados | Ninguna marca nueva |

### CP-007 · Cada tarea cita su criterio

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / RNF-06 |
| **Precondiciones** | Fase terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar.py flujo` y leer el plan | Ninguna tarea sin su criterio |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | El validador deja pasar un punto sin origen, o detiene uno que está bien | Antes de cerrar la fase |
| **Media** | Un validador falla o un enlace queda roto | Antes de cerrar la fase |
| **Baja** | Una marca de redacción | Antes de cerrar la fase |

### 9.2 Flujo del defecto

Un defecto se anota en el resultado de las pruebas. Si es un error dentro de lo que el plan aprobó, se corrige y se vuelve a correr el caso (análisis 1, conclusión 45). Si está fuera del plan, es un hallazgo: se detiene la fase y vuelve al análisis (análisis 1, conclusión 18).

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
| Hallazgos al ejecutar | Hallazgos que salieron al ejecutar el plan (análisis 1, conclusión 41) | Los que no se podían prever |

### 12.2 Dónde se miden

En el `resultado_pruebas.md` de la fase.
