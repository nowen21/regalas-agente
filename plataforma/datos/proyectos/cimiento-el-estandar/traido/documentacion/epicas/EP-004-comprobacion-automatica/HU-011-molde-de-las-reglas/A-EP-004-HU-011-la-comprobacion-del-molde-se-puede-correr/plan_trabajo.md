# Plan de Trabajo — Fase A-EP-004-HU-011-la-comprobacion-del-molde-se-puede-correr (módulo Comprobación automática)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-011](../HU-011-molde-de-las-reglas.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-011-la-comprobacion-del-molde-se-puede-correr` |
| **Épica** | [EP-004 Comprobación automática](../../epica.md) |
| **HU** | [HU-011 Comprobar que cada regla del estándar cumple su propio molde](../HU-011-molde-de-las-reglas.md) — una sola (`F12.1`) |
| **Módulo** | Comprobación automática |
| **Especificación del módulo** | [HU-011](../HU-011-molde-de-las-reglas.md). El entregable es un programa de comprobación: sus criterios de aceptación y el [checklist del estándar](../../../../../base/20-meta-reglas/checklist.md) son la especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-004-HU-011-la-comprobacion-del-molde-se-puede-correr` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 🔀 **Híbrido.** 📄 Retro-documenta lo que está escrito: [`validadores/metareglas.py`](../../../../../validadores/metareglas.py) comprueba once de las veinte filas del checklist —la 5, 6, 7, 10, 12, 13, 14, 15, 18, 19 y 20— más `M14` y, aparte, `M16`. ✨ Y construye lo que falta: **no se puede correr**. `python validadores/metareglas.py` no imprime nada y sale con 0, y `validar.py` no tiene subcomando para él. Es el punto 2 del pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md). Sale de la fila de HU-011 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-011 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-011-molde-de-las-reglas.md#ca-01--un-identificador-repetido-o-con-prefijo-ajeno-se-reporta) | Un identificador repetido o con prefijo ajeno se reporta | Escrito (fila 6) y **sin poder correrse** |
| [CA-02](../HU-011-molde-de-las-reglas.md#ca-02--una-dependencia-que-no-existe-o-que-manda-hacia-arriba-se-reporta) | Una dependencia que no existe o que manda hacia arriba se reporta | Escrito (filas 14 y 15) y sin poder correrse. Es la que protege el núcleo |
| [CA-03](../HU-011-molde-de-las-reglas.md#ca-03--una-regla-sin-su-checklist-se-reporta) | Una regla sin su checklist se reporta | Escrito (`M14`) y sin poder correrse. **Y hay 121 reglas sin bloque de checklist**, según el pendiente [19](../../../../../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md) |
| [CA-04](../HU-011-molde-de-las-reglas.md#ca-04--una-regla-que-nombra-una-tecnología-se-reporta) | Una regla que nombra una tecnología se reporta | Escrito (fila 5, que sostiene `M3`) y sin poder correrse |
| [CA-05](../HU-011-molde-de-las-reglas.md#ca-05--una-regla-del-proyecto-sin-respaldo-en-la-base-se-reporta) | Una regla del proyecto sin respaldo en la base se reporta | Escrito aparte (`M16`, sobre el catálogo del proyecto) y sin poder correrse |

**Por qué una sola fase.** Los cinco CA los comprueba el mismo programa, y ninguno se puede probar hasta que el programa se pueda correr (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que la comprobación del molde se pueda correr — hoy calla con código 0 — y que sus cinco casos queden probados.

**Fuera de alcance:**

- **Arreglar las 121 reglas sin checklist ni las siete publicadas en «no cumple».** Es el pendiente [19](../../../../../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md); acá se mide.
- **Revisar los otros treinta programas** del pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md): esta fase arregla el que su HU cubre.
- **Cambiar el checklist ni el molde,** que son de EP-001.
- **Las nueve filas que piden leer y entender.** El programa no las simula, y así se queda.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17: el programa tiene `validar()` y `validar_catalogo()`, ningún bloque de arranque, y `validar.py --help` no lo lista.

**Lo que ya existe:** el programa entero, con las once filas comprobables y el criterio escrito de por qué las otras nueve no se simulan; la tabla de qué fila mira cada comprobación, en su propia cabecera; el registro de reglas validables; y la medición del 2026-08-14 que se hizo con él y hoy no se puede repetir por la línea de comandos.

**Lo que no existe:**

1. **El punto de entrada.** Sin él, el programa calla y ese silencio se lee igual que «todo bien».
2. **La prueba de los cinco casos.** Ninguno está en la suite.
3. **La cuenta al día.** El pendiente 19 habla de 121 reglas sin bloque de checklist, medidas cuando el programa se podía correr.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/validar.py` | Modificar | El subcomando que corre la comprobación del molde, y la del catálogo de un proyecto |
| `validadores/metareglas.py` | Modificar | Bloque de arranque propio, o un aviso de por dónde se corre — nunca terminar en silencio |
| `validadores/pruebas.py` | Modificar | Los cinco casos |
| `validadores/docs/metareglas.md` | Nuevo | La documentación del programa, que hoy no está en `docs/` |
| `pendientes/53-enlaces-py-no-tiene-punto-de-entrada.md` | Modificar | Se marca este caso como resuelto, sin cerrar el pendiente |
| `pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md` | Modificar | Se corrige la cuenta con lo que dé la corrida |
| `…/A-EP-004-HU-011-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron |
| `HU-011-molde-de-las-reglas.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> Las comprobaciones no se cambian: se les abre la puerta. Si al correrlas aparece que alguna está mal, se para y se propone.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

| Archivo que cambia | Qué cambia | Quién depende | Dónde |
|---|---|---|---|
| `validadores/validar.py` | Un subcomando nuevo | Los enganches que llaman subcomandos por nombre | Nada se renombra: solo se agrega |
| `validadores/metareglas.py` | Gana un bloque de arranque | Nadie lo importa hoy | Su comportamiento como módulo no cambia |

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque son programas de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

**Sí tiene punto de entrada, y es lo que la fase construye:** `validar.py` con el subcomando nuevo. Hoy el programa no tiene ninguno.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Se le abre la puerta al programa que ya está, sin cambiar sus comprobaciones | Reescribirlo con lo aprendido | Reescribir y correr a la vez impide saber si un hallazgo es del programa viejo o del nuevo |
| Si algo no se puede correr, se muere diciendo por dónde se corre | Dejarlo callar | Es la exigencia del pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md): ninguno termina en silencio con código 0 sin haber mirado |
| La cuenta del pendiente 19 se corrige con lo que dé la corrida | Dejar el número viejo | Un pendiente con la cuenta vieja hace decidir sobre un dato falso |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién | Estado |
|---|---|---|---|
| 1 | Si el subcomando es uno con dos modos —el estándar en seco y el catálogo del proyecto— o dos subcomandos distintos | Usuario | **Resuelta** el 2026-08-18, decisión 38 del [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md): **uno con dos modos**. `validar.py metareglas --catalogo` ya funciona así |

La duda 1 bloquea T-01 y T-07, que son la puerta. Nada más se puede probar sin ella.

**Decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md). 👤 marca lo que sigue esperando un dato del usuario.

| Duda | Decisión |
|---|---|
| 38 | **Uno con dos modos.** `validar.py metareglas --catalogo` ya funciona así. |

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Un identificador repetido o con prefijo ajeno se reporta

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Darle punto de entrada al programa: subcomando en `validar.py` y bloque de arranque propio | `validadores/validar.py` · `metareglas.py` | 2,5 |
| T-02 | Caso de prueba: un identificador repetido y otro con prefijo de otro capítulo se reportan | `plan_pruebas.md` | 1,5 |

### CA-02 — Una dependencia que no existe o que manda hacia arriba se reporta

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Caso de prueba: una dependencia a un identificador que no existe, y una regla de capa 2 que deroga una blindada | `plan_pruebas.md` | 2,0 |

### CA-03 — Una regla sin su checklist se reporta

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-04 | Caso de prueba: una regla sin bloque de checklist se reporta, y una con el bloque no | `plan_pruebas.md` | 1,5 |
| T-05 | Anotar la cuenta real de reglas sin checklist el día de la corrida, contra las 121 del pendiente 19 | `resultado_pruebas.md` | 1,5 |

### CA-04 — Una regla que nombra una tecnología se reporta

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-06 | Caso de prueba: una regla que nombra un lenguaje se reporta; la misma, agnóstica, no | `plan_pruebas.md` | 1,5 |

### CA-05 — Una regla del proyecto sin respaldo en la base se reporta

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-07 | Que el punto de entrada acepte también la comprobación del catálogo de un proyecto | `validadores/validar.py` | 1,5 |
| T-08 | Caso de prueba: una regla propia sin respaldo se reporta; con respaldo a una regla que existe, no | `plan_pruebas.md` | 2,0 |

### RNF — Que ningún validador vuelva a callar sin haber mirado

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-09 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 9 tareas · 15,5 horas.**

---

## 4. Secuencia de ejecución

T-01 abre la puerta, y sin ella no hay nada que probar. Después T-02, T-03, T-04, T-06 en paralelo; T-07 → T-08 para el catálogo; T-05 con la corrida, y T-09 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Identificador repetido y con prefijo ajeno | T-02 |
| CA-02 | Dependencia inexistente y regla que manda sobre una blindada | T-03 |
| CA-03 | Regla sin bloque de checklist, y la cuenta real de hoy | T-04, T-05 |
| CA-04 | Regla que nombra un lenguaje, y su versión agnóstica | T-06 |
| CA-05 | Regla propia sin respaldo, y con respaldo válido | T-08 |

---

## 6. Datos y ambiente de prueba

Este repositorio y carpetas temporales para los casos negativos. Ningún dato real y ninguna clave: lo que parezca una clave se arma para la prueba.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

El estándar está en producción. El subcomando es **aditivo**: subida **MENOR**. Pero al poder correrse, la comprobación va a reportar lo que hoy nadie ve — eso no obliga a migrar, y conviene decirlo en la entrada del registro para que nadie lea el aumento de hallazgos como una regresión.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`05·E1`](../../../../../base/05-errores-y-logging.md), [`20·M3`](../../../../../base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md), [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), [`20·M14`](../../../../../base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md), [`20·M16`](../../../../../base/20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | La duda 1 sin resolver | Bloquea la puerta, y sin puerta no hay fase | Se presenta al usuario |
| R-01 | Que al abrir la puerta aparezcan cientos de hallazgos | Parece una regresión y no lo es | La entrada del registro lo dice, y el resultado anota la cuenta del primer día como línea base |
| R-02 | Que alguna comprobación esté mal y reporte de más | El programa se ignora | Se para y se propone: corregir la comprobación es otra fase |
| R-03 | Que el arreglo se lea como que el pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md) quedó cerrado | Los otros treinta siguen sin revisar | Se marca este caso como resuelto y el pendiente queda abierto por su punto 2 |

---

## 11. Definition of Done

- [ ] La comprobación del molde se corre por línea de comandos y dice qué encontró.
- [ ] Corrida sin nada que mirar, no calla: dice por dónde se corre.
- [ ] Los cinco casos están escritos y corridos.
- [ ] La cuenta de reglas sin checklist quedó al día en el pendiente 19.
- [ ] El caso quedó marcado como resuelto en el pendiente 53, que sigue abierto.
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
