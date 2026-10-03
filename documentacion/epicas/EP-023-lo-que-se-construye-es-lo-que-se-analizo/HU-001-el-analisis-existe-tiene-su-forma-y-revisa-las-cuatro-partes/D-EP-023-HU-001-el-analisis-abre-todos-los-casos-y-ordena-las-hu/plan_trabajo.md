# Plan de Trabajo · Fase `D-EP-023-HU-001-el-analisis-abre-todos-los-casos-y-ordena-las-hu` (módulo `plantillas/` y `validadores/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

**Versión 2**, del 2026-10-02. Cambia frente a la 1 por el [análisis 9](../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-9.md): el CA-20 en su versión siguiente, los CA-23 a CA-26, las recomendaciones consultadas de los análisis 1 a 9 en el CA-19, la versión 44.0.0 y la duda de 2.7 resuelta.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `D-EP-023-HU-001-el-analisis-abre-todos-los-casos-y-ordena-las-hu` |
| **Épica** | [EP-023](../../epica.md) |
| **HU** | [HU-001](../HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md), una sola (`F12.1`) |
| **Módulo** | `plantillas/`, `validadores/`, `analisis/` y `base/13-documentacion/` |
| **Especificación del módulo** | Los CA-17 a CA-26 de la HU-001 |
| **Fecha apertura** | 2026-10-02 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): complementa las fases A a C de la HU-001. Sale de los puntos 2, 3, 5, 7, 8 y 11 de «Lo que se tiene que hacer» del [análisis 8](../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-8.md) y de los puntos 1, 2, 3, 5, 6, 8 y 9 del [análisis 9](../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-9.md). El punto 6 del análisis 9 es esta versión del plan.

**Carencias que cierra** (`02·F14` Q3): el análisis se quedaba en el caso que lo destapó, el orden de las HU no tenía razón, lo aprendido no quedaba para el análisis siguiente (análisis 8, H-8), y el análisis principal solo anotaba los análisis que cambiaban algo (análisis 9, H-11).

**Aprobación** (`02·F4`): el usuario aprobó la versión 2 el 2026-10-02.

**Disparo** (`02·F15`, etapa 2): el usuario pidió escribir esta fase el 2026-10-02 con «Escriba», y su versión 2 con «Hágalo».

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-001 | Estado |
|---|---|
| CA-17 · El análisis abre todas las posibilidades | ☑ |
| CA-18 · Las HU salen con su dependencia y su orden | ☑ |
| CA-19 · Las recomendaciones del análisis | ☑ |
| CA-20 · El análisis principal al día | ☑ |
| CA-21 · Medir la respuesta antes de entregarla | ☑ |
| CA-22 · Las secciones nuevas no reabren los análisis aprobados | ☑ |
| CA-23 · Todo análisis aprobado se anota en el principal | ☑ |
| CA-24 · La sección «Lo que aporta al análisis principal» | ☑ |
| CA-25 · Sin una fila en «Lo que se tiene que hacer» no se aprueba | ☑ |
| CA-26 · Sin «Lo que aporta» no se aprueba | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que todo análisis nuevo consulte las recomendaciones, considere dónde más puede pasar lo mismo, entregue sus HU con su dependencia y su orden, y diga lo que suma al análisis principal; que el programa de aprobar pase eso tal cual al principal y no apruebe sin ello, y que un validador lo compruebe sin reabrir los análisis ya aprobados.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-17 | La sección «Dónde más puede pasar» en la plantilla; el validador no deja cerrar un análisis con un caso sin cubrir | Plantilla y validador | Media |
| CA-18 | La tabla de HU con dependencia, orden y razón, en el análisis y en la hoja de ruta de la épica; el validador detiene el orden que no respeta la dependencia | Plantilla y validador | Media |
| CA-19 | El archivo de recomendaciones, sus dos niveles, la sección que lo enlaza, el validador y las recomendaciones consultadas de los análisis 1 a 9 | Plantilla, documentos y validador | Alta |
| CA-20 | El análisis principal es la redacción que forman los aportes, con su «Lista de análisis»; el aviso | Documento y validador | Media |
| CA-21 | La recomendación de medir la respuesta antes de entregarla | Documento | Baja |
| CA-22 | El validador exige lo nuevo solo a los análisis aprobados desde la versión que lo trae | Validador | Media |
| CA-23 | `13·DOC25` pide anotar todo análisis aprobado, con lo que aportó tal cual | Regla | Baja |
| CA-24 | La sección «Lo que aporta» en la plantilla; el programa de aprobar la pasa al principal; el validador compara | Plantilla, programa y validador | Alta |
| CA-25 | El programa de aprobar no aprueba sin filas en «Lo que se tiene que hacer» | Programa | Baja |
| CA-26 | El programa de aprobar no aprueba sin «Lo que aporta» | Programa | Baja |

**Fuera de alcance:**

- La columna de las lecciones que dice qué recomendación complementan: es el CA-02 de la HU-006.
- Crear análisis principales de módulo: el programa usa el de su alcance si existe, y si no, el del proyecto.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-02, sobre la versión 43.0.0:

- `plantillas/analisis.md` tiene, en orden: hallazgo, pendiente, conversación, «Lo acordado», «Lo que aportó cada parte» con sus cuatro partes, propuesta final con la tabla de HU (número, título, parte del problema, puntos) y una línea libre para el orden, lecciones y «Lo que se tiene que hacer». No tiene recomendaciones, «Dónde más puede pasar» ni «Lo que aporta al análisis principal».
- Los análisis 1 a 8 del piloto ya tienen «Lo acordado», «Dónde más puede pasar» (del 1 al 7) y «Lo que aporta al análisis principal»; los análisis 1 y 2, la tabla de HU con su orden; el análisis 9 tiene todo eso. Ninguno dice qué recomendaciones consultó, porque el archivo no existe.
- `plantillas/ciclo-vida-proyectos/03-epica.md`, sección 15, reparte las HU en fases de entrega con fecha; no tiene dependencia, orden ni razón.
- `validadores/analisis.py` revisa que un análisis aprobado traiga las cuatro partes. No sabe con qué versión se aprobó.
- `analisis_en_curso.aprobar()` pone la marca con la fecha y el turno, sin la versión, y no revisa nada antes de ponerla.
- El análisis principal, `analisis/proyecto-2026-10-02-analisis-principal.md`, tiene «Qué es Cimiento», «Qué se construye hoy» y una «Lista de cambios» con los análisis 1, 2, 4 y 5.
- `13·DOC25` pide reescribir el principal solo «cuando un análisis individual cambia algo».
- Los análisis 1 a 8 dejaron 36 lecciones; con ellas se arman las recomendaciones de arranque.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `plantillas/analisis.md` | Modificar | Plantilla | «Recomendaciones» al inicio, «Dónde más puede pasar», la tabla de HU con dependencia, orden y razón, y «Lo que aporta al análisis principal» |
| `plantillas/recomendaciones-del-analisis.md` | Nuevo | Plantilla | Las recomendaciones de Cimiento, con su forma y las de arranque |
| `plantillas/ciclo-vida-proyectos/03-epica.md` | Modificar | Plantilla | La hoja de ruta con dependencia, orden y razón |
| `base/13-documentacion/reglas/DOC25-reescribe-el-analisis-principal-con-su-lista-de-cambios.md` | Modificar | Regla | Todo análisis aprobado se anota, con lo que aportó tal cual |
| `validadores/analisis.py` | Modificar | Validador | Las comprobaciones de los CA-17 a CA-20 y CA-24, con la puerta de versión del CA-22 |
| `validadores/analisis_en_curso.py` | Modificar | Programa | La marca con la versión; aprobar revisa las filas y la sección, y pasa lo que suma al principal |
| `adaptadores/claude-code/hook_analisis.py` | Modificar | Enganche | Dice por qué no se aprobó |
| `validadores/plantillas.py` | Modificar | Validador | Registra `recomendaciones-del-analisis.md` |
| `validadores/tests/test_analisis.py` y `validadores/tests/test_analisis_en_curso.py` | Modificar | Pruebas | Los casos del plan de pruebas |
| `analisis/proyecto-2026-10-02-analisis-principal.md` | Modificar | Documentación | La redacción que forman los aportes y la «Lista de análisis» |
| Los análisis 1 a 9 del pendiente 103 | Modificar | Documentación | Las recomendaciones consultadas, con la nota del piloto |
| `historico-chat/memory/el-analisis-cubre-todos-los-casos.md` y `historico-chat/memory/memory.md` | Modificar | Documentación | El recuerdo pasa a enlazar la R-1, sin copiarla |
| `anatomia/mapa-del-sitio.md` | Modificar | Documentación | Nombra el archivo de recomendaciones |
| `CHANGELOG.md` y `VERSION` | Modificar | Versión | 44.0.0 |
| Los documentos de esta fase, la HU-001 y el resumen de la sesión | Modificar | Documentación | Cierre |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| La marca de aprobado suma la versión | `analisis.aprobado()`, `analisis_en_curso.turno_aprobado()`, `origen.py` | Las expresiones siguen encontrando la marca; se prueba |
| `aprobar()` puede negarse y dice por qué | `hook_analisis.py` | El enganche muestra el motivo en vez de la nota de aprobado |
| La plantilla del análisis suma secciones | `analisis_en_curso.prender()`, que crea el análisis desde la plantilla | Los análisis nuevos nacen con las secciones |
| El análisis principal cambia de forma | `validar.py analisis`, la fase C de la HU-001 | El aviso lee la «Lista de análisis»; la fase C quedó cerrada con la forma anterior y no se reabre |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La puerta de versión se lee de la marca de aprobado, que desde ahora dice la versión | Compararla por fecha | La fecha no dice qué reglas regían; la versión sí, y no depende del reloj |
| Las recomendaciones de Cimiento viven en `plantillas/recomendaciones-del-analisis.md`; las de cada proyecto, en `analisis/recomendaciones.md` del proyecto, que nace con la primera | Que el instalador cree el archivo del proyecto vacío | Un archivo vacío no aporta, y crearlo no está en los criterios |
| Las comprobaciones nuevas van en `analisis.py`, bajo `13·DOC24` y `13·DOC25` | Una regla nueva | Son secciones de la plantilla del análisis, como las cuatro partes que `analisis.py` ya revisa |
| El principal de su alcance se busca subiendo desde la carpeta del análisis: el primer `analisis/*-analisis-principal.md` que aparezca; si no hay ninguno, el del proyecto | Pedir el alcance en cada análisis | Cubre el módulo que tenga su propio principal sin pedir un dato más, y cae en el del proyecto si no lo tiene (análisis 9, punto 5 de «Lo acordado») |
| Lo que suma un análisis se agrega al final de la redacción del principal, y su fila al final de la «Lista de análisis» | Reescribir la redacción | El análisis 9 acordó que pasa tal cual; reescribir es redactar de nuevo |
| El aviso del CA-20 revisa todos los análisis aprobados, sin puerta de versión | Pasarlo por la puerta del CA-22 | Así lo acordó el análisis 9 (punto 4 de «Lo acordado»), y los diez análisis quedan en la lista con esta fase |
| `13·DOC25` conserva su ID, su título y su archivo; cambia su texto | Renombrarla | Especificaciones y fases la citan por su ruta (`20·M11`) |
| La versión sube a 44.0.0, MAYOR | MENOR | Todo análisis nuevo tiene que traer las secciones nuevas, y no se aprueba sin ellas |

### 2.7 Dudas por resolver antes de codificar

Ninguna. La de la versión 1, sobre el aviso del CA-20 y el análisis 3, la resolvió el análisis 9: se anotan todos.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| Plantilla del análisis | Sin recomendaciones, otros casos ni aporte; orden de HU en texto libre | Recomendaciones al inicio, «Dónde más puede pasar», tabla de HU con dependencia, orden y razón, y «Lo que aporta al análisis principal» | `13·DOC24`, `13·DOC25` |
| Plantilla de la épica | Hoja de ruta por fases de entrega | Hoja de ruta con dependencia, orden y razón | `13·DOC16` |
| `13·DOC25` | Anota el análisis que cambia algo | Anota todo análisis aprobado, con lo que aportó tal cual | `13·DOC25` |
| `analisis.py` | Cuatro partes | Además: casos cubiertos, orden de HU y recomendaciones desde la 44.0.0; aviso de la lista y copia idéntica de lo que suma, en todos | `13·DOC24`, `13·DOC25` |
| `aprobar()` | Pone la marca con fecha y turno | Revisa las filas y la sección, pone la marca con la versión y pasa lo que suma al principal | `13·DOC24`, `13·DOC25` |
| Análisis principal | «Qué es Cimiento», «Qué se construye hoy» y «Lista de cambios» | La redacción que forman los aportes y la «Lista de análisis» con los diez análisis | `13·DOC25` |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-22 · Las secciones nuevas no reabren los análisis aprobados

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-09 | La marca de aprobado suma «con la versión X.Y.Z», leída de `VERSION`. `analisis.py` lee esa versión y exige lo nuevo solo desde 44.0.0; sin versión en la marca, no lo exige | `validadores/analisis_en_curso.py`, `validadores/analisis.py` | CA-22 | Los análisis que se aprueben desde ahora | 1 h | Ninguna | CP-006 |

### CA-17 · El análisis abre todas las posibilidades

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | Sumar la sección «Dónde más puede pasar» al final de «Lo que aportó cada parte», con su nota y la tabla de caso, dónde se presenta, riesgo y lo que lo cubre | `plantillas/analisis.md` | CA-17 | Los análisis nuevos | 0,3 h | Ninguna | CP-001 |
| T-02 | Falla si un análisis aprobado desde 44.0.0 no tiene la sección, o si una fila deja vacía la columna de lo que lo cubre | `validadores/analisis.py` | CA-17 | Ninguno en los aprobados antes | 1 h | T-09 | CP-001 |

### CA-18 · Las HU salen con su dependencia y su orden

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-03 | Cambiar la tabla de HU de la propuesta final a orden, HU, título, parte del problema, depende de, por qué en ese orden y puntos, con la nota de que el número identifica y el orden sale de las dependencias | `plantillas/analisis.md` | CA-18 | Los análisis nuevos | 0,3 h | Ninguna | CP-002 |
| T-04 | Cambiar la hoja de ruta a orden, HU, depende de, por qué y estado | `plantillas/ciclo-vida-proyectos/03-epica.md` | CA-18 | Las épicas nuevas | 0,3 h | Ninguna | CP-002 |
| T-05 | Falla si en la tabla de HU una va antes de una de la que depende, o un puesto no tiene razón | `validadores/analisis.py` | CA-18 | Ninguno en los aprobados antes | 1 h | T-09 | CP-002 |

### CA-19 · Las recomendaciones del análisis

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-06 | Crear el archivo con su forma (número, qué se hace, por qué, de qué análisis sale), sus dos niveles y las recomendaciones de arranque sacadas de las 36 lecciones de los análisis 1 a 8, juntando las que dicen lo mismo; registrarlo en el diccionario de plantillas y en el mapa del sitio | `plantillas/recomendaciones-del-analisis.md`, `validadores/plantillas.py`, `anatomia/mapa-del-sitio.md` | CA-19 | Los análisis nuevos | 1,5 h | Ninguna | CP-003 |
| T-07 | Sumar al inicio la sección «Recomendaciones», que enlaza el archivo de Cimiento y el del proyecto y pide decir cuáles aplican | `plantillas/analisis.md` | CA-19 | Los análisis nuevos | 0,3 h | T-06 | CP-003 |
| T-08 | Falla si una recomendación no cita su análisis, si dos tienen el mismo «qué se hace», o si un análisis aprobado desde 44.0.0 no dice cuáles consultó | `validadores/analisis.py` | CA-19 | Ninguno en los aprobados antes | 1 h | T-06, T-09 | CP-003 |
| T-15 | Sumar a los análisis 1 a 9 la sección «Recomendaciones», con la nota del piloto: ninguno consultó recomendaciones porque el archivo no existía, y se nombran las que salieron de sus lecciones | Los análisis 1 a 9 del pendiente 103 | CA-19 | Ninguno: no decide nada nuevo | 0,5 h | T-06 | CP-003 |
| T-12 | Dejar el recuerdo «El análisis cubre todos los casos» enlazando la R-1, con el registro de que el usuario lo pidió | `historico-chat/memory/el-analisis-cubre-todos-los-casos.md`, `historico-chat/memory/memory.md` | CA-19 | Ninguno | 0,2 h | T-06 | CP-003 |

### CA-21 · Medir la respuesta antes de entregarla

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-13 | Escribir la recomendación de medir la respuesta contra `00·ID9` antes de entregarla, con su origen en el análisis 8 | `plantillas/recomendaciones-del-analisis.md` | CA-21 | Los análisis nuevos | 0,1 h | T-06 | CP-005 |

### CA-23 · Todo análisis aprobado se anota en el principal

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-16 | Cambiar el texto de `DOC25`: cada análisis aprobado se anota en el análisis principal de su alcance, aunque no cambie el sistema, y lo que aportó pasa tal cual; ejemplo INCORRECTO/CORRECTO nuevo; checklist de nuevo contra 44.0.0; regenerar `base/reglas-por-tarea/` y el mapa de tareas | `base/13-documentacion/reglas/DOC25-reescribe-el-analisis-principal-con-su-lista-de-cambios.md`, `base/reglas-por-tarea/`, `base/mapa-de-tareas.md` | CA-23 | Todo proyecto que adopte la versión | 0,5 h | Ninguna | CP-008 |

### CA-24 · La sección «Lo que aporta al análisis principal»

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-17 | Sumar al final la sección «Lo que aporta al análisis principal», con su nota, el resultado (ratifica, aclara, amplía, modifica la idea o cambia lo que se construye) y lo que suma | `plantillas/analisis.md` | CA-24 | Los análisis nuevos | 0,2 h | Ninguna | CP-009 |
| T-18 | Al aprobar, `aprobar()` busca el principal de su alcance (2.6), agrega lo que suma al final de su redacción y una fila con la fecha, el resultado y el enlace al final de la «Lista de análisis» | `validadores/analisis_en_curso.py` | CA-24 | Los análisis que se aprueben desde ahora | 1,5 h | T-17, T-21 | CP-009 |
| T-19 | Falla si lo que suma un análisis aprobado no está, letra por letra, en el principal de su alcance | `validadores/analisis.py` | CA-24 | Los diez análisis, que quedan al día con T-10 | 0,5 h | T-10 | CP-009 |

### CA-25 · Sin una fila en «Lo que se tiene que hacer» no se aprueba

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-20 | `aprobar()` no pone la marca si «Lo que se tiene que hacer» no tiene filas, y devuelve qué falta; el enganche lo dice en el aviso del turno | `validadores/analisis_en_curso.py`, `adaptadores/claude-code/hook_analisis.py` | CA-25 | Los análisis que se aprueben desde ahora | 0,7 h | Ninguna | CP-010 |

### CA-26 · Sin «Lo que aporta» no se aprueba

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-21 | `aprobar()` no pone la marca si falta «Lo que aporta al análisis principal» con sus dos partes, y devuelve qué falta | `validadores/analisis_en_curso.py` | CA-26 | Los análisis que se aprueben desde ahora | 0,3 h | T-20 | CP-011 |

### CA-20 · El análisis principal al día

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-10 | Reescribir el análisis principal: su contenido pasa a ser la redacción que forman los aportes, del análisis con la forma anterior al 9, copiados tal cual y en el orden en que se aprobaron, sin «Qué se construye hoy»; la «Lista de cambios» pasa a «Lista de análisis», con fecha, resultado y enlace de los diez | `analisis/proyecto-2026-10-02-analisis-principal.md` | CA-20 | Ninguno | 0,5 h | Ninguna | CP-004 |
| T-11 | Aviso si un análisis aprobado, de la forma nueva o de la anterior, no aparece en la «Lista de análisis» del principal de su alcance; sin puerta de versión | `validadores/analisis.py` | CA-20 | Ninguno | 0,5 h | T-10 | CP-004 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-14 | Escribir los casos del plan de pruebas; subir a 44.0.0 con «⚠ obliga a migrar» y lo que cada proyecto tiene que hacer (`20·M10`) | `validadores/tests/test_analisis.py`, `validadores/tests/test_analisis_en_curso.py`, `VERSION`, `CHANGELOG.md` | CA-17 a CA-26 | Todo proyecto adopta la versión | 2 h | T-02, T-05, T-08, T-11, T-18, T-19, T-20, T-21 | CP-001 a CP-011 |

## 4. Secuencia de ejecución

T-09 primero, porque las comprobaciones se apoyan en la puerta de versión. Después las plantillas y la regla: T-01, T-03, T-04, T-17, T-06, T-07, T-13, T-12 y T-16. Luego el análisis principal y los análisis del piloto: T-10 y T-15. Luego el programa de aprobar: T-20, T-21 y T-18. Luego los validadores: T-02, T-05, T-08, T-11 y T-19. Al final T-14. Los validadores, las pruebas y la medición de marcas al final (`02·F5`); la suite completa por partes y en primer plano (`04·S9`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-17 | Leer la plantilla; el validador sobre un análisis con un caso sin cubrir | CP-001 |
| CA-18 | Leer las dos plantillas; el validador sobre una tabla con el orden roto | CP-002 |
| CA-19 | Leer el archivo, la plantilla y los análisis 1 a 9; el validador sobre una recomendación sin origen, una repetida y un análisis que no dice cuáles consultó | CP-003 |
| CA-20 | Leer el principal; el validador con un análisis aprobado que no aparece en la lista | CP-004 |
| CA-21 | Leer la recomendación | CP-005 |
| CA-22 | El validador sobre los análisis aprobados y sobre uno nuevo sin las secciones | CP-006 |
| CA-23 | Leer `DOC25` y su checklist | CP-008 |
| CA-24 | Leer la plantilla; aprobar un análisis de prueba y comparar; el validador con una copia cambiada | CP-009 |
| CA-25 | Aprobar un análisis de prueba sin filas | CP-010 |
| CA-26 | Aprobar un análisis de prueba sin «Lo que aporta» | CP-011 |

## 6. Datos y ambiente de prueba

El repositorio del estándar, y carpetas temporales con análisis y análisis principales de prueba.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Cada proyecto adopta la 44.0.0 con el instalador. Sus análisis ya aprobados no tienen que traer las secciones nuevas (CA-22); los que se aprueben desde esa versión las traen y no se aprueban sin filas ni sin «Lo que aporta». El aviso de la lista sí revisa todos los aprobados: el proyecto anota en su principal los que falten.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`13·DOC24`, `13·DOC25`, `13·DOC16`, `20·M2`, `20·M10`, `20·M11`, `20·M12`, `02·F27`, `01·C19`, `00·ID8`, `00·ID9`, `02·F5`, `02·F8`, `02·F18`, `04·S9`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Que cambiar la marca de aprobado rompa a quien la busca | Las expresiones que la leen empiezan por «Aprobado» y siguen sirviendo; lo comprueba el CP-006 |
| Que dos recomendaciones de arranque digan lo mismo con otras palabras | Se juntan al escribirlas, y el validador busca repetidas |
| Que el programa de aprobar escriba en el principal equivocado | La búsqueda del alcance se prueba con un principal de módulo y sin él (CP-009) |
| Que la suite completa pase de diez minutos y la herramienta la mande a segundo plano | Se corre por partes, cada una en primer plano |

## 11. Definition of Done

- [ ] CA-17 a CA-26 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Los validadores y las pruebas sin fallas nuevas, y cero marcas nuevas.
- [ ] `VERSION` y `CHANGELOG.md` en 44.0.0.
- [ ] Aprobación del usuario.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Se llena al cerrar la fase.
