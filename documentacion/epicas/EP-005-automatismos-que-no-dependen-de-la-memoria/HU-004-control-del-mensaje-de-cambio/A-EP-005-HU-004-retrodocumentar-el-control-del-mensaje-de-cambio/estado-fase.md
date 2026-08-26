# Estado de fase — Fase A-EP-005-HU-004-retrodocumentar-el-control-del-mensaje-de-cambio (módulo Automatismos)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-004-retrodocumentar-el-control-del-mensaje-de-cambio` |
| **Módulo** | Automatismos — [`validadores/commits.py`](../../../../../validadores/commits.py) |
| **Épica / HU / origen** | [EP-005](../../epica.md) · [HU-004](../HU-004-control-del-mensaje-de-cambio.md) · 🔀 híbrido: la comprobación existe, el disparo no. Fila de HU-004 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** cerrada. **Última puerta pasada:** 9, el commit `c6a775f`.

> **La estación se corrigió el 2026-08-25**, leyendo el historial: el trabajo de esta fase estaba guardado desde hacía tiempo, y lo que faltaba era la marca. El hash sale de `git log` sobre su documento de cierre, no de una suposición.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 presentado el 2026-08-17 | ☑ |
| 5 | Aprobación del plan detallado | 👤 «autorizados los planes de trabajo», 2026-08-17 | ☑ |
| 6 | Ejecución continua | ya estaba construido: se comprobó | ☑ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☑ Cumple, ciclo 1 |
| 8 | Cierre documental | trazabilidad sin faltantes | ☑ |
| 9 | Commit único | 👤 Commit `c6a775f`, verificado en el historial | ☑ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |



---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 2 de 2 |
| **CA en "No"** | Ninguno todavía. Los **dos están a medias de entrada**: la comprobación existe y **nadie la llama al guardar** |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

> **Puesto al día el 2026-08-22.** Este documento decía que no se había ejecutado ninguna tarea, y la fase estaba **hecha y probada**: su [resultado_pruebas](resultado_pruebas.md) trae el veredicto y su [funcionalidad_implementada](funcionalidad_implementada.md) el cierre. Lo que faltaba era este archivo, que es justo el que una sesión nueva lee para saber por dónde va. Sale del [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md).

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | Que la comprobación corra al guardar. Dudas 1 y 2 |
| T-02 | Hecha | Caso del mensaje vacío y el corto informativo — CP-001 |
| T-03 | Hecha | Caso de la firma de la herramienta — CP-003 |
| T-04 | Hecha | Caso del orden del cuerpo — CP-004 |
| T-05 | Hecha | Correr, escribir el incremento de la especificación y cerrar la trazabilidad |

**Hechas:** 5 de 5. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| El disparo se coordina con la fase de [HU-005](../../HU-005-cambio-de-reglas-con-version/HU-005-cambio-de-reglas-con-version.md): dos enganches en el mismo momento se estorban y se ordenan mal. Uno llama a las dos comprobaciones | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| La comprobación a mano **se queda**: correrla antes de guardar sirve para arreglar el mensaje sin que el commit falle | §2.6 del plan |
| Los mensajes viejos no se revisan: el historial es rastro y no se reescribe | §2.6 del plan |
| Un mensaje corto pero informativo tiene que pasar: sin ese caso, la comprobación podría estar midiendo largo en vez de contenido | CP-001 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **Duda 1 de §2.7:** si el disparo es un enganche de la herramienta o del control de versiones — uno viaja con el proyecto, el otro se queda en la máquina.
- **Duda 2 de §2.7:** si un mensaje que no pasa detiene el commit o solo avisa.
- **La aprobación del plan.** Sin ella no se instala el disparo.
- **Si detiene, el rechazo tiene que ser accionable** (riesgo `R-01`): un "no pasa" sin motivo bloquea el trabajo en el peor momento.
- **Cruce con la fase de HU-005** (riesgo `R-02`): las dos necesitan disparar en el mismo momento y se coordinan.

---

## 4. Si se bloqueó

- **Estación:** 6 — ejecución continua, detenida. **Motivo:** el plan **está aprobado** desde el 2026-08-17, y las dos dudas bloquean el disparo, que es lo único que falta construir. **Qué falta para desbloquear:** que el usuario apruebe el plan, diga dónde vive el disparo y si detiene o avisa. Los tres casos de prueba pueden escribirse apenas se apruebe.

---

## Lo que la desbloqueó

**Las dudas de la §2.7 quedaron decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md). La decisión está escrita en el propio plan, con su motivo.

**La fase no arrancó todavía:** decidir no es ejecutar.
