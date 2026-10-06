# Plan de Pruebas · Fase `A-EP-025-HU-022-reabrir-con-sus-enlaces`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU022-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-022: CA-01 y CA-02 |
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
| Unitario | Reabrir | Claude | Carpetas temporales | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01 |
| Errores | ☑ | CA-02 |

### 3.3 Técnicas de diseño de casos

- Ida y vuelta: cerrar y reabrir, y comparar con lo de antes.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01 | 100% |
| Media | CA-02 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`: `python -m unittest core.herramientas.tests_reabrir`, y `CerrarArrastraLasCitas` de `core.enganches.tests_freno`.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-022 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-022 | CA-02 | CP-002 | Errores | Media | Sí | ☑ |

## 6. Casos de prueba

### CP-001 · Reabrir

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Cerrar un pendiente citado desde otro documento y reabrirlo | La cita apunta a `pendientes/`, sin enlaces rotos; la fila queda abierta; el pendiente dice el motivo |
| 2 | Un pendiente que decía «**Estado:** hecho» | Pasa a «reabierto» |

### CP-002 · Rechazos y simulación

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Reabrir un número que no está cerrado | Error, nada cambia |
| 2 | Reabrir sin motivo | Error, nada cambia |
| 3 | Reabrir sin `--aplicar` | Dice qué haría, nada cambia |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Un enlace roto | Antes de cerrar la fase |
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
