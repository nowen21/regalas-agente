# Estado de fase — Fase A-EP-006-HU-001-retrodocumentar-que-se-guarda-y-con-que-alcance (módulo Memoria)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-001-retrodocumentar-que-se-guarda-y-con-que-alcance` |
| **Módulo** | Memoria — [`memoria/esquema.sql`](../../../../../memoria/esquema.sql) y [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md) |
| **Épica / HU / origen** | [EP-006](../../epica.md) · [HU-001](../HU-001-que-se-guarda-tipos-y-alcances.md) · retro-documentación, fila de HU-001 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 4 — pausa y presentación. **Última puerta pasada:** 3, con el plan de trabajo y el plan de pruebas escritos.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 pendiente: falta presentarlo | ☐ |
| 5 | Aprobación del plan detallado | 👤 pendiente | ☐ |
| 6 | Ejecución continua | 4 tareas, ninguna empezada | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** El esquema no se toca: quitar un tipo rompería las señales que ya lo tienen.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 2 |
| **CA en "No"** | Ninguno todavía. Los dos **se cumplen hoy**; lo que falta es la prueba escrita |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Pendiente | Caso de las cinco decisiones reales — CP-001 |
| T-02 | Pendiente | Prueba del esquema: sin tipo no entra, sin alcance entra con el de proyecto — CP-002 |
| T-03 | Pendiente | Tabla de los diez tipos con su uso real — CP-003 |
| T-04 | Pendiente | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 4. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Los tipos que no se usan se **anotan, no se quitan**: quitar un tipo rompe las señales que ya lo tienen, y ninguna se borra | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El criterio se prueba con decisiones reales de fases cerradas: las reales son las que cuesta clasificar, y los ejemplos inventados siempre caen claros | §2.6 del plan |
| Las pruebas corren sobre base temporal: la base real tiene el aprendizaje del proyecto | §2.6 del plan y riesgo `R-02` |
| Una decisión que no se pueda clasificar vale más que un cinco de cinco forzado: dice dónde al criterio le falta | CP-001 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar: §2.7 no dejó dudas.
- **El módulo de la memoria no tiene especificación aparte.** Es uno de los casos que [EP-001 · HU-010](../../../EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) viene a resolver.
- **Si la mitad de los tipos no se usa nunca** (riesgo `R-01`): se anota con la cuenta. Simplificar el esquema lo decide el usuario.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 4 esperando la aprobación del plan, que es la puerta normal, no un bloqueo.
