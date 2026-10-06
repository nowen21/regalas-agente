# Plan de Pruebas · Fase `A-EP-025-HU-017-guiones-repetidos`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU017-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-017: CA-01 y CA-02 |
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
| Unitario | Detener y avisar | Claude | Carpetas temporales | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01, CA-02 |

### 3.3 Técnicas de diseño de casos

- Un guion por cada tarea que Cimiento hace; nombres con y sin número; textos parecidos y distintos.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01 | 100% |
| Media | CA-02 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`, importando `core.validadores` primero: `core.enganches.tests_guiones` y `core.enganches.tests_freno`.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-017 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-017 | CA-02 | CP-002 | Funcional | Media | Sí | ☑ |

## 6. Casos de prueba

### CP-001 · Detener

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Un guion que escribe `estado-fase.md` y `resultado_pruebas.md` | Se detiene y nombra `manage.py cerrar_fase` |
| 2 | Uno que lee `historico-chat/.tocado` | Nombra `manage.py cambios_por_sesion` |
| 3 | Uno que mueve a `pendientes/hecho/` | Nombra `cerrar.py` |
| 4 | Un `.py` fuera de `historico-chat/scripts/` con esas señales | No se mira |

### CP-002 · Avisar

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `medir_algo_2.py` con `medir_algo_1.py` anterior | Avisa, nombra el anterior, deja escribir |
| 2 | Un guion con casi el mismo texto de otro, con otro nombre | Avisa |
| 3 | Uno distinto | Pasa sin aviso |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Se detiene un guion que no repite nada | Antes de cerrar la fase |
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
