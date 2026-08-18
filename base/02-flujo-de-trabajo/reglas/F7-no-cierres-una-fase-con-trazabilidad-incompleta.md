> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F7 · No cierres una fase con trazabilidad incompleta  ·  `[DEROGADA en 4.0.0 → ver 13·DOC3]`

> **Ya no rige.** Lo que exigía lo exige [`13·DOC3`](../../13-documentacion/reglas/DOC3-verifica-la-trazabilidad-especificacion-implementacion-antes-de-cerrar.md), dueño del tema *documentación* ([`M2`](../../20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md)), con el formato de la tabla en [`13·DOC11`](../../13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md). El texto original se conserva debajo y el ID no se reutiliza ([`M11`](../../20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md)).

Antes de cerrar, revisa ítem por ítem que cada afirmación técnica de la especificación esté en el código, el esquema, las pruebas y los docs, y no cierres con faltantes sin justificar (depende de [`13·DOC3`](../../13-documentacion/reglas/DOC3-verifica-la-trazabilidad-especificacion-implementacion-antes-de-cerrar.md), que fija el formato de la tabla de cierre).

```
INCORRECTO: "pruebas verdes → cierro"
CORRECTO:   "pruebas verdes + trazabilidad sin faltantes → cierro"
```

---

### Checklist  ·  **DEROGADA**

Reprobaba las filas **2** y **4** contra **v2.5.0** por duplicar a [`13·DOC3`](../../13-documentacion/reglas/DOC3-verifica-la-trazabilidad-especificacion-implementacion-antes-de-cerrar.md) —el ejemplo era idéntico palabra por palabra— ([`M2`](../../20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md), [`M12`](../../20-meta-reglas/reglas/M12-antes-de-crear-una-regla-buscar-la-duplicacion-es-el-defecto-mas-caro.md)). Se resolvió derogándola en **4.0.0**: quien citaba `02·F7` cita ahora [`13·DOC3`](../../13-documentacion/reglas/DOC3-verifica-la-trazabilidad-especificacion-implementacion-antes-de-cerrar.md).

> A una regla derogada no se le vuelve a aplicar el checklist: ya no rige. Queda para que las citas viejas resuelvan.
