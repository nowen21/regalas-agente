# Plan de Trabajo — Fase `A-EP-004-HU-020-lo-que-se-hereda-tampoco-se-cuenta-a-mano` (módulo Programas de comprobación)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Se escribe **antes** de tocar nada y se aprueba antes de empezar. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas`; lo que quedó hecho, en el `funcionalidad_implementada.md`.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-020-lo-que-se-hereda-tampoco-se-cuenta-a-mano` |
| **Épica** | [EP-004](../../epica.md) |
| **HU** | [HU-020](../HU-020-el-inventario-heredado-tampoco-se-mantiene-a-mano.md) — **una sola** (`F12.1`) |
| **Módulo** | Programas de comprobación |
| **Especificación del módulo** | **No hay documento aparte**, por lo mismo que la fase anterior: la historia trae alcance, reglas, criterios con pasos y requisitos no funcionales. **Es la cuarta fase que lo declara**, y sigue siendo evidencia para la [EP-001 · HU-010](../../../EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md), que está abierta para escribir esa regla |
| **Fecha apertura** | 2026-08-26 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):
- 📝 **Modifica la fase [`A-EP-004-HU-019`](../../HU-019-inventario-que-no-se-mantiene-a-mano/A-EP-004-HU-019-el-inventario-no-guarda-la-cuenta/funcionalidad_implementada.md), cerrada hoy mismo.** Aquella resolvió el problema puertas adentro y dejó dos mitades sin cubrir: la plantilla que reparte el defecto, y una comprobación atada a una ruta fija. La primera quedó declarada en su cierre §6; **la segunda apareció al verificar esta historia**, y no estaba declarada en ninguna parte.

**CA de la HU que cubre esta fase:**

| CA de `HU-020` | Estado |
|---|---|
| CA-01 — la plantilla ya no pide mantener una cuenta | ☐ |
| CA-02 — la comprobación encuentra el inventario donde el proyecto lo tenga | ☐ |
| CA-03 — lo que la plantilla enseña y no es derivable se conserva | ☐ |
| CA-04 — la versión sube, porque cambió una plantilla | ☐ |

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que lo que el estándar arregló para sí mismo llegue a quien lo hereda — la plantilla deja de enseñar la cuenta a mano, y la comprobación deja de mirar una sola ruta.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | La plantilla remite al comando, con su `--raiz` | Funcional | Baja |
| CA-02 | La comprobación busca donde el proyecto lo tenga | Funcional | Media |
| CA-03 | La guía de proceso sobrevive | Funcional | Baja |
| CA-04 | `VERSION` sube y el `CHANGELOG` lo dice | Funcional | Baja |
| RNF-01 | Buscar no recorre el proyecto entero | No funcional | Media |
| RNF-02 | Un inventario en `pendientes/` sigue funcionando | No funcional | Baja |

**Fuera de alcance:**

- **Cambiar inventarios ya escritos en proyectos existentes.** La plantilla rige lo nuevo; lo viejo lo avisa la comprobación.
- **Las demás plantillas.** Si otra enseña a mantener a mano algo derivable, sale de un barrido aparte.
- **Cambiar cómo se cuenta**, que sigue siendo de la `HU-017`.

---

## 2. Análisis previo — línea base verificada  ·  `02·F17`

> Verificado contra el repositorio el 2026-08-26, corriendo los comandos.

| Qué | Valor verificado | Cómo se obtuvo |
|---|---|---|
| Largo de la plantilla | 56 líneas | `wc -l plantillas/inventario-hu.md` |
| Lo que la plantilla trae a mano | Los 3 campos con `«N»`, una tabla de 8 columnas con 3 filas de ejemplo, y 6 pasos de «Cómo se llena la tabla» | Leyéndola entera |
| Ruta que mira la comprobación | `INVENTARIO = "pendientes/48-inventario-hu.md"`, escrita fija | `validadores/fases.py` línea 194 |
| Dónde dice la plantilla que vive el inventario en un proyecto | `documentacion/` | La plantilla, línea 7 |
| Versión actual del estándar | `34.1.0` | `cat VERSION` |
| Que un proyecto pueda correr el comando | **Sí.** `validar.py fases --raiz <proyecto>` da el detalle y la cuenta | Corrido sobre un árbol de prueba con una historia |
| Que los validadores no se copien al proyecto | **No se copian**: los enganches los llaman en su sitio | `validadores/instalar.py`, líneas 31 y 128 |

**El dato que decide el diseño:** si los proyectos no pudieran correr el comando, quitarle la tabla a la plantilla los dejaría sin nada. **Se verificó antes de escribir el plan, no después.**

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `plantillas/inventario-hu.md` | Modificar | Documentación | Se le quitan los 3 campos, la tabla y los 6 pasos; se conserva la guía del orden y la distinción construir/retrodocumentar |
| `validadores/fases.py` | Modificar | Servicio | `cuenta_escrita_a_mano` busca donde el proyecto lo tenga, no en una ruta fija |
| `validadores/pruebas.py` | Modificar | Test | Casos para el inventario fuera de `pendientes/` |
| `CHANGELOG.md` | Modificar | Documentación | Entrada de la versión nueva (`20·M10`) |
| `VERSION` | Modificar | Documentación | Sube la parte menor (`20·M10`) |
| `pendientes/48-inventario-hu.md` | **No se toca** | — | Ya quedó bien en la fase anterior. Se declara para que conste que se miró y se decidió no tocarlo |

### 2.2 Matriz de dependencias

| Archivo a refactorizar | Cambio de contrato | Archivos que dependen (rompen) | Dónde rompe |
|---|---|---|---|
| `validadores/fases.py` | `cuenta_escrita_a_mano` conserva su firma `(proyecto) -> [Hallazgo]`. Lo que cambia es dónde busca | `validadores/pruebas.py` | Las siete pruebas de la `HU-019` la llaman. **Tienen que seguir pasando sin cambios**, y eso es la comprobación de `RNF-02` |
| `plantillas/inventario-hu.md` | Deja de traer campos y tabla | Ninguno en código | Ningún programa lee esta plantilla; la usa una persona al armar su inventario |

### 2.3 Rutas / endpoints y control de acceso

**No aplica.**

### 2.4 Punto de entrada

- **Para el estándar:** `python validadores/validar.py fases`.
- **Para un proyecto:** `python <ruta-al-estandar>/validadores/validar.py fases --raiz .`, que es lo que la plantilla va a decir.

### 2.5 Permisos / roles a sembrar

**Ninguno.**

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El inventario se reconoce por **traer los campos de la cuenta**, no por su nombre | Buscar archivos llamados `inventario-hu.md` | El nombre lo elige cada proyecto; la plantilla no lo fija. Lo que sí es constante es la forma del defecto |
| Se busca solo en un puñado de carpetas declaradas | Recorrer el proyecto entero | `RNF-01`. Un proyecto grande pagaría el recorrido en cada corrida para vigilar un archivo |
| Las carpetas donde se busca se escriben en una constante con su porqué | Dejarlas dentro de la función | Es lo que alguien va a querer cambiar cuando aparezca un proyecto que lo guarde en otro sitio |
| **MENOR**, no mayor | Mayor | Es aditivo: ningún proyecto al día queda obligado a hacer algo. Lo que aparece es un aviso, y los avisos no detienen |
| La plantilla conserva la guía del orden de los documentos | Quitarla junto con la tabla | **No es derivable del árbol.** Que un documento falte se ve; en qué orden deben escribirse, no |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| — | Ninguna | — | — |

**La única que había —si los proyectos pueden correr el comando— se resolvió corriéndolo** antes de escribir este plan. Está en §2.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-02 — La comprobación encuentra el inventario donde el proyecto lo tenga

Va primero: **si la plantilla cambiara antes, los proyectos nuevos harían lo correcto y nadie se lo estaría comprobando.**

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Declarar en qué carpetas se busca, con su porqué | Backend | 0.5 h | — | EV-01 |
| T-02 | Que `cuenta_escrita_a_mano` busque ahí en vez de en la ruta fija | Backend | 2 h | T-01 | EV-01 |
| T-03 | Que el aviso nombre la ruta real del archivo que encontró | Backend | 0.5 h | T-02 | EV-01 |
| T-04 | Casos para el inventario fuera de `pendientes/` | Test | 2 h | T-02 | EV-02 |
| T-05 | Comprobar que las siete pruebas de la `HU-019` siguen pasando sin tocarlas | Test | 0.5 h | T-02 | EV-03 |

### CA-01 y CA-03 — La plantilla

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-06 | Listar las secciones de la plantilla antes de tocarla | Documentación | 0.5 h | — | EV-04 |
| T-07 | Quitar los tres campos de cuenta | Documentación | 0.5 h | T-06 | EV-04 |
| T-08 | Quitar la tabla y los seis pasos para llenarla | Documentación | 1 h | T-07 | EV-04 |
| T-09 | Escribir el comando con `--raiz`, **verificado corriéndolo** | Documentación | 1 h | T-02 | EV-05 |
| T-10 | Reescribir la guía de proceso sin la tabla, conservando lo no derivable | Documentación | 1 h | T-08 | EV-04 |
| T-11 | Listar las secciones otra vez y comparar | Documentación | 0.5 h | T-10 | EV-04 |

### CA-04 — Versionar

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-12 | Subir `VERSION` a `34.2.0` | Documentación | 0.5 h | T-10 | EV-06 |
| T-13 | Escribir la entrada del `CHANGELOG`, diciendo qué cambia para quien ya tiene el estándar | Documentación | 1 h | T-12 | EV-06 |
| T-14 | Correr `validar.py versionado` | Documentación | 0.5 h | T-13 | EV-06 |

### RNF

| ID | Tarea | Categoría | Est. | Ev. |
|---|---|---|:--:|---|
| T-15 | Medir que buscar no recorra el proyecto entero | Rendimiento | 0.5 h | EV-07 |
| T-16 | Sabotear las piezas y comprobar que las pruebas cazan | Calidad | 2 h | EV-08 |

**Total estimado:** 15 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-09 → T-10 → T-12 → T-13 → T-14

**Paralelizables:** T-06, T-07 y T-08 no dependen del código y avanzan en simultáneo con T-04 y T-05.

**T-09 depende de T-02 a propósito:** el comando que la plantilla va a enseñar **se corre antes de escribirlo**. Escribir un comando sin haberlo corrido es lo que deja a quien lo copia con un error en la mano.

**T-16 va al final**, y su corrida de cierre es la suite completa, no solo lo tocado.

> Solo se tocan los archivos declarados en §2.1 (`02·F8`). Descubrir uno nuevo: PAUSAR, reportar, ampliar el plan con aprobación.

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Lectura de la plantilla, y corrida del comando que enseña | EV-04, EV-05 | | ☐ |
| CA-02 | Pruebas con el inventario en dos carpetas distintas | EV-01, EV-02 | | ☐ |
| CA-03 | Lista de secciones antes y después | EV-04 | | ☐ |
| CA-04 | `VERSION`, la entrada del `CHANGELOG`, y el validador de versionado | EV-06 | | ☐ |
| RNF-01 | Se cuenta cuántas carpetas se abren al buscar | EV-07 | | ☐ |
| RNF-02 | Las siete pruebas de la `HU-019`, sin tocarlas | EV-03 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 a EV-08 | Salidas de corrida, listas y conteos | `resultado_pruebas.md` de esta fase |

---

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La máquina de quien trabaja, con la biblioteca estándar |
| Usuarios de prueba | No aplica. **Ninguna prueba usa credenciales** (`00·N6`) |
| Datos precargados | Proyectos de mentira en carpeta temporal, creados y borrados por la prueba |

**Ni la plantilla ni el pendiente real se editan para probar** (`08·T4`).

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit de la fase. **Con una salvedad que conviene decir:** si la versión ya se publicó, bajar `VERSION` no deshace que un proyecto la haya visto. La reversión sería una versión nueva que restituye, no un borrado — que es lo que el propio `CHANGELOG` exige al decir que nada se renumera.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Un proyecto que ya tenga el estándar** verá dos cosas al actualizar: un aviso nuevo si su inventario guarda la cuenta, y la plantilla sin la tabla la próxima vez que arme uno. **Su inventario actual no se toca ni se migra**: el aviso informa, y arreglarlo es decisión suya. Eso queda escrito en la entrada del `CHANGELOG` (T-13).

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `02·F8` — solo los archivos de §2.1.
- `02·F17` — todo lo que este plan afirma se verificó corriéndolo; los valores están en §2.
- `04·R4` — no se afirma sobre lo que no se leyó: por eso T-06 lista las secciones **antes** de que T-08 quite nada.
- `08·T4` — las pruebas no tocan los archivos reales.
- `13·DOC5` — lo decidido se registra como señal.
- `20·M10` — versionar es la condición para que el cambio de plantilla exista, y por eso es `CA-04` y no una tarea suelta.
- `EP-004 §10.2` y `DA-06` — el programa reporta y no corrige.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que buscar el inventario sea lento en un proyecto grande | Se paga en cada corrida | Se busca solo en carpetas declaradas, y T-15 lo mide en vez de suponerlo | Abierto |
| B-02 | Que la comprobación marque archivos que no son inventarios | El aviso se vuelve ruido | Se pide el rótulo **como campo de tabla con un número**, que es la forma exacta del defecto | Abierto |
| B-03 | Que quitar la tabla se lleve guía de proceso que sí sirve | Se pierde lo no derivable | T-06 y T-11 listan las secciones antes y después | Abierto |
| B-04 | Que el comando escrito en la plantilla no funcione al copiarlo | Quien lo copie se queda con un error | T-09 lo corre **antes** de escribirlo, y depende de T-02 por eso | Abierto |

---

## 11. Definition of Done

- [ ] Los cuatro CA de §0 verificados con evidencia (§5)
- [ ] Los dos requisitos no funcionales validados
- [ ] Pruebas de la fase en verde, y **la suite completa al final** (`02·F5`)
- [ ] Trazabilidad historia a implementación sin faltantes (`13·DOC11`)
- [ ] `VERSION` y `CHANGELOG` al día (`20·M10`)
- [ ] Señales registradas (`13·DOC5`)
- [ ] Rama lista para el commit único de la fase (`09·G1`)
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
