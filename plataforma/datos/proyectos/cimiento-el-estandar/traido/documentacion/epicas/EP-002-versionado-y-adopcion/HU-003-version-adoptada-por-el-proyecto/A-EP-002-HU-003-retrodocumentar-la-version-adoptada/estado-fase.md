# Estado de fase — Fase A-EP-002-HU-003-retrodocumentar-la-version-adoptada (módulo Versionado y adopción)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-002-HU-003-retrodocumentar-la-version-adoptada` |
| **Módulo** | Versionado y adopción — la declaración del [`CLAUDE.md.plantilla`](../../../../../plantillas/CLAUDE.md.plantilla), [`version.py`](../../../../../validadores/version.py) y el historial de [`documentacion/versiones/`](../../../../versiones/README.md) |
| **Épica / HU / origen** | [EP-002](../../epica.md) · [HU-003](../HU-003-version-adoptada-por-el-proyecto.md) · retro-documentación, fila de HU-003 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** cerrada con **No cumple**. **Última puerta pasada:** 11, el cierre documental.

> **La fase se cerró el 2026-08-27 con veredicto «No cumple».** Cerrar no es aprobar: es dejar escrito qué salió. El criterio en rojo y adónde fue a parar están en el [funcionalidad_implementada.md](funcionalidad_implementada.md).

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 presentado el 2026-08-17 | ☑ |
| 5 | Aprobación del plan detallado | 👤 «autorizados los planes de trabajo», 2026-08-17 | ☑ |
| 6 | Ejecución continua | 8 tareas · **dudas decididas el 2026-08-18** | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** La fase trabaja sobre una **copia** del proyecto elegido, y no modifica ningún validador.

> **El plan quedó aprobado el 2026-08-17** y la fase **no arrancó**: la duda 1 de §2.7 del plan sigue sin resolver, y solo la puede resolver el usuario. Lo que falta ya no es la aprobación — es la respuesta.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **No cumple** |
| **CA cumplidos** | 2 de 3 |
| **CA en "No"** | **CA-02.** Una versión inventada pasa, y si es mayor que la vigente apaga el aviso de desfase |
| **Defectos abiertos aceptados** | D-01 y D-02, los dos en el [pendiente 82](../../../../../pendientes/hecho/la-version-adoptada-no-se-comprueba-contra-nada.md). El D-03, los dos nombres de la carpeta en la plantilla, se corrigió acá mismo |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §5 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Bloqueada | Caso de la declaración leída — CP-001. Duda 1 |
| T-02 | Pendiente | Constancia del propio estándar, que no declara versión y recibe aviso |
| T-03 | Pendiente | Prueba de la versión que no existe en el registro — CP-002 |
| T-04 | Pendiente | Caso de la versión inventada en copia — CP-003 |
| T-05 | Bloqueada | Caso de la reconstrucción desde el historial — CP-004. Duda 1 |
| T-06 | Pendiente | Anotar contra los pendientes 44 y 46 lo que se encuentre mal |
| T-07 | Bloqueada | Comprobar dónde vive el registro de adopciones — CP-005. Duda 1 |
| T-08 | Pendiente | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 8. **Bloqueadas:** T-01, T-05 y T-07.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| La lista de versiones que existieron se lee del `CHANGELOG`: dos listas de lo mismo se separan solas | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El registro de adopciones se mide, no se arregla: ya tiene sus dos pendientes abiertos, y uno lo reportó otro proyecto | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Un historial que existe pero no permite decir bajo qué versión cerró una fase no cumple el CA-03. Por eso el caso lo **usa** en vez de mirar si el archivo está | CP-004 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **Duda 1 de §2.7:** sobre qué proyecto instalado se prueban el CA-01 y el CA-03. Bloquea tres tareas.
- **La aprobación del plan.** Sin ella no arranca la ejecución.
- **El CA-02 puede no cerrarse sin tocar `version.py`** (riesgo `R-01`). Si es así, **se para y se propone** con el plan ampliado: cambiar un validador no es de esta fase.
- **Los pendientes [44](../../../../../pendientes/hecho/el-registro-no-se-escribe-si-no-cambia-la-huella.md) y [46](../../../../../pendientes/hecho/el-registro-se-escribe-antes-de-contarse.md)** siguen abiertos sobre el registro de adopciones. Esta fase les produce evidencia; no los cierra.
- **El propio estándar no declara versión adoptada** y recibe el aviso. Queda como hallazgo escrito, no silenciado.

---

## 4. Si se bloqueó

- **Estación:** 6 — ejecución continua, detenida. **Motivo:** el plan **está aprobado** desde el 2026-08-17, y sin el proyecto de la duda 1 no arrancan el CA-01 ni el CA-03. **Qué falta para desbloquear:** que el usuario apruebe el plan y elija el proyecto. El CA-02 puede arrancar apenas se apruebe.

---

## Lo que la desbloqueó

**Las dudas de la §2.7 quedaron decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md). La decisión está escrita en el propio plan, con su motivo.

**La fase no arrancó todavía:** decidir no es ejecutar.
