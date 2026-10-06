# Plan de Pruebas · Fase `A-EP-025-HU-012-retirar-la-telemetria`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU012-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-012: CA-01 y CA-02 |
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
| Unitario | Ruta y retiro | Claude | Base de pruebas y archivos temporales | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01, CA-02 |

### 3.3 Técnicas de diseño de casos

- Una configuración con las seis, otras del usuario y una con otro valor.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01, CA-02 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`: `python manage.py test core.consumo` y `python -m unittest core.herramientas.tests_instalacion core.herramientas.tests_desinstalar`.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-012 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-012 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |

## 6. Casos de prueba

### CP-001 · Cimiento

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `POST /v1/logs` desde esta máquina | 404 |
| 2 | Las pruebas de consumo | Pasan sin el lector de la telemetría |

### CP-002 · Instalación

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Retirar con las seis, otras del usuario y una con otro valor | Salen las seis; las otras y la de otro valor se quedan |
| 2 | Retirar otra vez | Nada que quitar |
| 3 | Simular | Lo dice, nada cambia |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Se quita algo del usuario | Antes de cerrar la fase |
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
