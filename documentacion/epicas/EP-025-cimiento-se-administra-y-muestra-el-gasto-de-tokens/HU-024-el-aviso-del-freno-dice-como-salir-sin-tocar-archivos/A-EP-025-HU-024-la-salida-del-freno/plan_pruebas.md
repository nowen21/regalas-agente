# Plan de Pruebas · Fase `A-EP-025-HU-024-la-salida-del-freno`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU024-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-024: CA-01 a CA-03 |
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
| Unitario | Aviso, sesión y `cd` | Claude | Carpetas temporales | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01 a CA-03 |
| Seguridad | ☑ | El freno no deja pasar de más |

### 3.3 Técnicas de diseño de casos

- Dos sesiones con análisis distintos; órdenes con y sin `cd`.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-02, CA-03 | 100% |
| Media | CA-01 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`, importando `core.validadores` primero: `core.enganches.tests_freno_salida` y `core.enganches.tests_freno`.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-024 | CA-01 | CP-001 | Funcional | Media | Sí | ☑ |
| HU-024 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |
| HU-024 | CA-03 | CP-003 | Funcional | Alta | Sí | ☑ |

## 6. Casos de prueba

### CP-001 · El aviso

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Detener por `02·F8` | El aviso nombra las herramientas que deshacen y «Suspensiones» con su dirección |
| 2 | Detener por una regla del núcleo | Dice que no se suspende |

### CP-002 · La sesión

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | La sesión A con un análisis que nombra `a.py` «de una»; la B con otro que nombra `b.py` | El freno de A deja crear `a.py` y detiene `b.py`; el de B al revés |
| 2 | Sin sesión | Igual que antes: la fila más reciente |

### CP-003 · El `cd`

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `cd sub && rm x.txt` | Resuelve `sub/x.txt` |
| 2 | `cd /c/... && …` y `cd ..` | Resuelven desde donde quedó |
| 3 | Sin `cd` | Desde la carpeta de la sesión, como antes |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | El freno deja pasar lo que no está autorizado | Antes de cerrar la fase |
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
