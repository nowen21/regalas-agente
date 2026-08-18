# Plan de Trabajo — Fase A-EP-004-HU-002-retrodocumentar-la-clasificacion-de-cada-regla (módulo Comprobación automática)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-002](../HU-002-marca-de-comprobable-en-cada-regla.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-002-retrodocumentar-la-clasificacion-de-cada-regla` |
| **Épica** | [EP-004 Comprobación automática](../../epica.md) |
| **HU** | [HU-002 Marcar en cada regla si es comprobable](../HU-002-marca-de-comprobable-en-cada-regla.md) — una sola (`F12.1`) |
| **Módulo** | Comprobación automática |
| **Especificación del módulo** | [HU-002](../HU-002-marca-de-comprobable-en-cada-regla.md). El entregable es un registro y una obligación escrita: sus criterios de aceptación son la especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-004-HU-002-retrodocumentar-la-clasificacion-de-cada-regla` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md)). La clasificación existe y está completa: [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md) obliga a declararlo, el registro [`validadores/reglas-validables.md`](../../../../../validadores/reglas-validables.md) lo guarda y la fila 18 del [checklist](../../../../../base/20-meta-reglas/checklist.md) lo comprueba. Las 33 sin clasificar bajaron a cero el 2026-08-16. Sale de la fila de HU-002 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-002 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-002-marca-de-comprobable-en-cada-regla.md#ca-01--toda-regla-aparece-clasificada) | Toda regla aparece clasificada | Cumplido desde el 2026-08-16, en la fase A de [EP-001 · HU-009](../../../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/A-EP-001-HU-009-clasificar-las-que-faltan/README.md). **La comprobación que lo vigila no se puede correr** |
| [CA-02](../HU-002-marca-de-comprobable-en-cada-regla.md#ca-02--la-regla-comprobada-dice-quién-la-comprueba) | La regla comprobada dice quién la comprueba | **A medias.** El registro dice qué categoría tiene cada regla; qué programa la comprueba se deduce leyendo `validadores/docs/` |
| [CA-03](../HU-002-marca-de-comprobable-en-cada-regla.md#ca-03--una-regla-nueva-no-se-publica-sin-clasificar) | Una regla nueva no se publica sin clasificar | Exigido por `M9` y por la fila 18. **Nada lo impide** al momento de escribirla: el programa que lo vería no corre |

**Por qué una sola fase.** Los tres CA se comprueban sobre el mismo registro y la misma corrida (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que la clasificación deje de depender de un programa que nadie puede correr — con prueba propia en la suite — y que desde el registro se pueda llegar al programa que comprueba cada regla.

**Fuera de alcance:**

- **Escribir los validadores que faltan.** Son las 22 marcadas como pendientes, y son del pendiente [01](../../../../../pendientes/01-validadores-de-codigo-de-proyecto.md).
- **El criterio con que se clasifica,** que es [HU-001](../../HU-001-criterio-de-lo-comprobable/HU-001-criterio-de-lo-comprobable.md).
- **Darle punto de entrada a `metareglas.py`.** Pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md), punto 2.
- **Reclasificar reglas.** Lo que aparezca mal clasificado se anota.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 leyendo el registro y los 24 subcomandos de `validar.py`.

**Lo que ya existe:** el registro con las 188 reglas repartidas en tres categorías; `20·M9`, que obliga a declararlo; la fila 18 del checklist, que lo comprueba; una carpeta de documentación por validador, en [`validadores/docs/`](../../../../../validadores/docs/README.md), que dice qué hace cada uno.

**Lo que no existe:**

1. **La prueba en la suite.** Ninguna de las 246 pruebas comprueba que toda regla esté clasificada: eso vive en [`metareglas.py`](../../../../../validadores/metareglas.py), que no tiene punto de entrada.
2. **El camino de la regla al programa.** El registro dice la categoría, no qué subcomando la mira.
3. **La lección del rango.** El 2026-08-16 se supo que el programa no lee «C1–C17» como diecisiete reglas: quince estaban clasificadas y aparecían como faltantes. Eso no quedó escrito como caso de prueba.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/pruebas.py` | Modificar | Las pruebas del CA-01 y del CA-03, que hoy no existen |
| `validadores/reglas-validables.md` | Modificar | Le entra la columna de qué programa comprueba cada regla validable |
| `…/A-EP-004-HU-002-…/plan_pruebas.md` | Nuevo | Los casos de los tres CA |
| `…/A-EP-004-HU-002-…/resultado_pruebas.md` | Nuevo | Lo que dieron, con la tabla regla → programa |
| `HU-002-marca-de-comprobable-en-cada-regla.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> `base/` no se toca: `M9` ya exige lo que hace falta.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: se agregan pruebas y una columna a un registro que ningún programa lee por posición.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque son programas de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

**Sí tiene punto de entrada** la parte que corre: `python validadores/pruebas.py`. La que no corre es justamente el hallazgo de esta fase.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La prueba se escribe en `pruebas.py` y no en `metareglas.py` | Arreglar el programa que no corre | Es otro archivo y otro problema, ya anotado en el [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md) |
| El caso del rango se escribe como prueba | Confiar en que ya se corrigió | Fue un diagnóstico falso que costó una sesión: la prueba es para que no vuelva |
| La columna del programa va en el registro | Un documento nuevo con el mapa | Dos documentos sobre lo mismo se separan solos |

### 2.7 Dudas por resolver antes de escribir

Ninguna: todo lo que la fase afirma se verificó contra el repositorio.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Toda regla aparece clasificada

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Prueba: toda regla de `base/` aparece en el registro, y el registro no nombra reglas que no existan | `validadores/pruebas.py` | 2,5 |
| T-02 | Caso de prueba: el registro no se lee por rangos — «C1–C17» no clasifica diecisiete reglas | `plan_pruebas.md` | 1,5 |

### CA-02 — La regla comprobada dice quién la comprueba

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Levantar la tabla regla → programa que la comprueba, contra los 24 subcomandos que existen | `resultado_pruebas.md` | 3,0 |
| T-04 | Caso de prueba: por tres reglas validables, llegar al programa que las mira leyendo solo el registro | `plan_pruebas.md` | 1,5 |

### CA-03 — Una regla nueva no se publica sin clasificar

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-05 | Caso de prueba: escribir una regla en copia sin clasificarla y comprobar qué avisa hoy | `plan_pruebas.md` | 1,5 |
| T-06 | Dejar escrito que la vigilancia depende de un programa sin punto de entrada, atado al pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md) | `resultado_pruebas.md` | 1,0 |

### RNF — Que la clasificación se pueda revisar de una corrida

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-07 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 6 tareas · 11,0 horas.**

---

## 4. Secuencia de ejecución

T-01 → T-02 primero, que son la prueba y su caso borde. T-03 → T-04 en paralelo. T-05 y T-06 cierran.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Prueba automática sobre `base/` contra el registro, más el caso del rango | T-01, T-02 |
| CA-02 | Tabla regla → programa, recorrida por tres reglas | T-03, T-04 |
| CA-03 | Regla nueva sin clasificar en copia, y la constancia de qué no vigila | T-05, T-06 |

---

## 6. Datos y ambiente de prueba

Este repositorio, y carpetas temporales para la regla de mentira del CA-03. Ningún dato real y ninguna clave.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. Lo único ejecutable que entra son dos pruebas.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No aplica: no cambia lo que corre en los proyectos instalados. Sin subida de versión, porque no se toca `base/` ni `plantillas/`.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que la prueba del CA-01 encuentre reglas sin clasificar otra vez | Se destapa trabajo | Se listan y se anotan; clasificarlas es de la fase de EP-001 · HU-009 |
| R-02 | Que la tabla regla → programa quede incompleta porque hay reglas que ningún programa mira | Parece un hueco y es la clasificación correcta | La tabla distingue «no la comprueba nadie porque es humana» de «debería y no está» |
| R-03 | Que otra sesión esté tocando `validadores/pruebas.py` | Pisar trabajo ajeno | Se guarda solo lo propio |

---

## 11. Definition of Done

- [ ] Hay prueba en la suite de que toda regla está clasificada.
- [ ] El caso del rango quedó como prueba, para que el diagnóstico falso no vuelva.
- [ ] Desde el registro se llega al programa que comprueba cada regla validable.
- [ ] El CA-03 dice qué no vigila nadie y dónde quedó anotado.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
