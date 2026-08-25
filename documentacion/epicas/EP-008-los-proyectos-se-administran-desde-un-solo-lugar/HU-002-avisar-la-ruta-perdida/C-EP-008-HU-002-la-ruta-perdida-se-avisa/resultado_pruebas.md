# Resultado de Pruebas — Fase C-EP-008-HU-002: la ruta perdida se avisa   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección "qué se probó" del `funcionalidad_implementada.md`. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar: se aprobó antes y así se queda.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `C-EP-008-HU-002-la-ruta-perdida-se-avisa` |
| **HU** | [HU-002 Avisar cuando la ruta de un proyecto se pierde](../HU-002-avisar-la-ruta-perdida.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md), aprobado el 2026-08-25 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-25 |
| **Ejecutado por** | El agente, en la máquina del usuario |
| **Ambiente y versión** | Windows 11, Python 3.11.9, Django 5.2.11. Sobre `plataforma/`, sin commit todavía |

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 7 | 7 | 7 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

**103 comprobaciones automáticas**, las 86 que ya existían más 17 de esta fase.

**El sabotaje encontró una prueba floja, y esta vez sí lo era.** Uno de los seis sabotajes pasó en verde: el que hacía que corregir la ruta **guardara la versión nueva en el índice pero dejara la vieja en la ficha**. La lección de la fase H obliga a preguntar primero si el sabotaje cambia algo observable, y se comprobó: sí lo cambiaba. Al rehacer el índice volvía la versión vieja.

**Era una prueba que faltaba, no un sabotaje inofensivo.** La prueba miraba el objeto que devuelve la función, y ese traía la versión correcta. Se reforzó para que borre el índice, lo rehaga desde el texto, y compruebe ahí. Con eso el sabotaje quedó cazado.

---

## 2. Ejecución caso por caso

### CP-001 · La ruta que dejó de existir se marca, y se nombra

**El problema que resuelve:** un aviso que dice «esa ruta no existe» sin decir cuál obliga al usuario a comparar de memoria. Con la ruta a la vista se ve enseguida si fue un renombre, un movimiento o un disco sin montar.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Conectar un proyecto de mentira | Queda registrado | Quedó |
| 2 | Borrar su carpeta de código | La ruta queda perdida | Borrada |
| 3 | Pedir los avisos de ese proyecto | Hay uno, y **nombra la ruta que se buscó** | La nombra completa |
| 4 | Abrir la lista | El proyecto aparece marcado, con enlace para corregirlo | `Esa carpeta ya no está`, con su enlace |
| 5 | Entrar a su pantalla | El aviso trae la ruta | La trae |

**Cómo se verificó que la pareja cumple:** el paso 3 es el que decide, y es el que exige `RN-2`. Los pasos 4 y 5 comprueban que el aviso llega a las dos pantallas, no solo a una. **Este caso prueba código que ya existía**: `ruta_viva` salió de la fase B sin que nadie estuviera pensando en esta historia, y nunca se había probado contra ella. Lo que la fase agregó fue que el aviso nombre la ruta.

### CP-002 · Con la ruta perdida, su documentación sigue a la vista

**El problema que resuelve:** si la documentación desapareciera con la ruta, la plataforma estaría guardando en el sitio equivocado, y perder una carpeta costaría el doble.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Conectar un proyecto y guardarle un documento | Queda el punto de partida | `analisis.md` con su contenido |
| 2 | Borrar su carpeta de código entera | La ruta se pierde | `ruta_viva` da falso |
| 3 | Leer su documento | **Sigue diciendo lo mismo** | `# Lo suyo` |

**Cómo se verificó que la pareja cumple:** el paso 3 lo decide leyendo el contenido, no comprobando que el archivo exista. Es la misma exigencia que la fase H aplicó a desconectar: una carpeta vacía también existe.

### CP-003 · Corregir la ruta quita el aviso, y queda registrado

**El problema que resuelve:** de nada sirve avisar si no se puede arreglar. Y un registro que no dice de dónde a dónde no sirve para rastrear el cambio meses después.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Conectar un proyecto y borrar su carpeta | La ruta se pierde | Perdida |
| 2 | Corregir a una carpeta que sí existe | La ruta cambia | Cambió |
| 3 | Pedir los avisos | **Ya no hay aviso de ruta perdida** | Ninguno |
| 4 | Borrar el índice y rehacerlo desde las fichas | La ruta nueva está en el texto, no solo en la base | Está |
| 5 | Buscar el registro de auditoría | Trae **la ruta vieja y la nueva**, y la sesión | Las dos, con la sesión |
| 6 | Apuntar un proyecto a su propia ruta | No se rechaza a sí mismo | No se rechaza |

**Cómo se verificó que la pareja cumple:** el paso 4 es el que prueba que la corrección sobrevive, y el 5 el que la hace rastreable. El paso 6 cubre el caso que rompe una comprobación de duplicados escrita sin cuidado: el proyecto chocando consigo mismo.

### CP-004 · La ruta nueva se comprueba igual que al conectar

**El problema que resuelve:** si corregir aceptara lo que conectar rechaza, sería una puerta de atrás. Es el mismo hueco que la fase H cerró para la versión de reglas.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Corregir a una ruta que no existe | Rechaza, nombrando la ruta | `No existe la carpeta «…»` |
| 2 | Mirar qué ruta le quedó | **La que tenía**, no vacía | La que tenía |
| 3 | Corregir a una carpeta que ya tiene otro proyecto | Rechaza, diciendo cuál la tiene | `ya está registrada por el proyecto «El Primero»` |
| 4 | Mirar la ruta otra vez | Sigue la suya | Sigue |
| 5 | Corregir a una carpeta cuyo `CLAUDE.md` declara `999.0.0` | Rechaza | `VersionQueNoExiste` |
| 6 | Desde la pantalla, corregir a una ruta inventada | El rechazo se ve | `No existe la carpeta` |

**Cómo se verificó que la pareja cumple:** los pasos 2 y 4 son los que deciden. Rechazar y de paso dejar el campo vacío perdería un dato bueno por culpa de uno malo, y el usuario quedaría peor que antes de intentar corregir.

### CP-005 · Corregir la ruta relee la versión de reglas

**El problema que resuelve:** la carpeta cambió, así que lo que declara puede ser otra cosa. Dejar la versión vieja sería afirmar sobre lo que no se leyó.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Conectar un proyecto cuyo `CLAUDE.md` declara `34.1.0` | Queda con esa versión | `34.1.0` |
| 2 | Corregir la ruta a una carpeta **sin** `CLAUDE.md` | La versión que devuelve la función es vacía | Vacía |
| 3 | Borrar el índice y rehacerlo desde la ficha | **La versión sigue vacía** | Vacía |

**Cómo se verificó que la pareja cumple:** el paso 3 es el que decide, y es el que faltaba. Con solo los pasos 1 y 2, el sabotaje que dejaba la versión vieja en la ficha pasaba en verde: el objeto devuelto traía lo correcto y el texto no. Al rehacer el índice volvía la versión vieja, y nadie se enteraba hasta mucho después.

### CP-006 · Cincuenta proyectos listan bajo un segundo

**El problema que resuelve:** comprobar la existencia de cada ruta al listar es trabajo de disco, y el disco es lo lento. `RNF-02` pone el límite en un segundo.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Conectar cincuenta proyectos de mentira | Quedan los cincuenta | 50 |
| 2 | Pedir la lista, midiendo el tiempo | Responde | 200 |
| 3 | Comparar con el límite | Menos de un segundo | **0.010 s** |
| 4 | Escribir el número | Queda en la salida de la prueba, no solo en este documento | Queda |

**Cómo se verificó que la pareja cumple:** el paso 4 es lo que hace útil la medición mañana. Un «cumple» sin el número no sirve para comparar cuando haya doscientos proyectos o cuando alguien mueva la carpeta a un disco de red. El margen es amplio: **0.010 s contra un límite de 1 s**, casi cien veces por debajo.

### CP-007 · Que NO pase: que corregir toque las carpetas

**El problema que resuelve:** «corregir la ruta» suena parecido a «mover el proyecto», y esa confusión escrita en código movería el código de verdad.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Retratar **las dos** carpetas: la vieja y la nueva, archivo por archivo | Queda la comparación | Quedó |
| 2 | Corregir la ruta de la vieja a la nueva | La ficha cambia | Cambió |
| 3 | Comparar la carpeta vieja | **No cambió** | Idéntica |
| 4 | Comparar la carpeta nueva | Tampoco | Idéntica |
| 5 | Repetir con una corrección que se rechaza | Ninguna de las dos cambia | Idénticas |

**Cómo se verificó que la pareja cumple:** el paso 3 es el que decide, y es el que se olvida. Mirar solo la carpeta nueva dejaría pasar el caso peor: que la plataforma **mueva** el código de la vieja a la nueva. El sabotaje 5 hizo exactamente eso, y esta prueba lo cazó.

**Tabla de casos ejecutados:**

| Caso | Qué exige | Prioridad | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | `CA-01` | Crítica | 2026-08-25 | Se borró la carpeta de un proyecto y el aviso salió nombrando la ruta completa que se buscó | Aprobado | EV-01, EV-03 | — |
| CP-002 | `CA-02` | Crítica | 2026-08-25 | Con la carpeta de código borrada, `analisis.md` siguió diciendo `# Lo suyo` | Aprobado | EV-01, EV-03 | — |
| CP-003 | `CA-03` | Crítica | 2026-08-25 | Corregida la ruta, el aviso desapareció y el registro trae la vieja y la nueva | Aprobado | EV-01, EV-03 | — |
| CP-004 | `CA-03` | Crítica | 2026-08-25 | Ruta inventada, ruta de otro proyecto y versión `999.0.0`: las tres rechazadas, conservando la ruta que tenía | Aprobado | EV-01, EV-03 | — |
| CP-005 | La decisión del plan §2.6 | Alta | 2026-08-25 | Al mover a una carpeta sin `CLAUDE.md`, la versión quedó vacía **también en la ficha**, comprobado rehaciendo el índice | Aprobado | EV-01, EV-02 | — |
| CP-006 | `RNF-02` | Alta | 2026-08-25 | Cincuenta proyectos conectados; listar tardó **0.010 s** contra un límite de 1 s | Aprobado | EV-01 | — |
| CP-007 | `RN-1` de `HU-001` | Crítica | 2026-08-25 | Retrato idéntico de la carpeta vieja y la nueva, al corregir y al rechazar | Aprobado | EV-01 | — |

**Correspondencia con el plan:** 7 casos en el plan, 7 acá.

**Qué salió distinto de lo esperado:** nada falló en el código. Lo que falló fue una prueba, y se reforzó antes de cerrar.

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que las pruebas cacen lo que dicen cazar | Seis sabotajes, restaurando con copia y corriendo la suite completa al final | Cinco cazados a la primera. El sexto pasó, se comprobó que sí saboteaba, y se reforzó la prueba |
| 2 | Que la secuencia real funcione | Se conectó un proyecto de mentira, se le guardó un documento, **se movió su carpeta de verdad**, y se corrigió la ruta | El aviso nombró la ruta vieja, el documento sobrevivió, y la corrección quedó registrada de dónde a dónde |
| 3 | Que corregir a una ruta inventada conserve la que tenía | Se intentó antes de corregir bien | Rechazó y conservó |
| 4 | Que el registro sea legible sin la plataforma | `cat` sobre el archivo del mes | Las tres acciones, con las dos rutas en la corrección |
| 5 | Que los datos de prueba no quedaran | Se borraron y se rehicieron los índices | `0 proyecto(s)` y `0 acción(es)` |

---

## 4. Defectos encontrados

Ninguno en el código.

**Un defecto en una prueba**, encontrado por el sabotaje: `CP-005` comprobaba la versión releída mirando el objeto que devuelve la función, y no el texto de la ficha. Un código que guardara la versión nueva en el índice y la vieja en la ficha habría pasado, y al rehacer el índice habría vuelto la vieja. La prueba se reforzó para borrar el índice, rehacerlo desde el texto y comprobar ahí.

**Defectos abiertos que se aceptan y por qué:** ninguno.

---

## 5. Veredicto por criterio de aceptación

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| `CA-01` la ruta que dejó de existir se avisa | CP-001 | Marcada en la lista, y el aviso nombra la ruta | Sí |
| `CA-02` su documentación se sigue viendo | CP-002 | El documento sigue con lo que tenía | Sí |
| `CA-03` volver a apuntar la ruta quita el aviso | CP-003, CP-004 | El aviso desaparece, y lo que no debe entrar se rechaza conservando la ruta anterior | Sí |
| `RN-2` el aviso dice qué ruta se buscó | CP-001 paso 3 | La nombra completa | Sí |
| Transversal `RNF-02` | CP-006 | 0.010 s con cincuenta proyectos | Sí |
| `RN-1` de `HU-001`: no se toca el código | CP-007 | Ninguna de las dos carpetas cambia | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Los siete casos con veredicto escrito | Plan de pruebas §7 | 7 | 7 | Sí |
| Ningún caso en **No cumple** sin corregir | Plan de pruebas §7 | 0 | 0 | Sí |
| El número de la medición escrito, aunque cumpla | Plan de pruebas §7 | El dato | 0.010 s, en la salida de la prueba y acá | Sí |
| Pruebas validadas con sabotaje, restaurando con copia y corriendo la suite al final | Plan de pruebas §7 | Todas las promesas | 6 sabotajes; el que pasó destapó una prueba floja | Sí |
| Ninguna carpeta real del usuario borrada ni usada como conejillo | Plan de pruebas §7 | 0 | 0. Las carpetas que se borraron y se movieron son todas de mentira | Sí |
| Probar también lo que ya estaba construido | Plan de pruebas §3.2 | `CA-01` y `CA-02` | Los dos, con `CP-001` y `CP-002` | Sí |

**Lo que no se cumplió:** nada quedó corto.

---

## 6. Veredicto de la fase

**Concepto:** **Cumple**.

**Justificación:** los tres criterios de la historia quedaron probados por el paso que de verdad los decide: que el aviso **nombre** la ruta y no solo avise; que la ruta anterior **se conserve** cuando la corrección se rechaza; que la versión releída quede **en la ficha** y no solo en el índice. La medición de `RNF-02` salió con margen amplio y con su número escrito. Y `CP-001` y `CP-002` probaron por primera vez código que existía desde la fase B sin haberse probado nunca contra esta historia.

**Qué falta para que cumpla:** nada. **Con esto la HU-002 queda cerrada.**

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Salida de las 103 comprobaciones automáticas, con la medición de `CP-006` | [evidencias/EV-01-pruebas-automaticas.txt](evidencias/EV-01-pruebas-automaticas.txt) |
| EV-02 | Los seis sabotajes, y qué prueba cazó cada uno | [evidencias/EV-02-las-pruebas-cazan-el-sabotaje.txt](evidencias/EV-02-las-pruebas-cazan-el-sabotaje.txt) |
| EV-03 | Corrida real: se mueve la carpeta de un proyecto y se corrige la ruta | [evidencias/EV-03-corrida-real.txt](evidencias/EV-03-corrida-real.txt) |

---

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-08-25 | 7 | 0 | Primera ejecución |
