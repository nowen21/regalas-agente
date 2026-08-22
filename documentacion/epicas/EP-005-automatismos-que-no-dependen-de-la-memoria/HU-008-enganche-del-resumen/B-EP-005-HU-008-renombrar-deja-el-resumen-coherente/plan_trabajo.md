# Plan de Trabajo — Fase «B-EP-005-HU-008-renombrar-deja-el-resumen-coherente» (módulo «Histórico»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Se escribe **antes** de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-005-HU-008-renombrar-deja-el-resumen-coherente` |
| **Épica** | [EP-005 Automatismos que no dependen de la memoria](../../epica.md) |
| **HU** | [HU-008 — Enganche del resumen](../HU-008-enganche-del-resumen.md) — **una sola** (`F12.1`) |
| **Módulo** | Histórico (`validadores/historico.py`) |
| **Especificación del módulo** | No existe. Se declara como deuda en §10 (`B-03`) |
| **Fecha apertura** | 2026-08-16 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- 📝 **Modifica fase(s):** ninguna. La fase [`A`](../A-EP-005-HU-008-enganche-del-resumen/plan_trabajo.md) construyó el enganche que crea y avisa; el arrastre del resumen al renombrar es de `historico.py` y quedó incompleto desde que existe.
- ✨ **Funcionalidad nueva:** ninguna. Es completar lo que el arrastre ya hacía a medias.

**De dónde sale:** el pendiente 35 —cerrado por esta fase, y por eso su archivo vive ahora en [pendientes/hecho/renombrar-deja-el-resumen-coherente.md](../../../../../pendientes/hecho/renombrar-deja-el-resumen-coherente.md)—, reportado por el proyecto `shopnest-mesa` y reproducido en este repositorio el 2026-08-16 al nombrar una sesión.

**CA de la HU que cubre esta fase:**

| CA de `HU-008` que cierra esta fase | Estado |
|---|---|
| **CA-04 — Renombrar la sesión deja el resumen coherente** — se agrega a la HU en esta fase (T-01) | ☐ |

**Por qué un CA nuevo y no uno de los tres que hay.** El arrastre del resumen es exigencia de la HU: su `RN-06` dice que el enganche «crea, avisa y **arrastra**». Pero ninguno de los tres CA lo comprueba — el `CA-01` mira que el archivo nazca, el `CA-02` que avise y el `CA-03` el propósito. Sin CA no hay contra qué derivar el plan ([`02·F18`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F18-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md)), así que la exigencia se sube a la HU y el plan baja de ella. Aprobar este plan es aprobar también ese CA.

**Redacción propuesta del CA-04:**

```gherkin
Dado que una sesión ya tiene su resumen escrito
Cuando se le pone nombre con el comando que el propio enganche ofrece
Entonces el resumen queda con el nombre nuevo
Y el enlace que lleva de vuelta a la transcripción abre
```

---

## 1. Objetivo y alcance

**Objetivo:** que renombrar una sesión no deje ni un enlace roto — que el resumen que `historico.py` arrastra apunte a la transcripción con su nombre nuevo, y no al que ya no existe.

**Fuera de alcance:**

- **Los enlaces de fuera del resumen.** Quien cita la sesión desde `prompts/` o desde otro resumen sigue quedando roto: es el [pendiente 33 · punto 4](../../../../../pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md), que necesita el modo de reparación de `citas.py` y es una fase propia.
- **Arreglar los resúmenes que ya quedaron rotos.** Hoy no hay ninguno en este repositorio; si aparece uno, se arregla al correr el validador de enlaces, no acá.
- **La especificación del módulo.** Deuda heredada, declarada en §10.

---

## 2. Análisis previo — línea base verificada

### 2.1 Archivos que se crean o modifican

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `documentacion/epicas/EP-005-…/HU-008-…/HU-008-enganche-del-resumen.md` | Modificar | HU | Agregar el `CA-04` y nombrar esta fase en §8 |
| `validadores/historico.py` | Modificar | Histórico | Reescribir el enlace dentro del resumen que se arrastra |
| `validadores/tests/test_historico_renombrar.py` | Nuevo | Test | El caso del `CA-04` |
| `validadores/docs/historico.md` | Modificar | Documentación | Decir que `--renombrar` deja el enlace del resumen al día |
| `pendientes/README.md` · `pendientes/hecho/renombrar-deja-el-resumen-coherente.md` | Modificar / Nuevo | Backlog | Cerrar el 35 |
| `CHANGELOG.md` · `VERSION` | Modificar | Versionado | MENOR |

**Verificado el 2026-08-16 sobre el código real:**

- `_mover_resumen()` vive en [`validadores/historico.py:300`](../../../../../validadores/historico.py) y ya calcula `origen` y `destino` del resumen; después de `os.rename()` llama a `_reindexar_dia()` y termina. Ahí es donde falta reescribir el contenido.
- El enlace por corregir tiene esta forma, comprobada en un resumen real: `[historico-chat/<nombre>.md](../../<nombre>.md)`. **Son dos cosas que cambiar, no una:** el texto visible y el destino. El texto no es decorado — [`13·DOC14`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md) exige que diga dónde vive el archivo.
- `validadores/tests/` tiene hoy tres archivos de prueba y ninguno cubre `historico.py`.

### 2.2 Matriz de dependencias del cambio

| Quién | Impacto |
|---|---|
| `renombrar()` | Ninguno: sigue llamando a `_mover_resumen()` igual, con la misma firma |
| `_reindexar_dia()` | Ninguno: se sigue llamando después, sin cambios |
| El enganche del histórico | Ninguno: no llama a `_mover_resumen()`; el renombrado lo dispara el usuario |
| El validador de enlaces | Deja de reportar la falla que este defecto producía |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Reescribir el enlace **dentro** de `_mover_resumen()`, después de mover | Hacerlo en `renombrar()` | El nombre viejo y el nuevo del resumen solo los conoce esa función; sacarlos afuera es repetir el cálculo |
| Reemplazar el par exacto `[historico-chat/<viejo>](../../<viejo>)` y también el destino suelto | Reemplazar el nombre viejo en todo el archivo | Un resumen puede nombrar **otras** sesiones; reemplazar a ciegas les cambiaría el enlace a ellas |
| Si no se puede escribir, no detener el renombrado | Reventar | Es el mismo criterio que ya tiene `_mover_resumen()` con el `os.rename` fallido: el índice es lo que no puede quedar mal |
| Crear el archivo de pruebas de `historico.py` | Meter el caso en una suite existente | Las tres que hay son de instalación y enlaces; mezclar módulos rompe la corrida quirúrgica de [`02·F5`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md) |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Agregar el `CA-04` a la HU-008 y nombrar esta fase en su §8 | HU | 0,4 h | — | EV-02 |
| T-02 | `_mover_resumen()` reescribe el enlace a la transcripción | Histórico | 0,7 h | T-01 | EV-01 |
| T-03 | Caso de prueba: renombrar una sesión con resumen y comprobar el enlace | Test | 1 h | T-02 | EV-01 |
| T-04 | Prueba de la prueba: revertir el T-02 y ver el caso en rojo | Test | 0,2 h | T-03 | EV-01 |
| T-05 | `validadores/docs/historico.md` | Documentación | 0,3 h | T-02 | EV-02 |
| T-06 | Cerrar el 35 en `pendientes/`, con el aviso a `shopnest-mesa` anotado | Backlog | 0,4 h | T-05 | — |
| T-07 | `CHANGELOG.md` y `VERSION` (MENOR) | Versionado | 0,3 h | T-06 | — |

**Total estimado:** 3,3 h

**Por qué MENOR y no PARCHE.** No es solo redacción: `--renombrar` pasa a hacer algo que antes no hacía, y un proyecto al día no tiene que cambiar nada para recibirlo. Es aditivo ([`20·M10`](«RUTA-ESTANDAR»/base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-04 → T-05 → T-06 → T-07

> Solo se tocan los archivos de §2.1 ([`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| CA-04 (HU-008) | Prueba automática sobre un histórico de mentira: se renombra una sesión que ya tiene resumen y se lee el enlace de adentro | EV-01 | ☐ |
| CA-04 · el caso mide lo que dice | Se revierte el arreglo y el caso tiene que ponerse rojo | EV-01 | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de la prueba | `resultado_pruebas.md` de esta fase |
| EV-02 | Documentación al día | `funcionalidad_implementada.md` del cierre |

---

## 6. Datos y ambiente de prueba

Carpeta temporal desechable con un histórico armado a mano: una transcripción, su índice, y el resumen del día con el enlace de vuelta. **Nunca el `historico-chat/` real de este repositorio** ([`00·N4`](«RUTA-ESTANDAR»/base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)) — renombrar sobre el histórico vivo mueve archivos que son el registro del proyecto.

---

## 7. Reversión / rollback

El cambio es una función que reescribe un archivo de texto. Se revierte volviendo el commit atrás. Lo ya renombrado con la versión nueva queda correcto y no hay que deshacerlo.

---

## 8. Producción y migración incremental

Los proyectos herederos llaman a `historico.py` por su dirección en el estándar, así que reciben el arreglo sin hacer nada. Los resúmenes ya renombrados **antes** de esta fase siguen con su enlace roto: no se migran acá — hoy no hay ninguno en este repositorio, y en `shopnest-mesa` ya se corrigió a mano.

---

## 9. Reglas del estándar aplicadas

[`02·F23`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), [`02·F4`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`02·F18`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F18-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md), [`08·T4`](«RUTA-ESTANDAR»/base/08-pruebas.md#t4--protege-los-datos-reales-al-probar), [`13·DOC14`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md), [`20·M10`](«RUTA-ESTANDAR»/base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que el reemplazo toque el enlace de **otra** sesión nombrada dentro del mismo resumen | Se rompería un enlace que estaba bien | El reemplazo es del par exacto viejo→nuevo, y la prueba mete a propósito un enlace a otra sesión que no se debe tocar | Abierto hasta la corrida |
| B-02 | Que la prueba pase en verde con el defecto puesto | La fase se daría por cumplida sin estarlo | T-04: se revierte el arreglo y el caso tiene que ponerse rojo | Abierto hasta la corrida |
| B-03 | El módulo del histórico no tiene especificación | La fase se apoya en el código, no en un documento | Se declara la deuda; no se abre acá | Declarado |

---

## 11. Definition of Done

- [ ] El `CA-04` escrito en la HU-008 y esta fase nombrada en su §8
- [ ] El `CA-04` verificado con evidencia
- [ ] La prueba se pone roja si se revierte el arreglo
- [ ] El validador de enlaces en cero después de renombrar
- [ ] Documentación, pendiente 35 cerrado, `CHANGELOG` y `VERSION`
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** Vive en el `funcionalidad_implementada.md` de esta fase.
