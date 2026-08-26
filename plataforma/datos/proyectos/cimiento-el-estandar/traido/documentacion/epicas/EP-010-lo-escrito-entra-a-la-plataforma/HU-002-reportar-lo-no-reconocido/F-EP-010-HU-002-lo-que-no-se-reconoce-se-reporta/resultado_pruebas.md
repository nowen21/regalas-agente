# Resultado de Pruebas — Fase F-EP-010-HU-002: lo que no se reconoce se reporta   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección "qué se probó" del `funcionalidad_implementada.md`. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar: se aprobó antes y así se queda.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `F-EP-010-HU-002-lo-que-no-se-reconoce-se-reporta` |
| **HU** | [HU-002 Reportar lo no reconocido](../HU-002-reportar-lo-no-reconocido.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md), aprobado el 2026-08-25 |
| **Ciclo** | 2. El 1 encontró un defecto, se corrigió y se corrió completo otra vez |
| **Fecha de ejecución** | 2026-08-25 |
| **Ejecutado por** | El agente, en la máquina del usuario |
| **Ambiente y versión** | Windows 11, Python 3.11.9, Django 5.2.11. Sobre `plataforma/`, sin commit todavía |

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 8 | 8 | 7 | 1 | 0 | 0 |
| 2 | 8 | 8 | 8 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

**165 comprobaciones automáticas**, las 145 que ya existían más 20 de esta fase. Se validaron con **ocho sabotajes**, y los ocho quedaron cazados a la primera.

**El reporte real de este repositorio:**

```
Documentos que entraron    | 1000
Que NO entraron            |    1     →  cvds/cumplimiento.md
Carpetas que no se miraron |    8     →  base/, plantillas/, historico-chat/, …
```

Y el registro de auditoría pasó de decir «1 sin reconocer» a enlazar el detalle:

```
1000 reconocido(s), 1 sin reconocer.
El detalle, en proyectos/cimiento/reportes/2026-08-25-205102-lo-que-no-entro.md
```

---

## 2. Ejecución caso por caso

### CP-001 · El reporte lista lo no reconocido, con su ruta

**El problema que resuelve:** un reporte que dice el número sin los nombres no sirve para corregir nada. Es exactamente lo que hacía el registro de auditoría antes de esta fase.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Traer un proyecto con dos documentos con molde y tres sin él | Entran dos | Dos |
| 2 | Abrir el reporte guardado | Existe | Existe |
| 3 | Buscar los tres nombres en el reporte | **Los tres están**, con su ruta | Los tres |
| 4 | Buscar los recuentos | Dice cuántos entraron y cuántos no | Las dos filas |
| 5 | Abrir el archivo del reporte con un lector cualquiera | Se lee sin la plataforma | Empieza con `# Qué no entró al traer` |

**Cómo se verificó que la pareja cumple:** el paso 3 es el que decide, y el 5 es el que hace útil el reporte a largo plazo: es texto, se abre con cualquier editor, y no depende de que la plataforma levante.

### CP-002 · El reporte se puede volver a mirar sin traer otra vez

**El problema que resuelve:** es la razón por la que existe esta fase. Antes, para saber qué había quedado afuera había que traer el proyecto entero otra vez.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Traer un proyecto con un documento sin molde | Queda el reporte | Queda |
| 2 | **Borrar la carpeta del proyecto entera** | Ya no hay de dónde traer | Borrada |
| 3 | Pedir el reporte | Sale completo, nombrando lo que quedó afuera | Nombra `apuntes.md` |
| 4 | Contar los registros de auditoría antes y después de mirarlo | **No sube**: mirar no es una acción que cambie nada | No sube |
| 5 | Sobre el repositorio real, con la ruta apuntando a una carpeta que no existe | El reporte sigue nombrando `cvds/cumplimiento.md` | Lo nombra |

**Cómo se verificó que la pareja cumple:** el paso 2 es la forma dura, y el 4 es el que comprueba lo que **no** pasa: mirar un reporte no es un cambio de estado, así que no debe ensuciar la auditoría. Un registro por cada vez que alguien mira algo volvería el registro inútil.

### CP-003 · Cuando no quedó nada afuera, el reporte lo dice

**El problema que resuelve:** si el reporte solo se escribiera cuando hay problemas, su ausencia no distinguiría entre «salió limpio» y «no se corrió».

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Traer un proyecto donde todo tiene molde | Todo entra | Todo |
| 2 | Buscar el reporte | **Existe** | Existe |
| 3 | Leer lo que dice | «Nada quedó afuera» | Lo dice |

**Cómo se verificó que la pareja cumple:** el paso 2 es el que decide. Es más importante que el 3: un reporte que dice lo correcto pero solo a veces no se puede usar como prueba de nada.

### CP-004 · El reporte dice qué carpetas no se miraron, y por qué

**El problema que resuelve:** es la otra mitad de lo que no entró. Decir «esto quedó afuera» sin decir que hubo carpetas enteras que ni se abrieron es contar media verdad.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Traer un proyecto que tenga `base/` y `pendientes/` | Ninguna de las dos se recorre | Ninguna |
| 2 | Buscar sus nombres en el reporte | Están | Están |
| 3 | Buscar **la razón** de cada una | También está | «no es documentación del ciclo» |
| 4 | Sobre el repositorio real | Las ocho carpetas, con su razón | Las ocho |

**Cómo se verificó que la pareja cumple:** el paso 3 es el que decide. Nombrar las carpetas sin decir por qué se saltaron deja al usuario pensando que es un error de la plataforma.

### CP-005 · El registro de auditoría dice dónde está el reporte

**El problema que resuelve:** que se pueda llegar del registro al detalle, sin repetir el detalle en dos sitios.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Traer un proyecto y leer su registro de auditoría | Trae la **ruta** del reporte | `reportes/…-lo-que-no-entro.md` |
| 2 | Traer otro con dos documentos sin molde | El registro dice cuántos | `2 sin reconocer` |
| 3 | Buscar los **nombres** de esos dos en el registro | **No están** | No están |
| 4 | Tomar la ruta del registro y abrir ese reporte | Trae los nombres | Los trae |

**Cómo se verificó que la pareja cumple:** los pasos 3 y 4 juntos. El 3 comprueba que el registro **no copia**, y el 4 que **sí lleva**. Sin el 3, dos copias de lo mismo se separan con el tiempo; sin el 4, el enlace podría apuntar a cualquier parte.

### CP-006 · Dos traídas dejan dos reportes, y se ve qué cambió

**El problema que resuelve:** poder comparar es la mitad del valor. Si el segundo reporte pisa al primero, se pierde la historia de qué se corrigió.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Traer un proyecto con tres archivos sin molde | Queda el primer reporte | Queda |
| 2 | «Corregir» uno: renombrarlo a un molde conocido | Ahora hay dos sin molde | Dos |
| 3 | Traer otra vez | Queda un **segundo** reporte | Dos reportes |
| 4 | Leer el viejo | Sigue nombrando el que se corrigió | Lo nombra |
| 5 | Leer el nuevo | Ya no lo nombra | Ya no |
| 6 | Pedir la lista | Del más nuevo al más viejo | En ese orden |

**Cómo se verificó que la pareja cumple:** los pasos 4 y 5 son los que decidieron el veredicto. Que haya dos archivos no prueba nada si los dos dicen lo mismo; lo que prueba que sirve para comparar es que **digan cosas distintas**, y que el viejo conserve lo que ya no es cierto hoy.

### CP-007 · Los reportes se ven desde la pantalla del proyecto

**El problema que resuelve:** un reporte que hay que buscar en el disco es un reporte que nadie mira.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Pedir los reportes de un proyecto **sin traídas** | Lo dice, en vez de una lista vacía | «todavía no se ha traído» |
| 2 | Traer, y volver a pedir | Se ve, con su fecha | Se ve |
| 3 | Abrir un reporte desde la pantalla | Trae su texto | Lo trae |
| 4 | Pedir un reporte de una fecha que no existe | Responde que no está | 404 |
| 5 | Desde la pantalla del proyecto, buscar cómo llegar | Hay un enlace | «Ver qué no entró en cada traída» |

**Cómo se verificó que la pareja cumple:** el paso 1 cubre el caso del primer día, que casi nunca se prueba. Y el 4 comprueba que una fecha inventada no devuelve un reporte vacío que se leería como «no quedó nada afuera».

### CP-008 · Que NO pase: que lo no reconocido entre o se toque

**El problema que resuelve:** escribir el reporte no puede volverse una excusa para tocar lo que se reporta.

**Cómo se hizo la prueba, paso a paso, en el ciclo 1:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Retratar la carpeta del proyecto, con un documento con molde y otro sin él | Queda la comparación | Quedó |
| 2 | Traer | Entra uno | Uno |
| 3 | Comparar la carpeta archivo por archivo | Ninguno cambió | Ninguno |
| 4 | Comprobar que el reporte quedó en los datos de la plataforma y no en el proyecto | Adentro sí, allá no | **Falló: no había reporte** |

**Veredicto del ciclo 1: No cumple.** Es el defecto `DEF-01`.

**Qué era, y por qué es el peor posible para esta fase.** Cuando **no entraba ningún** documento reconocido, `traer` se salía antes de escribir nada: **ni reporte ni registro de auditoría**. Justo el caso donde más falta hacen los dos. Alguien trae un proyecto, no entra nada, y no queda constancia de que se intentó ni de por qué no entró.

**Cómo quedó.** Traer sin que entre nada también es una traída: deja su registro y su reporte, con el porqué escrito en el código.

**Cómo se hizo la prueba, paso a paso, en el ciclo 2:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Repetir los cuatro pasos del ciclo 1 | El reporte está en `datos/` | Está |
| 2 | Comprobar que no hay carpeta de reportes dentro del proyecto | No la hay | No la hay |
| 3 | Traer un proyecto donde **nada** se reconoce | Queda su reporte y su registro | Los dos |

**Cómo se verificó que la pareja cumple:** el paso 3 es el que el ciclo 1 no cubría bien y el que destapó el defecto. Probar solo con proyectos que traen algo deja fuera el caso en que la respuesta correcta es «no entró nada, y esto es por qué».

**Tabla de casos ejecutados:**

| Caso | Qué exige | Prioridad | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | `CA-01` | Crítica | 2026-08-25 | Tres archivos sin molde, los tres nombrados en el reporte con su ruta | Aprobado | EV-01, EV-03 | — |
| CP-002 | Transversal | Crítica | 2026-08-25 | Con la carpeta del proyecto borrada, el reporte sigue nombrando lo que quedó afuera. En el real: `cvds/cumplimiento.md` | Aprobado | EV-01, EV-03 | — |
| CP-003 | `CA-03` | Alta | 2026-08-25 | Un proyecto limpio deja igual su reporte, diciendo «Nada quedó afuera» | Aprobado | EV-01 | — |
| CP-004 | `RN-4` | Alta | 2026-08-25 | Las ocho carpetas del repositorio real, cada una con su razón | Aprobado | EV-01, EV-03 | — |
| CP-005 | Transversal | Crítica | 2026-08-25 | El registro trae la ruta y **no** los nombres; desde esa ruta se llega al detalle | Aprobado | EV-01, EV-03 | — |
| CP-006 | Transversal | Alta | 2026-08-25 | Dos traídas, dos reportes: el viejo nombra lo corregido, el nuevo ya no | Aprobado | EV-01 | — |
| CP-007 | `RNF-07` | Alta | 2026-08-25 | Sin traídas lo dice; con traídas se ven con su fecha; una fecha inventada da 404 | Aprobado | EV-01 | — |
| CP-008 | `CA-02` | Crítica | 2026-08-25 | Ciclo 1: sin documentos reconocidos no se escribía reporte ni registro. Ciclo 2: los dos quedan, y la carpeta del proyecto intacta | Aprobado en el ciclo 2 | EV-01, EV-02 | DEF-01, corregido |

**Correspondencia con el plan:** 8 casos en el plan, 8 acá.

**Qué salió distinto de lo esperado:** el defecto del ciclo 1, y una corrección de redacción: el reporte decía «Estos 1 archivos». Ahora distingue el singular.

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que las pruebas cacen lo que dicen cazar | Ocho sabotajes, restaurando con copia, limpiando rastros y corriendo la suite al final | Los ocho cazados a la primera |
| 2 | Que el reporte real diga la verdad | Se leyó entero, pegado en la evidencia | 1000 entraron, 1 no, 8 carpetas sin mirar |
| 3 | Que el registro enlace y no copie | Se leyó el registro de la traída real | Trae la ruta, no la lista |
| 4 | Que el reporte se lea sin la plataforma | `cat` sobre el archivo | Se lee completo |
| 5 | Que los datos de prueba no quedaran | Se borraron y se rehicieron los tres índices | Cero en los tres |

**El sabotaje 8 escribía dentro del repositorio, y el guion limpió su rastro.** Es la lección que dejó la fase E: restaurar el código con copia no deshace lo que el sabotaje escribió fuera de él. El guion lo declara y lo borra al terminar, diciendo qué borró.

---

## 4. Defectos encontrados

| ID | Título | Caso que lo destapó | Severidad | Estado | Dónde quedó registrado |
|---|---|---|---|---|---|
| DEF-01 | Cuando no entraba ningún documento reconocido, **no se escribía ni el reporte ni el registro de auditoría**. Es el caso donde más falta hacen: alguien trae un proyecto, no entra nada, y no queda constancia | CP-008, ciclo 1 | Crítica | Corregido y verificado en el ciclo 2 | El comentario en `traer`, con su porqué |

**Defectos abiertos que se aceptan y por qué:** ninguno.

---

## 5. Veredicto por criterio de aceptación

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| `CA-01` lo no reconocido se lista con su ruta y se dice cuántos | CP-001 | Los tres nombrados, con los dos recuentos | Sí |
| `CA-02` no entra, y su archivo de origen no cambia | CP-008 | Retrato idéntico, y el reporte fuera del proyecto | Sí |
| `CA-03` si todo se reconoció, se dice | CP-003 | El reporte existe igual y lo dice | Sí |
| Transversal: el reporte queda guardado con la acción de traer | CP-002, CP-005 | Se mira con la carpeta borrada, y el registro lo enlaza | Sí |
| `RN-4` nada se pierde en silencio | CP-001, CP-004 | Lo no reconocido **y** las carpetas que no se miraron | Sí |
| `RNF-07` el reporte se entiende sin conocer el proyecto | CP-007 | Se llega desde la pantalla, y dice cuándo se trajo y de dónde | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Los ocho casos con veredicto escrito | Plan de pruebas §7 | 8 | 8 | Sí |
| Ningún caso en **No cumple** sin corregir | Plan de pruebas §7 | 0 | 0. El del ciclo 1 se corrigió y se repitió el ciclo completo | Sí |
| El reporte del repositorio real leído y pegado en la evidencia | Plan de pruebas §7 | Pegado | Pegado entero en EV-03 | Sí |
| Pruebas validadas con sabotaje, restaurando con copia y limpiando rastros | Plan de pruebas §7 | Todas las promesas | 8 sabotajes, 8 cazados, y el rastro del octavo borrado | Sí |
| **Probar los cuatro criterios, no solo el que falta** | Plan de pruebas §2 | Los cuatro | Los cuatro, aunque tres venían de la fase E | Sí |

**Lo que no se cumplió:** nada quedó corto.

---

## 6. Veredicto de la fase

**Concepto:** **Cumple**.

**Justificación:** los cuatro criterios quedaron probados, incluidos los tres que ya venían construidos de la fase E y que nunca se habían probado contra esta historia. El transversal —lo único que esta fase construyó de cero— se probó de la forma dura: **con la carpeta del proyecto borrada**, el reporte sigue diciendo qué quedó afuera.

El defecto del ciclo 1 lo encontró el caso de «que NO pase», y era el peor posible para una fase que existe para que nada se pierda en silencio: **cuando no entraba nada, no quedaba ni reporte ni registro**.

**Qué falta para que cumpla:** nada. **Con esto la HU-002 queda cerrada, la épica `EP-010` completa, y la versión 1 del producto terminada**: sus ocho fases cerradas.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Salida de las 165 comprobaciones automáticas | [evidencias/EV-01-pruebas-automaticas.txt](evidencias/EV-01-pruebas-automaticas.txt) |
| EV-02 | Los ocho sabotajes, y la limpieza del rastro del octavo | [evidencias/EV-02-las-pruebas-cazan-el-sabotaje.txt](evidencias/EV-02-las-pruebas-cazan-el-sabotaje.txt) |
| EV-03 | Corrida real: el reporte de este repositorio, entero, y `CP-002` sobre él | [evidencias/EV-03-corrida-real.txt](evidencias/EV-03-corrida-real.txt) |

---

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-08-25 | 7 | 1 | Primera ejecución. `CP-008` encontró que traer sin que entrara nada no dejaba ni reporte ni registro |
| 2 | 2026-08-25 | 8 | 0 | Corregido, con su porqué escrito. Y el reporte pasó a distinguir el singular |
