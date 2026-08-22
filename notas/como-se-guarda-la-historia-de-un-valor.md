# Cómo se guarda la historia de un valor que cambia

Es el detalle de [`03·D7`](../base/03-datos.md). La regla dice **qué hay que lograr** —que preguntar «cuánto era esto en tal fecha» dé lo que era de verdad—; esto dice **cómo se logra**, y por qué el atajo no sirve.

## Por qué calcular al vuelo no alcanza

Reconstruir el pasado sumando los datos vivos hasta una fecha **solo funciona si el pasado no se toca**. En cuanto hay una anulación posterior, una corrección dentro de plazo, una reversión o un cambio de relación, esa reconstrucción devuelve **el estado teórico, no el que hubo**.

Y la diferencia aparece justo donde importa: en una auditoría, en un informe legal, en una disputa.

## Cuándo hace falta

| Sí | No |
|---|---|
| Valores derivados que cambian: saldos por período, participaciones, acumulados | Catálogos que no cambian con el uso |
| Relaciones que evolucionan y afectan cálculos: a quién pertenece, quién es responsable, en qué categoría está | Estadísticas del día, tableros en tiempo real |
| Estados que se citan en informes retrospectivos | Datos ya congelados por diseño (ver [`15`](../base/15-registros-inmutables.md)) |
| Cualquier valor que pueda aparecer en la pregunta «¿cuánto era en tal fecha?» | Informes de «estado actual» donde basta la marca de baja y las fechas |

## El patrón: tramos con inicio y fin

Una tabla de historial por entidad, donde cada fila es **un tramo de tiempo** con el estado congelado:

1. **La tabla** lleva la referencia a la entidad, las columnas del estado que se congela, **desde cuándo** vale el tramo, **hasta cuándo** —vacío mientras es el vigente—, un motivo corto que diga qué evento lo abrió, la auditoría de [`03·D10`](../base/03-datos.md) y un índice por entidad y fecha de inicio.
2. **Al migrar**, cada registro existente estrena su tramo inicial, desde su fecha de creación y sin cierre, con el motivo que lo diga.
3. **Cada cambio significativo emite un aviso**, y quien lo escucha hace dos cosas **en una sola transacción**: cierra el tramo vigente poniéndole su fin, y abre el nuevo.
4. **Una sola consulta** contesta «cómo estaba en tal fecha»: la del tramo vigente entonces.
5. **La entidad con historial no se borra de verdad**, solo se marca de baja. Su historial sobrevive.

**En la interfaz**, una línea de tiempo en la ficha deja que el usuario audite la evolución sin pedirle nada a nadie.

## Qué se prueba, sí o sí

- Que la migración inicial dejó bien los tramos.
- Que el aviso dispara el cierre y la apertura.
- Que preguntar por una fecha pasada **devuelve el valor de entonces, no el de hoy**.
- Que nunca hay dos tramos vigentes de la misma entidad a la vez.

## Cuando el volumen no da

Un tramo por entidad afectada puede ser mucho si un solo evento toca a muchas. La alternativa es **una fila por evento con el mapa completo del estado** en un campo estructurado.

**Se decide con datos reales delante, no por anticipado.** Elegir la alternativa antes de saber el volumen es optimizar lo que todavía no duele.

## El atajo que se rechaza, y su nombre

> *«Calcular al vuelo y ya, es más simple.»*

Simple hoy, incorrecto mañana. **La consulta histórica lee el historial; la consulta actual puede leer el estado vivo. No se mezclan**, porque en cuanto se mezclan nadie sabe cuál de las dos cosas está viendo.

## De dónde salió esta nota

Del [pendiente 19](../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md): `03·D7` medía **3 839 caracteres** contra los 320 del molde — doce veces. No era una regla larga: era **un patrón entero metido dentro de una regla**, y la exigencia real cabía en tres líneas.
