# Plan de Pruebas · Fase `A-EP-025-HU-020-quitar-con-sus-filas`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU020-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-020: CA-01 a CA-03 |
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
| Unitario | Quitar | Claude | Carpetas temporales | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01, CA-02 |
| Errores | ☑ | CA-03 |

### 3.3 Técnicas de diseño de casos

- Crear con el andamio y quitar enseguida; cambiar una letra y quitar.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01, CA-02 | 100% |
| Media | CA-03 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`: `python -m unittest core.herramientas.tests_andamio`, y las pruebas del andamio en `core.enganches.tests_freno` importando `core.validadores` primero.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-020 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-020 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |
| HU-020 | CA-03 | CP-003 | Errores | Media | Sí | ☑ |

## 6. Casos de prueba

### CP-001 · Borrar plantilla

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Crear una HU y quitarla | Sin carpeta; `epica.md` y su `README.md` iguales a antes de crear |
| 2 | Crear una fase y quitarla | Sin carpeta |
| 3 | Crear un pendiente y quitarlo | Sin carpeta |

### CP-002 · Archivar

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Crear una HU, cambiar su texto y quitarla | En `_archivo/` con el cambio; la fila apunta ahí con «(archivada)» |
| 2 | Crear otra HU | No reusa el número archivado |

### CP-003 · Rechazos y simulación

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Quitar una HU con una fase | Error, nada cambia |
| 2 | Quitar una carpeta que no es del andamio | Error, nada cambia |
| 3 | Quitar sin aplicar | Dice qué haría, nada cambia |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Se borra algo con trabajo | Antes de cerrar la fase |
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
