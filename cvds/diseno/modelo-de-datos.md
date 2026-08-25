# Modelo de datos y diccionario   ·   `[CAPA 3]`

**Para qué sirve este documento.** Qué guarda la plataforma, dónde, con qué campos y qué significa cada uno. Un campo sin significado escrito se interpreta distinto cada vez que alguien lo lee.

> **Escrito desde la propuesta**, igual que el resto de [cvds/](../README.md). Sale de los doce módulos de [cvds/diseno/README.md](README.md) y de [`DA-01`](decisiones-de-arquitectura.md), [`DA-02`](decisiones-de-arquitectura.md) y [`DA-07`](decisiones-de-arquitectura.md).

**Estado: APROBADO** (2026-08-24, por Ing. José Dúmar Jiménez Ruíz).

---

## 1. Dónde vive cada cosa

> **La verdad es el texto; la base es un índice.** Todo lo que está en la base existe primero como texto en el repositorio de la plataforma, una carpeta por proyecto. Perder la base no pierde información: se reconstruye leyendo.

| Qué | Dónde vive | Por qué ahí |
|---|---|---|
| Documentos del ciclo de cada proyecto | Texto, en la carpeta de su proyecto | Se leen sin la plataforma y se versionan línea por línea (`DA-02`) |
| Reglas y sus versiones | Texto, una regla por archivo | Se citan por identificador y sobreviven a la plataforma (`DA-05`) |
| Aprobaciones | Texto, junto al documento que aprueban | La firma tiene que poder leerse aunque la base no exista |
| Auditoría | Texto que solo se agrega, nunca se edita | Un registro editable no demuestra nada (`DA-08`) |
| Memoria de lo aprendido | Texto, con su índice en la base para buscar | Buscar entre cientos de anotaciones a ojo no se sostiene |
| Estado de cada proyecto y cada fase | Solo en el índice | Se calcula leyendo el texto, y se guarda para responder rápido |

## 2. Las entidades

Las cosas de las que la plataforma guarda información, y cómo se relacionan entre ellas.

| Entidad | Qué representa | Se relaciona con |
|---|---|---|
| **Proyecto** | Un proyecto administrado, con su código en alguna ruta | Documento, Fase, Configuración, Auditoría |
| **Configuración** | Qué reglas y qué moldes rigen en un proyecto | Proyecto (una por proyecto), Regla |
| **Documento** | Un documento del ciclo: planificación, análisis, fase, expediente | Proyecto, Aprobación, Versión de documento |
| **Versión de documento** | Cómo estaba un documento en un momento dado | Documento |
| **Aprobación** | Que alguien aceptó un texto exacto, con fecha | Documento, Versión de documento |
| **Épica** | Un grupo de valor dentro de un proyecto | Proyecto, Historia |
| **Historia** | Una unidad con criterios de aceptación | Épica, Fase, Funcionalidad |
| **Fase** | La unidad de trabajo que cabe en una jornada | Historia, Documento, Estación |
| **Funcionalidad** | Un ítem del inventario, con su ficha | Proyecto, Historia |
| **Regla** | Una exigencia con identificador propio | Capítulo, Comprobación, Versión de reglas |
| **Capítulo** | El grupo temático que ordena las reglas | Regla |
| **Versión de reglas** | Una publicación del cuerpo de reglas | Regla, Proyecto |
| **Comprobación** | El programa que revisa una regla | Regla, Resultado |
| **Resultado de comprobación** | Qué dio una comprobación, cuándo y sobre qué | Comprobación, Proyecto |
| **Anotación** | Algo aprendido que no se recupera leyendo el código | Proyecto, Sesión |
| **Sesión** | Un tramo de trabajo con el agente | Proyecto, Anotación |
| **Registro de auditoría** | Una acción que cambió algo | Proyecto, y la entidad que cambió |
| **Aviso** | Algo que se desvió y hay que mirar | Proyecto |

## 3. El diccionario, campo por campo

### Proyecto

| Campo | Qué significa | Valores | Obligatorio |
|---|---|---|---|
| `nombre` | Cómo se llama, para verlo en la lista | Texto | Sí |
| `ruta del código` | Dónde vive su código en la máquina | Ruta | Sí |
| `ruta viva` | Si esa ruta todavía existe | `sí` o `no`, se calcula | No |
| `versión de reglas adoptada` | Qué versión rige ahí. Debe existir | Número de versión | Sí |
| `fecha de conexión` | Cuándo se registró | Año, mes y día | Sí |
| `estado` | En qué va, calculado desde sus documentos | `sin empezar`, `en curso`, `entregado`, `archivado` | No |

> **`ruta viva` y `estado` se calculan, no se escriben.** Guardarlos a mano crea una segunda verdad que envejece.

### Documento y su versión

| Campo | Qué significa | Valores | Obligatorio |
|---|---|---|---|
| `tipo` | Qué documento del ciclo es | Uno de los tipos del ciclo | Sí |
| `proyecto` | A cuál pertenece | Identificador de proyecto | Sí |
| `contenido` | El texto | Texto | Sí |
| `espacios sin llenar` | Cuántos huecos le faltan | Número, se calcula | No |
| `huella del contenido` | Un resumen corto del texto, para saber si cambió | Cadena calculada | Sí |
| `guardado` | Cuándo se escribió esta versión | Fecha y hora | Sí |

> **La huella es lo que permite que una aprobación caduque sola.** Si el texto cambia, la huella cambia, y la firma deja de corresponder.

### Aprobación

| Campo | Qué significa | Valores | Obligatorio |
|---|---|---|---|
| `documento` | Qué se aprobó | Identificador de documento | Sí |
| `huella aprobada` | La huella del texto en el momento de firmar | Cadena | Sí |
| `quién` | Quién aprobó | Texto | Sí |
| `cuándo` | Fecha de la firma | Año, mes y día | Sí |
| `vigente` | Si la huella actual sigue siendo la aprobada | `sí` o `no`, se calcula | No |

### Fase

| Campo | Qué significa | Valores | Obligatorio |
|---|---|---|---|
| `nombre` | El nombre de la fase, con su historia | Texto | Sí |
| `historia` | De qué historia sale | Identificador de historia | Sí |
| `estación` | En qué punto del recorrido va | Número de estación | Sí |
| `puerta pendiente` | Qué falta para pasar a la siguiente | Texto, se calcula | No |
| `abierta` | Cuándo empezó | Año, mes y día | Sí |
| `cerrada` | Cuándo terminó | Año, mes y día, o vacío | No |

### Regla y versión de reglas

| Campo | Qué significa | Valores | Obligatorio |
|---|---|---|---|
| `identificador` | Lo que la nombra en cualquier documento. No se reutiliza | Letra de capítulo más número | Sí |
| `capítulo` | A qué grupo pertenece | Número de capítulo | Sí |
| `enunciado` | Lo único que exige, en una frase | Texto | Sí |
| `vigencia` | Si rige hoy | `vigente` o `derogada` | Sí |
| `publicada en` | Desde qué versión obliga | Número de versión | Sí |
| `derogada en` | Desde qué versión dejó de obligar | Número de versión, o vacío | No |
| `es comprobable` | Si un programa puede revisarla sin criterio | `sí` o `no` | Sí |
| `grado` de la versión | Qué tanto cambia para quien la adopta | `mayor`, `menor`, `parche` | Sí |
| `obliga a migrar` | Si un proyecto al día tiene que hacer algo | `sí` o `no` | Sí |

### Registro de auditoría

| Campo | Qué significa | Valores | Obligatorio |
|---|---|---|---|
| `qué se hizo` | La acción | `creó`, `editó`, `aprobó`, `publicó`, `trajo`, `derogó`, `cerró` | Sí |
| `sobre qué` | Qué entidad cambió | Tipo e identificador | Sí |
| `quién` | Quién la hizo | `usuario` o `agente` | Sí |
| `cuándo` | Fecha y hora | Fecha y hora | Sí |
| `qué cambió` | La diferencia, en corto | Texto | Sí |
| `proyecto` | En cuál ocurrió | Identificador de proyecto, o vacío si fue global | No |
| `sesión` | En qué sesión se hizo, para leer después lo que dejó escrito | Identificador de sesión, o vacío | No |

> **Este registro solo se agrega.** No hay campo para editarlo ni para borrarlo: `DA-08`.

> **Lo que la sesión dejó escrito se enlaza, y la conversación no se guarda.** Decidido el 2026-08-25: la acción responde qué se hizo, y el resumen de la sesión responde por qué. La transcripción sigue guardándose aparte, fuera de la auditoría.

### Anotación de memoria

| Campo | Qué significa | Valores | Obligatorio |
|---|---|---|---|
| `qué pasó` | El hecho, sin interpretación | Texto | Sí |
| `por qué importa` | Qué se pierde si nadie lo lee | Texto | Sí |
| `qué se decidió` | La decisión que quedó tomada | Texto | Sí |
| `dónde queda` | El documento donde vive el detalle | Ruta | Sí |
| `proyecto` | De cuál salió | Identificador de proyecto | Sí |
| `vigente` | Si sigue siendo cierta | `sí` o `no` | Sí |
| `corrige a` | Qué anotación reemplaza | Identificador de anotación, o vacío | No |

> **Lo que deja de ser cierto no se borra: se marca y se enlaza con lo que lo corrige.** Así la historia de una decisión se puede leer completa.

## 4. Qué se busca, y por eso se indexa

Las consultas que se van a hacer seguido, y por qué campo se resuelven.

| Qué consulta | Por qué campo | Para qué |
|---|---|---|
| Estado de todos los proyectos | `estado` y `ruta viva` de Proyecto | La pantalla de inicio, que debe responder en menos de un segundo |
| Documentos de un proyecto | `proyecto` y `tipo` de Documento | Armar el expediente |
| Qué está aprobado | `huella aprobada` contra `huella del contenido` | Saber qué firma sigue vigente |
| Reglas vigentes de un capítulo | `capítulo` y `vigencia` de Regla | Entregarle al agente solo lo que rige |
| Qué cambió entre dos versiones | `publicada en` y `derogada en` | Decirle a un proyecto qué le falta adoptar |
| Anotaciones sobre un tema | Texto de la Anotación, con `vigente` | Que la sesión siguiente no repita lo resuelto |
| Auditoría por proyecto y fecha | `proyecto` y `cuándo` | Rastrear qué se hizo |

## 5. Qué se guarda, por cuánto y quién lo lee

| Qué | Cuánto se conserva | Quién lo lee |
|---|---|---|
| Documentos y sus versiones | Sin caducidad: el historial es el valor | El usuario y el agente |
| Aprobaciones | Sin caducidad, incluidas las caducadas | El usuario, y quien reciba el proyecto |
| Auditoría | Sin caducidad, y no se edita | El usuario |
| Memoria | Sin caducidad; lo que deja de ser cierto se marca | El usuario y el agente |
| Credenciales | **Nunca se guardan** | Nadie |

## 6. Lo que este modelo deja fuera a propósito

- **Datos de personas.** No hay entidad de usuario: `quién` es `usuario` o `agente`, y nada más. El día que haya varios usuarios, esta decisión se rehace.
- **El contenido del código de los proyectos.** La plataforma guarda documentación, no código.
- **La conversación de las sesiones.** Se guarda lo que la sesión dejó, no lo que se dijo: `DA-08`.
- **Métricas históricas calculadas.** Se recalculan leyendo, para no tener dos versiones de la misma verdad.
