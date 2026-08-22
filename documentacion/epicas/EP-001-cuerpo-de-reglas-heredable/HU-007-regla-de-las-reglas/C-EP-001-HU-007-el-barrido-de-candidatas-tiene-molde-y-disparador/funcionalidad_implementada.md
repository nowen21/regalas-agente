# Funcionalidad implementada — Fase C-EP-001-HU-007-el-barrido-de-candidatas-tiene-molde-y-disparador

**Para qué sirve este documento.** Dice qué quedó hecho al cerrar la fase, con la trazabilidad de cada ítem hasta el archivo donde vive.

> **Cerrada el 2026-08-22, con el estándar en la versión 31.0.0.** Es el sello que dice **bajo qué reglas** cerró este trabajo: una regla escrita después no lo reabre ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).

## 0. Qué quedó, en una frase

**Lo que el usuario pide dos veces ya no depende de que alguien se acuerde:** al cerrar cada versión se relee el tramo y lo repetido se escribe como candidata a regla.

## 1. Trazabilidad ([`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))

| Ítem de la especificación | Categoría | Ubicación esperada | Estado | Evidencia |
|---|---|---|---|---|
| El barrido tiene molde | doc | `plantillas/` | ✅ | [candidatas-a-regla.md](../../../../../plantillas/candidatas-a-regla.md), con las cuatro salidas y la regla del conteo |
| El barrido tiene disparador | regla | `base/20-meta-reglas/` | ✅ | [`M20`](../../../../../base/20-meta-reglas/reglas/M20-antes-de-publicar-una-version-se-barre-lo-que-se-pidio-dos-veces.md), checklist en CUMPLE |
| La regla está enrutada y clasificada | doc | índices | ✅ | fila en el [índice del capítulo](../../../../../base/20-meta-reglas/base.md), en [plantillas/README.md](../../../../../plantillas/README.md) y en [reglas-validables.md](../../../../../validadores/reglas-validables.md) |
| El criterio existe en la historia | doc | esta HU | ✅ | `CA-06`, nacido con esta fase |
| El cambio queda versionado | doc | `CHANGELOG.md`, `VERSION` | ✅ | v31.0.0, MAYOR |

## 2. Lo que cambia para un proyecto que hereda

**Sí hay algo nuevo que hacer, y por eso es MAYOR:** antes de publicar una versión hay que releer el tramo cerrado y escribir el barrido. Un proyecto que nunca haya barrido **no tiene que barrer hacia atrás**: la regla rige del tramo en curso en adelante, como fija [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md) para cualquier norma nueva.

**Lo que no cambia:** ninguna candidata se convierte en regla desde el barrido. Escribirla sigue siendo el procedimiento completo, con su aprobación.

## 3. Lo que queda abierto

**El criterio `CA-06` nació con esta fase**, no antes. El pendiente 33 dejaba dos salidas —criterio nuevo o historia propia— y se eligió la primera, por `20·M2`: el tema de cómo nace una regla ya tiene dueña. Si el usuario prefiere historia propia, el `CA-06` se mueve entero y esta fase queda igual.

**El primer barrido real todavía no se hizo.** Lo dispara la próxima publicación, y ahí se sabrá si el molde pide los datos correctos.
