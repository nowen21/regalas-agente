# Plan de Trabajo — Fase A-EP-004-HU-018-el-numero-de-pendiente-libre (módulo Comprobación automática)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-018](../HU-018-numero-de-pendiente-ya-tomado.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-018-el-numero-de-pendiente-libre` |
| **Épica** | [EP-004 Comprobación automática](../../epica.md) |
| **HU** | [HU-018 Avisar cuando dos pendientes se disputan el mismo número](../HU-018-numero-de-pendiente-ya-tomado.md) — una sola (`F12.1`) |
| **Módulo** | Comprobación automática |
| **Especificación del módulo** | [HU-018](../HU-018-numero-de-pendiente-ya-tomado.md). El entregable es una comprobación corta: sus criterios de aceptación son la especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-004-HU-018-el-numero-de-pendiente-libre` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): ✨ **Funcionalidad nueva.** Hoy el número de un pendiente se elige **a ojo**, leyendo el índice, que puede estar más viejo que la carpeta. La HU nació el 2026-08-16, del hallazgo H-2 del [inventario de HU](../../../../../historico-chat/resumenes/2026-08-16/las-hu-sin-su-fase.md), el día en que dos sesiones tomaron el número 52. Sale de su fila en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-018 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-018-numero-de-pendiente-ya-tomado.md#ca-01--dice-cuál-es-el-próximo-número-libre) | Dice cuál es el próximo número libre | **No está.** El número se elige leyendo el índice |
| [CA-02](../HU-018-numero-de-pendiente-ya-tomado.md#ca-02--avisa-del-número-repetido) | Avisa del número repetido | **No está**, y ya pasó: dos archivos numerados 40 convivieron media hora el 2026-08-16 |
| [CA-03](../HU-018-numero-de-pendiente-ya-tomado.md#ca-03--cruza-la-carpeta-con-el-índice) | Cruza la carpeta con el índice | **No está**, y es donde se ve el desfase: hoy `validar.py estandar` reporta dos pendientes que la carpeta tiene y el índice no |

**Por qué una sola fase.** Los tres CA se resuelven leyendo la misma carpeta y el mismo índice (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que el número de un pendiente no se elija a ojo, y que un número repetido o una línea de índice sin archivo se vean al correr en vez de descubrirse por casualidad.

**Fuera de alcance:**

- **Decidir quién manda cuando dos sesiones escriben a la vez.** Es la decisión de fondo del pendiente [22](../../../../../pendientes/22-dos-sesiones-versionando-a-la-vez.md) y de [EP-002 · HU-006](../../../EP-002-versionado-y-adopcion/HU-006-quien-sube-la-version/HU-006-quien-sube-la-version.md). Esta HU avisa; no reparte turnos.
- **Asignar el número automáticamente.** Avisar y asignar son cosas distintas: asignar entra si el usuario lo pide.
- **Arreglar el índice del backlog.** Los dos que faltan hoy vienen de otra sesión sin guardar: se cuentan, no se tocan.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17: `validar.py estandar` reporta que el índice del backlog no menciona dos pendientes que la carpeta sí tiene.

**Lo que ya existe:** la comprobación de índices al día, que ya detecta el archivo sin su línea —es de `enlaces.py`, por `validar.py estandar`—; la carpeta con su numeración; y la evidencia de los dos casos: el número 52 tomado dos veces y los dos archivos numerados 40.

**Lo que no existe:**

1. **El próximo número libre.** Nadie lo dice: se lee el índice y se elige.
2. **La detección del número repetido.** La comprobación de índices mira si falta la línea, no si dos archivos comparten número.
3. **El cruce en los dos sentidos.** Hoy se detecta el archivo sin línea; la línea sin archivo no.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/pendientes.py` | Nuevo o modificar | La comprobación de numeración y cruce con el índice |
| `validadores/validar.py` | Modificar | Su subcomando, o el que ya tenga esa familia de comprobaciones |
| `validadores/docs/pendientes.md` | Nuevo o modificar | Qué mira y qué no |
| `validadores/pruebas.py` | Modificar | Los casos de los tres CA |
| `…/A-EP-004-HU-018-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron |
| `HU-018-numero-de-pendiente-ya-tomado.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> Ni el índice ni los pendientes se editan: lo que esté desfasado se reporta.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

| Archivo que cambia | Qué cambia | Quién depende | Dónde |
|---|---|---|---|
| `validadores/validar.py` | Un subcomando nuevo, o una comprobación más en el que exista | Los enganches que llaman por nombre | Solo se agrega |
| `validadores/pendientes.py` | Puede ser el mismo archivo de [HU-016](../../HU-016-el-pendiente-cerrado-nombra-su-fase/HU-016-el-pendiente-cerrado-nombra-su-fase.md) | Esa fase, si va primero | Las dos fases se coordinan: la segunda relee antes de escribir |

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque son programas de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

**Sí tendrá punto de entrada:** su subcomando en `validar.py`.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El próximo libre es el siguiente al mayor, no el primer hueco | Reusar los huecos | Un hueco puede ser un pendiente cerrado y movido; reusar su número rompe las citas que lo nombran |
| El programa avisa y no asigna | Que escriba el archivo con el número libre | Avisar deja la decisión en quien abre el pendiente, y no pisa lo que otra sesión esté haciendo |
| El cruce se reporta en los dos sentidos | Mirar solo el archivo sin línea | La línea sin archivo es el síntoma de un pendiente movido a `hecho/` sin actualizar el índice |

### 2.7 Dudas por resolver antes de escribir

Ninguna: los dos casos que la motivan están documentados y el desfase de hoy se puede medir.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Dice cuál es el próximo número libre

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Escribir la comprobación que lista los números tomados y dice el próximo libre | `validadores/` | 2,0 |
| T-02 | Caso de prueba: con huecos en la numeración, dice el siguiente al mayor y no el del hueco | `plan_pruebas.md` | 1,5 |

### CA-02 — Avisa del número repetido

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Que dos archivos con el mismo número se reporten, con los dos nombres | `validadores/` | 1,5 |
| T-04 | Caso de prueba: dos archivos con el mismo número en carpeta temporal se reportan | `plan_pruebas.md` | 1,5 |

### CA-03 — Cruza la carpeta con el índice

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-05 | Que la comprobación diga qué hay en la carpeta y no en el índice, y al revés | `validadores/` | 2,0 |
| T-06 | Caso de prueba: un pendiente sin línea en el índice y una línea sin archivo se reportan | `plan_pruebas.md` | 1,5 |

### RNF — Que el aviso llegue antes de escribir el archivo

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-07 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 7 tareas · 11,5 horas.**

---

## 4. Secuencia de ejecución

T-01 → T-03 → T-05 en el programa, con T-02, T-04 y T-06 detrás de cada uno. T-07 cierra. Si la fase de HU-016 va primero, esta se suma a su archivo en vez de crear uno nuevo.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Numeración con huecos, y el próximo libre | T-01, T-02 |
| CA-02 | Dos archivos con el mismo número | T-03, T-04 |
| CA-03 | Archivo sin línea y línea sin archivo | T-05, T-06 |

---

## 6. Datos y ambiente de prueba

Este repositorio y carpetas temporales para los casos negativos. Ningún dato real y ninguna clave.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

El estándar está en producción. Es **aditivo**: una comprobación más que avisa. Subida **MENOR**.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`13·DOC17`](../../../../../base/13-documentacion/reglas/DOC17-manten-un-readme-en-cada-nivel-del-arbol-de-trabajo.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que el aviso llegue tarde, cuando el archivo ya está escrito | No evita el choque, solo lo muestra | Es el límite de avisar: repartir turnos es la decisión del pendiente [22](../../../../../pendientes/22-dos-sesiones-versionando-a-la-vez.md) |
| R-02 | Que el desfase de hoy —dos pendientes sin línea— haga fallar la corrida propia | Se confunde con lo nuevo | Se anota el estado antes de empezar |
| R-03 | Cruce con la fase de HU-016, que puede crear el mismo archivo | Dos sesiones sobre el mismo programa | La segunda relee y se suma en vez de reescribir |

---

## 11. Definition of Done

- [ ] La comprobación dice cuál es el próximo número libre.
- [ ] Un número repetido se reporta con los dos nombres.
- [ ] El cruce carpeta-índice se reporta en los dos sentidos.
- [ ] El desfase de hoy quedó anotado como estado de partida.
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
