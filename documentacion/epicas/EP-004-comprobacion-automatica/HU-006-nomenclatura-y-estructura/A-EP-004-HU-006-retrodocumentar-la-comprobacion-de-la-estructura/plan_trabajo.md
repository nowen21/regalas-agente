# Plan de Trabajo — Fase A-EP-004-HU-006-retrodocumentar-la-comprobacion-de-la-estructura (módulo Comprobación automática)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-006](../HU-006-nomenclatura-y-estructura.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-006-retrodocumentar-la-comprobacion-de-la-estructura` |
| **Épica** | [EP-004 Comprobación automática](../../epica.md) |
| **HU** | [HU-006 Comprobar la nomenclatura y la estructura de carpetas del trabajo](../HU-006-nomenclatura-y-estructura.md) — una sola (`F12.1`) |
| **Módulo** | Comprobación automática |
| **Especificación del módulo** | [HU-006](../HU-006-nomenclatura-y-estructura.md). El entregable es un programa de comprobación: sus criterios de aceptación y `02·F12` son la especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-004-HU-006-retrodocumentar-la-comprobacion-de-la-estructura` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md)). El programa existe y corre todos los días: [`validadores/fases.py`](../../../../../validadores/fases.py) comprueba nueve partes de [`02·F12`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md) por `validar.py fases`, con su documentación en [`validadores/docs/fases.md`](../../../../../validadores/docs/fases.md). Sale de la fila de HU-006 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-006 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-006-nomenclatura-y-estructura.md#ca-01--un-identificador-fuera-de-convención-se-reporta) | Un identificador fuera de convención se reporta | Corriendo: `F12.6` y `F12.12`, con la variante de complemento incluida. Sin prueba propia de esta HU |
| [CA-02](../HU-006-nomenclatura-y-estructura.md#ca-02--un-hueco-en-la-numeración-se-reporta) | Un hueco en la numeración se reporta | Corriendo: `F12.5` y `F12.7` — el consecutivo alfabético no se salta ni se repite. Sin prueba propia |
| [CA-03](../HU-006-nomenclatura-y-estructura.md#ca-03--una-fase-sin-sus-documentos-se-reporta) | Una fase sin sus documentos se reporta | Corriendo: `F12.13`. **Hoy reporta 54 avisos** — 44 HU sin fase y las fases abiertas en esta sesión, a las que les faltan cuatro documentos |

**Por qué una sola fase.** Los tres CA los comprueba el mismo programa en la misma corrida (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar escrito qué parte de `02·F12` comprueba el programa y qué parte no, con prueba de los tres casos y la cuenta de hoy como línea base.

**Fuera de alcance:**

- **Arreglar los 54 avisos.** Cada uno es de la fase de otra HU: acá se cuentan.
- **Las partes de `F12` que el programa no mira** —`F12.8`, `F12.9` y `F12.10`, que piden criterio—: se declaran como no comprobables, no se construyen.
- **La estructura base del proyecto,** que es [`02·F13`](../../../../../base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md) y la revisa otro programa.
- **El veredicto de la fase,** ya retro-documentado en [HU-014](../../HU-014-un-solo-veredicto-por-fase/HU-014-un-solo-veredicto-por-fase.md).

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 corriendo `validar.py fases`: 0 fallas y 54 avisos.

**Lo que ya existe:** el programa, con nueve partes de `F12` comprobadas; su documentación, que dice qué mira y qué no; la decisión escrita de no exigir un formato de número que la norma no fija —hay proyectos que alternan `HU-01` y `HU-013`—; y el veredicto por fase, que se sumó en la fase A de HU-014.

**Lo que no existe:**

1. **La prueba por criterio de esta HU.** Hay pruebas del programa en la suite, y ninguna atada a estos tres criterios de aceptación.
2. **La declaración de qué parte de `F12` queda sin comprobar** y por qué: hoy está en el comentario de cabecera del programa, no en un documento que alguien vaya a leer.
3. **La línea base de la cuenta.** Los 54 avisos de hoy no están anotados en ninguna parte, así que mañana no se puede decir si bajaron.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/docs/fases.md` | Modificar | Le entra qué parte de `F12` se comprueba y qué parte no, con el motivo |
| `validadores/pruebas.py` | Modificar | Los tres casos de esta HU, si no están cubiertos |
| `…/A-EP-004-HU-006-…/plan_pruebas.md` | Nuevo | Los casos de los tres CA |
| `…/A-EP-004-HU-006-…/resultado_pruebas.md` | Nuevo | Lo que dieron, con los 54 avisos de línea base |
| `HU-006-nomenclatura-y-estructura.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> `fases.py` no se toca: hace lo que la HU pide.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: se agregan pruebas y documentación sobre lo que ya corre.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque son programas de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

**Sí tiene punto de entrada:** `python validadores/validar.py fases`.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Las partes de `F12` que piden criterio se declaran no comprobables | Intentar comprobarlas | Una comprobación que se equivoca vale menos que ninguna, y `F12.10` —que una fase represente trabajo real— no lo decide un programa |
| La cuenta de avisos se anota con su fecha | Anotar solo el número | Sin fecha el número no sirve para comparar |
| Los casos negativos se arman en carpeta temporal | Romper a propósito una fase del repositorio | Romper el árbol real deja el repositorio en rojo para las demás sesiones |

### 2.7 Dudas por resolver antes de escribir

Ninguna: todo lo que la fase afirma se verificó contra el repositorio.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Un identificador fuera de convención se reporta

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Caso de prueba: una fase con el nombre mal armado se reporta, y una con complemento válido no | `plan_pruebas.md` | 2,0 |

### CA-02 — Un hueco en la numeración se reporta

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-02 | Caso de prueba: una HU con fases `A` y `C` se reporta; con `A` y `B` no | `plan_pruebas.md` | 1,5 |

### CA-03 — Una fase sin sus documentos se reporta

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Caso de prueba: una fase con solo su plan se reporta diciendo qué cuatro le faltan | `plan_pruebas.md` | 1,5 |
| T-04 | Anotar los 54 avisos de hoy como línea base, con su fecha | `resultado_pruebas.md` | 1,0 |

### RNF — Que quede dicho qué no se comprueba

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-05 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 5 tareas · 7,5 horas.**

---

## 4. Secuencia de ejecución

T-01 → T-02 → T-03 primero, que son los tres casos. T-04 con la corrida. T-05 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Nombre mal armado y nombre con complemento válido | T-01 |
| CA-02 | Consecutivo con hueco y sin hueco | T-02 |
| CA-03 | Fase con solo su plan, y la cuenta de hoy | T-03, T-04 |

---

## 6. Datos y ambiente de prueba

Este repositorio y carpetas temporales para los casos negativos. Ningún dato real y ninguna clave: lo que parezca una clave se arma para la prueba.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No aplica: el programa no se toca. Sin subida de versión.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`02·F12`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md), [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que la cuenta de 54 cambie mientras se trabaja, porque se abren fases | La línea base nace vieja | Se cuenta al final y se escribe contra qué día |
| R-02 | Que las pruebas nuevas repitan las que ya están en la suite | Trabajo doble | Se lee primero qué cubre la suite y se escriben solo las que falten |
| R-03 | Que otra sesión esté tocando `validadores/pruebas.py` | Pisar trabajo ajeno | Se guarda solo lo propio |

---

## 11. Definition of Done

- [ ] La documentación del programa dice qué parte de `F12` se comprueba y qué parte no.
- [ ] Los tres casos están escritos y corridos.
- [ ] Los 54 avisos quedaron anotados con su fecha, como línea base.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
