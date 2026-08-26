# Funcionalidad implementada — Fase A-EP-001-HU-001-molde-de-regla

**Para qué sirve este documento.** Dice qué quedó hecho al cerrar la fase, con la trazabilidad de cada ítem hasta el archivo donde vive. El plan está en [plan_trabajo.md](plan_trabajo.md); lo probado, en [resultado_pruebas.md](resultado_pruebas.md).

> **Cerrada el 2026-08-22, con el estándar en la versión 31.8.0.** Es el sello que dice **bajo qué reglas** cerró este trabajo: una regla escrita después no lo reabre ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).

## 0. Qué quedó, en una frase

**Toda regla del estándar se escribe con el mismo molde, y eso ya no es una costumbre: es un documento con su comprobación.**

## 1. Trazabilidad ([`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))

| Ítem de la especificación | Categoría | Ubicación esperada | Estado | Evidencia |
|---|---|---|---|---|
| El molde está escrito y es la fuente única | doc | [`base/20-meta-reglas/estructura-regla.md`](../../../../../base/20-meta-reglas/estructura-regla.md) | ✅ | el anexo del capítulo, con su ejemplo terminado |
| La exigencia de usarlo es una regla | regla | [`20·M5`](../../../../../base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) | ✅ | checklist en CUMPLE |
| Cada regla tiene identificador único y prefijado | regla | [`20·M4`](../../../../../base/20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md) | ✅ | 249 identificadores, 249 distintos |
| Una regla con dos exigencias se detecta | doc | fila 9 del [checklist](../../../../../base/20-meta-reglas/checklist.md) | ✅ | 26 reglas marcadas dobles con esa fila |
| Qué hacer cuando no hay ejemplo posible | doc | fila 12 del checklist y el molde | ✅ | N/A admitido, siempre con el motivo escrito |
| La cita a una regla llega a la regla | prueba | `validar.py estandar` | ✅ | sin incumplimientos; la cita a un ID inexistente se reporta |
| Qué parte del molde es opcional | doc | el molde | parcial | está escrito («no obliga a rellenar lo que no hace falta») y no hay programa que lo compruebe: la fila 12 sí, las demás partes no |

## 2. Lo que cambia para un proyecto que hereda

**Nada nuevo que hacer.** El molde y `M5` ya viajaban; esta fase no cambia ninguna exigencia, deja probado lo que ya regía.

## 3. Lo que queda abierto

**Que el identificador repetido lo vea un programa.** Hoy lo ve quien lea el índice del capítulo, y hoy no hay ninguno repetido, pero eso se sostiene por conteo y no por comprobación. Queda dicho en el [resultado](resultado_pruebas.md) §4, con su caso de prueba ya escrito, para que EP-004 lo recoja.

**El plan pedía escribir dos reglas de prueba y no se escribieron:** se probó contra las 249 reglas reales que el molde ya produjo, que es mejor evidencia y no ensucia el cuerpo con reglas de mentira. Queda dicho para que nadie lea el plan y crea que ese paso se saltó por descuido.
