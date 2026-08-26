# Funcionalidad implementada — Fase E-EP-010-HU-001-se-trae-un-proyecto-con-lo-que-tenga-escrito (módulo Importación)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `E-EP-010-HU-001-se-trae-un-proyecto-con-lo-que-tenga-escrito` |
| **Módulo** | Importación |
| **Especificación del módulo** | [documentacion/importacion/spec.md](../../../../importacion/spec.md), aprobada el 2026-08-25 · `02·F2` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-25 |
| **HU / CA cubiertas** | [HU-001](../HU-001-traer-un-proyecto.md), con los seis criterios de la especificación |
| **Fecha de cierre** | 2026-08-25 |
| **Versión del estándar al cerrar** | 34.1.0 |
| **Commit** | `c998695` |

---

## 1. Qué se implementó — resumen

La documentación que un proyecto ya tiene escrita entra a la plataforma. **Se copia, nunca se mueve ni se modifica**: el proyecto de origen queda exactamente como estaba.

Primero se mira y se cuenta sin escribir nada; se muestra el **recuento por tipo** y **qué carpetas no se miraron**; y solo con la confirmación se trae. Traer dos veces no duplica, y un documento editado entra con su versión nueva.

**El caso real ya corrió:** este repositorio entró con **973 documentos, ninguno sin reconocer, en 13,6 segundos**.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| "Se recorre la carpeta del proyecto y se identifica cada documento por su forma" (§6) | servicio | [nucleo/importacion/moldes.py](../../../../../plataforma/nucleo/importacion/moldes.py) y `mirar` en [core.py](../../../../../plataforma/nucleo/importacion/core.py) | ✅ | CP-001, CP-008 |
| "Antes de escribir nada se muestra qué se va a traer, y el usuario confirma" (§6) | vista | [views.py](../../../../../plataforma/nucleo/importacion/views.py) y `templates/importacion/traer.html` | ✅ | CP-006 |
| "Documento que no se reconoce: no entra, y va al reporte" (§6) | servicio | `Hallazgo.sin_reconocer` | ✅ | CP-003 |
| "Un documento que ya se trajo antes: no se duplica" (§6) | modelo | El `unique_together` de [models.py](../../../../../plataforma/nucleo/importacion/models.py) y la búsqueda por origen | ✅ | CP-005 |
| "Falla a mitad: se descarta lo traído en esa pasada" (§6) | servicio | `_deshacer` en [core.py](../../../../../plataforma/nucleo/importacion/core.py) | ✅ | CP-007 |
| "Si todo se reconoció, se dice" (§6) | vista | `todo_reconocido` y la plantilla | ✅ | CP-004 |
| "`RN-1` traer no modifica el proyecto de origen" (§4) | servicio | Nada de `traer` escribe fuera de `datos/` | ✅ | CP-009 |
| "`RN-2` lo que no se reconoce no se transforma" (§4) | servicio | `moldes.tipo_de` devuelve vacío y el documento no entra | ✅ | CP-003 |
| "`RN-4` nada se pierde en silencio" (§4) | servicio · vista | Lo no reconocido se lista, y **las carpetas que no se miran se nombran con su porqué** | ✅ | CP-003, CP-008 |
| "Se copia, no se mueve" (§12) | servicio | `traer` lee y escribe en `datos/` | ✅ | CP-009 |
| "Nombres repetidos dentro del proyecto: se avisa antes de traer" (§6) | — | — | N/A | No aplica: cada documento se identifica por su **ruta completa**, así que dos con el mismo nombre en carpetas distintas no chocan |
| "Reportar lo no reconocido" (`F-028`, §1) | — | — | N/A | Fase F. Acá se cuenta y se puede ver; el reporte con su forma es de esa fase |

**Faltantes / diferimientos:** el reporte de `F-028`, que es la fase F y así lo declaraba el plan.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| 1 | Reconocer los documentos del ciclo por su molde | ✅ hecha | [moldes.py](../../../../../plataforma/nucleo/importacion/moldes.py) | CP-001 |
| 2 | Recorrer y decir qué se encontró | ✅ hecha | `mirar` en [core.py](../../../../../plataforma/nucleo/importacion/core.py) | CP-001, CP-003 |
| 3 | Mostrar qué se va a traer, y pedir confirmación | ✅ hecha | [views.py](../../../../../plataforma/nucleo/importacion/views.py) | CP-006 |
| 4 | Traer lo reconocido, copiando | ✅ hecha | `traer` en [core.py](../../../../../plataforma/nucleo/importacion/core.py) | CP-002, CP-009 |
| 5 | No duplicar al traer dos veces | ✅ hecha | La búsqueda por origen en `traer` | CP-005 |
| 6 | Que una falla a mitad no deje nada | ✅ hecha | `_deshacer` | CP-007 |
| 7 | Traer este mismo repositorio, y medir | ✅ hecha | `CasoRealTests` en [tests.py](../../../../../plataforma/nucleo/importacion/tests.py) | CP-008: **973 en 13,6 s** |

**Correspondencia con el plan:** 7 tareas en el plan, 7 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** el plan no estimó horas. Lo que acortó la fase fue **medir antes de planear**: la incertidumbre que la especificación declaraba como la mayor de la versión 1 se resolvió con un conteo, y lo que ese conteo encontró —tres moldes que faltaban— entró como tarea en vez de aparecer en producción.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Qué | Resultado |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | Cumple, en el ciclo 2 |
| **Suites ejecutadas** | `python manage.py test nucleo`, 126 de 126 verdes |
| **Defectos abiertos que se aceptaron** | Ninguno. `DEF-01` y `DEF-02` corregidos y verificados |

**Verificaciones manuales** (`08·T4`):

| # | Qué se verificó | Resultado |
|---|---|---|
| 1 | Que las pruebas cacen lo que dicen cazar | Ocho sabotajes, los ocho cazados a la primera |
| 2 | Que el repositorio real quede intacto | 1924 archivos antes y después |
| 3 | Que lo traído se lea sin la plataforma | Idéntico al original |
| 4 | Que los tres índices se rehagan desde el texto | Los tres |
| 5 | Que los datos de prueba no quedaran | Cero en los tres |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

En la pantalla de un proyecto hay un enlace **Traer lo que ya tiene escrito**. Lleva a una pantalla que muestra, **sin haber escrito nada todavía**: el recuento por tipo, qué no se reconoció con su ruta, y qué carpetas no se miraron con su porqué. Desde ahí se confirma.

- **Desde el código:** `core.mirar(proyecto)` cuenta sin escribir; `core.traer(proyecto, quien, sesion)` escribe.
- **Comando propio:** `python manage.py reconstruir_traido` rehace el índice leyendo los archivos copiados.
- **Dónde queda lo traído:** `datos/proyectos/<identificador>/traido/`, con la misma estructura de carpetas que tenía en el proyecto.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Se recorre solo la documentación del ciclo de vida | Recorrer todo dejaba un reporte de 540 líneas donde los tres casos reales se perdían. Decidido por el usuario con el conteo a la vista | [moldes.py](../../../../../plataforma/nucleo/importacion/moldes.py) |
| Las carpetas que **no** se miran se nombran, con su porqué | Saltarse carpetas sin decirlo es perder en silencio con otro nombre (`RN-4`) | `CARPETAS_QUE_NO_SE_MIRAN` |
| Se reconoce por nombre y ubicación, no por contenido | El estándar fija los nombres, así que el nombre **es** la forma. Adivinar por contenido es más frágil, y adivinar mal ensucia lo que sí sirve | `moldes.tipo_de` |
| Se lee con `newline=""` | Sin eso, un documento escrito en Windows entraba transformado, y **el texto se ve idéntico**. Es `DEF-01` | El comentario al lado, en `traer` |
| Deshacer borra los archivos **y** las filas del índice | Media importación puede vivir en cualquiera de los dos sitios. Es `DEF-02` | El comentario en `_deshacer` |
| La constancia se deja **una vez** por pasada, no por archivo | Traer es una sola acción del usuario que produce cientos de escrituras. Un comprobante por archivo llenaría el registro de mil líneas y escondería las acciones que sí hay que poder encontrar | El comentario en `_escribir` |
| Se muestra el recuento por tipo, no la lista de rutas | Mil líneas se confirman sin mirar, y entonces la confirmación deja de proteger | `Hallazgo.por_tipo` |
| Un documento se identifica por su **ruta de origen** | Es lo que distingue «no duplicar» de «no actualizar»: el contenido cambia cuando alguien edita, y sigue siendo el mismo documento | El `unique_together` de [models.py](../../../../../plataforma/nucleo/importacion/models.py) |

---

## 5.1 Un defecto encontrado después de cerrar

| Fecha | Qué era | Cómo se encontró | Dónde se corrigió |
|---|---|---|---|
| 2026-08-25 | **Esta fase declaraba recorrer «la documentación del ciclo de vida» y no recorría las etapas del ciclo**, que en este proyecto viven en `cvds/`. Peor: esa carpeta tampoco estaba en la lista de las que se declaran como no miradas, así que **se saltaba en silencio**, contra `RN-4` | Al planear la fase G, que fue la primera que necesitó leer esas etapas para calcular el estado de un proyecto | Tarea 1 de la [fase G](../../../EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-003-ver-el-estado-de-un-proyecto/G-EP-008-HU-003-se-ve-el-estado-de-un-proyecto/README.md), con su caso de prueba `CP-001` |

**Por qué los nueve casos y los ocho sabotajes de esta fase no lo cazaron.** Todos comprobaban que se trajera lo que se decía traer, y **ninguno preguntaba si lo que se decía traer era todo**. La comprobación que lo habría encontrado es la que la fase G necesitó: intentar usar lo traído para responder una pregunta concreta.

**Qué no cambia con esto.** El veredicto de la fase sigue siendo Cumple: los seis criterios de la especificación quedaron probados sobre lo que la fase declaraba recorrer. Lo que faltaba era el alcance, no el comportamiento.

---

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| Reconocer por nombre deja pasar un archivo con el nombre correcto y otra cosa adentro | Atajo decidido, declarado en el plan §10 | Si aparece un caso real, se decide si vale la pena mirar el contenido |
| El reconocimiento se midió sobre un proyecto que sigue el estándar al pie de la letra. Uno que lo siga a medias va a reconocer menos | Diferido por el plan | Se sabrá al conectar el primer proyecto que no sea este |
| Traer 973 documentos tarda 13,6 s y los lee todos en memoria uno por uno | No previsto | Hoy alcanza. Si un proyecto tiene diez veces más, hay que medirlo otra vez |
| Lo traído no se puede consultar todavía desde la plataforma: entra y se queda | Diferido por el plan | La pantalla que lo muestra es de la versión 2, con `F-014` |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] Mapa de dependencias: Importación depende de Proyectos y de Auditoría, como declaraba su especificación.
- [x] Catálogo de módulos: Importación ya está registrado con su especificación aprobada.
- [x] Índice de la carpeta de la fase: [README.md](README.md).
- [x] Especificación del módulo: no hizo falta cambiarla. Lo único que precisó la fase —que solo se recorre la documentación del ciclo— es una decisión de alcance que quedó en el plan, y no contradice nada de lo escrito allá.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** `python manage.py migrate`.
- **Datos base:** ninguno.
- **Qué cambia para quien ya tenía la plataforma:** aparece el enlace para traer en la pantalla de cada proyecto.
- **Reversión:** se descarta la rama de la fase. Lo traído vive en `datos/proyectos/`, y borrarlo no toca ningún proyecto de origen, porque nunca se escribió en ellos.
