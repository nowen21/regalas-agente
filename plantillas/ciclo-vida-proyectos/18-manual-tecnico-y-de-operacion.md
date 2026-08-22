# Manual técnico y de operación   ·   `[CAPA 3]`

**Para qué sirve este documento.** Es el manual de quien **mantiene** el sistema andando: cómo se respalda y se restaura, cómo se sabe que está vivo, qué tareas corren solas y qué hacer cuando algo falla a las tres de la mañana. El manual de usuario cuenta cómo se usa; este cuenta cómo se sostiene.

> Plantilla. Se alimenta desde que existe algo que operar, y cada procedimiento se escribe **probado**: un respaldo que nunca se restauró es una esperanza, no un respaldo ([`03·D6`](../../base/03-datos.md)). Mientras el proyecto no esté en producción, las secciones que dependan de ella dicen «No aplica todavía porque «el porqué»» y se llenan al desplegar. Reemplaza los `«…»` y borra esta caja.

## 1. El sistema en una página

«Qué es, de qué piezas se compone (aplicación, base de datos, tareas, integraciones) y dónde corre cada una. El detalle vive en el [modelo de datos](14-modelo-de-datos.md) y las especificaciones; acá va el mapa que orienta a quien llega a operar.»

## 2. Respaldo y restauración

| Qué se respalda | Con qué frecuencia | Cómo (comando) | Dónde queda | Última restauración **probada** |
|---|---|---|---|---|
| «base de datos» | «…» | «…» | «…» | «AAAA-MM-DD, por quién» |

**El procedimiento de restauración, paso a paso:** «literal, probado, con lo que se espera ver. La fecha de la última prueba de restauración se actualiza cada vez que se ejecuta.»

## 3. Cómo se sabe que está vivo

| Señal | Dónde se mira | Qué es normal | Qué obliga a actuar |
|---|---|---|---|
| «disponibilidad, errores, disco» | «…» | «…» | «…» |

«Si el proyecto adoptó el capítulo [`19`](../../base/19-observabilidad-y-operacion.md), el detalle de monitoreo y alertas vive bajo sus reglas y acá queda el puntero.»

## 4. Lo que corre solo

| Tarea programada | Cuándo corre | Qué hace | Qué pasa si no corre |
|---|---|---|---|
| «…» | «…» | «…» | «…» |

## 5. Cuando algo falla

> Los incidentes que ya se conocen, con su remedio probado. Cada incidente nuevo que se resuelva agrega su fila: este manual crece con las cicatrices.

| Síntoma | Causa probable | Qué hacer |
|---|---|---|
| «…» | «…» | «…» |

## 6. Accesos y contactos

«Quién tiene acceso a qué (roles, no credenciales: [`00·N6`](../../base/00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada)) y a quién se llama para qué.»
