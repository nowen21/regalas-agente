# Análisis 1: de los enganches, solo el freno se puede suspender desde Cimiento

> **Aprobado** por el usuario el 2026-10-09, en el turno 27, con la versión 56.8.0. Desde ese momento este análisis no se reescribe.

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Un análisis aprobado no se reescribe. Si al ejecutar el plan aparece un hallazgo que obliga a tocar algo que el plan no declara, se abre `analisis-2.md`, que trata solo lo que falló y sus implicaciones sobre lo ya hecho. El hallazgo que no obliga a eso no abre análisis: se anota con su pendiente donde pertenece y el plan continúa.

---

## Recomendaciones

Se leyeron las [recomendaciones de Cimiento](../../../../../plantillas/recomendaciones-del-analisis.md); el proyecto no tiene `analisis/recomendaciones.md` propio.

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-1 | «Dónde más puede pasar» revisa los 24 momentos de los enganches de Claude Code, las revisiones de los 4 enganches de git, el instalador, el checklist y los proyectos que heredan |
| R-2 | Se reutiliza lo que ya existe: el modelo `Suspension`, la pantalla de suspensiones y la lectura del freno en `niveles.py` |
| R-19 | El plan de cada fase declara todos sus archivos |
| Las demás | No aplican: no se cambia ninguna regla (R-3, R-4) y no hay piloto (R-16) |

---

## Hallazgo

### Hallazgo 1 del proyecto scilit, 2026-10-08 · Los enganches no se pueden suspender desde Cimiento, salvo el freno

**Los enganches no se pueden suspender desde Cimiento, salvo el freno.** El usuario decidió cuatro cosas: se suspende un momento concreto de cada enganche; todos se pueden suspender, con la recomendación de no hacerlo y el motivo; se consulta la base una sola vez por mensaje; y las revisiones de git entran en la misma pantalla. Se corrige en el estándar, no en scilit.

## Pendiente

**De dónde sale:** proyecto scilit, hallazgo 1 del resumen del 2026-10-08; allá lo sigue su pendiente 037.

**El problema.** Desde Cimiento se puede suspender una regla en un proyecto, pero de los enganches solo el freno. Los demás no tienen cómo apagarse, y en git la única salida es `--no-verify`, que salta todas las revisiones y no deja rastro. Quitar el enganche de `.claude/settings.json` no sirve: el checklist lo echa de menos. Decisiones del usuario: (1) se suspende un momento concreto, no el guion; (2) todos se pueden suspender, el histórico incluido, con la recomendación y el motivo, y `NO_SE_SUSPENDEN` desaparece; el freno sigue deteniendo lo que viole el núcleo; (3) una sola consulta a la base por mensaje: el primer enganche trae la lista y la deja para los demás; (4) las revisiones de git entran en la misma pantalla, cada una por separado, y git consulta la base una vez por guardado.

**Por qué importa.** Un enganche que estorba no se puede apagar sin que el checklist marque la instalación como incompleta, y en git saltar una revisión las salta todas sin registro.

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 23 · Usuario, 2026-10-09 10:39:15
> Analicemos: el pendiente 149

**Agente**, 2026-10-09 10:42:45
<!-- agente: 4d8f3b9c-40a3-499c-8c83-acbdc0956c0f -->

Reviso el código que toca el pendiente 149: la lista de enganches, las suspensiones y las revisiones de git.

Ahora las revisiones de git.

Ya tengo lo necesario. Escribo el análisis.

Corrijo tres números del análisis con lo que se acaba de contar: son 24 momentos (no 25), 8 enganches por mensaje (no 9) y cuatro guiones que se repiten (no seis).

Hay una decisión que cambia lo que se acordó en scilit: **¿Cimiento deja la lista de lo suspendido en un archivo del proyecto, en vez de que los enganches consulten la base?** Recomiendo el archivo.

El análisis quedó escrito en [analisis-1.md](../../../../../historico-chat/resumenes/2026-10-08/pendientes/149-cada-enganche-se-puede-suspender-desde-cimiento/analisis-1.md). Las cuatro decisiones de scilit se mantienen, pero la tercera no se puede cumplir tal como quedó escrita. Decía que el primer enganche consulta la base y les deja la lista a los demás. Sin embargo, los 8 enganches de cada mensaje corren al mismo tiempo, así que no hay un «primero».

- **Archivo (recomendado):** cada vez que se suspende algo o se levanta una suspensión, Cimiento escribe un archivo corto en el proyecto con lo suspendido y hasta cuándo. Los enganches y git lo leen al arrancar. Así no se consulta la base ni una vez por mensaje, y leer el archivo es más rápido.
- **Base:** cada enganche consulta la base al arrancar. Serían 8 consultas al mismo tiempo en cada mensaje, y eso suma demora (pendiente 143).

El trabajo va en la EP-025·HU-032 y se divide en tres fases, una por módulo:

1. **Nombres y pantalla:** un nombre para cada uno de los 24 momentos de los enganches y para cada revisión de git, con su recomendación, en la pantalla de suspensiones.
2. **Enganches de Claude Code:** salen sin hacer nada si están suspendidos.
3. **Revisiones de git:** hacen lo mismo.

### 24 · Usuario, 2026-10-09 10:44:05
> respondo: no entiendo

**Agente**, 2026-10-09 10:44:18
<!-- agente: 672463c8-2d4d-42b0-a6b8-b04c7ad36671 -->

Primero, qué es un enganche: es un programa pequeño que corre solo cada vez que llega un mensaje. Por ejemplo, el que guarda la conversación o el que recuerda las reglas. Con cada mensaje arrancan 8 de ellos al mismo tiempo.

Lo que se quiere es poder apagar cualquiera de esos programas durante un tiempo, desde la pantalla de Cimiento. Para eso, cada uno tiene que averiguar al arrancar si está apagado.

Funciona como 8 trabajadores que llegan juntos a la oficina y tienen que saber si hoy les toca descansar:

- **Opción 1, la base de datos:** cada trabajador llama a la oficina central para preguntar. Son 8 llamadas al mismo tiempo, y cada llamada se demora.
- **Opción 2, el archivo (la que recomiendo):** cada vez que alguien da un descanso o lo quita, Cimiento pega una nota en la puerta. Los trabajadores solo leen la nota al entrar, sin llamar a nadie, y eso es más rápido.

En la sesión de scilit se había acordado que el primer trabajador llamara y les pasara la respuesta a los demás. Eso no se puede hacer, porque los 8 llegan al mismo tiempo y ninguno es el primero.

**¿Se hace con la nota en la puerta, es decir, con el archivo?**

### 25 · Usuario, 2026-10-09 10:47:21
> respondo el que primero llegue le cuenta a los otros

**Agente**, 2026-10-09 10:48:06
<!-- agente: 3564da3f-bfc9-4e21-9608-9c8e40171269 -->

Entendido. Se hace como lo dijo: el primero que llegue les cuenta a los demás. Aunque los 8 lleguen al mismo tiempo, se puede lograr que uno solo gane el turno.

- El primero que logra crear un archivo de turno es el que consulta la base. Crear ese archivo es una operación que solo uno puede ganar, aunque lleguen a la vez.
- Cuando tiene la respuesta, la escribe para los demás.
- Los otros 7 esperan un momento (como máximo 2 segundos) y leen esa respuesta. No llaman a la base.
- Ese turno vale para todo el mensaje. En git, la primera revisión de cada guardado hace lo mismo para las demás.

Lo anoto en el análisis.

Quedó anotado en el análisis. Los cinco acuerdos son:

1. Se apaga un momento concreto de un enganche, cada uno con su nombre.
2. Todos se pueden apagar, también el histórico. Junto a cada uno se muestra la recomendación y su motivo.
3. El primero que llega consulta la base y les cuenta a los demás.
4. Las revisiones de git funcionan igual y van en la misma pantalla.
5. El trabajo va en la EP-025·HU-032, en tres fases.

No queda ninguna decisión pendiente. **Escriba «Apruebo el análisis»**, y con eso construyo las tres fases.

### 26 · Usuario, 2026-10-09 10:53:45
> Apruebo el análisis

**Agente**, 2026-10-09 10:54:37
<!-- agente: 649c4874-9120-469e-a8a1-fa1d3f008680 -->

La aprobación no quedó registrada. El programa que la revisa lee el turno entre paréntesis de cada acuerdo, y yo escribí «decisión 1 de scilit», que leyó como si fuera el turno 1. Corrijo las citas.

Los cinco acuerdos ya citan turnos que existen en la conversación (23 a 25). **Escriba otra vez «Apruebo el análisis»**: la vez anterior no quedó registrada, por un error mío en las citas.

### 27 · Usuario, 2026-10-09 10:55:06
> Apruebo el análisis

**Agente**, 2026-10-09 11:15:45
<!-- agente: 4c0769ba-b7f9-4b5f-8bbf-26d1d42c52b0 -->

Aprobado. Antes de escribir la HU, leo cómo se crean hoy las suspensiones: el catálogo de ajustes, la vista y la pantalla.

Ya sé cómo encaja todo. Primero registro la lección y escribo la HU-032 con sus tres fases.

Escribo los planes de las tres fases. Antes busco qué pruebas existentes tocan las suspensiones, porque alguna puede afirmar que el histórico no se suspende.

Las pruebas actuales afirman que el histórico no se puede suspender. Eso cambia por decisión del usuario, así que entran en el plan de la fase A. Escribo los tres planes.

La consola cortó el guion por las comillas. Lo guardo como archivo en `historico-chat/scripts/2026-10-09/` y lo corro desde ahí.

Escribo los seis documentos directamente, sin guion.

Ahora el código de la fase A, empezando por el catálogo en `enganches.py`.

Ahora el formulario: un enganche sin nombre sigue siendo el freno, como hasta hoy.

Actualizo las dos pruebas que afirmaban lo de antes.

Pasan las 35. Cierro la fase A.

La fase A quedó cerrada. Sigo con la fase B: que cada enganche sepa si está suspendido. Primero miro cómo arranca cada adaptador.

Agrego un cierre a una carrera posible: después de ganar el turno, se vuelve a leer la lista por si otro ya la dejó.

Los 18 adaptadores tienen un solo `main()`. Reviso qué viene justo después, para no romper un docstring al insertar la línea.

Esto ya corre en esta misma sesión, así que un error tumbaría los enganches. Hago que cualquier falla al revisar deje correr el enganche normalmente.

En la última prueba usé el nombre equivocado: `hook_relacionadas` después de escribir se llama `reglas-relacionadas`. Lo corrijo y corro las pruebas.

Pasan las 7. Falta el caso CP-005: que solo «freno» apague el freno entero. Lo agrego simulando la lectura de la base.

Pasan las 9 y las 17 del freno. Cierro la fase B.

Escribo los planes de la fase C.

Ahora el código de la fase C.

Ya nada usa `NO_SE_SUSPENDEN`. Corrijo también la descripción al comienzo del catálogo, que seguía diciendo que hay enganches que no se pueden suspender.

Pasan las 26. Compruebo con la base real que una revisión de git sin suspender sigue corriendo como siempre.

Encontré un problema que el plan aprobado no cubre, así que me detengo aquí. **Para seguir, escriba «Analicemos: el pendiente 149»**, que abre el análisis 2 de ese pendiente.

**Qué pasó.** Las listas de lo suspendido se guardan en la carpeta `.agente/`. En los proyectos que heredan el estándar, git ignora esa carpeta porque el instalador la agrega a `.gitignore`. Pero en este repositorio, el del estándar, no está ignorada: solo lo está `proyectos/*/.agente/`. Por eso:

- el freno detiene cualquier orden de consola que corra una revisión de git, porque la revisión deja su lista en `.agente/` y el freno lo ve como un archivo que el plan no declara;
- `git status` muestra `.agente/` como carpeta nueva, y un `git add` de todo la subiría.

**Lo que propondría en el análisis:** agregar `.agente/` al `.gitignore` de este repositorio, igual que ya lo tienen los proyectos que heredan. Es un cambio de una línea, pero toca un archivo que el plan no declara, y por eso necesita su análisis.

**Cómo va el pendiente 149:**

- **Fase A, catálogo y pantalla:** cerrada.
- **Fase B, los enganches:** cerrada. Ya funciona en esta sesión.
- **Fase C, revisiones de git:** el código está hecho y sus 26 pruebas pasan, pero queda sin cerrar hasta resolver esto.

> acá termina la conversación

---

## Lo acordado

1. Momentos: se suspende un momento concreto de un enganche, no el guion entero; cada entrada de `HOOKS_CLAUDE` lleva un nombre fijo. Viene de la sesión de scilit del 2026-10-08 (turno 23).
2. Todos se pueden suspender, el histórico incluido; la pantalla muestra junto a cada uno la recomendación de no suspenderlo y el motivo; `NO_SE_SUSPENDEN` desaparece; el freno sigue deteniendo lo que viole el núcleo aunque esté suspendido. Viene de la sesión de scilit (turno 23).
3. Una sola consulta a la base por mensaje: el primero que llega le cuenta a los otros. Como los enganches de un evento arrancan a la vez, el primero es el que gana el turno creando un archivo que solo uno puede crear; ese consulta la base y deja la lista; los demás esperan hasta 2 segundos y la leen. La lista vale hasta el mensaje siguiente. Si la espera se cumple sin lista, el enganche corre como si nada estuviera suspendido, y el freno se comporta como hoy sin base (turnos 24 y 25).
4. Git: las revisiones entran en la misma pantalla, cada una por separado, con motivo, vencimiento y recomendación; en cada guardado, la primera revisión consulta la base y les cuenta a las demás de la misma forma. Viene de la sesión de scilit (turnos 23 y 25).
5. La épica: se construye como EP-025·HU-032, en tres fases, una por módulo (turno 25).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `00·N10` y el núcleo: el freno sigue deteniendo lo que viole el núcleo aunque esté suspendido (decisión 2). `00·N6`: el histórico tapa las claves antes de guardar; suspenderlo deja de guardar, no guarda sin tapar. `02·F30`: suspender se deshace levantando la suspensión. `02·F11`: el trabajo toca tres módulos y va en una fase por módulo. No choca ninguna.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| El catálogo | `HOOKS_CLAUDE` (`core/comun/enganches.py:21`): 24 momentos, cada uno `(evento, filtro, guion, mensaje, argumentos)`, sin nombre propio. Cuatro guiones corren en dos momentos: `hook_historico`, `hook_resumen`, `hook_presupuesto` y `hook_recuerdos` |
| Lo que no se suspende | `NO_SE_SUSPENDEN = ("hook_historico.py",)` (`enganches.py:113`), que usan `ajustes.py` e `instalar.py` |
| La suspensión | El modelo `Suspension` (`core/proyectos/models.py:118`) guarda tipo, nombre, motivo, vencimiento (hasta 30 días), quién la creó y quién la levantó. `ajustes.py` acepta el tipo `enganche` solo con el valor `freno` |
| Quién la lee | Solo el freno, con PyMySQL y sin Django (`core/enganches/niveles.py`): una conexión y una consulta por acción |
| Los enganches en un mismo evento | **Corren a la vez** (comentario de `enganches.py:33`, H-9 de la sesión del 2026-10-01). En cada mensaje corren 8 de `UserPromptSubmit` juntos: no hay un «primero» que traiga la lista y la deje a los demás |
| Las revisiones de git | 13 llamadas a `validar.py` en los 4 enganches de `.githooks/` (`commit`, `versionado`, `marcas`, `plan`, `sesiones`, `pruebas`, `internas`, `metareglas` y otras), escritas por `instalar.py` desde sus plantillas |
| La demora | El pendiente 143 midió que los enganches ya demoran cada respuesta; abrir una conexión a la base desde 8 enganches a la vez lo empeora |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| H-9 de la sesión del 2026-10-01 | Contradice la decisión 3 tal como está: los enganches del mismo evento no corren uno tras otro |
| Análisis 1 del pendiente 116 | Arrancar Django tarda 2,4 s: por eso el freno lee con PyMySQL. Leer un archivo es más rápido que cualquier conexión |
| Pendiente 143 | Cada cosa que se suma a los enganches demora la respuesta |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | MENOR (`20·M10`): el instalador vuelve a escribir los enganches con el nombre de cada momento; no les pide nada. `02·F22` aplica: la reinstalación lo lleva a cada proyecto |
| Normas y leyes | Ninguna |
| Herramientas | Claude Code corre a la vez los enganches de un evento. Git corre sus enganches sin Django y puede correr fuera de una sesión del agente |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Un guion en dos momentos | `hook_historico`, `hook_resumen`, `hook_presupuesto`, `hook_recuerdos` | Suspender uno apaga el otro | Decisión 1: cada momento con su nombre |
| El histórico suspendido | Cualquier proyecto | Se deja de guardar la conversación | Decisión 2: la pantalla muestra la recomendación y el motivo |
| El freno suspendido | Cualquier proyecto | Pasa lo que viola el núcleo | Decisión 2: el núcleo sigue frenando, como hoy |
| La suspensión que vence | Cualquier proyecto | Que el enganche siga apagado | La lectura compara el vencimiento con la hora, en cada uso |
| La suspensión hecha por otro camino | El administrador de Django, un comando | Que el enganche no se entere | La copia se escribe al guardar el modelo, se haga desde donde se haga |
| Git fuera de una sesión | Un commit desde la consola | No saber qué está suspendido | Git lee lo mismo que los enganches |
| `--no-verify` | Git | Sigue saltando todo | No se puede quitar: es de git. La pantalla da la salida con registro |

---

## Propuesta final: hallazgo y pendiente, épica y HU

El hallazgo y el pendiente 149 quedan como están.

### Cómo se cumple la decisión 3

Se propusieron dos caminos: que Cimiento escribiera la lista en un archivo del proyecto al cambiar una suspensión, o que cada enganche consultara la base. El usuario decidió el suyo (acuerdo 3): el primero que llega consulta y les cuenta a los otros, ganando el turno con un archivo que solo uno puede crear.

### Épica y HU que salen del análisis

Se suma a la [EP-025: Cimiento se administra y muestra el gasto de tokens](../../../../../documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md), donde nació la suspensión (HU-013). Una HU con tres fases, una por módulo (`02·F11`):

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | 032 | Cada momento de cada enganche y cada revisión de git se puede suspender desde Cimiento | Solo el freno se puede suspender, y en git solo existe `--no-verify` | Ninguna | Es la única | 1, 2, 3 |

Las fases: **A**, el catálogo con un nombre por momento y por revisión, su recomendación y su motivo, y la pantalla (`core/comun`, `core/proyectos`); **B**, los enganches leen la copia y salen sin hacer nada si están suspendidos (`adaptadores/claude-code`, `core/enganches`); **C**, las revisiones de git (`core/herramientas/instalar.py` y sus plantillas, `validar.py`).

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Antes de repartir trabajo entre enganches, mirar si corren uno tras otro o a la vez | Falló | S-365 | No aplica |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Cada momento de `HOOKS_CLAUDE` y cada revisión de git lleva un nombre fijo, una recomendación y su motivo; `NO_SE_SUSPENDEN` desaparece; la pantalla de suspensiones deja suspender cualquiera, con motivo y vencimiento, y muestra la recomendación; el instalador y el checklist usan el nombre; con pruebas | 1, 2, 4, 5 | EP-025·HU-032 |
| 2 | Al arrancar, cada enganche sabe si su momento está suspendido: el primero que gana el turno del mensaje consulta la base y deja la lista; los demás esperan hasta 2 segundos y la leen; el suspendido sale sin hacer nada; el freno sigue deteniendo lo que viole el núcleo; con pruebas que lancen varios a la vez y cuenten una sola consulta | 2, 3, 5 | EP-025·HU-032 |
| 3 | Cada revisión de git sabe si está suspendida, con una sola consulta por guardado de la misma forma, y si lo está no detiene el guardado y lo dice; con pruebas | 3, 4, 5 | EP-025·HU-032 |

## Lo que aporta al análisis principal

**Resultado:** amplía.

**Lo que suma al análisis principal:** Todo enganche y toda revisión de git se puede apagar un tiempo desde Cimiento, con motivo y vencimiento, sin dejar la instalación incompleta.
