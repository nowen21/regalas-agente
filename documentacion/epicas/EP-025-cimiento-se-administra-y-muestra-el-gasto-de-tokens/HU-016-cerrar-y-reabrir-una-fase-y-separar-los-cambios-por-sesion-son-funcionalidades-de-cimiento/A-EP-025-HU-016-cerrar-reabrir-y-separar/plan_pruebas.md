# Plan de Pruebas · Fase `A-EP-025-HU-016-cerrar-reabrir-y-separar`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU016-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-016: CA-01 a CA-04 |
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
| Unitario | Cerrar, reabrir y separar | Claude | Carpetas temporales y un repositorio git temporal | Sí |
| Real | Cerrar esta misma fase | Claude | El repositorio | No |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01 a CA-03 |
| Errores | ☑ | CA-04 |

### 3.3 Técnicas de diseño de casos

- Fase de muestra creada con el andamio; ida y vuelta (cerrar y reabrir).

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01, CA-02, CA-03 | 100% |
| Media | CA-04 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`: `python -m unittest core.herramientas.tests_fase core.herramientas.tests_cambios`.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-016 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-016 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |
| HU-016 | CA-03 | CP-003 | Funcional | Alta | Sí | ☑ |
| HU-016 | CA-04 | CP-004 | Errores | Media | Sí | ☑ |

## 6. Casos de prueba

### CP-001 · Cerrar

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Cerrar una fase recién llenada | Estado, resultado y funcionalidad escritos con sus casos; dice dónde quedan marcas; la HU y la épica sin cambio |
| 2 | Llenar las marcas y cerrar otra vez | Matriz marcada, cierre del plan escrito, fila de la fase en la HU, HU y épica «Terminada» |
| 3 | Cerrar una tercera vez | Nada cambia: no se duplican filas |

### CP-002 · Reabrir

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Reabrir la fase cerrada con un motivo | Estación 8, HU y épica «En curso», motivo en el estado y en el plan, ciclo 2 con marcas |
| 2 | Cerrar sin llenar el ciclo 2 | No cierra: dice dónde faltan |

### CP-003 · Separar por sesión

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Listar con dos sesiones | Cada una con lo suyo; el archivo de las dos, como compartido |
| 2 | Preparar lo de una | `git diff --cached` trae solo lo suyo |
| 3 | Soltar | `git diff --cached` vacío |

### CP-004 · Rechazos y simulación

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Cerrar una carpeta que no es fase | Error, nada cambia |
| 2 | Cerrar con unas pruebas que fallan | No cierra, nada cambia |
| 3 | Cerrar, reabrir y preparar sin `--aplicar` | Dicen qué harían, nada cambia |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Se pisa lo escrito a mano o se prepara lo de otra sesión | Antes de cerrar la fase |
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
