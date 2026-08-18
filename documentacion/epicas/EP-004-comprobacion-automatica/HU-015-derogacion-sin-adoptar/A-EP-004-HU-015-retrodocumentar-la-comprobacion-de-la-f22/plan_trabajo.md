# Plan de Trabajo — Fase «A-EP-004-HU-015-retrodocumentar-la-comprobacion-de-la-f22» (módulo «Programas de comprobación»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Se escribe **antes** de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-015-retrodocumentar-la-comprobacion-de-la-f22` |
| **Épica** | [EP-004 Comprobación automática](../../epica.md) |
| **HU** | [HU-015 — Derogación sin adoptar](../HU-015-derogacion-sin-adoptar.md) — **una sola** (`F12.1`) |
| **Módulo** | Programas de comprobación (`validadores/version.py`, `validadores/flujo.py`) |
| **Especificación del módulo** | No existe. Se declara como deuda en §10 (`B-02`) |
| **Fecha apertura** | 2026-08-16 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- 📝 **Modifica fase(s):** ninguna.
- ✨ **Funcionalidad nueva:** ninguna. **Es retrodocumentación**: el código ya existe y esta fase le pone la cadena que le faltaba.

**De dónde sale:** el pendiente 38 —cerrado por esta fase, y por eso su archivo vive ahora en [pendientes/hecho/el-validador-de-la-f22-tiene-su-fase.md](../../../../../pendientes/hecho/el-validador-de-la-f22-tiene-su-fase.md)—. El 2026-08-16 se escribió [`02·F22`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md) y, en la misma sesión, el programa que la comprueba — sin épica, sin HU y sin fase. Es el propio repositorio que escribe la regla incumpliéndola mientras la escribe.

**CA de la HU que cubre esta fase:**

| CA de `HU-015` que cierra esta fase | Estado |
|---|---|
| [CA-01 — Falla el proyecto con una derogación sin adoptar](../HU-015-derogacion-sin-adoptar.md#ca-01--falla-el-proyecto-con-una-derogación-sin-adoptar) | ☐ |
| [CA-02 — No cuenta lo que ya está adoptado](../HU-015-derogacion-sin-adoptar.md#ca-02--no-cuenta-lo-que-ya-está-adoptado) | ☐ |
| [CA-03 — Sin fases no se cobra](../HU-015-derogacion-sin-adoptar.md#ca-03--sin-fases-no-se-cobra) | ☐ |

**Los tres, y no uno.** El código que se retrodocumenta los implementa a los tres; partirlos en fases distintas sería inventar un orden que el trabajo no tuvo.

---

## 1. Objetivo y alcance

**Objetivo:** que el programa que comprueba la `F22` tenga la fase que le faltaba — su plan, su evidencia y su cierre—, y que esa evidencia sea **una corrida de verdad**, no la afirmación de que alguna vez se probó a mano.

**Qué NO es esta fase:** reescribir el código. Lo que hay funciona; lo que falta es el registro que dice por qué es como es y la prueba que lo respalda.

**Fuera de alcance:**

- **Cambiar el comportamiento** de `derogaciones`, `sin_adoptar` o `validar_fase`. Si la evidencia destapa un defecto, se reporta; corregirlo es otra fase.
- **Reconocer la fase que adopta la derogación** para dejarla pasar. La HU ya lo declara fuera de alcance.
- **El filtro de las reglas opcionales** que el proyecto nunca encendió. Igual, ya declarado.
- **La especificación del módulo.** Deuda heredada.

---

## 2. Análisis previo — línea base verificada

### 2.1 Archivos que se crean o modifican

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/tests/test_version_derogaciones.py` | Nuevo | Test | La evidencia de los tres CA |
| `documentacion/.../HU-015-derogacion-sin-adoptar.md` | Modificar | HU | §8 con la fase, tareas y `DoD` al día, bitácora |
| `validadores/docs/version.md` | Modificar | Documentación | Las tres funciones, si no están |
| `pendientes/README.md` · `pendientes/hecho/` | Modificar / Nuevo | Backlog | Cerrar el 38 |
| `CHANGELOG.md` · `VERSION` | Modificar | Versionado | PARCHE |

**Verificado el 2026-08-16 sobre el código real:**

- `derogaciones(base=None)` en [`validadores/version.py:65`](../../../../../validadores/version.py) recorre `base/` y lee la marca del encabezado; devuelve `(versión, regla, reemplazo)` ordenado.
- `sin_adoptar(adoptada, estandar, derogadas)` en la línea 90 es **núcleo puro**, sin disco: filtra `desde < versión <= hasta`. Se puede probar sin armar ningún proyecto.
- `validar_fase(raiz)` en la línea 114 lee el `CLAUDE.md` del proyecto y arma la falla.
- [`validadores/flujo.py:256`](../../../../../validadores/flujo.py) la llama **solo si `hay_fases`**, que es exactamente el `CA-03`.

### 2.2 Matriz de dependencias del cambio

Ninguna: no se toca código de producción. El archivo de pruebas es nuevo y nadie depende de él.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La evidencia es una prueba automática, no el relato de una corrida a mano | Escribir el `resultado_pruebas` con lo que la sesión anterior dijo haber probado | Retrodocumentar no es dar fe de lo que no se vio. Una prueba que corre hoy vale más que un testimonio |
| El `CA-02` se prueba sobre `sin_adoptar()`, que no toca disco | Armar un tercer proyecto de mentira | La función es pura y el criterio es aritmético; montar carpetas para eso es ruido |
| Los `CA-01` y `CA-03` sí arman proyecto de mentira | Probar solo la función pura | Lo que el `CA-03` exige —que sin fases no se cobre— vive en `flujo.py`, no en `version.py` |
| Las derogaciones del caso se toman de las reales del estándar | Inventar una regla derogada de mentira | Si mañana cambia el formato de la marca, la prueba lo dice en vez de pasar contra un dato inventado |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Prueba del `CA-01`: proyecto atrasado con fases → falla que nombra las reglas | Test | 1,2 h | — | EV-01 |
| T-02 | Prueba del `CA-02`: `sin_adoptar()` con versión intermedia | Test | 0,5 h | T-01 | EV-01 |
| T-03 | Prueba del `CA-03`: el mismo proyecto sin fases → sin falla | Test | 0,5 h | T-01 | EV-01 |
| T-04 | Prueba de los transversales: sin `CLAUDE.md` y sin versión declarada | Test | 0,5 h | T-01 | EV-01 |
| T-05 | `validadores/docs/version.md` | Documentación | 0,4 h | T-04 | EV-02 |
| T-06 | La HU-015: §8, tareas, `DoD` y bitácora | HU | 0,4 h | T-04 | EV-02 |
| T-07 | Cerrar el 38 en `pendientes/` | Backlog | 0,3 h | T-06 | — |
| T-08 | `CHANGELOG.md` y `VERSION` | Versionado | 0,3 h | T-07 | — |

**Total estimado:** 4,1 h

**Por qué PARCHE y no MENOR.** No cambia qué exige el estándar ni agrega nada que un proyecto pueda usar: pone por escrito y bajo prueba algo que ya estaba corriendo.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-04 → T-05 → T-06 → T-07 → T-08

> Solo se tocan los archivos de §2.1 ([`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| CA-01 | Proyecto de mentira con versión vieja y una fase; se lee la falla | EV-01 | ☐ |
| CA-02 | `sin_adoptar()` con tres versiones distintas | EV-01 | ☐ |
| CA-03 | El mismo proyecto sin carpeta de fases; no sale falla | EV-01 | ☐ |
| Transversales | Sin `CLAUDE.md` y sin versión declarada: silencio, no error | EV-01 | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de la prueba | `resultado_pruebas.md` de esta fase |
| EV-02 | Documentación al día | `funcionalidad_implementada.md` del cierre |

---

## 6. Datos y ambiente de prueba

Carpetas temporales desechables con un `CLAUDE.md` y un árbol de épicas de mentira. Nunca un proyecto real ([`00·N4`](«RUTA-ESTANDAR»/base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)).

---

## 7. Reversión / rollback

No hay nada que revertir en producción: la fase agrega documentos y un archivo de pruebas.

---

## 8. Producción y migración incremental

No toca lo instalado. El comportamiento que se documenta ya está corriendo en todos los proyectos desde la 19.0.0.

---

## 9. Reglas del estándar aplicadas

[`02·F23`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), [`02·F0`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md), [`02·F4`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T4`](«RUTA-ESTANDAR»/base/08-pruebas.md#t4--protege-los-datos-reales-al-probar), [`13·DOC6`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`20·M10`](«RUTA-ESTANDAR»/base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que la prueba descubra que el código no hace lo que la HU dice | La fase cerraría con un CA en «No» | Se reporta y se deja escrito; corregirlo es otra fase, no esta | Abierto hasta la corrida |
| B-02 | El módulo no tiene especificación | La fase se apoya en el código | Se declara la deuda; no se abre acá | Declarado |
| B-03 | Que no haya ninguna regla derogada en el rango que arma la prueba | El caso pasaría sin comprobar nada | La prueba comprueba **primero** que hay derogaciones reales y falla si no las hay | Abierto hasta la corrida |

---

## 11. Definition of Done

- [ ] Los tres CA verificados con evidencia de una corrida real
- [ ] La HU-015 nombra esta fase en su §8
- [ ] Documentación, pendiente 38 cerrado, `CHANGELOG` y `VERSION`
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** Vive en el `funcionalidad_implementada.md` de esta fase.
