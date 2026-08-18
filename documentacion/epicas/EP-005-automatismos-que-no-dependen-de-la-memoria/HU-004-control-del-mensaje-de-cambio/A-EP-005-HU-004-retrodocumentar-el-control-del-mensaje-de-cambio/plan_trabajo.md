# Plan de Trabajo — Fase A-EP-005-HU-004-retrodocumentar-el-control-del-mensaje-de-cambio (módulo Automatismos)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-004](../HU-004-control-del-mensaje-de-cambio.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-004-retrodocumentar-el-control-del-mensaje-de-cambio` |
| **Épica** | [EP-005 Automatismos que no dependen de la memoria](../../epica.md) |
| **HU** | [HU-004 Controlar el mensaje con que se guarda un cambio](../HU-004-control-del-mensaje-de-cambio.md) — una sola (`F12.1`) |
| **Módulo** | Automatismos |
| **Especificación del módulo** | [documentacion/automatismos/spec.md](../../../../automatismos/spec.md). Existe desde el 2026-08-14 y crece por incrementos; esta fase le agrega el suyo (`02·F2`) |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-005-HU-004-retrodocumentar-el-control-del-mensaje-de-cambio` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 🔀 **Híbrido.** 📄 Retro-documenta lo que existe: [`commits.py`](../../../../../validadores/commits.py) revisa el mensaje por `validar.py commit` — que diga algo, que esté bien armado y que no lleve la firma de ninguna herramienta. ✨ Y construye lo que falta: **nadie lo llama al guardar**. Los enganches instalados son seis y ninguno se dispara en el commit, así que la comprobación depende de que alguien la corra. Sale de la fila de HU-004 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-004 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-004-control-del-mensaje-de-cambio.md#ca-01--un-mensaje-sin-contenido-no-pasa) | Un mensaje sin contenido no pasa | **A medias.** La comprobación existe y **no se dispara**: hay que acordarse de correrla |
| [CA-02](../HU-004-control-del-mensaje-de-cambio.md#ca-02--el-rastro-de-la-herramienta-se-detecta) | El rastro de la herramienta se detecta | La comprobación existe y hay un acuerdo explícito del usuario sobre no firmar los commits con la herramienta. **Sin disparo automático** |

**Por qué una sola fase.** Los dos CA los comprueba el mismo programa en el mismo momento (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que el control del mensaje no dependa de que alguien se acuerde de correrlo.

**Fuera de alcance:**

- **Impedir el commit de un cambio de reglas sin versión,** que es [HU-005](../../HU-005-cambio-de-reglas-con-version/HU-005-cambio-de-reglas-con-version.md) y necesita el mismo disparo: las dos fases se coordinan.
- **Hacer commit por iniciativa propia.** Lo prohíbe `00·N2`, y esta fase no lo cambia: comprueba el mensaje de un commit que el usuario pidió.
- **Reescribir mensajes viejos.** El historial no se reescribe.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17: los seis enganches instalados se disparan al abrir sesión, al mandar un mensaje, al terminar la respuesta y al escribir un archivo. Ninguno en el commit.

**Lo que ya existe:** el programa que revisa el mensaje, con sus cuatro comprobaciones y su subcomando; la regla del capítulo de control de versiones sobre cómo se escribe un mensaje; el acuerdo del usuario de no firmar con la herramienta, escrito en la memoria del repositorio; y la exigencia del `CLAUDE.md` de que el cuerpo ponga primero la idea del usuario.

**Lo que no existe:**

1. **El disparo.** Ningún enganche corre en el momento de guardar.
2. **La prueba por criterio de esta HU.**
3. **La decisión de dónde vive el disparo.** Puede ser un enganche de la herramienta o uno del control de versiones, y no es lo mismo: uno viaja con el proyecto instalado y el otro se queda en la máquina.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/hook_commit.py` | Nuevo | El disparo, con la forma que decida la duda 1 |
| `validadores/instalar.py` | Modificar | Que el instalador lo deje puesto |
| `validadores/docs/hook_commit.md` | Nuevo | Qué hace y cuándo |
| `validadores/pruebas.py` | Modificar | Los casos de los dos CA |
| `documentacion/automatismos/spec.md` | Modificar | El incremento del control del mensaje |
| `…/A-EP-005-HU-004-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron |
| `HU-004-control-del-mensaje-de-cambio.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `CHANGELOG.md` · `VERSION` | Modificar | Cambia lo que el instalador deja puesto: entrada y subida |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> `commits.py` no se toca: ya comprueba lo que la HU pide.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

| Archivo que cambia | Qué cambia | Quién depende | Dónde |
|---|---|---|---|
| `validadores/instalar.py` | Deja puesto un enganche más | Los proyectos ya instalados, que no lo tienen | Los pone al día el mismo camino que ya existe para eso; sin actualizar, siguen sin el disparo |
| El momento del commit | Pasa a tener una comprobación | Cualquier sesión que guarde un cambio | Si la comprobación falla, el commit no se hace: eso obliga, y va declarado |

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque son enganches de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

**Sí tendrá punto de entrada, y no hará falta pedirlo:** el disparo corre al guardar. La comprobación a mano sigue existiendo con su subcomando.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El disparo se coordina con [HU-005](../../HU-005-cambio-de-reglas-con-version/HU-005-cambio-de-reglas-con-version.md) | Escribir dos disparos distintos | Dos enganches en el mismo momento se estorban y se ordenan mal; uno llama a las dos comprobaciones |
| La comprobación a mano se queda | Reemplazarla por el disparo | Correrla antes de guardar sirve para arreglar el mensaje sin que el commit falle |
| Los mensajes viejos no se revisan | Auditar el historial | El historial es rastro y no se reescribe; auditarlo sería otra unidad de trabajo |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién | Estado |
|---|---|---|---|
| 1 | Si el disparo es un enganche de la herramienta o del control de versiones — uno viaja con el proyecto, el otro se queda en la máquina | Usuario | Pendiente |
| 2 | Si un mensaje que no pasa detiene el commit o solo avisa | Usuario | Pendiente |

Las dos bloquean T-01. Los casos de prueba se pueden escribir antes.

**Decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md). 👤 marca lo que sigue esperando un dato del usuario.

| Duda | Decisión |
|---|---|
| 8 | **Detiene.** El molde del mensaje es forma, y la forma se comprueba. |
| 39 | **Enganche de la herramienta.** El del control de versiones no corre cuando el agente escribe. |

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Un mensaje sin contenido no pasa

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Que la comprobación del mensaje corra en el momento de guardar | `validadores/` | 3,0 |
| T-02 | Caso de prueba: un mensaje vacío o de una palabra no pasa; uno que dice qué se hizo, sí | `plan_pruebas.md` | 1,5 |

### CA-02 — El rastro de la herramienta se detecta

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Caso de prueba: un mensaje con la firma de la herramienta se detecta | `plan_pruebas.md` | 1,5 |
| T-04 | Caso de prueba: el cuerpo del mensaje pone primero la idea del usuario y después lo que hizo el agente, como pide el `CLAUDE.md` de este repositorio | `plan_pruebas.md` | 1,5 |

### RNF — Que el control no dependa de la memoria de nadie

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-05 | Correr las pruebas, escribir el incremento de la especificación y cerrar la trazabilidad de la HU y del inventario | Cierre | 2,0 |

**Total: 5 tareas · 9,5 horas.**

---

## 4. Secuencia de ejecución

T-02 → T-03 → T-04 primero, que son los casos. T-01 con las dudas resueltas. T-05 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Mensaje vacío y mensaje que dice qué se hizo | T-01, T-02 |
| CA-02 | Mensaje con la firma de la herramienta, y el orden del cuerpo | T-03, T-04 |

---

## 6. Datos y ambiente de prueba

Carpetas temporales para los casos, y este repositorio para las corridas. Ningún dato real y ninguna clave: lo que parezca una clave se arma para la prueba.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

El estándar está en producción. Un enganche que puede detener el commit **obliga**: subida **MAYOR** con su marca, salvo que la duda 2 resuelva que solo avise, y entonces **MENOR**. Los proyectos que no se actualicen siguen sin el disparo.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`00·N2`](../../../../../base/00-nucleo-blindado.md), [`09`](../../../../../base/09-git.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Las dos dudas sin resolver | Bloquean el disparo | Se presentan al usuario |
| R-01 | Que el enganche impida guardar en un momento urgente | Trabajo bloqueado | Es la duda 2: si detiene, tiene que decir exactamente qué arreglar |
| R-02 | Cruce con la fase de HU-005, que necesita el mismo disparo | Dos enganches en el mismo momento | Se coordinan: uno llama a las dos comprobaciones |
| R-03 | Que el enganche corra en proyectos que no lo esperan | Sorpresa al guardar | Entra por el camino de puesta al día, con su entrada en el registro de cambios |

---

## 11. Definition of Done

- [ ] La comprobación del mensaje corre al guardar, sin que nadie la pida.
- [ ] Un mensaje sin contenido y uno con la firma de la herramienta quedan detectados.
- [ ] El orden del cuerpo —primero la idea del usuario— quedó probado.
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
