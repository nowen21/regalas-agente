# Resultado de Pruebas — Fase G-EP-008-HU-003: se ve el estado de un proyecto   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección "qué se probó" del `funcionalidad_implementada.md`. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar: se aprobó antes y así se queda.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `G-EP-008-HU-003-se-ve-el-estado-de-un-proyecto` |
| **HU** | [HU-003 Ver el estado de un proyecto](../HU-003-ver-el-estado-de-un-proyecto.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md), aprobado el 2026-08-25 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-25 |
| **Ejecutado por** | El agente, en la máquina del usuario |
| **Ambiente y versión** | Windows 11, Python 3.11.9, Django 5.2.11. Sobre `plataforma/`, sin commit todavía |

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 9 | 9 | 9 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

**145 comprobaciones automáticas**, las 126 que ya existían más 19 de esta fase. Se validaron con **siete sabotajes**, y los siete quedaron cazados a la primera.

**El estado del repositorio real, que es lo que la fase vino a producir:**

```
etapas del ciclo con documento : 7 de 7
fases en total                 : 127
fases todavía abiertas         :  41
fases que no se dejan leer     :   5   (nombradas, con su ruta)
documentos aprobados           : 228 de 994
última aprobación              : 2026-08-25
```

---

## 2. Ejecución caso por caso

### CP-001 · Las etapas del ciclo entran al traer

**El problema que resuelve:** sin las etapas adentro, el estado no puede decir qué etapas tienen documento, que es la mitad de `CA-01`.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Armar un proyecto con sus siete etapas en `cvds/` y traerlo | Las siete entran, reconocidas como etapas | Las siete |
| 2 | Armar otro con documentos propios de etapa: modelo de datos, acta de constitución | Entran con su tipo | Los dos |
| 3 | Comprobar que el `README.md` de una etapa **no** se confunde con un índice | El de `cvds/planificacion/` es etapa; el de `documentacion/epicas/` es índice | Distintos |
| 4 | Traer el repositorio real | Entran las siete etapas y sus documentos | 994 documentos, con 7 etapas del ciclo entre ellos |

**Cómo se verificó que la pareja cumple:** el paso 3 es el que decide, y es el que el nombre solo no resuelve. Dos archivos que se llaman igual son documentos distintos según dónde están, y tratarlos igual habría dejado las siete etapas contadas como índices.

**Este caso existe porque una fase cerrada tenía un defecto.** La fase E declaraba que recorría «la documentación del ciclo de vida» y no recorría las etapas del ciclo, que viven en otra carpeta. Peor: esa carpeta tampoco estaba en la lista de las que se declaran como no miradas, así que **se saltaba en silencio**. Queda anotado en el cierre.

### CP-002 · El estado dice qué etapas tienen documento

**El problema que resuelve:** un estado que solo lista lo que hay no deja ver qué falta, que es justamente para lo que se mira.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Traer un proyecto con cuatro de las siete etapas | Dice cuáles cuatro tiene | Cuatro |
| 2 | Preguntar por las que faltan | **Dice cuáles tres no tiene** | Tres, con `pruebas` entre ellas |
| 3 | Mirar la pantalla | Las que faltan también se ven | Sale la fila «Etapas todavía sin documento» |
| 4 | Sobre el repositorio real | Las siete tienen documento | 7 de 7 |

**Cómo se verificó que la pareja cumple:** el paso 2 es el que decide. Es la diferencia entre un estado que informa y uno que solo enumera.

### CP-003 · El estado dice cuántas fases hay y en qué estación

**El problema que resuelve:** saber cuántas fases quedaron abiertas es el dato que dice si un proyecto está al día o tiene trabajo colgando.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Traer un proyecto con tres fases: una en la estación 6, una en la 9, y una que dice «cerrada» | Cuenta las tres | 3 |
| 2 | Contar las abiertas | Solo la de la estación 6 | 1 |
| 3 | Sobre el repositorio real | Dice cuántas hay y cuántas siguen abiertas | **127 fases, 41 abiertas** |

**Cómo se verificó que la pareja cumple:** el paso 1 mete las dos formas de estar cerrada que aparecen de verdad —el número final y la palabra «cerrada»— porque contar solo una dejaría la otra como abierta.

### CP-004 · Una estación que no se deja leer se dice, no se supone

**El problema que resuelve:** hay **doce formas distintas** de escribir en qué estación va una fase, y cinco de los 125 estados del repositorio no se dejan leer. Suponer que están cerradas daría un número falso, y suponerlas abiertas también.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Traer un proyecto con una fase legible y otra cuya estación dice «ya casi, falta poco» | Cuenta las dos fases | 2 |
| 2 | Contar las abiertas | Solo la legible | 1 |
| 3 | Contar las ilegibles | Una, **con su ruta** | Una, con `EP-001/B` en la ruta |
| 4 | Traer un proyecto con **solo** una fase ilegible | Ni abierta ni cerrada | 1 fase, 0 abiertas, 1 ilegible |
| 5 | Mirar la pantalla | Dice cuáles no se pudieron leer | Las nombra |
| 6 | Sobre el repositorio real | Las cinco salen con su ruta | Las cinco, nombradas |

**Cómo se verificó que la pareja cumple:** el paso 4 es el que decide. Una fase ilegible tiene que quedar **fuera de las dos cuentas**: si se sumara a las abiertas o a las cerradas, el número sería una afirmación sobre lo que no se leyó. Sobre el repositorio real la diferencia es concreta: 41 abiertas y 5 sin saber, en vez de 46 abiertas inventadas.

### CP-005 · Lo aprobado se distingue, y se dice con palabras

**El problema que resuelve:** `CA-03` pide decirlo **con palabras**. Un color no se lee en voz alta ni lo distingue quien no ve los colores.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Traer un proyecto con dos documentos aprobados y uno sin aprobar | Cuenta dos de tres | 2 de 3 |
| 2 | Preguntar desde cuándo | Trae la fecha de la aprobación | `2026-08-25` |
| 3 | Mirar la pantalla | Dice «están aprobados», con la fecha | Las dos cosas |
| 4 | Sobre el repositorio real | Dice cuántos | **228 de 994** |

**Cómo se verificó que la pareja cumple:** el paso 3 busca las palabras en la pantalla, no una clase de estilo. Es lo único que comprueba que se dijo, y no que se pintó.

### CP-006 · Un proyecto sin nada dice qué haría falta

**El problema que resuelve:** una pantalla vacía se lee como un error de la plataforma, y el usuario no sabe si falló o si no hay nada.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Conectar un proyecto y pedir su estado sin traer nada | Dice `sin empezar` | `sin empezar` |
| 2 | Preguntar qué haría falta | Dice traer lo escrito, y que si no hay, lo primero es planificación | Lo dice |
| 3 | Repetir con un proyecto cuya **ruta se perdió** | Lo que falta es **otra cosa** | «corregir dónde vive su código» |
| 4 | Mirar la pantalla | No queda vacía | Sale «Sin empezar» y «Para empezar...» |

**Cómo se verificó que la pareja cumple:** el paso 3 es el que decide. Decirle «traiga su documentación» a alguien cuya carpeta no está sería un consejo inútil: primero hay que arreglar la ruta. Un mensaje que no mira el caso es tan malo como no tenerlo.

### CP-007 · Con la ruta perdida, el estado se ve igual

**El problema que resuelve:** un proyecto entregado, archivado o movido de máquina tiene que seguir mostrando su estado.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Traer un proyecto con etapas y fases | Queda el punto de partida | Quedó |
| 2 | **Borrar su carpeta entera** | La ruta queda perdida | Perdida |
| 3 | Pedir la pantalla | El estado sale completo | Sale, con sus etapas |
| 4 | Buscar el aviso de la ruta | Está, al lado del estado | Está |

**Cómo se verificó que la pareja cumple:** el paso 3 comprueba que el estado sigue, y el 4 que el aviso no lo tapa. Las dos cosas: un estado sin aviso escondería el problema, y un aviso sin estado dejaría al usuario sin lo que vino a ver.

### CP-008 · Cincuenta proyectos con estado listan bajo un segundo

**El problema que resuelve:** calcular el estado es más caro que no calcularlo, y `RNF-02` no cambió por eso.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Conectar cincuenta proyectos, **cada uno con documentación traída** | Quedan los cincuenta, con documentos | 50 |
| 2 | Pedir la lista, midiendo | Responde | 200 |
| 3 | Comparar con el límite | Menos de un segundo | **0,278 s** |
| 4 | Escribir el número | Queda en la salida de la prueba | Queda |

**Cómo se verificó que la pareja cumple:** el paso 1 es el que hace válida la medición. Medir con cincuenta proyectos vacíos habría dado un número bonito y falso, porque no habría nada que calcular. El margen real es de casi cuatro veces, no de cien como en la fase C, y eso también es información.

### CP-009 · Que NO pase: que calcular el estado lea la carpeta del proyecto

**El problema que resuelve:** si el estado se calculara leyendo el proyecto, la plataforma dependería de que el proyecto esté ahí. Y `CA-01` dice «sin abrir su carpeta».

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Traer un proyecto con etapas, fases y aprobaciones, y anotar **todo** su estado | Queda la comparación | Ocho datos anotados |
| 2 | Borrar su carpeta entera | La ruta se pierde | Perdida |
| 3 | Volver a calcular el estado y comparar los ocho datos | **Idénticos** | Idénticos |
| 4 | Sobre el repositorio real, apuntar el proyecto a una carpeta que no existe | El estado no cambia | 994 documentos, 127 fases, 41 abiertas, 228 aprobados: **iguales** |

**Cómo se verificó que la pareja cumple:** el paso 3 compara **todos** los datos del estado, no solo uno. Un código que leyera la carpeta para una sola cosa —por ejemplo, las etapas— habría pasado una comprobación parcial. El paso 4 lo repite sobre el caso real, que es el que tiene las 127 fases.

**Tabla de casos ejecutados:**

| Caso | Qué exige | Prioridad | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | El hueco de la fase E | Crítica | 2026-08-25 | Las siete etapas entraron reconocidas; el `README.md` de una etapa no se confunde con un índice | Aprobado | EV-01, EV-03 | — |
| CP-002 | `CA-01` | Crítica | 2026-08-25 | Cuatro de siete etapas: dice las cuatro que hay **y las tres que faltan** | Aprobado | EV-01 | — |
| CP-003 | `CA-01` | Crítica | 2026-08-25 | Tres fases, una abierta. Sobre el repositorio real: 127 fases, 41 abiertas | Aprobado | EV-01, EV-03 | — |
| CP-004 | `04·R4` | Crítica | 2026-08-25 | Una fase con la estación ilegible quedó fuera de las dos cuentas, nombrada. En el repositorio real son cinco | Aprobado | EV-01, EV-03 | — |
| CP-005 | `CA-03` | Alta | 2026-08-25 | Dos de tres aprobados, con su fecha, y la pantalla lo dice con palabras. En el real: 228 de 994 | Aprobado | EV-01, EV-03 | — |
| CP-006 | `CA-02` | Alta | 2026-08-25 | Un proyecto sin nada dice qué haría falta, y uno con la ruta perdida dice **otra cosa** | Aprobado | EV-01 | — |
| CP-007 | Transversal | Alta | 2026-08-25 | Con la carpeta borrada, la pantalla sigue mostrando las etapas y el aviso | Aprobado | EV-01 | — |
| CP-008 | `RNF-02` | Alta | 2026-08-25 | Cincuenta proyectos **con documentación traída**: 0,278 s contra un límite de 1 s | Aprobado | EV-01 | — |
| CP-009 | `CA-01` | Crítica | 2026-08-25 | Los ocho datos del estado idénticos con la carpeta borrada, y lo mismo sobre el repositorio real | Aprobado | EV-01, EV-03 | — |

**Correspondencia con el plan:** 9 casos en el plan, 9 acá.

**Qué salió distinto de lo esperado:** nada falló. Apareció un documento sin molde que antes no se veía, explicado abajo.

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que las pruebas cacen lo que dicen cazar | Siete sabotajes, restaurando con copia, limpiando rastros y corriendo la suite al final | Los siete cazados a la primera |
| 2 | Que el estado del repositorio real sea correcto | Se calculó y se leyeron sus números | 7 de 7 etapas, 127 fases, 41 abiertas, 228 aprobados |
| 3 | Que las cinco fases ilegibles sean reales | Se leyeron sus rutas | Son cinco fases del repositorio, nombradas una por una |
| 4 | Que el estado no dependa del proyecto | Se apuntó el proyecto a una carpeta que no existe | Los seis datos comparados salieron **idénticos** |
| 5 | Que los datos de prueba no quedaran | Se borraron y se rehicieron los tres índices | Cero en los tres |

**Un documento sin molde que antes no se veía.** Al entrar `cvds/`, el repositorio pasó a tener un archivo sin reconocer: `cvds/cumplimiento.md`. **No es un fallo**: es un documento propio de este repositorio que el estándar no tiene como molde, y el módulo hace lo que debe —lo reporta en vez de adivinar—, que es lo que `CA-4` de la fase E pide. Queda como deuda en el cierre.

---

## 4. Defectos encontrados

Ninguno en el código de esta fase.

**Un defecto en una fase ya cerrada**, encontrado al planear esta:

| ID | Título | Dónde estaba | Severidad | Estado |
|---|---|---|---|---|
| DEF-E1 | La fase E declaraba recorrer «la documentación del ciclo de vida» y no recorría las etapas del ciclo, que viven en `cvds/`. Y esa carpeta **tampoco estaba declarada como no mirada**, así que se saltaba en silencio, contra `RN-4` | Fase E, cerrada en el commit `c998695` | Alta | Corregido en esta fase, tarea 1 |

**Cómo pasó desapercibido en la fase E.** Sus nueve casos y sus ocho sabotajes probaban que se traía lo que se decía traer, y ninguno preguntaba **si lo que se decía traer era todo**. La comprobación que lo habría cazado es la que esta fase necesitó: intentar usar lo traído para responder una pregunta concreta.

**Defectos abiertos que se aceptan y por qué:** ninguno.

---

## 5. Veredicto por criterio de aceptación

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| `CA-01` el estado se ve sin abrir la carpeta | CP-002, CP-003, CP-009 | Etapas, fases y aprobaciones, y con la carpeta borrada sale idéntico | Sí |
| `CA-02` un proyecto sin trabajo abierto lo dice | CP-006 | Dice `sin empezar` y qué haría falta, distinto según el caso | Sí |
| `CA-03` lo aprobado se distingue, con palabras | CP-005 | «están aprobados», con la fecha | Sí |
| Transversal `RNF-02` | CP-008 | 0,278 s con cincuenta proyectos con documentación | Sí |
| Transversal: ruta perdida | CP-007 | El estado sale completo, con el aviso al lado | Sí |
| `04·R4` no afirmar sobre lo que no se leyó | CP-004 | Cinco fases ilegibles fuera de las dos cuentas, nombradas | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Los nueve casos con veredicto escrito | Plan de pruebas §7 | 9 | 9 | Sí |
| Ningún caso en **No cumple** sin corregir | Plan de pruebas §7 | 0 | 0 | Sí |
| El número de la medición escrito | Plan de pruebas §7 | El dato | 0,278 s | Sí |
| Pruebas validadas con sabotaje | Plan de pruebas §7 | Todas las promesas | 7 sabotajes, 7 cazados | Sí |
| El defecto de la fase E anotado en su documento de cierre | Plan de pruebas §7 | Anotado | Anotado, con su fecha y su porqué | Sí |

**Lo que no se cumplió:** nada quedó corto.

---

## 6. Veredicto de la fase

**Concepto:** **Cumple**.

**Justificación:** los tres criterios de la historia quedaron probados por el paso que de verdad los decide: comparar **todos** los datos del estado con la carpeta borrada, no uno solo; contar las etapas **que faltan** y no solo las que hay; y dejar las fases ilegibles **fuera de las dos cuentas** en vez de repartirlas.

Y la fase produjo lo que vino a producir: la plataforma ya dice que este repositorio tiene **41 de sus 127 fases abiertas**, un dato que antes no existía en ninguna parte.

**Qué falta para que cumpla:** nada. **Con esto la HU-003 queda cerrada**, y con ella la épica `EP-008` completa: sus cuatro historias tienen sus criterios probados.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Salida de las 145 comprobaciones automáticas, con las mediciones | [evidencias/EV-01-pruebas-automaticas.txt](evidencias/EV-01-pruebas-automaticas.txt) |
| EV-02 | Los siete sabotajes, y qué prueba cazó cada uno | [evidencias/EV-02-las-pruebas-cazan-el-sabotaje.txt](evidencias/EV-02-las-pruebas-cazan-el-sabotaje.txt) |
| EV-03 | Corrida real: el estado de este repositorio, y `CP-009` sobre él | [evidencias/EV-03-corrida-real.txt](evidencias/EV-03-corrida-real.txt) |

---

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-08-25 | 9 | 0 | Primera ejecución |
