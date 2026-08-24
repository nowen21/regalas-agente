# Análisis de requisitos: ¿qué debe hacer el sistema?   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **qué** tiene que hacer el sistema, sin decir todavía cómo. Confundir las dos cosas acá es el error caro del ciclo: un requisito escrito como solución cierra opciones antes de haberlas mirado.

> Plantilla. Se llena durante la etapa y se cierra al pasar a la siguiente. La envergadura ajusta la profundidad, nunca la existencia: la sección sin materia se llena con `N/A porque «…»`, nunca se borra. Reemplaza los `«…»` y borra esta caja.

> **Cómo se redacta lo que va dentro de cada `«…»`.** En el idioma del proyecto ([`01·C8`](«RUTA-ESTANDAR»/base/01-conducta.md#c8--habla-el-idioma-del-proyecto)) y en la menor cantidad de palabras con la que se entienda ([`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md)): el dato primero, sin repaso, sin justificación que nadie pidió y sin paso a paso. Lo que no cabe se escribe en su documento y se enlaza.

**Estado: «BORRADOR / APROBADO»** («AAAA-MM-DD», aprobado por «quién»).

---

## 1. Qué entra a esta etapa

> **Lo que la etapa recibe ya aprobado.** Si algo llega sin aprobar, esta etapa no arranca: se trabaja sobre un acuerdo que puede cambiar.

| Qué se recibe | De dónde viene | ¿Aprobado? |
|---|---|---|
| El problema, el alcance y los objetivos | Planificación | «Sí / No, y qué falta» |
| Las restricciones y los supuestos | Planificación | «…» |

## 2. Los requisitos funcionales

> **Un requisito funcional es algo que el sistema debe hacer**, dicho como resultado y no como pantalla ni como tabla. Se escribe en la voz de quien lo necesita.

| # | Qué debe hacer el sistema | Quién lo necesita | ¿De qué objetivo sale? | Prioridad |
|---|---|---|---|---|
| 1 | «…» | «…» | «Objetivo N de planificación» | «Obligatorio / Complementario / Futuro» |
| 2 | «…» | «…» | «…» | «…» |

> El alcance completo ítem por ítem no cabe acá: va al inventario, [plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md](../../ciclo-vida-proyectos/02-inventario-funcionalidades.md), que es la ficha de cada funcionalidad. Esta tabla es el resumen que se acuerda; aquella es el detalle que se construye.

## 3. Los requisitos no funcionales

> **Un requisito no funcional es una exigencia sobre cómo se comporta el sistema**, no sobre qué hace. Es el que nadie escribe y todos reclaman cuando falta. Se escribe con número: «rápido» no es un requisito, «responde en menos de dos segundos con cien usuarios» sí.

| Frente | Exigencia | Cómo se comprueba |
|---|---|---|
| Rendimiento | «…» | «…» |
| Disponibilidad | «…» | «…» |
| Seguridad y acceso | «…» | «…» |
| Datos personales y normativa | «…» | «…» |
| Usabilidad y accesibilidad | «…» | «…» |
| Compatibilidad | «…» | «…» |

## 4. Las reglas del negocio

> **Una regla del negocio manda sobre el sistema y sobre todo lo demás:** existe aunque el sistema no exista. No se inventa acá, se recoge de quien la dicta, y se escribe con su origen para poder discutirla después.

| # | Regla | Quién la dicta | Qué pasa si se rompe |
|---|---|---|---|
| 1 | «…» | «…» | «…» |

## 5. Los actores y sus permisos

| Actor | Qué hace en el sistema | Qué no puede hacer |
|---|---|---|
| «…» | «…» | «…» |

## 6. El glosario del proyecto

> **Cada término del negocio, con una sola definición.** Dos palabras para la misma cosa cuestan una migración; una palabra para dos cosas cuesta un error de datos.

| Término | Qué significa acá | Cómo NO se llama |
|---|---|---|
| «…» | «…» | «…» |

## 7. Lo que se preguntó y no tiene respuesta

> Una duda escrita detiene un supuesto inventado. Cada una con quién la responde y para cuándo se necesita.

| # | Duda | Quién responde | Se necesita antes de | Estado |
|---|---|---|---|---|
| 1 | «…» | «…» | «…» | «Abierta / Resuelta» |

## 8. Los entregables de esta etapa, y a quién van

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Inventario de funcionalidades | [plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md](../../ciclo-vida-proyectos/02-inventario-funcionalidades.md) | Cliente, se aprueba | «…» |
| Épicas | [plantillas/ciclo-vida-proyectos/03-epica.md](../../ciclo-vida-proyectos/03-epica.md) | Equipo | «…» |
| Historias de usuario con criterios | [plantillas/ciclo-vida-proyectos/04-HU.md](../../ciclo-vida-proyectos/04-HU.md) | Cliente, se aprueba una por una | «…» |
| Requisitos no funcionales | Sección 3 de este documento | Cliente y equipo | «…» |
| Glosario | Sección 6 de este documento | Ambos | «…» |

## 9. Las puertas de esta etapa

| Qué no se puede hacer | Hasta que | Regla |
|---|---|---|
| Derivar épicas | el inventario esté aprobado por el usuario | [`02·F26`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md) |
| Pasar a diseño | cada historia tenga criterios de aceptación verificables | «…» |

## 10. La decisión de cierre

**«Se pasa a diseño / No se pasa»**, decidido por «quién» el «AAAA-MM-DD».

«Qué quedó fuera de esta etapa a propósito, y qué duda de la sección 7 sigue abierta con su riesgo.»
