# Plan de Pruebas · Fase D-EP-025-HU-032, la pantalla en pestañas   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU032-D |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-032](../HU-032-cada-momento-de-cada-enganche-y-cada-revision-de-git-se-puede-suspender.md) |
| **Fecha** | 2026-10-09 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 3 del pendiente 149](../../../../../historico-chat/resumenes/2026-10-08/pendientes/149-cada-enganche-se-puede-suspender-desde-cimiento/analisis-3.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`: `manage.py test core.proyectos.tests_suspender_enganches core.proyectos.tests_configuracion core.ayuda`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-032 | CA-04 | CP-008 | Funcional | Alta | Sí | ☑ |
| HU-032 | CA-04 | CP-009 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 1 de 1 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-008 · Las tres pestañas y sus tablas

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir la pantalla con una cuenta de administrador | Salen las pestañas «Suspensiones» (activa), «Reglas» y «Enganches» |
| 2 | Mirar la pestaña «Reglas» | Una tabla con `data-tabla-avanzada` que trae `02·F8` |
| 3 | Mirar la pestaña «Enganches» | Una tabla con `data-tabla-avanzada` que trae `historico-del-usuario` y su advertencia |

### CP-009 · El botón y el modal

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir la pantalla con una cuenta de administrador | El botón «Suspender» abre el modal `#suspender` |
| 2 | Suspender con un nombre que no existe | La página vuelve con el modal abierto y el error |
| 3 | Abrir la pantalla con una cuenta de consulta | No sale el botón ni el modal |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 2, en `resultado_pruebas.md`.
