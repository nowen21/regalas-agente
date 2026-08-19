# Plan de Trabajo — Fase A-EP-005-HU-005-el-cambio-de-reglas-no-se-guarda-sin-version (módulo Automatismos)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-005](../HU-005-cambio-de-reglas-con-version.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-005-el-cambio-de-reglas-no-se-guarda-sin-version` |
| **Épica** | [EP-005 Automatismos que no dependen de la memoria](../../epica.md) |
| **HU** | [HU-005 Impedir guardar un cambio de reglas sin versión ni registro](../HU-005-cambio-de-reglas-con-version.md) — una sola (`F12.1`) |
| **Módulo** | Automatismos |
| **Especificación del módulo** | [documentacion/automatismos/spec.md](../../../../automatismos/spec.md). Existe desde el 2026-08-14 y crece por incrementos; esta fase le agrega el suyo (`02·F2`) |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-005-HU-005-el-cambio-de-reglas-no-se-guarda-sin-version` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): ✨ **Funcionalidad nueva.** La exigencia existe —[`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md): todo cambio de regla suma entrada en el registro y sube la versión— y **nada lo impide**. Ningún enganche corre al guardar, y la fila 19 del checklist, que lo comprobaría, vive en un programa sin punto de entrada. Sale de la fila de HU-005 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-005 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-005-cambio-de-reglas-con-version.md#ca-01--un-cambio-de-reglas-sin-versión-no-se-guarda) | Un cambio de reglas sin versión no se guarda | **No está.** Hoy depende de que quien edita se acuerde, y el `CLAUDE.md` del repositorio tiene que repetirlo: «versionar no es opcional» |
| [CA-02](../HU-005-cambio-de-reglas-con-version.md#ca-02--un-cambio-que-no-toca-reglas-no-se-ve-afectado) | Un cambio que no toca reglas no se ve afectado | **No está**, y es lo que decide si el enganche se puede vivir con él: casi todos los cambios no tocan reglas |

**Por qué una sola fase.** Los dos CA son el mismo enganche: uno exige y el otro se calla (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que un cambio de reglas no se pueda guardar sin su entrada en el registro y su subida de versión, y que el resto de los cambios no note nada.

**Fuera de alcance:**

- **Elegir el tipo de subida.** Si es mayor, menor o parche lo decide quien hace el cambio: el enganche comprueba que haya subida y entrada, no que el tipo sea el correcto.
- **Quién sube la versión con dos sesiones abiertas,** que es [EP-002 · HU-006](../../../EP-002-versionado-y-adopcion/HU-006-quien-sube-la-version/HU-006-quien-sube-la-version.md) y el pendiente [22](../../../../../pendientes/hecho/dos-sesiones-versionando-a-la-vez.md). Este enganche puede empeorar ese cruce, y por eso se coordinan.
- **El control del mensaje,** que es [HU-004](../../HU-004-control-del-mensaje-de-cambio/HU-004-control-del-mensaje-de-cambio.md) y comparte el disparo.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17: ningún enganche corre al guardar, y `metareglas.py` —donde vive la fila 19— no se puede correr.

**Lo que ya existe:** la exigencia escrita, con su procedimiento y sus tres tipos de subida; el registro de cambios y el archivo de la versión; la fila 19 del checklist, escrita en un programa que no tiene punto de entrada; y la insistencia del `CLAUDE.md` del repositorio, que es la señal de que hoy esto se sostiene a pulso.

**Lo que no existe:**

1. **El enganche.** Nada corre al guardar.
2. **La forma de saber si el cambio toca reglas.** Hay que mirar qué archivos entran en el commit, y eso hoy no lo mira nadie.
3. **La prueba del silencio.** Sin ella, el enganche molestaría en cada cambio y se apagaría.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/hook_commit.py` | Nuevo o modificar | La comprobación, en el mismo disparo que [HU-004](../../HU-004-control-del-mensaje-de-cambio/HU-004-control-del-mensaje-de-cambio.md) |
| `validadores/instalar.py` | Modificar | Que el instalador lo deje puesto |
| `validadores/docs/hook_commit.md` | Nuevo o modificar | Qué exige, cuándo y cuándo se calla |
| `validadores/pruebas.py` | Modificar | Los casos de los dos CA |
| `documentacion/automatismos/spec.md` | Modificar | El incremento |
| `…/A-EP-005-HU-005-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron |
| `HU-005-cambio-de-reglas-con-version.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `CHANGELOG.md` · `VERSION` | Modificar | Entrada y subida |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> Ni `base/` ni `plantillas/` se tocan: la fase construye quien las vigila.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

| Archivo que cambia | Qué cambia | Quién depende | Dónde |
|---|---|---|---|
| `validadores/hook_commit.py` | Puede ser el mismo archivo de HU-004 | Esa fase, si va primero | La segunda relee y se suma en vez de reescribir |
| El momento del commit | Pasa a poder detenerse | Cualquier sesión que toque `base/` | Obliga, y va declarado con su marca |

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque son enganches de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

**Sí tendrá punto de entrada, y no hará falta pedirlo:** corre al guardar.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El enganche mira los archivos del cambio, no el mensaje | Pedir que el mensaje diga que hubo cambio de reglas | El mensaje lo escribe quien guarda; los archivos son un hecho |
| Comprueba que haya entrada y subida, no que el tipo sea correcto | Juzgar si el cambio obliga a migrar | Eso es criterio, y un enganche que se equivoca en eso trabaría cambios legítimos |
| Se coordina con el disparo de HU-004 | Un enganche propio | Dos enganches en el mismo momento se estorban |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién | Estado |
|---|---|---|---|
| 1 | Si detiene el commit o solo avisa — y si eso puede depender del tipo de cambio | Usuario | Pendiente |
| 2 | Si esta fase va después de HU-004, que crea el disparo, o si esta lo crea y aquella se suma | Usuario | Pendiente |

Las dos bloquean T-01. Los casos de prueba se pueden escribir antes.

**Decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md). 👤 marca lo que sigue esperando un dato del usuario.

| Duda | Decisión |
|---|---|
| 9 | **Detiene**, y no depende del tipo de cambio: `20·M10` no admite excepción por tamaño. |
| 32 | **`HU-004` crea el disparo y esta se suma.** Dos enganches sobre el mismo momento se pisan. |

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Un cambio de reglas sin versión no se guarda

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Que al guardar se mire si el cambio toca `base/` o `plantillas/` y, si sí, que exija entrada en el registro y subida de versión | `validadores/` | 3,0 |
| T-02 | Caso de prueba: un cambio en una regla sin entrada ni subida no se guarda; con las dos, sí | `plan_pruebas.md` | 2,0 |

### CA-02 — Un cambio que no toca reglas no se ve afectado

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Que el enganche se calle cuando el cambio no toca `base/` ni `plantillas/` | `validadores/` | 1,5 |
| T-04 | Caso de prueba: un cambio en `documentacion/` o en `pendientes/` no exige nada | `plan_pruebas.md` | 1,5 |

### RNF — Que el resto de los cambios no note nada

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-05 | Correr las pruebas, escribir el incremento de la especificación y cerrar la trazabilidad de la HU y del inventario | Cierre | 2,0 |

**Total: 5 tareas · 10,0 horas.**

---

## 4. Secuencia de ejecución

T-02 → T-04 primero, que son los casos. T-01 → T-03 con las dudas resueltas. T-05 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Cambio en una regla sin entrada ni subida, y con las dos | T-01, T-02 |
| CA-02 | Cambio en `documentacion/` o `pendientes/`, sin exigencia | T-03, T-04 |

---

## 6. Datos y ambiente de prueba

Carpetas temporales para los casos, y este repositorio para las corridas. Ningún dato real y ninguna clave: lo que parezca una clave se arma para la prueba.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

El estándar está en producción. Un enganche que puede detener el commit **obliga**: subida **MAYOR** con su marca, salvo que la duda 1 resuelva que solo avise. Los proyectos que no se actualicen siguen sin él.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`00·N2`](../../../../../base/00-nucleo-blindado.md), [`09`](../../../../../base/09-git.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), [`20·M14`](../../../../../base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Las dos dudas sin resolver | Bloquean el enganche | Se presentan al usuario |
| R-01 | Que el enganche empeore el cruce de dos sesiones versionando | Dos numeraciones vivas y ahora con un enganche exigiendo | Se coordina con [EP-002 · HU-006](../../../EP-002-versionado-y-adopcion/HU-006-quien-sube-la-version/HU-006-quien-sube-la-version.md): si la decisión de allá cambia el momento de subir, este enganche cambia con ella |
| R-02 | Que trabe un cambio urgente en una regla | Trabajo bloqueado | Es la duda 1, y si detiene tiene que decir exactamente qué falta |
| R-03 | Que el enganche no vea el cambio porque el archivo entró en otro commit | Falso verde | La comprobación mira lo que se está guardando, y el resultado dice qué caso no cubre |

---

## 11. Definition of Done

- [ ] Un cambio de reglas sin entrada ni subida no se guarda.
- [ ] Un cambio que no toca reglas no nota nada, con prueba.
- [ ] El enganche está coordinado con el de HU-004.
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
