# Reglas del proyecto · «Nombre»   ·   `[CAPA 3 · LOCAL]`

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |

> Catálogo de las reglas propias de este proyecto ([`13·DOC10`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC10-registra-en-el-catalogo-del-proyecto-toda-regla-propia.md)) que sobrescriben o complementan la base común. Cada regla va numerada `P<N>` para poder citarse de forma estable desde especificaciones, planes y señales. Vive en `.agente/reglas-proyecto.md`, que es local y no se versiona porque es configuración del agente. Al llenarlo se reemplazan los `«…»` y se borran esta caja y las notas de cada sección.

## Precedencia (dónde mandan estas reglas)

> Ubica las reglas `P` frente a la base común.

Se aplican en este orden: el núcleo blindado (`00`), las convenciones (`01`-`17`) y estas reglas `P`. Nada queda por encima del núcleo.

Una regla `P` puede endurecer o complementar una convención (`01`-`17`), pero **nunca** contradecir el núcleo (`00`). Ante choque, gana el núcleo.

## Ninguna `P` se sostiene sola  ·  [`20·M16`](«RUTA-ESTANDAR»/base/20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md)

> Exige que cada regla propia se apoye en una regla de la base.

Toda `P` declara, con su enlace, la regla de la base cuyo criterio concreta: la base dice qué hay que decidir y la `P` dice con qué valor se decide en este proyecto.

Si ningún criterio de la base la cubre, la regla no se escribe todavía: primero se crea la regla en el estándar, sin el detalle de este proyecto, y después la `P` la concreta. Sin ese respaldo el catálogo se vuelve un estándar paralelo, sin checklist, sin versión y sin nadie que lo audite.

## Sincronización con la memoria  ·  [`13·DOC10`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC10-registra-en-el-catalogo-del-proyecto-toda-regla-propia.md)

> Dice qué se hace en la memoria cuando una regla `P` nace, cambia o sube a la base.

- Al crear o endurecer una regla `P`, se registra la señal correspondiente en la memoria (`tipo` `restriccion` / `patron` / `aprendizaje`) con puntero `Ver P<N>`.
- Al guardar una señal generalizable, se evalúa si merece volverse regla `P`; si sí, se crea en el mismo cierre.
- Si una `P` se promueve a la base común, se deja al inicio de la regla el banner *"promovida a base → `NN·Xn`"* y se compacta al mínimo específico del proyecto (nombres, rutas, matices que la base no cubre). El cuerpo de la base no se duplica.

## Reglas

> Es el catálogo: una regla por bloque, numerada `P<N>`. Cada regla nueva se agrega como `P<N+1>`, sin reusar números borrados. Si el proyecto no tiene reglas propias todavía, se escribe «Ninguna por ahora».

### P1 · «Título corto»

> Ejemplo de una regla con todos sus campos.

- **Regla:** «qué se debe / no se debe hacer, sin ambigüedad».
- **Respaldo:** [`NN·Xn · Título de la regla de la base`](«enlace al archivo de la regla») · «concreta / endurece: qué mitad pone esta `P`». Obligatorio ([`20·M16`](«RUTA-ESTANDAR»/base/20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md)).
- **Por qué:** «el motivo: qué problema evita o qué convención del equipo fija».
- **Ejemplo:** «un caso concreto» (si ayuda a entenderla).
- **Señal asociada:** «id o enlace en la memoria ([`13·DOC5`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md))».

### P2 · «…»

> Molde de la regla siguiente.

- **Regla:** «…»
- **Respaldo:** «…»
- **Por qué:** «…»
- **Señal asociada:** «…»
