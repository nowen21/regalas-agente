# Plan de Trabajo — Fase «A-EP-007-HU-006-poner-al-dia-lo-ya-instalado» (módulo «Instalación»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Se escribe **antes** de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-007-HU-006-poner-al-dia-lo-ya-instalado` |
| **Épica** | [EP-007 Instalación y actualización](../../epica.md) |
| **HU** | [HU-006 — Poner al día lo ya instalado](../HU-006-poner-al-dia.md) — **una sola** (`F12.1`) |
| **Módulo** | Instalación (`validadores/instalar.py`) |
| **Especificación del módulo** | No existe todavía. Esta fase **no la escribe**: sigue declarada como deuda desde la fase [`A-EP-007-HU-001`](../../HU-001-instalar-con-una-linea/A-EP-007-HU-001-rellenar-los-marcadores-al-copiar/plan_trabajo.md) (§10, `B-02`) |
| **Fecha apertura** | 2026-08-16 |
| **Rama** | `main` — el repositorio del estándar trabaja sobre la principal |

**ORIGEN** (`13·DOC12`):

- 📝 **Modifica fase(s):** complementa a [`A-EP-007-HU-001`](../../HU-001-instalar-con-una-linea/A-EP-007-HU-001-rellenar-los-marcadores-al-copiar/plan_trabajo.md), que arregló los tres puntos de copia. Aquella alcanza a lo que se instale **desde ahora**; esta alcanza a lo que **ya estaba instalado**.
- ✨ **Funcionalidad nueva:** el registro de versión cuando sube el estándar sin que cambie ninguna plantilla del proyecto.
- 🔀 **Híbrido:** sí, es de los dos tipos.

**De dónde sale:** los pendientes [42](../../../../../pendientes/42-el-arreglo-del-40-no-llega-a-los-proyectos-ya-instalados.md) y [44](../../../../../pendientes/44-el-registro-de-version-no-se-escribe-si-no-cambia-una-huella.md), los dos reportados por el proyecto `shopnest-mesa`.

**Por qué los dos en una sola fase.** Son el mismo defecto: el instalador decide si hay trabajo mirando una huella, y cuando la huella no cambia se queda quieto aunque el proyecto sí esté mal. Separarlos deja dos parches en la misma decisión de `instalar.py`. Y calzan uno por criterio: el 42 es el CA-01 de la HU y el 44 es su CA-02.

**CA de la HU que cubre esta fase:**

| CA de `HU-006` que cierra esta fase | Estado |
|---|---|
| [CA-01 — Lo viejo se detecta y se pone al día](../HU-006-poner-al-dia.md#ca-01--lo-viejo-se-detecta-y-se-pone-al-día) | ☐ |
| [CA-02 — Queda registro de qué se actualizó](../HU-006-poner-al-dia.md#ca-02--queda-registro-de-qué-se-actualizó) | ☐ |

**Por qué el CA-01.** «Ese componente se detecta como viejo y queda al día» hoy solo vale si cambió la plantilla. Un archivo que quedó mal escrito por un defecto del instalador está viejo igual, y la detección no lo ve.

**Por qué el CA-02.** «Se puede reconstruir desde cuándo el proyecto usa cada versión» es exactamente lo que hoy no se puede: `shopnest-mesa` usa la `21.1.1` y su último registro dice `20.0.1`.

---

## 1. Objetivo y alcance

**Objetivo:** que un proyecto ya instalado quede al día corriendo el instalador —sin banderas, sin editar nada a mano— tanto en el texto de lo copiado como en el registro de versión.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Un archivo ya copiado conserva un marcador crudo y el instalador lo repara | Funcional | Media |
| CA-02 | Sube la versión del estándar sin cambiar plantillas y queda el registro | Funcional | Baja |

**Decisiones del usuario que abren esta fase** (las dos estaban pendientes en los archivos de los pendientes, y se resolvieron el 2026-08-16):

| Pendiente | Salida elegida | Descartadas |
|---|---|---|
| 42 | **Rellenar los marcadores en lo ya copiado**, sin tocar nada más | La bandera `--forzar` y calcular la huella del archivo copiado |
| 44 | **Subir de versión es por sí solo motivo de registro** | Que el checklist deje de reprobar |

**Fuera de alcance:**

- **Reescribir el contenido de los archivos que llena el proyecto.** Se sustituye el marcador y nada más. Los cuatro archivos de `.agente/` traen huecos a propósito —lo dejó dicho el `DEF-01` de la fase anterior— y esos no se tocan.
- **Escribir la especificación del módulo de instalación.** Sigue siendo deuda de la fase anterior.
- **Avisarle a `shopnest-mesa`** que sus dos reportes cerraron. Depende del [pendiente 36](../../../../../pendientes/36-falta-la-regla-que-obliga-a-reportar-lo-que-es-del-estandar.md), que todavía no fija el procedimiento.
- **Poner al día los demás proyectos del registro.** Correrles el instalador es una operación aparte, y la autoriza el usuario.

---

## 2. Análisis previo — línea base verificada

### 2.1 Archivos que se crean o modifican

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/instalar.py` | Modificar | Instalación | El envoltorio de relleno y la condición del registro; ver §2.2 |
| `plantillas/stack-instalacion.md` | Modificar | Plantilla | El texto de arreglo de la fila `versiones` manda hacer lo que ya se hizo |
| `validadores/tests/test_instalar_reparar.py` | Nuevo | Test | Los casos de esta fase |
| `validadores/docs/instalar.md` | Modificar | Documentación | Qué repara el instalador en una copia que ya existía |
| `documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-006-poner-al-dia/HU-006-poner-al-dia.md` | Modificar | Documentación | §8, nombrar esta fase (trazabilidad en los dos lados) |
| `pendientes/README.md` | Modificar | Backlog | Marcar el 42 y el 44 como hechos |
| `pendientes/hecho/` | Nuevo | Backlog | El archivo de lo cerrado |
| `CHANGELOG.md` | Modificar | Versionado | Entrada de la versión |
| `VERSION` | Modificar | Versionado | Sube el número |

**Verificado el 2026-08-16** contra el repositorio y contra `shopnest-mesa`:

- `.agente/stack-instalacion.md` de `shopnest-mesa` conserva `«RUTA-ESTANDAR»` literal; los cuatro archivos de `.agente/` y el índice de memoria de ese proyecto **no** tienen marcadores crudos de los que el instalador sabe llenar.
- Su carpeta `documentacion/versiones/` tiene tres registros y el último es `2026-08-16-20.0.1.md`, con la `21.1.1` instalada.

### 2.2 Matriz de dependencias del cambio

**CA-01 — dónde se repara.** Hoy cada punto de copia decide por su cuenta si escribe, y cuando decide que no, el archivo se queda como esté. Se agrega **un solo envoltorio** por el que pasa toda copia ya existente — que es la deuda que la fase anterior declaró en su §2.6 y no quiso meter en un arreglo `P0`.

| Función | Qué hace hoy con un archivo que ya existe | Qué hará |
|---|---|---|
| `instalar_stack` (línea 311) | Si la huella coincide, devuelve «ya estaba al día» y no lo abre | Antes de devolver, pasa el archivo por el envoltorio |
| `instalar_agente_config` (línea 690) | `continue`: no lo toca | Pasa cada uno de los cuatro por el envoltorio |
| `instalar_recuerdos` (línea 402) | Solo le refresca el sello | Pasa el índice por el envoltorio |
| `instalar_historico` (línea 338) | Solo le refresca el sello | Pasa el README por el envoltorio. Hoy su plantilla no tiene marcadores; entra igual para que mañana no sea la excepción olvidada |
| `instalar_claude_md` (línea 577) | **Ya rellena** los marcadores del archivo existente | No cambia. Es el precedente del que sale esta salida |

**El envoltorio no inventa nada:** aplica `_rellenar(texto, _rellenos(ruta))`, que solo sustituye los marcadores que el instalador sabe calcular. Un hueco que llena el proyecto no está en ese diccionario, así que no se toca. Si el texto no cambia, no se escribe el archivo ni se reporta paso.

**CA-02 — cuándo se registra.** `registrar_version` (línea 874) solo escribe si alguna huella cambió. Se le agrega la segunda condición: que la versión del estándar sea distinta de la que traía el proyecto — dato que ya se calcula en `_version_anterior` y ya se le pasa. `versiones.registrar` **ya sabe escribir ese caso**: su rama `else` imprime «Ninguno cambió de huella: solo se refrescó la instalación». No hay que tocar `versiones.py`.

| Quién depende | Impacto |
|---|---|
| `checklist.revisar_registro` | Deja de reprobar solo: el registro que le falta pasa a existir. No se modifica |
| `versiones.registrar` | Se llama en un caso más. Su firma y su salida no cambian |

### 2.3 Rutas / endpoints y control de acceso

No aplica: es un programa de línea de comandos, sin rutas ni permisos.

### 2.4 Punto de entrada en la interfaz

No aplica. Lo que cambia se ve al correr la instalación en un proyecto que ya la tenía.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Un envoltorio único de reparación por el que pasan las cinco copias | Repetir el relleno en cada función | Es el mismo defecto que la fase anterior dejó como deuda: cinco sitios que deciden por separado ya produjeron un olvido, y repetirlo produciría el siguiente |
| Reparar siempre, sin bandera | `--forzar` | Una bandera hay que acordarse de correrla, y sobre los cuatro archivos de `.agente/` reescribir borraría lo que el proyecto llenó |
| El envoltorio no escribe si el texto no cambió | Reescribir siempre | Reescribir sin cambios ensucia la salida y toca la fecha de archivos que están bien |
| El registro por subida de versión **no** se escribe en la carpeta del propio estándar | Escribirlo también ahí | El estándar ya lleva su `CHANGELOG`, no es un proyecto que lo herede, y su `versiones` ni siquiera se revisa (`comprobar` sale antes cuando es el propio) |
| Corregir el texto de arreglo de la fila `versiones` de la plantilla | Dejarlo | Hoy dice «Escribe un registro cada vez que algo cambia de huella», que describe lo que el instalador ya hizo: quien lo lea vuelve a correr el instalador y vuelve al mismo sitio |

**Efecto lateral querido:** tocar `plantillas/stack-instalacion.md` le cambia la huella, así que todo proyecto que corra el instalador reescribirá su `.agente/stack-instalacion.md`. El de `shopnest-mesa` queda reparado por esa vía **además** de por el envoltorio. Las dos rutas se prueban por separado (CP-001 y CP-002).

### 2.7 Dudas por resolver antes de codificar

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | ¿Se repara sin bandera o con `--forzar`? | usuario | **Resuelta 2026-08-16:** sin bandera, rellenando en sitio |
| 2 | ¿Subir de versión es motivo de registro? | usuario | **Resuelta 2026-08-16:** sí |

---

## 3. Desglose de tareas por criterio de aceptación

### [CA-01](../HU-006-poner-al-dia.md#ca-01--lo-viejo-se-detecta-y-se-pone-al-día) — Lo viejo se detecta y se pone al día

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Escribir el envoltorio `_reparar_marcadores(archivo, ruta, aplicar, etiqueta)`: lee, aplica `_rellenar`, escribe solo si cambió y devuelve el paso | Instalación | 1 h | — | EV-01 |
| T-02 | Llamarlo desde `instalar_stack`, incluso en el camino de «ya estaba al día» | Instalación | 0,5 h | T-01 | EV-01 |
| T-03 | Llamarlo desde `instalar_agente_config` para cada archivo que ya existía | Instalación | 0,5 h | T-01 | EV-01 |
| T-04 | Llamarlo desde `instalar_recuerdos` e `instalar_historico` | Instalación | 0,5 h | T-01 | EV-01 |
| T-05 | Prueba: instalar, ensuciar a mano una copia con un marcador, reinstalar y comprobar que quedó limpia | Test | 2 h | T-02, T-03, T-04 | EV-01 |
| T-06 | Prueba: que un hueco que llena el proyecto **sobreviva** a la reparación | Test | 1 h | T-05 | EV-02 |

### [CA-02](../HU-006-poner-al-dia.md#ca-02--queda-registro-de-qué-se-actualizó) — Queda registro de qué se actualizó

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-07 | En `registrar_version`, registrar también cuando la versión anterior difiere de la instalada; exento el propio estándar | Instalación | 1 h | — | EV-03 |
| T-08 | Corregir el texto de arreglo de la fila `versiones` en `plantillas/stack-instalacion.md` | Plantilla | 0,5 h | — | EV-04 |
| T-09 | Prueba: instalar, subir el `VERSION` del estándar sin tocar plantillas, reinstalar y comprobar que aparece el registro y que el checklist llega a completo | Test | 2 h | T-07 | EV-03 |
| T-10 | Prueba: reinstalar sin cambio de versión ni de huella **no** agrega registro | Test | 1 h | T-09 | EV-03 |

### Cierre de la fase

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-11 | Actualizar `validadores/docs/instalar.md` y el §8 de la HU-006 | Documentación | 0,5 h | T-10 | EV-05 |
| T-12 | Cerrar el 42 y el 44 en `pendientes/README.md` y escribir su archivo en `pendientes/hecho/` | Backlog | 0,5 h | T-11 | — |
| T-13 | Entrada en `CHANGELOG.md` y subir `VERSION` | Versionado | 0,5 h | T-12 | — |

**Total estimado:** 11,5 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-04 → T-05 → T-06 → T-09 → T-10 → T-11 → T-12 → T-13
**Paralelizables:** T-07 y T-08 son independientes del envoltorio y pueden ir en cualquier momento antes de T-09.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Descubrir uno nuevo → PAUSAR, reportar, ampliar el plan con OK.

---

## 5. Verificación de criterios de aceptación

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| [CA-01](../HU-006-poner-al-dia.md#ca-01--lo-viejo-se-detecta-y-se-pone-al-día) | Prueba automática sobre carpeta temporal + comprobación manual en `shopnest-mesa` | EV-01, EV-02, EV-06 | | ☐ |
| [CA-02](../HU-006-poner-al-dia.md#ca-02--queda-registro-de-qué-se-actualizó) | Prueba automática con subida de versión simulada | EV-03, EV-04 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de la prueba de reparación | `resultado_pruebas.md` de esta fase |
| EV-02 | Salida de la prueba del hueco que sobrevive | `resultado_pruebas.md` de esta fase |
| EV-03 | Salida de la prueba del registro | `resultado_pruebas.md` de esta fase |
| EV-04 | Texto nuevo de la fila `versiones` | `resultado_pruebas.md` de esta fase |
| EV-05 | Documentación al día | `funcionalidad_implementada.md` del cierre |
| EV-06 | Verificación manual: correr el instalador en `shopnest-mesa` y abrir el enlace de la línea 25 de su `.agente/stack-instalacion.md` | `resultado_pruebas.md` de esta fase |

---

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | Carpeta temporal desechable, creada y borrada por la prueba ([`00·N4`](«RUTA-ESTANDAR»/base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada), [`08·T4`](«RUTA-ESTANDAR»/base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)) |
| Excepción | La EV-06 sí corre sobre `shopnest-mesa`, que es un proyecto real. Es lo único que prueba de verdad que el reporte cerró, y **la autoriza el usuario aparte**: el instalador ahí escribe |
| Usuarios de prueba | No aplica |
| Datos precargados | Ninguno: la prueba instala primero y ensucia después, que es la secuencia del defecto |

---

## 7. Reversión / rollback

Se revierte volviendo el commit atrás. Lo que el envoltorio escribe es idempotente y solo sustituye marcadores conocidos, así que revertir deja los proyectos como están hoy — con el marcador crudo, que es el punto de partida. Los registros de versión ya escritos se quedan; sobran, no estorban.

---

## 8. Producción y migración incremental

**Sí toca algo que está en producción:** los proyectos ya instalados. El cambio es **reparador y aditivo**, y se aplica la próxima vez que cada proyecto corra el instalador. Ninguno pierde texto propio: el envoltorio no sustituye lo que no está en `_rellenos`.

`shopnest-mesa` es el caso de origen y el que confirma el cierre (EV-06). Los demás proyectos del registro se ponen al día cuando el usuario lo pida — no entra en esta fase.

---

## 9. Reglas del estándar y del proyecto aplicadas

- Base: [`02·F23`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) (por qué esta fase existe), [`02·F4`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F12`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md), [`02·F14`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md), [`02·F17`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T4`](«RUTA-ESTANDAR»/base/08-pruebas.md#t4--protege-los-datos-reales-al-probar), [`13·DOC19`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md), [`20·M10`](«RUTA-ESTANDAR»/base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).
- Proyecto: el `CLAUDE.md` de este repositorio, §2 y §4.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que el envoltorio sustituya un hueco que el proyecto tenía que llenar | Se perdería texto que el estándar no sabe reponer | `_rellenar` solo conoce los marcadores de `_rellenos`; el CP-003 lo comprueba a propósito | Abierto hasta el CP-003 |
| B-02 | Que el registro por subida de versión llene la carpeta de ruido | Un archivo por versión aunque no pase nada | Es lo que se decidió: el rastro de bajo qué versión cerró cada fase es el propósito de la carpeta. Sin cambio de versión no se escribe (CP-005) | Aceptado |
| B-03 | Que el propio estándar empiece a escribirse registros | Ruido en un repositorio que ya lleva `CHANGELOG` | Exento por `es_el_estandar` (T-07) | Abierto hasta el CP-004 |
| B-04 | El módulo de instalación sigue sin especificación | Se toca código sin documento que diga qué debe hacer | Deuda heredada de la fase anterior; no se salda acá | Abierto |

---

## 11. Definition of Done

- [ ] Los dos CA de §0 verificados con evidencia (§5)
- [ ] Una copia ensuciada con un marcador queda limpia al reinstalar
- [ ] Un hueco que llena el proyecto sobrevive a la reparación
- [ ] Sube la versión sin cambiar plantillas → hay registro y el checklist llega a completo
- [ ] `validadores/docs/instalar.md` y el §8 de la HU-006 al día
- [ ] El 42 y el 44 cerrados en `pendientes/`
- [ ] Entrada en `CHANGELOG.md` y `VERSION` subida
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica: el trabajo lo lleva una sola persona y el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md` de esta fase. Este plan se queda como se aprobó, para poder comparar lo que se dijo contra lo que pasó.
