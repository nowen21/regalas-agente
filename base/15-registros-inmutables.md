# 15 · Registros inmutables (patrón opt-in)  ·  `[CAPA 2 · opt-in]`

**Opt-in.** Para registros cuyo hecho ya se materializó y tiene valor legal/contable/de auditoría: **no se editan ni se borran, se anulan con trazabilidad**. La capa 3 lo **activa** y dice a qué entidades aplica (documentos contables, transacciones, actas, comprobantes).

---

## IM1 · Un registro materializado es inmutable

Cuando un registro ya surtió efecto (movimiento contable generado, pago aplicado, saldo afectado, documento emitido), **no se edita ni se borra físico**. La única operación válida es **anular con motivo y trazabilidad**. En borrador (aún no materializado) sí se edita.

```
INCORRECTO: editar un documento materializado con un update, sin revertir su efecto
CORRECTO:   anularlo (con motivo, revirtiendo el efecto en transacción) y preservar la fila
```

## IM2 · Estados y campos de anulación

Al menos tres estados: **borrador** (editable), **materializado** (inmutable), **anulado** (revertido, fila preservada). Para anular guarda: cuándo, quién y **el motivo** (obligatorio, con sustancia).

## IM3 · Anular revierte el efecto en transacción

1. Verifica que el estado permita anular (rechaza borrador → usar edición; o ya anulado).
2. Exige **motivo** no vacío.
3. En **transacción**: revierte todos los efectos (movimientos, saldos, derivados) y marca anulado con su trazabilidad.
4. Avisa a los demás módulos (evento) para invalidar cachés/agregados.

Si algo de la reversión falla, se revierte entera: sin estados a medias (`05` · E2).

## IM4 · Las consultas agregadoras excluyen los anulados

Toda consulta que sume/cuente/promedie **excluye** los anulados. Idealmente por **defecto** en el modelo/consulta, no confiando en que cada consulta lo recuerde.

```
INCORRECTO: un reporte que suma incluyendo anulados "y que el usuario tenga cuidado"
CORRECTO:   la consulta excluye anulados por defecto
```

## IM5 · Permiso propio para anular

Anular pesa más que crear o editar: **permiso separado** del de eliminar, para roles con responsabilidad (`04` · S1). En la UI, los materializados ofrecen "Anular" (motivo obligatorio) en vez de "Eliminar"; los anulados quedan visibles, marcados y con su motivo.

---

Ver: `03` D1 (auditoría, soft delete), `05` E2 (transacción), `04` S1 (permiso/scope), `12` PR5 (anonimizar en vez de borrar).
