# Plan de Trabajo — Fase A-EP-002-HU-006-quien-manda-sobre-la-version (módulo Versionado y adopción)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-006](../HU-006-quien-sube-la-version.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-002-HU-006-quien-manda-sobre-la-version` |
| **Épica** | [EP-002 Versionado y adopción](../../epica.md) |
| **HU** | [HU-006 Quién sube la versión cuando hay dos sesiones abiertas](../HU-006-quien-sube-la-version.md) — una sola (`F12.1`) |
| **Módulo** | Versionado y adopción |
| **Especificación del módulo** | [HU-006](../HU-006-quien-sube-la-version.md). El entregable es un acuerdo escrito sobre quién manda: sus criterios de aceptación son la especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-002-HU-006-quien-manda-sobre-la-version` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): ✨ **Funcionalidad nueva.** Acá **no hay nada construido**: ninguna regla dice quién manda sobre `VERSION` cuando hay dos sesiones abiertas. Baja del pendiente [22](../../../../../pendientes/22-dos-sesiones-versionando-a-la-vez.md) por la vía de [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), y su fila es la de HU-006 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-006 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-006-quien-sube-la-version.md#ca-01--dos-sesiones-no-dejan-dos-numeraciones) | Dos sesiones no dejan dos numeraciones | **No está.** El 2026-08-14 quedaron dos numeraciones vivas y el día cerró en `12.2.0` |
| [CA-02](../HU-006-quien-sube-la-version.md#ca-02--nadie-arrastra-el-trabajo-de-otro) | Nadie arrastra el trabajo de otro | **No está**, y ya volvió a pasar tres veces desde entonces |

**Por qué una sola fase.** Los dos CA son la misma decisión vista de los dos lados (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que quede escrito quién manda sobre la versión y en qué momento se sube, de forma que dos sesiones abiertas no puedan dejar dos numeraciones vivas ni arrastrar trabajo ajeno para guardar el propio.

**Fuera de alcance:**

- **El número de pendiente que dos sesiones se disputan.** Es [EP-004 · HU-018](../../../EP-004-comprobacion-automatica/HU-018-numero-de-pendiente-ya-tomado/HU-018-numero-de-pendiente-ya-tomado.md), la misma pregunta un piso más abajo.
- **Los casos ya ocurridos.** El registro es rastro: el tramo de las dos numeraciones del 2026-08-14 se documenta, no se corrige.
- **Un candado técnico entre sesiones.** Si la decisión pide uno, es otra fase: acá se escribe el acuerdo.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 leyendo el pendiente [22](../../../../../pendientes/22-dos-sesiones-versionando-a-la-vez.md) con sus tres ampliaciones y el estado del árbol de trabajo.

**Lo que ya existe:** nada normativo. Lo que hay son cuatro casos ocurridos:

| Cuándo | Qué pasó |
|---|---|
| 2026-08-14 | Dos sesiones subieron versiones en paralelo; el día cerró en `12.2.0` con dos numeraciones vivas |
| 2026-08-16 | Dos sesiones editaron `pendientes/README.md` a la vez; no se perdió nada porque la herramienta avisó antes de sobrescribir |
| 2026-08-16 | Otra sesión ya había ejecutado entero el pendiente 40; casi se hace el mismo trabajo dos veces |
| 2026-08-16 | Dos sesiones tomaron el número 52 de `pendientes/` |

**Lo que no existe:**

1. **La regla.** Ninguna dice quién sube la versión ni cuándo.
2. **El acuerdo sobre el alcance.** El pendiente 22 lo dejó abierto: si cubre cualquier archivo único compartido —índices, `plantillas/proyectos.md`— o solo la versión.
3. **La prueba.** No hay forma de probar un acuerdo que no está escrito.

**Y hay evidencia fresca:** al abrir esta sesión, el árbol de trabajo tenía cambios sin guardar de la sesión anterior, y `validar.py estandar` reportaba tres fallas que no eran de esta. Es el mismo problema, hoy.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `base/09-git.md` **o** `base/20-meta-reglas/reglas/` | Modificar o nuevo | Donde caiga la regla, según el enrutado de [`20·M2`](../../../../../base/20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md): el momento de subir es del capítulo de control de versiones; quién manda sobre la numeración del estándar es del capítulo de meta-reglas |
| `validadores/reglas-validables.md` | Modificar | La regla nueva declara si es comprobable ([`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md)) |
| `pendientes/22-dos-sesiones-versionando-a-la-vez.md` | Modificar | Se cierra cuando la regla lo resuelva, con los cuatro casos como evidencia |
| `…/A-EP-002-HU-006-…/plan_pruebas.md` | Nuevo | Los casos de los dos CA |
| `…/A-EP-002-HU-006-…/resultado_pruebas.md` | Nuevo | Lo que dieron |
| `HU-006-quien-sube-la-version.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `CHANGELOG.md` · `VERSION` | Modificar | Regla nueva: entrada y subida ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)) |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

### 2.2 Matriz de dependencias del refactor  ·  `F17`

| Archivo que cambia | Qué cambia | Quién depende | Dónde |
|---|---|---|---|
| La regla nueva | Fija el momento en que se sube la versión | [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), que hoy exige subir en el mismo cambio | Si la salida elegida es «se sube al guardar», `M10` hay que releerla y declarar si se extiende o si se ajusta; no se toca sin decirlo |

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque el entregable es texto normativo.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

No aplica. La regla se lee al ir a subir la versión.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Los cuatro casos ocurridos van al resultado como evidencia | Escribir la regla sin ellos | Una regla de convivencia sin los casos que la motivaron se discute de nuevo cada vez |
| El tramo de las dos numeraciones no se corrige | Renumerar para que la serie quede limpia | El registro es rastro, y renumerar rompe toda cita hecha a esas versiones |
| La regla se escribe una sola vez, en un solo capítulo | Repetirla en el capítulo de control de versiones y en el de meta-reglas | [`20·M2`](../../../../../base/20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md): un tema, un dueño; el otro capítulo la enlaza |

**Cuál de las tres salidas se toma no lo decide esta fase:** es la duda 1.

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién | Estado |
|---|---|---|---|
| 1 | Cuál de las tres salidas del pendiente 22: la versión se sube al guardar el cambio; cada sesión escribe su entrada del registro aparte y se juntan al guardar; o una sola sesión a la vez toca el estándar | Usuario | Pendiente |
| 2 | Si el acuerdo cubre cualquier archivo único compartido o queda acotado a `VERSION` y al registro | Usuario | Pendiente |
| 3 | En qué capítulo cae la regla, según lo que resuelvan las dos anteriores | Usuario | Pendiente |

Las tres bloquean todas las tareas de construcción. **Ninguna arranca con una duda abierta que la bloquee.**

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Dos sesiones no dejan dos numeraciones

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Escribir la regla con lo que decidan las dudas 1 a 3, por el procedimiento del capítulo `20` | `base/` | 2,5 |
| T-02 | Revisar si `M10` queda tocada por el momento nuevo, y declararlo | `base/20-meta-reglas/reglas/M10-…md` | 1,0 |
| T-03 | Caso de prueba: dos sesiones simuladas suben versión sobre la misma copia y se comprueba que la regla resuelve quién manda | `plan_pruebas.md` | 2,0 |

### CA-02 — Nadie arrastra el trabajo de otro

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-04 | Caso de prueba: con trabajo ajeno sin guardar en el árbol, una sesión guarda lo propio sin llevarse nada de la otra | `plan_pruebas.md` | 2,0 |
| T-05 | Escribir los cuatro casos ocurridos como evidencia, con qué habría hecho la regla nueva en cada uno | `resultado_pruebas.md` | 2,0 |

### RNF — Que el registro no pierda entradas

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-06 | Comprobar que, con la regla aplicada, ninguna entrada del registro se pierde por el cruce (RN-04) | Trazabilidad | 1,5 |
| T-07 | Clasificar la regla nueva, versionar, cerrar el pendiente 22 y la trazabilidad de la HU y del inventario | Cierre | 2,0 |

**Total: 7 tareas · 13,0 horas.**

---

## 4. Secuencia de ejecución

T-05 se puede escribir de entrada: son hechos ya ocurridos. Todo lo demás espera las tres dudas: T-01 → T-02 → T-03 → T-04 → T-06 → T-07.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Dos sesiones simuladas sobre la misma copia, aplicando la regla | T-03 |
| CA-02 | Guardar lo propio con trabajo ajeno presente en el árbol | T-04, y los cuatro casos de T-05 |
| RNF | Recuento de entradas del registro antes y después del cruce simulado | T-06 |

---

## 6. Datos y ambiente de prueba

Dos copias locales de este repositorio para simular las dos sesiones. Nada se escribe en el repositorio vivo durante la simulación. Ningún dato real y ninguna clave.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase: saca la regla nueva, devuelve el pendiente 22 y `VERSION`. Las copias de la simulación se borran al terminar.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

Se asume que el estándar está en producción. Una regla que cambia **cuándo** se sube la versión obliga a quien versione de aquí en adelante: la subida es **MAYOR**, con su marca de que obliga a migrar. Si la salida elegida solo describe lo que ya se hacía, es **MENOR**; cuál de las dos se declara al cerrar, con el texto que entre.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), [`09`](../../../../../base/09-git.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`20·M2`](../../../../../base/20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md), [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), [`20·M14`](../../../../../base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Las tres dudas sin resolver | Bloquean toda la construcción | Se presentan al usuario con lo que deja cada salida | Abierto |
| R-01 | Que la salida elegida obligue a tocar `M10` | Cambio en cascada sobre una meta-regla | Se declara en T-02 antes de tocarla, y si es más que una nota, se propone como fase aparte | Abierto |
| R-02 | Que el acuerdo se escriba solo para la versión y el problema siga en los índices | Vuelve a pasar en otro archivo | Es la duda 2, y por eso se pregunta antes de escribir | Abierto |
| R-03 | Que la regla no se pueda comprobar con un programa | Queda a la buena voluntad | Se declara así en `reglas-validables.md`: una regla honesta sobre lo que no se comprueba vale más que una comprobación falsa | Abierto |

---

## 11. Definition of Done

- [ ] Está escrito quién manda sobre la versión y en qué momento se sube.
- [ ] Está dicho si el acuerdo cubre cualquier archivo único compartido.
- [ ] Los dos CA tienen su caso escrito y corrido con dos copias.
- [ ] Los cuatro casos ocurridos quedaron como evidencia, sin corregir el rastro.
- [ ] La regla está clasificada y trae su bloque de checklist.
- [ ] `CHANGELOG.md` con su entrada y `VERSION` subida, con el tipo que corresponda.
- [ ] El pendiente 22 dice la verdad, y se cerró si la regla lo resuelve.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
