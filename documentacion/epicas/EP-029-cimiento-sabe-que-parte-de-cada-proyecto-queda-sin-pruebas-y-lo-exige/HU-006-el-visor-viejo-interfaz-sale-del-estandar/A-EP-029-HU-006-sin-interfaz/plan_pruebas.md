# Plan de Pruebas · Fase A-EP-029-HU-006, sin interfaz   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP029-HU006-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-006](../HU-006-el-visor-viejo-interfaz-sale-del-estandar.md) |
| **Fecha** | 2026-10-08 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 4 del pendiente 141](../../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-4.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.pruebas.tests_un_programa`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-006 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 1 de 1 exigencias cubiertas = 100%.

## 6. Casos de prueba

### CP-001 · `interfaz/` ya no está y el estándar es un solo programa

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar la carpeta | No existe |
| 2 | Buscar `interfaz/` en `.claude/settings.json` y `anatomia/` | No aparece |
| 3 | Reconocer el lenguaje del estándar | Django, en `proyectos/cimiento` |

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 1, en `resultado_pruebas.md`.
