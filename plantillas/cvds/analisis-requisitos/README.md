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

## 2. De dónde salieron los requisitos

> **Un requisito sin origen no se puede discutir después.** Acá va con quién se habló, cómo y cuándo. Preguntarle solo a los jefes y no a quien va a usar el sistema todos los días es el error que más requisitos falsos produce.

| Fuente | Quién | Técnica | Cuándo | Dónde quedó lo acordado |
|---|---|---|---|---|
| «Usuario que lo usa a diario / cliente / normativa / sistema actual» | «…» | «Entrevista / encuesta / observación en sitio / taller / lectura de documentos / prototipo desechable» | «AAAA-MM-DD» | «…» |

**Quién no se consultó, y por qué:** «…»

## 3. Los requisitos funcionales

> **Un requisito funcional es algo que el sistema debe hacer**, dicho como resultado y no como pantalla ni como tabla. Molde de redacción: **el sistema debe «acción» «objeto» «condición» «criterio medible»**.
>
> Cada uno se comprueba contra ocho preguntas: ¿es **único** (una sola condición)? ¿**completo** (no depende de lo que no está escrito)? ¿**consistente** (no contradice a otro)? ¿**verificable** (existe una prueba que lo demuestra)? ¿**medible** (los números están escritos)? ¿**trazable** (tiene identificador propio)? ¿**factible** (cabe en el tiempo y el dinero)? ¿**necesario** (si se quita, alguien pierde algo real)?
>
> La prioridad usa cuatro grados: **debe** (sin esto el sistema no sirve), **debería** (importante, pero opera sin ello), **podría** (si sobra tiempo), **no será** (excluido de esta versión, y queda escrito para no volver a discutirlo).

| ID | Qué debe hacer el sistema | Quién lo necesita | Origen | Objetivo del que sale | Prioridad |
|---|---|---|---|---|---|
| RF-01 | «…» | «…» | «Fila de la sección 2» | «Objetivo N de planificación» | «Debe / Debería / Podría / No será» |
| RF-02 | «…» | «…» | «…» | «…» | «…» |

> El alcance completo ítem por ítem no cabe acá: va al inventario, [plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md](../../ciclo-vida-proyectos/02-inventario-funcionalidades.md), que es la ficha de cada funcionalidad. Esta tabla es el resumen que se acuerda; aquella es el detalle que se construye.

## 4. Los requisitos no funcionales

> **Un requisito no funcional es una exigencia sobre cómo se comporta el sistema**, no sobre qué hace. Es el que nadie escribe y todos reclaman cuando falta, casi siempre en producción y casi siempre tarde. Se escribe con número: «rápido» no es un requisito, «responde en menos de dos segundos con cien usuarios» sí.

| ID | Frente | Exigencia, con su número | Cómo se comprueba |
|---|---|---|---|
| RNF-01 | Rendimiento | «Tiempo de respuesta y usuarios a la vez» | «…» |
| RNF-02 | Disponibilidad | «Cuánto tiempo operativo, y cuándo se puede parar» | «…» |
| RNF-03 | Seguridad | «Quién entra, cómo se comprueba, qué queda auditado» | «…» |
| RNF-04 | Datos personales y normativa | «…» | «…» |
| RNF-05 | Usabilidad y accesibilidad | «…» | «…» |
| RNF-06 | Escalabilidad | «Cuánto se espera que crezcan datos y usuarios» | «…» |
| RNF-07 | Portabilidad | «Dónde tiene que funcionar» | «…» |
| RNF-08 | Mantenibilidad | «…» | «…» |

## 5. Las reglas del negocio

> **Una regla del negocio manda sobre el sistema y sobre todo lo demás:** existe aunque el sistema no exista. No se inventa acá, se recoge de quien la dicta, y se escribe con su origen para poder discutirla después.

| # | Regla | Quién la dicta | Qué pasa si se rompe |
|---|---|---|---|
| 1 | «…» | «…» | «…» |

## 6. Los actores y sus permisos

| Actor | Qué hace en el sistema | Qué no puede hacer |
|---|---|---|
| «…» | «…» | «…» |

## 7. Los casos de uso

> **Un caso de uso cuenta el camino completo, no el feliz.** Los flujos alternos y de excepción son la mitad del trabajo de la etapa y la mitad que se omite: de ahí salen las validaciones que después nadie programó.

| # | Caso de uso | Actor | Precondición | Qué debe quedar al terminar | Flujos alternos y de error |
|---|---|---|---|---|---|
| CU-01 | «…» | «…» | «…» | «…» | «…» |

**Modelos que se dibujaron para validar lo entendido:** «casos de uso, actividades, entidades del negocio, bocetos de pantalla; cuáles se hicieron y dónde están.»

## 8. La trazabilidad

> **Cada requisito se sigue hasta la prueba que lo demuestra.** La fila que se corta a mitad de camino señala trabajo que nadie va a comprobar, o código que nadie pidió.

| Requisito | Historia que lo ejecuta | Módulo que lo implementa | Caso de prueba que lo demuestra |
|---|---|---|---|
| «RF-01» | «…» | «…» | «…» |

## 9. Lo que se preguntó y no tiene respuesta

> Una duda escrita detiene un supuesto inventado. Cada una con quién la responde y para cuándo se necesita.

| # | Duda | Quién responde | Se necesita antes de | Estado |
|---|---|---|---|---|
| 1 | «…» | «…» | «…» | «Abierta / Resuelta» |

## 10. Cómo se pide un cambio a lo ya acordado

> Cuando esta etapa cierra, lo aprobado queda como **línea base**: el punto contra el cual se mide todo cambio posterior. Sin línea base no hay con qué negociar, y el alcance crece sin que nadie note cuánto costó.

| Quién pide | Por dónde entra | Quién evalúa el impacto | Quién aprueba |
|---|---|---|---|
| «…» | «…» | «…» | «…» |

## 11. Los entregables de esta etapa, y a quién van

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Inventario de funcionalidades | [plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md](../../ciclo-vida-proyectos/02-inventario-funcionalidades.md) | Cliente, se aprueba | «…» |
| Épicas | [plantillas/ciclo-vida-proyectos/03-epica.md](../../ciclo-vida-proyectos/03-epica.md) | Equipo | «…» |
| Historias de usuario con criterios | [plantillas/ciclo-vida-proyectos/04-HU.md](../../ciclo-vida-proyectos/04-HU.md) | Cliente, se aprueba una por una | «…» |
| Requisitos no funcionales | Sección 4 de este documento | Cliente y equipo | «…» |
| Casos de uso | Sección 7 de este documento | Cliente y quien prueba | «…» |
| Reglas del negocio | Sección 5 de este documento | Equipo | «…» |
| Trazabilidad | Sección 8 de este documento | Equipo y quien prueba | «…» |
| Glosario del proyecto | «Su documento en el proyecto» | Ambos | «…» |
| Bocetos de pantalla | «…» | Cliente | «…» |

## 12. Las puertas de esta etapa

| Qué no se puede hacer | Hasta que | Regla |
|---|---|---|
| Derivar épicas | el inventario esté aprobado por el usuario | [`02·F26`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md) |
| Pasar a diseño | cada historia tenga criterios de aceptación verificables | «…» |
| Pasar a diseño | ningún requisito quede con palabras sin medida | Sección 3 de este documento |

## 13. La decisión de cierre

**«Se pasa a diseño / No se pasa»**, decidido por «quién» el «AAAA-MM-DD».

**Lo aprobado queda como línea base de requisitos** desde esa fecha: lo que venga después entra por la sección 10.

«Qué quedó fuera de esta etapa a propósito, y qué duda de la sección 9 sigue abierta con su riesgo.»
