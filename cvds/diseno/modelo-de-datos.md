# Modelo de datos y diccionario   ·   `[CAPA 3]`

**Para qué sirve este documento.** Qué guarda el sistema, dónde, con qué campos y qué significa cada uno. Un campo sin significado escrito se interpreta distinto cada vez que alguien lo lee.

> **Escrito como si no hubiera nada construido**, igual que el resto de [cvds/](../README.md). Sale de los módulos de [cvds/diseno/README.md](README.md) y de las decisiones [DA-01](decisiones-de-arquitectura.md) y [DA-07](decisiones-de-arquitectura.md).

**Estado: BORRADOR** (2026-08-24, sin aprobar).

---

## 1. Dónde vive cada cosa

> El sistema guarda en dos sitios y ninguno es un servicio: **archivos de texto** para lo que una persona lee y edita, y **una base local** solo para lo que hay que buscar. Lo que está en la base también existe como texto: la base es un índice, no la fuente.

| Qué | Dónde vive | Por qué ahí |
|---|---|---|
| Reglas, moldes y documentos del ciclo | Archivos de texto en el repositorio | Se leen sin herramienta y se versionan línea por línea (`DA-01`) |
| Registro de cada sesión | Archivos de texto en el repositorio | Es transcripción: no se reescribe, se acumula |
| Lo aprendido, para buscarlo | Base local dentro del proyecto | Buscar entre cientos de anotaciones a ojo no se sostiene (`DA-07`) |
| Versión adoptada por el proyecto | Archivo de texto en el proyecto que hereda | Tiene que poder leerse sin correr nada |

## 2. Las entidades

Las cosas de las que el sistema guarda información, y cómo se relacionan entre ellas.

| Entidad | Qué representa | Se relaciona con |
|---|---|---|
| **Regla** | Una exigencia con identificador propio | Capítulo (pertenece a uno), Comprobación (cero o una), Versión (la que la publicó y la que la derogó) |
| **Capítulo** | El grupo temático que ordena las reglas | Regla (tiene muchas) |
| **Comprobación** | El programa que revisa una regla y reporta | Regla (revisa una) |
| **Versión** | Una publicación del estándar, con su grado y su fecha | Regla (publica y deroga), Proyecto adoptante (es adoptada) |
| **Proyecto adoptante** | Un proyecto que heredó el estándar | Versión (adoptó una) |
| **Sesión** | Un tramo de trabajo con el agente, de la apertura al cierre | Anotación (deja muchas) |
| **Anotación** | Algo que la sesión dejó y no se recupera leyendo el código | Sesión (viene de una) |

## 3. El diccionario, campo por campo

### Regla

| Campo | Qué significa | Valores | Obligatorio |
|---|---|---|---|
| `identificador` | Lo que la nombra en cualquier documento. No se reutiliza ni cuando se deroga | Letra de capítulo más número, `F26`, `DOC11` | Sí |
| `capítulo` | A qué grupo pertenece | El número del capítulo | Sí |
| `enunciado` | Lo único que la regla exige, en una frase | Texto | Sí |
| `vigencia` | Si rige hoy | `vigente` o `derogada` | Sí |
| `versión que la publicó` | Desde cuándo obliga | Número de versión | Sí |
| `versión que la derogó` | Desde cuándo dejó de obligar | Número de versión, o vacío si sigue vigente | No |
| `es comprobable` | Si un programa puede revisarla sin criterio humano | `sí` o `no` | Sí |

> **`vigencia` no se borra: cambia.** Una regla derogada sigue existiendo porque hay trabajos cerrados que la citan, y un documento de hace un año tiene que poder leerse.

### Versión

| Campo | Qué significa | Valores | Obligatorio |
|---|---|---|---|
| `número` | Cuál es | Tres números separados por punto | Sí |
| `grado` | Qué tanto cambia para quien la adopta | `mayor` obliga a rehacer algo, `menor` agrega sin romper, `parche` corrige redacción | Sí |
| `fecha` | Cuándo se publicó | Año, mes y día | Sí |
| `qué cambió` | Lo que trae, dicho para quien la usa | Texto | Sí |
| `obliga a migrar` | Si un proyecto al día tiene que hacer algo | `sí` o `no` | Sí |

### Proyecto adoptante

| Campo | Qué significa | Valores | Obligatorio |
|---|---|---|---|
| `nombre` | Cómo se llama el proyecto | Texto | Sí |
| `versión adoptada` | Qué versión declara seguir | Número de versión, que **debe existir** | Sí |
| `fecha de instalación` | Cuándo se instaló | Año, mes y día | Sí |
| `desfase` | Cuántas versiones lo separan de la publicada | Se calcula, no se guarda | No |

> **`versión adoptada` se comprueba contra las versiones que existen.** Un número inventado, si es mayor que el real, apagaría el aviso de desfase en vez de dispararlo.

### Sesión

| Campo | Qué significa | Valores | Obligatorio |
|---|---|---|---|
| `identificador` | Cuál sesión es | Fecha más un nombre corto del tema | Sí |
| `abierta` | Cuándo empezó | Fecha y hora del reloj de la máquina | Sí |
| `cerrada` | Cuándo terminó | Fecha y hora, o vacío si quedó abierta | No |
| `tema` | De qué trató, en pocas palabras | Texto | Sí |

### Anotación

| Campo | Qué significa | Valores | Obligatorio |
|---|---|---|---|
| `qué pasó` | El hecho, sin interpretación | Texto | Sí |
| `por qué importa` | Qué se pierde si nadie lo lee | Texto | Sí |
| `qué se decidió` | La decisión que quedó tomada | Texto | Sí |
| `dónde queda` | El archivo donde vive el detalle | Ruta | Sí |
| `fecha` | Cuándo se escribió | Año, mes y día | Sí |
| `sesión` | De qué sesión salió | Identificador de sesión | Sí |

## 4. Qué se busca, y por eso se indexa

Las consultas que se van a hacer seguido, y por qué campo se resuelven.

| Qué consulta | Por qué campo | Para qué |
|---|---|---|
| Anotaciones sobre un tema | Texto de `qué pasó` y `qué se decidió` | Que la sesión siguiente no repita lo ya resuelto |
| Reglas de un capítulo | `capítulo` y `vigencia` | Cargar solo lo que rige |
| Qué cambió entre dos versiones | `versión que la publicó` y `versión que la derogó` | Decirle a un proyecto qué le falta adoptar |

## 5. Qué se guarda, por cuánto y quién lo lee

| Qué | Cuánto se conserva | Quién lo lee |
|---|---|---|
| Reglas y documentos | Sin caducidad: el historial es el valor | Cualquiera con el repositorio |
| Registro de sesiones | Sin caducidad | El usuario, y el agente de la sesión siguiente |
| Anotaciones | Sin caducidad, y las que dejan de ser ciertas se corrigen sin borrar la corrección | El usuario y el agente |
| Credenciales | **Nunca se guardan** | Nadie |

## 6. Lo que este modelo deja fuera a propósito

- **Datos de personas.** No hay entidad de usuario: el único nombre que aparece es el de autoría en un documento.
- **Estado de avance como dato.** Qué está hecho se lee en los documentos del ciclo, no en una tabla que habría que mantener al día por separado.
- **Métricas históricas.** Se calculan leyendo, para no tener dos versiones de la misma verdad.
