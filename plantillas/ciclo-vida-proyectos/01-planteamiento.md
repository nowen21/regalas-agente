# Planteamiento · «Nombre del módulo / épica»   ·   `[CAPA 3]`

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |

> **Qué es este archivo.** El planteamiento de entrada de un desarrollo: la necesidad y sus restricciones (pasos 0-3 del flujo [`02·F0`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md)). Es el **insumo** del agente, no la especificación ni una orden de entregar código.
>
> **Cómo usarlo.**
> 1. Copiar esta plantilla al proyecto como `prompts/<slug>-planteamiento.md` (un planteamiento por módulo/épica).
> 2. Reemplazar los `«…»` y borrar las secciones que no apliquen.
> 3. Borrar este recuadro, y solo este: el encuadre que va debajo, fuera de la caja, es texto fijo y se conserva. Es lo que le dice al que abra el documento qué está leyendo y qué no lo autoriza a hacer.
>
> **Si el proyecto ya está construido.** El mismo molde sirve, y el documento que sale tiene que ser indistinguible de uno escrito antes de construir. No hay entrevista: la información se levanta del propio repositorio (el README, los pedidos guardados del usuario, la documentación, las notas de diseño y el código). Lo que cambia es que hay que **traducir** lo que se encuentra a lo que se necesita, y ahí es donde se falla:
>
> | Lo que uno encuentra | Lo que va escrito |
> |---|---|
> | «El sistema **es** un cuerpo de reglas versionado» | «**Hace falta** un cuerpo de reglas versionado» |
> | «La revisión da hoy 14 de 14» | «La revisión no deja ningún punto incumplido» |
> | «Ya pasó; señal S-018» | El riesgo contado como riesgo, sin el rastro de que ya ocurrió |
> | «Ya está construido, entonces no se pide» | Lo construido **sí** entra en el alcance: se plantea lo que el proyecto necesita, no lo que le falta |
>
> Las secciones 9 y 10 son la excepción: ahí sí se nombran los documentos y las épicas que existen, porque son trazabilidad y no relato.
>
> **Y reconstruir es también auditar.** Si al escribirlo aparece algo ya construido que no cabe en el alcance de §4 o choca con un no negociable de §7, no se acomoda el documento para que quepa. Se anota como hallazgo y lo decide el usuario. Sin esto, el molde se vuelve una máquina de justificar hacia atrás cualquier cosa que ya esté en el disco.
>
> **Regla de oro.** El cómo y el cuándo que pone el estándar son el alcance, las HU, la especificación, el plan, el orden y la entrega. En cuanto un planteamiento dice "dame el código de X", dejó de ser planteamiento y choca con el flujo ([`02·F2`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md) sin especificación no hay código, [`02·F4`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md) sin plan aprobado no hay código). Por eso un planteamiento no incluye una sección "Formato de respuesta" que pida código completo, ni "Actúa como desarrollador senior..." (la identidad ya está en `00`), ni el orden de implementación, ni la entrega esperada.

**Encuadre para el agente:** este documento es el planteamiento de entrada. Dice qué se necesita y qué no se negocia; el cómo y el cuándo los pone el estándar. La cadena que se recorre es la de [`02·F0`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md), sin saltar eslabones. No generar código hasta que el plan esté **aprobado**.

## 0. Identificación

> Identifica el proyecto, lo que cubre este encargo, la fecha y de dónde salió la información.

| Campo | Valor |
|---|---|
| **Nombre del proyecto** | «Cómo se llama el proyecto. Es el nombre con que lo van a nombrar todos los documentos que salgan de acá, así que se decide una vez y no se cambia sin plan» |
| **Qué cubre este encargo** | «Todo el proyecto, o el módulo o la épica a la que corresponde» |
| **Fecha** | «AAAA-MM-DD» |
| **Cómo se levantó** | «Entrevista, o Reconstruido del proyecto existente. Y de qué salió: el README, los pedidos guardados, la documentación, el código. Es el único lugar del documento donde va la procedencia» |

## 1. Necesidad, en una frase

> Es el problema que motiva el desarrollo, visto desde el negocio.

«Qué quiere resolver el negocio, en lenguaje de negocio, sin detalle técnico.»

## 2. Contexto

> Describe de dónde se parte. Si el punto de partida (un solo usuario, corre en local, etc.) **no** es un límite del diseño, se declara: "esto es el punto de partida, no un tope: no recortar estructura apoyándose en ello".

«Situación actual, problema que se resuelve, quién lo usa hoy, antecedentes.»

## 3. Objetivo y criterio de éxito

> Dice qué se busca lograr y cómo se comprueba que se logró.

- **Objetivo:** «qué se logra cuando esto esté hecho».
- **Criterio de éxito:** «cómo se sabe, de forma medible, que se logró».

## 4. Alcance esperado (acota expectativas)

> Es el borde inicial de lo que se pide, para que el agente no asuma de más. El alcance formal se acuerda después, en la estación `proponer-alcance`.

- **Qué sí se pide:** «capacidades que entran».
- **Qué no se pide / fuera de alcance:** «lo que explícitamente queda afuera».

## 5. Restricciones técnicas (si el proyecto las fija)

> Son las condiciones técnicas que el proyecto impone desde el comienzo.

«Stack obligatorio, motor de BD, versiones, integraciones. Para los datos ya verificados del entorno (versiones, puertos, rutas), remitir a `.agente/stack.md`, no repetirlos aquí para no tener dos versiones que se contradigan.»

## 6. Requerimientos funcionales

> Son las capacidades que se piden, numeradas y una por línea. Si hay un requisito central, se marca.

1. «Requerimiento...»
2. «Requerimiento...  ← REQUISITO CENTRAL» (si aplica)

## 7. Restricciones no negociables

> Son las reglas duras que el diseño debe cumplir sí o sí: seguridad, privacidad, decisiones de arquitectura ya tomadas.

- «Restricción...»

## 8. Casos borde a considerar

> Es lo que el agente debe contemplar aunque no sea el camino feliz.

- «Encoding raro, archivos enormes, permisos, concurrencia, entradas inválidas...»

## 9. Referencias

> Son los documentos que el agente consulta para entender el pedido.

- «Mockups, documentos funcionales, prompts previos, especificaciones de módulos con los que convive.»

## 10. Épicas derivadas

> Son las épicas que salen de este planteamiento, para seguir la trazabilidad hacia abajo. Se completa a medida que el planteamiento se descompone en épicas ([`02·F0`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) paso 4). Normalmente es una; un planteamiento grande puede dar varias. Cada épica apunta de vuelta a este planteamiento (`epica.md §1`).

| Épica | Título | Estado |
|---|---|---|
| EP-«NNN» | «…» | Uno de [los estados del glosario](«RUTA-ESTANDAR»/base/glosario.md#5--en-qué-estado-está-algo) para una épica |
