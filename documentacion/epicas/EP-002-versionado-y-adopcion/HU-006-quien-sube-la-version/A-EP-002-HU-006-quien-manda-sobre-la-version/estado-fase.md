# Estado de fase — Fase A-EP-002-HU-006-quien-manda-sobre-la-version (módulo Versionado y adopción)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-002-HU-006-quien-manda-sobre-la-version` |
| **Módulo** | Versionado y adopción — el acuerdo sobre quién toca [`VERSION`](../../../../../VERSION) y el [`CHANGELOG`](../../../../../CHANGELOG.md) |
| **Épica / HU / origen** | [EP-002](../../epica.md) · [HU-006](../HU-006-quien-sube-la-version.md) · ✨ funcionalidad nueva, bajada del pendiente [22](../../../../../pendientes/22-dos-sesiones-versionando-a-la-vez.md) por [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md). Fila de HU-006 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 6 — ejecución continua, **lista para arrancar**. **Última puerta pasada:** 5, el plan aprobado por el usuario el 2026-08-17 («autorizados los planes de trabajo»).

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 presentado el 2026-08-17 | ☑ |
| 5 | Aprobación del plan detallado | 👤 «autorizados los planes de trabajo», 2026-08-17 | ☑ |
| 6 | Ejecución continua | 7 tareas · **detenida por las 3 dudas de §2.7** | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** Acá no hay nada construido que retrodocumentar: ninguna regla dice hoy quién manda sobre `VERSION`.

> **El plan quedó aprobado el 2026-08-17** y la fase **no arrancó**: las 3 dudas de §2.7 del plan sigue sin resolver, y solo la puede resolver el usuario. Lo que falta ya no es la aprobación — es la respuesta.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 2 |
| **CA en "No"** | Los dos están en «No» **de entrada**, y por eso existe la fase: el 2026-08-14 quedaron dos numeraciones vivas, y desde entonces volvió a pasar tres veces |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Bloqueada | Escribir la regla. Las tres dudas la bloquean |
| T-02 | Bloqueada | Revisar si `M10` queda tocada por el momento nuevo |
| T-03 | Bloqueada | Caso de las dos sesiones simuladas — CP-001 |
| T-04 | Bloqueada | Caso del guardado con trabajo ajeno en el árbol — CP-003 |
| T-05 | Pendiente | Escribir los cuatro casos ocurridos. **Son hechos: no dependen de la decisión** |
| T-06 | Bloqueada | Recuento de entradas del registro — CP-005 |
| T-07 | Bloqueada | Clasificar, versionar, cerrar el pendiente 22 y la trazabilidad |

**Hechas:** 0 de 7. **Bloqueadas:** todas menos T-05.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Los cuatro casos ocurridos van al resultado como evidencia: una regla de convivencia sin los casos que la motivaron se vuelve a discutir cada vez | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El tramo de las dos numeraciones no se corrige: el registro es rastro, y renumerar rompe toda cita hecha a esas versiones | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| La regla se valida contra el 2026-08-14, no contra sí misma: si aplicada a ese día no resuelve el cruce, no sirve | CP-002 del [`plan_pruebas.md`](plan_pruebas.md) |
| Si la regla no se puede comprobar con un programa, se declara así: una regla honesta sobre lo que no comprueba vale más que una comprobación falsa | Riesgo `R-03` del plan |

---

## 3. Pendiente / preguntas abiertas

- **Duda 1 de §2.7:** cuál de las tres salidas del pendiente [22](../../../../../pendientes/22-dos-sesiones-versionando-a-la-vez.md) — subir la versión al guardar; entradas separadas que se juntan al guardar; o una sola sesión a la vez sobre el estándar.
- **Duda 2 de §2.7:** si el acuerdo cubre cualquier archivo único compartido o queda acotado a `VERSION` y al registro.
- **Duda 3 de §2.7:** en qué capítulo cae la regla, según lo que resuelvan las dos anteriores.
- **La aprobación del plan.** Sin ella no se escribe la regla.
- **Si la salida elegida obliga a tocar `M10`** (riesgo `R-01`): se declara antes de tocarla, y si es más que una nota, se propone como fase aparte.

---

## 4. Si se bloqueó

- **Estación:** 4 — pausa y presentación. **Motivo:** las tres dudas bloquean toda la construcción; solo la escritura de los cuatro casos ocurridos puede avanzar. **Qué falta para desbloquear:** que el usuario apruebe el plan y elija la salida de la duda 1, de la que dependen las otras dos.

---

## Lo que la desbloqueó

**Las dudas de la §2.7 quedaron decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md). La decisión está escrita en el propio plan, con su motivo.

**La fase no arrancó todavía:** decidir no es ejecutar.
