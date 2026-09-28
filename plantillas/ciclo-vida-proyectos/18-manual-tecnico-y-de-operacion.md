# Manual técnico y de operación   ·   `[CAPA 3]`

**Para qué sirve este documento.** Es el manual de quien **mantiene** el sistema andando: cómo se respalda y se restaura, cómo se sabe que está vivo, qué tareas corren solas y qué hacer cuando algo falla a las tres de la mañana. El manual de usuario cuenta cómo se usa; este cuenta cómo se sostiene.

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Plantilla. Se alimenta desde que existe algo que operar, y cada procedimiento se escribe después de **probarlo**: de un respaldo que nunca se restauró no se sabe si sirve ([`03·D6`](../../base/03-datos.md)). Mientras el proyecto no esté en producción, las secciones que dependan de ella dicen «No aplica todavía porque «el porqué»» y se llenan al desplegar.
>
> Al llenarla se reemplazan los `«…»` y se borran todas las notas como esta.

## 1. El sistema en una página

> Da a quien llega a operar el sistema la vista completa, sin entrar en detalle.

«Qué es, de qué piezas se compone (aplicación, base de datos, tareas, integraciones) y dónde corre cada una. El detalle vive en el [modelo de datos](14-modelo-de-datos.md) y las especificaciones; acá va el mapa que orienta a quien llega a operar.»

## 2. Respaldo y restauración

> Dice qué se respalda, cada cuánto, con qué comando y dónde queda, y cuándo se comprobó por última vez que la restauración funciona.

| Qué se respalda | Con qué frecuencia | Cómo (comando) | Dónde queda | Última restauración **probada** |
|---|---|---|---|---|
| «base de datos» | «…» | «…» | «…» | «AAAA-MM-DD, por quién» |

**El procedimiento de restauración, paso a paso:** «literal, probado, con lo que se espera ver. La fecha de la última prueba de restauración se actualiza cada vez que se ejecuta.»

## 3. Cómo se sabe que está vivo

> Son las señales que muestran si el sistema funciona: dónde se miran, qué valor es normal y cuál obliga a actuar.

| Señal | Dónde se mira | Qué es normal | Qué obliga a actuar |
|---|---|---|---|
| «disponibilidad, errores, disco» | «…» | «…» | «…» |

«Si el proyecto adoptó el capítulo [`19`](../../base/19-observabilidad-y-operacion.md), el detalle de monitoreo y alertas vive bajo sus reglas y acá queda el puntero.»

## 4. Lo que corre solo

> Son las tareas programadas que corren sin que nadie las lance, y lo que se daña si una deja de correr. Si no hay, se escribe «Ninguna».

| Tarea programada | Cuándo corre | Qué hace | Qué pasa si no corre |
|---|---|---|---|
| «…» | «…» | «…» | «…» |

## 5. Cuando algo falla

> Son los incidentes ya conocidos, cada uno con su remedio probado. Cada incidente nuevo que se resuelve agrega su fila.

| Síntoma | Causa probable | Qué hacer |
|---|---|---|
| «…» | «…» | «…» |

## 6. Accesos y contactos

> Reúne los roles con acceso al sistema y a quién se acude en cada tipo de problema.

«Quién tiene acceso a qué (roles, no credenciales: [`00·N6`](../../base/00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada)) y a quién se llama para qué.»
