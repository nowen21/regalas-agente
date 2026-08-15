# Plan de Trabajo — Fase A-EP-005-HU-008-enganche-del-resumen (módulo Automatismos)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en [HU-008](../HU-008-enganche-del-resumen.md); el detalle de las pruebas, en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase; lo que dieron al correrlas, en el [resultado_pruebas.md](resultado_pruebas.md); lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (identificador · [`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-008-enganche-del-resumen` |
| **Épica** | [EP-005](../../epica.md) |
| **HU** | [HU-008 El enganche que sostiene el resumen de la sesión](../HU-008-enganche-del-resumen.md) |
| **Módulo** | Automatismos |
| **Especificación del módulo** | [documentacion/automatismos/spec.md](../../../../automatismos/spec.md), escrita en esta fase: el módulo no tenía |
| **Fecha apertura** | 2026-08-14 |
| **Rama** | `feature/A-EP-005-HU-008-enganche-del-resumen` |

**ORIGEN** (`DOC12`): ✨ **Funcionalidad nueva.** Tercer y último eslabón de la cadena que abre el hallazgo H-4 del 2026-08-14. Los dos anteriores cerraron el mismo día: [`A-EP-003-HU-001`](../../../EP-003-documentos-modelo-y-procedimientos/HU-001-marca-de-espacio-por-llenar/A-EP-003-HU-001-marca-de-espacio-por-llenar/README.md) con el commit `b877f37` y [`A-EP-003-HU-009`](../../../EP-003-documentos-modelo-y-procedimientos/HU-009-modelo-del-resumen-de-sesion/A-EP-003-HU-009-modelo-del-resumen-de-sesion/README.md) con `e998cc2`. Con esta, H-4 queda cerrado: el resumen deja de depender de que alguien se acuerde.

**CA de la HU que cubre esta fase** (una sola HU · [`02·F12.1`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md) · trazabilidad `DOC11`)

| CA de HU-008 | Qué valida | Estado |
|---|---|---|
| [CA-01](../HU-008-enganche-del-resumen.md#ca-01--el-archivo-nace-solo) | El archivo nace solo | Cumple |
| [CA-02](../HU-008-enganche-del-resumen.md#ca-02--avisa-cuando-la-sesión-ya-produjo-algo-y-el-resumen-sigue-vacío) | Avisa qué le falta al resumen cuando la sesión produjo algo | Cumple |
| [CA-03](../HU-008-enganche-del-resumen.md#ca-03--del-propósito-se-muestra-lo-que-sigue-abierto-y-nada-más) | Del propósito se muestra lo que sigue abierto, y nada más | Cumple |

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que el resumen de la sesión exista aunque nadie se acuerde de escribirlo, que el hueco se vea mientras la sesión corre y diga qué falta, y que al declarar el propósito se vea lo que sigue abierto de él, sin ruido de otros temas.

**Resumen de exigencias a cubrir:**

| Exigencia | Escenario | Tipo | Complejidad |
|---|---|---|---|
| [CA-01](../HU-008-enganche-del-resumen.md#ca-01--el-archivo-nace-solo) | Se abre una sesión y el archivo aparece con el modelo puesto | Funcional | Media |
| [CA-02](../HU-008-enganche-del-resumen.md#ca-02--avisa-cuando-la-sesión-ya-produjo-algo-y-el-resumen-sigue-vacío) | La sesión hizo un commit y al resumen le falta algo | Funcional | Alta |
| [CA-03](../HU-008-enganche-del-resumen.md#ca-03--del-propósito-se-muestra-lo-que-sigue-abierto-y-nada-más) | Se muestra lo que sigue abierto del propósito de la sesión | Funcional | Media |
| [RNF-01](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales) | Avisa durante la sesión, no al cerrarla | No funcional | Baja |
| [RNF-02](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales) | Una vez por cada cosa que falta, máximo dos en la sesión | No funcional | Media |
| [RNF-03](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales) | No demora el arranque | No funcional | Media |

**Fuera de alcance** (qué explícitamente NO entra en esta fase):

- **Escribir los hallazgos.** El enganche crea, avisa y arrastra; reconocer un hallazgo es criterio.
- **Decidir con qué señal se sabe que el tema cerró.** Es la pregunta viva de H-4 y sigue sin decidir. No bloquea: el enganche mira si la sección de cierre está llena, no si el tema cerró de verdad.
- **Los siete enganches que ya existen.** Esta fase no los toca, salvo `historico.py`, que tiene que renombrar los dos archivos juntos.
- **Retro-documentar los enganches viejos**, que pide [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md). Es trabajo aparte.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado contra el repositorio el 2026-08-14, leyendo los enganches que ya corren y la tabla del instalador.

**Cómo se conecta un enganche.** [`validadores/instalar.py`](../../../../../validadores/instalar.py) tiene una tabla, `HOOKS_CLAUDE`, con una fila por enganche: evento, filtro, programa, mensaje y argumentos. De ahí sale el `.claude/settings.json` de cada proyecto. Agregar un enganche es agregar una fila; no hay que tocar la lógica.

**Los tres comportamientos caen en dos eventos que ya se usan:**

| Comportamiento | Evento | Con quién comparte |
|---|---|---|
| Crear el archivo y mostrar lo abierto | `SessionStart` | `hook_sesion.py`, `hook_recuerdos.py` |
| Avisar qué le falta al resumen | `UserPromptSubmit` | `hook_historico.py`, `hook_checklist.py` |

**El detalle que condiciona todo.** La transcripción nace como `AAAA-MM-DD-sesion.md` y se renombra cuando el tema está claro, con `historico.py --renombrar`. El resumen se llama igual sin la fecha, así que **los dos archivos tienen que moverse juntos**. Hoy `renombrar()` solo mueve la transcripción; si el resumen ya existe cuando se renombra, queda con el nombre viejo y el enlace del índice apunta a un archivo que no está.

**Cómo se sabe que "la sesión ya produjo algo"**, sin criterio y por dos caminos independientes:

1. Hubo un commit después de que la sesión abrió.
2. Cambió algún archivo de `base/` o de `plantillas/` respecto a la última confirmación.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/resumen.py` | Nuevo | Programa | Crea el archivo del día, lee los hallazgos de un resumen y junta lo que sigue abierto. No interpreta nada |
| `validadores/hook_resumen.py` | Nuevo | Programa | Los dos enganches: `SessionStart` crea y arrastra, `UserPromptSubmit` avisa |
| `validadores/historico.py` | Modificar | Programa | `renombrar()` mueve también el resumen, y el índice queda al día |
| `validadores/instalar.py` | Modificar | Programa | Dos filas nuevas en `HOOKS_CLAUDE` |
| `validadores/pruebas.py` | Modificar | Pruebas | Los casos de esta fase |
| `validadores/README.md` | Modificar | Documentación | Qué hace cada programa nuevo |
| `.claude/settings.json` | Modificar | Configuración | Los dos enganches, en este mismo repositorio |
| `plantillas/historico-chat.md` | Modificar | Plantilla | Explica que el resumen también lo crea un enganche |
| `validadores/reglas-validables.md` | Modificar | Documentación | [`DOC22`](../../../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md) pasa de pendiente a hecha, en la parte que un programa sí puede comprobar |
| `CHANGELOG.md` · `VERSION` | Modificar | Versionado | Entrada y subida de versión ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)) |

> **`validadores/reglas-validables.md` lo está editando otra sesión.** Ya pasó en las dos fases anteriores y se resolvió guardando solo las líneas propias. Se hace igual.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

| Archivo a refactorizar | Cambio de contrato | Archivos que dependen (rompen) | Dónde rompe |
|---|---|---|---|
| `validadores/historico.py` · `renombrar()` | Suma un efecto: mueve también el resumen. La firma no cambia | `hook_historico.py`, que lo llama; el comando que corre el usuario | No rompen: la firma y la salida son las mismas |
| `validadores/instalar.py` · `HOOKS_CLAUDE` | Dos filas más en una lista | El `.claude/settings.json` de cada proyecto instalado | No rompe: el instalador reescribe el archivo y ya sabe no duplicar |

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

N/A: son programas de línea de comandos. La entrada es la carpeta del proyecto y la salida es texto.

### 2.4 Punto de entrada en la UI  ·  `F14` Q7

N/A. Lo que se ve es el mensaje que el enganche imprime en la sesión.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Un programa aparte, `resumen.py`, y un enganche delgado que lo llama | Meterlo todo en `hook_resumen.py` | Es como están hechos los demás: la lógica se puede probar sin simular un enganche |
| El renombrado del resumen va dentro de `historico.py` | Un comando aparte que el agente corra después | Dos comandos que hay que acordarse de correr en orden es justo lo que esta fase viene a eliminar |
| "Produjo algo" se mide contra el estado de git al abrir la sesión | Contar los archivos escritos en el turno | Escribir un archivo no es producir: una sesión puede escribir borradores y no dejar nada |
| El aviso deja su marca dentro del propio resumen | Un archivo de estado aparte | Un archivo aparte se desincroniza y hay que limpiarlo. La marca vive donde vive el dato |
| El enganche no crea el resumen si la sesión no tiene todavía carpeta del día | Crear la carpeta siempre | Un proyecto sin carpeta de resúmenes no se ve afectado, que es lo que pide el criterio transversal de límites de la HU |

> Las decisiones no obvias se registran también como señal ([`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)).

### 2.7 Dudas por resolver antes de codificar

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | Qué se muestra de lo abierto al arrancar | usuario | **Resuelta** el 2026-08-14: solo lo del propósito que la sesión declara, sin límite de días pero sin nada de otros temas |
| 2 | Si el aviso se imprime también cuando el resumen tiene hallazgos pero no dice si se puede cerrar | usuario | **Resuelta** el 2026-08-14: sí. Avisa una vez por cada cosa que falta, máximo dos, y dice cuál |
| 3 | Qué hallazgos cuentan para cerrar la sesión | usuario | **Resuelta** el 2026-08-14: los del propósito de la sesión. Los que nacen acá y son de otro tema basta con dejarlos anotados |

> Ninguna tarea de construcción inicia con una duda abierta que la bloquee.

---

## 3. Desglose de tareas por criterio de aceptación

> Cada CA se descompone en tareas atómicas. **Depende de** ordena la ejecución; **Ev.** referencia la evidencia de §5.
>
> Cada `CA-0N` y cada `RNF-0N` se escriben como enlace a su exigencia en la HU.

### [CA-01](../HU-008-enganche-del-resumen.md#ca-01--el-archivo-nace-solo) — El archivo nace solo

| ID | Tarea | Capa | Est. | Depende de | Estado | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | Escribir `resumen.py`: dónde va el archivo del día y cómo se llama, a partir del nombre de la transcripción | Backend | 2 h | — | ☑ | EV-01 |
| T-02 | Crearlo con el modelo puesto y sin hallazgos, y no pisarlo si ya está | Backend | 2 h | T-01 | ☑ | EV-01 |
| T-03 | Escribir `hook_resumen.py` para `SessionStart`, que llama a lo anterior | Backend | 1 h | T-02 | ☑ | EV-01 |
| T-04 | Que `renombrar()` de `historico.py` mueva también el resumen y corrija el índice | Backend | 3 h | T-01 | ☑ | EV-01 |
| T-05 | Prueba: sesión nueva, segunda sesión el mismo día, y renombrado que mueve los dos | Test | 2 h | T-03, T-04 | ☑ | EV-01 |

### [CA-02](../HU-008-enganche-del-resumen.md#ca-02--avisa-cuando-la-sesión-ya-produjo-algo-y-el-resumen-sigue-vacío) — Avisa cuando la sesión produjo algo y el resumen sigue vacío

| ID | Tarea | Capa | Est. | Depende de | Estado | Ev. |
|---|---|---|:--:|---|---|---|
| T-06 | Detectar que la sesión produjo algo, por los dos caminos: commit y cambio en `base/` o `plantillas/` | Backend | 3 h | — | ☑ | EV-02 |
| T-07 | Detectar qué le falta al resumen: ningún hallazgo, o hallazgos sin decir si se puede cerrar | Backend | 2 h | T-01 | ☑ | EV-02 |
| T-08 | Imprimir el aviso con la lista de lo que falta, una vez por hueco, y dejar la marca en el propio resumen | Backend | 3 h | T-06, T-07 | ☑ | EV-02 |
| T-09 | Prueba: los dos avisos, cada uno una vez; calla cuando no falta nada y cuando la sesión no produjo nada | Test | 2 h | T-08 | ☑ | EV-02 |

### [CA-03](../HU-008-enganche-del-resumen.md#ca-03--del-propósito-se-muestra-lo-que-sigue-abierto-y-nada-más) — Lo que no se cerró aparece en la sesión siguiente

| ID | Tarea | Capa | Est. | Depende de | Estado | Ev. |
|---|---|---|:--:|---|---|---|
| T-10 | Encontrar el hallazgo del propósito por su `AAAA-MM-DD · tema · H-N` y leer si sigue abierto | Backend | 3 h | T-01 | ☑ | EV-03 |
| T-11 | Imprimirlo con su archivo y su pregunta viva, y no imprimir nada de otros temas | Backend | 2 h | T-03, T-10 | ☑ | EV-03 |
| T-12 | Prueba: dos abiertos se listan; cerrados no aparecen | Test | 2 h | T-11 | ☑ | EV-03 |

### RNF — Requisitos no funcionales

| ID | Tarea | Categoría | Est. | Estado | Ev. |
|---|---|---|:--:|---|---|
| T-13 | Comprobar que el enganche sale con código 0 aunque no pueda escribir | [RNF-01](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales) | 1 h | ☑ | EV-04 |
| T-14 | Comprobar que cada aviso sale una sola vez y que no pasan de dos | [RNF-02](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales) | 1 h | ☑ | EV-04 |
| T-15 | Medir cuánto suma al arranque, con un histórico de 35 sesiones | [RNF-03](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales) | 1 h | ☑ | EV-04 |
| T-16 | Dos filas nuevas en `HOOKS_CLAUDE` y correr el instalador contra este repositorio | Backend | 2 h | T-03, T-08 | ☑ | EV-04 |
| T-17 | Documentar los dos programas en `validadores/README.md` y pasar [`DOC22`](../../../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md) a hecha | Documentación | 1 h | T-16 | ☑ | EV-04 |
| T-18 | Entrada en `CHANGELOG.md` y subida de `VERSION` ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)) | Documentación | 1 h | T-17 | ☑ | EV-04 |

**Total estimado:** 34 h. Eran 31 antes de que el usuario precisara el aviso: dice qué falta, sale una vez por hueco y mira solo los hallazgos del propósito.

### Ampliación del 2026-08-14 — la fase se reabre

> **Por qué.** La fase se dio por cerrada y el programa no hace lo que [CA-01](../HU-008-enganche-del-resumen.md#ca-01--el-archivo-nace-solo) pide: el archivo no nace nunca. Las tareas de arriba quedaron hechas, pero seis de los nueve casos se corrieron llamando la función por dentro, así que no probaron el camino. El usuario decidió reabrir esta fase y no abrir una nueva: lo que falla es este trabajo, y su documentación decía que estaba hecho.

| ID | Tarea | Capa | Est. | Depende de | Estado | Ev. |
|---|---|---|:--:|---|---|---|
| T-19 | Sacar la creación de `inicio()` a una función que usen los dos modos, porque al abrir la sesión la transcripción todavía no existe | Backend | 2 h | — | ☑ | EV-05 |
| T-20 | Que el turno en que nace el archivo muestre el mensaje de arranque, y el aviso empiece en el siguiente | Backend | 1 h | T-19 | ☑ | EV-05 |
| T-21 | Que el instalador deje puesta `historico-chat/resumenes/` con su índice | Backend | 1,5 h | — | ☑ | EV-05 |
| T-22 | Quitar del encabezado del resumen el enlace a `plantillas/`, que no viaja al proyecto | Backend | 0,5 h | — | ☑ | EV-05 |
| T-23 | Corrida 2 de las pruebas: cada caso dispara el enganche como orden del sistema, sobre un proyecto que instala el instalador | Test | 3 h | T-19 a T-22 | ☑ | EV-05 |
| T-24 | Anular la corrida 1 en el resultado, corregir la especificación del módulo y versionar | Documentación | 2 h | T-23 | ☐ | EV-05 |

**Ampliación:** 6 tareas · 10 h. **Total de la fase:** 44 h.

**Archivos que suma esta ampliación a §2.1:** `validadores/hook_resumen.py` (modificar), `validadores/resumen.py` (modificar), `validadores/instalar.py` (modificar), `validadores/pruebas.py` (modificar), `documentacion/automatismos/spec.md` (modificar).

**Decisiones de la ampliación:**

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El archivo se asegura en los dos modos | Solo en el mensaje del usuario | Así la sesión que se retoma lo tiene desde el arranque y la nueva en el primer turno |
| Si en un turno la transcripción no está, el siguiente lo crea | Ordenar los enganches del evento | Los enganches del mismo evento pueden correr a la vez y el orden no está garantizado |
| La carpeta la deja el instalador | Que el programa la cree | Así sigue en pie el límite de la HU: un proyecto sin instalar no se ve afectado |
| El encabezado enlaza el índice del histórico del proyecto | Enlazar `plantillas/sesion.md` | `plantillas/` es del estándar y no viaja: ahí el enlace nacía roto |

> **Corrige la decisión de §2.6** *"el enganche no crea el resumen si la sesión no tiene todavía carpeta del día"*: la decisión se conserva, lo que cambia es que la carpeta llegue instalada.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-04 → T-06 → T-08 → T-11 → T-16 → T-18

**Paralelizables:** T-10 no depende de T-06; las pruebas de cada CA avanzan apenas su comportamiento está.

> Solo se tocan los archivos declarados en §2.1 (`F8`). Descubrir uno nuevo → PAUSAR, reportar, ampliar el plan con OK, no editar por iniciativa.

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

> Una exigencia no se marca cumplida sin evidencia. La fase no cierra con alguna en rojo.

| Exigencia | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| [CA-01](../HU-008-enganche-del-resumen.md#ca-01--el-archivo-nace-solo) | Prueba automática sobre un proyecto de prueba, abriendo dos sesiones el mismo día | EV-01 | 2026-08-14 | ☑ |
| [CA-02](../HU-008-enganche-del-resumen.md#ca-02--avisa-cuando-la-sesión-ya-produjo-algo-y-el-resumen-sigue-vacío) | Prueba automática con commit sembrado y resumen vacío | EV-02 | 2026-08-14 | ☑ |
| [CA-03](../HU-008-enganche-del-resumen.md#ca-03--del-propósito-se-muestra-lo-que-sigue-abierto-y-nada-más) | Prueba automática con dos temas abiertos: se muestra el del propósito y no el otro | EV-03 | 2026-08-14 | ☑ |
| [RNF-01](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales) | El aviso sale en un turno intermedio, no al final | EV-04 | 2026-08-14 | ☑ |
| [RNF-02](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales) | Dos turnos seguidos con la misma condición: un solo aviso | EV-04 | 2026-08-14 | ☑ |
| [RNF-03](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales) | Medición del arranque con el histórico real | EV-04 | 2026-08-14 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de la suite, casos de creación y renombrado | `validadores/pruebas.py` |
| EV-02 | Salida de la suite, casos del aviso | `validadores/pruebas.py` |
| EV-03 | Salida de la suite, casos de lo abierto del propósito | `validadores/pruebas.py` |
| EV-04 | Corrida completa y medición del arranque | Terminal |

---

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | Carpetas temporales creadas por la propia suite. Nunca datos reales ([`00·N4`](../../../../../base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada) · [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)) |
| Usuarios de prueba | N/A: no hay autenticación |
| Datos precargados | Proyectos de prueba: sin carpeta de resúmenes, con resumen vacío, y con resumen de hallazgos abiertos y cerrados |

> El detalle completo va en el [plan_pruebas.md](plan_pruebas.md).

---

## 7. Reversión / rollback  ·  `F14` Q11

Los dos programas nuevos se borran y los tres modificados vuelven a su versión anterior. Los enganches salen del `.claude/settings.json` al correr el instalador otra vez. Los resúmenes ya creados no se borran: son documentos del usuario, no artefactos del programa.

---

## 8. Producción y migración incremental  ·  `F10` · `F14` Q12

Aditivo. Un proyecto instalado hoy no tiene los dos enganches: los recibe al correr el instalador, y desde ahí sus sesiones nuevas empiezan a crear el resumen. Las sesiones viejas no se tocan. Por eso el cambio es MENOR y no MAYOR: lo que obliga es [`13·DOC22`](../../../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md), que ya rige desde la 14.0.0; esto es lo que la hace cumplible sin depender de la memoria.

---

## 9. Reglas del estándar y del proyecto aplicadas  ·  `F14` Q13

- Base: [`02·F2`](../../../../../base/02-flujo-de-trabajo/reglas/F2-sin-spec-acordada-no-hay-codigo.md), [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F12.1`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar), [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md), [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`13·DOC22`](../../../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md), [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).
- Proyecto: N/A. Este repositorio es el estándar y no tiene catálogo de reglas propias.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Las tres dudas de §2.7 sin responder | Bloqueaban T-08 y T-11 | Respondidas por el usuario el 2026-08-14 | Cerrado |
| B-02 | Leer git en cada mensaje puede demorar el turno | El agente se sentiría lento | T-06 mide antes de dejarlo fijo; si demora, se consulta una vez y se guarda | Abierto |
| B-03 | El renombrado toca dos archivos y puede quedar a medias | El índice apuntaría a un archivo que no existe | T-04 mueve primero el resumen y después la transcripción, y deja el índice de último | Abierto |
| B-04 | Que el aviso se vuelva ruido | Se deja de leer, y con eso se pierde el resumen igual | Máximo dos en la sesión, cada uno una vez, y siempre diciendo qué falta | Abierto |

---

## 11. Definition of Done

- [ ] Todas las exigencias de §0 y §1 verificadas con evidencia (§5)
- [ ] Pruebas de la fase en verde (alcance quirúrgico · `F5`)
- [ ] Trazabilidad especificación → implementación sin faltantes (`DOC11`)
- [ ] Documentación e índices actualizados (`13`)
- [ ] Señales registradas (`DOC5`)
- [ ] Rama lista para el commit único de la fase (`G1`)
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario  ·  *(opcional — equipo)*

| Fecha | Tareas cerradas | Avance CA | Bloqueos | Ajuste al plan |
|---|---|---|---|---|
| 2026-08-14 | Las dieciocho | Las siete exigencias en verde | Ninguno | Sin ampliaciones: el plan alcanzó |

---

## 13. Cierre

**Resultado:** las siete exigencias cumplidas, con dos defectos encontrados y corregidos dentro de la fase. **Esfuerzo real vs. estimado:** 31 h estimadas.

**Lecciones aprendidas:** la suite encontró los dos defectos, y el peor era el que rompía el límite de la propia historia: el programa escribía un hallazgo de ejemplo, cuando la HU dice que el enganche no escribe hallazgos. Un límite declarado en la HU necesita su caso de prueba, o no se nota que se rompió.

**Deuda técnica generada:**

| Descripción | Registro / ticket |
|---|---|
| El aviso mira si la sección de cierre está llena, no si el tema cerró de verdad | La pregunta viva de H-4: con qué señal se sabe que un tema cerró |
| Los siete enganches viejos siguen sin especificación de módulo | `13·DOC6` pide retro-documentarlos; es trabajo aparte |
