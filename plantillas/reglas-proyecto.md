# Reglas del proyecto — «Nombre»   ·   `[CAPA 3 · LOCAL]`

> Catálogo de reglas **propias de este proyecto** ([`13·DOC10`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC10-registra-en-el-catalogo-del-proyecto-toda-regla-propia.md)) que sobrescriben o complementan la base común. Cada regla va numerada `P<N>` para poder citarse de forma estable desde especificaciones, planes y señales. Vive en `.agente/reglas-proyecto.md` (**local, no versionado** — es configuración del agente). Reemplaza los `«…»` y borra esta caja.

---

## Precedencia (dónde mandan estas reglas)

`00` núcleo blindado  →  `01`-`17` convenciones  →  **estas reglas `P`**  →  (nada por encima del núcleo).

Una regla `P` puede **endurecer o complementar** una convención (`01`-`17`), pero **nunca** contradecir el núcleo (`00`). Ante choque, gana el núcleo.

## Ninguna `P` se sostiene sola  ·  [`20·M16`](«RUTA-ESTANDAR»/base/20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md)

Toda `P` declara, con su enlace, la regla de la base cuyo criterio concreta: la base dice **qué hay que decidir**, la `P` dice **con qué valor se decide en este proyecto**.

Si ningún criterio de la base la cubre, la regla **no se escribe todavía**: primero se crea la regla en el estándar, sin el detalle de este proyecto, y después la `P` la concreta. Sin ese respaldo el catálogo se vuelve un estándar paralelo, sin checklist, sin versión y sin nadie que lo audite.

## Sincronización con la memoria  ·  [`13·DOC10`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC10-registra-en-el-catalogo-del-proyecto-toda-regla-propia.md)

- **Al crear o endurecer una regla `P`:** registrar la señal correspondiente en la memoria (`tipo` `restriccion` / `patron` / `aprendizaje`) con puntero `Ver P<N>`.
- **Al guardar una señal generalizable:** evaluar si merece volverse regla `P`; si sí, crearla en el mismo cierre.
- **Si una `P` se promueve a la base común:** dejar banner *"promovida a base → `NN·Xn`"* al inicio de la regla y **compactarla** al mínimo específico del proyecto (nombres, rutas, matices que la base no cubre). No duplicar el cuerpo de la base.

---

## Reglas

### P1 · «Título corto»

- **Regla:** «qué se debe / no se debe hacer, sin ambigüedad».
- **Respaldo:** [`NN·Xn · Título de la regla de la base`](«enlace al archivo de la regla») · «concreta / endurece: qué mitad pone esta `P`». Obligatorio ([`20·M16`](«RUTA-ESTANDAR»/base/20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md)).
- **Por qué:** «el motivo: qué problema evita o qué convención del equipo fija».
- **Ejemplo:** «un caso concreto» (si ayuda a entenderla).
- **Señal asociada:** «id o enlace en la memoria ([`13·DOC5`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md))».

### P2 · «…»

- **Regla:** «…»
- **Respaldo:** «…»
- **Por qué:** «…»
- **Señal asociada:** «…»

---

_(Si el proyecto no tiene reglas propias todavía: dejar "Ninguna por ahora". Cada regla nueva se agrega numerada `P<N+1>`, sin reusar números borrados.)_
