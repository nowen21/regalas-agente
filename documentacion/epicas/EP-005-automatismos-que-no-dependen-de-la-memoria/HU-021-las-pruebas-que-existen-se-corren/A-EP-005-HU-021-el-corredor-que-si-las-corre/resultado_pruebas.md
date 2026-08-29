# Resultado de Pruebas — Fase `A-EP-005-HU-021-el-corredor-que-si-las-corre`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. Alimenta el [estado-fase.md](estado-fase.md) y la sección «qué se probó» del [funcionalidad_implementada.md](funcionalidad_implementada.md). El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md), que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-005-HU-021-el-corredor-que-si-las-corre` |
| **HU** | [HU-021](../HU-021-las-pruebas-que-existen-se-corren.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-28 |
| **Ejecutado por** | El agente, sobre este repositorio |
| **Ambiente y versión** | Windows 11 · Python 3.11 · git de verdad · Cimiento `35.9.0` |

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 9 | 9 | 9 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

---

## 2. Ejecución caso por caso

### CP-000 — La línea base, archivo por archivo

**El problema que resuelve:** sin saber cuáles estaban en verde **antes**, un rojo que aparezca después no se distingue de uno de siempre, y la `T-01` no se puede juzgar.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr los 67 uno por uno con `corren-las-pruebas-de-tests.py --todos` | Queda la lista | Quedó, en `linea-base-t00.txt` |
| 2 | Contar verdes y rojos | **61 y 6** | 61 y 6 |
| 3 | Guardar la salida | Queda | Queda, con los 67 nombrados uno a uno |

**Cómo se verificó que la pareja cumple:** decide el paso 3, no el 2. Los números solos no sirven: lo que hace juzgable la `T-01` es **la lista con nombres**, porque el cambio que importa es *cuál* pasó de verde a rojo, no cuántos.

---

### CP-001 — El `__init__.py` no rompe ninguno   ·   **podía tumbar el diseño**

**El problema que resuelve:** un `__init__.py` cambia cómo un módulo resuelve sus importaciones, y estos 67 hoy se corren sueltos. Si rompe alguno, el camino de «que la orden documentada funcione» se cae.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Crear `validadores/tests/__init__.py` | — | Creado |
| 2 | Correr los 67 uno por uno otra vez | — | Corrió |
| 3 | Comparar contra `CP-000` | **Los mismos 61 y los mismos 6** | Los mismos 6 archivos en rojo |
| 4 | Investigar la única diferencia: `test_el_mapa_del_amarre_no_envejece` pasó de 1 falla a 5 | Saber de qué es | **De `corredor.py`**, que acababa de nacer y no estaba en el mapa del amarre |
| 5 | Apartar `corredor.py` y correr ese archivo solo | Vuelve a 1 falla | **Volvió a 1** — la diferencia era mía, no del `__init__.py` |

**Cómo se verificó que la pareja cumple:** decide el paso 5. Los pasos 3 y 4 dejaban una duda razonable —«subió de 1 a 5 fallas, ¿fue el `__init__.py`?»— y la única forma de responderla era **quitar la otra variable y volver a medir**. Sin ese paso, el criterio de suspensión se habría juzgado sobre una sospecha.

---

### CP-002 — Cero pruebas no pasa por verde   ·   **el crítico**

**El problema que resuelve:** es el defecto original. Durante semanas hubo una orden documentada que no corría nada, y su silencio se leyó como que estaba todo bien. Un corredor que repita eso no arregla nada: lo disfraza.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Apuntar el corredor a una carpeta **vacía** | **Rojo**, y dice que no encontró ninguna | `se corrieron **0 pruebas** — cero no es verde` |
| 2 | Apuntarlo a una carpeta **que no existe** | Rojo, con mensaje claro | `no existe la carpeta de pruebas — no se comprobó nada` |
| 3 | Apuntarlo a una carpeta con un archivo **sin pruebas dentro** | Rojo | Rojo |
| 4 | Correr `unittest discover` solo, en el mismo caso | **Da 0** — y por eso hace falta el corredor | Dio 0 |

**Cómo se verificó que la pareja cumple:** el paso 4 no prueba el corredor: **prueba que el corredor hace falta**, y queda como prueba viva. Si algún día `discover` dejara de dar 0 con cero pruebas, esa prueba falla y avisa de que la justificación de esta pieza cambió — que es más de lo que hace un comentario.

Pruebas: `test_la_carpeta_vacia_es_roja`, `test_la_carpeta_que_no_existe_es_roja`, `test_archivos_sin_ninguna_prueba_dentro_es_rojo`, `test_unittest_discover_solo_daria_cero_y_por_eso_hace_falta`.

---

### CP-003 — Las 650 corren y se cuentan

**El problema que resuelve:** «corre» sin conteo es exactamente lo que teníamos.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | `python validadores/validar.py internas` sobre el repositorio real | Corre | Corrió |
| 2 | Leer el conteo | **Nunca 0** | `650 prueba(s) en 67 archivo(s) · 7 falla(s) · 0 error(es)` |
| 3 | Leer las fallas | Los archivos de `CP-000` | **5 archivos**, no 6: uno se cerró en el camino |
| 4 | Medir lo que tarda | Se anota | **577,4 s la primera vez, 667 s la segunda — entre 9,6 y 11 minutos** |
| 5 | Volver a correrla al cerrar la fase, ya con todo escrito | El mismo resultado | **8 fallas en los mismos 5 archivos**, no 7 — `DEF-05` |

**Cómo se verificó que la pareja cumple:** decide el paso 2, y el 4 es el que cambió el diseño. **El paso 5 es el que se ganó su fila:** correrla una segunda vez, al final, destapó una falla que la primera no tenía — y era mía, de cerrar un pendiente a mano. **Una corrida al empezar y otra al cerrar no son la misma corrida repetida: la segunda mide lo que el trabajo hizo.** **El plan estimaba ~3 minutos y el número real fue 9,6.** Ese dato no confirmó la `T-04`: la reformuló, porque con 9,6 minutos ninguna opción que *corra* las pruebas cabe en el umbral.

---

### CP-004 — La orden documentada es la que funciona

**El problema que resuelve:** que la documentación mienta es la mitad del defecto. La orden estaba escrita desde la primera prueba del repositorio y se caía antes de correr nada.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Buscar qué orden se documenta para esta carpeta | Se encuentra | `python -m unittest discover -s validadores/tests`, en el `CHANGELOG` |
| 2 | Correrla tal cual, con el `__init__.py` puesto | **Corre** | Corre: carga y ejecuta |
| 3 | Comprobar que el `README` de `validadores/` la nombra | La nombra | Ahora nombra **las dos suites**, con su tiempo y su motivo de estar separadas |

**Cómo se verificó que la pareja cumple:** decide el paso 2. El 3 no se limitó a corregir: **el `README` ahora dice por qué son dos**, porque la pregunta que sigue a «hay dos órdenes» es «¿cuál corro?», y dejarla sin respuesta reproduce el problema con otra forma.

---

### CP-005 — Se puede pedir un subconjunto

**El problema que resuelve:** sin esto la única opción es 9,6 minutos o nada, y `02·F5` —correr las suites que la fase toca— no se puede cumplir sobre esta carpeta.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Pedir **un** archivo por su nombre | Corre solo ese, y el conteo lo dice | `9 prueba(s) en 1 archivo(s)` |
| 2 | Pedir **dos** | Corren los dos | `29 prueba(s) en 2 archivo(s)` |
| 3 | Pedir un nombre **que no existe** | **Rojo** | `se pidió … y no está en la carpeta`, más el rojo de cero pruebas |
| 4 | Comprobar que el conteo es menor que el total | Lo es | 9 y 29 contra 650 |

**Cómo se verificó que la pareja cumple:** el paso 3 importa tanto como el 1. **Pedir un archivo mal escrito y recibir verde sería `CP-002` otra vez, por la puerta de al lado**, y es la forma más fácil de que el defecto vuelva sin que nadie lo note.

Pruebas: `test_se_puede_pedir_un_solo_archivo`, `test_un_nombre_que_no_existe_es_rojo_no_una_corrida_vacia`.

---

### CP-006 — Cuánto cuesta lo colgado   ·   **el que tumbó el enganche que se pensaba**

**El problema que resuelve:** un control que cuesta más de lo que evita se apaga, y deja algo peor que su ausencia: la apariencia de estar puesto.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Medir lo que tardan las 650 | Se anota | **577,4 s = 9,6 min** |
| 2 | Contar el ritmo real de los últimos 14 días | Se anota | **245 commits en 15 días de actividad — 16,3 por día** |
| 3 | Multiplicar por cada sitio posible | **Menos de un minuto por commit** | En cada commit: **39,3 horas**. En cada push: **2,4 horas**. Al abrir sesión: **2,4 horas** |
| 4 | Si no pasa, elegir otro sitio y decirlo con el número | — | **Ninguna opción que corra las pruebas cabe.** Se cuelga el **reclamo**, no la corrida |

**Cómo se verificó que la pareja cumple:** decide el paso 3, y su resultado fue **«no»** para todas las opciones que el plan contemplaba. Ese es el caso escrito para que la fase pudiera fracasar, y **fracasó como estaba planteado**: lo que cayó no fue la fase sino el diseño del enganche. La pregunta pasó de *«¿dónde las corro?»* a *«¿cómo me entero de que hace falta correrlas sin pagar 9,6 minutos?»*, y eso ya tiene forma en esta casa — el enganche del checkpoint **reclama en vez de hacer**.

**Lo que quedó:** el corredor sella la última corrida entera y limpia; el `pre-push` mira esa fecha contra el último commit y avisa si hay trabajo que las pruebas no vieron. Cuesta leer un archivo.

---

### CP-007 — Está colgado

**El problema que resuelve:** en `EP-002·HU-004` un aviso quedó construido, probado, en verde — y nadie lo llamaba.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Buscar el reclamo en la plantilla del `pre-push` del instalador | Está | Está |
| 2 | Correr el instalador y mirar el enganche real en `.githooks/` | Está | Está, línea 46 |
| 3 | Una prueba que compruebe que el enganche **no corre las 650** | No las corre | No las corre |
| 4 | Sabotear el nombre y correr las pruebas | Fallan | Fallaron |

**Cómo se verificó que la pareja cumple:** el paso 3 se ganó su fila aparte. Comprobar que el reclamo está colgado no basta: **si mañana alguien cambia `--reclamo` por la corrida entera, el enganche seguiría "puesto" y se apagaría en una semana.** Esa prueba vigila la decisión, no la presencia.

---

### CP-008 — Los seis rojos quedan declarados

**El problema que resuelve:** un rojo que se arrastra sin decisión escrita apaga el semáforo otra vez, que es de donde venimos.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer el `funcionalidad_implementada.md` | Los seis, por su nombre | Los seis: **uno cerrado, cinco declarados** |
| 2 | Comprobar que cada uno dice qué falla y adónde va | Lo dice | Lo dice, y cuatro de las siete fallas salen de una misma fase |
| 3 | Comprobar que ninguno queda como «se verá» | Ninguno | Ninguno |

**Cómo se verificó que la pareja cumple:** decide el paso 2, y lo que lo hace útil es haber agrupado por **causa** y no por archivo: cuatro de las siete fallas apuntan a `estacion_commit.py` y `hook_estacion.py`, de la fase `A-EP-005-HU-019`. Eso convierte «cinco rojos sueltos» en dos destinos concretos.

---

| Caso | CA | Prioridad | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-000 | Previo | — | 2026-08-28 | los 67 uno por uno: **61 verdes, 6 rojos**, con nombres | Aprobado | EV-00 | — |
| CP-001 | Previo | **Crítica** | 2026-08-28 | con el `__init__.py`: los mismos 6; la subida a 5 fallas era de `corredor.py`, comprobado apartándolo | Aprobado | EV-01 | DEF-01 |
| CP-002 | CA-02 | **Crítica** | 2026-08-28 | carpeta vacía, inexistente y sin pruebas: rojo en las tres; `discover` da 0 en la misma | Aprobado | EV-02 | — |
| CP-003 | CA-01 | Alta | 2026-08-28 | `validar.py internas`: `650 prueba(s) en 67 archivo(s)`, **8 falla(s) en 5 archivos** en 667 s | Aprobado | EV-03 | DEF-05 |
| CP-004 | CA-01 | Alta | 2026-08-28 | la orden del `CHANGELOG`, corrida tal cual: carga y ejecuta | Aprobado | EV-04 | — |
| CP-005 | CA-03 | Media | 2026-08-28 | uno: `9 en 1`; dos: `29 en 2`; inexistente: rojo | Aprobado | EV-02 | — |
| CP-006 | CA-04 | **Crítica** | 2026-08-28 | 9,6 min × 245 commits/14 días = **39,3 h**; ninguna opción cabe en 1 min | Aprobado | EV-05 | DEF-02 |
| CP-007 | CA-04 | Media | 2026-08-28 | en `PLANTILLA_PRE_PUSH` y en `.githooks/pre-push`; sabotearlo tumba las pruebas | Aprobado | EV-06 | — |
| CP-008 | CA-05 | Media | 2026-08-28 | los seis, en §6 del cierre: uno cerrado, cinco con destino | Aprobado | EV-07 | — |

**Correspondencia con el plan:** 9 casos en el plan, 9 acá.

**Qué salió distinto de lo esperado:** **el tiempo.** El plan decía ~3 minutos y son 9,6, y ese número cambió la respuesta de `CP-006`. Está en §4 como `DEF-02`, porque una estimación que decide un diseño y está tres veces corta es un defecto del análisis, no un detalle.

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que el enganche quedó en el archivo de verdad, no solo en la plantilla | Correr el instalador y leer `.githooks/pre-push` | Está, línea 46, con `\|\| true` para que no detenga el push |
| 2 | Que el reclamo cuesta lo que dice costar | `validar.py internas --reclamo` | Responde de inmediato: lee una fecha |
| 3 | Que los sabotajes se cazan | `sabotajes-hu021.py` | **12 de 12**, tras corregir **tres** mal armados |
| 4 | Que el reclamo diga la verdad **después** de una corrida entera | Correr las 650 y leer el aviso | Dice «la última corrida (21:57:12) dejó **8 falla(s)**», no «nunca corrieron» |

---

## 4. Defectos encontrados

| ID | Título | Caso que lo destapó | Severidad | Estado | Dónde quedó registrado |
|---|---|---|---|---|---|
| DEF-01 | `corredor.py` nació sin entrada en el mapa del amarre, y sumó 4 fallas que parecían del `__init__.py` | `CP-001` | Media | Corregido | Su fila en `anatomia/que-esta-amarrado-a-la-herramienta.md` |
| DEF-02 | El plan estimó ~3 minutos y son **9,6** | `CP-003` | **Alta** — el número decidía dónde colgar la corrida | Corregido en el diseño | `CP-006`: se cuelga el reclamo, no la corrida |
| DEF-03 | Dos sabotajes mal armados: uno cambiaba el texto sin cambiar el comportamiento, el otro no aplicaba | `T-11` | Media | Corregidos | `sabotajes-hu021.py` |
| DEF-06 | **El reclamo decía «nunca corrieron» sobre unas pruebas que habían corrido dos veces ese día.** El sello solo se escribía en verde, y la carpeta tiene ocho fallas conocidas | El primer `push` de verdad, **después del ciclo** | **Alta** — manda a esperar 10 minutos para volver a leer lo mismo | Corregido | El sello guarda el conteo; el reclamo dice **tres motivos distintos**. Señal `S-077` |
| DEF-07 | Un sabotaje se reportó **CAZADO** y no cazaba nada: dejaba el archivo sin compilar, así que las pruebas fallában por sintaxis | Mirar la salida de la tanda, no su total | Media | Corregido | El guion marca **NO VALE** ante `SyntaxError`. Señal `S-078` |
| DEF-05 | La corrida de cierre dio **8 fallas**, no las 7 de la primera. La octava es `test_cp001_cada_subcomando_sigue_corriendo_por_separado`, y la causó **cerrar el pendiente 90 a mano**: al moverlo a `hecho/` quedaron cuatro enlaces rotos, y ese caso corre `validar.py estandar` esperando cero | `CP-003`, segunda corrida | Media | Corregido | Las citas arrastradas; `validar.py estandar` en verde |
| DEF-04 | Una prueba **no podía fallar**: buscaba «internas» en un bloque donde la exclusión no vive | `T-11`, sabotaje 11 | **Alta** — es el patrón `S-062` | Corregida | Ahora mira `FUERA_DE_LA_CORRIDA` |

**Defectos abiertos que se aceptan y por qué:** ninguno. Los cuatro quedaron corregidos dentro del ciclo 1.

**`DEF-06` no lo encontró ninguna de las 22 pruebas ni ninguno de los once sabotajes: lo encontró correrlo de verdad, una vez, en el momento en que sirve.** Las pruebas cubrían «sin sello reclama» y «con sello limpio calla»; el caso real —sello ausente **porque** hubo fallas— caía justo entre las dos. Está en `S-077`.

**`DEF-04` es el que más enseña, y lo destapó un sabotaje que dijo «NO APLICA».** Ese aviso parecía un problema del guion de sabotaje —el texto que buscaba no existía— y era cierto; pero al buscar el texto correcto apareció que **la prueba miraba el sitio equivocado**, y por lo tanto no podía fallar. Es la tercera forma de `S-062`, encontrada por accidente.

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia | Casos | Resultado | Cumple |
|---|---|---|---|
| CA-01 — la carpeta se corre con una orden, y es la documentada | CP-003, CP-004 | 650 en 67 archivos, con conteo; la orden del `CHANGELOG` carga y corre | Sí |
| CA-02 — cero pruebas no pasa por verde | CP-002 | Vacía, inexistente y sin pruebas: rojo en las tres | Sí |
| CA-03 — se puede pedir un subconjunto | CP-005 | Uno, dos, y un nombre inexistente en rojo | Sí |
| CA-04 — la corrida completa está colgada de algo | CP-006, CP-007 | Colgado el **reclamo**, medido y justificado con el número | Sí |
| CA-05 — los seis rojos quedan declarados | CP-008 | Uno cerrado, cinco con destino | Sí |
| RNF-01 — rendimiento | CP-003, CP-005 | El corredor no las hace más lentas; el subconjunto baja de 650 a 9 | Sí |
| RNF-02 — no estorbar | CP-006, CP-007 | El enganche lee una fecha; no corre nada y no detiene el push | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de criterios y RNF | Plan §5 | 100% | 5 CA y 2 RNF, todos con caso | Sí |
| Casos críticos ejecutados | Plan §3.2 | 100% | `CP-001`, `CP-002` y `CP-006` | Sí |
| Casos ejecutados | Plan §12 | 8 de 8 | 9 de 9 | Sí |
| **Archivos que el `__init__.py` pone en rojo** | Plan §12 | **0** | **0** | Sí |
| **Casos donde cero pruebas da verde** | Plan §12 | **0** | **0** | Sí |
| **Lo que agrega lo colgado, por commit** | Plan §12 | menos de 1 min | **Lee una fecha.** Correrlas habría costado 9,6 min | Sí |
| Rojos declarados de los 6 | Plan §12 | 6 | 6 — uno cerrado, cinco enrutados | Sí |
| Sabotajes cazados | Plan §12 | Todos | **12 de 12**, ninguno por error de sintaxis | Sí |
| Fallas en `pruebas.py` | Plan §12 | 0, con conteo ≠ 0 | **537 pruebas, 0 fallas** (4 esperadas) | Sí |
| Fallas nuevas en la carpeta de 650 | Plan §12 | 0 sobre la línea base | **0 archivos nuevos en rojo**: 5, contra 6 de la línea base. Las fallas quedaron en 8, las mismas que al empezar | Sí |
| Criterios de suspensión | Plan §4.3 | Ninguno alcanzado | Ninguno | Sí |

**Lo que no se cumplió:** nada.

---

## 6. Veredicto de la fase

**Concepto:** **Cumple**

**Justificación:** los cinco criterios y los dos requisitos no funcionales quedaron cubiertos por casos ejecutados (§5) y las once metas del plan se alcanzaron (§5.1). **Los dos casos escritos para poder tumbar la fase se ejecutaron y decidieron**: `CP-001` la dejó pasar —el `__init__.py` no rompió ninguno de los 61— y **`CP-006` tumbó el enganche que se planeaba**, no la fase: con 9,6 minutos y 16 commits por día, ninguna opción que corriera las pruebas cabía en el umbral, así que se cuelga el reclamo. Los cuatro defectos salieron del sabotaje y de las mediciones, no del ciclo.

**Qué falta para que cumpla:** nada.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-00 | La línea base, los 67 con nombre | [linea-base-t00.txt](../../../../../historico-chat/scripts/2026-08-28/linea-base-t00.txt) |
| EV-01 | La misma corrida con el `__init__.py` | [t01-con-init.txt](../../../../../historico-chat/scripts/2026-08-28/t01-con-init.txt) |
| EV-02 | Las 22 pruebas de la fase | `validadores/pruebas.py`, clase `LasPruebasQueExistenSeCorren` |
| EV-03 | La corrida de las 650 | [salida-internas.txt](../../../../../historico-chat/scripts/2026-08-28/salida-internas.txt) |
| EV-04 | La orden documentada | `validadores/README.md`, sección de las dos suites |
| EV-05 | La medición de dónde colgar | [t04-donde-cuelga.py](../../../../../historico-chat/scripts/2026-08-28/t04-donde-cuelga.py) |
| EV-06 | El enganche | `.githooks/pre-push`, línea 46 |
| EV-07 | Los seis rojos declarados | [funcionalidad_implementada.md](funcionalidad_implementada.md) §6 |
| EV-08 | Los doce sabotajes | [sabotajes-hu021.py](../../../../../historico-chat/scripts/2026-08-28/sabotajes-hu021.py) |

---

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-08-28 | 9 | 0 | Primera ejecución |
