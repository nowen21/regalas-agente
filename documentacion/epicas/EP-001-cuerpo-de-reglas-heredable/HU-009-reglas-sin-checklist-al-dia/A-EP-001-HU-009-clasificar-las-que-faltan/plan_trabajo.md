# Plan de Trabajo — Fase «A-EP-001-HU-009-clasificar-las-que-faltan» (módulo «Cuerpo de reglas»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Se escribe **antes** de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-001-HU-009-clasificar-las-que-faltan` |
| **Épica** | [EP-001 Cuerpo de reglas heredable](../../epica.md) |
| **HU** | [HU-009 — Poner al día las reglas que no pasan su propio checklist](../HU-009-reglas-sin-checklist-al-dia.md) — **una sola** (`F12.1`) |
| **Módulo** | Cuerpo de reglas (`validadores/reglas-validables.md`) |
| **Fecha apertura** | 2026-08-16 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- 📝 **Modifica fase(s):** ninguna. La HU-009 no tenía fases.
- ✨ **Funcionalidad nueva:** ninguna. Es completar un registro.

**De dónde sale:** el [pendiente 19](../../../../../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md). El validador de meta-reglas midió por primera vez el propio cuerpo de reglas y encontró tres deudas: **129 reglas sin bloque de checklist**, **7 publicadas en «no cumple»** y **33 sin clasificar** en el registro de lo validable.

**CA de la HU que cubre esta fase:**

| CA de `HU-009` que cierra esta fase | Estado |
|---|---|
| [CA-02 — Toda regla aparece clasificada](../HU-009-reglas-sin-checklist-al-dia.md#ca-02--toda-regla-aparece-clasificada) | ☐ |

**Los otros dos CA no entran, y se dice por qué.** El `CA-01` —las siete en «no cumple»— pide una decisión que no es del agente: corregirlas cambia lo que el estándar exige, y eso lo decide quien define el estándar. El `CA-03` —las 129 sin bloque— es trabajo largo y por capítulo, y la propia HU lo plantea así. Esta fase cierra **la parte que es mecánica y no depende de nadie**, que es exactamente como el pendiente propone partirlo.

---

## 1. Objetivo y alcance

**Objetivo:** que ninguna regla del estándar quede fuera del registro que dice si se puede comprobar sola. Hoy hay 33 que no aparecen, incluidos los capítulos `18` y `19` **completos**.

**Fuera de alcance:**

- **Escribir los validadores que faltan.** Clasificar no es construir; lo construido vive en el pendiente 01.
- **Las siete en «no cumple»** y **las 129 sin bloque**, por lo dicho arriba.
- **Revisar la clasificación de las que ya están.** El registro es una foto del 2026-08-05 y se respeta.

---

## 2. Análisis previo — línea base verificada

### 2.1 Archivos que se crean o modifican

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/reglas-validables.md` | Modificar | Registro | Las 33 filas y el conteo |
| `documentacion/.../HU-009-reglas-sin-checklist-al-dia.md` | Modificar | HU | La fase en §8, tareas y bitácora |
| `pendientes/19-...md` | Modificar | Backlog | Queda abierto con lo que falta, no se cierra |
| `CHANGELOG.md` · `VERSION` | Modificar | Versionado | PARCHE |

**Verificado el 2026-08-16 corriendo el validador de meta-reglas sobre este repositorio:**

- **33 sin clasificar**, y son estas: `C2` a `C16` (quince de conducta), `G9`, `M15`, `F4`, `F12`, `DP1` a `DP8` y `OB1` a `OB6`.
- Los capítulos `18` (despliegue) y `19` (observabilidad) no aparecen en el registro **ni una sola vez**: nacieron después de la foto.
- El registro tiene tres listas —✅ ya son validadores · 🟡 validables, faltan · 🔴 no validables— y un conteo al principio que hay que corregir con ellas.

### 2.2 Matriz de dependencias del cambio

| Quién | Impacto |
|---|---|
| El validador de meta-reglas | Deja de reportar 33 hallazgos de `M9` |
| El pendiente 01 | Su lista de validadores por construir crece con los 🟡 nuevos |
| Las reglas | Ninguno: no se toca el texto de ninguna |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Las quince reglas de conducta van a **no validables** | Intentar comprobar alguna | Son cómo se porta el agente en la conversación, no algo que quede escrito en disco. Un programa no puede decir si «se quedó en su tarea» |
| `M15` va a **ya son validadores** | Dejarla en 🟡 | El validador ya reporta «la cita X no lleva enlace»; está construido y corriendo |
| `F12` va a **ya son validadores** | Dejarla en 🟡 | `fases.py` comprueba su nomenclatura, su unicidad y su ruta física |
| `F4` va a **validable, falta** | Darla por hecha | Que existan el plan y el plan de pruebas ya se comprueba; **la aprobación explícita no**, y esa es la mitad que importa |
| Los capítulos `18` y `19` se clasifican **aunque sean opt-in** | Dejarlos fuera por opcionales | `M9` no exceptúa a las reglas opcionales, y no clasificarlas es lo que las volvió invisibles |
| Cada 🟡 dice **qué le falta** | Marcarla y ya | Un registro que dice «falta» sin decir qué, no sirve para planear |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Clasificar las quince de conducta | Registro | 0,8 h | — | EV-01 |
| T-02 | Clasificar `G9`, `M15`, `F4` y `F12` | Registro | 0,5 h | T-01 | EV-01 |
| T-03 | Clasificar los ocho de despliegue | Registro | 0,7 h | T-02 | EV-01 |
| T-04 | Clasificar los seis de observabilidad | Registro | 0,6 h | T-03 | EV-01 |
| T-05 | Corregir el conteo del principio del registro | Registro | 0,3 h | T-04 | EV-01 |
| T-06 | La HU-009: §8, tareas y bitácora | HU | 0,4 h | T-05 | EV-02 |
| T-07 | Dejar el pendiente 19 con lo que sigue faltando | Backlog | 0,4 h | T-06 | — |
| T-08 | `CHANGELOG.md` y `VERSION` | Versionado | 0,3 h | T-07 | — |

**Total estimado:** 4 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-04 → T-05 → T-06 → T-07 → T-08

> Solo se tocan los archivos de §2.1 ([`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| CA-02 | Correr el validador de meta-reglas y contar los hallazgos de «no aparece en el registro» | EV-01 | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida del validador, antes y después | `resultado_pruebas.md` de esta fase |
| EV-02 | Documentación al día | `funcionalidad_implementada.md` del cierre |

---

## 6. Datos y ambiente de prueba

El propio cuerpo de reglas de este repositorio. No hay datos que proteger: el validador solo lee.

---

## 7. Reversión / rollback

Se revierte el commit. El registro es un documento y no cambia el comportamiento de nada.

---

## 8. Producción y migración incremental

No toca a ningún proyecto: el registro vive en el estándar y no se copia.

---

## 9. Reglas del estándar aplicadas

[`02·F23`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), [`02·F9`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F9-no-subdividas-ni-renegocies-un-plan-ya-aprobado.md), [`20·M9`](«RUTA-ESTANDAR»/base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md), [`20·M10`](«RUTA-ESTANDAR»/base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Clasificar de más como «no validable» para bajar el número de pendientes | El registro mentiría hacia el lado cómodo | Cada 🟡 dice qué le falta; si no se puede decir, es 🔴 de verdad | Abierto hasta la corrida |
| B-02 | Que la HU quede a medias y parezca cerrada | Se daría por resuelto el pendiente 19 entero | La fase cubre **un** CA de tres y lo dice en su §0; el pendiente 19 **no se cierra** | Declarado |

---

## 11. Definition of Done

- [ ] Las 33 clasificadas, cada 🟡 con qué le falta
- [ ] El validador no reporta ninguna regla sin clasificar
- [ ] El conteo del registro corregido
- [ ] El pendiente 19 al día con lo que sigue faltando, y **abierto**
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** Vive en el `funcionalidad_implementada.md` de esta fase.
