# Plan de Trabajo — Fase A-EP-005-HU-010-el-capitulo-llega-al-escribir-el-archivo (módulo Automatismos)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-010](../HU-010-la-regla-llega-al-escribir-el-archivo.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-010-el-capitulo-llega-al-escribir-el-archivo` |
| **Épica** | [EP-005 Automatismos que no dependen de la memoria](../../epica.md) |
| **HU** | [HU-010 El capítulo que rige lo que se escribe llega al escribirlo](../HU-010-la-regla-llega-al-escribir-el-archivo.md) — una sola (`F12.1`) |
| **Módulo** | Automatismos |
| **Especificación del módulo** | [documentacion/automatismos/spec.md](../../../../automatismos/spec.md). Existe desde el 2026-08-14 y crece por incrementos; esta fase le agrega el suyo (`02·F2`) |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-005-HU-010-el-capitulo-llega-al-escribir-el-archivo` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): ✨ **Funcionalidad nueva.** El disparo existe —[`hook_md.py`](../../../../../validadores/hook_md.py) corre con cada escritura— y lo que hace es **comprobar enlaces**, no entregar el capítulo que rige lo que se está escribiendo. Lo que llega puesto al abrir la sesión son los capítulos `00` y `01`, por [`cargador.py`](../../../../../validadores/cargador.py), ya retro-documentado en la fase A de [HU-009](../../HU-009-lo-que-rige-cada-frase-llega-puesto/A-EP-005-HU-009-retrodocumentar-el-reparto-de-las-reglas/README.md). Del resto llega el índice. Sale de la fila de HU-010 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-010 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-010-la-regla-llega-al-escribir-el-archivo.md#ca-01--al-escribir-el-documento-llega-su-capítulo) | Al escribir el documento llega su capítulo | **No está.** Al escribir un plan de trabajo, el capítulo `02` no llega: llega su índice al abrir la sesión, y hay que acordarse de abrirlo |
| [CA-02](../HU-010-la-regla-llega-al-escribir-el-archivo.md#ca-02--no-se-repite-lo-que-ya-llegó) | No se repite lo que ya llegó | **No está**, y es lo que decide si se puede vivir con esto: repetir el capítulo en cada escritura llenaría la sesión de texto |
| [CA-03](../HU-010-la-regla-llega-al-escribir-el-archivo.md#ca-03--lo-que-no-le-toca-no-dispara-nada) | Lo que no le toca no dispara nada | Ya resuelto para los enlaces por el mismo enganche, que se calla con lo que no le toca. Falta que valga para la entrega del capítulo |

**Por qué una sola fase.** Los tres CA son la misma entrega: qué llega, cuándo no se repite y cuándo no llega nada (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que la regla que gobierna un documento llegue en el momento de escribirlo, sin llenar la sesión repitiendo capítulos.

**Fuera de alcance:**

- **El reparto al abrir la sesión,** ya retro-documentado en la fase A de [HU-009](../../HU-009-lo-que-rige-cada-frase-llega-puesto/HU-009-lo-que-rige-cada-frase-llega-puesto.md).
- **Las comprobaciones de enlaces** que el enganche ya corre, que son [HU-003](../../HU-003-disparo-al-escribir-un-archivo/HU-003-disparo-al-escribir-un-archivo.md).
- **Cambiar el reparto de qué va completo y qué en índice.** Si medir muestra que hay que cambiarlo, se para y se propone.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17: `hook_md.py` solo corre las comprobaciones de enlaces, y `cargador.py` manda completos los capítulos `00` y `01` al abrir la sesión.

**Lo que ya existe:** el disparo en cada escritura; el reparto al abrir, con su medición hecha —lo que se inyecta pesa unos 73 KB—; el índice de capítulos, con el peso de cada uno; y la decisión ya probada de que no todo puede llegar completo, porque el arranque se encarece.

**Lo que no existe:**

1. **La entrega por documento.** Nada relaciona «estoy escribiendo un plan de trabajo» con «el capítulo `02` es el que manda acá».
2. **La memoria de lo ya entregado.** Sin ella la sesión se llena de repeticiones.
3. **La medida del costo.** El reparto al abrir ya está medido; lo que sumaría esta entrega, no.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/hook_md.py` | Modificar | Le entra la entrega del capítulo, junto a lo que ya hace |
| `validadores/cargador.py` | Modificar | Le pide el capítulo que corresponde, reusando lo que ya sabe leer |
| `validadores/docs/hook_md.md` · `docs/cargador.md` | Modificar | Qué se entrega, cuándo y cuándo no |
| `validadores/pruebas.py` | Modificar | Los casos de los tres CA |
| `documentacion/automatismos/spec.md` | Modificar | El incremento |
| `…/A-EP-005-HU-010-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron |
| `HU-010-la-regla-llega-al-escribir-el-archivo.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `CHANGELOG.md` · `VERSION` | Modificar | Entrada y subida |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> El reparto de qué va completo al abrir no se toca: acá se agrega una entrega por escritura.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

| Archivo que cambia | Qué cambia | Quién depende | Dónde |
|---|---|---|---|
| `validadores/hook_md.py` | Hace algo más que comprobar enlaces | La fase A de HU-003, que lo prueba | Las comprobaciones de enlaces siguen igual, y eso va probado: si la entrega falla, los enlaces se comprueban de todos modos |
| `validadores/cargador.py` | Gana una forma de pedirle un capítulo suelto | La fase A de HU-009, que midió su costo | Lo que ya entrega al abrir no cambia |

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque son enganches de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

**Sí tiene punto de entrada, y no hace falta pedirlo:** el enganche corre después de cada escritura.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La relación documento → capítulo se declara en una tabla, no se adivina | Deducirla del nombre del archivo | Adivinar por el nombre falla con los documentos que no siguen la convención, y el estándar ya tiene varios |
| Lo entregado en la sesión no se repite | Entregar siempre | El arranque ya pesa 73 KB: repetir capítulos en cada escritura haría inutilizable la sesión |
| Si la entrega falla, las comprobaciones de enlaces corren igual | Que el enganche se caiga entero | Perder la comprobación de enlaces por un fallo de la entrega es cambiar algo que funciona por algo que no |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién | Estado |
|---|---|---|---|
| 1 | Qué capítulo rige cada tipo de documento — la tabla la decide quien mantiene el estándar | Usuario | Pendiente |
| 2 | Si llega el capítulo completo o solo la regla que aplica, dado lo que pesa | Usuario | Pendiente |

Las dos bloquean T-01. La prueba del silencio del CA-03 se puede escribir antes.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Al escribir el documento llega su capítulo

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Escribir la entrega del capítulo según qué documento se está escribiendo | `validadores/` | 3,0 |
| T-02 | Caso de prueba: al escribir un plan de trabajo llega el capítulo de flujo; al escribir una regla, el de meta-reglas | `plan_pruebas.md` | 2,0 |

### CA-02 — No se repite lo que ya llegó

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Que lo ya entregado en la sesión no se vuelva a entregar | `validadores/` | 2,0 |
| T-04 | Prueba: dos escrituras del mismo tipo de documento entregan el capítulo una sola vez | `validadores/pruebas.py` | 2,0 |

### CA-03 — Lo que no le toca no dispara nada

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-05 | Caso de prueba: escribir un archivo que no es documento del proyecto no entrega nada | `plan_pruebas.md` | 1,5 |

### RNF — Que la sesión no se llene de repeticiones

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-06 | Correr las pruebas, escribir el incremento de la especificación y cerrar la trazabilidad de la HU y del inventario | Cierre | 2,0 |

**Total: 6 tareas · 12,5 horas.**

---

## 4. Secuencia de ejecución

T-05 primero, que es el silencio. T-01 → T-02 → T-03 → T-04 con las dudas resueltas. T-06 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Plan de trabajo y regla, cada uno con su capítulo | T-01, T-02 |
| CA-02 | Dos escrituras del mismo tipo, una sola entrega | T-03, T-04 |
| CA-03 | Archivo que no es documento, sin entrega | T-05 |

---

## 6. Datos y ambiente de prueba

Carpetas temporales para los casos, y este repositorio para las corridas. Ningún dato real y ninguna clave: lo que parezca una clave se arma para la prueba.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

El estándar está en producción y este enganche corre en cada proyecto instalado. Cambia lo que el agente recibe al escribir: **obliga** en el sentido de que cambia el comportamiento, así que se declara **MAYOR** con su marca, salvo que la duda 2 lo deje en un agregado pequeño.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`00·ID9`](../../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md), [`02·F1`](../../../../../base/02-flujo-de-trabajo/reglas/F1-carga-el-contexto-antes-de-actuar.md), [`06`](../../../../../base/06-rendimiento.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Las dos dudas sin resolver | Bloquean la entrega | Se presentan al usuario |
| R-01 | Que la entrega llene la sesión de texto | El arranque y cada escritura se encarecen | El CA-02 es esa prueba, y el resultado mide cuánto suma |
| R-02 | Que la tabla documento → capítulo quede incompleta | Documentos sin su regla | Lo que no esté en la tabla no entrega nada, y eso se reporta como hueco en vez de adivinar |
| R-03 | Que un fallo de la entrega tumbe la comprobación de enlaces | Se pierde algo que ya funcionaba | Va probado: la entrega falla y los enlaces se comprueban igual |

---

## 11. Definition of Done

- [ ] Al escribir un documento llega el capítulo que lo rige.
- [ ] Lo ya entregado en la sesión no se repite, con prueba.
- [ ] Lo que no le toca no entrega nada.
- [ ] Está medido cuánto suma la entrega al costo de la sesión.
- [ ] Si la entrega falla, las comprobaciones de enlaces corren igual.
- [ ] `CHANGELOG.md` con su entrada y `VERSION` subida.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
