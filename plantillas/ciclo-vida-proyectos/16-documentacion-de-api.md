# Documentación de la API   ·   `[CAPA 3]`

**Para qué sirve este documento.** Es el contrato de la API con quien la consume: qué expone, cómo se autentica, qué recibe y qué devuelve cada punto, y qué errores da. Se escribe para quien integra **sin leer el código**, y se actualiza en la misma fase que cambia el contrato: una API documentada con retraso es una API documentada mal.

> Plantilla. Acompaña a la estación 06 y madura con el sistema. Si el proyecto genera su documentación desde el código (OpenAPI o equivalente), este documento no la duplica: dice dónde vive la generada y conserva solo lo que aquella no cuenta (autenticación, convenciones, versionado). Si el proyecto no expone API, existe igual y dice: «No aplica porque «el porqué»». Reemplaza los `«…»` y borra esta caja.

## 1. Las convenciones

| Aspecto | Convención |
|---|---|
| **Base y versión** | «`/api/v1/...` y cómo se versiona un cambio que rompe» |
| **Autenticación** | «cómo se obtiene y se envía la credencial; nunca la credencial misma» |
| **Formato** | «JSON, fechas en ISO-8601, paginación por «esquema»» |
| **Errores** | «la forma única del error: código, mensaje para humanos, detalle» |

## 2. El inventario de puntos

> Una fila por punto expuesto. «Permiso» dice quién puede llamarlo; un punto sin permiso declarado es público, y eso se dice.

| Método y ruta | Qué hace | Permiso | Estado |
|---|---|---|---|
| «`GET /api/...`» | «…» | «…» | «Existe / Por construir» |

## 3. El contrato de cada punto

> Un bloque por punto. Los datos de ejemplo son inventados: nunca datos reales ni credenciales ([`00·N4`](../../base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)).

### «MÉTODO /api/.../recurso»

```http
Request:  { «campos con ejemplo inventado» }
Response 200: { «…» }
Errores: «400 cuándo · 401 cuándo · 403 cuándo · 404 cuándo · 422 cuándo»
```

«Reglas del punto que el esquema no cuenta: idempotencia, límites, efectos secundarios.»

## 4. Qué se promete, y hasta cuándo

> Un contrato sin promesa escrita no es un contrato: quien integra no sabe con qué puede contar. Y una promesa sin fecha de caducidad amarra para siempre.

| Promesa | Hasta cuándo |
|---|---|
| «Los nombres de los puntos de arriba» | «Mientras no haya versión mayor» |
| «…» | «…» |

## 5. Qué NO se promete

> **Lo que no se promete se escribe, o se promete sin querer.** Quien integra da por seguro todo lo que no esté dicho.

- **«Qué no se garantiza».** «Por ejemplo: que la forma de la respuesta no crezca, que el tiempo se sostenga con cualquier volumen, que dos instalaciones respondan igual.»

## 6. Cuando el otro lado no responde

| Qué pasa | Qué hace quien integra |
|---|---|
| «El servicio no está disponible» | «…» |
| «Responde con error» | «…» |
| «Demora más de lo esperado» | «…» |
