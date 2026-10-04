# Plan de Pruebas · Fase `B-EP-023-HU-004-solo-detiene-el-hallazgo-que-obliga-a-salirse-del-plan`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP023-HU004-B |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-004: CA-08 |
| **Fecha** | 2026-10-03 |
| **Elaborado por** | Claude |
| **Revisado por** | Ing. José Dúmar Jiménez Ruíz |
| **Aprobado por** | Ing. José Dúmar Jiménez Ruíz, el 2026-10-03 |
| **Estado** | Aprobado |

Para una fase, la plantilla pide las secciones 3, 5, 6, 9 y 12; las demás son opcionales y no se usan.

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Revisión | `02·F9` dice lo del CA-08 | Claude | El repositorio del estándar | No |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-08 |

### 3.3 Técnicas de diseño de casos

- Partición por hallazgo: el que obliga a tocar algo fuera del plan y el que no.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-08 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Las del programa que escribe lo que cambia: `validadores/tests/test_cada_tarea_sabe_que_reglas_le_aplican.py`; `validar.py estandar`, `flujo` y `origen`, y las marcas de lo que se va a guardar.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-004 | CA-08 | CP-001 | Funcional | Alta | No | ☐ |
| HU-004 | CA-08 | CP-002 | Funcional | Media | Sí | ☐ |

**Cobertura:** 1 de 1 criterio de esta fase.

## 6. Casos de prueba

### CP-001 · `02·F9` dice qué hallazgo detiene

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-08 |
| **Precondiciones** | T-01 terminada |
| **Datos de entrada** | `02·F9` |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer la excepción | Detiene solo el hallazgo que, para cerrar la fase, obliga a tocar algo que el plan no declara |
| 2 | Leer qué pasa con el otro | Se anota con su pendiente donde pertenece y el trabajo sigue |
| 3 | Leer `13·DOC24` y la nota de `plantillas/analisis.md` | Solo el hallazgo que obliga a tocar algo fuera del plan abre el análisis siguiente |

### CP-002 · La copia de la regla queda al día

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-08 |
| **Precondiciones** | T-01 terminada |
| **Datos de entrada** | `base/reglas-por-tarea/trabajar-cadena-2.md` y `base/reglas-por-tarea/escribir-documento-2.md` |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar.py estandar` | Sin fallas: la copia dice lo mismo que la regla y el sello vale |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | `02·F9` no dice lo del CA-08 | Antes de cerrar la fase |
| **Baja** | Una marca de redacción | Antes de cerrar la fase |

### 9.2 Flujo del defecto

Un defecto se anota en el resultado de las pruebas. Si es un error dentro de lo que el plan aprobó, se corrige y se vuelve a correr el caso. Si para cerrar la fase obliga a tocar algo que el plan no declara, es un hallazgo: se detiene la fase y vuelve al análisis.

### 9.3 Contenido mínimo de un reporte

- Caso y paso donde apareció.
- Resultado esperado frente al obtenido.

### 9.4 Registro

Los defectos van en el `resultado_pruebas.md` de la fase.

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de exigencias | Criterios con caso / criterios de la fase | 100% |
| Casos ejecutados | Ejecutados / diseñados | 100% |

### 12.2 Dónde se miden

En el `resultado_pruebas.md` de la fase.
