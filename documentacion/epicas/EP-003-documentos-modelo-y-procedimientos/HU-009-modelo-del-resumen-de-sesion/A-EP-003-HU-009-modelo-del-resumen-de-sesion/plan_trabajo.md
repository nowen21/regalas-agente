# Plan de Trabajo — Fase A-EP-003-HU-009-modelo-del-resumen-de-sesion (módulo Documentos modelo)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en [HU-009](../HU-009-modelo-del-resumen-de-sesion.md); el detalle de las pruebas, en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase; lo que dieron al correrlas, en el [resultado_pruebas.md](resultado_pruebas.md); lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (identificador · [`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-003-HU-009-modelo-del-resumen-de-sesion` |
| **Épica** | [EP-003](../../epica.md) |
| **HU** | [HU-009 Crear el modelo del resumen de sesión](../HU-009-modelo-del-resumen-de-sesion.md) |
| **Módulo** | Documentos modelo |
| **Especificación del módulo** | [documentacion/documentos-modelo/spec.md](../../../../documentos-modelo/spec.md). Es la misma del módulo, ampliada con las reglas 8 a 16, que son las del resumen |
| **Fecha apertura** | 2026-08-14 |
| **Rama** | `feature/A-EP-003-HU-009-modelo-del-resumen-de-sesion` |

**ORIGEN** (`DOC12`): ✨ **Funcionalidad nueva.** Segundo eslabón de la cadena que abre el hallazgo H-4 del 2026-08-14. El primero, [`A-EP-003-HU-001`](../../HU-001-marca-de-espacio-por-llenar/A-EP-003-HU-001-marca-de-espacio-por-llenar/README.md), cerró el 2026-08-14 con el commit `b877f37`. El tercero es EP-005 · HU-008, el enganche, que escribe el archivo con este modelo adentro.

**CA de la HU que cubre esta fase** (una sola HU · [`02·F12.1`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md) · trazabilidad `DOC11`)

| CA de HU-009 | Qué valida | Estado |
|---|---|---|
| [CA-01](../HU-009-modelo-del-resumen-de-sesion.md#ca-01--el-modelo-existe-y-se-distingue-de-la-transcripción) | El modelo existe y se distingue de la transcripción | Cumple |
| [CA-02](../HU-009-modelo-del-resumen-de-sesion.md#ca-02--un-hallazgo-dice-si-está-cerrado-y-por-dónde-sigue) | Un hallazgo dice si está cerrado y por dónde sigue | Cumple |
| [CA-03](../HU-009-modelo-del-resumen-de-sesion.md#ca-03--el-resumen-dice-si-la-sesión-se-puede-cerrar) | El resumen dice si la sesión se puede cerrar | Cumple |

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar el modelo del resumen de sesión terminado y encontrable: con sus campos decididos, enlazado desde donde alguien lo va a buscar, y con respuesta escrita para el hallazgo que se arrastra de una sesión a otra.

**Resumen de exigencias a cubrir:**

| Exigencia | Escenario | Tipo | Complejidad |
|---|---|---|---|
| [CA-01](../HU-009-modelo-del-resumen-de-sesion.md#ca-01--el-modelo-existe-y-se-distingue-de-la-transcripción) | El resumen responde preguntas que la transcripción no responde | Funcional | Baja |
| [CA-02](../HU-009-modelo-del-resumen-de-sesion.md#ca-02--un-hallazgo-dice-si-está-cerrado-y-por-dónde-sigue) | Un hallazgo abierto se retoma sin preguntarle a quien estuvo | Funcional | Media |
| [CA-03](../HU-009-modelo-del-resumen-de-sesion.md#ca-03--el-resumen-dice-si-la-sesión-se-puede-cerrar) | La sección de cierre dice qué falta | Funcional | Baja |
| [RNF-01](../HU-009-modelo-del-resumen-de-sesion.md#5-requisitos-no-funcionales) | Brevedad: el resumen se lee de una vez | No funcional | Media |
| [RNF-02](../HU-009-modelo-del-resumen-de-sesion.md#5-requisitos-no-funcionales) | Autonomía: se entiende sin abrir la transcripción | No funcional | Media |
| [RNF-03](../HU-009-modelo-del-resumen-de-sesion.md#5-requisitos-no-funcionales) | Uniformidad: todos los resúmenes traen los mismos campos | No funcional | Baja |

**Fuera de alcance** (qué explícitamente NO entra en esta fase):

- **El enganche que crea el archivo y avisa cuando falta.** Es EP-005 · HU-008, y así lo dice la propia HU en su §3.3.
- **La transcripción de la sesión.** Sigue su curso y no cambia de forma por esto.
- **Reescribir los resúmenes ya escritos.** Los dos del 2026-08-14 se usan como prueba, no como trabajo.
- **Los otros ocho modelos de EP-003.**

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado contra el repositorio el 2026-08-14.
>
> **Ampliación aprobada el 2026-08-14**, al ejecutar T-06. El plan declaraba `validadores/historico.py` solo para revisarlo, y la revisión mostró que hay que modificarlo: el índice del histórico no es una lista cualquiera, sino una que ese programa reconoce con una forma exacta. Agregarle el enlace al resumen en la misma línea la vuelve irreconocible, y el programa escribiría una línea duplicada en el siguiente renombrado en vez de corregir la que ya está. El aviso salió de [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md).

**Qué hay hoy.** El modelo existe y ya se usó dos veces:

| Qué | Dónde | Estado |
|---|---|---|
| El modelo | [`plantillas/sesion.md`](../../../../../plantillas/sesion.md) | Escrito. Doce campos por hallazgo, más «viene de» y el orden de lo que dispara, agregados el 2026-08-14 |
| Resumen 1 | [`historico-chat/resumenes/2026-08-14/hu-de-la-comprobacion-automatica.md`](../../../../../historico-chat/resumenes/2026-08-14/hu-de-la-comprobacion-automatica.md) | 9 hallazgos |
| Resumen 2 | [`historico-chat/resumenes/2026-08-14/h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md`](../../../../../historico-chat/resumenes/2026-08-14/h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md) | 7 hallazgos |
| Índice del día | [`historico-chat/resumenes/2026-08-14/README.md`](../../../../../historico-chat/resumenes/2026-08-14/README.md) | Con sus dos líneas |
| Índice de la carpeta | [`historico-chat/resumenes/README.md`](../../../../../historico-chat/resumenes/README.md) | Existe |

**Los tres huecos que quedan**, y son el trabajo de esta fase:

1. **Desde dónde se enlaza.** El índice del histórico ([`historico-chat/README.md`](../../../../../historico-chat/README.md)) lista las transcripciones y no menciona los resúmenes. Quien busca qué dejó una sesión llega a la transcripción, que es lo que el resumen viene a evitar.
2. **El hallazgo que se arrastra.** El modelo tiene «nace en» y «cerrado en», pero no dice qué hace la sesión que lo hereda: si lo copia, si lo enlaza, o si solo lo nombra. Hoy pasó de verdad: H-4 nació en una sesión y esta lo trabajó, y quedó resuelto a mano.
3. **La numeración de los hallazgos.** Los dos resúmenes usan `H-1`, `H-2`… cada uno desde el uno, así que "el H-4" no identifica nada sin decir de qué sesión. Se ve en este mismo plan, que tiene que escribir "el H-4 del 2026-08-14".

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `plantillas/sesion.md` | Modificar | Plantilla | Qué hace la sesión que hereda un hallazgo, y cómo se identifica un hallazgo entre sesiones |
| `historico-chat/README.md` | Modificar | Documentación | El índice apunta al resumen de cada sesión, no solo a su transcripción |
| `historico-chat/resumenes/README.md` | Modificar | Documentación | Dice qué responde el resumen y qué la transcripción |
| `base/13-documentacion/reglas/DOC22-…` | Nuevo | Regla | Cada sesión deja escrito lo que dejó, con el modelo. Es lo que hace exigible al modelo fuera de este repositorio |
| `base/13-documentacion/base.md` | Modificar | Regla | La fila nueva en el índice del capítulo |
| `validadores/historico.py` | Modificar | Programa | Reconocer y escribir la línea del índice con el enlace al resumen |
| `validadores/reglas-validables.md` | Modificar | Documentación | La regla nueva, en la lista que le toque |
| `CHANGELOG.md` · `VERSION` | Modificar | Versionado | Entrada y subida de versión ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)) |

> **`validadores/reglas-validables.md` lo está editando otra sesión.** Las tres filas de la fase anterior siguen sin commitear por eso. Esta fase escribe la suya igual, y el commit decide qué se puede guardar sin arrastrar trabajo ajeno.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

| Archivo a refactorizar | Cambio de contrato | Archivos que dependen (rompen) | Dónde rompe |
|---|---|---|---|
| `plantillas/sesion.md` | Suma campos; ninguno de los que hay cambia de nombre ni desaparece | Los dos resúmenes ya escritos | No rompen: lo que se suma se puede llenar después |
| `historico-chat/README.md` | Suma una columna al índice | `validadores/historico.py`, que escribe la línea al renombrar | **Sí rompe** si el script escribe la línea con el número de columnas viejo. Hay que mirarlo antes de tocar el índice |

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

N/A: el entregable es texto normativo y plantillas.

### 2.4 Punto de entrada en la UI  ·  `F14` Q7

N/A. Se lee abriendo `historico-chat/README.md` y de ahí al resumen del día.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

N/A.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El resumen se enlaza desde el índice del histórico, al lado de su transcripción | Una carpeta aparte con su propio índice y nada más | Quien busca qué dejó una sesión arranca por el histórico. Un índice que solo alguien que ya lo conoce sabe abrir no sirve |
| El hallazgo se identifica con `AAAA-MM-DD · tema · H-N` | Numeración corrida entre todas las sesiones | La numeración corrida obliga a un contador central, y dos sesiones abiertas a la vez lo rompen. Ya pasó con la versión, y está anotado en el pendiente 22 |
| La sesión que hereda un hallazgo **no lo copia**: lo nombra y trabaja sobre el original | Copiarlo al resumen nuevo | Dos copias del mismo hallazgo terminan diciendo cosas distintas, y la que manda es la que nadie está mirando |

> Las decisiones no obvias se registran también como señal ([`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)).

### 2.7 Dudas por resolver antes de codificar

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | Si la regla nueva [`DOC22`](../../../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md) obliga a todo proyecto a escribir resumen de sesión, o si es *opt-in* | usuario | **Resuelta** el 2026-08-14: obliga. Este repositorio es la línea base de todo proyecto, y lo que acá se exige se hereda. El cambio es MAYOR |
| 2 | Si el resumen se enlaza desde el índice del histórico o desde cada línea de sesión | usuario | **Resuelta** el 2026-08-14: por sesión. Cada sesión resuelve un tema, así que su resumen va pegado a su línea |

> Ninguna tarea de construcción inicia con una duda abierta que la bloquee.

---

## 3. Desglose de tareas por criterio de aceptación

> Cada CA se descompone en tareas atómicas. **Depende de** ordena la ejecución; **Ev.** referencia la evidencia de §5.
>
> Cada `CA-0N` y cada `RNF-0N` se escriben como enlace a su exigencia en la HU.

### [CA-01](../HU-009-modelo-del-resumen-de-sesion.md#ca-01--el-modelo-existe-y-se-distingue-de-la-transcripción) — El modelo existe y se distingue de la transcripción

| ID | Tarea | Capa | Est. | Depende de | Estado | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | Escribir en `historico-chat/resumenes/README.md` qué responde el resumen y qué la transcripción | Documentación | 1 h | — | ☑ | EV-01 |
| T-02 | Escribir [`DOC22`](../../../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md), con su ejemplo y su checklist | Regla | 2 h | T-01 | ☑ | EV-01 |
| T-03 | Sumar su fila al índice de `base/13-documentacion/base.md` | Regla | 1 h | T-02 | ☑ | EV-01 |

### [CA-02](../HU-009-modelo-del-resumen-de-sesion.md#ca-02--un-hallazgo-dice-si-está-cerrado-y-por-dónde-sigue) — Un hallazgo dice si está cerrado y por dónde sigue

| ID | Tarea | Capa | Est. | Depende de | Estado | Ev. |
|---|---|---|:--:|---|---|---|
| T-04 | Escribir en `plantillas/sesion.md` cómo se identifica un hallazgo entre sesiones: `AAAA-MM-DD · tema · H-N` | Plantilla | 1 h | — | ☑ | EV-02 |
| T-05 | Escribir qué hace la sesión que hereda un hallazgo abierto: lo nombra y trabaja sobre el original, no lo copia | Plantilla | 1 h | T-04 | ☑ | EV-02 |
| T-06 | Revisar `validadores/historico.py` antes de tocar el índice, por la matriz de §2.2 | Programa | 1 h | — | ☑ | EV-02 |
| T-06b | Modificar `historico.py`: reconocer la línea con enlace al resumen y escribirla, solo si el resumen existe | Programa | 2 h | T-06 | ☑ | EV-02 |
| T-07 | Enlazar el resumen en la línea de cada sesión de `historico-chat/README.md`, al lado de su transcripción | Documentación | 2 h | T-06 | ☑ | EV-02 |

### [CA-03](../HU-009-modelo-del-resumen-de-sesion.md#ca-03--el-resumen-dice-si-la-sesión-se-puede-cerrar) — El resumen dice si la sesión se puede cerrar

| ID | Tarea | Capa | Est. | Depende de | Estado | Ev. |
|---|---|---|:--:|---|---|---|
| T-08 | Comprobar la sección de cierre contra los dos resúmenes reales y ajustar lo que no sirva | Plantilla | 1 h | T-05 | ☑ | EV-03 |

### RNF — Requisitos no funcionales

| ID | Tarea | Categoría | Est. | Estado | Ev. |
|---|---|---|:--:|---|---|
| T-09 | Medir cuánto se demora en leer un resumen real y decidir si hay que acortar el modelo | [RNF-01](../HU-009-modelo-del-resumen-de-sesion.md#5-requisitos-no-funcionales) | 1 h | ☑ | EV-04 |
| T-10 | Leer un hallazgo abierto sin abrir la transcripción y ver si se puede retomar | [RNF-02](../HU-009-modelo-del-resumen-de-sesion.md#5-requisitos-no-funcionales) | 1 h | ☑ | EV-04 |
| T-11 | Comparar los dos resúmenes campo por campo | [RNF-03](../HU-009-modelo-del-resumen-de-sesion.md#5-requisitos-no-funcionales) | 1 h | ☑ | EV-04 |
| T-12 | Anotar [`DOC22`](../../../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md) en `validadores/reglas-validables.md` | Documentación | 1 h | ☑ | EV-04 |
| T-13 | Entrada en `CHANGELOG.md` y subida de `VERSION` ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)) | Documentación | 1 h | ☑ | EV-04 |

**Total estimado:** 17 h. Eran 15 al aprobar; las dos de más son la modificación de `historico.py` que descubrió T-06.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-04 → T-05 → T-08 → T-01 → T-02 → T-03 → T-13

**Paralelizables:** T-06 y T-07 no dependen de las de plantilla; las tres de requisitos no funcionales corren al final, sobre lo ya escrito.

> Solo se tocan los archivos declarados en §2.1 (`F8`). Descubrir uno nuevo → PAUSAR, reportar, ampliar el plan con OK, no editar por iniciativa.

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

> Un CA no se marca cumplido sin evidencia. La fase no cierra con algún CA en rojo. El detalle de casos vive en el `plan_pruebas`.

| Exigencia | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| [CA-01](../HU-009-modelo-del-resumen-de-sesion.md#ca-01--el-modelo-existe-y-se-distingue-de-la-transcripción) | Comparar un resumen con su transcripción y buscar en cuál está cada respuesta | EV-01 | 2026-08-14 | ☑ |
| [CA-02](../HU-009-modelo-del-resumen-de-sesion.md#ca-02--un-hallazgo-dice-si-está-cerrado-y-por-dónde-sigue) | Retomar un hallazgo abierto real sin haber estado en esa sesión | EV-02 | 2026-08-14 | ☑ |
| [CA-03](../HU-009-modelo-del-resumen-de-sesion.md#ca-03--el-resumen-dice-si-la-sesión-se-puede-cerrar) | Leer la sección de cierre de los dos resúmenes | EV-03 | 2026-08-14 | ☑ |
| [RNF-01](../HU-009-modelo-del-resumen-de-sesion.md#5-requisitos-no-funcionales) | Lectura cronometrada de un resumen real | EV-04 | 2026-08-14 | ☑ |
| [RNF-02](../HU-009-modelo-del-resumen-de-sesion.md#5-requisitos-no-funcionales) | Retomar sin abrir la transcripción | EV-04 | 2026-08-14 | ☑ |
| [RNF-03](../HU-009-modelo-del-resumen-de-sesion.md#5-requisitos-no-funcionales) | Comparación campo por campo de los dos resúmenes | EV-04 | 2026-08-14 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | La regla escrita y el índice de la carpeta | `base/13-documentacion/reglas/DOC22-…` · `historico-chat/resumenes/README.md` |
| EV-02 | El modelo con la identificación y la herencia, y el índice enlazado | `plantillas/sesion.md` · `historico-chat/README.md` |
| EV-03 | La sección de cierre de los dos resúmenes reales | `resultado_pruebas.md` de esta fase |
| EV-04 | Las tres mediciones | `resultado_pruebas.md` de esta fase |

---

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | El propio repositorio. El entregable es texto |
| Usuarios de prueba | N/A: no hay autenticación |
| Datos precargados | Los dos resúmenes reales del 2026-08-14 y sus dos transcripciones |

> El detalle completo va en el [plan_pruebas.md](plan_pruebas.md).

---

## 7. Reversión / rollback  ·  `F14` Q11

Todo es texto y no toca datos: se revierte con la reversión del commit. `plantillas/sesion.md` cambia de huella, así que la copia de cada proyecto queda marcada vieja hasta la siguiente corrida del instalador.

---

## 8. Producción y migración incremental  ·  `F10` · `F14` Q12

**Obliga.** [`DOC22`](../../../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md) exige a todo proyecto escribir el resumen de cada sesión, así que el cambio es MAYOR y lleva su aviso de migración.

Qué tiene que hacer un proyecto al día: correr el instalador para recibir el modelo, y crear la carpeta de resúmenes la primera vez que la use. Lo que ya está escrito no se rehace, y una sesión vieja sin resumen no se reabre: la regla aplica al trabajo en curso y al que viene.

Lo que hace llevadera la migración es que el archivo lo va a crear el enganche de EP-005 · HU-008, la fase siguiente. Mientras eso no exista, la regla depende de que alguien se acuerde, y esa es exactamente la falla que H-4 vino a señalar.

---

## 9. Reglas del estándar y del proyecto aplicadas  ·  `F14` Q13

- Base: [`02·F2`](../../../../../base/02-flujo-de-trabajo/reglas/F2-sin-spec-acordada-no-hay-codigo.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F12.1`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md), [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`13·DOC17`](../../../../../base/13-documentacion/reglas/DOC17-manten-un-readme-en-cada-nivel-del-arbol-de-trabajo.md), [`13·DOC19`](../../../../../base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md), [`20·M5`](../../../../../base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md), [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), [`20·M13`](../../../../../base/20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md).
- Proyecto: N/A. Este repositorio es el estándar y no tiene catálogo de reglas propias.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Las dos dudas de §2.7 sin responder | La 1 decidía si el cambio es MAYOR o MENOR; la 2 bloqueaba T-07 | Respondidas por el usuario el 2026-08-14 | Cerrado |
| B-02 | `validadores/historico.py` escribe la línea del índice, y tocar el índice a mano puede romperlo | El índice quedaría inconsistente en la siguiente sesión | T-06 lo revisa antes de T-07 | Abierto |
| B-03 | `validadores/reglas-validables.md` lo está editando otra sesión | T-12 se escribe pero no se puede commitear | Se decide en el commit, no antes | Abierto |

---

## 11. Definition of Done

- [ ] Todas las exigencias de §0 y §1 verificadas con evidencia (§5)
- [ ] Pruebas de la fase en verde (alcance quirúrgico · `F5`)
- [ ] Trazabilidad especificación → implementación sin faltantes (`DOC11`)
- [ ] Documentación e índices actualizados (`13`)
- [ ] Señales registradas (`DOC5`)
- [ ] Rama lista para el commit único de la fase (`G1`)
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario  ·  *(opcional — equipo)*

| Fecha | Tareas cerradas | Avance CA | Bloqueos | Ajuste al plan |
|---|---|---|---|---|
| 2026-08-14 | Las catorce | Las seis exigencias en verde | Ninguno | Una ampliación aprobada, en §2 |

---

## 13. Cierre

**Resultado:** las seis exigencias cumplidas, con un defecto abierto que el plan ya declaraba fuera de alcance (DEF-01). **Esfuerzo real vs. estimado:** 17 h estimadas tras la ampliación.

**Lecciones aprendidas:** la tarea que decía "revisar antes de tocar" fue la que salvó la fase. Sin ella, el índice del histórico habría quedado con líneas duplicadas y nadie se habría dado cuenta hasta la sesión siguiente.

**Deuda técnica generada:**

| Descripción | Registro / ticket |
|---|---|
| El resumen más viejo no tiene el campo «viene de» | DEF-01 del resultado de pruebas. Se llena si alguna vez se toca ese archivo |
| La regla [`DOC22`](../../../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md) obliga y todavía no la valida ningún programa | Anotada en `validadores/reglas-validables.md`; la construye EP-004 |
