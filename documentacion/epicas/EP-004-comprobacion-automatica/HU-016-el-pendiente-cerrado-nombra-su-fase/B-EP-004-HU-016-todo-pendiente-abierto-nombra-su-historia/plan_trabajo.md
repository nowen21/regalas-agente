# Plan de Trabajo — Fase B-EP-004-HU-016-todo-pendiente-abierto-nombra-su-historia (módulo Comprobación automática)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-016](../HU-016-el-pendiente-cerrado-nombra-su-fase.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `B-EP-004-HU-016-todo-pendiente-abierto-nombra-su-historia` |
| **Épica** | [EP-004 Comprobación automática](../../epica.md) |
| **HU** | [HU-016 Comprobar que el pendiente cerrado nombra su fase](../HU-016-el-pendiente-cerrado-nombra-su-fase.md) — una sola (`F12.1`) |
| **Módulo** | Comprobación automática (`validadores/pendientes.py`) |
| **Especificación del módulo** | [HU-016](../HU-016-el-pendiente-cerrado-nombra-su-fase.md). El entregable es un programa de comprobación: sus `CA-05` a `CA-07` son la especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/B-EP-004-HU-016-todo-pendiente-abierto-nombra-su-historia` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 🔀 **Híbrido.**

- 📝 **Complementa** a la [fase A](../A-EP-004-HU-016-el-pendiente-cerrado-declara-su-fase/plan_trabajo.md), que comprueba al pendiente **cerrado**. Esta comprueba al **abierto**. Es la misma pieza, `validadores/pendientes.py`, con la exigencia corrida al otro extremo de la vida del pendiente.
- ✨ **Funcionalidad nueva:** los `CA-05` a `CA-07`, que no existían cuando se escribió la fase A.

**De dónde sale.** El 2026-08-17 el usuario cortó un triaje por urgencia con una línea: *«todos los pendientes deben estar dentro de una HU, nada puede estar suelto»*. Ese día se enrutaron los 33 archivos del backlog y hubo que escribir seis historias nuevas. **El enrutamiento quedó hecho y nada lo sostiene:** el pendiente 60 nace suelto igual que nacieron los 33.

**CA de la HU que cubre esta fase**

| CA de HU-016 | Qué exige | Estado hoy |
|---|---|---|
| [CA-05](../HU-016-el-pendiente-cerrado-nombra-su-fase.md#ca-05--un-pendiente-abierto-sin-historia-se-reporta) | Un pendiente abierto sin historia se reporta | **No está.** Los 33 tienen su fila porque se escribieron a mano; el 34 no la va a tener |
| [CA-06](../HU-016-el-pendiente-cerrado-nombra-su-fase.md#ca-06--la-historia-nombrada-existe) | La historia nombrada existe | **No está.** La fila se puede llenar con `EP-009 · HU-042` y nadie se entera |
| [CA-07](../HU-016-el-pendiente-cerrado-nombra-su-fase.md#ca-07--el-tema-declarado-no-se-reporta) | El tema declarado no se reporta | **No está**, y sin esto el programa reportaría los cuatro temas el primer día |

**Por qué una sola fase.** Los tres son la misma comprobación con su excepción: sin el `CA-07` el programa reporta de más y se deja de correr (`02·F12.10`). Y no se juntan con los cuatro de la fase A porque **aquella está detenida** y esta no lo está — juntarlas la detendría también.

**Esta fase no espera a la A.** Las dos escriben en el mismo archivo, pero en funciones distintas y sin orden entre ellas: la A mira los cerrados, esta los abiertos. Si la A se aprueba primero, esta se apoya en lo que aquella deje; si se aprueba después, aquella se apoya en esto. Está comprobado en §2.2.

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que un pendiente abierto sin su historia rompa la corrida, para que el enrutamiento del 2026-08-17 no dependa de que alguien se acuerde.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-05 | El abierto sin fila se reporta | Funcional | Baja |
| CA-06 | La historia inventada se reporta | Funcional | Baja |
| CA-07 | El tema declarado pasa; la fila vacía no | Funcional — excepción | Media |

**Fuera de alcance:**

- **El texto de la regla en `base/`.** Es otro módulo y no hay historia que sea dueña del texto del capítulo `02`. Va en §10 como bloqueo declarado, y es lo que impide que esta fase se dé por suficiente.
- **Los seis pendientes cerrados que no tienen la fila** — el 25, el 31, el 40, el 41, el 42 y el 44. Esos son de la fase A y de su fecha de corte. Acá no se tocan.
- **Juzgar si la historia que el pendiente nombra es la correcta.** Eso es criterio y lo lee una persona. Acá solo se comprueba que exista.
- **El aviso al abrir un pendiente.** Sería un enganche, y eso es de EP-005.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

**Medido el 2026-08-17 contra el repositorio**, no recordado:

| Qué | Cuánto |
|---|---|
| Archivos en `pendientes/`, sin el índice | 40 |
| Con la fila `Historia de usuario` | **33** |
| Sin ella | **7** — seis cerrados (25, 31, 40, 41, 42, 44) y el 48, que se enrutó aparte |
| Que declaran `**Estado:** abierto` | 32 |
| En `pendientes/hecho/` | 17 |
| Líneas de `validadores/pendientes.py` | 156 |

> El 33 con fila y 32 abiertos no se contradicen: el [10](../../../../../pendientes/10-ideas.md) tiene fila y no tiene línea de estado, porque es la libreta y no un pendiente.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/pendientes.py` | Modificar | Comprobación | Las tres comprobaciones nuevas, en funciones aparte de las de la fase A |
| `validadores/validar.py` | Modificar | Comprobación | El subcomando `pendientes` ya existe; suma estos hallazgos a los suyos |
| `validadores/tests/test_pendientes_historia.py` | Nuevo | Test | Los casos de §3 |
| `validadores/docs/pendientes.md` | Modificar o nuevo | Documentación | Qué mira, qué no, y qué es un tema |
| `pendientes/README.md` | Modificar | Documentación | Dice que la fila es obligatoria y cuál es su nombre exacto |
| `HU-016-el-pendiente-cerrado-nombra-su-fase.md` | Modificar | Documentación | §8 nombra esta fase |
| `validadores/reglas-validables.md` | Modificar | Documentación | Deja escrito qué mitad de `02·F23` queda comprobada |

> Los seis pendientes cerrados sin fila **no se editan**, y los 33 enrutados tampoco: ya están como tienen que estar.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ningún contrato cambia. `pendientes.validar(proyecto)` conserva su firma y su tipo de retorno; devuelve más hallazgos que antes, que es lo que se pide.

| Archivo a cambiar | Cambio | Quién depende | Dónde podría romper |
|---|---|---|---|
| `validadores/pendientes.py` | Suma hallazgos a `validar()` | `validar.py pendientes` | Si alguna corrida daba «sin incumplimientos» y pasa a fallar. Hoy los 33 tienen su fila, así que la corrida sigue en verde — y eso se comprueba, no se supone (T-01) |
| `validadores/validar.py` | Ninguno de firma | Los enganches | Nada: el subcomando ya existe |

**Cruce con la fase A, comprobado.** La fase A declara en su §2.1 que **crea** `validadores/pendientes.py`; el archivo ya existe —156 líneas, escrito para HU-018— y su plan quedó viejo en ese punto. Esta fase lo **modifica**, que es lo que corresponde. Las dos escriben funciones nuevas y ninguna toca las de la otra.

**Comprobación previa obligatoria (T-01):** correr `validar.py pendientes` y guardar la salida. Es la línea base. «No cambió nada para los 33» se comprueba comparando, no recordando.

### 2.3 Rutas / endpoints y control de acceso

No aplica.

### 2.4 Punto de entrada en la interfaz

No aplica. Lo que cambia se ve en la salida de `validar.py pendientes`.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La fila se reconoce por su nombre exacto, `Historia de usuario`, en la ficha de cabecera | Buscar cualquier enlace a una HU en el archivo | Un pendiente cita historias en su prosa todo el tiempo. Sin sitio fijo, el programa acierta por casualidad — y es lo que `RN-02` prohíbe |
| La ficha se reconoce por su encabezado sin nombres de columna (`\| \| \|`) | La primera tabla del archivo | **Ya falló así el 2026-08-17.** El script de enrutamiento metió la fila dentro de una tabla de contenido en el 18, el 19 y el 23. Ningún validador lo habría visto |
| Un tema se declara en la misma fila, con texto y sin enlace | Una marca aparte, o una lista de excepciones en el programa | Una lista de excepciones dentro del código envejece sin que nadie la mire; la declaración vive al lado de lo que declara |
| Solo se exige a los **abiertos** | Exigírselo también a los cerrados | Los cerrados son de la fase A y de su fecha de corte. Pisarlo desde acá dejaría dos reglas para lo mismo |

### 2.7 Dudas por resolver antes de escribir

**Ninguna abierta.** Las dos dudas que detienen la fase A no aplican acá, y una de ellas la contestó el trabajo del 2026-08-17:

| Duda de la fase A | Por qué no detiene a esta |
|---|---|
| La fecha de corte | No hay legado: los 33 ya están enrutados, así que la exigencia rige desde hoy y no reporta a nadie hacia atrás |
| Dónde se declara — línea fija o sección | **Contestada:** es la fila `Historia de usuario` de la ficha de cabecera, escrita en los 33 archivos. Deja de ser una duda y pasa a ser un hecho medido |

> Esto también **destraba la duda 27 del [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md)**, que es la misma pregunta. Se reporta y no se aprovecha desde acá: cerrarla es de la fase A.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-05 — Un pendiente abierto sin historia se reporta

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Guardar la salida de `validar.py pendientes` **antes** del cambio | Test | 0,25 h | — | EV-01 |
| T-02 | Leer la ficha de cabecera: encabezado sin nombres de columna, y su fila `Historia de usuario` | Comprobación | 1 h | T-01 | EV-02 |
| T-03 | Reportar el pendiente abierto al que le falte la fila, diciendo dónde escribirla | Comprobación | 0,5 h | T-02 | EV-02 |
| T-04 | Prueba: archivo sin fila reporta; con fila no | Test | 0,75 h | T-03 | EV-02 |

### CA-06 — La historia nombrada existe

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-05 | Resolver la historia contra el árbol de épicas, por el destino del enlace | Comprobación | 0,75 h | T-02 | EV-03 |
| T-06 | Prueba: `EP-009 · HU-042` reporta; una real no | Test | 0,5 h | T-05 | EV-03 |

### CA-07 — El tema declarado no se reporta

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-07 | Dejar pasar la fila que declara un tema, y no la que está vacía | Comprobación | 0,5 h | T-03 | EV-04 |
| T-08 | Prueba: los cuatro temas pasan; la fila vacía no | Test | 0,5 h | T-07 | EV-04 |

### Transversales y cierre

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-09 | Comparar la salida contra la de T-01: los 33 siguen en verde | Test | 0,25 h | T-07 | EV-01 |
| T-10 | Correr la suite del repositorio: las 36 siguen pasando | Test | 0,25 h | T-09 | EV-05 |
| T-11 | `pendientes/README.md`, `validadores/docs/pendientes.md` y `reglas-validables.md` | Documentación | 0,75 h | T-07 | — |
| T-12 | §8 de HU-016 nombra esta fase | Documentación | 0,25 h | T-09 | — |

**Total estimado:** 6,25 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-07 → T-09 → T-10
**Paralelizables:** T-05 y T-06 después de T-02; T-11 y T-12 después de T-07.

**T-01 va primero y no se salta.** Es lo único que permite afirmar que los 33 enrutados siguen pasando.

**T-07 va antes que T-09**, y no al revés: sin la excepción del tema, la comparación de T-09 daría cuatro hallazgos nuevos y habría que leerlos como falsos.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| CA-05 | Prueba automática sobre archivos de mentira + corrida real | EV-01, EV-02 | ☐ |
| CA-06 | Prueba automática con una historia inventada y una real | EV-03 | ☐ |
| CA-07 | Prueba automática sobre los cuatro temas y una fila vacía | EV-04 | ☐ |
| No regresión | La suite del repositorio y la línea base | EV-01, EV-05 | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de `validar.py pendientes` antes y después | `resultado_pruebas.md` de esta fase |
| EV-02 | Salida de la prueba del CA-05 | `resultado_pruebas.md` de esta fase |
| EV-03 | Salida de la prueba del CA-06 | `resultado_pruebas.md` de esta fase |
| EV-04 | Salida de la prueba del CA-07 | `resultado_pruebas.md` de esta fase |
| EV-05 | Salida de la suite completa | `resultado_pruebas.md` de esta fase |

---

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | Carpetas temporales desechables. Nunca el backlog real ([`00·N4`](../../../../../base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)) |
| Usuarios de prueba | No aplica |
| Datos precargados | Un `pendientes/` de mentira: uno con fila buena, uno sin fila, uno con historia inventada, uno declarado tema y uno con la fila vacía |

**El backlog real entra solo de lectura**, en T-01 y T-09, para comparar la salida. No se le escribe nada.

---

## 7. Reversión / rollback

Se revierte volviendo el commit atrás. No hay datos de por medio y ningún archivo del backlog se modifica al correr: el programa comprueba, no arregla.

---

## 8. Producción y migración incremental

**No toca datos ni esquemas.** Sí cambia el veredicto que recibe quien corra `validar.py pendientes`: un backlog con un pendiente abierto sin historia pasa a fallar donde antes pasaba. Eso es la corrección, no una regresión.

**Un proyecto que herede el estándar y tenga `pendientes/` va a recibir esta exigencia.** Hay que decidir en la ejecución si aplica a cualquier proyecto o solo a esta casa; si aplica a todos, es un cambio **MAYOR** y se avisa. Queda como B-03.

---

## 9. Reglas del estándar y del proyecto aplicadas

- Base: [`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F11`](../../../../../base/02-flujo-de-trabajo/reglas/F11-una-fase-solo-modifica-codigo-de-su-propio-modulo.md), [`02·F12`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md), [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md), [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar), [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).
- Proyecto: el [CLAUDE.md](../../../../../CLAUDE.md) de este repositorio, §2 y §4.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| **B-01** | **El texto de `02·F23` no dice «desde que se abre».** El programa haría fallar por algo que la regla no exige, y eso es peor que no comprobarlo | Alto | Se declara acá y **no se construye desde esta fase**: es otro módulo. Necesita su propia fase, en la historia que sea dueña del texto | Abierto |
| **B-02** | **Ninguna historia es dueña del texto del capítulo `02`.** Se buscó el 2026-08-17: EP-001 cubre los capítulos `00` y `01` y el cuerpo de reglas en general; nadie declara el `02` como su módulo. Sin dueño, B-01 no tiene dónde caer | Alto | Se reporta como pendiente nuevo. Es un hueco del árbol de épicas, no de esta fase | Abierto |
| B-03 | Que la exigencia le llegue a un proyecto heredero sin avisar | Medio | Se decide en la ejecución si aplica a todos; si aplica, es **MAYOR** y se avisa | Abierto |
| B-04 | Que la fase A se apruebe en medio y las dos escriban el mismo archivo | Bajo | Funciones separadas, comprobado en §2.2. Quien vaya segundo compara contra la línea base del primero | Abierto |
| B-05 | Que el programa reconozca mal la ficha, como ya pasó con el script de enrutamiento | Alto | La decisión de §2.6 y el `CA-07`; y el caso del 18/19/23 entra como caso de prueba | Abierto |

**El B-01 y el B-02 son la razón por la que esta fase no cierra el tema.** Cierra la mitad que comprueba; la mitad que exige sigue sin escribirse, y esta fase no se puede dar por suficiente hasta que aquella exista.

---

## 11. Definition of Done

- [ ] Los tres CA verificados con evidencia (§5)
- [ ] La salida de `validar.py pendientes` sobre el backlog real sigue sin fallas
- [ ] Las 36 pruebas del repositorio siguen pasando, más las nuevas
- [ ] `pendientes/README.md` dice que la fila es obligatoria y con qué nombre exacto
- [ ] `reglas-validables.md` dice qué mitad de `02·F23` quedó comprobada y cuál no
- [ ] §8 de HU-016 nombra esta fase
- [ ] El B-01 y el B-02 reportados como pendiente, con su historia
- [ ] Rama lista para el commit único de la fase
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md` de esta fase.
