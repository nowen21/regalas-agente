# Análisis 2: cómo se reparten las reglas de cambiar código en pruebas, código y configuración

> **Aprobado** por el usuario el 2026-10-09, en el turno 37, con la versión 56.8.0. Desde ese momento este análisis no se reescribe.

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Un análisis aprobado no se reescribe. Si al ejecutar el plan aparece un hallazgo que obliga a tocar algo que el plan no declara, se abre `analisis-3.md`, que trata solo lo que falló y sus implicaciones sobre lo ya hecho. El hallazgo que no obliga a eso no abre análisis: se anota con su pendiente donde pertenece y el plan continúa.

---

## Recomendaciones

Se leyeron las [recomendaciones de Cimiento](../../../../../plantillas/recomendaciones-del-analisis.md); el proyecto no tiene `analisis/recomendaciones.md` propio.

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-1 | Se revisa qué pasa con cada tipo de archivo que se escribe, en cualquier proyecto |
| R-2 | Se parte de la medición: 128 reglas, 67 KB, en 21 capítulos |
| R-6 | Se leyó completo el análisis 1; este trata solo cómo se reparten las reglas (su acuerdo 3) |
| R-10 | Se explica con ejemplos de archivos concretos |
| Las demás | Se aplican al escribir lo acordado |

---

## Hallazgo

### H-6 · Partir `cambiar-codigo` pide decidir cómo se reparten sus reglas

| Campo | Valor |
|---|---|
| Qué pasó | Al llegar a la HU-026, el análisis 1 del pendiente 133 dice que `cambiar-codigo` se parte en pruebas, código y configuración, pero no dice cómo se reparten sus 128 reglas (67 KB, en 21 capítulos). Repartirlas una por una es cambiar la línea `**Aplica a:**` de cada regla, en unos 20 archivos del estándar, cada uno con su propuesta. Repartirlas por capítulo solo cambia `base/tareas.md` |
| Por qué importa | Es una decisión de diseño del estándar que el plan no puede tomar por su cuenta, y cambia cuántas propuestas tiene que aprobar el usuario |
| Pendiente | El mismo 133: se trata en su análisis 2 |

## Pendiente

| | |
|---|---|
| **De dónde sale** | [Hallazgo V2 de H-1 · Las reglas llegan repetidas en cada mensaje y no llegan cuando se actúa](../../reglas-de-cada-turno-sin-tokens.md), según el [análisis 1](analisis-1.md), en el resumen de la sesión del 2026-10-05 |

## El problema

Las reglas se eligen solo por la palabra clave del mensaje. Lo que de verdad dice qué reglas rigen es la acción, y antes de ella no llega nada: [base/tareas.md](../../../../../base/tareas.md) lo describe, pero ningún enganche lo hace. Por eso `cambiar-codigo`, `tocar-datos`, `ir-afuera` y `cambiar-estandar`, que no tienen palabra clave, no entregan sus reglas en ningún momento. Mientras tanto, con cada mensaje llegan las mismas listas, y seis reglas llegan dos veces.

## Por qué importa

El agente trabaja sin las reglas de lo que está haciendo, y cada mensaje de todos los proyectos paga reglas que no usa.

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 32 · Usuario, 2026-10-09 12:14:32
> Analicemos: el pendiente 133

**Agente**, 2026-10-09 12:15:22
<!-- agente: ed30efbd-c7cc-486e-a109-102105da3b1b -->

El análisis 2 quedó abierto, con el encabezado lleno: [analisis-2.md](../../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-2.md).

**El problema.** Cuando el agente toca código le corresponden 128 reglas, y caben unas 15 por entrega. Para recibirlas todas hacen falta unas 10 entregas, aunque la mayoría no aplique a lo que se está haciendo. Por ejemplo, al escribir una prueba también llegan las reglas de despliegue.

**Hay dos formas de repartirlas:**

1. **Por capítulo.** Cada tipo de archivo recibe los capítulos que le tocan:
   - Una prueba (`tests_*.py`, carpeta `tests/`): las reglas generales y el capítulo 08, de pruebas. Unos 17 KB.
   - Un archivo de configuración (`settings`, `.json`, `.yml`, `Dockerfile`): las generales y los capítulos 10, 11 y 18, de dependencias, configuración y despliegue. Unos 20 KB.
   - Cualquier otro código: el resto. Unos 55 KB.

   Solo cambia un archivo del estándar, `base/tareas.md`, así que el usuario aprueba una sola propuesta.
2. **Regla por regla.** Se revisa cada una de las 128 reglas y se marca a cuál de los tres tipos pertenece. Queda más preciso, pero cambia unos 20 archivos del estándar, y cada uno es una propuesta para aprobar.

**Recomendación: la forma 1.** Es más barata, se puede deshacer con una sola propuesta y ya baja mucho lo que llega al escribir pruebas o configuración.

¿Cuál de las dos se aplica?

### 33 · Usuario, 2026-10-09 12:19:38
> respondo Resuma la información aplicando las reglas 00·ID7 y 00·ID9, para que el resumen cumpla con lo establecido en ambas.

**Agente**, 2026-10-09 12:19:44
<!-- agente: 83706f26-de19-40f0-bfe2-22736aa06f0f -->

Cuando el agente toca código le llegan 128 reglas, demasiadas para recibirlas de una vez. Hay dos formas de repartirlas:

1. **Por tipo de archivo.** Al escribir una prueba llegan solo las reglas de pruebas, y al tocar la configuración, solo las de configuración. Para esto se cambia un único archivo del estándar, así que se aprueba una sola propuesta.
2. **Regla por regla.** Queda más preciso, pero se cambian unos 20 archivos y cada uno hay que aprobarlo por separado.

**Recomiendo la 1.** ¿Cuál se aplica?

### 34 · Usuario, 2026-10-09 12:20:41
> analicemos: propongo que se reparta por temas

**Agente**, 2026-10-09 12:21:05
<!-- agente: 85186a7b-6f55-422b-9b2b-4546a0512b3f -->

Entiendo «por temas» así: cada capítulo del estándar es un tema (datos, seguridad, pruebas, interfaz, configuración...), y cada archivo recibe solo los temas que toca. Es más fino que los tres grupos que yo había propuesto.

**Ejemplos**
| Archivo que se escribe | Temas que le llegan |
|---|---|
| `tests_*.py` | pruebas |
| `models.py`, migraciones | datos, privacidad |
| `views.py`, `forms.py` | seguridad, errores |
| plantillas `.html`, `.css` | interfaz |
| `settings`, `.env.example`, `Dockerfile` | configuración, despliegue, dependencias |
| cualquier otro código | calidad, estructura, rendimiento |

Además, todo archivo de código recibe las reglas generales (conducta y flujo de trabajo), una sola vez en la sesión.

**Lo bueno:** cada acción trae poco y casi todo le aplica. Igual que antes, solo cambia `base/tareas.md`, que dice qué archivo pide qué tema, y eso es una sola propuesta para aprobar.

**El riesgo:** un archivo que no encaje en ningún patrón se quedaría sin sus reglas. Para cubrirlo, ese archivo recibe todos los temas de código, como pasa hoy.

¿Lo entendí bien?

### 35 · Usuario, 2026-10-09 12:30:49
> Respondo: si que el agente sepa que si está haciendo esto aplico esta o estas reglas estoy si estoy haciendo esto otro aplico esta regla o estas reglas, etc ...

**Agente**, 2026-10-09 12:32:51
<!-- agente: 9b924255-6662-4e14-9307-eab7a9bfc4d4 -->

La consola no aceptó el bloque, por cómo están las comillas. Lo paso a un guion de apoyo en el repositorio.

Quedó anotado como acuerdo 1 del [análisis 2](../../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-2.md). El análisis está completo y no queda ninguna pregunta abierta.

**Cómo se van a repartir las reglas.** Lo que sigue es la tabla que propongo; se puede corregir antes de aprobar:
- Al escribir una prueba: las reglas de pruebas.
- Al tocar modelos o migraciones: datos y privacidad.
- Al tocar vistas, formularios o rutas: seguridad, errores y rendimiento.
- Al tocar pantallas, estilos o scripts del navegador: interfaz.
- Al tocar configuración o despliegue: configuración, despliegue, dependencias y observabilidad.
- Todo código recibe además las reglas de calidad, estructura y cumplimiento, y las generales.
- Un archivo que no encaje en ninguno de los casos anteriores recibe todas las de código.

**Para seguir, hace falta escribir «Apruebo el análisis».** Con eso paso a construir la HU-026.

### 36 · Usuario, 2026-10-09 12:36:21
> Apruebo el análisis

**Agente**, 2026-10-09 12:37:08
<!-- agente: 6ac1e7e9-4c26-4772-97fb-fafb5b80b6c5 -->

Para aprobar falta un paso: el pendiente tiene que pasar antes a su versión 3, con el hallazgo H-6 en «De dónde sale». Lo hago ahora.

Listo: el pendiente pasó a su versión 3 y el hallazgo H-6 a su versión 2.

**Para seguir, hace falta escribir otra vez «Apruebo el análisis».** La aprobación anterior no quedó registrada porque faltaba ese paso.

### 37 · Usuario, 2026-10-09 12:44:28
> Apruebo el análisis

**Agente**, 2026-10-09 12:52:23
<!-- agente: 4dd41c1c-4015-40be-bed2-cd5637feb4ad -->

Aprobado. Construyo la HU-026. Primero registro la lección y paso la HU a su versión 2, «por temas», mientras el análisis sigue prendido.

La HU-026 quedó en su versión 2. Abro su fase A, la del código, y escribo el plan.

Escribo la tabla de temas sobre el texto de la propuesta 18.

Ahora el código: leer la tabla y elegir los capítulos según la ruta del archivo.

Ahora las pruebas de la HU-026, con la tabla leída de `tareas-con-temas.txt`.

Las 37 pruebas pasan. Mido cuánto llega ahora al escribir una prueba, para el informe, y dejo la tabla propuesta en Cimiento.

Al escribir una prueba ahora llegan 46 reglas (24 KB) en lugar de 128 (67 KB). La tabla quedó como propuesta 19. Cierro la fase A de la HU-026.

La HU-026 quedó hecha y probada. Ahora, al escribir una prueba, llegan 46 reglas (24 KB) en lugar de 128 (67 KB). Esa reducción empieza a regir cuando se aprueben en Cimiento las dos propuestas del estándar.

**Lo que falta, en orden**
1. **Aprobar la propuesta 18** en Cimiento → Estándar → Propuestas. Dice cuándo llegan las reglas.
2. **Aprobar la propuesta 19.** Es la tabla de temas, armada sobre el texto de la 18; por eso va después.
3. **Subir la versión.** Lo hago yo cuando las dos estén aprobadas.
4. **El commit.** Todavía no hay ninguno; se decide aparte.

**Lo que se necesita ahora:** aprobar las propuestas 18 y 19, en ese orden.

> acá termina la conversación

---

## Lo acordado

> Se escribe en el mismo turno en que el usuario acepta algo: un punto por cada decisión, con su tema y el turno de la conversación donde se acordó.

1. Las reglas de cambiar código se reparten por temas: cada capítulo del estándar es un tema, y el agente sabe que si está haciendo una cosa le aplican unas reglas y si está haciendo otra, otras. Cada tipo de archivo recibe solo los temas que toca, según una tabla en `base/tareas.md`; el archivo que no encaja en la tabla recibe todos los temas de código; las reglas generales llegan una vez a todo archivo de código. Reemplaza los tres grupos del acuerdo 3 del análisis 1 (turno 35).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

> Cada subsección es obligatoria: el validador detiene el cierre si falta una. Lo que aportan el usuario y Claude queda en la conversación y no se repite aquí.

### Cimiento: las reglas que aplican y las que chocan

Aplican `02·F28` (el cambio baja en orden: la HU-026 pasa a su versión siguiente), `13·DOC26` (el pendiente pasa a su versión siguiente) y `20·M10` (cambia `base/tareas.md`). No choca ninguna.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| Las reglas de `cambiar-codigo` | 128 reglas, 67 KB, en 21 capítulos. Llegan en unas 10 entregas, todas, sin importar el archivo |
| La entrega por acción | `core/herramientas/entrega_de_reglas.py` (HU-025) elige la tarea con la columna de acciones de `base/tareas.md`; `escribe otro` no distingue tipos de archivo |
| La HU-026 | Dice tres tareas: pruebas, código y configuración. Sin empezar |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Análisis 1 de este pendiente, acuerdo 3 | Partir en tres grupos. El acuerdo 1 de este análisis lo afina: por temas |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | MENOR (`20·M10`): no les pide hacer nada |
| Normas y leyes | Ninguna |
| Herramientas | El enganche de antes de la acción conoce la ruta del archivo que se escribe; con eso se elige el tema |

### Dónde más puede pasar

> Lo que destapó el hallazgo puede pasar en otros sitios, otros proyectos u otras herramientas. Cada caso dice qué lo cubre: un punto de «Lo que se tiene que hacer», un punto de «Lo acordado» o la razón por la que no hace falta cubrirlo. Ningún caso queda sin esa columna.

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Un archivo que no encaja en la tabla | Cualquier proyecto, cualquier lenguaje | Se queda sin sus reglas | Acuerdo 1: recibe todos los temas de código |
| Un archivo que toca varios temas | Una vista que valida y guarda | Le faltan reglas | Acuerdo 1: la tabla le da todos sus temas |
| Otros lenguajes y marcos | Proyectos que no son Django | La tabla no los reconoce | Acuerdo 1: sin patrón, todos los temas |
| Comandos de consola que escriben código | `sed`, `python -c` | No hay ruta clara | No cambia: la acción de consola sigue en `correr-comando` |

---

## Propuesta final: hallazgo y pendiente V3, épica y HU

### Hallazgo V2. Partir `cambiar-codigo` se hace por temas

| Campo | Valor |
|---|---|
| Qué pasó | El análisis 1 dijo partir `cambiar-codigo` en pruebas, código y configuración, sin decir cómo repartir sus 128 reglas. Se decidió repartirlas por temas: cada capítulo es un tema y cada tipo de archivo recibe los suyos |
| Por qué importa | Cada acción sobre código trae solo lo que le aplica, con una sola propuesta del estándar |

### Pendiente V3. Las reglas llegan cuando se actúa, una sola vez, y las de código por temas

| Campo | Valor |
|---|---|
| De dónde sale | El hallazgo V2 de H-1 del 2026-10-05 y el hallazgo V2 de H-6 del 2026-10-09: partir `cambiar-codigo` se hace por temas |
| El problema | Además de lo de la versión 2: las reglas de código llegan todas, sin importar qué archivo se escribe |
| Por qué importa | El agente recibe reglas que no aplican a lo que hace, y tarda unas 10 entregas en tener las que sí |

### Épica y HU que salen del análisis

Sigue en la [EP-005: automatismos que no dependen de que alguien se acuerde](../../../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/epica.md). La [HU-026: las reglas de cambiar código llegan partidas según lo que se toca](../../../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-026-las-reglas-de-cambiar-codigo-llegan-partidas-segun-lo-que-se-toca/HU-026-las-reglas-de-cambiar-codigo-llegan-partidas-segun-lo-que-se-toca.md) pasa a su versión siguiente: por temas en vez de tres grupos.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | HU-026 | Las reglas de cambiar código llegan partidas según lo que se toca | Las reglas de código llegan todas, sin importar el archivo | HU-025 | La HU-025 ya entrega por acción | 3 y 4 |

## Lecciones aprendidas

> Salen de lo que funcionó, para repetirlo, y de lo que falló, para no repetirlo. Cada una se escribe como señal de tipo `leccion` en la base de señales (`python memoria/memoria.py add --tipo leccion`) y aquí va el número que le da. «Recomendación» dice si la lección complementa una de las [recomendaciones](../../../../../plantillas/recomendaciones-del-analisis.md), crea una nueva o no aplica; antes de crear una se busca si ya existe.

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Medir antes de proponer cómo partir: contar reglas y KB por capítulo mostró el tamaño real del problema | Funcionó | Se escribe al aprobar | Complementa R-2 |

## Lo que se tiene que hacer

> Cada fila se convierte en un criterio de aceptación de una HU, y «Pasó a» dice cuál. Ninguna fila queda sin destino. «Sale de» cita de dónde sale, de una de tres formas: un número es un punto de «Lo acordado» de este análisis, «Análisis N, acuerdo M» es un acuerdo de otro análisis del mismo pendiente, y una regla del estándar, como `13·DOC26`, es lo que la regla exige. Lo que no tenga acuerdo no entra. La fila que se hace «de una y sin fase» nombra las rutas exactas que toca, entre comillas invertidas: mientras el análisis está prendido, el freno deja escribir esas y ninguna otra.
>
> La fila 1 va siempre, salvo en el análisis que origina el pendiente: pasar el pendiente a su versión siguiente, con el hallazgo de este análisis en «De dónde sale».

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Pasar el pendiente a su versión siguiente | `13·DOC26` | Este análisis, de una y sin fase: `historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/pendiente.md` |
| 2 | Pasar la HU-026 a su versión siguiente: por temas | `02·F28` | Este análisis, de una y sin fase: `documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-026-las-reglas-de-cambiar-codigo-llegan-partidas-segun-lo-que-se-toca/HU-026-las-reglas-de-cambiar-codigo-llegan-partidas-segun-lo-que-se-toca.md` |
| 3 | `base/tareas.md` trae la tabla de temas: qué capítulos recibe cada tipo de archivo, y que sin patrón recibe todos los de código. Propuesta del agente para la tabla: pruebas (`tests*`, `test_*`, `*.spec.*`) → 08; datos (`models*`, `migrations/`, `*.sql`) → 03, 12, 15; servidor (`views*`, `forms*`, `urls*`, `api*`, `services*`) → 04, 05, 06; interfaz (`*.html`, `*.css`, `*.js`, `*.ts`, `templates/`, `static/`) → 17; configuración (`settings*`, `*.env*`, `*.yml`, `*.toml`, `Dockerfile`, `requirements*`, `package.json`) → 10, 11, 18, 19; procesos (`tasks*`, `jobs*`) → 21; todo código además 07, 14, 16 y las generales 00, 01, 02 | 1 | EP-005·HU-026 |
| 4 | `entrega_de_reglas.py` elige los temas por la ruta del archivo con esa tabla, y entrega solo las reglas de esos capítulos | 1 | EP-005·HU-026 |

## Lo que aporta al análisis principal

> Todo análisis se anota en el análisis principal de su alcance, aunque no cambie el sistema ([`13·DOC25`](../../../../../base/13-documentacion/reglas/DOC25-reescribe-el-analisis-principal-con-su-lista-de-cambios.md)). Al aprobar, el programa pasa tal cual lo que suma al final de la redacción del principal, y una fila con la fecha, el resultado y el enlace a su «Lista de análisis». Sin esta sección el análisis no se aprueba.

**Resultado:** modifica la idea.

**Lo que suma al análisis principal:** Las reglas de código llegan por temas: cada tipo de archivo recibe solo los capítulos que toca, y el que no encaja recibe todos.
