# 15 · Registros inmutables (patrón opt-in)

> **Capa 2 · agnóstica al stack · opt-in.** Patrón para los registros cuyo hecho ya se materializó y tiene valor legal, contable o de auditoría: **no se editan ni se borran, se anulan con trazabilidad**. No todo proyecto lo necesita; la capa 3 lo **activa** y declara a qué entidades aplica (documentos contables, transacciones, actas, comprobantes, cualquier registro con efecto irreversible en el mundo real).

---

## IM1 · Un registro materializado es inmutable

Cuando un registro representa un hecho que ya surtió efecto (un movimiento contable generado, un pago aplicado, un saldo afectado, un documento emitido), **no se puede editar ni borrar físicamente**. La única operación válida sobre él es la **anulación con motivo y trazabilidad**.

- Mientras el registro está en borrador (aún no materializado), se edita normalmente.
- Una vez materializado, cambia de estado y queda inmutable.

```
INCORRECTO: editar un documento ya materializado con un update normal, sin revertir su efecto
CORRECTO:   anularlo (con motivo, revirtiendo su efecto en transacción) y preservar la fila
```

---

## IM2 · Estados mínimos y campos de anulación

El registro maneja al menos tres estados: **borrador** (editable), **materializado** (inmutable) y **anulado** (revertido, fila preservada). Para la anulación, guarda: **cuándo** se anuló, **quién** la ejecutó y **el motivo** (obligatorio, no trivial).

---

## IM3 · La anulación revierte el efecto en una transacción

La operación de anular:

1. Verifica que el estado actual permita anular (rechaza si está en borrador —usar edición normal— o ya anulado).
2. Exige un **motivo** no vacío y con sustancia.
3. En una **transacción**, revierte todos los efectos del registro (movimientos, saldos, registros derivados) y marca el registro como anulado con sus datos de trazabilidad.
4. Avisa a los demás módulos (evento) para que invaliden cachés o agregados que dependían del registro.

> Si algo de la reversión falla, la transacción se revierte entera: no queda un estado a medias (`05-errores-y-logging.md` E2).

---

## IM4 · Las consultas agregadoras excluyen los anulados

Toda consulta que sume, cuente o promedie montos **excluye explícitamente** los registros anulados. Idealmente, la exclusión es el comportamiento **por defecto** del modelo/consulta, para no depender de que cada consulta lo recuerde.

```
INCORRECTO: un reporte que suma totales incluyendo los anulados "y el usuario que tenga cuidado"
CORRECTO:   la consulta excluye los anulados por defecto
```

---

## IM5 · Permiso propio para anular

Anular tiene mayor peso que crear o editar: lleva un **permiso separado**, distinto del de eliminación corriente, restringido a los roles con responsabilidad (`04-seguridad.md` S1). En la interfaz, los registros materializados ofrecen "Anular" (con motivo obligatorio) en vez de "Eliminar"; los anulados siguen visibles, marcados y con su motivo consultable.

---

## Relación con el resto del estándar

- **`03-datos.md` D1** — auditoría y borrado lógico son la base de este patrón.
- **`05-errores-y-logging.md` E2** — la reversión va en transacción; o todo o nada.
- **`04-seguridad.md` S1** — permiso propio y scope para la anulación.
- **`12-privacidad-datos.md` PR5** — cuando hay que "borrar" datos personales de un registro que debe preservarse, anonimizar en vez de borrar.
