# Estado de fase — Fase A-EP-005-HU-005-el-cambio-de-reglas-no-se-guarda-sin-version (módulo Automatismos)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-005-el-cambio-de-reglas-no-se-guarda-sin-version` |
| **Módulo** | Automatismos — el disparo al guardar, sobre [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md) |
| **Épica / HU / origen** | [EP-005](../../epica.md) · [HU-005](../HU-005-cambio-de-reglas-con-version.md) · ✨ funcionalidad nueva. Fila de HU-005 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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
| 6 | Ejecución continua | 5 tareas · **detenida por las 2 dudas de §2.7** | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** Un enganche que puede trabar el guardado no se instala sin aprobación.

> **El plan quedó aprobado el 2026-08-17** y la fase **no arrancó**: las 2 dudas de §2.7 del plan sigue sin resolver, y solo la puede resolver el usuario. Lo que falta ya no es la aprobación — es la respuesta.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 2 |
| **CA en "No"** | Los **dos están en «No» de entrada**: hoy nada impide guardar un cambio de reglas sin versión |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Bloqueada | Que al guardar se exija entrada y subida si el cambio toca reglas. Dudas 1 y 2 |
| T-02 | Pendiente | Caso del cambio de regla sin versión — CP-001 |
| T-03 | Bloqueada | Que el enganche se calle con lo que no toca reglas |
| T-04 | Pendiente | Caso del cambio que no toca reglas — CP-003 |
| T-05 | Pendiente | Correr, escribir el incremento de la especificación y cerrar la trazabilidad |

**Hechas:** 0 de 5. **Bloqueadas:** T-01 y T-03.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| El enganche mira **los archivos** del cambio, no el mensaje: el mensaje lo escribe quien guarda, los archivos son un hecho | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Comprueba que **haya** entrada y subida, no que el tipo sea el correcto: juzgar si un cambio obliga a migrar es criterio, y un enganche equivocado trabaría cambios legítimos | §2.6 del plan |
| El CA-02 pesa más que el CA-01: casi todos los cambios no tocan reglas, y si el enganche los molesta se apaga | §3 del [`plan_pruebas.md`](plan_pruebas.md) |
| El caso mezclado —una regla y documentación en el mismo cambio— es donde una decisión mal hecha se cae | CP-002 del `plan_pruebas.md` |

---

## 3. Pendiente / preguntas abiertas

- **Duda 1 de §2.7:** si detiene el commit o solo avisa, y si eso puede depender del tipo de cambio.
- **Duda 2 de §2.7:** si esta fase va después de [HU-004](../../HU-004-control-del-mensaje-de-cambio/HU-004-control-del-mensaje-de-cambio.md), que crea el disparo, o si esta lo crea y aquella se suma.
- **La aprobación del plan.** Sin ella no se instala el enganche.
- **Coordinación con [EP-002 · HU-006](../../../EP-002-versionado-y-adopcion/HU-006-quien-sube-la-version/HU-006-quien-sube-la-version.md)** (riesgo `R-01`): si allá se decide cambiar el momento de subir la versión, este enganche cambia con ella.
- **Si el archivo de regla entró en otro commit** (riesgo `R-03`): el enganche no lo ve. Se escribe qué caso queda fuera.

---

## 4. Si se bloqueó

- **Estación:** 6 — ejecución continua, detenida. **Motivo:** el plan **está aprobado** desde el 2026-08-17, y las dos dudas bloquean el enganche entero. **Qué falta para desbloquear:** que el usuario apruebe el plan, decida si detiene o avisa y en qué orden va respecto de HU-004. Los dos casos de prueba pueden escribirse apenas se apruebe.

---

## Lo que la desbloqueó

**Las dudas de la §2.7 quedaron decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md). La decisión está escrita en el propio plan, con su motivo.

**La fase no arrancó todavía:** decidir no es ejecutar.
