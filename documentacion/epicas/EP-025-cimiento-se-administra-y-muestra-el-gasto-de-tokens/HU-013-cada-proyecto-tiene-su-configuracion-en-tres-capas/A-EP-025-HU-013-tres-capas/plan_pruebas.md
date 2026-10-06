# Plan de Pruebas · Fase `A-EP-025-HU-013-tres-capas`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU013-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-013: CA-01 a CA-03 |
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
| Integración | Capas, suspensiones, copia | Claude | Base de pruebas en MariaDB | Sí |
| Pantallas | Lo que ve y guarda cada cuenta | Claude | Cliente de pruebas de Django | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01 a CA-03 |
| Seguridad | ☑ | Solo el administrador cambia; el núcleo y el histórico no se suspenden |

### 3.3 Técnicas de diseño de casos

- Cada capa vacía y llena; suspensión vigente, vencida y levantada; bordes de 30 días.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01, CA-02 | 100% |
| Media | CA-03 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`: `python manage.py test core.proyectos core.niveles core.consumo`, y `python -m unittest core.enganches.tests_limites core.enganches.tests_freno` importando `core.validadores` primero.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-013 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-013 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |
| HU-013 | CA-03 | CP-003 | Funcional | Media | Sí | ☑ |

## 6. Casos de prueba

### CP-001 · Base y proyecto

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer un ajuste sin valor en ninguna capa | El de fábrica |
| 2 | Con valor en la base | El de la base |
| 3 | Con valor en el proyecto, y cambiar la base | El del proyecto |
| 4 | Sin base de datos | El de fábrica |
| 5 | El administrador guarda «Configuración» y los ajustes del proyecto; la consulta solo mira | Se guardan; la consulta recibe 403 al enviar |
| 6 | Un valor fuera de lo permitido | No se guarda nada |

### CP-002 · Suspender y levantar

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Suspender `02·F8` y leer los niveles | «apagada» mientras dure |
| 2 | Suspender el freno entero | Todo «apagada» menos el núcleo |
| 3 | Levantar, o dejar vencer | Vuelve a su nivel |
| 4 | Suspender `00·N6`, otra del núcleo o el histórico; sin motivo; por más de 30 días; con fecha pasada | Se rechaza, nada cambia |

### CP-003 · Copia y límites

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Guardar la base, el proyecto o una suspensión | `.agente/configuracion.md` dice lo que vale |
| 2 | Leer los límites | Los de los ajustes |
| 3 | La migración con un proyecto que tenía límites propios | Quedan en sus ajustes |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Se suspende el núcleo o el histórico, o se pierde un límite | Antes de cerrar la fase |
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
