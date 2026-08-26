# Plan de Trabajo — Fase A-EP-002-HU-002-retrodocumentar-el-registro-de-cambios (módulo Versionado y adopción)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-002](../HU-002-registro-de-cambios.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-002-HU-002-retrodocumentar-el-registro-de-cambios` |
| **Épica** | [EP-002 Versionado y adopción](../../epica.md) |
| **HU** | [HU-002 Llevar el registro de qué cambió en cada versión](../HU-002-registro-de-cambios.md) — una sola (`F12.1`) |
| **Módulo** | Versionado y adopción |
| **Especificación del módulo** | [HU-002](../HU-002-registro-de-cambios.md). El entregable es un documento de registro: sus criterios de aceptación son la especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-002-HU-002-retrodocumentar-el-registro-de-cambios` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md)). El registro existe y lleva 23 versiones anotadas: [`CHANGELOG.md`](../../../../../CHANGELOG.md), con su cabecera que define los tres tipos y la regla de retroactividad, y [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md) que lo obliga. Sale de la fila de HU-002 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-002 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-002-registro-de-cambios.md#ca-01--cada-versión-tiene-su-entrada) | Cada versión tiene su entrada | Comprobable por la fila 19 del [checklist](../../../../../base/20-meta-reglas/checklist.md), y el programa que la mira **no se puede correr** |
| [CA-02](../HU-002-registro-de-cambios.md#ca-02--un-cambio-sin-entrada-no-pasa) | Un cambio sin entrada no pasa | **Nada lo impide hoy.** `M10` lo exige y ningún enganche frena el cambio sin entrada |
| [CA-03](../HU-002-registro-de-cambios.md#ca-03--el-registro-se-entiende-sin-haber-seguido-el-cambio) | El registro se entiende sin haber seguido el cambio | Se cumple por costumbre. Sin prueba |

**Por qué una sola fase.** Los tres CA se comprueban sobre el mismo archivo (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar comprobado que ninguna de las 23 versiones se quedó sin entrada, que cada entrada trae lo que la RN-02 pide, y que el registro se entiende sin haber seguido el cambio.

**Fuera de alcance:**

- **Frenar el cambio sin entrada con un enganche.** Eso es [EP-005 · HU-005](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-005-cambio-de-reglas-con-version/HU-005-cambio-de-reglas-con-version.md), no esta fase.
- **Darle punto de entrada a `metareglas.py`,** donde vive la fila 19. Pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md), punto 2.
- **El registro por proyecto** (`documentacion/versiones/`), que es [HU-003](../../HU-003-version-adoptada-por-el-proyecto/HU-003-version-adoptada-por-el-proyecto.md) y arrastra los pendientes [44](../../../../../pendientes/hecho/el-registro-no-se-escribe-si-no-cambia-la-huella.md) y [46](../../../../../pendientes/hecho/el-registro-se-escribe-antes-de-contarse.md).
- **Reescribir entradas viejas.** La RN-04 lo prohíbe: el registro es rastro.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 sobre `CHANGELOG.md` y `VERSION` (`23.2.0`).

**Lo que ya existe:** el registro con las 23 versiones; su cabecera, que define MAYOR, MENOR y PARCHE y la marca `⚠ obliga a migrar`; la regla de retroactividad escrita ahí mismo; `M10`, que obliga a entrada y subida en el mismo cambio.

**Lo que no existe:**

1. **La prueba de que no falta ninguna entrada.** Lo decidiría la fila 19, y su programa no corre.
2. **Algo que impida el cambio sin entrada.** Hoy depende de que quien edita se acuerde.
3. **La prueba de que cada entrada nombra las reglas que cambiaron** por su identificador (RN-05).

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `…/A-EP-002-HU-002-…/plan_pruebas.md` | Nuevo | Los casos de los tres CA |
| `…/A-EP-002-HU-002-…/resultado_pruebas.md` | Nuevo | Lo que dieron, con la lista de entradas incompletas si aparece alguna |
| `validadores/pruebas.py` | Modificar | Prueba: la versión de `VERSION` tiene entrada, y ninguna entrada del registro se salta el formato de la RN-02 |
| `HU-002-registro-de-cambios.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> El `CHANGELOG` no se toca.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: se agrega una prueba y no cambia el contrato de ningún validador.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque el entregable es un documento y una prueba de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

No aplica. El registro se lee abriendo el archivo.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La prueba se escribe en `pruebas.py`, no dentro de `metareglas.py` | Arreglar la fila 19 donde vive | `metareglas.py` no se puede correr, y una comprobación que no corre no comprueba nada |
| Las entradas incompletas se listan, no se completan | Rellenarlas ahora | La RN-04 dice que el registro no se reescribe; lo que falte se anota como hallazgo |
| El CA-03 se prueba con un lector que no siguió el cambio | Juzgarlo quien lo escribió | Quien lo escribió entiende su propia entrada por definición |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién | Estado |
|---|---|---|---|
| 1 | Quién hace de lector del CA-03 — tiene que ser alguien que no siguió los cambios | Usuario | **Resuelta el 2026-08-22:** el lector fue la propia comprobación de `M17`, que reprobó una entrada escrita ese día. Es mejor lector que el previsto, porque no puede ser indulgente |

La duda 1 bloquea T-05. Los demás CA no dependen de ella.

**Decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md). 👤 marca lo que sigue esperando un dato del usuario.

| Duda | Decisión |
|---|---|
| 17 | 👤 **Propuesta: el usuario, leyendo una entrada del registro de una versión que no siguió.** Es el único lector que cumple la condición. |
---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Cada versión tiene su entrada

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Prueba: la versión de `VERSION` tiene su entrada, y no hay versión mencionada sin entrada propia | `validadores/pruebas.py` | 2,0 |
| T-02 | Caso de prueba: recorrer las 23 y comprobar que cada una trae versión, fecha, tipo, qué cambió y por qué | `plan_pruebas.md` | 2,0 |

### CA-02 — Un cambio sin entrada no pasa

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Caso de prueba: editar una regla en copia y comprobar qué avisa hoy — se espera que nada lo frene | `plan_pruebas.md` | 1,5 |
| T-04 | Dejar escrito que la exigencia hoy no tiene quién la haga cumplir, y atarlo a EP-005 · HU-005 | `resultado_pruebas.md` | 1,0 |

### CA-03 — El registro se entiende sin haber seguido el cambio

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-05 | Caso de prueba: alguien que no siguió los cambios lee tres entradas y dice qué cambió y a quién le afecta | `plan_pruebas.md` | 1,5 |

### RNF — Que cada entrada cite por identificador

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-06 | Prueba: toda entrada que dice haber cambiado una regla la nombra por su identificador (RN-05) | `validadores/pruebas.py` | 2,0 |
| T-07 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 7 tareas · 11,5 horas.**

---

## 4. Secuencia de ejecución

T-01 → T-06 primero, que comparten el recorrido del registro. T-02, T-03 y T-04 en paralelo. T-05 espera la duda 1. T-07 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Prueba automática más el recorrido de las 23 entradas | T-01, T-02 |
| CA-02 | Edición en copia, para ver qué avisa hoy | T-03, y la constancia de T-04 |
| CA-03 | Lectura por alguien ajeno a los cambios | T-05 |
| RNF | Prueba automática de la cita por identificador | T-06 |

---

## 6. Datos y ambiente de prueba

Este repositorio, y una copia para la edición del CA-02. Las pruebas leen y no escriben sobre el registro. Ningún dato real y ninguna clave.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. Lo único ejecutable que entra son dos pruebas.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No aplica: no cambia nada de lo instalado. Sin subida de versión, porque no se toca `base/` ni `plantillas/`.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`15`](../../../../../base/15-registros-inmutables.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | La duda 1 sin resolver | Bloquea el CA-03 | Elegir el lector con el usuario | Abierto |
| R-01 | Que aparezcan entradas sin todo lo que pide la RN-02 | Se destapa trabajo de fondo | Se listan como hallazgo; el registro no se reescribe | Abierto |
| R-02 | Que la prueba del CA-01 falle por el tramo de las dos numeraciones vivas | Suite roja por un hecho conocido | Se documenta la excepción, atada al pendiente [22](../../../../../pendientes/hecho/dos-sesiones-versionando-a-la-vez.md) | Abierto |
| R-03 | Que otra sesión esté tocando `validadores/pruebas.py` | Pisar trabajo ajeno | Se guarda solo lo propio | Abierto |

---

## 11. Definition of Done

- [ ] Los tres CA tienen su caso escrito y corrido.
- [ ] Ninguna versión sin entrada, y las entradas incompletas están listadas.
- [ ] El CA-02 dice quién debería hacer cumplir la exigencia y que hoy nadie lo hace.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
