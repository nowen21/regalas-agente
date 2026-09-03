# Especificación del módulo Expediente  ·  `[CAPA 3]`

- **Slug del módulo:** `expediente`
- **Estado:** aprobada, el 2026-08-31 por Ing. José Dúmar Jiménez Ruíz
- **Versión del producto:** 2, según [cvds/implementacion/README.md](../../cvds/implementacion/README.md)

---

## 1. Propósito y alcance

Juntar la documentación de un proyecto en el orden del ciclo, decir qué le falta, y convertirla en el archivo que el cliente espera, sin escribir una línea a mano.

- **Dentro de alcance:** armar el expediente con el alcance que se pida (`F-025`) y generar el entregable de ofimática desde el texto (`F-026`).
- **Fuera de alcance:** la auditoría y la memoria —decidido el 2026-08-31, cerrando la duda 5 del análisis—; recibir cambios hechos encima del entregable (`DA-09`); y llenar los documentos desde la plataforma (`F-014`).

## 2. Contexto — qué hay hoy

Los documentos ya están en la plataforma. El módulo Importación los trajo y **reconoció 1 054 en este repositorio**, repartidos en 19 tipos, y sabe decir de cada archivo qué documento es.

Lo que no hay es forma de juntarlos. Hoy se arma abriendo carpeta por carpeta, y por eso cuesta un día y sale distinto cada vez.

**Módulo nuevo, sin código previo.** El primer expediente que se arme será el de este repositorio, que es el proyecto conectado.

## 3. Supuestos, dependencias y preguntas abiertas

- **Supuestos:** que lo que Importación reconoció alcanza. Un archivo que ese módulo no reconoce **no entra y se dice**.
- **Dependencias:** Importación, que aporta los documentos y su tipo; Proyectos, que dice de cuál son; Auditoría, donde queda registrado que se generó un entregable.
- **Preguntas abiertas:** ninguna que detenga. Si un cliente exige trabajar sobre el entregable como documento vivo, `DA-09` se revisa.

## 4. Reglas de negocio

1. **El expediente se arma en el orden del ciclo**, no en el que los documentos llegaron. Baja de `RN-1` de la `HU-001`.
2. **Lo que falta se lista con su nombre, y nunca se inventa.** Un expediente que no dice qué le falta es peor que no tenerlo: se entrega incompleto sin que nadie lo note.
3. **Lo que está a medio llenar se marca antes de entregar.** Baja de `RN-5` del inventario: lo sin verificar se entrega diciendo que lo está.
4. **La auditoría y la memoria no entran.** Sirven para saber cómo se llegó, no para entregar.
5. **Armar y generar no modifican ningún documento.** Solo leen.
6. **La fuente es el texto; la salida se rehace y no se edita.** Baja de [`DA-09`](../../cvds/diseno/decisiones-de-arquitectura.md) y de `RN-7` del inventario.
7. **Recortar por alcance dice qué quedó fuera.** Recortar en silencio es lo mismo que perder.

## 5. Modelo de datos

- **Entidades:** ninguna nueva que se guarde. **El expediente se calcula al pedirlo**, leyendo lo que Importación ya indexó; guardarlo crearía una segunda verdad que envejece, que es lo que `DA-01` viene a evitar.

**Lo que sí se guarda** es el entregable generado, como un archivo más de `datos/`, y su registro en la auditoría:

| Qué | Dónde vive | Por qué ahí |
|---|---|---|
| El expediente | En ninguna parte: se calcula | Es una vista de lo que ya está indexado |
| El entregable generado | Texto en `datos/`, en la carpeta del proyecto | Se rehace cuando se quiera; se guarda para poder entregarlo dos veces igual |
| Que se generó, y cuándo | Auditoría | `DA-08`: se registra cada acción que cambia algo |

- **Valores configurables:** ninguno en esta versión.
- **Migración:** no aplica.

### 5.1 El orden del ciclo, tipo por tipo

Es lo que la `HU-001` pedía declarar. Sale de las siete etapas del ciclo y del árbol de trabajo, que ya están escritos:

| Orden | Qué entra | Tipos que lo componen |
|---|---|---|
| 1 | **Planificación** | etapa del ciclo de vida, acta de constitución, estudio de factibilidad |
| 2 | **Análisis de requisitos** | etapa del ciclo de vida, inventario de funcionalidades |
| 3 | **Diseño** | etapa del ciclo de vida, modelo de datos, decisiones de arquitectura, diseño de interfaz, contrato de la interfaz |
| 4 | **Especificaciones de módulo** | especificación de módulo |
| 5 | **Épicas** | épica |
| 6 | **Historias de usuario** | historia de usuario |
| 7 | **Fases** | plan de trabajo, plan de pruebas, resultado de pruebas, estado de fase, funcionalidad implementada — en ese orden dentro de cada fase |
| 8 | **Implementación, pruebas, despliegue y mantenimiento** | etapa del ciclo de vida |
| 9 | **Registros de versión** | registro de versión |

**Los índices no entran como documentos**: son la tabla de contenido de una carpeta, y el expediente arma la suya.

**Lo que no encaje en ningún grupo se lista aparte**, con su tipo y su ruta. No se acomoda a la fuerza en el grupo más parecido: eso convierte un dato en una suposición.

## 6. Comportamiento y flujos

**Armar el expediente.** Se recibe qué proyecto y qué alcance. Se leen los documentos que Importación indexó de ese proyecto, se agrupan por el orden de la §5.1 y se devuelve el conjunto con tres listas más:

- **Lo que falta:** los documentos que el ciclo espera y no están, con su nombre.
- **Lo incompleto:** los que conservan marcas de espacio por llenar, con cuántas.
- **Lo que no encaja:** los que Importación no reconoció, o cuyo tipo no está en el orden.

Un proyecto sin documentos responde que no hay ninguno; no devuelve un expediente vacío.

**Recortar por alcance.** Se puede pedir hasta cierta fase. Lo que quede fuera se lista, con cuántos documentos son.

**Generar el entregable.** Se recibe el expediente armado y se produce **un solo archivo**, con su índice y sus documentos en el mismo orden.

- Si hay documentos incompletos, **se avisa antes de generar** y se genera igual si el usuario lo pide: la decisión de entregar es suya.
- Generar dos veces sobre lo mismo da el mismo archivo. La fecha de generación, si se escribe, va en un sitio que la comparación excluye **y eso se dice**.
- Generar queda registrado en la auditoría.

## 7. Interfaz

Una pantalla dentro de la vista de un proyecto: pedir el expediente, ver las tres listas, y generar. **`F-025` puede terminarse sin pantalla**, con orden de consola, igual que se hizo en Medición; la pantalla llega con `F-026` o después.

## 8. Permisos y autorización

**Desde `EP-022` hay cuentas, dos grupos y permisos.** Quién puede qué está en la [especificación de Acceso](../acceso/spec.md) §8. Acá vale la regla general: **el agente no aprueba, no publica versiones, no deroga reglas y no administra cuentas.**

## 9. Marco normativo

**Sí aplica.** El entregable sale del proyecto y llega a un tercero, así que es la única salida del sistema hacia afuera. Lo que se entrega es lo que el usuario ya escribió; lo que **no** se entrega —auditoría y memoria— está decidido y escrito. Ninguna credencial puede aparecer: los documentos ya vienen sin ellas, y el generador no agrega nada que no esté en el texto.

## 10. Plan de pruebas

| Qué se prueba | Casos |
|---|---|
| Armar | Proyecto completo · con un documento faltante · con uno incompleto · con uno que no se reconoce · sin documentos |
| Orden | Que sea el del ciclo y no el del disco |
| Alcance | Completo contra acotado, y que lo acotado diga qué dejó fuera |
| Que NO entre | La auditoría y la memoria, sobre este repositorio, que tiene las dos |
| Generar | Expediente completo · con incompletos · **una tabla con viñetas adentro** |
| Repetible | Generar dos veces y comparar la huella |
| Que NO pase | Que armar o generar modifique un documento |

## 11. Criterios de aceptación

- `CA-1` El expediente se arma en el orden del ciclo.
- `CA-2` Lo que falta se lista con su nombre, y no se inventa.
- `CA-3` Lo incompleto se marca antes de entregar.
- `CA-4` La auditoría y la memoria no entran.
- `CA-5` Lo acotado dice qué dejó fuera.
- `CA-6` El entregable trae todas las secciones, en el mismo orden.
- `CA-7` Las listas dentro de una celda salen como listas, sin marcas del texto de origen.
- `CA-8` Generar dos veces da el mismo archivo.
- `CA-9` Con documentos incompletos, avisa antes de generar y no lo impide.

Los cinco primeros son de `F-025`; los cuatro últimos, de `F-026`.

## 12. Decisiones tomadas

| Decisión | Alternativa descartada | Por qué |
|---|---|---|
| **El expediente se calcula al pedirlo** | Guardarlo | Guardarlo crea una segunda verdad que envejece (`DA-01`) |
| **El entregable se genera en formato abierto, con la librería estándar** | Instalar una biblioteca que produzca el formato binario del procesador de texto | Decidido con el usuario el 2026-08-31. Cumple `RNF-03` —sin red, sin instalar nada— y el procesador de texto lo abre y lo guarda en su formato si el cliente lo pide. Además, las tablas con listas adentro, que es el `CA-7`, salen bien sin pelear con un formato binario |
| **El orden del ciclo se declara acá**, en la §5.1 | Deducirlo del disco | El orden del disco es alfabético, y el del ciclo es el que le sirve a quien lee |
| **Lo que no encaja se lista aparte** | Meterlo en el grupo más parecido | Acomodarlo a la fuerza convierte un dato en una suposición |
| **Avisar de lo incompleto sin impedir generar** | Bloquear | La decisión de entregar algo incompleto es del usuario, no del programa |
| Los índices no entran como documentos | Incluirlos | Son la tabla de contenido de una carpeta; el expediente arma la suya |

## 13. Trazabilidad

| Funcionalidad | Requisito | Historia | Fase que lo construye |
|---|---|---|---|
| F-025 | RF-25 | [documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/HU-001-armar-el-expediente-de-un-proyecto/HU-001-armar-el-expediente-de-un-proyecto.md](../epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/HU-001-armar-el-expediente-de-un-proyecto/HU-001-armar-el-expediente-de-un-proyecto.md) | [A-EP-012-HU-001-el-expediente-se-arma-y-dice-que-le-falta](../epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/HU-001-armar-el-expediente-de-un-proyecto/A-EP-012-HU-001-el-expediente-se-arma-y-dice-que-le-falta/estado-fase.md), cerrada el 2026-08-31 |
| F-026 | RF-26 | [documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/HU-002-generar-el-entregable-de-ofimatica/HU-002-generar-el-entregable-de-ofimatica.md](../epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/HU-002-generar-el-entregable-de-ofimatica/HU-002-generar-el-entregable-de-ofimatica.md) | [A-EP-012-HU-002-el-entregable-sale-del-texto](../epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/HU-002-generar-el-entregable-de-ofimatica/A-EP-012-HU-002-el-entregable-sale-del-texto/estado-fase.md), cerrada el 2026-08-31 |

## 14. Cruces con otros módulos

- **Importación:** aporta los documentos y el tipo de cada uno. Este módulo **no vuelve a recorrer** el proyecto de origen.
- **Proyectos:** dice de qué proyecto son.
- **Auditoría:** guarda que se generó un entregable, cuándo y de qué proyecto.
- **Medición:** no se cruza. Lo que ese módulo indexa —las conversaciones— es justamente lo que no se entrega.

---

## 15. Cambios después de aprobada

| Fecha | Qué cambió | Por qué | Aprobado por |
|---|---|---|---|
| — | — | — | — |
