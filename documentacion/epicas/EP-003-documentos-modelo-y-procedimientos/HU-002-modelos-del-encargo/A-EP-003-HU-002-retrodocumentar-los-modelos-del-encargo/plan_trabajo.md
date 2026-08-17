# Plan de Trabajo — Fase A-EP-003-HU-002-retrodocumentar-los-modelos-del-encargo (módulo Documentos modelo)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-002](../HU-002-modelos-del-encargo.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-003-HU-002-retrodocumentar-los-modelos-del-encargo` |
| **Épica** | [EP-003 Documentos modelo y procedimientos](../../epica.md) |
| **HU** | [HU-002 Crear los modelos del encargo: brief, épica, historia de usuario](../HU-002-modelos-del-encargo.md) — una sola (`F12.1`) |
| **Módulo** | Documentos modelo |
| **Especificación del módulo** | [documentacion/documentos-modelo/spec.md](../../../../documentos-modelo/spec.md). Existe y crece por incrementos; esta fase le agrega el suyo (`02·F2`) |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-003-HU-002-retrodocumentar-los-modelos-del-encargo` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md)). Los tres modelos existen y se usan todos los días: [`plantillas/planteamiento.md`](../../../../../plantillas/planteamiento.md), [`plantillas/epica.md`](../../../../../plantillas/epica.md) y [`plantillas/HU.md`](../../../../../plantillas/HU.md), con [`13·DOC16`](../../../../../base/13-documentacion/reglas/DOC16-crea-la-epica-desde-la-plantilla-central.md) y [`13·DOC15`](../../../../../base/13-documentacion/reglas/DOC15-crea-la-historia-de-usuario-desde-la-plantilla-central.md) obligando a nacer de ellos. Sale de la fila de HU-002 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-002 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-002-modelos-del-encargo.md#ca-01--los-tres-modelos-existen-y-se-encadenan) | Los tres modelos existen y se encadenan | Los tres existen. Que se encadenen se ve en las 68 HU escritas; sin prueba |
| [CA-02](../HU-002-modelos-del-encargo.md#ca-02--la-historia-trae-criterios-que-se-pueden-comprobar) | La historia trae criterios que se pueden comprobar | Cumplido: las 68 traen sus CA en forma de escenario. Sin prueba |
| [CA-03](../HU-002-modelos-del-encargo.md#ca-03--un-encargo-llenado-a-medias-se-nota) | Un encargo llenado a medias se nota | Corriendo por [`validar.py plantilla`](../../../../../validadores/plantillas.py), con la marca de hueco de [HU-001](../../HU-001-marca-de-espacio-por-llenar/HU-001-marca-de-espacio-por-llenar.md) |

**Por qué una sola fase.** Los tres CA se comprueban sobre los mismos tres modelos y con la misma corrida (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar en la especificación del módulo qué exigen los tres modelos del encargo y cómo se encadenan, con prueba de que un encargo a medias se nota.

**Fuera de alcance:**

- **Escribir el planteamiento de este repositorio.** Falta —es el pendiente [56](../../../../../pendientes/56-el-estandar-no-tiene-planteamiento.md)— y no se puede reconstruir leyendo el repositorio: sale de una conversación.
- **Los modelos de la fase,** que son [HU-003](../../HU-003-modelos-de-la-fase/HU-003-modelos-de-la-fase.md).
- **La marca del hueco,** ya cerrada en la fase A de [HU-001](../../HU-001-marca-de-espacio-por-llenar/HU-001-marca-de-espacio-por-llenar.md). Acá se usa como línea base.
- **Cambiar los tres modelos.** Si aparece algo que falta, se propone: son `plantillas/` y suben versión.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 leyendo los tres modelos y contando las 68 HU escritas del árbol de épicas.

**Lo que ya existe:** el modelo del planteamiento, que declara ser el insumo de entrada y no la especificación; el de la épica y el de la historia, con sus reglas `DOC16` y `DOC15` que obligan a usarlos; el validador que compara un documento contra su modelo; la marca de hueco, que hace visible lo que quedó sin llenar.

**Lo que no existe:**

1. **El incremento en la especificación del módulo.** La spec cubre hoy la marca, el resumen de sesión y el glosario; los tres modelos del encargo no están.
2. **La prueba del encadenamiento.** Que la épica nombre sus historias y cada historia su épica se cumple, y ninguna prueba lo sostiene.
3. **El planteamiento de esta casa.** El modelo existe y este repositorio no lo usó: `prompts/` tiene cuarenta archivos y ninguno es un planteamiento.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `documentacion/documentos-modelo/spec.md` | Modificar | Le entra el incremento: los tres modelos del encargo y su encadenamiento |
| `…/A-EP-003-HU-002-…/plan_pruebas.md` | Nuevo | Los casos de los tres CA |
| `…/A-EP-003-HU-002-…/resultado_pruebas.md` | Nuevo | Lo que dieron |
| `validadores/pruebas.py` | Modificar | Prueba del encadenamiento: toda HU nombra su épica y toda épica lista sus HU |
| `HU-002-modelos-del-encargo.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> `plantillas/` no se toca.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: la especificación crece por incrementos y no cambia lo ya escrito en ella; la prueba nueva no toca ningún contrato.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque el entregable son modelos de documento.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

No aplica. Los modelos se usan copiándolos al proyecto, y el validador se corre por línea de comandos.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El encadenamiento se prueba sobre las 68 HU reales | Armar una épica de prueba con dos historias | Las 68 traen los casos raros que un ejemplo armado no tiene |
| El planteamiento de esta casa no se escribe acá | Redactarlo leyendo el repositorio | El pendiente 56 lo advierte: saldría describiendo la solución en vez del problema, y apagaría el aviso sin arreglar nada |
| Lo que falte a los modelos se propone | Corregirlo de paso | Son `plantillas/` y suben versión ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)) |

### 2.7 Dudas por resolver antes de escribir

Ninguna: los tres CA se prueban contra lo que ya está.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Los tres modelos existen y se encadenan

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Escribir el incremento en la especificación: qué pide cada modelo y cómo se pasa del uno al otro | `documentos-modelo/spec.md` | 2,5 |
| T-02 | Prueba: toda HU nombra su épica y toda épica lista sus HU | `validadores/pruebas.py` | 2,0 |

### CA-02 — La historia trae criterios que se pueden comprobar

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Caso de prueba: tomar tres HU y comprobar que cada CA dice cómo se valida y cuándo se aprueba | `plan_pruebas.md` | 1,5 |

### CA-03 — Un encargo llenado a medias se nota

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-04 | Caso de prueba: llenar a medias una copia de cada modelo y comprobar que `validar.py plantilla` lo dice | `plan_pruebas.md` | 1,5 |
| T-05 | Dejar escrito el caso del planteamiento que le falta a esta casa, atado al pendiente [56](../../../../../pendientes/56-el-estandar-no-tiene-planteamiento.md) | `resultado_pruebas.md` | 1,0 |

### RNF — Que el modelo se entienda sin explicación

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-06 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 6 tareas · 10,0 horas.**

---

## 4. Secuencia de ejecución

T-02 → T-03 → T-04 primero, que son medición. T-01 con lo que salga de ellas. T-05 y T-06 cierran.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Prueba automática del encadenamiento sobre las 68 HU | T-02 |
| CA-02 | Tres HU revisadas por sus criterios | T-03 |
| CA-03 | Copias a medias contra `validar.py plantilla` | T-04, y la constancia de T-05 |

---

## 6. Datos y ambiente de prueba

Este repositorio, y carpetas temporales para las copias a medias. Ningún dato real y ninguna clave.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. Lo único ejecutable que entra es una prueba.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No aplica: la especificación es documentación del módulo y no cambia lo que corre en los proyectos instalados. Sin subida de versión, porque no se toca `base/` ni `plantillas/`.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F2`](../../../../../base/02-flujo-de-trabajo/reglas/F2-sin-spec-acordada-no-hay-codigo.md), [`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`13·DOC15`](../../../../../base/13-documentacion/reglas/DOC15-crea-la-historia-de-usuario-desde-la-plantilla-central.md), [`13·DOC16`](../../../../../base/13-documentacion/reglas/DOC16-crea-la-epica-desde-la-plantilla-central.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que la prueba del encadenamiento falle en varias HU viejas | Suite roja por deuda heredada | Se listan y se anotan; corregirlas es trabajo aparte con su propia fase | Abierto |
| R-02 | Que la especificación crezca describiendo los modelos en vez de exigirles | Documento largo que nadie usa | El incremento dice qué se exige y enlaza el modelo, no lo copia | Abierto |
| R-03 | Que otra sesión esté tocando la especificación del módulo | Pisar trabajo ajeno | Se relee justo antes de escribir | Abierto |

---

## 11. Definition of Done

- [ ] La especificación del módulo cubre los tres modelos del encargo y su encadenamiento.
- [ ] Hay prueba de que toda HU nombra su épica y toda épica lista sus HU.
- [ ] Un encargo a medias queda detectado, con caso escrito.
- [ ] El planteamiento que le falta a esta casa quedó anotado, sin inventarlo.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
