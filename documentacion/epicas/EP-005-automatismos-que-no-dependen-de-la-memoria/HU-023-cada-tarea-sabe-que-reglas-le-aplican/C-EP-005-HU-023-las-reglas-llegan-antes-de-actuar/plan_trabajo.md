# Plan de Trabajo · Fase `C-EP-005-HU-023-las-reglas-llegan-antes-de-actuar` (módulo Cuerpo de reglas y validadores)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba acepta el alcance y el costo. El requisito vive en la HU, el detalle de las pruebas en el `plan_pruebas` de la misma fase, y lo que quedó hecho en el `funcionalidad_implementada.md` del cierre.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-005-HU-023-las-reglas-llegan-antes-de-actuar` |
| **Épica** | [EP-005](../../epica.md) |
| **HU** | [HU-023](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md), una sola (`F12.1`) |
| **Módulo** | Cuerpo de reglas, `validadores/` y el adaptador |
| **Especificación del módulo** | RN-07 a RN-09 de la HU-023 |
| **Fecha apertura** | 2026-09-28 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- Modifica la [fase `B`](../B-EP-005-HU-023-todas-las-reglas-declaran-sus-tareas/funcionalidad_implementada.md), que eligió las tareas por las palabras del mensaje. Dos casos del 2026-09-28 lo mostraron: el agente corrió las 568 pruebas de `pruebas.py` contra `02·F5`, que le había llegado solo por su nombre, y la palabra «reglas» trajo las reglas de cambiar el estándar a un mensaje que solo preguntaba. El usuario decidió: *«el agente debe saber las reglas en todo momento»* y *«nada de adivinar»*. Es el mismo problema de H-1 de esa sesión, que se reabre.

> **Este plan cambió después de aprobado.** Lo que se construyó no es lo que describen las secciones 1 a 3: la sección [12](#12-cambios-después-de-la-aprobación) dice qué cambió, quién lo pidió y qué archivos tocó. El usuario aprobó esos cambios el 2026-09-29 (`02·F8`).

**CA de la HU que cubre esta fase** (trazabilidad `13·DOC11`):

| CA de HU-023 que cierra esta fase | Estado |
|---|---|
| [CA-08](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md#ca-08--la-palabra-clave-dice-las-tareas-del-mensaje) | ☐ |
| [CA-09](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md#ca-09--antes-de-actuar-el-agente-tiene-completas-las-reglas-de-esa-acción) | ☐ |
| [CA-10](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md#ca-10--los-archivos-de-reglas-por-tarea-no-envejecen) | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que el agente tenga completas las reglas de lo que va a hacer, en el momento de hacerlo, sin que nada se elija adivinando.

**Cómo funciona, en tres piezas:**

1. **Un archivo por tarea con sus reglas completas**, en `base/reglas-por-tarea/`, escrito por un programa. Si una tarea no cabe en una lectura, se parte en varios archivos.
2. **Con cada mensaje**, las tareas salen de la palabra clave de `01·C28`. Sin palabra clave, solo `recibir-pedido` y `responder`.
3. **Antes de cada acción**, las tareas salen de la acción: el comando, el archivo o el servicio. Si el agente no leyó en esta sesión el archivo de esa tarea, la acción se detiene y se le dice cuál leer. Lo mismo antes de entregar una respuesta, con `recibir-pedido` y `responder`. Cuando la conversación se resume, lo leído se olvida.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-08 | Las tareas del mensaje salen solo de la palabra clave | Funcional | Media |
| CA-09 | Ninguna acción pasa sin que el agente haya leído las reglas de su tarea | Funcional | Alta |
| CA-10 | Los archivos de reglas por tarea no pueden quedar viejos | Funcional, error | Media |
| RNF | Versionado, pruebas y amarre | No funcional | Baja |

**Fuera de alcance:**

- Cambiar qué exige cualquier regla o qué tareas declara.
- La medición de la respuesta anterior y el recordatorio de cada turno, que siguen como están.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-09-28:

```
Reglas de cada tarea (texto completo): recibir-pedido 34.960 · responder 28.682
  escribir-documento 98.721 · cambiar-codigo 217.871 · correr-comando 40.882
  tocar-git 28.865 · tocar-datos 36.811 · ir-afuera 9.946
  cambiar-estandar 47.213 · trabajar-cadena 85.392
Tope de un enganche: 10.000 caracteres (Claude Code, hooks.md)
PreToolUse: puede entregar texto y puede detener la acción (hooks.md)
Enganches PreToolUse instalados hoy: ninguno
`02·F5` declara: trabajar-cadena, correr-comando
```

- `base/tareas.md` tiene la columna «Palabras del pedido que la señalan», que es la que adivina.
- `validadores/recuperar.py` elige por esas palabras (`tareas_del_mensaje`).
- `validadores/sesiones.py` ya guarda estado por sesión en `historico-chat/.tocado/`, fuera del control de versiones. El registro de lo leído sigue esa forma.
- La herramienta de lectura no lee de una vez un archivo muy grande. Por eso las tareas que pasan de unos 50.000 caracteres se parten.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `base/tareas.md` | Modificar | Estándar | La columna de palabras se reemplaza por dos: las palabras clave que piden cada tarea y las acciones que la señalan |
| `base/reglas-por-tarea/` | Nuevo | Estándar | Un archivo por tarea, o por parte, con el texto completo de sus reglas; lo escribe el programa |
| `validadores/mapa_tareas.py` | Modificar | Validador | Lee las dos columnas, escribe los archivos por tarea y valida que coincidan |
| `validadores/recuperar.py` | Modificar | Validador | Elige por la palabra clave; sin palabra clave, solo lo que rige siempre |
| `validadores/leidas.py` | Nuevo | Validador | Qué tareas pide una acción, qué leyó cada sesión y qué le falta |
| `adaptadores/claude-code/hook_antes.py` | Nuevo | Adaptador | Detiene la acción o la respuesta hasta que se lea lo que falta, anota lo leído y lo olvida al resumir |
| `validadores/instalar.py` y `.gitignore` | Modificar | Validador | Instala el enganche en `PreToolUse`, `PostToolUse` de lectura, `Stop` y `SessionStart`; `historico-chat/.leido/` fuera del control de versiones |
| `.claude/settings.json` | Modificar | Adaptador | Los mismos enganches en el estándar |
| `anatomia/que-esta-amarrado-a-la-herramienta.md` | Modificar | Documentación | Clasifica `hook_antes.py` y `leidas.py` |
| `validadores/docs/` | Crear y modificar | Documentación | Guías de `hook_antes.py`, `leidas.py`, `mapa_tareas.py` y `recuperar.py` |
| `CLAUDE.md` y `plantillas/CLAUDE.md.plantilla` | Modificar | Estándar | Cómo llegan ahora las reglas |
| `validadores/tests/` y `validadores/pruebas.py` | Crear y modificar | Pruebas | Los casos nuevos y los del recuperador |
| `CHANGELOG.md` y `VERSION` | Modificar | Estándar | `39.6.0`, MENOR |
| Los documentos de esta fase, HU-023 y el resumen de la sesión | Modificar | Documentación | Cierre |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Archivo a refactorizar | Cambio de contrato | Archivos que dependen (rompen) | Dónde rompe |
|---|---|---|---|
| `base/tareas.md` | Cambia la tercera columna | `mapa_tareas.palabras()`, `recuperar.py` y sus pruebas | Se reescriben en la fase |
| `validadores/recuperar.py` | `tareas_del_mensaje` elige por palabra clave | `hook_reglas.py` y los casos de `pruebas.py` | `hook_reglas.py` usa `como_texto()`, que conserva su firma; los casos que esperaban palabras sueltas se reescriben |
| `validadores/instalar.py` | Suma enganches | Las pruebas del instalador | Se ajustan las que cuentan enganches |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica: el agente recibe el aviso antes de actuar.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El agente lee el archivo de la tarea; el enganche no le pega el texto | Pegar las reglas en el enganche | El enganche se corta en 10.000 caracteres y ninguna tarea cabe, salvo `ir-afuera` |
| La acción se detiene hasta que el archivo se lea | Solo avisar | Un aviso depende de que el agente se acuerde, que es lo que falló |
| Las tareas del mensaje salen de la palabra clave | Las palabras del mensaje | La palabra clave es una lista cerrada; las demás palabras se adivinan |
| Las tareas de la acción salen de una tabla escrita: `git` es `tocar-git`; todo comando es `correr-comando`; un `.md` es `escribir-documento`; otro archivo, `cambiar-codigo`; `base/`, `plantillas/`, `validadores/` y `adaptadores/` del estándar, `cambiar-estandar`; `documentacion/epicas/` y `pendientes/`, `trabajar-cadena`; un servicio de afuera, `ir-afuera`; los programas de base de datos, `tocar-datos` | Deducir la tarea del contenido | La acción se conoce exacta; el contenido se interpreta |
| La respuesta también se detiene si no se leyó `recibir-pedido` y `responder`, una vez por sesión | Dejar la respuesta sin control | Responder también es actuar, y es donde más se incumplen las reglas de redacción. El enganche mira si ya detuvo una vez, para no quedar en un ciclo |
| Lo leído se olvida al resumirse la conversación | Recordarlo toda la sesión | Lo que se resume sale del contexto, y el agente vuelve a no tenerlo |
| El registro de lo leído vive en `historico-chat/.leido/`, fuera del control de versiones | En el almacén de la herramienta | `01·C29`: dentro del repositorio; es estado de trabajo, como `.tocado/` |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

## 3. Desglose de tareas por criterio de aceptación

### CA-10 · Los archivos de reglas por tarea

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `base/tareas.md`: columnas de palabras clave y de acciones, en lugar de la de palabras | Estándar | 0,7 h | — | CP-001 |
| T-02 | `mapa_tareas.py`: leer las columnas nuevas, escribir `base/reglas-por-tarea/` partiendo lo que no quepa en una lectura, y validar que coincida | Validador | 2 h | T-01 | CP-003 |

### CA-08 · La palabra clave dice las tareas del mensaje

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-03 | `recuperar.py`: tareas por palabra clave; sin palabra, solo lo que rige siempre; nombra el archivo de cada tarea | Validador | 1,5 h | T-02 | CP-001 |

### CA-09 · Antes de actuar, las reglas completas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-04 | `leidas.py`: tareas de una acción, registro de lo leído por sesión y lo que falta | Validador | 1,5 h | T-01 | CP-002 |
| T-05 | `hook_antes.py`: detener la acción o la respuesta, anotar lo leído, olvidarlo al resumir | Adaptador | 1,5 h | T-04 | CP-002 |
| T-06 | `instalar.py`, `.gitignore` y `.claude/settings.json` | Validador | 0,7 h | T-05 | CP-002 |

### RNF · Requisitos no funcionales

| ID | Tarea | Categoría | Est. | Ev. |
|---|---|---|:--:|---|
| T-07 | Pruebas de `mapa_tareas`, `recuperar`, `leidas` y `hook_antes`, y ajuste de las del instalador | Pruebas | 2 h | CP-001 a CP-004 |
| T-08 | Guías, anatomía, `CLAUDE.md` y su plantilla | Documentación | 1 h | CP-004 |
| T-09 | `CHANGELOG.md` y `VERSION` en `39.6.0` | Trazabilidad | 0,2 h | CP-004 |
| T-10 | Cerrar HU-023 y H-1 | Trazabilidad | 0,2 h | — |

**Total estimado:** 11,3 h.

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-04, T-05, T-06, T-07, T-08, T-09, T-10.

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-08 | Mensajes reales de la sesión contra el recuperador | CP-001 | | ☐ |
| CA-09 | Entradas de la herramienta simuladas contra el enganche, en carpeta temporal | CP-002 | | ☐ |
| CA-10 | `validar.py tareas` sobre el repositorio y sobre una copia alterada | CP-003 | | ☐ |
| RNF | Pruebas tocadas, `estandar`, `amarre`, `versionado` | CP-004 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| CP-001 a CP-004 | Resultado de cada caso | [resultado_pruebas.md](resultado_pruebas.md) |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | El repositorio y carpetas temporales |
| Usuarios de prueba | No aplica |
| Datos precargados | Los mensajes reales del 2026-09-28 que se equivocaron |

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit de la fase. Si el enganche detiene de más, se quita de `.claude/settings.json` y el agente sigue trabajando con los avisos de cada mensaje.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Un proyecto no tiene que tocar nada: el instalador pone los enganches y los archivos por tarea le llegan con `base/`. Ninguna regla cambia qué exige. Por eso es MENOR.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

- Base: `01·C28`, `01·C29`, `01·C23`, `02·F5`, `02·F8`, `02·F23`, `20·M10`, `00·ID8`, `00·ID9`, `00·ID11` e `00·ID12` en todo lo que se escribe.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que leer las reglas de `cambiar-codigo`, unos 218.000 caracteres, llene el contexto | El resumen automático llega antes | Se lee una vez por sesión y después de cada resumen; se mide en la fase cuánto pesa cada parte | Abierto |
| B-02 | Que la detención de la respuesta quede en un ciclo | El agente no puede terminar | El enganche detiene una sola vez y deja pasar la segunda | Abierto |
| B-03 | Que una acción no esté en la tabla | Pasa sin reglas | Toda acción que no calza cae en `correr-comando` o `cambiar-codigo`, nunca en ninguna | Abierto |

## 11. Definition of Done

- [ ] CA-08 a CA-10 verificados con evidencia en la sección 5
- [ ] Las pruebas tocadas, `estandar`, `amarre` y `versionado` sin fallas
- [ ] HU-023 y H-1 cerrados, sin nada pendiente
- [ ] Commit autorizado por el usuario

## 12. Cambios después de la aprobación

El plan se aprobó el 2026-09-28. Lo que sigue se hizo después, sin actualizar el plan antes de tocar los archivos, en contra de `02·F8`. Se escribe acá para que el plan y el código vuelvan a coincidir.

| # | Qué cambió | Quién lo pidió | Archivos |
|---|---|---|---|
| 1 | Los archivos por tarea quedaron primero en la raíz y se movieron a `base/reglas-por-tarea/`, como decía el plan; los validadores los saltan | El usuario, 2026-09-28: corregir lo que el agente hizo sin autorización | `validadores/mapa_tareas.py`, `validadores/comun.py`, `base/reglas-por-tarea/` |
| 2 | Lo leído se olvidaba con cada mensaje del usuario, no solo al resumir; no contaba la lectura parcial | El usuario, 2026-09-28 | `hook_antes.py`, `validadores/instalar.py` |
| 3 | Toda escritura fuera del proyecto se detiene | El usuario, 2026-09-28 | `hook_antes.py` |
| 4 | Las reglas se leían con un comando, y cada archivo por tarea bajó a 25.000 caracteres | El usuario, 2026-09-28 («Hágalo») | `hook_antes.py`, `validadores/mapa_tareas.py`, `base/reglas-por-tarea/` |
| 5 | El enganche del commit no cuenta como marcas nuevas las de `base/reglas-por-tarea/` | El usuario, 2026-09-28 («Hágalo») | `validadores/marcas.py` |
| 6 | **Se quitó la lectura obligatoria**: sin la palabra de `01·C28`, el agente la recuerda y espera; con ella, recibe las reglas por dentro. `hook_antes.py` quedó solo con el freno de escrituras fuera del proyecto, y se borró `leidas.py` | El usuario, 2026-09-29 («Hágalo»): *«no se busca que el agente muestre constantemente que está leyendo o consultando las reglas»* | `validadores/recuperar.py`, `hook_antes.py`, `validadores/instalar.py`, `.gitignore`, `validadores/leidas.py` (borrado) |

**Archivos que el plan de la sección 2.1 no declaraba:** `validadores/comun.py`, `validadores/marcas.py`, `validadores/pruebas.py`, `validadores/docs/README.md`, `historico-chat/scripts/2026-09-28/` y el borrado de `validadores/leidas.py` y `validadores/docs/leidas.md`.

**Lo que ya no rige de las secciones 1 a 3:** la pieza 3 de la sección 1, las filas de `leidas.py` y de los enganches de `PostToolUse`, `Stop` y `SessionStart` de la sección 2.1, las decisiones de la sección 2.6 sobre detener la acción y la respuesta, y las tareas T-04 a T-06 tal como estaban escritas.

**Estado:** aprobados por el usuario el 2026-09-29 («Apruebo»). Rigen el 1, el 3, el 5 y el 6; el 2 y el 4 los quitó el 6 y quedan como registro.

## 13. Cierre

El cierre va en [funcionalidad_implementada.md](funcionalidad_implementada.md).
