# Las fichas de `prompts/` como candidatas a regla

> **Qué es.** El mapa de qué hacer con cada ficha de [`prompts/`](../README.md) antes de crear o cambiar una sola regla. Sale del prompt [`prompt-analisis-reglas-v2.md`](prompt-analisis-reglas-v2.md).
>
> **Cuándo.** 2026-08-13, contra el estándar en **v8.0.0**.
>
> **Qué no es.** No se creó ni se cambió ninguna regla. Esto es el mapa; qué se construye de él lo decide el usuario.

**27 fichas analizadas.** 13 ya están cubiertas por una regla vigente, 7 piden regla nueva, 3 se resuelven afinando una existente y 4 no son regla del estándar.

---

## 1 · Tabla resumen

| # | Ficha | Salida | Regla relacionada | Versión |
|---|---|---|---|---|
| 1 | [redaccion-clara-para-quien-no-sabe](../redaccion-clara-para-quien-no-sabe.md) | Ya está cubierta | [`00·ID7`](../../base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md) | — |
| 2 | [menos-es-mas](../menos-es-mas.md) | Ya está cubierta | [`01·C5`](../../base/01-conducta.md#c5--responde-corto) · [`00·ID7`](../../base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md) | — |
| 3 | [sin-marcadores-de-ia](../1. sin-marcadores-de-ia.md) | Ya está cubierta | [`00·ID8`](../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | — |
| 4 | [espanol-colombiano-correcto](../espanol-colombiano-correcto.md) | **Complementar una regla** → `00·ID9` | extiende [`00·ID7`](../../base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md) | MAYOR |
| 5 | [historico-de-cada-sesion](../historico-de-cada-sesion.md) | **Regla nueva sin dependencia** → `13·DOC19` | ninguna | MAYOR |
| 6 | [la-sesion-se-nombra-al-abrirla](../la-sesion-se-nombra-al-abrirla.md) | **Complementar una regla** → `13·DOC20` | extiende `13·DOC19` | MENOR |
| 7 | [memoria-en-el-repo](../memoria-en-el-repo.md) | Ya está cubierta | [`01·C19`](../../base/01-conducta.md#c19--escribe-la-memoria-del-agente-dentro-del-repositorio-del-proyecto) | — |
| 8 | [la-instalacion-no-borra-lo-que-ya-existe](../la-instalacion-no-borra-lo-que-ya-existe.md) | **Regla nueva sin dependencia** → `11·CFG5` | ninguna | MAYOR |
| 9 | [toda-herramienta-se-replica-sola](../toda-herramienta-se-replica-sola.md) | **No es regla** → `CLAUDE.md` del repositorio | [`01·C18`](../../base/01-conducta.md#c18--auto-sincronización-del-claudemd-con-la-plantilla-central) | — |
| 10 | [claude-md-es-el-setup-del-agente](../claude-md-es-el-setup-del-agente.md) | Ya está cubierta | [`01·C18`](../../base/01-conducta.md#c18--auto-sincronización-del-claudemd-con-la-plantilla-central) · [`02·F13`](../../base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md) | — |
| 11 | [checklist-de-instalacion-incompleta](../checklist-de-instalacion-incompleta.md) | Ya está cubierta | [`02·F13`](../../base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md) | — |
| 12 | [stack-de-instalacion-y-actualizaciones](../stack-de-instalacion-y-actualizaciones.md) | **Afinar una regla** | [`01·C18`](../../base/01-conducta.md#c18--auto-sincronización-del-claudemd-con-la-plantilla-central) | PARCHE |
| 13 | [cada-cita-lleva-su-link](../cada-cita-lleva-su-link.md) | Ya está cubierta | [`20·M15`](../../base/20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md) · [`13·DOC14`](../../base/13-documentacion/reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md) | — |
| 14 | [checklist-dentro-de-cada-regla](../checklist-dentro-de-cada-regla.md) | Ya está cubierta | [`20·M14`](../../base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md) | — |
| 15 | [la-regla-en-reglas-la-explicacion-en-base](../la-regla-en-reglas-la-explicacion-en-base.md) | **Afinar una regla** | [`20·M2`](../../base/20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md) | PARCHE |
| 16 | [analisis-de-reglas-candidatas](../analisis-de-reglas-candidatas.md) | **No es regla** → instrumento del repositorio | [`13·DOC8`](../../base/13-documentacion/reglas/DOC8-cierra-todo-analisis-con-su-tabla-de-decisiones.md) | — |
| 17 | [analisis-de-cumplimiento-de-reglas](../analisis-de-cumplimiento-de-reglas.md) | **No es regla** → instrumento del repositorio | [`20·checklist.md`](../../base/20-meta-reglas/checklist.md) | — |
| 18 | [el-informe-no-se-corrige-se-enlaza](../el-informe-no-se-corrige-se-enlaza.md) | Ya está cubierta | [`13·DOC8`](../../base/13-documentacion/reglas/DOC8-cierra-todo-analisis-con-su-tabla-de-decisiones.md) | — |
| 19 | [documentacion-de-cada-archivo-de-codigo](../documentacion-de-cada-archivo-de-codigo.md) | **Complementar una regla** → `13·DOC21` *opt-in* | extiende [`13·DOC13`](../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md) | MENOR |
| 20 | [mapa-del-sitio-siempre-al-dia](../mapa-del-sitio-siempre-al-dia.md) | Ya está cubierta | [`13·DOC17`](../../base/13-documentacion/reglas/DOC17-manten-un-readme-en-cada-nivel-del-arbol-de-trabajo.md) | — |
| 21 | [no-tocar-lo-de-otras-sesiones](../no-tocar-lo-de-otras-sesiones.md) | **Complementar una regla** → `09·G9` | extiende [`09·G1`](../../base/09-git.md#g1--commits-atómicos-un-solo-propósito) | MAYOR |
| 22 | [una-pregunta-no-es-una-instruccion](../una-pregunta-no-es-una-instruccion.md) | **Complementar una regla** → `01·C20` | extiende [`01·C4`](../../base/01-conducta.md#c4--no-decidas-por-tu-cuenta) | MAYOR |
| 23 | [trabajo-confinado-a-la-carpeta](../trabajo-confinado-a-la-carpeta.md) | Ya está cubierta | [`01·C3`](../../base/01-conducta.md#c3--quédate-en-tu-tarea) · [`02·F8`](../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md) | — |
| 24 | [preguntas-en-el-chat-no-en-formulario](../preguntas-en-el-chat-no-en-formulario.md) | Ya está cubierta | [`01·C13`](../../base/01-conducta.md#c13--preguntas-de-análisis-van-en-chat-abierto-no-en-formulario-cerrado) | — |
| 25 | [corregir-lo-que-esta-mal-sin-preguntar](../corregir-lo-que-esta-mal-sin-preguntar.md) | **Afinar una regla** | [`02·F20`](../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md) | PARCHE |
| 26 | [lo-que-pueda-hacer-un-script-no-lo-hace-la-ia](../lo-que-pueda-hacer-un-script-no-lo-hace-la-ia.md) | **No es regla** → `pendientes/` | [`20·M9`](../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md) | — |
| 27 | [regla-reglas-proyecto](../regla-reglas-proyecto.md) | Ya está cubierta | [`20·M16`](../../base/20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md) | — |

---

## 2 · Lo que pide regla nueva

### 4 · El texto cumple la norma del idioma que el proyecto declara

**Qué exige la ficha:** que lo escrito respete ortografía, gramática y sintaxis del español colombiano.

**Por qué no está cubierta.** [`01·C8`](../../base/01-conducta.md#c8--habla-el-idioma-del-proyecto) fija **cuál** idioma y nada más. [`00·ID7`](../../base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md) exige que se entienda y [`00·ID8`](../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) que no suene a máquina. Un texto puede cumplir las tres y estar lleno de faltas: son exigencias distintas. El propio `CHANGELOG` de la 7.0.0 lo dejó dicho, *"y la primera todavía no tiene regla"*.

| | |
|---|---|
| **Salida** | Complementar: regla nueva que declara `(extiende 00·ID7)` |
| **Capa y capítulo** | Preámbulo · [`00 · Identidad y rol`](../../base/00-identidad-y-rol/base.md), dueño de cómo escribe el agente |
| **ID libre** | `ID9` |
| **Agnóstica** | Sí, si la regla exige *"la norma del idioma y la variedad que el proyecto declara"*. Nombrar el español colombiano dentro de `base/` reprobaría [`20·M3`](../../base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md): la variedad la declara la capa 3, y esa `P` queda respaldada por esta regla ([`20·M16`](../../base/20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md)) |
| **Validable** | Parcial: un corrector cuenta faltas de ortografía; concordancia y sintaxis las juzga quien lee |
| **Versión** | MAYOR |

### 5 · Toda sesión queda escrita en el histórico

**Qué exige la ficha:** que cada intercambio, del usuario y del agente, quede transcrito literal, con fecha y hora, sin que haya que pedirlo.

**Por qué no está cubierta.** Es el hallazgo más grande de este análisis. El histórico se sostiene hoy en tres cosas que **no son regla del estándar**: el [`CLAUDE.md`](../../CLAUDE.md) de este repositorio, la plantilla [`historico-chat.md`](../../plantillas/historico-chat.md) y el enganche `hook_historico.py`. En `base/` no hay ninguna regla que lo exija: [`01·C19`](../../base/01-conducta.md#c19--escribe-la-memoria-del-agente-dentro-del-repositorio-del-proyecto) cubre la **memoria**, que es otra cosa. Un proyecto que herede el estándar y desactive el enganche no incumple nada.

| | |
|---|---|
| **Salida** | Regla nueva sin dependencia |
| **Capa y capítulo** | Capa 2 · [`13 · Documentación`](../../base/13-documentacion/base.md), dueño de lo que se persiste |
| **ID libre** | `DOC19` |
| **Agnóstica** | Sí: ningún stack ni dominio |
| **Validable** | Sí, y ya hay validador (`historico.py`); falta atarlo a la regla |
| **Versión** | MAYOR |

### 6 · La sesión se nombra por su tema

**Qué exige la ficha:** que la sesión pida su nombre y que ese nombre se vea también en la pestaña.

| | |
|---|---|
| **Salida** | Complementar: regla nueva que declara `(extiende 13·DOC19)` |
| **Capa y capítulo** | Capa 2 · `13 · Documentación` |
| **ID libre** | `DOC20` |
| **Agnóstica** | Sí |
| **Validable** | Sí: el archivo con nombre genérico y la marca de que ya se preguntó |
| **Versión** | MENOR (aditivo) |
| **Depende de** | La `DOC19`. Sin la regla del histórico, esta no tiene de qué colgar |

### 8 · Instalar no destruye lo que ya existe

**Qué exige la ficha:** que el instalador sea idempotente y que, si algo ya está, no lo toque.

**Por qué no está cubierta.** Nace de un daño real: el instalador borró la carpeta de memoria del proyecto, dos veces. [`00·N3`](../../base/00-nucleo-blindado.md#n3--no-romper-cosas-para-pasar-un-obstáculo-blindada) prohíbe romper para avanzar y [`00·N5`](../../base/00-nucleo-blindado.md#n5--operaciones-masivas-previsualizar-antes-de-aplicar-blindada) obliga a previsualizar lo masivo, pero ninguna exige que **instalar de nuevo sea inofensivo**. [`01·C18`](../../base/01-conducta.md#c18--auto-sincronización-del-claudemd-con-la-plantilla-central) lo dice solo del `CLAUDE.md`.

| | |
|---|---|
| **Salida** | Regla nueva sin dependencia. No puede declararse `extiende` de una `[BLINDADA]`: [`20·M7`](../../base/20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md) prohíbe apuntar hacia arriba |
| **Capa y capítulo** | Capa 2 · [`11 · Configuración y entornos`](../../base/11-configuracion-entornos.md) |
| **ID libre** | `CFG5` |
| **Agnóstica** | Sí: vale para cualquier instalador o script de arranque |
| **Validable** | Sí: correr el instalador dos veces y comparar el árbol |
| **Versión** | MAYOR |

### 19 · Cada archivo de código tiene su documento

**Qué exige la ficha:** un `.md` por archivo, sacado del código y no de suposiciones, en lenguaje claro.

**Por qué no está cubierta.** [`13·DOC13`](../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md) registra el **módulo** en el catálogo y [`13·DOC6`](../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md) retro-documenta el que no tiene spec. Ninguna baja al archivo.

| | |
|---|---|
| **Salida** | Complementar: regla nueva `(extiende 13·DOC13)`, marcada `*opt-in*` |
| **ID libre** | `DOC21` |
| **Agnóstica** | Sí |
| **Validable** | Sí: por cada archivo de código, su documento |
| **Versión** | MENOR, por ser opt-in. Sin el opt-in sería MAYOR y obligaría a documentar el código ya escrito de todos los proyectos |

### 21 · Se versiona solo lo que hizo esta sesión

**Qué exige la ficha:** no commitear el trabajo de otras sesiones, porque mezcla el versionado.

**Por qué no está cubierta.** [`09·G1`](../../base/09-git.md#g1--commits-atómicos-un-solo-propósito) pide un solo propósito por commit y [`09·G7`](../../base/09-git.md#g7--todo-commit-se-muestra-al-usuario-y-se-aprueba-antes-de-ejecutarlo) que el usuario lo apruebe. Dos trabajos de sesiones distintas pueden compartir propósito y aun así no deben ir juntos: lo que falta es **de quién es el cambio**, no de qué trata.

| | |
|---|---|
| **Salida** | Complementar: regla nueva `(extiende 09·G1)` |
| **Capa y capítulo** | Capa 2 · [`09 · Git`](../../base/09-git.md) |
| **ID libre** | `G9` |
| **Agnóstica** | Sí |
| **Validable** | Parcial: un script ve qué archivos tocó la sesión, pero no siempre quién los dejó modificados antes |
| **Versión** | MAYOR |
| **Ojo** | Esta sesión tropezó justo con eso: la 7.0.0 quedó sin commitear y hubo que separarla a mano de la 8.0.0 |

### 22 · Una pregunta no es una instrucción

**Qué exige la ficha:** si el usuario pregunta, se responde y no se edita nada.

**Por qué no está cubierta.** [`01·C4`](../../base/01-conducta.md#c4--no-decidas-por-tu-cuenta) prohíbe decidir por cuenta propia y [`01·C1`](../../base/01-conducta.md#c1--avisa-antes-de-tocar) obliga a avisar antes de tocar. Ninguna dice que **una pregunta no autoriza a escribir**, que es el caso concreto y repetido: aparece cuatro veces en el histórico, en tres sesiones distintas.

| | |
|---|---|
| **Salida** | Complementar: regla nueva `(extiende 01·C4)` |
| **Capa y capítulo** | Capa 2 · [`01 · Conducta`](../../base/01-conducta.md) |
| **ID libre** | `C20` |
| **Agnóstica** | Sí |
| **Validable** | No: distinguir pregunta de orden es criterio |
| **Versión** | MAYOR |

---

## 3 · Lo que se resuelve afinando

| Ficha | Regla | Qué se le agrega | Versión |
|---|---|---|---|
| 12 · stack y actualizaciones | [`01·C18`](../../base/01-conducta.md#c18--auto-sincronización-del-claudemd-con-la-plantilla-central) | El paso 5 ya deja el registro de versiones. Falta lo que el usuario pidió expreso: al proyecto se le avisa **solo lo que le toca aplicar**, no el `CHANGELOG` entero | PARCHE |
| 15 · la regla en `reglas/`, la explicación en `base.md` | [`20·M2`](../../base/20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md) | Hoy dice "una regla, un archivo" y el reparto vive solo en la práctica. Falta escribir que en `reglas/` va la exigencia y en `base.md` su desarrollo. Ojo con [`20·M5`](../../base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md), que manda el **porqué** a `notas/`: son dos cosas distintas y hay que dejarlas separadas en el texto | PARCHE |
| 25 · corregir sin preguntar | [`02·F20`](../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md) | Choque real con la ficha: `F20` manda parar y proponer lo que se descubre fuera del criterio de aceptación; el usuario pide que lo que el agente **reporta como defecto** lo arregle sin preguntar. Se separan los dos casos dentro de `F20`: mejora fuera de alcance se propone, defecto que el propio agente señaló se corrige | PARCHE |

---

## 4 · Lo que no es regla del estándar

| Ficha | A dónde va | Por qué |
|---|---|---|
| 9 · toda herramienta se replica sola | [`CLAUDE.md`](../../CLAUDE.md) del repositorio | Es instructivo para **mantener el estándar**, no norma para cualquier proyecto ([`20·M13`](../../base/20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md)). Lo que sí es regla ya está en [`01·C18`](../../base/01-conducta.md#c18--auto-sincronización-del-claudemd-con-la-plantilla-central) |
| 16 · análisis de reglas candidatas | Instrumento del repositorio | Es un procedimiento del estándar sobre sí mismo, como el [checklist](../../base/20-meta-reglas/checklist.md). Su sitio natural es `20-meta-reglas/`, junto al procedimiento, o `prompts/analisis/` como está hoy. No exige nada a un proyecto |
| 17 · análisis de cumplimiento | Instrumento del repositorio | Mismo caso, y en buena parte ya existe: el [checklist](../../base/20-meta-reglas/checklist.md) con [`20·M14`](../../base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md) es la versión regla por regla de esa auditoría |
| 26 · lo que pueda un script no lo hace la IA | [`pendientes/`](../../pendientes/README.md) | Es criterio de construcción del agente, no norma de trabajo. Ya tiene su pendiente: [`09-autonomia-sin-ia.md`](../../pendientes/09-autonomia-sin-ia.md). Para reglas, [`20·M9`](../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md) ya obliga a declarar si es validable |

---

## 5 · Choques entre fichas

| Se pisan | Qué pasa | Qué queda |
|---|---|---|
| 1 · redacción clara **vs** 2 · menos es más | Las dos piden lo mismo por dos lados: entender fácil y no extenderse | `00·ID7` las absorbe. `01·C5` cubre el largo de la respuesta en el chat. Ninguna ficha nueva |
| 5 · histórico **vs** 6 · nombre de la sesión | La 6 no se sostiene sin la 5 | Se escribe primero la `DOC19` y la `DOC20` la extiende |
| 9 · replicar sola **vs** 10 · setup **vs** 11 · checklist **vs** 12 · actualizaciones | Las cuatro orbitan la misma pieza: el instalador y `C18` | 10 y 11 ya están cubiertas, 12 afina `C18`, 9 sale de `base/` |
| 16 · candidatas **vs** 17 · cumplimiento | Dos formatos de análisis del mismo objeto | Se unifican en un solo instrumento; hoy el checklist ya hace la mitad |
| 25 · corregir sin preguntar **vs** `02·F20` | Contradicción de fondo, no de redacción | Se resuelve **en el texto** de `F20` ([`20·M6`](../../base/20-meta-reglas/reglas/M6-ante-un-conflicto-el-desempate-es-este-y-en-este-orden.md)), separando defecto de mejora |
| 22 · pregunta no es instrucción **vs** 24 · preguntas en el chat | Suenan parecidas y no lo son: una es quién pregunta al agente, la otra cómo pregunta el agente | Las dos se quedan, sin cruzarse |

---

## 6 · Cierre: en qué orden

| Orden | Qué | Depende de | Versión |
|---|---|---|---|
| 1 | `13·DOC19` · toda sesión queda escrita | — | MAYOR |
| 2 | `13·DOC20` · la sesión se nombra por su tema | `DOC19` | MENOR |
| 3 | `01·C20` · una pregunta no es una instrucción | — | MAYOR |
| 4 | `09·G9` · se versiona solo lo de esta sesión | — | MAYOR |
| 5 | `11·CFG5` · instalar no destruye | — | MAYOR |
| 6 | `00·ID9` · la norma del idioma | Que la capa 3 declare su variedad | MAYOR |
| 7 | `13·DOC21` · un documento por archivo de código | `DOC13` | MENOR |
| 8 | Afinar `01·C18`, `20·M2` y `02·F20` | Independientes entre sí | PARCHE |
| 9 | Mover al `CLAUDE.md` lo de la ficha 9 y cerrar 16, 17 y 26 | — | — |

**Cómo conviene versionarlo.** Los pasos 1 a 6 son cinco MAYOR seguidas. Si se hacen de a una, un proyecto que herede el estándar recibe cinco avisos de migración en el mismo día. Conviene una sola entrada del `CHANGELOG` que las agrupe, o un orden en el que cada una se cierre y se avise con la anterior. Lo decide el usuario ([`20·M10`](../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).

**Lo que este análisis deja abierto.** Los ID propuestos (`ID9`, `C20`, `G9`, `CFG5`, `DOC19`, `DOC20`, `DOC21`) son los consecutivos libres **hoy**. Si otra sesión crea una regla en esos capítulos antes de ejecutar este plan, hay que volver a pedir el siguiente libre ([`20·M4`](../../base/20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md)).
