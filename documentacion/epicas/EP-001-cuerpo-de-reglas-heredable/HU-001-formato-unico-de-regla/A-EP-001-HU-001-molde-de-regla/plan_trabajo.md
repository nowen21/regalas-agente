# Plan de Trabajo — Fase A-EP-001-HU-001-molde-de-regla

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en [HU-001](../HU-001-formato-unico-de-regla.md); el detalle de las pruebas, en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase; lo que dieron al correrlas, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-001-HU-001-molde-de-regla` |
| **Épica** | [EP-001](../../epica.md) |
| **HU** | [HU-001 Formato único para escribir una regla](../HU-001-formato-unico-de-regla.md) |
| **Módulo** | Cuerpo de reglas |
| **Especificación del módulo** | No hay especificación aparte. El entregable es texto normativo, no código, y su especificación son los criterios de aceptación de la HU. Confirmarlo antes de arrancar (duda 1 de §2.7) |
| **Fecha apertura** | 2026-08-13 |
| **Rama** | `feature/A-EP-001-HU-001-molde-de-regla` |

**Origen:** funcionalidad nueva. No existe nada del cuerpo de reglas. Esta es la primera fase del proyecto y define la forma sobre la que se escribe todo lo demás.

**Por qué una sola fase para los tres CA.** Los tres validan el mismo documento, el molde, y ninguno se puede probar sin él. Partirlos daría fases que existen solo para cumplir la nomenclatura, que es justo lo que prohíbe `02·F12.10`.

**CA de la HU que cubre esta fase**

| CA de HU-001 | Qué valida | Estado |
|---|---|---|
| CA-01 | Una regla escrita con el molde queda citable y comprobable | Pendiente |
| CA-02 | Una regla que exige dos cosas no pasa | Pendiente |
| CA-03 | Un identificador repetido se detecta | Pendiente |

## 1. Objetivo y alcance

**Objetivo.** Dejar escrito el molde con que se escribe toda regla del estándar, y probarlo escribiendo dos reglas reales con él.

**Resumen de CA a cubrir**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Camino feliz: una regla con el molde queda citable | Funcional | Media |
| CA-02 | La regla que exige dos cosas se detecta | Funcional | Baja |
| CA-03 | El identificador repetido se detecta | Funcional | Baja |
| RNF-01 | El molde lo entiende quien no sabe del tema | No funcional | Media |

**Fuera de alcance**

- El contenido de las reglas del estándar. Acá solo se define la forma. El contenido es HU-003, HU-004 y HU-005.
- El programa que comprueba el molde. Es de EP-004, y esta fase solo deja marcado qué partes son comprobables.
- El procedimiento para agregar una regla. Es HU-007.
- La derogación. Es HU-008.
- El número de versión del cuerpo. Es EP-002.

## 2. Análisis previo

### 2.1 Archivos que se crean o modifican

| Archivo | Tipo | Qué es |
|---|---|---|
| `base/20-meta-reglas/base.md` | Nuevo | El capítulo que agrupa las reglas sobre reglas, con su índice |
| `base/20-meta-reglas/estructura-regla.md` | Nuevo | El molde: qué partes tiene una regla y cuáles son obligatorias |
| `base/20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md` | Nuevo | La regla del identificador y de la cita |
| `base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md` | Nuevo | La regla que obliga al molde |
| `base/README.md` | Nuevo | Índice de capítulos, para que el capítulo 20 tenga dónde aparecer |

Las dos reglas de prueba del CA-01 son `M4` y `M5` mismas: se escriben con el molde que definen, así que el molde se prueba contra sí mismo. No se crean reglas de mentira que después haya que borrar.

### 2.2 Matriz de dependencias del refactor

No aplica porque no existe código ni documento previo al que esta fase le cambie el contrato. Es la primera fase del proyecto.

### 2.3 Rutas y control de acceso

No aplica porque el entregable son archivos de texto del repositorio. No hay sistema con usuarios ni endpoints.

### 2.4 Punto de entrada en la interfaz

No aplica porque la fase no introduce interfaz. El entregable se lee abriendo los archivos.

### 2.5 Permisos o roles a sembrar

Ninguno. El control de quién edita lo da el acceso al repositorio.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El molde vive en un archivo aparte del capítulo, no dentro de una regla | Meter el molde completo en el cuerpo de `M5` | El cuerpo de una regla es corto. Una lista larga adentro haría ilegible la regla y rompería su propio molde |
| El identificador lleva prefijo de letra por capítulo y número correlativo, y se cita como capítulo más identificador | Numerar las reglas de corrido en todo el estándar | Con numeración corrida, agregar una regla en el capítulo 3 recorre todos los números siguientes, y `M4` exige que el identificador sea estable |
| El identificador no repite el prefijo del capítulo | Repetirlo para que la regla se lea sola | La cita ya nombra el capítulo. Repetirlo alarga cada referencia sin agregar información |
| Cada regla lleva ejemplo incorrecto y correcto en un bloque de código | Describir el error en prosa | El bloque se lee de un vistazo y se puede comparar renglón contra renglón |
| El molde marca qué partes puede comprobar un programa | Decidirlo después, cuando se escriban las comprobaciones | Decidirlo al final obliga a releer todas las reglas una por una |

Estas decisiones se registran como señal cuando exista la memoria (EP-006). Mientras tanto quedan acá.

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | Si un entregable de texto normativo necesita especificación aparte o si la HU con sus CA hace las veces de especificación | Usuario | Pendiente |
| 2 | Si el capítulo de reglas sobre reglas se numera 20, al final, o 00, al principio | Usuario | Pendiente |
| 3 | Cuántas partes del molde son obligatorias y cuáles opcionales cuando la regla no admite ejemplo | Usuario | Pendiente |

Ninguna tarea de construcción arranca con una duda abierta que la bloquee. Las dudas 2 y 3 bloquean T-02 en adelante.

## 3. Desglose de tareas por criterio de aceptación

Sin columna de estado, a propósito: este plan se aprueba y no se vuelve a tocar. El avance en vivo va en [estado-fase.md](estado-fase.md) §1.2, y la verificación de qué se hizo, en el documento de cierre §2.2.

### CA-01 — Una regla escrita con el molde queda citable y comprobable

| ID | Tarea | Est. | Depende de | Evidencia |
|---|---|:--:|---|---|
| T-01 | Resolver las tres dudas de §2.7 con el usuario | 1 h | — | EV-01 |
| T-02 | Escribir el molde: partes obligatorias, opcionales y qué va en cada una | 3 h | T-01 | EV-02 |
| T-03 | Escribir la regla del identificador y de la forma de citar entre capítulos | 2 h | T-02 | EV-03 |
| T-04 | Escribir la regla que obliga al molde | 2 h | T-02 | EV-03 |
| T-05 | Crear el capítulo con su índice y el índice de capítulos | 1 h | T-03, T-04 | EV-04 |
| T-06 | Citar una regla desde otro documento y comprobar que el enlace llega | 1 h | T-05 | EV-05 |

### CA-02 — Una regla que exige dos cosas no pasa

| ID | Tarea | Est. | Depende de | Evidencia |
|---|---|:--:|---|---|
| T-07 | Escribir en el molde la exigencia de una sola cosa por regla, con su ejemplo | 1 h | T-02 | EV-02 |
| T-08 | Escribir a propósito una regla con dos exigencias y revisarla contra el molde | 1 h | T-07 | EV-06 |
| T-09 | Partirla en dos y verificar que ambas pasan | 1 h | T-08 | EV-06 |

### CA-03 — Un identificador repetido se detecta

| ID | Tarea | Est. | Depende de | Evidencia |
|---|---|:--:|---|---|
| T-10 | Escribir en el molde cómo se elige un identificador libre | 1 h | T-03 | EV-02 |
| T-11 | Duplicar a propósito un identificador y revisar el capítulo | 1 h | T-10 | EV-07 |

### Requisitos no funcionales

| ID | Tarea | Categoría | Est. | Evidencia |
|---|---|---|:--:|---|
| T-12 | Releer el molde y las dos reglas contra la exigencia de que lo entienda quien no sabe del tema | Legibilidad | 1 h | EV-08 |
| T-13 | Marcar en el molde qué partes puede comprobar un programa | Comprobabilidad | 1 h | EV-02 |

**Total estimado:** 17 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-04, T-05, T-06.

**En paralelo:** T-07 y T-10 pueden avanzar apenas exista el borrador del molde en T-02. T-12 y T-13 se hacen al final, sobre lo escrito.

Solo se tocan los archivos declarados en §2.1. Si aparece uno nuevo, se pausa, se reporta y se amplía el plan con visto bueno. No se edita por iniciativa.

## 5. Verificación de criterios de aceptación

| CA | Método de verificación | Evidencia | Estado |
|---|---|---|---|
| CA-01 | Se escriben dos reglas con el molde y se cita una desde otro documento | EV-02, EV-03, EV-05 | Pendiente |
| CA-02 | Se escribe una regla doble a propósito y se revisa contra el molde | EV-06 | Pendiente |
| CA-03 | Se duplica un identificador a propósito y se revisa el capítulo | EV-07 | Pendiente |
| RNF-01 | Relectura contra la exigencia de legibilidad | EV-08 | Pendiente |

**Registro de evidencias**

| ID | Tipo | Dónde queda |
|---|---|---|
| EV-01 | Respuestas del usuario a las tres dudas | En este plan, §2.7 actualizado |
| EV-02 | El molde escrito | `base/20-meta-reglas/estructura-regla.md` |
| EV-03 | Las dos reglas escritas con el molde | `base/20-meta-reglas/reglas/` |
| EV-04 | Los índices del capítulo y de la base | `base/20-meta-reglas/base.md`, `base/README.md` |
| EV-05 | La cita que llega a la regla | Enlace probado, anotado en el cierre de la fase |
| EV-06 | La regla doble y sus dos partes | Anotado en el cierre de la fase |
| EV-07 | El identificador duplicado y su corrección | Anotado en el cierre de la fase |
| EV-08 | Resultado de la relectura de legibilidad | Anotado en el cierre de la fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | El repositorio del estándar, en una rama aparte. No hay base de datos ni datos reales |
| Usuarios de prueba | No aplica porque no hay sistema con usuarios |
| Datos precargados | No aplica. La prueba se hace sobre los propios documentos |

El detalle de casos va en el `plan_pruebas` de esta misma fase.

## 7. Reversión

Todo lo de esta fase son archivos nuevos en una rama aparte. Si el molde no sirve, se descarta la rama y no queda nada que deshacer. No hay cambio destructivo ni datos que restaurar.

## 8. Producción y migración

No aplica porque nada de esto está en producción todavía. Es la primera fase del proyecto y no hay proyecto que haya adoptado el estándar.

## 9. Reglas aplicadas

Ninguna del estándar, porque esta fase es la que empieza a escribirlo. Es el único caso en que la casilla queda vacía por motivo legítimo, y conviene dejarlo dicho para que no se lea como un olvido.

Lo que sí guía la fase son los criterios de aceptación de [HU-001](../HU-001-formato-unico-de-regla.md) y el alcance de [EP-001](../../epica.md).

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Las tres dudas de §2.7 sin resolver | Bloquea T-02 en adelante, que es casi toda la fase | Resolverlas con el usuario en T-01, antes de escribir nada | Abierto |
| R-01 | Que el molde salga tan estricto que escribir una regla se vuelva pesado | Se descubriría tarde, cuando ya haya decenas de reglas escritas | Probarlo con dos reglas reales dentro de esta misma fase, no después | Abierto |
| R-02 | Que el molde no aguante una regla que sí exige varias cosas relacionadas | Obligaría a reescribir el molde con reglas ya escritas encima | Definir desde el molde el anexo, para lo que no cabe en el cuerpo de la regla | Abierto |
| R-03 | Elegir mal el esquema de identificadores y tener que renumerar después | Alto: renumerar rompe toda cita hecha hasta ese momento | Decidirlo en T-01 con el usuario y dejarlo escrito en §2.6 antes de escribir la primera regla | Abierto |

## 11. Definition of Done

- [ ] Los tres CA de §0 verificados con su evidencia
- [ ] El molde entendible por quien no sabe del tema
- [ ] Las dos reglas escritas cumplen el molde que ellas mismas definen
- [ ] Una cita desde otro documento llega a la regla
- [ ] Los índices del capítulo y de la base están al día
- [ ] Las partes comprobables del molde están marcadas
- [ ] Las decisiones de §2.6 quedan escritas donde se puedan recuperar después
- [ ] Rama lista para el commit único de la fase
- [ ] Aprobada por el usuario

## 12. Cierre

No se escribe acá. El cierre de la fase vive en el `funcionalidad_implementada.md`: qué se hizo de cada tarea, qué se probó, qué se decidió y qué deuda quedó. Este plan se queda como se aprobó, para poder comparar lo que se dijo contra lo que pasó.
