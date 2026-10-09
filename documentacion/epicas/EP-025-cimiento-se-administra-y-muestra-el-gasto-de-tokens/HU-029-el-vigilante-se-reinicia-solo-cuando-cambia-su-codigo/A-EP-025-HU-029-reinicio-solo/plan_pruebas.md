# Plan de Pruebas · Fase A-EP-025-HU-029, el reinicio solo   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU029-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-029](../HU-029-el-vigilante-se-reinicia-solo-cuando-cambia-su-codigo.md) |
| **Fecha** | 2026-10-08 |
| **Elaborado por** | El agente |
| **Aprobado por** | El usuario, con «apruebo» a la opción 1, el 2026-10-08 |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde la raíz: `manage.py test core.consumo`. En esta máquina, con el vigilante corriendo: cambiar un `.py` de Cimiento y ver que el número de proceso cambia.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-029 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-029 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 2 de 2 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Un cambio de código reinicia el vigilante

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Avisar el cambio de un `.py` de `core/` | Cuenta como código |
| 2 | Avisar una prueba, algo de `.venv`, `__pycache__`, `node_modules`, `.agente` o `.git`, o un `.html` | No cuenta |
| 3 | Avisar varios cambios seguidos | Un solo reinicio, después de la calma |
| 4 | Con `watchdog` de verdad, escribir un `.py` en la carpeta vigilada | Llega el aviso de código |

### CP-002 · El relevo no deja al consumo sin vigilante

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Reiniciar con un nuevo que escribe su número | El viejo se detiene |
| 2 | Reiniciar con un nuevo que no escribe su número | El viejo sigue, vuelve a escribir el suyo y anota por qué |
| 3 | En esta máquina, cambiar un `.py` con el vigilante corriendo | El número de proceso cambia y sigue habiendo uno solo |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 2, en `resultado_pruebas.md`.
