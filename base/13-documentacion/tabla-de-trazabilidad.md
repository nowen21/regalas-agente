# La tabla canónica de trazabilidad, anexo de `13·DOC11`

> Anexo del capítulo [`13 · Documentación`](base.md). **No es una regla**: no lleva molde ni identificador propio. Es la tabla que [`DOC11`](reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md) manda usar, escrita una sola vez para que no se copie con variaciones.

Se escribe en el documento de cierre de la unidad, con estas cinco columnas y en este orden:

| Ítem de la especificación | Categoría | Ubicación esperada | Estado | Evidencia |
|---|---|---|---|---|
| (frase de la especificación) | (esquema, modelo, servicio, vista, prueba, permiso, ruta o doc) | (archivo real) | ✅, ❌, N/A o parcial | (prueba concreta o commit) |

**Qué se espera de cada estado.** El ✅ no lleva nada más. El ❌ dice a qué unidad se traslada lo que falta. El **parcial** dice qué parte queda. El **N/A** dice por qué no aplica: un «N/A porque sí» no es justificación.

**Un faltante que debía estar en esta unidad se corrige acá**, no se difiere: diferir es para lo que pertenece a otra unidad.
