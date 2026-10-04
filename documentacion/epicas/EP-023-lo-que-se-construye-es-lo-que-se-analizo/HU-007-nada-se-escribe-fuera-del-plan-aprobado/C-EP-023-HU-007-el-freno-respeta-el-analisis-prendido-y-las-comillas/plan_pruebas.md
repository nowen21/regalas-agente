# Plan de Pruebas · Fase `C-EP-023-HU-007-el-freno-respeta-el-analisis-prendido-y-las-comillas`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP023-HU007-C |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-007: CA-05 y CA-06 |
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
| Unitario | El freno con análisis prendido y con comillas | Claude | Proyecto de prueba con git en una carpeta temporal | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-05, CA-06 |

### 3.3 Técnicas de diseño de casos

- Partición por estado del análisis (prendido o no) y por forma del `>` (entre comillas simples, dobles o suelto).

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-05, CA-06 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Las pruebas de la fase y del programa que cambia: `validadores/tests/test_el_freno.py`; `validar.py estandar`, `tareas`, `flujo` y `origen`, y las marcas de lo que se va a guardar.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-007 | CA-05 | CP-001 | Funcional | Alta | Sí | ☐ |
| HU-007 | CA-06 | CP-002 | Funcional | Alta | Sí | ☐ |

**Cobertura:** 2 de 2 criterios de esta fase.

## 6. Casos de prueba

### CP-001 · Con un análisis prendido, no se anota

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-05 |
| **Precondiciones** | T-01 y T-02 terminadas |
| **Datos de entrada** | Una sesión con su resumen, con y sin análisis prendido |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Con un análisis prendido, el freno detiene una escritura | El resumen no cambia y el aviso dice que se reporta en la conversación |
| 2 | Sin análisis prendido, lo mismo | El resumen suma el hallazgo, como antes |
| 3 | Leer `13·DOC22` | Lo dice |

### CP-002 · Un `>` entre comillas no es escritura

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-06 |
| **Precondiciones** | T-03 terminada |
| **Datos de entrada** | Órdenes de consola con `>` |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Una búsqueda con `"> acá"` entre comillas dobles | Pasa |
| 2 | Lo mismo con comillas simples | Pasa |
| 3 | Una redirección real a un archivo que el plan no declara | Se detiene |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | El freno anota con un análisis prendido, o deja pasar una redirección real | Antes de cerrar la fase |
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
