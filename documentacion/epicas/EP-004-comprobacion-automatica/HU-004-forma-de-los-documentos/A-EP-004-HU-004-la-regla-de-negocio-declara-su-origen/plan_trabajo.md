# Plan de Trabajo — Fase «A-EP-004-HU-004-la-regla-de-negocio-declara-su-origen» (módulo «Programas de comprobación»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Se escribe **antes** de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-004-la-regla-de-negocio-declara-su-origen` |
| **Épica** | [EP-004 Comprobación automática](../../epica.md) |
| **HU** | [HU-004 — Forma de los documentos](../HU-004-forma-de-los-documentos.md) — **una sola** (`F12.1`) |
| **Módulo** | Programas de comprobación (`validadores/plantillas.py`) |
| **Especificación del módulo** | No existe. Se declara como deuda en §10 (`B-03`) |
| **Fecha apertura** | 2026-08-16 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- 📝 **Modifica fase(s):** ninguna.
- ✨ **Funcionalidad nueva:** una comprobación más sobre los documentos de especificación.

**De dónde sale:** la exigencia 2 del [pendiente 43](../../../../../pendientes/hecho/el-origen-de-la-regla-de-negocio.md). La 1 —el molde— la construyó la fase [`A-EP-003-HU-004`](../../../EP-003-documentos-modelo-y-procedimientos/HU-004-modelo-de-la-especificacion/A-EP-003-HU-004-el-origen-de-la-regla-de-negocio/README.md), que fijó el formato para que hubiera qué comprobar.

**CA de la HU que cubre esta fase:**

| CA de `HU-004` que cierra esta fase | Estado |
|---|---|
| **CA-04 — Una regla de negocio sin origen se marca** — se agrega a la HU en esta fase (T-01) | ☐ |

**Por qué un CA nuevo.** Los tres que hay miran marcadores sin llenar, secciones ausentes y planes sin especificación. Este mira **el contenido de una sección concreta**, que es otra cosa.

---

## 1. Objetivo y alcance

**Objetivo:** que una regla de negocio escrita sin procedencia se reporte, en vez de depender de que alguien pregunte de dónde salió. En `shopnest-mesa` tardó un día en verse, y solo porque alguien preguntó.

**Fuera de alcance:**

- **Comprobar que el identificador exista de verdad** en el requisito o la historia que nombra. Esta fase comprueba que **haya** identificador; que apunte a algo real es trabajo de trazabilidad y es otra fase.
- **Las especificaciones ya escritas.** El programa las va a reportar, y está bien: reportar no es reabrir. Contarlas y arreglarlas es la exigencia 3 del pendiente, que no se hace acá.
- **La columna `Origen` del §5.1**, la tabla de campos.
- **La especificación del módulo de comprobación.** Deuda heredada.

---

## 2. Análisis previo — línea base verificada

### 2.1 Archivos que se crean o modifican

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `documentacion/.../HU-004-forma-de-los-documentos.md` | Modificar | HU | El `CA-04`, la fase en §8 y la bitácora |
| `validadores/plantillas.py` | Modificar | Comprobación | `spec` en la tabla de plantillas, y la comprobación nueva |
| `validadores/tests/test_plantillas_origen_regla.py` | Nuevo | Test | Los casos del `CA-04` |
| `validadores/docs/plantillas.md` | Modificar | Documentación | La comprobación nueva |
| `pendientes/README.md` · `pendientes/hecho/` | Modificar / Nuevo | Backlog | Cerrar el 43, ahora sí completo |
| `CHANGELOG.md` · `VERSION` | Modificar | Versionado | MENOR |

**Verificado el 2026-08-16 sobre el código real:**

- `deducir_plantilla()` en [`validadores/plantillas.py:61`](../../../../../validadores/plantillas.py) resuelve la plantilla por el prefijo del título o por el nombre del archivo, contra `POR_NOMBRE` (línea 30).
- **`spec` no está en esa tabla.** Un documento llamado `spec.md` hoy no se compara contra ninguna plantilla: el programa no lo reconoce. Sin eso, la comprobación nueva no se dispararía nunca.
- `validar(ruta_documento, ruta_plantilla)` en la línea 88 hace hoy tres comprobaciones: líneas sin llenar, notas sin borrar y secciones ausentes.

### 2.2 Matriz de dependencias del cambio

| Quién | Impacto |
|---|---|
| `hook_md.py` y `validar.py plantilla` | Reciben un hallazgo más; no cambia la firma |
| Los documentos llamados `spec.md` | **Empiezan a compararse contra la plantilla**, cosa que hoy no pasaba. Van a aparecer hallazgos de forma que antes nadie veía |
| Las tres comprobaciones que ya existen | Ninguno: la nueva se agrega al final y no toca las anteriores |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La comprobación vive en `plantillas.py` | En `trazabilidad.py` | Lo que se mira es la **forma** de una sección de un documento contra su plantilla, que es lo que hace este módulo. Trazabilidad mira que lo citado exista, y eso está fuera de alcance |
| Se dispara solo si la plantilla deducida es la de especificación | Buscar la sección en cualquier documento | Un `## 4. Reglas de negocio` puede aparecer en otro documento con otro sentido |
| El identificador se reconoce como `LETRAS-NÚMERO` | Una lista cerrada de prefijos válidos | Cada proyecto nombra sus requisitos a su manera (`RF-13`, `HU-001`, `D-22`, `RN-05`); una lista cerrada obligaría a mantenerla desde el estándar |
| Es **FALLA**, no aviso | Aviso | Una regla sin fuente ya se coló hasta un criterio de aceptación. Si avisa, se ignora |
| Las líneas que siguen siendo el molde no se cuentan | Reportarlas también | Ya las reporta la comprobación 1, y reportar dos veces lo mismo enseña a ignorar |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | El `CA-04` en la HU-004, con su fase en §8 y su bitácora | HU | 0,4 h | — | EV-02 |
| T-02 | `spec` en la tabla de plantillas de `plantillas.py` | Comprobación | 0,2 h | T-01 | EV-01 |
| T-03 | La comprobación de la regla sin origen | Comprobación | 1,2 h | T-02 | EV-01 |
| T-04 | Los casos de prueba, incluida la regla real que lo destapó | Test | 1,2 h | T-03 | EV-01 |
| T-05 | Prueba de la prueba: revertir el T-03 y ver los casos en rojo | Test | 0,2 h | T-04 | EV-01 |
| T-06 | `validadores/docs/plantillas.md` | Documentación | 0,4 h | T-04 | EV-02 |
| T-07 | Cerrar el 43, con el aviso a `shopnest-mesa` anotado | Backlog | 0,4 h | T-06 | — |
| T-08 | `CHANGELOG.md` y `VERSION` | Versionado | 0,3 h | T-07 | — |

**Total estimado:** 4,3 h

**Por qué MENOR y no MAYOR.** Lo que obliga —escribir la procedencia— ya lo declaró la 22.0.0. Esta versión solo agrega el programa que lo mira.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-04 → T-05 → T-06 → T-07 → T-08

> Solo se tocan los archivos de §2.1 ([`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| CA-04 | Especificaciones de mentira con reglas con y sin origen | EV-01 | ☐ |
| CA-04 · el caso mide lo que dice | Se revierte la comprobación y los casos se ponen rojos | EV-01 | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de la prueba | `resultado_pruebas.md` de esta fase |
| EV-02 | Documentación al día | `funcionalidad_implementada.md` del cierre |

---

## 6. Datos y ambiente de prueba

Carpetas temporales con especificaciones de mentira. Una de ellas trae **las dos reglas reales** del caso de `shopnest-mesa`: la que baja de `RF-13` y la que no baja de nada. Nunca una especificación viva ([`00·N4`](«RUTA-ESTANDAR»/base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)).

---

## 7. Reversión / rollback

Se revierte el commit. Nada queda escrito de forma distinta: el programa lee y reporta, no modifica.

---

## 8. Producción y migración incremental

Los proyectos llaman a los validadores por su dirección en el estándar, así que reciben la comprobación sin hacer nada. **Van a aparecer hallazgos en especificaciones que ayer estaban en verde**, y eso es lo esperado: son reglas sin fuente que ya estaban ahí. Reportar no es reabrir la fase donde se escribieron.

---

## 9. Reglas del estándar aplicadas

[`02·F23`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), [`02·F11`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F11-una-fase-solo-modifica-codigo-de-su-propio-modulo.md), [`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T4`](«RUTA-ESTANDAR»/base/08-pruebas.md#t4--protege-los-datos-reales-al-probar), [`20·M10`](«RUTA-ESTANDAR»/base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que reconocer `spec` haga aparecer una avalancha de hallazgos de forma en las especificaciones vivas | Ruido que enseña a ignorar el validador | Se cuenta cuántos salen en este repositorio y se deja escrito; si son muchos, se anota como lo que sigue, no se calla la comprobación | Abierto hasta la corrida |
| B-02 | Que el patrón del identificador dé falsos positivos con una regla que nombra una tabla o un código | Se reportaría una regla que sí tiene fuente | Los casos incluyen una regla con texto que se le parece | Abierto hasta la corrida |
| B-03 | El módulo no tiene especificación | La fase se apoya en el código | Se declara la deuda | Declarado |

---

## 11. Definition of Done

- [ ] El `CA-04` escrito en la HU-004 y esta fase nombrada en su §8
- [ ] La comprobación reporta la regla sin origen y calla con la que lo tiene
- [ ] Los casos se ponen rojos si se revierte la comprobación
- [ ] Documentación, pendiente 43 cerrado, `CHANGELOG` y `VERSION`
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** Vive en el `funcionalidad_implementada.md` de esta fase.
