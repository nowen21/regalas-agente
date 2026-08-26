# Planteamiento — «Nombre del módulo / épica»   ·   `[CAPA 3]`

> **Qué es este archivo.** El **planteamiento de entrada** de un desarrollo: la necesidad y sus restricciones (pasos 0-3 del flujo [`02·F0`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md)). Es el **insumo** del agente, no la especificación ni una orden de entregar código.
>
> **Cómo usarlo.**
> 1. Copiar esta plantilla al proyecto como `prompts/<slug>-planteamiento.md` (un planteamiento por módulo/épica).
> 2. Reemplazar los `«…»` y borrar las secciones que no apliquen.
> 3. Borrar este recuadro. **Solo este recuadro**: el encuadre que va debajo, fuera de la caja, es texto fijo y se conserva. Es lo que le dice al que abra el documento qué está leyendo y qué no lo autoriza a hacer.
>
> **Si el proyecto ya está construido.** El mismo molde sirve, y el documento que sale tiene que ser indistinguible de uno escrito antes de construir. No hay entrevista: la información se levanta del propio repositorio (el README, los pedidos guardados del usuario, la documentación, las notas de diseño y el código). Lo que cambia es que **hay que traducir lo que se encuentra a lo que se necesita**, y ahí es donde se falla:
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
> **Regla de oro.** El planteamiento responde **QUÉ se necesita y QUÉ no se negocia**. El **CÓMO y el CUÁNDO** (alcance, HU, especificación, plan, orden, entrega) los pone el estándar. En cuanto un planteamiento dice "dame el código de X", dejó de ser planteamiento y choca con el flujo ([`02·F2`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md) sin especificación no hay código, [`02·F4`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md) sin plan aprobado no hay código).

**Encuadre para el agente:** este documento es el planteamiento de entrada. Dice **qué se necesita y qué no se negocia**; el cómo y el cuándo los pone el estándar. La cadena que se recorre es la de [`02·F0`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md), sin saltar eslabones. **No generar código hasta que el plan esté aprobado.**

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Nombre del proyecto** | «Cómo se llama el proyecto. Es el nombre con que lo van a nombrar todos los documentos que salgan de acá, así que se decide una vez y no se cambia sin plan» |
| **Qué cubre este encargo** | «Todo el proyecto, o el módulo o la épica a la que corresponde» |
| **Fecha** | «AAAA-MM-DD» |
| **Cómo se levantó** | «Entrevista, o Reconstruido del proyecto existente. Y de qué salió: el README, los pedidos guardados, la documentación, el código. Es el único lugar del documento donde va la procedencia» |

## 1. Necesidad — en una frase

«Qué quiere resolver el negocio, en lenguaje de negocio, sin detalle técnico.»

## 2. Contexto

«Situación actual, problema que se resuelve, quién lo usa hoy, antecedentes.»

> Si el punto de partida (un solo usuario, corre en local, etc.) **no** es un límite del diseño, decláralo: "esto es el punto de partida, no un tope: no recortar estructura apoyándose en ello".

## 3. Objetivo y criterio de éxito

- **Objetivo:** «qué se logra cuando esto esté hecho».
- **Criterio de éxito:** «cómo se sabe, de forma medible, que se logró».

## 4. Alcance esperado (acota expectativas)

- **Qué SÍ se pide:** «capacidades que entran».
- **Qué NO se pide / fuera de alcance:** «lo que explícitamente queda afuera».

> El alcance **formal** se acuerda en la estación `proponer-alcance`. Esto es solo el borde inicial para que el agente no asuma de más.

## 5. Restricciones técnicas (si el proyecto las fija)

«Stack obligatorio, motor de BD, versiones, integraciones. Para los datos ya verificados del entorno (versiones, puertos, rutas), remitir a `.agente/stack.md`, no repetirlos aquí para no tener dos versiones que se contradigan.»

## 6. Requerimientos funcionales

Numerados. Uno por capacidad. Marcar el central si hay uno.

1. «Requerimiento...»
2. «Requerimiento...  ← REQUISITO CENTRAL» (si aplica)

## 7. Restricciones no negociables

Reglas duras que el diseño debe cumplir sí o sí (seguridad, privacidad, decisiones de arquitectura ya tomadas).

- «Restricción...»

## 8. Casos borde a considerar

Lo que el agente debe contemplar aunque no sea el camino feliz.

- «Encoding raro, archivos enormes, permisos, concurrencia, entradas inválidas...»

## 9. Referencias

- «Mockups, documentos funcionales, prompts previos, especificaciones de módulos con los que convive.»

## 10. Épicas derivadas

> Trazabilidad hacia abajo: se completa **a medida** que el planteamiento se descompone en épicas ([`02·F0`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) paso 4). Normalmente **1**; un planteamiento grande puede dar varias. Cada épica apunta de vuelta a este planteamiento (`epica.md §1`).

| Épica | Título | Estado |
|---|---|---|
| EP-«NNN» | «…» | Uno de [los estados del glosario](«RUTA-ESTANDAR»/base/glosario.md#5--en-qué-estado-está-algo) para una épica |

---

> **No incluir en un planteamiento** (lo pone el estándar, no tú): sección "Formato de respuesta" que pida código completo, "Actúa como desarrollador senior..." (la identidad ya está en `00`), el orden de implementación, la entrega esperada. Si aparece algo de eso, es señal de que el planteamiento se convirtió en orden y va a chocar con el flujo.
