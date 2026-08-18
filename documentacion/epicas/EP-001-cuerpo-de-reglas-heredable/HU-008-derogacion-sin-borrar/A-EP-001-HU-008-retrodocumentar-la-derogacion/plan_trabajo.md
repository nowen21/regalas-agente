# Plan de Trabajo — Fase A-EP-001-HU-008-retrodocumentar-la-derogacion (módulo Cuerpo de reglas)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en [HU-008](../HU-008-derogacion-sin-borrar.md); el detalle de las pruebas, en el `plan_pruebas.md` de esta misma fase; lo que dieron al correrlas, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (identificador · [`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-001-HU-008-retrodocumentar-la-derogacion` |
| **Épica** | [EP-001 Cuerpo de reglas heredable y en capas](../../epica.md) |
| **HU** | [HU-008 Derogar una regla sin borrarla ni renumerarla](../HU-008-derogacion-sin-borrar.md) — una sola (`F12.1`) |
| **Módulo** | Cuerpo de reglas |
| **Especificación del módulo** | [HU-008](../HU-008-derogacion-sin-borrar.md). El entregable es texto normativo: sus criterios de aceptación son la especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-001-HU-008-retrodocumentar-la-derogacion` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md)). La derogación existe y ya se usó ocho veces: [`20·M11`](../../../../../base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md) la exige, la marca `[DEROGADA en X.Y.Z → ver ID]` está en la lista cerrada, y [`validadores/version.py`](../../../../../validadores/version.py) las lee para saber qué falta adoptar. Lo que falta es la cadena de esta HU. Sale de la fila de HU-008 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-008 | Qué exige | Estado hoy, sin haber tocado nada |
|---|---|---|
| [CA-01](../HU-008-derogacion-sin-borrar.md#ca-01--una-regla-derogada-sigue-siendo-legible) | Una regla derogada sigue siendo legible | Cumplido: las ocho conservan su texto y dicen desde cuándo y por cuál se reemplazan. **Sin prueba escrita** |
| [CA-02](../HU-008-derogacion-sin-borrar.md#ca-02--un-identificador-liberado-no-se-reutiliza) | Un identificador liberado no se reutiliza | Exigido por [`20·M4`](../../../../../base/20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md) y `M11`, y comprobable por la fila 6 del checklist. El programa que la mira **no se puede correr** |
| [CA-03](../HU-008-derogacion-sin-borrar.md#ca-03--una-regla-derogada-no-se-cuenta-como-incumplimiento) | Una regla derogada no se cuenta como incumplimiento | Escrito en el código de [`validadores/metareglas.py`](../../../../../validadores/metareglas.py), que saltea las derogadas — y **no corre**. Lo que sí corre es [`02·F22`](../../../../../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md), por otro camino |

**Por qué una sola fase para los tres CA.** Los tres se comprueban sobre las mismas ocho reglas derogadas y con la misma corrida. Partirlos daría fases que existen para cumplir la nomenclatura (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar probado sobre las ocho derogaciones que existen que el texto se conserva, que el identificador no se reutiliza y que una regla derogada no cuenta como incumplida — y decir por qué camino se comprueba cada cosa hoy.

**Fuera de alcance:**

- **La derogación sin adoptar,** que es [`02·F22`](../../../../../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md) y ya tiene su fase cerrada en [EP-004 · HU-015](../../../EP-004-comprobacion-automatica/HU-015-derogacion-sin-adoptar/A-EP-004-HU-015-retrodocumentar-la-comprobacion-de-la-f22/plan_trabajo.md). Acá se cita como línea base, no se rehace.
- **Derogar alguna regla.** Si al revisar aparece una candidata, se propone: derogar es decisión del usuario.
- **Darle punto de entrada a `metareglas.py`.** Pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md), punto 2.
- **Las siete reglas publicadas con el checklist en «no cumple»**, que son del pendiente [19](../../../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado contra el repositorio el 2026-08-17, corriendo `version.derogaciones()` y `validar.py version`.

**Las ocho derogaciones que hay hoy:**

| Regla derogada | Desde | Reemplazada por |
|---|---|---|
| `F4.1` | 3.1.0 | `F14` |
| `F4.2` | 3.1.0 | `F15` |
| `F4.3` | 3.1.0 | `F16` y `F17` |
| `F4.4` | 3.1.0 | `F18` |
| `F4.5` | 3.1.0 | `F19` y `F20` |
| `F6` | 4.0.0 | `13·DOC1` |
| `F7` | 4.0.0 | `13·DOC3` |
| `ID2` | 6.0.0 | `00·ID7` |

**Lo que ya existe:**

| Exigencia de la HU | Dónde está hoy | Estado |
|---|---|---|
| RN-01 y RN-02 · ninguna regla se borra, ningún identificador se reutiliza | [`20·M11`](../../../../../base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md) y [`20·M4`](../../../../../base/20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md) | Regla |
| RN-03 y RN-04 · dice desde cuándo, por qué y cuál la reemplaza | La marca `[DEROGADA en X.Y.Z → ver ID]` de la lista cerrada, fila 13 del checklist | Regla, y usada en las ocho |
| RN-05 · una derogada no se cuenta como incumplida | El salteo de derogadas dentro de [`validadores/metareglas.py`](../../../../../validadores/metareglas.py) | Escrito, sin poder correrse |
| Que una derogación sin adoptar frene la fase | [`validadores/version.py`](../../../../../validadores/version.py), que llama [`flujo.py`](../../../../../validadores/flujo.py) · `validar.py flujo` | Corriendo |
| Que las derogaciones se lean sin equivocarse | [`validadores/tests/test_version_derogaciones.py`](../../../../../validadores/tests/test_version_derogaciones.py), dentro de las 246 pruebas de `validadores/pruebas.py` | Corriendo |

**Lo que no existe:**

1. **La prueba del CA-01.** Que las ocho sigan legibles se ve abriendo los archivos; no hay caso que lo fije, así que nadie se enteraría si mañana alguien borra una.
2. **La comprobación del CA-02.** Que un identificador liberado no vuelva a usarse lo decidiría la fila 6, y su programa no corre. Hoy lo sostiene que alguien se acuerde.
3. **Un camino que corra para el CA-03.** El salteo de derogadas vive en el programa que no tiene punto de entrada.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `documentacion/epicas/EP-001-…/HU-008-…/A-EP-001-HU-008-…/plan_pruebas.md` | Nuevo | Documentación | Los casos de esta fase, uno por CA |
| `documentacion/epicas/EP-001-…/HU-008-…/A-EP-001-HU-008-…/resultado_pruebas.md` | Nuevo | Documentación | Lo que dieron, con la tabla de las ocho |
| `validadores/pruebas.py` | Modificar | Pruebas | Los casos del CA-01 y del CA-02, que hoy no existen: nadie prueba que las ocho sigan ahí |
| `documentacion/epicas/EP-001-…/HU-008-…/HU-008-derogacion-sin-borrar.md` | Modificar | Documentación | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Documentación | Las casillas de la fila de HU-008 |

> **`base/` no se toca, y `metareglas.py` tampoco.** Lo que se agrega son pruebas sobre lo que ya está.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: se agregan pruebas nuevas a `validadores/pruebas.py`, sin cambiar las 246 que ya corren ni la interfaz de ningún validador.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque es un programa de línea de comandos y archivos de texto.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

No aplica. Las derogaciones se leen en el capítulo donde vive la regla, y `validar.py version` las nombra cuando el proyecto quedó atrás.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La prueba se ata a la lista de las ocho, leída del propio cuerpo, no a una lista escrita a mano en el archivo de pruebas | Escribir los ocho identificadores dentro de la prueba | Una lista escrita a mano envejece con la primera derogación nueva y la prueba pasa a mentir |
| El CA-02 se prueba comprobando que ningún identificador derogado vuelve a aparecer como regla vigente | Confiar en la fila 6 del checklist | La fila la decidiría un programa que no corre; la prueba sí corre, y con las 246 |
| El CA-03 se cierra diciendo por qué camino se comprueba cada mitad | Marcarlo cumplido porque el código lo contempla | Código que no se puede correr no comprueba nada, y es el mismo error que ya cerró un resultado de pruebas falso en agosto |

### 2.7 Dudas por resolver antes de escribir

Ninguna. Las ocho derogaciones están verificadas y las tres pruebas se pueden escribir contra ellas sin esperar decisión.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Una regla derogada sigue siendo legible

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Prueba: por cada derogación que devuelve `version.derogaciones()`, su archivo existe y conserva el cuerpo de la regla | `validadores/pruebas.py` | 2,0 |
| T-02 | Caso de prueba: la marca de cada una dice desde qué versión y cuál la reemplaza, y el identificador que nombra existe | `plan_pruebas.md` | 1,5 |

### CA-02 — Un identificador liberado no se reutiliza

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Prueba: ningún identificador derogado aparece además como regla vigente en el mismo capítulo | `validadores/pruebas.py` | 2,0 |
| T-04 | Caso de prueba: al agregar una regla al capítulo, el consecutivo que toma no es uno liberado | `plan_pruebas.md` | 1,0 |

### CA-03 — Una regla derogada no se cuenta como incumplimiento

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-05 | Caso de prueba: una derogada no aparece en la cuenta de reglas sin checklist al día | `plan_pruebas.md` | 1,5 |
| T-06 | Dejar escrito qué mitad la comprueba un programa que corre y qué mitad vive en uno que no tiene punto de entrada | `resultado_pruebas.md` | 1,0 |

### RNF — Que la cuenta de derogaciones no se pierda

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-07 | Correr las 246 pruebas más las nuevas y dejar el número en el resultado | Comprobabilidad | 1,0 |
| T-08 | Escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 8 tareas · 11,5 horas.**

---

## 4. Secuencia de ejecución

T-01 → T-03 primero, que son las dos pruebas nuevas y comparten la lectura del cuerpo. T-02, T-04 y T-05 se escriben en paralelo. T-06, T-07 y T-08 cierran.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Si otra sesión está tocando `validadores/pruebas.py`, se guarda solo lo propio.

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método de verificación | Evidencia |
|---|---|---|
| CA-01 | Prueba automática sobre la lista que devuelve el propio cuerpo, más la revisión de las ocho marcas | T-01 y T-02 |
| CA-02 | Prueba automática de que ningún identificador derogado vuelve como vigente | T-03 y T-04 |
| CA-03 | Revisión de que una derogada no entra en la cuenta, y la constancia de por qué camino se comprueba | T-05 y T-06 |
| RNF | Corrida completa de `validadores/pruebas.py` con el número de pruebas | T-07 |

---

## 6. Datos y ambiente de prueba

Este repositorio. Las pruebas nuevas leen `base/` y no escriben nada; las que necesiten archivos los crean en carpeta temporal, como las 246 que ya están. Ningún dato real y ninguna clave.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. Lo único ejecutable que entra son dos pruebas: revertirlas devuelve la suite a las 246 y no deja datos que restaurar.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No aplica: no cambia el comportamiento de nada instalado. Las pruebas nuevas corren donde vive el estándar. No hay subida de versión, porque no se toca `base/` ni `plantillas/`.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`02·F22`](../../../../../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`13·DOC17`](../../../../../base/13-documentacion/reglas/DOC17-manten-un-readme-en-cada-nivel-del-arbol-de-trabajo.md), [`20·M4`](../../../../../base/20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md), [`20·M11`](../../../../../base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que la suite esté roja por algo ajeno y no se pueda leer el verde de lo nuevo | No se distingue lo propio de lo heredado | Se anota el estado de la suite **antes** de tocarla, y el resultado compara contra ese número | Abierto |
| R-02 | Que la prueba del CA-02 dé falso positivo con un identificador con punto, como `F4.1` | La prueba se ignoraría | Se cubren los dos formatos en el caso, y se prueba con `F4.1` a propósito | Abierto |
| R-03 | Que otra sesión esté tocando `validadores/pruebas.py` | Pisar trabajo ajeno | Se guarda solo lo propio, como ya se hizo en agosto | Abierto |
| R-04 | Que al revisar aparezca una regla que debería estar derogada y no lo está | Se destapa trabajo de fondo | Se propone; derogar es decisión del usuario | Abierto |

---

## 11. Definition of Done

- [ ] Las ocho derogaciones tienen prueba automática de que siguen legibles.
- [ ] Ningún identificador derogado puede volver como vigente sin que una prueba lo detecte.
- [ ] El resultado dice, para el CA-03, qué comprueba un programa que corre y qué no.
- [ ] La suite corre con su número anotado antes y después.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila de HU-008 del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase. Este plan se queda como se aprobó, para poder comparar lo que se dijo contra lo que pasó.
