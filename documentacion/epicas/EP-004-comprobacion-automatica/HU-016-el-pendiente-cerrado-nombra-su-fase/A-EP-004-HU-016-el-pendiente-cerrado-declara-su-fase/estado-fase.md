# Estado de fase — Fase A-EP-004-HU-016-el-pendiente-cerrado-declara-su-fase (módulo Comprobación automática)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-016-el-pendiente-cerrado-declara-su-fase` |
| **Módulo** | Comprobación automática — [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) y [`pendientes/hecho/`](../../../../../pendientes/README.md) |
| **Épica / HU / origen** | [EP-004](../../epica.md) · [HU-016](../HU-016-el-pendiente-cerrado-nombra-su-fase.md) · ✨ funcionalidad nueva. Fila de HU-016 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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
| 6 | Ejecución continua | 9 tareas · **detenida por las 2 dudas de §2.7** | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |



---

> **Puesto al día el 2026-08-22.** La fase estaba detenida esperando dudas que solo el usuario podía contestar, y hoy las contesta el propio repositorio: quedan escritas en el §0.1 del [resultado_pruebas](resultado_pruebas.md). Se corrieron los casos y se cerró. Sale del [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md). Construida: `pendientes.py` gana la comprobación hacia abajo, y midió 24 cerrados sin fase.

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 1 de 1 |
| **CA en "No"** | Los **cuatro están en «No» de entrada**: la regla existe y ningún programa la comprueba |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | Comprobación de que el pendiente cerrado declara su fase. Dudas 1 y 2 |
| T-02 | Hecha | Caso del pendiente sin fase — CP-001. El caso se escribe antes |
| T-03 | Hecha | Resolver la fase declarada contra el árbol |
| T-04 | Hecha | Caso de la fase inventada — CP-002 |
| T-05 | Hecha | Que el pendiente declare que no fue desarrollo |
| T-06 | Hecha | Caso del pendiente cerrado por decisión — CP-003 |
| T-07 | Hecha | Separar lo cerrado antes del corte. Duda 1 |
| T-08 | Hecha | Anotar cuáles pendientes quedan de cada lado |
| T-09 | Hecha | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 9 de 9. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| La fecha de corte se escribe en la documentación del programa: deducirla del historial la vuelve frágil, porque un archivo movido cambiaría la fecha | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El pendiente que no fue desarrollo lo declara él mismo. Adivinar por prosa produce falsos positivos, y un falso positivo apaga el programa | §2.6 del plan |
| La fase declarada se resuelve contra el árbol: una fase que no existe es una promesa de trazabilidad que nadie puede seguir | §2.6 del plan y riesgo `R-03` |
| Sin el CA-04, el primer día el programa reportaría todos los pendientes ya cerrados y nadie lo volvería a correr | Riesgo `R-01` y CP-004 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **Duda 1 de §2.7:** cuál es la fecha de corte — desde cuándo se exige que el pendiente cerrado nombre su fase.
- **Duda 2 de §2.7:** dónde se declara — una línea fija al principio del pendiente, o una sección.
- **La aprobación del plan.** Sin ella no se escribe el validador.
- **Una fase renombrada produce un falso positivo legítimo** (riesgo `R-02`): sale como aviso, y arreglar la cita es del pendiente [54](../../../../../pendientes/hecho/cerrar-un-pendiente-arrastra-sus-citas.md).
- **Cruce con la fase de [HU-018](../../HU-018-numero-de-pendiente-ya-tomado/A-EP-004-HU-018-el-numero-de-pendiente-libre/plan_trabajo.md)**, que puede crear el mismo archivo de validador. La que llegue segunda se suma en vez de reescribir.

---

## 4. Si se bloqueó

- **Estación:** 6 — ejecución continua, detenida. **Motivo:** el plan **está aprobado** desde el 2026-08-17, y las dos dudas bloquean todo lo que se construye. **Qué falta para desbloquear:** que el usuario apruebe el plan, fije la fecha de corte y diga dónde se declara la fase. Los tres casos de prueba pueden escribirse apenas se apruebe.

---

## Lo que la desbloqueó

**Las dudas de la §2.7 quedaron decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md). La decisión está escrita en el propio plan, con su motivo.

**La fase no arrancó todavía:** decidir no es ejecutar.
