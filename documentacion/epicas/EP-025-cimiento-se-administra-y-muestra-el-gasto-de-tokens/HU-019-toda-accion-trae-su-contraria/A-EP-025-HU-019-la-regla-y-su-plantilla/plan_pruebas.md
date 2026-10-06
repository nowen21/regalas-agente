# Plan de Pruebas · Fase `A-EP-025-HU-019-la-regla-y-su-plantilla`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU019-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-019: CA-01 a CA-03 |
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
| Validadores | Forma de la regla, índices y versión | Claude | El repositorio | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01 a CA-03 |

### 3.3 Técnicas de diseño de casos

- Los validadores del estándar sobre lo cambiado.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01, CA-03 | 100% |
| Media | CA-02 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde la raíz: `python validadores/validar.py metareglas`, `estandar`, `indices` y `versionado`.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-019 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-019 | CA-02 | CP-002 | Funcional | Media | No | ☑ |
| HU-019 | CA-03 | CP-003 | Funcional | Alta | Sí | ☑ |

## 6. Casos de prueba

### CP-001 · La regla

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `validar.py metareglas`, `estandar` e `indices` | Sin fallas sobre `F30` |
| 2 | Buscar `F30` en `base/mapa-de-tareas.md` | Aparece bajo sus tareas |

### CP-002 · La plantilla

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir la plantilla del plan | La sección 2.8 enlaza `F30` y trae su tabla |

### CP-003 · La versión

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `validar.py versionado` | Sin fallas; versión mayor nueva |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Una falla de un validador sobre lo cambiado | Antes de cerrar la fase |
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
