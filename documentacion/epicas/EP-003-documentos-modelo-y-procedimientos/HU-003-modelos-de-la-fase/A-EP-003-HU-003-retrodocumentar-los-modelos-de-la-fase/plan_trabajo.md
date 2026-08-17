# Plan de Trabajo — Fase A-EP-003-HU-003-retrodocumentar-los-modelos-de-la-fase (módulo Documentos modelo)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-003](../HU-003-modelos-de-la-fase.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-003-HU-003-retrodocumentar-los-modelos-de-la-fase` |
| **Épica** | [EP-003 Documentos modelo y procedimientos](../../epica.md) |
| **HU** | [HU-003 Crear los modelos de la fase: plan de trabajo, plan de pruebas, cierre](../HU-003-modelos-de-la-fase.md) — una sola (`F12.1`) |
| **Módulo** | Documentos modelo |
| **Especificación del módulo** | [documentacion/documentos-modelo/spec.md](../../../../documentos-modelo/spec.md). Existe y crece por incrementos; esta fase le agrega el suyo (`02·F2`) |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-003-HU-003-retrodocumentar-los-modelos-de-la-fase` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md)). Los cinco modelos de la fase existen y sostienen las 32 fases abiertas del árbol: [`planes/trabajo.md`](../../../../../plantillas/planes/trabajo.md), [`planes/pruebas.md`](../../../../../plantillas/planes/pruebas.md), [`planes/resultados.md`](../../../../../plantillas/planes/resultados.md), [`estado-fase.md`](../../../../../plantillas/estado-fase.md) y [`funcionalidad-implementada.md`](../../../../../plantillas/funcionalidad-implementada.md), con la ruta y los nombres fijados por `02·F12.13`. Sale de la fila de HU-003 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-003 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-003-modelos-de-la-fase.md#ca-01--los-documentos-de-la-fase-existen-y-no-se-pisan) | Los documentos de la fase existen y no se pisan | Cumplido y **comprobado**: [`fases.py`](../../../../../validadores/fases.py) reporta los que faltan (`F12.13`). Sin prueba propia de esta HU |
| [CA-02](../HU-003-modelos-de-la-fase.md#ca-02--el-plan-se-aprueba-antes-y-no-se-reescribe-después) | El plan se aprueba antes y no se reescribe después | Escrito en el modelo, que dice a propósito que el plan no lleva columna de estado. **Nadie comprueba** que no se haya reescrito |
| [CA-03](../HU-003-modelos-de-la-fase.md#ca-03--cada-criterio-de-aceptación-tiene-su-caso-y-cada-tarea-su-criterio) | Cada CA tiene su caso y cada tarea su criterio | Corriendo: [`flujo.py`](../../../../../validadores/flujo.py) lo comprueba por `F18` — hoy avisa en varias fases |

**Por qué una sola fase.** Los tres CA se comprueban sobre los mismos cinco modelos y con las mismas dos corridas (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar en la especificación qué exige cada uno de los cinco modelos y qué pregunta responde, y probar que el plan aprobado no se puede reescribir sin que se note.

**Fuera de alcance:**

- **Los modelos del encargo,** que son [HU-002](../../HU-002-modelos-del-encargo/HU-002-modelos-del-encargo.md).
- **Los avisos de `F18` que ya reporta el revisor** en las fases viejas: se cuentan como línea base y se arreglan en la fase de cada una.
- **El sello de versión en el cierre,** que es [EP-002 · HU-005](../../../EP-002-versionado-y-adopcion/HU-005-sellar-el-trabajo-cerrado/HU-005-sellar-el-trabajo-cerrado.md) y toca los mismos modelos: si las dos fases avanzan, la que llegue segunda relee.
- **Cambiar los cinco modelos.** Lo que falte se propone: son `plantillas/` y suben versión.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 corriendo `validar.py fases` y `validar.py flujo` sobre este repositorio.

**Lo que ya existe:** los cinco modelos, con la tabla de «qué documento responde qué» repetida en cada HU para no buscar en el que no es; la exigencia de que el plan y las pruebas se aprueben antes de tocar código ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)); la separación entre el plan de pruebas —que se aprueba antes— y el resultado, que el usuario pidió el 2026-08-13 justo para no perder la línea base; dos programas que comprueban presencia y desglose.

**Lo que no existe:**

1. **El incremento en la especificación** de los cinco modelos.
2. **La comprobación de que el plan no se reescribió** después de aprobado. El modelo lo dice —el avance en vivo va en el estado de la fase— y nada lo verifica.
3. **La prueba de que los cinco no se pisan** entre sí: qué pregunta contesta cada uno, sin que dos contesten la misma.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `documentacion/documentos-modelo/spec.md` | Modificar | Le entra el incremento: los cinco modelos, qué pide cada uno y qué pregunta responde |
| `…/A-EP-003-HU-003-…/plan_pruebas.md` | Nuevo | Los casos de los tres CA |
| `…/A-EP-003-HU-003-…/resultado_pruebas.md` | Nuevo | Lo que dieron, con la cuenta de avisos de `F18` como línea base |
| `validadores/pruebas.py` | Modificar | Prueba: ningún modelo de la fase pide lo que ya pide otro |
| `HU-003-modelos-de-la-fase.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> `plantillas/` no se toca.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna propia. Cuidado con el cruce: [EP-002 · HU-005](../../../EP-002-versionado-y-adopcion/HU-005-sellar-el-trabajo-cerrado/A-EP-002-HU-005-el-sello-de-version-en-el-cierre/plan_trabajo.md) sí planea tocar dos de estos modelos, y las dos fases no deben correr a la vez sobre ellos.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque el entregable son modelos de documento.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

No aplica. Los modelos se usan copiándolos a la carpeta de la fase.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El CA-02 se prueba por el rastro del control de versiones, no por el contenido | Comparar el plan con una copia guardada aparte | El historial ya guarda cada versión del archivo: una copia paralela sería otro archivo que se desincroniza |
| El solape entre modelos se prueba por «qué pregunta responde» | Comparar sección por sección | Dos modelos pueden compartir una sección y contestar preguntas distintas; lo que no puede repetirse es la pregunta |
| Los avisos de `F18` de las fases viejas se cuentan, no se arreglan | Corregirlos de paso | Cada uno es de la fase de otra HU, y tocarlo sería editar trabajo ajeno |

### 2.7 Dudas por resolver antes de escribir

Ninguna: los tres CA se prueban contra lo que ya está.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Los documentos de la fase existen y no se pisan

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Escribir el incremento: los cinco modelos y qué pregunta responde cada uno | `documentos-modelo/spec.md` | 2,5 |
| T-02 | Prueba: ninguna de las cinco preguntas la responde más de un modelo | `validadores/pruebas.py` | 2,0 |

### CA-02 — El plan se aprueba antes y no se reescribe después

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Caso de prueba: sobre una fase cerrada, comprobar por el historial que el plan no cambió después de aprobado | `plan_pruebas.md` | 2,0 |
| T-04 | Caso de prueba: el plan no lleva columna de estado, y el avance en vivo aparece en el estado de la fase | `plan_pruebas.md` | 1,0 |

### CA-03 — Cada criterio de aceptación tiene su caso y cada tarea su criterio

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-05 | Caso de prueba: correr `validar.py flujo` y comprobar que detecta la tarea sin criterio y el criterio sin desglose | `plan_pruebas.md` | 1,5 |
| T-06 | Anotar la cuenta de avisos de `F18` que hay hoy, como línea base para las fases que los arreglen | `resultado_pruebas.md` | 1,0 |

### RNF — Que no haya dos documentos con la misma respuesta

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-07 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 7 tareas · 11,5 horas.**

---

## 4. Secuencia de ejecución

T-05 → T-06 primero, que son medición con lo que ya corre. T-03 → T-04 después. T-01 con lo que salga, T-02 detrás de T-01. T-07 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Prueba de que las cinco preguntas no se repiten entre modelos | T-02 |
| CA-02 | Historial de una fase cerrada, y la ausencia de columna de estado en el plan | T-03, T-04 |
| CA-03 | Corrida de `validar.py flujo` sobre casos con tarea suelta y criterio sin desglose | T-05, T-06 |

---

## 6. Datos y ambiente de prueba

Este repositorio: las 32 fases del árbol son el material. Carpetas temporales para los casos negativos. Ningún dato real y ninguna clave.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. Lo único ejecutable que entra es una prueba.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No aplica: no cambia lo que corre en los proyectos instalados. Sin subida de versión, porque no se toca `base/` ni `plantillas/`.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F2`](../../../../../base/02-flujo-de-trabajo/reglas/F2-sin-spec-acordada-no-hay-codigo.md), [`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F9`](../../../../../base/02-flujo-de-trabajo/reglas/F9-no-subdividas-ni-renegocies-un-plan-ya-aprobado.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`02·F18`](../../../../../base/02-flujo-de-trabajo/reglas/F18-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que el CA-02 falle en alguna fase donde el plan se editó después de aprobado | Se destapa un incumplimiento de `F9` | Se anota con la fase y la fecha; corregirlo es de esa fase, no de esta | Abierto |
| R-02 | Cruce con la fase de EP-002 · HU-005, que toca dos de estos modelos | Dos sesiones sobre el mismo archivo | La que llegue segunda relee antes de escribir | Abierto |
| R-03 | Que la prueba del solape quede a criterio de quien la escribe | Prueba frágil | La lista de las cinco preguntas se toma de la tabla que ya traen las HU, no se inventa | Abierto |

---

## 11. Definition of Done

- [ ] La especificación cubre los cinco modelos y qué pregunta responde cada uno.
- [ ] Hay prueba de que ninguna pregunta la responden dos modelos.
- [ ] Está comprobado que el plan aprobado no se reescribió, con el caso de una fase cerrada.
- [ ] La cuenta de avisos de `F18` quedó anotada como línea base.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
