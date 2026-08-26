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

**Estación actual:** 9 — commit único. **Última puerta pasada:** 8, con la trazabilidad cerrada.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 presentado el 2026-08-17 | ☑ |
| 5 | Aprobación del plan detallado | 👤 «autorizados los planes de trabajo», 2026-08-17 | ☑ |
| 6 | Ejecución continua | 5 tareas, las 5 hechas | ☑ |
| 7 | Pruebas | [`resultado_pruebas.md`](resultado_pruebas.md) con veredicto **No cumple** | ☑ |
| 8 | Cierre documental | [`funcionalidad_implementada.md`](funcionalidad_implementada.md), §8 de la HU y fila del inventario 48 | ☑ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**`memoria.py` no se tocó**, como decía §2.1 del plan — aun cuando la corrida encontró dos defectos que se arreglan con una línea cada uno. Están probados, no parcheados.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **No cumple** |
| **CA cumplidos** | 1 de 2. El RNF y el transversal de no regresión, en «Sí» |
| **CA en "No"** | **CA-01**, en su segunda mitad: lo marcado queda, pero **sin la fecha y sin decir qué lo reemplazó**. Y con él, el transversal de **trazabilidad** |
| **Defectos abiertos aceptados** | 3 — `D-01` el reemplazo no guarda el `--by` ni fecha; `D-02` archivar no deja fecha; `D-03` el plan declaró cobertura completa sin contar los transversales |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) de esta fase |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | **Hecha** | CP-001. Destapó `D-01`: el paso 6 falla |
| T-02 | **Hecha** | CP-002. Destapó `D-02`: el paso 4 falla |
| T-03 | **Hecha** | CP-003, con los cinco estados y el conteo. Pasa |
| T-04 | **Hecha** | CP-004, incluido el borde del huso horario. Pasa |
| T-05 | **Hecha** | Corrida completa (52 pruebas, verde con 4 fallos esperados), resultado escrito y trazabilidad cerrada |

**Hechas:** 5 de 5. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| La prueba comprueba que la **fila siga existiendo**, no solo que no aparezca: no aparecer y no existir se ven igual desde la búsqueda, y la exigencia es que exista | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| La vigencia se prueba con **fechas puestas a mano**: una prueba no puede tardar meses, y atarla a la fecha de hoy la vuelve frágil | §2.6 del plan y riesgo `R-03` |
| Los cinco estados se prueban uno por uno: cada uno tiene su motivo, y **el que no se prueba es el que se rompe en silencio** | §2.6 del plan |
| El enlace del reemplazo se comprueba en los dos sentidos: desde la nueva se llega a la vieja, y desde la vieja se sabe cuál la reemplazó | CP-001 del [`plan_pruebas.md`](plan_pruebas.md) — **y ahí falló**: solo funciona un sentido |
| **`cmd_supersede` imprime el dato y no lo guarda.** Es lo que `13·DOC5` manda evitar, incumplido por el programa que implementa esa regla | `D-01` del [`resultado_pruebas.md`](resultado_pruebas.md) |
| Los dos defectos se prueban con fallo esperado en vez de arreglarse, para no salirse del plan aprobado | §4 del `funcionalidad_implementada` |

---

## 3. Pendiente / preguntas abiertas

- **Los dos arreglos de `memoria.py`**, que no cabían en el plan aprobado: que `cmd_supersede` guarde el `--by` y la fecha (`D-01`), y que archivar deje fecha (`D-02`). Piden una fase `B-EP-006-HU-007` — proponerla es del agente, abrirla es del usuario.
- **El riesgo `R-01` no se materializó:** los cinco estados hacen lo que dicen, y ninguna señal se borró en ningún recorrido.
- **El módulo de la memoria no tiene especificación aparte.** Es uno de los casos que [EP-001 · HU-010](../../../EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) viene a resolver.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 9 esperando la autorización del commit, que es la puerta normal.
