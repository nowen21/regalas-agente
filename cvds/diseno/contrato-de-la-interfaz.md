# El contrato de la interfaz local   ·   `[CAPA 3]`

**Para qué sirve este documento.** Qué puede pedirle otro programa a la interfaz local, qué recibe, y qué se promete que no va a cambiar. **No se expone ningún servicio a la red** ([`DA-06`](decisiones-de-arquitectura.md)): esto es el contrato de lo que corre en la propia máquina.

> **Escrito como si no hubiera nada construido**, igual que el resto de [cvds/](../README.md).

**Estado: BORRADOR** (2026-08-24, sin aprobar).

---

## 1. Qué es y qué no es este contrato

| Es | No es |
|---|---|
| Lo que la interfaz responde a quien se lo pida desde la misma máquina | Un servicio publicado: no escucha fuera de la máquina |
| Un contrato de solo lectura | Una forma de cambiar el proyecto: nada de acá modifica nada |
| Estable entre versiones menores | Inmutable: una versión mayor puede cambiarlo, y lo declara antes |

## 2. Lo que se puede pedir

| # | Qué se pide | Qué se recibe | Qué pasa si no está |
|---|---|---|---|
| 1 | El estado del ciclo | Las siete etapas, con si tienen documento y si está aprobado | Nunca falta: una etapa sin documento se responde como «sin escribir» |
| 2 | La lista de documentos de una etapa | Nombre, ruta y estado de cada uno | Etapa que no existe: se responde que no existe, con las que sí |
| 3 | Un documento | Su contenido, y cuántos espacios sin llenar tiene | Documento que figura y no está en el disco: se responde cuál falta y dónde debería estar |
| 4 | El entregable de un documento | El `.docx` generado desde su `.md` | Con espacios sin llenar: se avisa antes de generar · Sin molde conocido: no se genera, y se dice por qué |
| 5 | Lo guardado en la memoria | Las anotaciones, de la más reciente a la más vieja | Memoria no disponible: se responde que no se pudo leer, sin inventar una lista vacía |
| 6 | Buscar en la memoria | Las anotaciones que coinciden | Ninguna coincide: se responde que no hay, y no se sugiere nada parecido |
| 7 | Las reglas vigentes | Las reglas por capítulo, con desde qué versión rigen | Nunca falta |

## 3. Qué se promete que no cambia

| Promesa | Hasta cuándo |
|---|---|
| Los nombres con que se piden las siete cosas de arriba | Mientras no haya versión mayor |
| Que ninguna petición cambie el estado del proyecto | Siempre: es la decisión `DA-06`, no una elección de esta versión |
| Que la respuesta diga siempre qué falta, en vez de responder vacío | Siempre |
| Que funcione sin red | Siempre, mientras rija RNF-02 |

## 4. Qué NO se promete

- **Que la forma de la respuesta no crezca.** Se pueden agregar datos nuevos; lo que no se quita es lo que ya estaba.
- **Que responda rápido con cualquier tamaño.** El único tiempo comprometido es el de abrir la sesión, y ese es RNF-01.
- **Que dos máquinas respondan lo mismo.** Cada una responde por su propio repositorio.

## 5. Cuando el otro lado no responde

| Qué pasa | Qué hace quien pide |
|---|---|
| La interfaz no está levantada | Lee los archivos directamente: son la fuente, y la interfaz solo los muestra |
| La memoria no responde | Sigue con los documentos, que no dependen de ella |
| El generador falla | El `.md` sigue intacto: se vuelve a pedir cuando se corrija |

> **Ninguna de estas fallas pierde datos.** La interfaz no guarda nada propio: todo lo que muestra existe antes que ella y sigue existiendo si se cae.
