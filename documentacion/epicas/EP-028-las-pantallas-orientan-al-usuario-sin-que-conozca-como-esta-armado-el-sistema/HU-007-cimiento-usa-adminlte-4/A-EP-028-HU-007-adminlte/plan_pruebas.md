# Plan de Pruebas · Fase A-EP-028-HU-007, AdminLTE   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP028-HU007-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-007](../HU-007-cimiento-usa-adminlte-4.md) |
| **Fecha** | 2026-10-07 |
| **Elaborado por** | El agente |
| **Aprobado por** | El usuario, con «Hágalo si la reemplaza», el 2026-10-07 |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.inicio core.estandar core.historia core.proyectos core.niveles core.consumo core.ayuda core.cuentas`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-007 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-007 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |
| HU-007 | CA-03 | CP-003 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 3 de 3 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Las pantallas usan AdminLTE

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir el inicio, el estándar, la historia, los proyectos y el gasto | Cargan AdminLTE y Bootstrap, no Tabler, y traen `app-wrapper`, `app-header`, `app-sidebar` y `app-main` |
| 2 | Abrir la página de entrada sin sesión | Es la página de entrada de AdminLTE |

### CP-002 · El menú y sus submenús llevan íconos

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir el inicio | Cada `nav-link` del menú lateral trae su ícono `bi` |

### CP-003 · Ninguna clase de Tabler queda

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar las clases propias de Tabler en las plantillas y en `presentar.py` | Ninguna |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 3, en `resultado_pruebas.md`.
