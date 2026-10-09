# Análisis 3: llenar un análisis se hace con un guion suelto en vez de un comando de Cimiento

> **Aprobado** por el usuario el 2026-10-09, en el turno 52, con la versión 56.8.0. Desde ese momento este análisis no se reescribe.

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Un análisis aprobado no se reescribe. Si al ejecutar el plan aparece un hallazgo que obliga a tocar algo que el plan no declara, se abre `analisis-4.md`, que trata solo lo que falló y sus implicaciones sobre lo ya hecho. El hallazgo que no obliga a eso no abre análisis: se anota con su pendiente donde pertenece y el plan continúa.

---

## Recomendaciones

Se leyeron las [recomendaciones de Cimiento](../../../../../plantillas/recomendaciones-del-analisis.md); el proyecto no tiene `analisis/recomendaciones.md` propio.

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-1 | Se revisan todos los análisis de todos los proyectos, no solo los del 133 |
| R-2 | Ya existe la EP-030·HU-003, sin empezar, que pasa los pendientes y los análisis a la base |
| R-12 | Lo que se construya sirve a cualquier análisis de cualquier proyecto |
| Las demás | Se aplican al escribir lo acordado |

---

## Hallazgo

### H-7 · Llenar un análisis sigue siendo un guion suelto

- **Qué pasó.** Para llenar las secciones del análisis 1 del pendiente 133 se escribió `historico-chat/scripts/2026-10-09/llenar_analisis_133.py`. El freno avisó que se parece a `historico-chat/scripts/2026-10-05/llenar_analisis_124.py`.
- **Por qué importa.** Según `04·S18`, lo que se repite va como funcionalidad de Cimiento, no como otro guion. Es el mismo caso del pendiente 147, pero para los análisis en vez de las fases.
- **Dónde queda.** Sin pendiente todavía. Lo decide el usuario.

## Pendiente

| | |
|---|---|
| **De dónde sale** | [Hallazgo V2 de H-1 · Las reglas llegan repetidas en cada mensaje y no llegan cuando se actúa](../../reglas-de-cada-turno-sin-tokens.md), según el [análisis 1](analisis-1.md), en el resumen de la sesión del 2026-10-05, y [hallazgo V2 de H-6 · Partir `cambiar-codigo` se hace por temas](../../../2026-10-09/sesion-2.md), según el [análisis 2](analisis-2.md), en el resumen de la sesión 2 del 2026-10-09 |

## El problema

Las reglas se eligen solo por la palabra clave del mensaje. Lo que de verdad dice qué reglas rigen es la acción, y antes de ella no llega nada: [base/tareas.md](../../../../../base/tareas.md) lo describe, pero ningún enganche lo hace. Por eso `cambiar-codigo`, `tocar-datos`, `ir-afuera` y `cambiar-estandar`, que no tienen palabra clave, no entregan sus reglas en ningún momento. Mientras tanto, con cada mensaje llegan las mismas listas, y seis reglas llegan dos veces. Y las reglas de código llegan todas, sin importar qué archivo se escribe.

## Por qué importa

El agente trabaja sin las reglas de lo que está haciendo, recibe reglas que no aplican a lo que hace, y cada mensaje de todos los proyectos paga reglas que no usa.

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 48 · Usuario, 2026-10-09 13:33:08
> Analicemos: el pendiente 133

**Agente**, 2026-10-09 13:34:20
<!-- agente: 7a26dacf-17b7-4de1-b982-ed9105387dc6 -->

El análisis 3 quedó abierto, con el encabezado lleno: [analisis-3.md](../../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-3.md).

**Lo que encontré:** en `historico-chat/scripts/` hay **49 programas sueltos** que llenan análisis. Casi todos hacen una de dos cosas:
- **Llenar el encabezado.** Copiar el pendiente y el hallazgo, y poner las rutas. Es un trabajo mecánico: siempre se hace igual.
- **Llenar una sección.** Lo acordado, las lecciones o lo que se tiene que hacer. El texto lo escribe el agente; el programa solo lo pone en su lugar.

**Propuesta:**
1. Cuando se escribe «Analicemos: el pendiente N», Cimiento llena solo el encabezado.
2. Un comando fijo para poner el texto de cada sección: `manage.py analisis seccion «análisis» «sección» --archivo texto.md`.

Con eso no vuelve a hacer falta un programa suelto para llenar un análisis. Cuando la EP-030·HU-003 pase los análisis a la base, el comando seguirá siendo el mismo y solo cambiará dónde guarda.

¿Se acepta la propuesta, o se cambia algo?

### 49 · Usuario, 2026-10-09 13:38:41
> Explique aplicando las reglas 00·ID7 y 00·ID9, de modo que la explicación cumpla con lo establecido en ambas.

**Agente**, 2026-10-09 13:38:47
<!-- agente: b9bc1c15-b826-4b93-ac8b-88443953cd34 -->

Hoy, cada vez que hay que llenar un análisis, el agente escribe un programa nuevo solo para eso. Ya van 49.

La propuesta es que Cimiento haga ese trabajo:

1. **La parte que siempre es igual la hace Cimiento solo.** Apenas se escribe «Analicemos: el pendiente N», copia el pendiente y el hallazgo dentro del análisis.
2. **La parte que cambia la escribe el agente y Cimiento la pone en su lugar.** Lo acordado o lo que falta por hacer lo redacta el agente, y lo guarda en el análisis con un comando fijo de Cimiento, sin programas nuevos.

Así no vuelven a aparecer programas sueltos.

¿Se acepta?

### 50 · Usuario, 2026-10-09 13:39:26
> apruebo

**Agente**, 2026-10-09 13:43:16
<!-- agente: 590012d6-6a4f-49fe-aa12-153c83144e08 -->

Anoto el acuerdo y completo el análisis 3 con ediciones directas, sin escribir otro programa suelto.

Ahora paso el pendiente a su versión 4 y el hallazgo a su versión 2, que es lo que pide la aprobación.

El acuerdo quedó anotado y el [análisis 3](../../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-3.md) está completo. El pendiente ya pasó a su versión 4, así que la aprobación puede quedar registrada en este mismo paso.

Cuando se apruebe, construyo la HU-033 de la EP-025:
1. Al escribir «Analicemos: el pendiente N», Cimiento llena solo la parte del análisis que siempre es igual.
2. Un comando fijo guarda lo que redacta el agente, sección por sección.

**Lo que se necesita ahora:** escribir «Apruebo el análisis».

### 51 · Usuario, 2026-10-09 13:55:30
> Apruebo el análisis

**Agente**, 2026-10-09 13:55:54
<!-- agente: 9b623211-5d4e-49c9-981c-8aae8b43c147 -->

Falta un detalle: el hallazgo tiene que llevar su número con la forma «H-N». Lo renombro como H-7 en el resumen, en el análisis y en el pendiente.

Listo. El hallazgo ya figura como H-7 en el resumen, en el análisis 3 y en el pendiente.

**Para seguir, hace falta escribir otra vez «Apruebo el análisis».** La aprobación anterior no quedó registrada porque faltaba ese número.

### 52 · Usuario, 2026-10-09 13:57:57
> Apruebo el análisis

**Agente**, 2026-10-09 14:06:00
<!-- agente: 9b45c589-db7e-4b7b-a29d-1912ca23cd91 -->

Aprobado. Construyo la HU-033. Primero leo cómo se crea hoy un análisis al prenderlo.

La HU-033 sigue libre en la EP-025. La escribo.

La épica EP-025 no tenía `README.md`, y la orden anterior creó uno con una sola línea. Lo quito: no estaba antes y no corresponde crearlo.

Escribo el índice de la HU y el plan de su fase A.

Ahora el código: llenar el encabezado al prender y guardar una sección.

Ahora las pruebas de la fase.

Las 5 pruebas pasan. Como cambié `analisis_en_curso.py`, corro también sus pruebas.

Todo en verde. Cierro la fase.

Quedó resuelto. Cimiento ya llena los análisis sin programas sueltos:

- **Al escribir «Analicemos: el pendiente N»,** Cimiento pone solo lo que siempre es igual: las rutas, la copia del pendiente y, en el primer análisis, la copia del hallazgo.
- **Lo que redacta el agente** se guarda con un comando fijo: `manage.py analisis seccion «análisis» "Lo acordado" --archivo texto.md`.

Las pruebas pasan: 18 de 18.

**Lo que falta para cerrar la sesión:**
1. Los dos problemas del freno que siguen sin pendiente: el de los cambios de otra sesión y el de las palabras dentro de un `sed`. Para cada uno hay que decidir si se anota o se descarta.
2. El commit de la HU-033. Todavía no está hecho.

¿Hago el commit?

> acá termina la conversación

---

## Lo acordado

> Se escribe en el mismo turno en que el usuario acepta algo: un punto por cada decisión, con su tema y el turno de la conversación donde se acordó.

1. Llenar un análisis lo hace Cimiento, sin guiones sueltos: al escribir «Analicemos: el pendiente N», Cimiento llena solo la parte que siempre es igual (las rutas y las copias del pendiente y del hallazgo); la parte que cambia la redacta el agente y la guarda con un comando fijo de Cimiento, sección por sección (turno 49).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

> Cada subsección es obligatoria: el validador detiene el cierre si falta una. Lo que aportan el usuario y Claude queda en la conversación y no se repite aquí.

### Cimiento: las reglas que aplican y las que chocan

Aplican `04·S18` (lo que se repite va como funcionalidad de Cimiento), `13·DOC24` (el análisis cierra en su mismo archivo) y `13·DOC26` (el pendiente pasa a su versión siguiente). No choca ninguna.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| Los guiones que llenan análisis | 49 en `historico-chat/scripts/`; casi todos llenan el encabezado o una sección |
| Crear el análisis | `AnalisisEnCurso.nuevo_analisis` (`core/enganches/analisis_en_curso.py`) lo copia de `plantillas/analisis.md` al prender, sin llenar nada |
| Leer un análisis | `LectorDeAnalisis` ya lo parte por secciones |
| Los análisis en la base | La EP-030·HU-003 los pasa a la base; está sin empezar |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Pendiente 147 | El mismo problema para cerrar las fases: `cerrar_fase` deja huecos que se llenan a mano. Lo trabaja otra sesión; este análisis no lo toca |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | MENOR (`20·M10`): les llega un comando nuevo, que nadie está obligado a usar |
| Normas y leyes | Ninguna |
| Herramientas | Ninguna condición nueva |

### Dónde más puede pasar

> Lo que destapó el hallazgo puede pasar en otros sitios, otros proyectos u otras herramientas. Cada caso dice qué lo cubre: un punto de «Lo que se tiene que hacer», un punto de «Lo acordado» o la razón por la que no hace falta cubrirlo. Ningún caso queda sin esa columna.

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Un pendiente sin hallazgo enlazado | Pendientes viejos | El encabezado no tiene qué copiar | Acuerdo 1: deja ese hueco para el agente |
| La sección no existe en el análisis | Análisis hechos con plantillas viejas | El comando no sabe dónde escribir | Acuerdo 1: el comando falla diciendo qué secciones hay |
| Otros proyectos | Todos los de la base | Siguen con guiones | El comando viaja con Cimiento a todos |

---

## Propuesta final: hallazgo y pendiente V4, épica y HU

### Hallazgo V2. Llenar un análisis lo hace Cimiento, sin guiones sueltos

| Campo | Valor |
|---|---|
| Qué pasó | Para llenar los análisis del pendiente 133 se escribieron guiones sueltos, y ya hay 49 en `historico-chat/scripts/`. Se decidió que Cimiento llene solo la parte que siempre es igual y que la parte que cambia se guarde con un comando fijo |
| Por qué importa | Según `04·S18`, lo que se repite va como funcionalidad de Cimiento; cada guion nuevo gasta trabajo y puede traer un error distinto |

### Pendiente V4. Las reglas llegan cuando se actúa, por temas, y los análisis se llenan sin guiones

| Campo | Valor |
|---|---|
| De dónde sale | Los hallazgos de las versiones anteriores, y el hallazgo V2 de H-7 · Llenar un análisis sigue siendo un guion suelto, del 2026-10-09 |
| El problema | Además de lo de la versión 3: cada análisis se llena con un guion escrito para él |
| Por qué importa | Además de lo de la versión 3: se gasta trabajo repetido y cada guion puede traer su propio error |

### Épica y HU que salen del análisis

Se suma a la [EP-025: Cimiento se administra y muestra el gasto de tokens](../../../../../documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md), donde están los comandos que cierran y reabren las fases.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | HU-033 | Cimiento llena los análisis sin guiones sueltos | Cada análisis se llena con un guion escrito para él | Ninguna | Es la única | 2 y 3 |

## Lecciones aprendidas

> Salen de lo que funcionó, para repetirlo, y de lo que falló, para no repetirlo. Cada una se escribe como señal de tipo `leccion` en la base de señales (`python memoria/memoria.py add --tipo leccion`) y aquí va el número que le da. «Recomendación» dice si la lección complementa una de las [recomendaciones](../../../../../plantillas/recomendaciones-del-analisis.md), crea una nueva o no aplica; antes de crear una se busca si ya existe.

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Contar los guiones que repiten una tarea muestra cuándo vale la pena volverla comando: 49 para llenar análisis | Funcionó | Se escribe al aprobar | Complementa R-2 |

## Lo que se tiene que hacer

> Cada fila se convierte en un criterio de aceptación de una HU, y «Pasó a» dice cuál. Ninguna fila queda sin destino. «Sale de» cita de dónde sale, de una de tres formas: un número es un punto de «Lo acordado» de este análisis, «Análisis N, acuerdo M» es un acuerdo de otro análisis del mismo pendiente, y una regla del estándar, como `13·DOC26`, es lo que la regla exige. Lo que no tenga acuerdo no entra. La fila que se hace «de una y sin fase» nombra las rutas exactas que toca, entre comillas invertidas: mientras el análisis está prendido, el freno deja escribir esas y ninguna otra.
>
> La fila 1 va siempre, salvo en el análisis que origina el pendiente: pasar el pendiente a su versión siguiente, con el hallazgo de este análisis en «De dónde sale».

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Pasar el pendiente a su versión siguiente | `13·DOC26` | Este análisis, de una y sin fase: `historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/pendiente.md` |
| 2 | Al prender un análisis, Cimiento llena solo las rutas del estándar, la copia del pendiente y la copia del hallazgo que nombra su «De dónde sale»; lo que no encuentra queda para el agente | 1 | EP-025·HU-033 |
| 3 | Un comando fijo guarda en un análisis el texto de una sección: `manage.py analisis seccion «análisis» «sección» --archivo texto.md`; si la sección no existe, falla diciendo cuáles hay | 1 | EP-025·HU-033 |

## Lo que aporta al análisis principal

> Todo análisis se anota en el análisis principal de su alcance, aunque no cambie el sistema ([`13·DOC25`](../../../../../base/13-documentacion/reglas/DOC25-reescribe-el-analisis-principal-con-su-lista-de-cambios.md)). Al aprobar, el programa pasa tal cual lo que suma al final de la redacción del principal, y una fila con la fecha, el resultado y el enlace a su «Lista de análisis». Sin esta sección el análisis no se aprueba.

**Resultado:** amplía.

**Lo que suma al análisis principal:** Llenar un análisis lo hace Cimiento: al prenderlo copia solo lo que siempre es igual, y lo que redacta el agente se guarda sección por sección con un comando fijo, sin guiones sueltos.
