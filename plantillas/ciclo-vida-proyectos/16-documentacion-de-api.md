# Documentación de la API   ·   `[CAPA 3]`

**Para qué sirve este documento.** Es el contrato de la API con quien la consume: qué expone, cómo se autentica, qué recibe y qué devuelve cada punto, y qué errores da. Se escribe para quien integra sin leer el código, y se actualiza en la misma fase que cambia el contrato: una API documentada con retraso es una API documentada mal.

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |

> Plantilla de la documentación de la API. Acompaña a la estación 06 y madura con el sistema. Si el proyecto genera su documentación desde el código (OpenAPI o equivalente), este documento no la duplica: dice dónde vive la generada y conserva solo lo que aquella no cuenta (autenticación, convenciones, versionado). Si el proyecto no expone API, el documento existe igual y dice: «No aplica porque «el porqué»».
>
> Al llenarla se reemplazan los `«…»` y se borran todas las notas como esta. El párrafo «Para qué sirve este documento» se queda.

## 1. Las convenciones

> Son las reglas que comparten todos los puntos de la API.

| Aspecto | Convención |
|---|---|
| **Base y versión** | «`/api/v1/...` y cómo se versiona un cambio que rompe» |
| **Autenticación** | «cómo se obtiene y se envía la credencial; nunca la credencial misma» |
| **Formato** | «JSON, fechas en ISO-8601, paginación por «esquema»» |
| **Errores** | «la forma única del error: código, mensaje para humanos, detalle» |

## 2. El inventario de puntos

> Lista los puntos que la API expone, uno por fila. La columna Permiso dice quién puede llamarlo; un punto sin permiso declarado es público, y eso se dice.

| Método y ruta | Qué hace | Permiso | Estado |
|---|---|---|---|
| «`GET /api/...`» | «…» | «…» | «Existe / Por construir» |

## 3. El contrato de cada punto

> Detalla qué recibe, qué devuelve y qué errores da cada punto, un bloque por punto. Los datos de ejemplo son inventados: nunca datos reales ni credenciales ([`00·N4`](../../base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)).

### «MÉTODO /api/.../recurso»

> Agrupa el contrato de un punto: la petición, la respuesta y los errores.

```http
Request:  { «campos con ejemplo inventado» }
Response 200: { «…» }
Errores: «400 cuándo · 401 cuándo · 403 cuándo · 404 cuándo · 422 cuándo»
```

«Reglas del punto que el esquema no cuenta: idempotencia, límites, efectos secundarios.»

## 4. Qué se promete, y hasta cuándo

> Lista lo que la API garantiza a quien la integra y hasta cuándo. Sin promesa escrita, quien integra no sabe con qué puede contar; sin fecha de caducidad, la promesa amarra para siempre.

| Promesa | Hasta cuándo |
|---|---|
| «Los nombres de los puntos de arriba» | «Mientras no haya versión mayor» |
| «…» | «…» |

## 5. Qué NO se promete

> Lista lo que la API no garantiza. Lo que no se promete se escribe, o se promete sin querer: quien integra da por seguro todo lo que no esté dicho.

- **«Qué no se garantiza».** «Por ejemplo: que la forma de la respuesta no crezca, que el tiempo se sostenga con cualquier volumen, que dos instalaciones respondan igual.»

## 6. Cuando el otro lado no responde

> Dice cómo reacciona quien integra ante cada falla de la API.

| Qué pasa | Qué hace quien integra |
|---|---|
| «El servicio no está disponible» | «…» |
| «Responde con error» | «…» |
| «Demora más de lo esperado» | «…» |
