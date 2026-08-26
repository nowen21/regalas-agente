# Plan de Trabajo — Fase `A-EP-004-HU-019-el-inventario-no-guarda-la-cuenta` (módulo Programas de comprobación)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Se escribe **antes** de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-019-el-inventario-no-guarda-la-cuenta` |
| **Épica** | [EP-004](../../epica.md) |
| **HU** | [HU-019](../HU-019-inventario-que-no-se-mantiene-a-mano.md) — **una sola** (`F12.1`) |
| **Módulo** | Programas de comprobación |
| **Especificación del módulo** | **No hay documento aparte, y la regla que lo permite ya existe.** [`02·F19`](../../../../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md) dice que **la redacción del CA es la especificación funcional**. La historia trae alcance, reglas de negocio, criterios con sus pasos y requisitos no funcionales: un documento aparte la repetiría. **Corregido el 2026-08-26:** acá se citó primero la [EP-001 · HU-010](../../../EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) como si estuviera abierta esperando escribir esa regla. Está **cerrada** desde el 2026-08-18, y cerró diciendo «nada nuevo, y ese es el resultado»: el capítulo ya la contestaba dos reglas más abajo, y agregar otra chocaba con `02·F0`. Se afirmó sin leer su estado. |
| **Fecha apertura** | 2026-08-26 |
| **Rama** | `main` — el repositorio trabaja sobre la rama principal |

**ORIGEN** (`13·DOC12`):
- ✨ **Funcionalidad nueva:** una comprobación que hoy no existe, la de que el inventario no guarde una cuenta que el árbol ya sabe.
- 📝 **Modifica lo que dejó la [HU-017](../../HU-017-inventario-de-hu-sin-fase/HU-017-inventario-de-hu-sin-fase.md):** aquella construyó la cuenta y dejó **fuera de alcance** llenar el tablero, con la frase «el programa da la cuenta; el tablero lo escribe una persona». Esa decisión es la que se cambia, y por eso esta fase es híbrida y no solo aditiva.

**CA de la HU que cubre esta fase:**

| CA de `HU-019` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-019-inventario-que-no-se-mantiene-a-mano.md) — el pendiente responde sin guardar la respuesta | ☐ |
| [CA-02](../HU-019-inventario-que-no-se-mantiene-a-mano.md) — reponer un número a mano no pasa desapercibido | ☐ |
| [CA-03](../HU-019-inventario-que-no-se-mantiene-a-mano.md) — la narrativa sobrevive | ☐ |

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que el pendiente del inventario deje de guardar una segunda copia de la cuenta, conserve lo que solo él sabe, y quede una comprobación que impida que la copia vuelva.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | El pendiente remite al comando en vez de guardar la cuenta | Funcional | Baja |
| CA-02 | Reponer un número fijo se reporta, y no se corrige solo | Funcional | Media |
| CA-03 | La narrativa fechada y la condición de cierre sobreviven | Funcional | Media |
| RNF-01 | El pendiente dice de dónde sale la cuenta | No funcional | Baja |
| RNF-02 | La comprobación no agrega un recorrido nuevo | No funcional | Baja |

**Fuera de alcance:**

- **Corregir las filas que faltan.** No se corrigen: la tabla entera se quita.
- **Cambiar cómo se cuenta.** `inventario` en `validadores/fases.py` no se toca.
- **Los demás pendientes que traigan números a mano.** Si los hay, salen de un barrido aparte, que no es esta fase.
- **Marcar la estación del commit**, que es el pendiente [87](../../../../../pendientes/87-la-estacion-del-commit-casi-nunca-se-marca.md).

---

## 2. Análisis previo — línea base verificada  ·  `02·F17`

> Verificado contra el repositorio el 2026-08-26, corriendo los comandos, no de memoria.

**Lo que se midió:**

| Qué | Valor verificado | Cómo se obtuvo |
|---|---|---|
| Lo que dice el encabezado del pendiente | 78 total, 47 completas, 31 incompletas | Leyendo `pendientes/48-inventario-hu.md` |
| Lo que cuenta el árbol | 113 total, 69 completas, 44 incompletas | `python validadores/validar.py fases` |
| Filas de la tabla del pendiente | 74 | Contando las que abren con una épica |
| Párrafos de narrativa fechada | 11 | Contando las citas del archivo |

**Dos cosas que aparecieron al medir y conviene que consten:**

1. **El pendiente no cuadra ni consigo mismo.** Dice 78 historias en el encabezado y su tabla tiene 74 filas. No es solo que esté atrasado contra el árbol: las dos mitades del propio documento ya se habían separado.
2. **El total subió a 113 al escribir la `HU-019`.** La historia que viene a arreglar el conteo entra en el conteo. Es correcto y conviene no confundirlo con un desfase nuevo.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `pendientes/48-inventario-hu.md` | Modificar | Documentación | Se le quitan los tres números y las 74 filas; se conservan los 11 párrafos fechados y la condición de cierre |
| `validadores/fases.py` | Modificar | Servicio | Se agrega la comprobación de `CA-02`, dentro del recorrido que ya hace `validar` |
| `validadores/pruebas.py` | Modificar | Test | La prueba que compara las dos copias se reemplaza por la de `CA-02` |
| `validadores/docs/` | Modificar | Documentación | Solo si el catálogo de lo que comprueba `fases` se lista ahí; se verifica antes de tocar |

### 2.2 Matriz de dependencias

| Archivo a refactorizar | Cambio de contrato | Archivos que dependen (rompen) | Dónde rompe |
|---|---|---|---|
| `validadores/fases.py` | **Ninguno.** `inventario`, `linea_inventario` y `validar` conservan su firma; la comprobación se suma dentro de `validar` | Ninguno | — |
| `pendientes/48-inventario-hu.md` | Deja de tener tres campos y una tabla | `validadores/pruebas.py`, que hoy los lee | La prueba `test_la_cuenta_del_programa_coincide_con_la_del_inventario_escrito`, que por eso se reemplaza en esta misma fase |

**No hay más dependientes.** Se verificó buscando en el repositorio quién más lee ese pendiente.

### 2.3 Rutas / endpoints y control de acceso

**No aplica.** Los programas de comprobación se corren desde la terminal y no exponen rutas.

### 2.4 Punto de entrada

- **Dónde queda accesible:** `python validadores/validar.py fases`, el mismo comando de siempre. La comprobación nueva sale en su reporte, entre las demás.
- **No aplica interfaz gráfica:** esta fase no introduce pantallas.

### 2.5 Permisos / roles a sembrar

**Ninguno.**

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La comprobación vive en `fases.py` | Un validador nuevo | La cuenta la calcula `fases`, y `EP-004 §10.2` pide un solo insumo y un solo resultado. Un archivo aparte recorrería el árbol otra vez para decir lo mismo |
| Se reporta como **aviso**, no como falla | Falla, que detiene el commit | Un pendiente con un número de más no rompe nada; detener el trabajo por eso es lo que hace que se desactiven los enganches. Y `RN-05` de la `HU-017` ya dejó dicho que este recorrido avisa |
| La tabla se **quita**, no se regenera | Un programa aparte que la reescriba, que `§10.2` permitiría | Regenerarla deja dos copias y alguien tiene que acordarse de correrlo: el mismo fallo, más lento |
| Se detecta el **campo**, no cualquier número | Buscar cualquier cifra en el archivo | El pendiente seguirá teniendo números dentro de su narrativa —«68 a 74»— y marcarlos sería ruido que enseña a ignorar el aviso |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | Si alguna de las 74 filas anota trabajo que **solo** está ahí y no en el árbol | Se resuelve leyendo, no preguntando: T-01 las compara una por una antes de quitarlas | Pendiente, y bloquea a T-02 |

> Ninguna tarea de construcción inicia con una duda abierta que la bloquee. T-01 existe para cerrar la única que hay.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — El pendiente responde sin guardar la respuesta

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Comparar las 74 filas contra el árbol y listar lo que solo esté en la tabla | Documentación | 1 h | — | EV-01 |
| T-02 | Quitar del encabezado los tres campos con su número | Documentación | 0.5 h | T-01 | EV-02 |
| T-03 | Escribir en su lugar el comando que da la cuenta, copiable | Documentación | 0.5 h | T-02 | EV-02 |

### CA-02 — Reponer un número a mano no pasa desapercibido

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-04 | Comprobar en `validar` que el pendiente no traiga los campos de la cuenta | Backend | 2 h | — | EV-03 |
| T-05 | Redactar el aviso para que diga qué campo sobra y de dónde sale la cuenta | Backend | 0.5 h | T-04 | EV-03 |
| T-06 | Reemplazar la prueba que compara las dos copias por la de este criterio | Test | 1.5 h | T-04 | EV-03 |

### CA-03 — La narrativa sobrevive

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-07 | Contar los 11 párrafos fechados antes de tocar, y volver a contarlos después | Documentación | 0.5 h | T-01 | EV-04 |
| T-08 | Quitar la tabla, dejando lo que T-01 haya marcado como solo suyo | Documentación | 1 h | T-07 | EV-04 |
| T-09 | Comprobar que la condición de cierre sigue escrita | Documentación | 0.5 h | T-08 | EV-04 |

### RNF — Requisitos no funcionales

| ID | Tarea | Categoría | Est. | Ev. |
|---|---|---|:--:|---|
| T-10 | Verificar que la comprobación no agregue un recorrido del árbol | Rendimiento | 0.5 h | EV-05 |
| T-11 | Sabotear las tres piezas y comprobar que las pruebas las cazan | Calidad | 1.5 h | EV-06 |

**Total estimado:** 10 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-07 → T-08 → T-09

**Paralelizables:** T-04 y T-05 no dependen de que el pendiente ya esté cambiado, así que avanzan en simultáneo. **T-06 se corre al final**, cuando el pendiente ya no trae la cuenta: antes, la prueba nueva fallaría contra el archivo viejo y sería un rojo que no significa nada.

> Solo se tocan los archivos declarados en §2.1 (`02·F8`). Descubrir uno nuevo: PAUSAR, reportar, ampliar el plan con aprobación, no editar por iniciativa.

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Lectura del archivo y corrida del comando que nombra | EV-01, EV-02 | | ☐ |
| CA-02 | Prueba automática, más el caso de que **no** corrija | EV-03 | | ☐ |
| CA-03 | Conteo de párrafos antes y después | EV-04 | | ☐ |
| RNF-01 | El comando escrito en el pendiente se copia, se pega y responde | EV-02 | | ☐ |
| RNF-02 | Se comprueba que no hay un recorrido nuevo del árbol | EV-05 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Lista de lo que solo estaba en la tabla | `resultado_pruebas.md` de esta fase |
| EV-02 | El pendiente después del cambio, y la salida del comando | `resultado_pruebas.md` |
| EV-03 | Reporte de la suite | `resultado_pruebas.md` |
| EV-04 | Conteo de párrafos fechados, antes y después | `resultado_pruebas.md` |
| EV-05 | Comprobación de que el recorrido es el mismo | `resultado_pruebas.md` |
| EV-06 | Los sabotajes y qué cazó cada uno | `resultado_pruebas.md` |

---

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La máquina de quien trabaja. Las pruebas que necesitan un pendiente con números lo arman **en una carpeta temporal**, nunca sobre el archivo real |
| Usuarios de prueba | No aplica: no hay autenticación |
| Datos precargados | Ninguno. El insumo es el propio árbol de épicas |

**Nota sobre `CA-02`.** Su paso 1 dice «hacer una copia de trabajo del pendiente». En la prueba automática eso es un árbol de mentira en carpeta temporal. **El archivo real no se ensucia** para probar, que es lo que dejó rastros en sesiones anteriores.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Los tres archivos están versionados y el cambio es una edición de texto y dos de código. **Se revierte descartando el commit de la fase.** No hay migración, ni datos que reconstruir, ni nada que quede a medias: la tabla que se quita sigue en el historial y se recupera con `git show`.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**No aplica.** Los programas de comprobación se corren a mano y no tienen esquema ni datos desplegados. Quien tenga el repositorio verá el aviso nuevo la próxima vez que corra `validar.py fases`, y el pendiente ya sin la cuenta.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `02·F8` — solo se tocan los archivos de §2.1.
- `02·F17` — todo lo que este plan afirma se verificó corriendo los comandos, y los números están en §2.
- `02·F23` — el pendiente 48 baja a historia y se construye como fase; no se ejecuta desde su archivo.
- `04·R4` — no se afirma sobre lo que no se leyó: por eso T-01 lee las 74 filas antes de que T-08 las quite.
- `08·T4` — las pruebas no tocan el archivo real.
- `13·DOC5` — lo decidido acá se registra como señal.
- `EP-004 §10.2` y `DA-06` — el programa reporta y no corrige. Es lo que hace que la salida sea quitar la copia y no generarla.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que alguna de las 74 filas guarde trabajo que no está en ninguna otra parte | Se perdería al quitar la tabla | T-01 las compara una por una **antes** de que T-08 las quite, y lo que solo esté ahí se conserva | Abierto |
| B-02 | Que la comprobación nueva marque números legítimos de la narrativa | El aviso se vuelve ruido y se aprende a ignorarlo | Se detecta el **campo con su rótulo**, no cualquier cifra suelta (§2.6) | Abierto |
| B-03 | Que quitar la cuenta deje sin respuesta a quien no puede correr el comando | Se pierde el tablero que la `HU-017` quería | El pendiente deja el comando escrito y copiable (`T-03`, `RNF-01`). Si aun así hace falta un tablero durable, es historia nueva y no esta | Abierto |

---

## 11. Definition of Done

- [ ] Los tres CA de §0 verificados con evidencia (§5)
- [ ] Los dos requisitos no funcionales validados
- [ ] Pruebas de la fase en verde, y **la suite completa al final** (`02·F5`)
- [ ] Trazabilidad historia a implementación sin faltantes (`13·DOC11`)
- [ ] Documentación e índices actualizados (`13`)
- [ ] Señales registradas (`13·DOC5`)
- [ ] Rama lista para el commit único de la fase (`09·G1`)
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2, no acá.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md). Este plan se queda como se aprobó, para poder comparar lo que se dijo contra lo que pasó.
