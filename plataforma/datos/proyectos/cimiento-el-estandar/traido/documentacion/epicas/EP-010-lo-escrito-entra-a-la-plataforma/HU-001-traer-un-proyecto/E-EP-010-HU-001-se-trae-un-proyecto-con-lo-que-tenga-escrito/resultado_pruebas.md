# Resultado de Pruebas — Fase E-EP-010-HU-001: se trae un proyecto con lo que tenga escrito   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección "qué se probó" del `funcionalidad_implementada.md`. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar: se aprobó antes y así se queda.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `E-EP-010-HU-001-se-trae-un-proyecto-con-lo-que-tenga-escrito` |
| **HU** | [HU-001 Traer un proyecto](../HU-001-traer-un-proyecto.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md), aprobado el 2026-08-25 |
| **Ciclo** | 2. El 1 encontró dos defectos, se corrigieron y se corrió completo otra vez |
| **Fecha de ejecución** | 2026-08-25 |
| **Ejecutado por** | El agente, en la máquina del usuario |
| **Ambiente y versión** | Windows 11, Python 3.11.9, Django 5.2.11. Sobre `plataforma/`, sin commit todavía |

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 9 | 9 | 7 | 2 | 0 | 0 |
| 2 | 9 | 9 | 9 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

**126 comprobaciones automáticas**, las 103 que ya existían más 23 de esta fase. Se validaron con **ocho sabotajes**, y los ocho quedaron cazados a la primera.

**El caso real superó lo previsto.** Al planear se contó que el repositorio tenía 969 archivos en `documentacion/` y que 966 seguían un molde conocido. La corrida dio **973 de 973 reconocidos, ninguno afuera**: los tres moldes que faltaban se agregaron en esta fase, y eran justo los que quedaban.

---

## 2. Ejecución caso por caso

### CP-001 · Lo que sigue un molde entra con su tipo

**El problema que resuelve:** si los documentos entran sin tipo, lo traído es un montón de archivos y no la documentación de un proyecto. La plataforma no podría decir qué fases tiene ni qué falta aprobar.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Armar un proyecto de mentira con los siete documentos del ciclo | Queda el punto de partida | Épica, historia, plan de trabajo, plan de pruebas, resultado, cierre y estado |
| 2 | Traerlo | Entran los siete, cada uno con su tipo | Los siete, con sus siete tipos distintos |
| 3 | Mirar de qué archivo salió cada uno | Trae su ruta dentro del proyecto | `documentacion/epicas/EP-001/epica.md` |
| 4 | Armar otro proyecto con **los tres moldes que faltaban** y traerlo | Los tres se reconocen | Señales, resultado de segundo ciclo y registro de versión |
| 5 | Traer un proyecto sin carpeta de documentación | Lo dice, en vez de fallar | `hay_documentacion` da falso, y cero reconocidos |

**Cómo se verificó que la pareja cumple:** el paso 4 es el que salió de la medición previa. Esos tres archivos eran los únicos de `documentacion/` que no se reconocían, y resultaron ser **moldes que faltaban en la lista**, no casos raros. Sin haber contado antes de planear, se habrían descubierto en producción.

### CP-002 · Lo traído dice lo mismo que el original

**El problema que resuelve:** «traer» promete copiar tal cual. Cualquier cambio silencioso convierte esa promesa en mentira, y el más silencioso de todos es el que no se ve al leer.

**Cómo se hizo la prueba, paso a paso, en el ciclo 1:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Traer un documento con acentos, comillas y una tabla | Idéntico | Idéntico |
| 2 | Traer un documento con **saltos de línea de Windows** y comparar los bytes | Idéntico | **Falló: llegaron como saltos de Unix** |

**Veredicto del ciclo 1: No cumple.** Es el defecto `DEF-01`.

**Qué era.** El módulo leía cada archivo con la apertura normal de texto, y Python traduce los saltos de línea al leer. Un documento escrito en Windows entraba a la plataforma transformado, incumpliendo `CA-5`. **El texto se ve exactamente igual**, así que ninguna revisión lo habría encontrado.

**Cómo quedó.** Se lee con `newline=""`, que es lo que apaga esa traducción, y el porqué quedó escrito al lado para que nadie lo quite por parecer de más.

**Cómo se verificó que la pareja cumple:** el paso 2 decide, y decide **porque compara los bytes**. La forma cómoda de escribir esta prueba —leer los dos lados y comparar cadenas— habría pasado en verde, porque al leer los dos con la misma función los dos salen iguales. Es la trampa exacta de este caso.

### CP-003 · Lo que no sigue ningún molde no entra, y se cuenta

**El problema que resuelve:** adivinar la forma de un documento y meterlo igual ensucia lo que sí sirve, y nadie sabe después qué es de fiar.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Armar un proyecto con dos documentos con molde y tres sin él | Queda el caso | Quedó |
| 2 | Traerlo | Entran **dos** | Dos |
| 3 | Contar lo que quedó afuera | Tres, y no entraron | Tres |
| 4 | Mirar cada uno | Trae su ruta completa | `documentacion/apuntes.md` y los otros dos |

**Cómo se verificó que la pareja cumple:** el paso 3 y el 4 juntos. Contar sin decir cuáles no sirve para actuar; decir cuáles sin contar no deja ver el tamaño del problema.

### CP-004 · Si todo se reconoció, se dice

**El problema que resuelve:** una sección vacía se lee como «el reporte no se generó», y el usuario se queda sin saber si salió bien o no salió.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Traer un proyecto donde todo tiene molde | `todo_reconocido` da verdadero | Verdadero |
| 2 | Mirar la pantalla | Lo dice con palabras | `Nada quedó afuera` |

**Cómo se verificó que la pareja cumple:** el paso 2 es el que importa. Que el dato exista adentro no sirve si la pantalla muestra una lista vacía sin explicación.

### CP-005 · Traer dos veces no duplica

**El problema que resuelve:** traer es una acción que se repite —cada vez que el proyecto avanza—, y si duplicara, la segunda pasada volvería inservible lo traído.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Traer un proyecto de dos documentos y contar | Quedan dos | Dos |
| 2 | Traerlo otra vez | La cuenta **no sube** | Sigue en dos |
| 3 | Mirar lo que devuelve la segunda pasada | Dice cuántos ya estaban | `0 nuevos, 2 ya estaban` |
| 4 | **Editar** un documento en el origen y traer otra vez | No se crea otro documento | Sigue habiendo uno |
| 5 | Leer lo traído | Trae la versión **nueva** | `# Como quedó` |

**Cómo se verificó que la pareja cumple:** los pasos 4 y 5 son los que distinguen «no duplicar» de «no actualizar». Un código que se saltara los documentos ya traídos pasaría los pasos 1 a 3 y fallaría acá, y el usuario tendría la documentación congelada en la primera pasada sin enterarse.

### CP-006 · Se muestra qué se va a traer antes de traerlo

**El problema que resuelve:** `00·N1` sobre una acción que mueve cientos de documentos de una vez. Es la acción más grande que la plataforma sabe hacer.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Pedir traer sin confirmar | Sale la pantalla, y **nada entró** | Cero documentos, cero registros nuevos |
| 2 | Armar un proyecto de veinte documentos y mirar la pantalla | Muestra el **recuento por tipo** | Sale la tabla por tipo |
| 3 | Buscar en la pantalla la ruta de uno de los veinte | **No está**: se muestra el recuento, no la lista | No está |
| 4 | Leer lo que dice antes de confirmar | Dice qué NO va a pasar | «se copia, no se mueve», «no queda nada de esta pasada» |
| 5 | Confirmar | Ahora sí entra, y queda un registro con el recuento | Un documento, un registro con `1 documento` |

**Cómo se verificó que la pareja cumple:** el paso 3 es el que decide y es el que se olvida. Mostrar las mil rutas es honesto y a la vez inútil: nadie las lee, se confirma sin mirar, y la confirmación deja de proteger. El recuento por tipo se lee en cinco segundos.

### CP-007 · Una falla a mitad no deja media importación

**El problema que resuelve:** con media documentación adentro, nadie sabe qué falta ni por dónde seguir. Es peor que no haber traído nada.

**Cómo se hizo la prueba, paso a paso, en el ciclo 1:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Armar un proyecto de tres documentos | Queda el caso | Quedó |
| 2 | Hacer fallar la escritura **en el segundo** | Revienta con `NoSePudoTraer` | Reventó |
| 3 | Contar los documentos en el índice | Cero | **Falló: quedó uno** |
| 4 | Buscar archivos en la carpeta de lo traído | Ninguno | Ninguno |
| 5 | Comparar la carpeta del proyecto de origen | Intacta | Intacta |

**Veredicto del ciclo 1: No cumple.** Es el defecto `DEF-02`.

**Qué era.** Al fallar se borraban los archivos escritos, **pero no las filas del índice**. Quedaba media importación con otra cara: el índice diciendo que había documentos traídos que ya no existían.

**Cómo quedó.** Deshacer borra las dos cosas, y el porqué quedó escrito en la función.

**Cómo se verificó que la pareja cumple:** el paso 3 y el 4 juntos, y esa es la lección. Comprobar solo los archivos daba verde con el defecto adentro. Media importación puede vivir en cualquiera de los dos sitios, y hay que mirar los dos.

### CP-008 · Se trae este mismo repositorio

**El problema que resuelve:** es el caso más grande que existe hoy. Si el módulo no puede con él, no puede con nada.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Contar los archivos del repositorio antes | Queda la comparación | 973 `.md` en `documentacion/`, 1924 archivos en todo el repositorio |
| 2 | Conectarlo y **mirar** sin traer | Cuenta sin escribir nada | 973 reconocidos, 0 sin reconocer, 0 traídos |
| 3 | Ver qué carpetas dice que no mira | Las nombra con su porqué | Ocho: `base/`, `plantillas/`, `historico-chat/`, `pendientes/`, `validadores/`, `skills/`, `notas/`, `prompts/` |
| 4 | Traerlo, midiendo | Entran los 973 | **973 en 13,6 s** |
| 5 | Mirar el recuento por tipo | Cuadra con lo contado al planear | 236 índices, 126 estados de fase, 126 planes de pruebas, 126 planes de trabajo, 122 resultados, 112 historias, 107 cierres, 11 épicas, 5 especificaciones, 1 registro de versión, 1 de señales |
| 6 | Traerlo otra vez | No duplica | 0 nuevos, 973 ya estaban |
| 7 | Contar los archivos del repositorio después | Los mismos | **973 y 1924**, iguales |

**Cómo se verificó que la pareja cumple:** el paso 7 cuenta **el repositorio entero**, no solo `documentacion/`. Contar solo la carpeta que se lee dejaría pasar un archivo escrito en cualquier otra parte, que es el error más probable de este módulo.

**Sobre el número.** Al planear se contó 966 de 969 reconocidos. La corrida dio 973 de 973 porque los tres moldes que faltaban se agregaron en esta fase, y porque el repositorio creció mientras se trabajaba. **La diferencia no fue un hallazgo: fue el efecto de haberlos agregado.**

### CP-009 · Que NO pase: que se toque el proyecto de origen

**El problema que resuelve:** traer es la operación que **más archivos ajenos lee** de toda la plataforma. Es donde más caro sale equivocarse.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Retratar la carpeta del proyecto entera: cada archivo, con su contenido y su fecha | Queda la comparación | Quedó |
| 2 | Traerlo, incluyendo un documento que **no** se reconoce | Entra lo reconocido | Entró |
| 3 | Comparar la lista de archivos | Ninguno se creó ni se borró | Idéntica |
| 4 | Comparar archivo por archivo el contenido y la fecha | Ninguno cambió | Ninguno |
| 5 | Comprobar que lo traído está en los datos de la plataforma y **no** en el proyecto | Adentro sí, allá no | Adentro sí, allá no |
| 6 | Repetir después de una falla a mitad | Tampoco lo toca | Retrato idéntico |
| 7 | En la corrida real, contar los 1924 archivos del repositorio antes y después | Iguales | Iguales |

**Cómo se verificó que la pareja cumple:** el paso 6 es el que cubre el momento peligroso. Un código escrito con prisa podría limpiar mal al fallar y llevarse algo del origen; ahí es donde un error de una línea hace daño de verdad.

**Tabla de casos ejecutados:**

| Caso | Qué exige | Prioridad | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | `CA-1` | Crítica | 2026-08-25 | Siete documentos del ciclo entraron con siete tipos distintos; los tres moldes que faltaban también | Aprobado | EV-01 | — |
| CP-002 | `CA-5` | Crítica | 2026-08-25 | Un documento con saltos de Windows: en el ciclo 1 llegó transformado; en el 2, byte por byte idéntico | Aprobado en el ciclo 2 | EV-01, EV-02 | DEF-01, corregido |
| CP-003 | `CA-4` | Crítica | 2026-08-25 | Dos con molde entraron, tres sin molde quedaron afuera con su ruta | Aprobado | EV-01 | — |
| CP-004 | `CA-6` | Alta | 2026-08-25 | La pantalla dijo `Nada quedó afuera` | Aprobado | EV-01 | — |
| CP-005 | `CA-3` | Crítica | 2026-08-25 | Segunda pasada: 0 nuevos, 2 ya estaban. Un documento editado entró con su versión nueva sin duplicarse | Aprobado | EV-01, EV-03 | — |
| CP-006 | `00·N1` | Crítica | 2026-08-25 | Sin confirmar no entró nada; con veinte documentos se mostró el recuento por tipo y ninguna ruta | Aprobado | EV-01 | — |
| CP-007 | Falla a mitad | Crítica | 2026-08-25 | Falla en el segundo de tres: en el ciclo 1 quedó una fila en el índice; en el 2, nada | Aprobado en el ciclo 2 | EV-01, EV-02 | DEF-02, corregido |
| CP-008 | El caso real | Crítica | 2026-08-25 | **973 documentos reconocidos, 0 afuera, en 13,6 s.** Segunda pasada: 0 nuevos, 973 ya estaban | Aprobado | EV-03 | — |
| CP-009 | `CA-2` | Crítica | 2026-08-25 | Retrato idéntico del proyecto de mentira, y 1924 archivos del repositorio real antes y después | Aprobado | EV-01, EV-03 | — |

**Correspondencia con el plan:** 9 casos en el plan, 9 acá.

**Qué salió distinto de lo esperado:** los dos defectos del ciclo 1, y el número del caso real, que salió mejor de lo previsto por la razón explicada en `CP-008`.

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que las pruebas cacen lo que dicen cazar | Ocho sabotajes, restaurando con copia y corriendo la suite completa al final | Los ocho cazados a la primera |
| 2 | Que el repositorio real quede intacto | Conteo de sus 1924 archivos antes y después | Iguales |
| 3 | Que lo traído se lea sin la plataforma | `head` sobre un documento traído | Se lee, idéntico al original |
| 4 | Que los tres índices se rehagan desde el texto | Los tres comandos de reconstrucción | Los tres en cero después de limpiar |
| 5 | Que los datos de prueba no quedaran | Se borraron y se rehicieron los índices | Cero en los tres |

**Un hallazgo que no era de la fase, y que casi se va en el commit.** Uno de los sabotajes hacía que traer escribiera un archivo **dentro del repositorio**. La prueba lo cazó y el código se restauró, pero **el archivo que ese sabotaje alcanzó a escribir se quedó ahí**: 973 líneas en la raíz del proyecto. Se descubrió porque la corrida real preguntaba «¿hay rastro dentro del repositorio?» y salió en verdadero.

Restaurar con copia protege el código, no el mundo. El guion ahora declara sus rastros, los limpia al terminar y dice qué limpió.

---

## 4. Defectos encontrados

| ID | Título | Caso que lo destapó | Severidad | Estado | Dónde quedó registrado |
|---|---|---|---|---|---|
| DEF-01 | Traer transformaba los saltos de línea de Windows, incumpliendo `CA-5`. El texto se ve idéntico | CP-002, ciclo 1 | Crítica | Corregido y verificado en el ciclo 2 | El `newline=""` de `traer`, con su porqué escrito |
| DEF-02 | Al fallar a mitad se borraban los archivos pero no las filas del índice: media importación con otra cara | CP-007, ciclo 1 | Crítica | Corregido y verificado en el ciclo 2 | `_deshacer`, con su porqué escrito |

**Defectos abiertos que se aceptan y por qué:** ninguno.

---

## 5. Veredicto por criterio de aceptación

| Exigencia de la especificación | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| `CA-1` lo que sigue un molde queda adentro con su tipo | CP-001, CP-008 | 973 documentos del repositorio real, con once tipos | Sí |
| `CA-2` el proyecto de origen queda intacto | CP-009 | Retrato idéntico, y 1924 archivos antes y después | Sí |
| `CA-3` traer dos veces no duplica | CP-005, CP-008 | 0 nuevos y 973 ya estaban en la segunda pasada | Sí |
| `CA-4` lo no reconocido queda listado con su ruta | CP-003 | Tres afuera, con su ruta completa | Sí |
| `CA-5` nada se transforma sin que el usuario lo diga | CP-002 | Byte por byte idéntico, saltos de línea incluidos | Sí |
| `CA-6` si todo se reconoció, se dice | CP-004 | Con esas palabras en la pantalla | Sí |
| `00·N1` se muestra qué se va a traer antes de traerlo | CP-006 | Recuento por tipo, y nada entra sin confirmar | Sí |
| `RN-4` nada se pierde en silencio | CP-003, CP-008 paso 3 | Lo no reconocido se lista, y **las carpetas que no se miran se nombran con su porqué** | Sí |
| Una falla a mitad no deja nada | CP-007 | Ni archivos ni filas del índice | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Los nueve casos con veredicto escrito | Plan de pruebas §7 | 9 | 9 | Sí |
| Ningún caso en **No cumple** sin corregir | Plan de pruebas §7 | 0 | 0. Los dos del ciclo 1 se corrigieron y se repitió el ciclo completo | Sí |
| Los números del caso real escritos | Plan de pruebas §7 | Cuántos, de qué tipo, cuántos no, y cuánto tardó | 973, once tipos, 0 afuera, 13,6 s | Sí |
| Pruebas validadas con sabotaje, restaurando con copia y corriendo la suite al final | Plan de pruebas §7 | Todas las promesas | 8 sabotajes, 8 cazados | Sí |
| El repositorio de origen comprobado intacto | Plan de pruebas §7 | Sin cambios | 1924 archivos antes y después | Sí |

**Lo que no se cumplió:** nada quedó corto.

---

## 6. Veredicto de la fase

**Concepto:** **Cumple**.

**Justificación:** los seis criterios de la especificación quedaron probados, y el caso real —traer este repositorio— entró con **973 documentos y ninguno afuera**. La incertidumbre que la especificación declaraba como la mayor de la versión 1 se resolvió midiendo antes de planear, y lo que se encontró midiendo (tres moldes que faltaban) entró a la fase en vez de descubrirse en producción.

Los dos defectos del ciclo 1 los encontraron pruebas escritas de la forma incómoda: comparar **bytes** en vez de texto, y mirar **las dos** formas en que puede quedar media importación. Escritas de la forma cómoda, las dos habrían pasado en verde con el defecto adentro.

**Qué falta para que cumpla:** nada.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Salida de las 126 comprobaciones automáticas, con la medición de `CP-008` | [evidencias/EV-01-pruebas-automaticas.txt](evidencias/EV-01-pruebas-automaticas.txt) |
| EV-02 | Los ocho sabotajes, qué prueba cazó cada uno, y la limpieza de sus rastros | [evidencias/EV-02-las-pruebas-cazan-el-sabotaje.txt](evidencias/EV-02-las-pruebas-cazan-el-sabotaje.txt) |
| EV-03 | Corrida real: se trae este repositorio, con sus números y el conteo de intacto | [evidencias/EV-03-corrida-real.txt](evidencias/EV-03-corrida-real.txt) |

---

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-08-25 | 7 | 2 | Primera ejecución. `CP-002` encontró la transformación de saltos de línea; `CP-007`, las filas del índice que no se deshacían |
| 2 | 2026-08-25 | 9 | 0 | Los dos defectos corregidos, con su porqué escrito en el código |
