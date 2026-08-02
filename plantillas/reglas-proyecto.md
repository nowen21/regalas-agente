# Reglas del proyecto — «Nombre»   ·   `[CAPA 3 · LOCAL]`

> Catálogo de reglas **propias de este proyecto** (`13·DOC10`) que sobrescriben o complementan la base común. Cada regla va numerada `P<N>` para poder citarse de forma estable desde specs, planes y señales. Vive en `.agente/reglas-proyecto.md` (**local, no versionado** — es configuración del agente). Reemplaza los `«…»` y borra esta caja.

---

## Precedencia (dónde mandan estas reglas)

`00` núcleo blindado  →  `01`–`17` convenciones  →  **estas reglas `P`**  →  (nada por encima del núcleo).

Una regla `P` puede **endurecer o complementar** una convención (`01`–`17`), pero **nunca** contradecir el núcleo (`00`). Ante choque, gana el núcleo.

## Sincronización con la memoria  ·  `13·DOC10`

- **Al crear o endurecer una regla `P`:** registrar la señal correspondiente en la memoria (`tipo` `restriccion` / `patron` / `aprendizaje`) con puntero `Ver P<N>`.
- **Al guardar una señal generalizable:** evaluar si merece volverse regla `P`; si sí, crearla en el mismo cierre.
- **Si una `P` se promueve a la base común:** dejar banner *"promovida a base → `NN·Xn`"* al inicio de la regla y **compactarla** al mínimo específico del proyecto (nombres, rutas, matices que la base no cubre). No duplicar el cuerpo de la base.

---

## Reglas

### P1 · «Título corto»

- **Regla:** «qué se debe / no se debe hacer, sin ambigüedad».
- **Por qué:** «el motivo — qué problema evita o qué convención del equipo fija».
- **Ejemplo:** «un caso concreto» (si ayuda a entenderla).
- **Relación con la base:** «endurece / complementa `NN·Xn`» — o «regla nueva, no cubierta por la base».
- **Señal asociada:** «id o enlace en la memoria (`13·DOC5`)».

### P2 · «…»

- **Regla:** «…»
- **Por qué:** «…»
- **Relación con la base:** «…»
- **Señal asociada:** «…»

---

_(Si el proyecto no tiene reglas propias todavía: dejar "Ninguna por ahora". Cada regla nueva se agrega numerada `P<N+1>`, sin reusar números borrados.)_
