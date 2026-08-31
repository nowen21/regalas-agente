# Plan de Trabajo — Fase «A-EP-005-HU-012-que-cada-regla-del-nucleo-diga-quien-la-hace-cumplir» (módulo «Automatismos — enganches»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Se escribe **antes** de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-012-que-cada-regla-del-nucleo-diga-quien-la-hace-cumplir` |
| **Épica** | [`EP-005 · Automatismos que no dependen de la memoria`](../../epica.md) |
| **HU** | [`HU-012 · Hacer cumplir lo que hoy solo se recuerda`](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md) — **una sola** (`F12.1`) |
| **Módulo** | Automatismos — enganches ([`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)) |
| **Especificación del módulo** | La HU citada arriba. El estándar no lleva especificación de módulo aparte: la exigencia y sus criterios viven en la historia ([`02·F2`](../../../../../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md)) |
| **Fecha apertura** | 2026-08-31 |
| **Rama** | `main` — el estándar trabaja sobre la rama principal, por decisión registrada del usuario |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- ✨ **Funcionalidad nueva:** una comprobación que hoy no existe —que toda regla del núcleo diga quién la hace cumplir— y la pieza que hace cumplir las tres reglas de redacción, que hasta hoy dependían de que el agente se acordara.

**CA de la HU que cubre esta fase** (una sola HU, `02·F12.1`, trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-012` que cierra esta fase | Estado |
|---|---|
| [CA-01 — Una regla de núcleo sin forma de cumplirse se reporta](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#ca-01--una-regla-de-núcleo-sin-forma-de-cumplirse-se-reporta) | ☐ |
| [CA-02 — «No se puede hacer cumplir» vale, pero con motivo](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#ca-02--no-se-puede-hacer-cumplir-vale-pero-con-motivo) | ☐ |
| [CA-03 — La pieza declarada existe](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#ca-03--la-pieza-declarada-existe) | ☐ |
| [CA-04 — `ID9` queda con su decisión escrita](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#ca-04--id9-queda-con-su-decisión-escrita) | ☐ |

---

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que ninguna regla del capítulo `00` pueda existir sin decir quién la hace cumplir, y que la respuesta quede escrita en las dieciocho que hoy rigen.

**La medición que abre la fase.** Se contaron las reglas vigentes del capítulo `00` y se buscó su identificador dentro de los programas de comprobación y de los enganches ([`historico-chat/scripts/2026-08-31/medir-quien-hace-cumplir-el-nucleo.py`](../../../../../historico-chat/scripts/2026-08-31/medir-quien-hace-cumplir-el-nucleo.py)):

| Lo medido | Cuántas |
|---|---|
| Reglas vigentes del capítulo `00` | 18 |
| No se nombran en ningún programa ni enganche | 7 — `N5`, `N8`, `ID1`, `ID4`, `ID5`, `ID6`, `ID10` |
| Se nombran en alguno | 11 |
| De esas once, **hacen cumplir de verdad** | 2 — `ID8`, que el `pre-commit` rechaza, y `N6`, que caza `secretos.py` |

**Catorce de dieciocho no tienen quién las ejecute.** Esa es la cuenta que la fase deja escrita, y que el usuario decidió no dejar como catorce pendientes sueltos.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | La regla sin declaración se reporta y la corrida falla | Funcional | Media |
| CA-02 | «Nadie la hace cumplir» vale con motivo, no sin él | Funcional | Baja |
| CA-03 | La pieza declarada tiene que existir en el repositorio | Funcional | Baja |
| CA-04 | `ID9` queda con su decisión escrita | Funcional | Baja |
| RNF-01 | El mensaje dice qué falta y dónde escribirlo | No funcional | Baja |
| RNF-02 | El mismo cuerpo de reglas da el mismo resultado | No funcional | Baja |

**Fuera de alcance:**

- Las reglas que no son del capítulo `00` (§3.3 de la HU). Se hará si el caso se repite fuera del núcleo.
- Hacer cumplir con un programa las reglas de criterio. La declaración de que **no lo tienen**, con su motivo, es lo que la fase entrega para ellas; construirles un programa sería simular la comprobación.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/redaccion.py` | Nuevo | Validador | Mide sobre un texto el trato de `ID10`, las marcas de `ID8` y el largo contra el umbral de `brevedad.py` |
| `adaptadores/claude-code/hook_redaccion.py` | Nuevo | Enganche | `Stop`: mide lo que el agente acaba de escribir y lo deja a la vista |
| `validadores/ejecutable.py` | Nuevo | Validador | Recorre el capítulo `00` y reporta la regla que no declara quién la hace cumplir |
| `validadores/validar.py` | Modificar | Punto de entrada | Subcomando `ejecutable`, y entrada en la corrida de `estandar` |
| `validadores/instalar.py` | Modificar | Instalador | El enganche `Stop` nuevo, que es el único canal (`RN-04`) |
| `base/00-nucleo-blindado.md` | Modificar | Reglas | La declaración de `N1` a `N9`. **No cambia lo que exigen** |
| `base/00-identidad-y-rol/reglas/ID*.md` (9 archivos) | Modificar | Reglas | La declaración de cada una |
| `validadores/metareglas.py` | Modificar | Validador | **Descubierto al construir** (`02·F8`): la línea nueva le caía dentro del cuerpo de la regla, y hacía reprobar la fila 10 y vencer el sello a reglas que no habían cambiado lo que exigen |
| `base/20-meta-reglas/estructura-regla.md` | Modificar | Molde | Dónde va la declaración dentro de la regla |
| `validadores/reglas-validables.md` | Modificar | Catálogo | La nota de que `ID8`, `ID9` e `ID10` ya tienen quien las mida |
| `validadores/tests/test_la_regla_del_nucleo_dice_quien_la_hace_cumplir.py` | Nuevo | Prueba | CA-01 a CA-04 |
| `validadores/tests/test_lo_que_se_acaba_de_escribir_se_mide.py` | Nuevo | Prueba | La pieza de redacción y su enganche |
| `CHANGELOG.md` · `VERSION` | Modificar | Versión | `20·M10` |

### 2.2 Matriz de dependencias del refactor

No aplica: nada de lo que se toca cambia un contrato del que dependa otro archivo. `redaccion.py` **usa** `marcas.py` y `brevedad.py` sin modificarlos.

### 2.3 Rutas / endpoints y control de acceso

No aplica: el estándar no expone rutas.

### 2.4 Punto de entrada en la UI

No aplica: no hay interfaz. Los dos puntos de entrada son la línea de comandos (`validar.py ejecutable`) y el enganche de cierre de turno, que escribe en la consola de la sesión.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La declaración va **dentro del archivo de la regla**, en una línea de molde fijo | Registrarla en `validadores/reglas-validables.md`, como hace `20·M9` con la validabilidad | Ese catálogo es prosa larga y por capítulos; leer de ahí «quién hace cumplir a `N5`» exige interpretar, y `RNF-02` pide que el mismo cuerpo de reglas dé siempre el mismo resultado. En el archivo de la regla la respuesta está donde se lee la exigencia |
| Dos aperturas exactas: **Quién la hace cumplir** y **Nadie la hace cumplir** | Un campo único de valor libre | Un campo libre deja «pendiente» y «se está viendo» como respuestas válidas, que es justo lo que la historia quiere impedir |
| El motivo del «nadie» se exige con un largo mínimo | Aceptar cualquier texto | El `CA-02` lo dice de frente: una casilla marcada sin motivo no es una decisión |
| Una sola pieza para `ID8`, `ID9` e `ID10`: medir el turno al cerrarlo | Catorce pendientes, uno por regla | Decisión del usuario el 2026-08-31: *«no las deje como pendiente de una solución»*. Las tres son medibles sobre el mismo texto y en el mismo momento |
| El enganche **mide y no detiene** | Devolver la respuesta para que se reescriba | Está escrito en la HU §3 como límite técnico: cuando el enganche corre el texto ya salió, y devolverlo le cuesta al usuario leer la versión larga primero y la corta después |
| El umbral de largo sale de `brevedad.HOLGADO` | Un número propio en `redaccion.py` | Dos umbrales que empiezan iguales se separan sin que nadie lo note (`S-091`) |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | Si las catorce reglas sin quién las ejecute se dejan como pendientes o se resuelven en esta fase | usuario | **Resuelta** el 2026-08-31: se resuelven acá, con una sola pieza para las tres medibles y la declaración escrita para las demás |
| 2 | Si avisarle a `shopnest-mesa` (CA-04, paso 3) lo hace esta fase escribiendo en ese repositorio | usuario | **Abierta.** Escribir en otro repositorio es un cambio de estado ajeno ([`00·N1`](../../../../../base/00-nucleo-blindado.md)); se pregunta antes de hacerlo, y no bloquea ningún CA |

---

## 3. Desglose de tareas por criterio de aceptación

### [CA-01](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#ca-01--una-regla-de-núcleo-sin-forma-de-cumplirse-se-reporta) — Una regla de núcleo sin forma de cumplirse se reporta

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Fijar en [`estructura-regla.md`](../../../../../base/20-meta-reglas/estructura-regla.md) dónde va la declaración y con qué palabras abre | Reglas | 1 h | — | EV-04 |
| T-02 | `ejecutable.py`: leer las reglas vigentes del capítulo `00` y su declaración | Validador | 2 h | T-01 | EV-01 |
| T-03 | Subcomando `validar.py ejecutable`, y entrada en la corrida de `estandar` | Validador | 1 h | T-02 | EV-01 |
| T-04 | Pruebas del CA-01 | Test | 1 h | T-03 | EV-01 |

### [CA-02](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#ca-02--no-se-puede-hacer-cumplir-vale-pero-con-motivo) — «No se puede hacer cumplir» vale, pero con motivo

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-05 | Aceptar la declaración de «nadie» con motivo, y reportarla sin él | Validador | 1 h | T-02 | EV-01 |
| T-06 | Pruebas del CA-02 | Test | 1 h | T-05 | EV-01 |

### [CA-03](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#ca-03--la-pieza-declarada-existe) — La pieza declarada existe

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-07 | Resolver contra el disco cada pieza nombrada, y reportar la que no exista | Validador | 1 h | T-02 | EV-01 |
| T-08 | Pruebas del CA-03 | Test | 1 h | T-07 | EV-01 |

### [CA-04](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#ca-04--id9-queda-con-su-decisión-escrita) — `ID9` queda con su decisión escrita

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-09 | `redaccion.py`: medir sobre un texto el trato de `ID10`, las marcas de `ID8` y el largo contra `brevedad.HOLGADO` | Validador | 2 h | — | EV-02 |
| T-10 | `hook_redaccion.py`: enganche `Stop` que mide lo que el agente acaba de escribir | Enganche | 1 h | T-09 | EV-02 |
| T-11 | Declararlo en `instalar.py`, que es el único canal (`RN-04`), y correr el instalador | Instalador | 1 h | T-10 | EV-03 |
| T-12 | Escribir la declaración en las dieciocho reglas del capítulo `00` | Reglas | 3 h | T-01 | EV-04 |
| T-13 | Poner al día [`reglas-validables.md`](../../../../../validadores/reglas-validables.md): `ID8`, `ID9` e `ID10` ya tienen quien las mida | Catálogo | 1 h | T-12 | EV-04 |
| T-14 | Pruebas de la pieza de redacción y de su enganche | Test | 2 h | T-10 | EV-02 |

### RNF — Requisitos no funcionales

| ID | Tarea | Categoría | Est. | Ev. |
|---|---|---|:--:|---|
| T-15 | Que el mensaje diga qué falta declarar y dónde escribirlo ([RNF-01](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#5-requisitos-no-funcionales)) | Claridad | 1 h | EV-01 |
| T-16 | Que dos corridas sobre el mismo cuerpo de reglas den lo mismo ([RNF-02](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#5-requisitos-no-funcionales)) | Determinismo | 1 h | EV-01 |
| T-17 | Versionar (`20·M10`) y registrar en el `CHANGELOG.md` | Versión | 1 h | EV-05 |

**Total estimado:** 22 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-12 → T-17
**Paralelizables:** T-09 y T-10 no dependen del molde de la declaración; T-05 y T-07 cuelgan de T-02 y no entre sí.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| [CA-01](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#ca-01--una-regla-de-núcleo-sin-forma-de-cumplirse-se-reporta) | Correr la comprobación sobre un cuerpo de reglas de prueba al que le falta la declaración, y sobre el núcleo real | EV-01 | | ☐ |
| [CA-02](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#ca-02--no-se-puede-hacer-cumplir-vale-pero-con-motivo) | Declaración de «nadie» con motivo y sin motivo | EV-01 | | ☐ |
| [CA-03](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#ca-03--la-pieza-declarada-existe) | Pieza inventada contra pieza real | EV-01 | | ☐ |
| [CA-04](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#ca-04--id9-queda-con-su-decisión-escrita) | Leer `ID9` después del cambio; correr el enganche de punta a punta | EV-02, EV-03, EV-04 | | ☐ |
| [RNF-01](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#5-requisitos-no-funcionales) | El texto del hallazgo nombra el archivo y la línea de molde que falta | EV-01 | | ☐ |
| [RNF-02](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#5-requisitos-no-funcionales) | Dos corridas seguidas sobre el mismo árbol | EV-01 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Corrida de las pruebas del validador | `resultado_pruebas.md` §3 |
| EV-02 | Corrida de las pruebas de la pieza de redacción | `resultado_pruebas.md` §3 |
| EV-03 | Salida del instalador y del enganche de punta a punta | `resultado_pruebas.md` §4 |
| EV-04 | Las dieciocho reglas con su declaración escrita | `base/00-nucleo-blindado.md` y `base/00-identidad-y-rol/reglas/` |
| EV-05 | Entrada del registro de cambios y número de versión | [`CHANGELOG.md`](../../../../../CHANGELOG.md) · [`VERSION`](../../../../../VERSION) |

---

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | El propio repositorio del estándar, y cuerpos de reglas armados en carpetas temporales. Nunca datos reales ([`00·N4`](../../../../../base/00-nucleo-blindado.md)) |
| Usuarios de prueba | No aplica |
| Datos precargados | Cuerpos de reglas de mentiras que la propia prueba escribe y borra |

---

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Todo lo que se toca está versionado y se revierte con el control de versiones. La única salvedad es `.claude/settings.json`, que no se versiona: se reconstruye corriendo `python validadores/instalar.py <ruta> --aplicar`, que es idempotente.

---

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

**Aditivo, y con una consecuencia para quien hereda.** La comprobación nueva recorre el `base/` del propio estándar, no el de los proyectos: un proyecto al día no tiene que hacer nada. El enganche nuevo le llega la próxima vez que corra el instalador, y como mide sin detener, no puede romperle una sesión a nadie. Sube **MENOR**.

---

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md) (la hermana: declarar si es validable), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md), [`00·ID9`](../../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md), [`00·ID10`](../../../../../base/00-identidad-y-rol/reglas/ID10-escribe-en-el-idioma-del-proyecto-en-tercera-persona-y-en-infinitivo.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md).
- Proyecto: no aplica — este repositorio **es** el estándar y no tiene capa de proyecto.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que la declaración se llene con «nadie» en las dieciocho y la exigencia quede vacía | Alto — la historia quedaría cumplida en la forma y no en el fondo | El motivo lo lee una persona, y la fase entrega **una pieza que sí ejecuta** para las tres medibles | Cerrado |
| B-02 | Que la línea nueva dentro de una regla `[BLINDADA]` se lea como una modificación de la regla | Medio | La declaración va **fuera del cuerpo**, después del ejemplo, y no cambia lo que la regla exige. `20·M7` prohíbe aflojarla, no describirla | Cerrado |
| B-03 | Avisarle a `shopnest-mesa` exige escribir en otro repositorio | Bajo — no bloquea ningún CA | Se pregunta antes (duda 2 de §2.7) | Abierto |

---

## 11. Definition of Done

- [ ] Todos los CA de §0 verificados con evidencia (§5)
- [ ] Requisitos no funcionales validados
- [ ] Pruebas de la fase en verde (alcance quirúrgico, [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md))
- [ ] Trazabilidad especificación → implementación sin faltantes ([`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))
- [ ] Documentación e índices del estándar al día (`13`)
- [ ] Señales registradas ([`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md))
- [ ] Versionada (`20·M10`)
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario  ·  *(opcional — equipo)*

No aplica: la fase se ejecuta en una jornada y una sola persona la lleva.

---

## 13. Cierre

**No se escribe acá.** El cierre de la fase vive en el `funcionalidad_implementada.md`.
