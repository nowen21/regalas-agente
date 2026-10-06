# Plan de Pruebas · Fase `A-EP-025-HU-011-el-vigilante`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU011-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-011: CA-01 a CA-03 |
| **Fecha** | 2026-10-05 |
| **Elaborado por** | Claude |
| **Revisado por** | Ing. José Dúmar Jiménez Ruíz |
| **Aprobado por** | [Análisis 2 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md), el 2026-10-05 |
| **Estado** | Aprobado |

Para una fase, la plantilla pide las secciones 3, 5, 6, 9 y 12; las demás son opcionales y no se usan.

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Integración | Vigilar y guardar | Claude | Base de pruebas en MariaDB | Sí |
| En vivo | El gasto de esta sesión llega solo | Claude | La base real | No |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01 a CA-03 |

### 3.3 Técnicas de diseño de casos

- Un archivo que cambia, uno de un proyecto inactivo, y el vigilante real sobre una carpeta temporal.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01, CA-03 | 100% |
| Media | CA-02 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`: `python manage.py test core.consumo`, y `python -m unittest core.herramientas.tests_desinstalar core.herramientas.tests_instalacion`.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-011 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-011 | CA-02 | CP-002 | Funcional | Media | Sí | ☑ |
| HU-011 | CA-03 | CP-003 | Funcional | Alta | Sí | ☑ |

## 6. Casos de prueba

### CP-001 · Guardar al cambiar

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Cambiar un `.jsonl` de un proyecto activo | Sus llamadas en la base, sin duplicar si se avisa dos veces |
| 2 | Cambiar uno de un proyecto inactivo o desconocido | No se lee |
| 3 | El vigilante real con `watchdog`, sobre una carpeta temporal | Lo escrito llega a la base en menos de 5 segundos |

### CP-002 · Arrancar, detener, instalar

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Guardar el número de un proceso y pedir `--parar` | El proceso termina y el archivo se borra |
| 2 | Arrancar con un número guardado de un proceso vivo | No arranca otro |
| 3 | Desinstalar con el archivo de inicio puesto | El archivo se quita |

### CP-003 · Tablero

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir «Gasto» | No llama al lector de `.jsonl` |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | El gasto no llega, o se duplica | Antes de cerrar la fase |
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
