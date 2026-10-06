# Plan de Pruebas · Fase `A-EP-025-HU-023-desde-un-turno-y-en-la-base`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU023-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-023: CA-01 y CA-02 |
| **Fecha** | 2026-10-05 |
| **Elaborado por** | Claude |
| **Revisado por** | Ing. José Dúmar Jiménez Ruíz |
| **Aprobado por** | [Análisis 3 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md), el 2026-10-05 |
| **Estado** | Aprobado |

Para una fase, la plantilla pide las secciones 3, 5, 6, 9 y 12; las demás son opcionales y no se usan.

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Unitario | Desde un turno | Claude | Carpetas temporales | Sí |
| Integración | El estado en la base | Claude | Base de pruebas en MariaDB | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01, CA-02 |

### 3.3 Técnicas de diseño de casos

- Turnos en el borde (1, el actual, uno más); proyecto con y sin registro.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01, CA-02 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`: `python -m unittest core.enganches.tests_analisis_desde core.enganches.tests_analisis_en_curso`, `python manage.py test core.proyectos.tests_analisis_prendido`, y las pruebas del análisis prendido en `core.enganches.tests_freno`.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-023 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-023 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |

## 6. Casos de prueba

### CP-001 · Desde un turno

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | «Analicemos: el pendiente 7 desde el turno 4» en el turno 12 | Prendido desde el 4 |
| 2 | Ya prendido desde el 10, pedir desde el 4 | Pasa al 4 |
| 3 | Pedir desde el 20 en el turno 12, o desde el 0 | Se rechaza con el motivo |
| 4 | Sin «desde» | Desde el turno actual, como antes |

### CP-002 · En la base

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Prender en un proyecto registrado | Fila en la tabla; ningún archivo |
| 2 | Pausar y borrar | La fila cambia y se borra |
| 3 | Un estado en archivo de ese proyecto | Pasa a la tabla y el archivo se borra |
| 4 | Un proyecto sin registro | Sigue con su archivo |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | La conversación deja de pasar al análisis | Antes de cerrar la fase |
| **Baja** | Una marca de redacción | Antes de cerrar la fase |

### 9.2 Flujo del defecto

Un defecto se anota en el resultado. Si se corrige dentro del plan, se vuelve a correr el caso; si pide tocar algo que el plan no declara, se resuelve en la conversación con el usuario.

### 9.3 Contenido mínimo de un reporte

- Caso y paso donde apareció.
- Resultado esperado frente al obtenido.

### 9.4 Registro

En el `resultado_pruebas.md` de la fase.

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de exigencias | Criterios con caso / criterios de la fase | 100% |
| Casos ejecutados | Ejecutados / diseñados | 100% |

### 12.2 Dónde se miden

En el `resultado_pruebas.md` de la fase.
