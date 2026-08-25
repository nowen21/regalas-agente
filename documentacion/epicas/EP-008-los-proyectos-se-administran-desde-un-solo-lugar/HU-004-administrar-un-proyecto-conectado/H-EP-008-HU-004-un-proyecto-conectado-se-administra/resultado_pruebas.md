# Resultado de Pruebas — Fase H-EP-008-HU-004: un proyecto conectado se administra   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección "qué se probó" del `funcionalidad_implementada.md`. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar: se aprobó antes y así se queda.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `H-EP-008-HU-004-un-proyecto-conectado-se-administra` |
| **HU** | [HU-004 Administrar un proyecto conectado](../HU-004-administrar-un-proyecto-conectado.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md), aprobado el 2026-08-25 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-25 |
| **Ejecutado por** | El agente, en la máquina del usuario |
| **Ambiente y versión** | Windows 11, Python 3.11.9, Django 5.2.11. Sobre `plataforma/`, sin commit todavía |

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 8 | 8 | 8 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

**86 comprobaciones automáticas**, las 62 que ya existían más 24 de esta fase. Se validaron con **seis sabotajes**, restaurando con copia y corriendo la suite completa al final, que es la lección que dejó la fase B.

**El primer sabotaje pasó en verde, y eso también es un resultado.** Borraba la ficha y la reescribía enseguida: no cambiaba nada observable, así que ninguna prueba tenía por qué fallar. **No era un hueco de las pruebas: era un sabotaje que no saboteaba.** Se cambió por uno que sí toca lo que la fase promete —borrar la documentación del proyecto— y ahí sí fallaron las dos pruebas correctas. Queda escrito porque la conclusión fácil habría sido la contraria: "una prueba falta".

---

## 2. Ejecución caso por caso

### CP-001 · Desconectar saca el proyecto, y su documentación se queda

**El problema que resuelve:** desconectar tiene que ser reversible. Si al desconectar se pierde la documentación, deja de ser deshacer y pasa a ser borrar, que es lo que la especificación descartó a propósito.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Conectar un proyecto y guardarle un documento en su carpeta | Queda el punto de partida | `analisis.md` con su contenido |
| 2 | Anotar qué decía ese documento | Queda la comparación | `# El análisis` |
| 3 | Desconectar el proyecto | Sale de los conectados | Cero conectados, uno desconectado |
| 4 | Leer ese documento otra vez | **Dice exactamente lo mismo** | Lo mismo |
| 5 | Comprobar que quedó marcado con su fecha | Tiene fecha de desconexión | La tiene |
| 6 | Comprobar que la acción quedó en la auditoría | Un registro, con quién y qué sesión | `desconectar un proyecto`, con su sesión |

**Cómo se verificó que la pareja cumple:** el paso 4 es el que decide, y no el 3. Comprobar que la carpeta **existe** no basta: una carpeta vacía también existe. Lo que prueba que no se borró nada es leer el contenido y compararlo. El sabotaje 1 lo confirmó: al borrar la documentación al desconectar, esta prueba falló y la de existencia habría pasado igual.

### CP-002 · Rehacer el índice no resucita al desconectado

**El problema que resuelve:** si la marca vive solo en la base, el proyecto vuelve solo cada vez que alguien rehace el índice, y nadie entiende por qué.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Desconectar un proyecto | Queda marcado | Marcado |
| 2 | Borrar el índice de proyectos entero | Cero filas | Cero |
| 3 | Rehacer el índice desde las fichas | Vuelve el proyecto | Volvió |
| 4 | Preguntar si está conectado | **Sigue desconectado** | Sigue desconectado |
| 5 | Abrir su ficha en el disco | Trae la fecha de desconexión, no «sigue conectado» | La trae |

**Cómo se verificó que la pareja cumple:** el paso 4 es el que prueba `DA-01` en este caso concreto. El 5 lo confirma desde el otro lado: la marca está en el texto, que es la fuente. El sabotaje 2 quitó la marca de la ficha dejando el índice intacto, y las dos pruebas fallaron: sin ellas, el proyecto habría vuelto solo la primera vez que alguien reconstruyera el índice, y eso se descubre semanas después.

### CP-003 · Renombrar cambia el nombre y no mueve la carpeta

**El problema que resuelve:** si renombrar mueve la carpeta, se rompen los enlaces y la historia. Y se ve igual de bien en la pantalla, así que nadie lo nota hasta que algo apunta a la ruta vieja.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Conectar `Nombre Viejo` y anotar dónde está su carpeta de documentación, con lo que tiene dentro | Queda la comparación | Quedó |
| 2 | Renombrarlo a `Nombre Nuevo` | La lista muestra el nombre nuevo | Lo muestra |
| 3 | Comprobar el identificador | **No cambió** | El mismo |
| 4 | Comprobar la carpeta | Existe, en la misma ruta, con lo mismo dentro | Idéntica |
| 5 | Borrar el índice y rehacerlo | El nombre nuevo está en la ficha, no solo en la base | Está |
| 6 | Intentar dejarlo sin nombre | Rechaza, y conserva el que tenía | `NombreVacio`, y sigue llamándose igual |

**Cómo se verificó que la pareja cumple:** el paso 3 es el que decide. El nombre puede cambiar bien y la carpeta haberse movido igual; lo que garantiza que no se mueva es que el identificador no se recalcule. El sabotaje 3 hizo exactamente eso —recalcularlo con el nombre nuevo— y esta prueba fue la única que lo cazó.

### CP-004 · Corregir la versión la vuelve a comprobar

**El problema que resuelve:** corregir no puede ser una puerta de atrás para meter un número que al conectar se habría rechazado.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Conectar un proyecto que no declara versión | Entra con el campo vacío | Vacío |
| 2 | Escribirle en su `CLAUDE.md` una versión que sí existe, y pedir corregir | Se relee del proyecto y se guarda | `34.1.0` |
| 3 | Conectar otro con versión válida, y cambiarle el `CLAUDE.md` a `999.0.0` | Queda el caso | Quedó |
| 4 | Pedir corregir | Rechaza | `VersionQueNoExiste` |
| 5 | Mirar qué versión le quedó | **La que tenía antes**, no vacía ni la falsa | `34.1.0` |
| 6 | Comparar la carpeta del proyecto antes y después de corregir | No cambió nada | Idéntica |

**Cómo se verificó que la pareja cumple:** el paso 5 es el que decide. Rechazar y de paso dejar el campo vacío sería perder un dato bueno por culpa de uno malo. El 6 comprueba lo que la operación **no** hace: corregir lee del proyecto, nunca le escribe.

### CP-005 · Los cuatro preguntan antes, y quedan registrados

**El problema que resuelve:** `00·N1`. Un cambio de estado que ocurre sin que el usuario lo confirme es exactamente lo que el núcleo prohíbe.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Pedir desconectar sin confirmar | Sale la pantalla de confirmación | Salió |
| 2 | Mirar qué dice esa pantalla | Dice qué va a pasar **y qué no** | Las dos cosas |
| 3 | Comprobar el proyecto y los registros | **Nada cambió todavía** | Sigue conectado, mismos registros |
| 4 | Confirmar | Ahora sí se desconecta, y queda un registro | Desconectado, un registro más |
| 5 | Pedir renombrar sin confirmar | La confirmación dice que la carpeta no se mueve | Lo dice, y el nombre no cambió |
| 6 | Pedir corregir la versión sin confirmar | La confirmación dice que solo se lee del proyecto | Lo dice |

**Cómo se verificó que la pareja cumple:** el paso 3 es el que decide: si algo hubiera cambiado antes de confirmar, la pregunta era decorativa. El paso 2 es lo que hace útil la confirmación: **decir qué NO va a pasar** es lo que permite confirmar en vez de adivinar. Sin esa mitad, el usuario que desconecta no sabe si va a perder su documentación.

### CP-006 · Los desconectados se ven, y se ve que su documentación sigue ahí

**El problema que resuelve:** si desconectar es lo mismo que desaparecer, el usuario no tiene cómo saber que quedó algo suyo guardado, ni cómo llegar a ello.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Con un proyecto conectado y otro desconectado, pedir la lista | Se ven los dos, separados | Los dos, en secciones distintas |
| 2 | Leer lo que dice la sección de desconectados | Que su documentación sigue guardada | Lo dice |
| 3 | Entrar a la pantalla del desconectado | Dice desde cuándo, y que su documentación sigue | Lo dice |

**Cómo se verificó que la pareja cumple:** el paso 2 es el que decide. Verlos en una lista aparte sin explicación dejaría al usuario preguntándose si eso es basura que hay que limpiar. El texto es lo que convierte la sección en información.

### CP-007 · Reconectar la ruta de un desconectado lo reactiva

**El problema que resuelve:** es el caso que motivó toda la fase. Conectar mal, desconectar, y volver a conectar bien. Si al reconectar se creara un proyecto nuevo, la documentación del anterior quedaría sin dueño.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Conectar un proyecto, guardarle un documento, y desconectarlo | Queda el punto de partida | Quedó |
| 2 | Volver a conectar **la misma carpeta**, con otro nombre | Vuelve el **mismo** proyecto | Mismo identificador |
| 3 | Comprobar su documento | Volvió con él | El mismo contenido |
| 4 | Contar los proyectos | Uno, no dos | Uno |
| 5 | Contar cuántos apuntan a esa ruta | Uno | Uno |
| 6 | Desde la pantalla, pedir conectar esa carpeta sin confirmar | **Avisa antes**: ese proyecto ya estuvo conectado | Avisa, y menciona empezar de cero |
| 7 | Comprobar que no se reactivó todavía | Sigue desconectado | Sigue |
| 8 | Confirmar | Ahora sí vuelve | Volvió |

**Cómo se verificó que la pareja cumple:** los pasos 6 y 7 son los que decidieron el veredicto, no el 2. Reactivar es lo correcto casi siempre, pero **no siempre es lo que el usuario quería**: si pensaba empezar de cero con esa carpeta, recibiría la historia vieja sin haberla pedido. El aviso convierte una suposición de la plataforma en una decisión suya. El sabotaje 6 quitó la reactivación y tres pruebas fallaron.

### CP-008 · Que NO pase: que desconectar toque la carpeta del proyecto

**El problema que resuelve:** es peor que al conectar. Acá el usuario cree que está quitando algo, y si la plataforma se pasa de lista podría quitarlo del lado equivocado.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Retratar la carpeta del proyecto: cada archivo, con su contenido y su fecha | Queda la comparación | Quedó |
| 2 | Desconectarlo | Sale de la lista | Salió |
| 3 | Comparar la lista de archivos | Ninguno se creó ni se borró | Idéntica |
| 4 | Comparar archivo por archivo el contenido y la fecha | Ninguno cambió | Ninguno |
| 5 | Repetir todo con renombrar | Tampoco lo toca | Retrato idéntico |
| 6 | En la corrida real, hacer la secuencia entera sobre el repositorio del estándar | Nada suyo cambia | Nada |

**Cómo se verificó que la pareja cumple:** el paso 4 es el que decide, igual que en la fase B: la lista de archivos puede ser idéntica y el contenido de uno haber cambiado. El paso 5 cubre la otra operación que escribe.

**Tabla de casos ejecutados:**

| Caso | Qué exige | Prioridad | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | `CA-01` | Crítica | 2026-08-25 | Se desconectó un proyecto con `analisis.md` guardado, y el documento siguió diciendo `# El análisis` | Aprobado | EV-01, EV-03 | — |
| CP-002 | `CA-01` | Crítica | 2026-08-25 | Se borró el índice entero y se rehizo: el proyecto volvió **desconectado**, y su ficha trae la fecha | Aprobado | EV-01 | — |
| CP-003 | `CA-02` | Crítica | 2026-08-25 | `Nombre Viejo` pasó a `Nombre Nuevo` y el identificador siguió siendo el mismo, con la carpeta idéntica | Aprobado | EV-01, EV-03 | — |
| CP-004 | `CA-03` | Crítica | 2026-08-25 | Con `999.0.0` en el `CLAUDE.md`, corregir fue rechazado y la versión quedó en `34.1.0`, la que tenía | Aprobado | EV-01 | — |
| CP-005 | `CA-04` | Crítica | 2026-08-25 | Pedir desconectar sin confirmar mostró qué pasa y qué no, y el proyecto siguió conectado con los mismos registros | Aprobado | EV-01, EV-04 | — |
| CP-006 | Transversal | Alta | 2026-08-25 | La lista mostró conectados y desconectados aparte, diciendo que la documentación de estos sigue guardada | Aprobado | EV-01 | — |
| CP-007 | La decisión del 2026-08-25 | Crítica | 2026-08-25 | Reconectar la carpeta trajo de vuelta al mismo proyecto con su `analisis.md`, avisando antes | Aprobado | EV-01, EV-03 | — |
| CP-008 | `CA-05` | Crítica | 2026-08-25 | Retrato archivo por archivo idéntico al desconectar y al renombrar | Aprobado | EV-01, EV-03 | — |

**Correspondencia con el plan:** 8 casos en el plan, 8 acá. Ninguno de más, ninguno de menos.

**Qué salió distinto de lo esperado:** nada falló. Lo que hubo fue el sabotaje que no saboteaba, explicado en la sección 1.

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que las pruebas cacen lo que dicen cazar | Seis sabotajes, restaurando con copia y corriendo la suite completa al final | Cinco cazados a la primera; el sexto pasó y resultó ser un sabotaje que no saboteaba, se corrigió y también quedó cazado |
| 2 | Que la secuencia completa sirva de verdad | Se conectó el repositorio del estándar con el nombre mal escrito (`Cimeinto`), se le guardó un documento, se renombró, se desconectó y se volvió a conectar | Todo funcionó, y el documento sobrevivió a las cuatro operaciones |
| 3 | Que la confirmación diga qué NO va a pasar | Se pidió desconectar desde la pantalla, sin confirmar | Salieron las tres cosas que no pasan, incluida la documentación |
| 4 | Que la ficha y el registro se lean sin la plataforma | `cat` sobre los dos | Los dos legibles; el registro trae las cinco acciones en orden |
| 5 | Que los dos índices se rehagan desde el texto | `reconstruir_proyectos` y `reconstruir_auditoria` | 1 proyecto y 5 acciones recuperados |
| 6 | Que los datos de prueba no quedaran | Se borraron y se rehicieron los índices | `0 proyecto(s)` y `0 acción(es)` |

---

## 4. Defectos encontrados

Ninguno en el código.

**Lo que sí apareció, y no es un defecto de esta fase:** al escribir `CP-001` se vio que `Registro.objects.last()` no sirve para saber cuál fue la última acción cuando varias caen en el mismo segundo. La marca de tiempo del registro tiene precisión de segundos, y el orden entre acciones del mismo segundo queda indeterminado. La prueba se escribió buscando por lo que se hizo en vez de por el orden, y **la limitación quedó declarada como deuda** en el documento de cierre.

**Defectos abiertos que se aceptan y por qué:** ninguno.

---

## 5. Veredicto por criterio de aceptación

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| `CA-01` desconectar saca el proyecto y deja su documentación | CP-001, CP-002 | El documento sigue con lo que tenía, y rehacer el índice no lo resucita | Sí |
| `CA-02` renombrar no mueve la carpeta | CP-003 | El identificador no cambia, y la carpeta queda idéntica | Sí |
| `CA-03` la versión corregida se vuelve a comprobar | CP-004 | Una versión inventada se rechaza y se conserva la que tenía | Sí |
| `CA-04` los cambios piden confirmación y quedan registrados | CP-005 | Nada cambia antes de confirmar, y cada uno deja un registro | Sí |
| `CA-05` que NO pase: que desconectar toque el proyecto | CP-008 | Retrato idéntico al desconectar y al renombrar | Sí |
| La decisión sobre reconectar, del 2026-08-25 | CP-007 | Reactiva el mismo proyecto, con su documentación, avisando antes | Sí |
| Transversal: los desconectados se siguen viendo | CP-006 | En su sección, diciendo que su documentación sigue guardada | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Los ocho casos con veredicto escrito | Plan de pruebas §7 | 8 | 8 | Sí |
| Ningún caso en **No cumple** sin corregir | Plan de pruebas §7 | 0 | 0 | Sí |
| Pruebas validadas con sabotaje, restaurando con copia y corriendo la suite al final | Plan de pruebas §7 | Todas las promesas | 6 sabotajes; el guion termina corriendo la suite y avisa si algo quedó roto | Sí |
| Ninguna carpeta real del usuario usada como conejillo | Plan de pruebas §7 | 0 | 0. Los proyectos de prueba se crean y se borran solos | Sí |

**Lo que no se cumplió:** nada quedó corto.

**Sobre el repositorio del estándar en la corrida real.** Se usó para la secuencia completa, incluido desconectarlo. No es un conejillo: `CP-008` comprobó que nada suyo cambia, y lo que se desconectó fue su registro en la plataforma, no la carpeta.

---

## 6. Veredicto de la fase

**Concepto:** **Cumple**.

**Justificación:** los cinco criterios de la historia quedaron probados por el paso que de verdad los decide: leer el contenido del documento y no solo comprobar que la carpeta existe; mirar el identificador y no solo el nombre; contar los registros **antes** de confirmar. La decisión sobre reconectar quedó probada con su aviso previo, que es lo que la vuelve una decisión del usuario y no una suposición de la plataforma. Las 86 comprobaciones se validaron con seis sabotajes, y el que pasó en verde se corrigió en vez de darlo por bueno.

**Qué falta para que cumpla:** nada.

**Con esto la HU-004 queda cerrada**, y con ella la épica `EP-008` en lo que toca a la versión 1: las cuatro historias tienen sus criterios probados salvo las que dependen de fases todavía sin abrir.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Salida de las 86 comprobaciones automáticas, con versiones | [evidencias/EV-01-pruebas-automaticas.txt](evidencias/EV-01-pruebas-automaticas.txt) |
| EV-02 | Los seis sabotajes, y qué prueba cazó cada uno | [evidencias/EV-02-las-pruebas-cazan-el-sabotaje.txt](evidencias/EV-02-las-pruebas-cazan-el-sabotaje.txt) |
| EV-03 | Corrida real: conectar mal, renombrar, desconectar y volver a conectar | [evidencias/EV-03-corrida-real.txt](evidencias/EV-03-corrida-real.txt) |
| EV-04 | Las pantallas y la confirmación, tal como las sirvió el servidor | [evidencias/EV-04-las-pantallas.txt](evidencias/EV-04-las-pantallas.txt) |

---

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-08-25 | 8 | 0 | Primera ejecución |
