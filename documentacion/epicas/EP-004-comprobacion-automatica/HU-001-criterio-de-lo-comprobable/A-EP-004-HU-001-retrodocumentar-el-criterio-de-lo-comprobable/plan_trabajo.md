# Plan de Trabajo — Fase A-EP-004-HU-001-retrodocumentar-el-criterio-de-lo-comprobable (módulo Comprobación automática)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-001](../HU-001-criterio-de-lo-comprobable.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-001-retrodocumentar-el-criterio-de-lo-comprobable` |
| **Épica** | [EP-004 Comprobación automática](../../epica.md) |
| **HU** | [HU-001 Fijar el criterio de qué se comprueba con un programa](../HU-001-criterio-de-lo-comprobable.md) — una sola (`F12.1`) |
| **Módulo** | Comprobación automática |
| **Especificación del módulo** | [HU-001](../HU-001-criterio-de-lo-comprobable.md). El entregable es un criterio escrito, no código: sus criterios de aceptación son la especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-004-HU-001-retrodocumentar-el-criterio-de-lo-comprobable` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md)). El criterio existe y se aplicó a las 188 reglas: está escrito en [`validadores/reglas-validables.md`](../../../../../validadores/reglas-validables.md) —«si un script puede decir sí o no sin opinar, es validable; si dos personas pueden discutir si se cumplió, se queda en el documento»— y [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md) obliga a declararlo. Sale de la fila de HU-001 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-001 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-001-criterio-de-lo-comprobable.md#ca-01--el-criterio-existe-y-se-puede-citar) | El criterio existe y se puede citar | Cumplido en forma: está escrito. **Pero vive en `validadores/`, no en `base/`**, así que se cita como documento de esta casa y no como regla que se hereda |
| [CA-02](../HU-001-criterio-de-lo-comprobable.md#ca-02--una-regla-que-se-discute-queda-afuera) | Una regla que se discute queda afuera | Aplicado: unas 100 reglas están clasificadas como criterio humano. Sin prueba |
| [CA-03](../HU-001-criterio-de-lo-comprobable.md#ca-03--una-regla-comprobable-a-medias-se-parte) | Una regla comprobable a medias se parte | Aplicado en el registro, que marca cuatro reglas como pesadas o difusas. Sin prueba |

**Por qué una sola fase.** Los tres CA se comprueban sobre el mismo registro y el mismo criterio (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar el criterio citable desde una regla, y probado sobre casos reales de las tres clases: validable, humana y validable a medias.

**Fuera de alcance:**

- **Reclasificar reglas.** El registro está al día desde el 2026-08-16; si aparece una mal clasificada, se anota.
- **La marca en cada regla,** que es [HU-002](../../HU-002-marca-de-comprobable-en-cada-regla/HU-002-marca-de-comprobable-en-cada-regla.md).
- **Escribir los validadores que faltan,** que son las 22 marcadas como pendientes en el registro y el pendiente [01](../../../../../pendientes/01-validadores-de-codigo-de-proyecto.md).

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 leyendo el registro, que se puso al día en la fase A de [EP-001 · HU-009](../../../EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/A-EP-001-HU-009-clasificar-las-que-faltan/README.md).

**Lo que ya existe:** el criterio, en dos líneas y con su ejemplo implícito; la advertencia de que muchas reglas validables necesitan un proyecto real y no se pueden comprobar en seco; el conteo por categoría —unas 53 ya son validadores, unas 22 validables y sin escribir, unas 100 de criterio humano—; `20·M9`, que obliga a que cada regla declare si es validable; y la fila 18 del [checklist](../../../../../base/20-meta-reglas/checklist.md), que lo comprueba.

**Lo que no existe:**

1. **El criterio como regla.** Vive en `validadores/reglas-validables.md`, que es de esta casa. Un proyecto que hereda recibe `M9` —la obligación de declarar— y no el criterio con que se decide.
2. **La prueba de las tres clases.** Ninguna de las 246 pruebas toma una regla y comprueba que su clasificación es la que el criterio le da.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `base/20-meta-reglas/reglas/M9-…md` | Modificar | Le entra el criterio, o el enlace al documento que lo tiene, según la duda 1 |
| `validadores/reglas-validables.md` | Modificar | Queda apuntando a donde viva el criterio, para no tener dos versiones |
| `…/A-EP-004-HU-001-…/plan_pruebas.md` | Nuevo | Los casos de los tres CA |
| `…/A-EP-004-HU-001-…/resultado_pruebas.md` | Nuevo | Lo que dieron |
| `HU-001-criterio-de-lo-comprobable.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `CHANGELOG.md` · `VERSION` | Modificar | Si toca `M9`: entrada y subida ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)) |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

### 2.2 Matriz de dependencias del refactor  ·  `F17`

| Archivo que cambia | Qué cambia | Quién depende | Dónde |
|---|---|---|---|
| `M9` | Le entra el criterio | El checklist del estándar, fila 18, y la clasificación de las 188 reglas | El sello del checklist de `M9` queda anulado al cambiar su texto y hay que rehacerlo (`20·M14`) |

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque el entregable es texto normativo.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

No aplica. El criterio se lee al ir a clasificar una regla.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El criterio queda en un solo sitio y el otro documento lo enlaza | Dejarlo escrito en los dos | La fila 11 del checklist prohíbe el texto prestado, y dos copias se separan solas |
| Las reglas mal clasificadas se anotan | Reclasificarlas de paso | Reclasificar cambia lo que se exige comprobar, y eso es decisión del usuario |
| Las pruebas toman reglas reales de cada clase | Inventar tres reglas de ejemplo | Una regla inventada no discute: el CA-02 necesita una sobre la que dos personas puedan discutir de verdad |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién | Estado |
|---|---|---|---|
| 1 | Si el criterio entra al cuerpo de `M9` o si `M9` lo enlaza y el criterio se queda en `validadores/` | Usuario | Pendiente |

La duda 1 bloquea T-01 y T-02. Las pruebas no dependen de ella.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — El criterio existe y se puede citar

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Escribir el criterio donde decida la duda 1, y dejar el otro documento enlazando | `base/20-meta-reglas/reglas/M9-…md` · `reglas-validables.md` | 2,0 |
| T-02 | Rehacer el bloque de checklist de `M9` si su texto cambió | `base/20-meta-reglas/reglas/M9-…md` | 1,5 |

### CA-02 — Una regla que se discute queda afuera

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Caso de prueba: tomar tres reglas clasificadas como criterio humano y comprobar que el criterio las deja afuera | `plan_pruebas.md` | 1,5 |

### CA-03 — Una regla comprobable a medias se parte

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-04 | Caso de prueba: tomar las cuatro marcadas como difusas o pesadas y decir qué mitad se comprueba y qué mitad no | `plan_pruebas.md` | 2,0 |

### RNF — Que la clasificación no se vuelva a perder

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-05 | Anotar el conteo por categoría del día de la corrida, para poder comparar más adelante | `resultado_pruebas.md` | 1,0 |
| T-06 | Versionar si tocó `base/`, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 6 tareas · 9,5 horas.**

---

## 4. Secuencia de ejecución

T-03 → T-04 → T-05 primero: son lectura. T-01 → T-02 con la duda resuelta. T-06 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | El criterio citado desde otro documento por su identificador | T-01 |
| CA-02 | Tres reglas de criterio humano contra el criterio | T-03 |
| CA-03 | Las cuatro difusas, partidas en la mitad comprobable y la que no | T-04 |
| RNF | Conteo por categoría anotado con su fecha | T-05 |

---

## 6. Datos y ambiente de prueba

Este repositorio. Todo es lectura. Ningún dato real y ninguna clave.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase: devuelve `M9`, el registro y `VERSION`.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

Se asume que el estándar está en producción. Escribir el criterio dentro de `M9` es **aditivo**: no obliga a reclasificar nada, así que la subida es **MENOR**.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), [`20·M14`](../../../../../base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | La duda 1 sin resolver | Bloquea el CA-01 | Se presenta al usuario: tocar `M9` sube versión | Abierto |
| R-01 | Que al probar aparezcan reglas mal clasificadas | Se destapa trabajo del pendiente [19](../../../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md) | Se anotan; reclasificar es decisión del usuario | Abierto |
| R-02 | Que el criterio, escrito como regla, quede tan corto que no decida nada | Vuelve a decidirse a ojo | El caso del CA-03 es la prueba: si con el criterio no se puede partir una regla difusa, falta texto | Abierto |

---

## 11. Definition of Done

- [ ] El criterio se puede citar por identificador, y está en un solo sitio.
- [ ] Tres reglas de criterio humano quedaron probadas contra él.
- [ ] Las cuatro difusas quedaron partidas en lo que se comprueba y lo que no.
- [ ] El conteo por categoría quedó anotado con su fecha.
- [ ] `CHANGELOG.md` con su entrada y `VERSION` subida, si tocó `base/`.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
