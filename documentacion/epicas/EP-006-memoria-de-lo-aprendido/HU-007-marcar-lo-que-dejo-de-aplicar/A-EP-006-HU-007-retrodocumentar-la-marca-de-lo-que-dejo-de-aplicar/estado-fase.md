# Estado de fase — Fase A-EP-006-HU-007-retrodocumentar-la-marca-de-lo-que-dejo-de-aplicar (módulo Memoria)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-007-retrodocumentar-la-marca-de-lo-que-dejo-de-aplicar` |
| **Módulo** | Memoria — los cinco estados de [`memoria/esquema.sql`](../../../../../memoria/esquema.sql) |
| **Épica / HU / origen** | [EP-006](../../epica.md) · [HU-007](../HU-007-marcar-lo-que-dejo-de-aplicar.md) · retro-documentación; salió del pendiente [02](../../../../../pendientes/hecho/vigencia-y-poda-de-memoria.md), ya cerrado. Fila de HU-007 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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
| 6 | Ejecución continua | 5 tareas, ninguna empezada | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** Las pruebas corren sobre bases temporales; la base real tiene el aprendizaje del proyecto.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 2 |
| **CA en "No"** | Ninguno todavía. Los dos **corren hoy**; lo que falta es la prueba de los cinco estados, uno por uno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Pendiente | Prueba del reemplazo que conserva y enlaza — CP-001 |
| T-02 | Pendiente | Caso de lo archivado que se sigue leyendo — CP-002 |
| T-03 | Pendiente | Prueba de que la búsqueda no devuelve lo marcado — CP-003 |
| T-04 | Pendiente | Caso de la vigencia — CP-004 |
| T-05 | Pendiente | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 5. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| La prueba comprueba que la **fila siga existiendo**, no solo que no aparezca: no aparecer y no existir se ven igual desde la búsqueda, y la exigencia es que exista | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| La vigencia se prueba con **fechas puestas a mano**: una prueba no puede tardar meses, y atarla a la fecha de hoy la vuelve frágil | §2.6 del plan y riesgo `R-03` |
| Los cinco estados se prueban uno por uno: cada uno tiene su motivo, y **el que no se prueba es el que se rompe en silencio** | §2.6 del plan |
| El enlace del reemplazo se comprueba en los dos sentidos: desde la nueva se llega a la vieja, y desde la vieja se sabe cuál la reemplazó | CP-001 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar: §2.7 no dejó dudas.
- **Si alguno de los cinco estados no funciona como dice** (riesgo `R-01`): se anota y se propone. Un estado que falla pierde memoria en silencio.
- **El módulo de la memoria no tiene especificación aparte.** Es uno de los casos que [EP-001 · HU-010](../../../EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) viene a resolver.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 4 esperando la aprobación del plan, que es la puerta normal, no un bloqueo.
