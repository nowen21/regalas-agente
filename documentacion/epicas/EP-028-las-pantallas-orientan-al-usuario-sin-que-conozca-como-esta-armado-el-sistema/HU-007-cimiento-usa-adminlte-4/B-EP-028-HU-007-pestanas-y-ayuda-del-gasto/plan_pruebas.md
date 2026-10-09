# Plan de Pruebas · Fase B-EP-028-HU-007, las pestañas y la ayuda del gasto   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP028-HU007-B |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-007](../HU-007-cimiento-usa-adminlte-4.md), CA-04 y CA-05 |
| **Fecha** | 2026-10-08 |
| **Elaborado por** | El agente |
| **Aprobado por** | El usuario, con la corrección de las pestañas y la ayuda del gasto, el 2026-10-08 |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.consumo core.ayuda`. En el navegador: `node historico-chat/scripts/2026-10-08/ver_pestanas.mjs`, con Cimiento en marcha.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-007 | CA-04 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-007 | CA-05 | CP-002 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 2 de 2 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Las pestañas del gasto funcionan

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir el gasto | Se ve el contenido de la pestaña Resumen, no «Cargando...» |
| 2 | Pulsar cada pestaña en el navegador | Su contenido reemplaza al anterior, la pestaña queda marcada y la dirección cambia |
| 3 | Pedir el tablero con `?pestana=` de cada una | La pestaña pedida sale marcada y es la que se carga |

### CP-002 · Las pestañas del gasto tienen su ayuda

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir cada pestaña y la franja | Cada título, cifra y columna con nombre trae su «?», y ninguna clave queda sin texto |
| 2 | Pulsar un «?» de una pestaña cargada por htmx en el navegador | Abre su globo |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 2, en `resultado_pruebas.md`.
