# Estado de fase — Fase A-EP-006-HU-003-retrodocumentar-la-busqueda-por-palabra (módulo Memoria)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-003-retrodocumentar-la-busqueda-por-palabra` |
| **Módulo** | Memoria — [`memoria/memoria.py`](../../../../../memoria/memoria.py) |
| **Épica / HU / origen** | [EP-006](../../epica.md) · [HU-003](../HU-003-busqueda-por-palabra.md) · retro-documentación, fila de HU-003 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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
| **CA en "No"** | Ninguno todavía. Los dos **corren hoy**; lo que falta es la prueba escrita, y en particular la de sincronía del índice |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Pendiente | Caso de la búsqueda con su ubicación — CP-001 |
| T-02 | Pendiente | Prueba de los acentos — CP-002 |
| T-03 | Pendiente | Prueba de los filtros de tipo y alcance — CP-003 |
| T-04 | Pendiente | Caso de la señal archivada — CP-004 |
| T-05 | Pendiente | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 5. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Se prueba que el índice esté **sincronizado**, no solo que la búsqueda responda: un índice desincronizado responde mal, y eso es peor que no responder | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El caso de lo archivado entra en esta fase porque **no aparecer en la búsqueda** es comportamiento de la búsqueda; marcarlo es de [HU-007](../../HU-007-marcar-lo-que-dejo-de-aplicar/HU-007-marcar-lo-que-dejo-de-aplicar.md) | §2.6 del plan |
| Los acentos se prueban en los dos sentidos: un índice que normaliza solo al guardar, o solo al buscar, pasa la mitad de los casos | CP-002 del [`plan_pruebas.md`](plan_pruebas.md) |
| El caso comprueba que la señal archivada **sigue en la base**: con solo comprobar que no aparece, un programa que borra pasaría igual | CP-004 del `plan_pruebas.md` |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar: §2.7 no dejó dudas.
- **Si la prueba de sincronía destapa un disparador roto** (riesgo `R-01`): es exactamente para lo que sirve. Se anota y se propone el arreglo.
- **Si otra sesión está tocando `memoria/pruebas.py`** (riesgo `R-03`): se guarda solo lo propio.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 4 esperando la aprobación del plan, que es la puerta normal, no un bloqueo.
