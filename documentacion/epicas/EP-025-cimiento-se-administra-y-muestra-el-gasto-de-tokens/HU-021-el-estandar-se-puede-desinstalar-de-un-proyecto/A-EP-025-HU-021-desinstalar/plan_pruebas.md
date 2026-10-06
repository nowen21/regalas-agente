# Plan de Pruebas · Fase `A-EP-025-HU-021-desinstalar`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU021-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-021: CA-01 a CA-03 |
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
| Unitario | Desinstalar | Claude | Repositorio git temporal | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01, CA-02 |
| Errores | ☑ | CA-03 |

### 3.3 Técnicas de diseño de casos

- Ida y vuelta: instalar, desinstalar y comparar con lo de antes.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01, CA-02 | 100% |
| Media | CA-03 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`: `python -m unittest core.herramientas.tests_desinstalar core.herramientas.tests_instalacion`.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-021 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-021 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |
| HU-021 | CA-03 | CP-003 | Errores | Media | Sí | ☑ |

## 6. Casos de prueba

### CP-001 · Quitar

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Instalar los enganches con uno ajeno en git y en Claude Code, y desinstalar | Sin `.githooks/` propios ni `core.hooksPath`; en `settings.json` solo el ajeno |
| 2 | Con la copia del stack, la plantilla sellada, la integración continua y carpetas base vacías | Ya no están |
| 3 | Con el proyecto en el registro | Sale del registro |
| 4 | En el estándar, con la telemetría | Sin sus variables; las otras del usuario siguen |

### CP-002 · Lo propio se queda

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Con `CLAUDE.md`, `.agente/stack.md`, `historico-chat/` y `documentacion/` con contenido | Iguales |

### CP-003 · Simular y repetir

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Desinstalar sin aplicar | Dice qué quitaría, nada cambia |
| 2 | Desinstalar dos veces | La segunda no tiene nada que quitar |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Se borra algo del proyecto | Antes de cerrar la fase |
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
