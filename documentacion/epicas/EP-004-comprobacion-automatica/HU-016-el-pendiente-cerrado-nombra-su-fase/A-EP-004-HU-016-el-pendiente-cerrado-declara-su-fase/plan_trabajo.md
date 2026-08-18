# Plan de Trabajo — Fase A-EP-004-HU-016-el-pendiente-cerrado-declara-su-fase (módulo Comprobación automática)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-016](../HU-016-el-pendiente-cerrado-nombra-su-fase.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-016-el-pendiente-cerrado-declara-su-fase` |
| **Épica** | [EP-004 Comprobación automática](../../epica.md) |
| **HU** | [HU-016 Comprobar que el pendiente cerrado nombra su fase](../HU-016-el-pendiente-cerrado-nombra-su-fase.md) — una sola (`F12.1`) |
| **Módulo** | Comprobación automática |
| **Especificación del módulo** | [HU-016](../HU-016-el-pendiente-cerrado-nombra-su-fase.md). El entregable es un programa de comprobación: sus criterios de aceptación y [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) son la especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-004-HU-016-el-pendiente-cerrado-declara-su-fase` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): ✨ **Funcionalidad nueva.** La regla existe —[`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md): un pendiente se ejecuta como fase de una historia de usuario— y **ningún programa comprueba** que el pendiente cerrado diga en qué fase se hizo. El registro de reglas validables lo dice con estas palabras: «`02·F23` necesita que el pendiente cerrado declare su fase». Sale de la fila de HU-016 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-016 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-016-el-pendiente-cerrado-nombra-su-fase.md#ca-01--un-pendiente-cerrado-sin-fase-se-reporta) | Un pendiente cerrado sin fase se reporta | **No está.** Hay 17 pendientes cerrados y 12 nombran algo parecido a una fase; los otros cinco no |
| [CA-02](../HU-016-el-pendiente-cerrado-nombra-su-fase.md#ca-02--una-fase-que-no-existe-se-reporta) | Una fase que no existe se reporta | **No está.** Un pendiente podría nombrar una fase que nadie creó y nadie se enteraría |
| [CA-03](../HU-016-el-pendiente-cerrado-nombra-su-fase.md#ca-03--el-pendiente-que-no-era-desarrollo-no-se-reporta) | El pendiente que no era desarrollo no se reporta | **No está**, y sin esto el programa reportaría de más: no todo pendiente cerrado fue una fase |
| [CA-04](../HU-016-el-pendiente-cerrado-nombra-su-fase.md#ca-04--lo-cerrado-antes-de-la-regla-se-separa) | Lo cerrado antes de la regla se separa | **No está.** Los 17 cerrados son de antes: exigirles la fase hacia atrás sería reabrir lo cerrado |

**Por qué una sola fase.** Los cuatro CA son la misma comprobación con sus tres excepciones: sin ellas el programa reporta de más y se ignora (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que un pendiente cerrado diga en qué fase se hizo y que eso se pueda comprobar, sin exigirlo hacia atrás ni a lo que no fue desarrollo.

**Fuera de alcance:**

- **Completar los 17 pendientes cerrados.** Lo cerrado no se reabre; se cuenta y se separa.
- **La cadena que baja el pendiente a historia y a fase,** que es la regla misma y ya está escrita.
- **El aviso al cerrar un pendiente.** Sería un enganche, y eso es de EP-005.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17: `pendientes/hecho/` tiene 17 archivos, 12 mencionan una fase de alguna forma, y ningún validador lo mira.

**Lo que ya existe:** la regla que lo exige; los 17 pendientes cerrados, la mayoría nombrando su fase por costumbre; el árbol de épicas contra el que se puede resolver el nombre de una fase; y el registro de reglas validables, que ya dejó anotado qué le falta a esta regla para poder comprobarse.

**Lo que no existe:**

1. **El programa.** Nada mira `pendientes/hecho/`.
2. **La forma de declararlo.** Los 12 que nombran su fase lo hacen cada uno a su manera: un programa necesita un lugar fijo donde mirar.
3. **La fecha de corte.** Sin ella, la comprobación exigiría hacia atrás y reportaría 17 incumplimientos el primer día.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/pendientes.py` | Nuevo | La comprobación, con sus tres excepciones |
| `validadores/validar.py` | Modificar | Su subcomando |
| `validadores/docs/pendientes.md` | Nuevo | Qué mira, qué no y desde cuándo |
| `validadores/pruebas.py` | Modificar | Los casos de los cuatro CA |
| `pendientes/README.md` | Modificar | Dice dónde se declara la fase en un pendiente que se cierra |
| `validadores/reglas-validables.md` | Modificar | `02·F23` pasa de validable pendiente a validador escrito |
| `…/A-EP-004-HU-016-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron |
| `HU-016-el-pendiente-cerrado-nombra-su-fase.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> Los 17 pendientes cerrados no se editan.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

| Archivo que cambia | Qué cambia | Quién depende | Dónde |
|---|---|---|---|
| `pendientes/README.md` | Fija dónde se declara la fase | Los pendientes que se cierren de aquí en adelante | Los 17 ya cerrados quedan del lado viejo por la fecha de corte |
| `validadores/validar.py` | Un subcomando nuevo | Los enganches que llaman por nombre | Solo se agrega |

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque son programas de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

**Sí tendrá punto de entrada:** su subcomando en `validar.py`.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La fecha de corte se escribe en la documentación del programa | Dejar que el programa la deduzca del historial | Deducirla del historial la vuelve frágil: un archivo movido cambiaría la fecha |
| El pendiente que no fue desarrollo lo declara él mismo | Que el programa lo adivine por el texto | Adivinar por prosa es lo que produce falsos positivos, y un falso positivo apaga el programa |
| El nombre de la fase se resuelve contra el árbol | Confiar en que está bien escrito | Es la mitad del valor: una fase que no existe es una promesa de trazabilidad que nadie puede seguir |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién | Estado |
|---|---|---|---|
| 1 | Cuál es la fecha de corte: desde cuándo se exige que el pendiente cerrado nombre su fase | Usuario | Pendiente |
| 2 | Dónde se declara — una línea fija al principio del pendiente, o una sección | Usuario | Pendiente |

Las dos bloquean T-01 y T-07. Los casos de prueba se pueden escribir antes.

**Decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md). 👤 marca lo que sigue esperando un dato del usuario.

| Duda | Decisión |
|---|---|
| 26 | **Desde el 2026-08-16**, que es cuando nació la exigencia. Lo cerrado antes no se reabre (`20·M10`). |
| 27 | **Una fila fija en la ficha de cabecera.** Una sección se olvida; una fila vacía se ve. |

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Un pendiente cerrado sin fase se reporta

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Escribir la comprobación: todo archivo de `pendientes/hecho/` declara la fase en que se hizo | `validadores/` | 2,5 |
| T-02 | Caso de prueba: un pendiente cerrado sin fase se reporta; uno que la nombra, no | `plan_pruebas.md` | 1,5 |

### CA-02 — Una fase que no existe se reporta

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Que la fase declarada se resuelva contra el árbol de épicas | `validadores/` | 2,0 |
| T-04 | Caso de prueba: una fase inventada se reporta; una que existe, no | `plan_pruebas.md` | 1,5 |

### CA-03 — El pendiente que no era desarrollo no se reporta

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-05 | Que el pendiente pueda declarar que no fue desarrollo, y con qué motivo | `validadores/` | 1,5 |
| T-06 | Caso de prueba: un pendiente cerrado por decisión, no por construcción, no se reporta | `plan_pruebas.md` | 1,5 |

### CA-04 — Lo cerrado antes de la regla se separa

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-07 | Que la comprobación separe lo cerrado antes de la fecha de la regla, y lo cuente aparte | `validadores/` | 2,0 |
| T-08 | Anotar cuáles de los 17 quedan del lado viejo y cuáles del nuevo | `resultado_pruebas.md` | 1,5 |

### RNF — Que el programa no reporte de más

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-09 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 9 tareas · 15,5 horas.**

---

## 4. Secuencia de ejecución

T-02, T-04 y T-06 primero, que son los casos. T-01 → T-03 → T-05 → T-07 con las dudas resueltas. T-08 y T-09 cierran.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Pendiente cerrado sin fase y con fase | T-01, T-02 |
| CA-02 | Fase inventada y fase que existe | T-03, T-04 |
| CA-03 | Pendiente cerrado por decisión, no reportado | T-05, T-06 |
| CA-04 | Los 17 cerrados, separados por la fecha de corte | T-07, T-08 |

---

## 6. Datos y ambiente de prueba

Este repositorio y carpetas temporales para los casos negativos. Ningún dato real y ninguna clave.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

El estándar está en producción. Exigir la declaración **obliga** a quien cierre un pendiente de aquí en adelante: subida **MAYOR** con su marca, salvo que la duda 2 resuelva que el programa solo avise, y entonces es **MENOR**.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md), [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Las dos dudas sin resolver | Bloquean el programa | Se presentan al usuario |
| R-01 | Que sin fecha de corte el primer día reporte 17 incumplimientos | Nadie lo mira | El CA-04 existe para eso, y es parte del alcance |
| R-02 | Que un pendiente cerrado nombre una fase que se renombró después | Falso positivo por un cambio legítimo | Se reporta como aviso y se arregla la cita, que es lo que el pendiente [54](../../../../../pendientes/hecho/cerrar-un-pendiente-arrastra-sus-citas.md) ya tiene planteado |
| R-03 | Que la declaración se vuelva un trámite que se llena de cualquier manera | La trazabilidad queda de adorno | La fase declarada se resuelve contra el árbol: un nombre inventado se reporta |

---

## 11. Definition of Done

- [ ] Un pendiente cerrado sin fase se reporta.
- [ ] Una fase que no existe se reporta.
- [ ] El pendiente que no fue desarrollo no se reporta.
- [ ] Lo cerrado antes de la fecha de corte queda separado y contado aparte.
- [ ] `pendientes/README.md` dice dónde se declara la fase.
- [ ] `CHANGELOG.md` con su entrada y `VERSION` subida, con el tipo que corresponda.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
