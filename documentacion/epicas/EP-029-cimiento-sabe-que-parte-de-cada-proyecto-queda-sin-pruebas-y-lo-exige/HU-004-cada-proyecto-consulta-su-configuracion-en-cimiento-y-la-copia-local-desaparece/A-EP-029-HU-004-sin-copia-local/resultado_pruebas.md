# Resultado de Pruebas · Fase `A-EP-029-HU-004-sin-copia-local`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-029-HU-004-sin-copia-local` |
| **HU** | [HU-004](../HU-004-cada-proyecto-consulta-su-configuracion-en-cimiento-y-la-copia-local-desaparece.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-08 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | La base de pruebas de Django sobre MariaDB; versión 56.8.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `tests_configuracion.py`, `tests_opt_in.py` y `LaAyudaNoNombraLaCopia` | Guardar no escribe la copia; la ayuda no la nombra | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `VolverAInstalarBorraLaCopiaVieja` | La borra y lo dice; sin copia, nada | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 2 casos en el plan, 2 acá.

**Qué salió distinto de lo esperado:** nada.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que nada siga importando la copia | Búsqueda de `proyectos import copia` en `core/` | Ninguno |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| RNF-01 | La regresión de `core.proyectos` | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los dos criterios tienen su caso aprobado y la regresión pasa entera.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `manage.py test core.proyectos core.ayuda core.herramientas.tests_instalacion`: Ran 299 tests, OK |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-08 | 2 | 0 | Primera ejecución |
