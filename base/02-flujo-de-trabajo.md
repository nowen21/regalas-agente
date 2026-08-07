# 02 · Flujo de trabajo  ·  `[CAPA 2]`

Cómo trabaja el agente: de la solicitud a la tarea terminada. La capa 3 define dónde viven los documentos y cómo se corren las pruebas.

---

## F0 · La secuencia completa — de la necesidad al cierre

Este capítulo detalla sobre todo **del plan hacia abajo** (F2 en adelante). Pero un desarrollo empieza **antes** del plan. Esta es la secuencia macro completa, con dónde vive la regla de cada paso:

| # | Paso | Qué responde | Dónde está la regla |
|---|---|---|---|
| 0 | **Necesidad / idea** | qué quiere resolver el negocio | se escribe **siempre** como **brief** (`plantillas/brief.md` → `prompts/<slug>-brief.md`) · **obligatorio** |
| 1 | **Análisis / contexto** | qué existe hoy, restricciones, normativa | `F1` · `F4.3` · skill `analizar-proyecto` |
| 2 | **Objetivo + criterio de éxito** | qué se logra y cómo se sabe que se logró | `00-identidad` · skill `proponer-alcance` |
| 3 | **Alcance (qué SÍ / qué NO)** | el borde del trabajo | skill `proponer-alcance` · `00-identidad` |
| 4 | **Épica / Feature** | el bloque grande de funcionalidad | `plantillas/epica.md` → `13·DOC16` (definición abajo) |
| 5 | **HU** | la épica descompuesta en historias con criterios de aceptación | `13·DOC15` |
| 6 | **Fase (ejecución)** — spec → **plan** → implementar → probar → cerrar → commit | cómo y cuándo se construye | `F2`–`F11` · las 11 etapas de `F4.2` |

**Cadena obligatoria — sin excepción por tamaño.** Sin **brief** no hay **épica**, sin épica no hay **HU**, sin HU no hay **spec/plan**, sin plan aprobado no hay **código**. Ningún eslabón se salta, se fusiona con otro ni se omite por ser el trabajo "chico": **todo desarrollo** (funcionalidad nueva o cambio de comportamiento) recorre la cadena completa `brief → épica → HU → spec → plan → código`, grande o chico. Si te piden un paso y falta el anterior, **PAUSAR y crearlo primero** — nunca inventar hacia adelante. Lo **único** fuera de la cadena es lo que **no es desarrollo**: lectura/investigación, config local, comandos que el usuario pide y bugfix que solo realinea el código a la spec existente (`F2` excepciones).

**El brief (paso 0)** es la necesidad escrita y sus restricciones — el insumo del flujo, no una orden. Plantilla: `plantillas/brief.md` → se copia al proyecto como `prompts/<slug>-brief.md`.

**Épica / Feature (paso 4)** — un bloque de funcionalidad con valor de negocio, demasiado grande para una sola HU. Se descompone en varias HUs, y cada HU declara a qué épica pertenece (`HU.md §1`). No confundir con:

- **Módulo** — unidad **técnica** (un dominio del sistema con su código y rutas · `13·DOC13`).
- **Fase** — unidad de **ejecución** (**el paso 6**): un plan de trabajo con su cierre y commit (`F4.2`). Es lo que sigue después de la HU; su **relación con la HU** (`F12.1`) y su **nomenclatura** (`F12.6`) las define F12 (fuente única).
- **Épica** — unidad de **necesidad**: agrupa historias afines por el valor que entregan.

Ejemplo: épica *"Facturación electrónica"* → HU *"emitir factura"* + HU *"anular factura"* + HU *"consultar factura"*.

**Sin atajos por tamaño.** Un trabajo chico **no** exime de la cadena: igual lleva su brief, su épica, su HU, su spec y su plan — cada uno **existe como artefacto propio**, no se omite ni se fusiona con otro. El orden es siempre: entender → definir necesidad y borde → descomponer (épica → HU) → planificar → construir.

```
INCORRECTO: llega una idea → se escribe el plan de trabajo directo
            (sin contexto, sin objetivo, sin alcance, sin HU)
CORRECTO:   idea → análisis (F1) → objetivo + alcance (proponer-alcance)
            → épica → HU (13·DOC15) → spec (F2) → plan (F4) → construir
```

**Encadenamiento:** los pasos 0–5 alimentan al 6. `F1` (contexto) y `F4.3` (línea base) cubren el análisis; `00-identidad` y la skill `proponer-alcance` cubren objetivo y alcance; `13·DOC15` cubre las HU; `F2`–`F11` cubren el plan y la ejecución.

## F1 · Carga el contexto antes de actuar

Antes de analizar o implementar, revisa la documentación del proyecto (qué existe, qué se decidió, qué está probado). Aplica también **antes** de decir "esto no existe". Si el usuario menciona algo existente, primero búscalo.
Evita: duplicar lo hecho, contradecir reglas previas, re-entender el proyecto desde cero.

```
INCORRECTO: "agregá validación X" → la diseño desde cero
CORRECTO:   reviso docs → ya hay un servicio que hace algo similar → propongo extenderlo
```

## F2 · Sin spec acordada no hay código

Ningún desarrollo, refactor o migración sin una **spec acordada** (prompt de módulo) que lo respalde: alcance, reglas de negocio, datos, pruebas, permisos. Sin spec, el código es opinión del agente.

1. **¿Existe la spec?** (la capa 3 dice dónde). Si no, el agente **no toca código**: ofrece redactar un borrador y aprobarlo primero.
2. **¿El requerimiento ya está?** Si está y falta implementarlo, hazlo donde debía ir. Si no está, **primero actualiza la spec**, luego codifica.

Excepciones (no requieren spec): correcciones triviales, bugfixes que realinean el código a la spec, config local, comandos que el usuario pide, y lectura/investigación.

```
INCORRECTO: "hacé que el módulo permita X" → escribo código directo
CORRECTO:   busco X en la spec → si no está: "no está en la spec; ¿lo agrego a la fase Y
            o es dominio nuevo?" → aprueban → actualizo spec → implemento + pruebas
```

> La capa 3 puede ajustar cuán estricta es, pero viene **activada por defecto**.

## F3 · Plan aprobado = ejecución continua

Aprobado el plan, ejecuta **todos** sus cambios seguidos, sin pedir permiso por cada archivo. Solo pausa si surge algo **no cubierto** por el plan.

```
INCORRECTO: "hago el cambio 1, ¿procedo?" → "el 2, ¿procedo?" → ...
CORRECTO:   ejecuto todo el plan → reporto el resultado
```

## F4 · Todo plan lleva su plan de pruebas y su aprobación explícita

Cada plan se acompaña de las pruebas: qué se prueba, escenarios (feliz, límites, errores, permisos), qué archivo, qué se verifica. Si no amerita prueba (visual/trivial), decláralo: "Sin pruebas — cambio visual".

**Plantillas canónicas** (capa 3): el `plan_trabajo` sigue `plantillas/planes/trabajo.md` (responde las 13 preguntas de `F4.1` sobre la línea base de `F4.3`, con trazabilidad a la HU/CA que cubre la fase — **una sola HU**, `F12.1`); el `plan_pruebas` sigue `plantillas/planes/pruebas.md` (triangulación de casos, trazabilidad CA→caso y alcance quirúrgico de la corrida `F5`). Ambos se guardan en la ruta de la fase (`F12.13`; identificador `F12.6`). La capa 3 puede ajustar las secciones opcionales (equipo/sprint) por proporcionalidad.

**Antes de redactar el plan — verificar la cadena que lo respalda.** Un plan no nace de la nada: se deriva de una **HU con sus criterios de aceptación** (y la **spec del módulo**, `F2`). Si te piden "creá el plan de X" y falta el eslabón que lo respalda (no hay HU/spec, o no se sabe de qué épica/brief sale), **PAUSAR y retroceder** al paso faltante — no inventar el plan. La cadena `brief → épica → HU → spec` es **obligatoria siempre**, sin atajo por tamaño. Encadena con `F0` (cadena obligatoria) y `F2` (sin spec no hay código).

```
INCORRECTO: "creá el plan de trabajo de X" → el agente redacta el plan sin que exista
            HU ni spec que respalde X → planifica sobre supuestos
CORRECTO:   "creá el plan de trabajo de X" → ¿hay HU/spec de X? · no → "no hay HU que
            respalde X; ¿la creamos primero?" · sí → el plan se deriva de esa HU
```

**La aprobación no es un hito abstracto — es una acción operativa obligatoria del agente:**

1. **Redactar** `plan_trabajo` + `plan_pruebas` respondiendo lo que exige F4.1.
2. **PAUSAR** — no tocar código todavía.
3. **Presentar** ambos documentos al usuario con un resumen corto de qué hará.
4. **Esperar OK explícito** del usuario (o iteración de cambios).
5. Solo con el OK, pasar a la implementación (F3).

**Aprobar iniciar una fase** ("arranque con Fase X") NO aprueba el plan detallado. El alcance macro viene del spec del módulo; el plan detallado necesita su **propia aprobación**. Son dos autorizaciones distintas.

```
INCORRECTO: usuario dice "arranque con Fase X" → agente redacta plan + implementa
            todo seguido → reporta al final
CORRECTO:   usuario dice "arranque con Fase X" → agente redacta plan + pruebas →
            PAUSA + presenta → usuario aprueba (o pide cambios) → agente implementa
```

## F4.1 · Preguntas que TODO plan de trabajo debe responder

Un plan de trabajo no es un texto libre: es un contrato con el usuario y con quien continúe el proyecto en el futuro. Debe cerrar toda ambigüedad **antes** de escribir código. Un lector nuevo (otro dev, futuro yo, el usuario en 6 meses) tiene que leer solo el plan y saber exactamente qué se va a hacer, dónde queda visible, cómo se verifica y cómo se revierte — sin abrir código.

Las preguntas siguientes son **genéricas** — aplican a cualquier proyecto que use este estándar. La capa 3 (`.agente/` de cada proyecto) especializa cada pregunta con los artefactos concretos del proyecto (framework de UI, sistema de permisos, herramienta de pruebas, ubicación de la documentación, etc.).

Si una pregunta no aplica al alcance de la fase, se deja el encabezado con "No aplica porque …" — no se omite.

1. **¿Qué es esta fase y a qué módulo pertenece?** Código de fase, slug, fecha apertura, referencia al spec/prompt del módulo.
2. **¿Por qué nace esta fase?** Origen: ¿es funcionalidad nueva, modifica una fase anterior, es híbrido? ¿Qué requerimiento, gap o hallazgo la dispara?
3. **¿Qué carencias documentadas del módulo (`gap-N`, ítems pendientes del cierre de análisis) cierra esta fase?** Puntero explícito al documento de origen.
4. **¿Qué entra en el alcance y qué NO?** Fuera-de-scope explícito para cerrar expectativas.
5. **¿Qué cambia técnicamente?** Un bloque por artefacto: esquema/migraciones, modelos/entidades, servicios/lógica, eventos, componentes/UI, comandos e importadores. Con firma y regla que aplica.
6. **¿Qué rutas/endpoints nuevos se exponen y con qué control de acceso?** (autenticación + permiso + alcance).
7. **¿Dónde queda accesible para el usuario final?** Punto de entrada en la UI: menú, navegación principal, dashboard, link desde otra vista. Si es una entidad contextual que depende de un padre en la ruta, la regla se cumple asegurando que el padre esté en la navegación **y** que su vista exponga el link al hijo. Si la fase no introduce UI navegable, declararlo.
8. **¿Qué permisos / roles nuevos requiere sembrar?** Con la nomenclatura del proyecto.
9. **¿Qué archivos se crean o modifican?** Tabla completa `Archivo | Tipo (Nuevo/Modificar) | Nota`. Debe incluir explícitamente el archivo de navegación cuando aplique el punto 7. **Cada ruta debe estar verificada contra el proyecto real antes de escribir el plan** (F4.3) — nada de `(o donde esté)`, `(o similar)`, `TBD`.
10. **¿Cómo se verifica que quedó bien?** Criterios de aceptación **medibles** (pruebas verdes con conteo, ítem visible con permiso correcto, migración corre y revierte, regresión = 0, verificaciones manuales enumeradas).
11. **¿Cómo se revierte si algo sale mal?** Plan B concreto: rollback de esquema, reversión de commit, backfill inverso, script de emergencia.
12. **¿Toca algo que puede estar en producción y cómo se migra sin bloquear?** Estrategia de migración incremental cuando aplique (aditiva, expand-and-contract, backfill previo, downtime programado).
13. **¿Qué reglas del estándar y del proyecto se aplican explícitamente?** Trazabilidad de decisiones — lista de reglas por su identificador.

```
INCORRECTO: plan que dice "creo el CRUD X" y omite dónde queda accesible al usuario
            → se implementa el CRUD y el usuario tiene que ir a la URL a mano
CORRECTO:   plan que responde las 13 preguntas → nadie ejecuta a medias porque el
            checklist obliga a declarar cada respuesta antes de aprobar
```

> La capa 3 del proyecto ajusta CÓMO se responde cada pregunta (qué archivo es la "navegación", qué framework de permisos usa, dónde vive el plan, etc.), pero las 13 preguntas son obligatorias por defecto.

## F4.2 · Ciclo consolidado de una fase — 11 etapas

Cada fase de trabajo (spec + plan + código + pruebas + docs + commit) sigue **11 etapas ordenadas**. Ninguna se salta ni se reordena. Las etapas identifican **quién actúa** en cada momento y **cuál es el hito** que la cierra. Sirve como marco explícito para no confundir el disparo macro (etapa 2) con la aprobación del plan detallado (etapa 5).

| # | Etapa | Quién actúa | Hito de cierre |
|---|---|---|---|
| 1 | **Declaración macro de la fase** en el spec/prompt del módulo (§Fases). | Agente (redacta) + usuario (aprueba spec en su momento) | Bloque de fase con su **identificador** (`F12.6`), origen, alcance macro, fuera-de-scope |
| 2 | **Disparo / autorización de inicio** de la fase | Usuario ("arranque con X", "siga con Y") | El agente entiende que puede empezar a diseñar el plan detallado |
| 3 | **Diseño del plan detallado** — `plan_trabajo` (responde F4.1) + `plan_pruebas` | Agente | Documentos redactados. NO toca código todavía |
| 4 | **Pausa + presentación** del par de documentos al usuario | Agente | Mensaje al usuario con resumen y punteros a los documentos |
| 5 | **Aprobación del plan detallado** | Usuario | OK explícito → pasa a 6 · pide cambios → vuelve a 3 |
| 6 | **Ejecución continua** del plan aprobado (F3) | Agente | Todo el plan implementado. Pausa solo por descubrimiento genuino no cubierto |
| 7 | **Pruebas** (F5) — corre suite del módulo + suites relacionadas + regresión completa cuando aplique | Agente | Reporta conteo verde. Si falla: diagnostica, corrige, vuelve a correr |
| 8 | **Cierre documental** (F6, F7) — registro de lo implementado, trazabilidad, actualización del spec y de índices/mapas del proyecto | Agente | Documentación completa; trazabilidad spec → código sin faltantes |
| 9 | **Commit único** de la fase | Agente | Mensaje que resume el porqué. **Publicación remota es acción aparte** (etapa 11) |
| 10 | **Reporte al usuario** | Agente | Hash del commit + resumen corto + estado de pruebas + próxima fase natural |
| 11 | **Publicación / despliegue** (opcional) | Usuario autoriza → agente ejecuta | Cambios publicados en remoto / desplegados. Requiere autorización explícita del usuario (acciones con efecto fuera de la máquina local) |

**Aplicabilidad:** las 11 etapas aplican a toda fase con documentación completa. Trabajos triviales que el estándar del proyecto exima de fase (fixes de una línea, correcciones ortográficas) siguen un flujo abreviado, pero solo si el proyecto lo permite explícitamente. Por defecto, todo cambio pasa por las 11 etapas.

**Encadenamiento con el resto del capítulo:** las etapas consolidan F1 (contexto) → F2 (spec) → F4 + F4.1 (plan + preguntas) → F3 (ejecución) → F5 (pruebas) → F6 (persistir) → F7 (trazabilidad), agregando explícitamente las etapas 4-5 (pausa + aprobación del plan detallado), 10 (reporte) y 11 (publicación como acción autorizada aparte).

## F4.3 · Plan sobre línea base verificada — sin supuestos

Un `plan_trabajo` no es un documento de intenciones ni una aproximación — es la **guía de ejecución**. Se construye sobre una **línea base** obtenida del **análisis real del proyecto**: existencia de archivos, rutas exactas, dependencias reales, estado actual del código. **Nunca sobre supuestos.**

**Cinco componentes que TODO plan debe dejar sin ambigüedad para cada intervención declarada:**

1. **QUÉ** — la acción concreta (crear, modificar, eliminar, migrar). No verbos vagos ("ajustar", "revisar", "mejorar").
2. **CÓMO** — el mecanismo técnico específico (agregar campo `X` a tabla `Y`, extender método `foo()` con parámetro `bar`, inyectar servicio `Z` en constructor). Suficiente detalle para que otro dev lo ejecute igual.
3. **DÓNDE** — la ruta exacta del archivo, verificada. Nombre real, no aproximado. Si el archivo no existe todavía, decir "crear en `<ruta exacta>`" — no "en algún lugar de `<carpeta>`".
4. **POR QUÉ** — la justificación: qué gap cierra, qué requerimiento cumple, qué defecto corrige. Encadena con F4.1 preguntas 2, 3.
5. **IMPACTO** — qué otras partes del sistema se ven afectadas: consumidores del código tocado, pruebas que hay que actualizar, riesgos, reversibilidad.

**Prohibido en un `plan_trabajo`:**

- Marcas de incertidumbre visibles: `(o donde esté)`, `(o similar)`, `(revisar)`, `(por confirmar)`, `TBD`, `?`, `~`.
- Aproximaciones de ruta: "en algún archivo de tal carpeta" cuando puedes listar el directorio y saber la ruta exacta.
- Nombres genéricos donde el nombre real existe: "el componente de X", "el servicio de Y", cuando el archivo ya tiene nombre concreto.
- Alcance abierto: "y lo demás que aplique", "más lo necesario".

**Cómo se construye la línea base (obligatorio antes de redactar el plan — etapa 3 del ciclo F4.2):**

1. **Encadena con F1** (cargar contexto antes de actuar). El plan es el segundo paso, no el primero.
2. **Consultar primero el mapa de dependencias del proyecto** (si el proyecto lo mantiene — patrón recomendado; ubicación definida por la capa 3). El mapa consolida qué entidad se relaciona con qué, qué componente consume qué servicio, qué ruta monta qué vista, qué permisos aplican dónde. Es una única lectura contra información persistida y organizada — mucho más rápido que escanear el proyecto entero cada vez. **Si el proyecto no mantiene ese mapa, saltear al punto 3** (descubrimiento sobre el código real).
3. **Solo si el mapa no cubre la duda** (o si aparece contradicción entre mapa y código): usar herramientas de descubrimiento sobre el código real — enumeración de archivos existentes (Glob/`ls`/find), búsqueda de símbolos (Grep/rg), lectura de código relevante (Read), historial (git log/blame). Acotado a la duda concreta; NO Explore comprehensivo global salvo que la fase toque muchas áreas nuevas.
4. **Verificación cruzada** — si el plan menciona "extender el método `foo()`", primero abrir el archivo y verificar que existe y su firma. Si menciona "agregar un ítem a la navegación", primero abrir el archivo de navegación real y ver su estructura.
5. **Documentar el estado inicial** cuando ayude a entender la diferencia: "hoy el archivo tiene `X`, se agrega `Y`" es más útil que "agregar `Y`".
6. **Matriz de dependencias del refactor — OBLIGATORIA cuando el módulo cambia contratos de código existente.** Por cada archivo que va a modificarse, enumerar TODOS los archivos que dependen de él y que romperán al aplicar el cambio. La matriz mínima es:

   | Archivo a refactorizar | Cambio de contrato | Archivos que dependen (rompen) | Ubicación del rompimiento |
   |---|---|---|---|
   | `<archivo A>` | eliminar columna X · renombrar método Y · cambiar la cardinalidad de la relación Z (1:N → N:M) · etc. | `<archivo B> · <archivo C> · …` | `B: lee el atributo X` · `C: carga la relación Y` · `vista D: usa Z.attr` · … |

   Se construye con: buscar los usos de la columna/método/relación que cambia + las cargas de esa relación + los accesos a ese atributo (donde el campo pasa a ser derivado o desaparece) + verificar la firma en las llamadas al método.

   El plan de trabajo (F4.1 §Pregunta 9 · qué archivos) es la unión de {archivos declarados en refactor} ∪ {archivos dependientes DIRECTOS que rompen}. Nunca solo el conjunto A — siempre A ∪ B. Si un archivo dependiente NO se puede refactorizar en esta fase (por volumen, por scope, por decisión), se declara EXPLÍCITAMENTE en §Fuera-de-scope con nota de "queda para Fase X" — nunca se ignora silenciosamente.

   **No encadenar dependencias transitivas.** Si A depende de B, ajustar B es necesario (o diferirlo explícitamente). Pero **no seguir la cadena B→C→D→…** dentro del alcance de la misma fase — cada eslabón adicional expande la fase infinitamente. Cuando un archivo dependiente se difiere a otra fase, **todos los archivos que dependen a su vez de él (tests, consumidores) se difieren también a la misma fase** — no se refactorizan a medias.

   **Regla derivada — coherencia de tests refactorizados:** un test refactorizado en una fase solo puede depender de código refactorizado en esa misma fase (o del código base ya estable). Si un test testea un archivo B que se difiere a Fase futura, el test también se difiere a esa fase — jamás se refactoriza el test en la fase A esperando que quede verde con un B roto. Verificación obligatoria antes de aprobar el plan: por cada test listado como "refactorizado y verde en Fase X", cruzar sus dependencias contra §Fuera-de-scope; si toca algo diferido, moverlo también a diferido.

   **Anti-patrón rechazado:** enumerar solo los consumidores del legacy que se va a dropear pero omitir las dependencias del refactor propuesto. Ambas fuentes de rompimiento importan.

   **Anti-patrón rechazado (dependencia transitiva):** refactorizar un test T que depende de un servicio S diferido a otra fase, esperando que T quede verde en esta fase. T y S se cierran juntos — se refactorizan en la misma fase o se difieren juntos.

**Consecuencia operativa:** si al redactar el plan hay algo que no puedes verificar (porque requiere decisión del usuario, porque el módulo no existe todavía, porque hay opciones legítimas), **no lo escribas como suposición** — decláralo como pregunta abierta al usuario y espera su decisión. Un plan con partes sin verificar no está listo para aprobar.

**Proporcionalidad del análisis** — el análisis es proporcional al alcance y riesgo de la fase, no siempre exhaustivo:
- **Fase pequeña / self-contained** (tabla nueva, servicio nuevo, refactor local): línea base breve + matriz de dependencias resumida. Basta consultar el mapa + verificaciones puntuales sobre 2-3 archivos.
- **Fase grande / refactor global / que toca múltiples áreas del sistema**: línea base exhaustiva justificada. Explore comprehensivo apropiado si el mapa no cubre + hallazgos previos indican riesgo.
- **Signal para escalar el análisis:** número de archivos que rompen al aplicar el refactor (matriz de dependencias). **≤ 5:** análisis mínimo (mapa + verificación puntual). **6–15:** análisis medio — mapa + verificación dirigida de cada archivo que rompe. **> 15:** análisis exhaustivo justificado.

**Filtrar decisiones antes de escalar al usuario** — no todo lo que aparece en el análisis debe ir al usuario como decisión pendiente. Reglas de filtro:
- **Cerrar con criterio profesional (sin escalar):** decisiones puramente técnicas (nomenclatura de rutas, orden de migración, cascadas de borrado en FK, cardinalidad de una relación (1:N vs N:M), código idiomático del framework, etc.). El agente decide y lo declara en el plan.
- **Escalar al usuario:** decisiones que impactan UX visible (cómo se muestra algo en la vista), contrato de API (cambio breaking o retrocompat), breaking changes de datos (drops, renames), alcance de la fase (qué difiere y qué no), o cambios que introducen deuda estructural. El usuario decide.
- **Anti-patrón:** listar 10 decisiones al usuario cuando 7 son técnicas triviales. Sobrecarga cognitiva innecesaria + retrasa la fase.

```
INCORRECTO: "el archivo de navegación de la carpeta de vistas (o donde esté)"
            → el plan admite explícitamente que no verificó la ruta real
CORRECTO:   listar la carpeta de vistas → localizar el archivo de navegación → leerlo
            → plan dice "<ruta real del archivo de navegación>, sección <X>: agregar
            el ítem con la verificación de permiso <permiso.ver>"

INCORRECTO: refactor de una entidad (columna `estado` de valor fijo → referencia a
            catálogo) enumera solo el modelo de la entidad como archivo tocado
            → durante la ejecución se descubre que su servicio referencia `estado`
            (la columna vieja) en 3 métodos → pausa forzada + ampliación a mitad de camino
CORRECTO:   antes del plan, matriz de dependencias: buscar los usos de `estado` en el
            código → el servicio de la entidad coincide en 3 líneas → plan §Archivos
            incluye desde el inicio: Modelo (Modificar) + Servicio (Modificar)
```

**Encadenamiento con otras reglas:**

- **F1** — cargar contexto es prerequisito del plan; F4.3 lo hace explícito para el `plan_trabajo`.
- **F4.1 pregunta 9** — el listado de archivos es verificado, no aproximado.
- **F4.2 etapa 3** — "diseño del plan detallado" implica análisis previo del proyecto para construir la línea base.
- La capa 3 del proyecto puede endurecer con reglas como "línea base inquebrantable del prompt del módulo" y equivalentes.

## F4.4 · `plan_trabajo` se deriva de los CA de la HU — nunca de la proactividad

El `plan_trabajo.md` de toda fase se construye a partir de los **Criterios de Aceptación** aprobados de la HU madre — específicamente, los CA etiquetados para esa fase (`[XX]` cuando aplique). El plan NO se construye a partir de:

- Lo que al agente le parece que "también debería ir".
- Proactividad sobre "aprovechamos y arreglamos también Y".
- Lecturas del código que revelan "código legacy que podríamos limpiar de paso".

**Trazabilidad obligatoria — cada intervención rastrea a un CA:**

Toda intervención listada en el plan (código · migración · seed · vista · test) debe tener **rastro explícito** al CA que la justifica. La `F4.1 · pregunta 9` (qué archivos se tocan) se combina con la `pregunta 3` (qué gap/CA cierra) en una tabla o listado del plan donde cada línea muestre `intervención → CA`.

**Ítem sin CA asociado — dos rutas y solo dos:**

1. **Soporte técnico obligatorio:** limpiar código legacy que impide el nuevo comportamiento · crear helper que evita duplicar código · agregar la columna sin la cual el CA es imposible. **Declararlo** en el §Alcance como "soporte de CA-X" y **explicar** por qué es indispensable para cumplir ese CA. Si sin ese ítem el CA no funciona, es soporte legítimo.
2. **Proactividad:** todo lo demás. **Retirarlo del plan** y proponerlo como fase separada con su propia HU/CA (F4.5). No se agrega "por conveniencia" al plan actual.

**Anti-patrones rechazados:**

- Escribir el plan **antes** de tener los CA aprobados de la HU.
- Empezar a tocar código antes de que el plan esté persistido como archivo Y aprobado explícitamente por el usuario (`F4` requiere la aprobación previa).
- Agregar en §Alcance "También aprovechamos para X" cuando X no es CA de esta fase.
- Escribir el plan "según lo que la IA infirió" cuando el usuario dio N CA concretos — el plan debe ceñirse a esos N.

**Encadenamiento:**
- **F12.9** — «una fase puede corresponder directamente a un CA»; F4.4 desarrolla que el `plan_trabajo` se deriva de esos CA de la HU.
- **F4.1** — la pregunta 3 (qué gap cierra) y la pregunta 9 (qué archivos se tocan) se cruzan en una tabla ítem→CA.
- **F4.2 · etapa 3** — el diseño del plan es DERIVADO de los CA aprobados, no invención.
- **F4.5** — lo que "convendría" agregar pero no está en CA sigue la ruta de propuesta (parar + mostrar + esperar), no se cuela al plan.
- **F9** — una vez presentado y aprobado el plan derivado de CA, se ejecuta completo; no se re-piden opciones sobre CA ya aprobados.
- **C17** — la confirmación previa de entendimiento asegura que los CA reflejen el pedido REAL antes de derivar el plan.

## F4.5 · Ejecutar LITERAL los CA · descubrimientos fuera de CA se PROPONEN, no se actúan

**Dos partes indivisibles.**

**(1) Ejecución literal de los CA.** La implementación debe hacer LITERAL lo que dicen los CA aprobados — ni más, ni menos, ni "más seguro por si acaso", ni "de paso arreglamos". La redacción de un CA es la especificación funcional; el agente no la interpreta libremente ni la endurece unilateralmente.

**(2) Descubrimientos fuera de CA → proponer, no actuar.** Si durante el análisis, la construcción del plan, o la ejecución el agente detecta algo que "convendría" agregar (defensa en profundidad · limpieza · validación extra · UX complementaria · refactor colateral · guard adicional), la única ruta válida es:

1. **PARAR** de tocar código, plan o análisis.
2. **MOSTRAR** al usuario la propuesta con: qué observó · por qué considera que aportaría · impacto (líneas de código · tests nuevos · migración · etc.) · qué CA quedaría sin cambios y qué CA se sumaría (si aplica).
3. **ESPERAR** decisión del usuario:
   - **"Sí, agrégalo"** → o bien se agrega como CA nuevo a la HU antes de continuar (recomendado si es funcional), o bien se declara como soporte técnico obligatorio de un CA (F4.4) con justificación explícita.
   - **"No"** → se descarta y NO se menciona más.
   - **"Después"** → se anota como brecha (en el prompt del módulo si el proyecto lo mantiene) y se retoma en fase futura.

**Anti-patrones rechazados:**

- Agregar un guard server-side cuando el CA solo pide "botón oculto en UI" → NO. El CA es la especificación; endurecerlo es rewrite unilateral.
- Ante una pregunta del usuario ("¿de dónde sale X?") · interpretarla como corrección y **editar el plan/código** para "corregir". La pregunta pide EXPLICACIÓN, no acción. Se responde y se espera instrucción explícita.
- "Aprovechamos y limpiamos código legacy" cuando la limpieza no está en CA → NO. Se propone como fase separada.
- "El CA dice X pero técnicamente conviene X + Y" → NO se implementa Y. Se propone Y al usuario.
- "Es defensa en profundidad, es buena práctica" → aunque lo sea, si no está en CA se propone, no se actúa.

**Aplica a los tres momentos donde el agente históricamente se desvía:**

1. **Al construir el `plan_trabajo`** — cada ítem debe rastrear a un CA (F4.4); un ítem "conviene técnicamente" que no viene de CA se propone antes de agregarlo al plan.
2. **Al escribir código** — la implementación debe cumplir el CA sin agregar guards, validaciones o efectos que no estén en el CA.
3. **Al responder a una pregunta del usuario** — la pregunta se responde, no se convierte en autorización para editar/corregir/refactorizar (`C3` · quédate en tu tarea).

**Encadenamiento:**
- **F4.4** — proveedor del "plan deriva de CA"; F4.5 añade que **descubrimientos** fuera de CA también se proponen (no solo se filtran del plan · se pausan y consultan).
- **F12.9 / F12.10** — «una fase puede corresponder a un CA» y «no crear una fase solo por nomenclatura»; F4.5 asegura que la ejecución sea **literal** a esos CA.
- **C17** — la confirmación previa y F4.5 se refuerzan: C17 dice "no ejecutar sin OK explícito"; F4.5 dice "los descubrimientos no son excepción a C17".
- **C3** — preguntas del usuario NO son autorización de acción; una pregunta se responde y se espera instrucción.
- **F8** — solo se tocan archivos declarados en el plan aprobado; los descubrimientos activan la vía "PAUSAR + reportar + esperar OK" para ampliar el plan.

## F5 · Ejecuta las pruebas antes de dar por terminado

Las pruebas se **corren**, no solo se escriben. La tarea no está lista hasta que pasan.
Reporta el conteo ("9/9 verdes"). Si fallan: diagnostica, corrige, vuelve a correr. Nunca las silencies para que pasen (`00` · N3).

**Alcance de la corrida — solo las suites que la fase toca directamente.** No arrastrar la suite completa del proyecto ni suites de fases anteriores no relacionadas — cada test extra consume tiempo y memoria sin aportar señal útil. Correr:

1. **La suite del módulo nuevo/refactorizado** (obligatoria — es el objeto de la fase).
2. **Las suites que la fase refactorizó explícitamente** (declaradas en el `plan_trabajo`).
3. **Suites que dependen directamente de los archivos tocados**, según la matriz de dependencias del refactor (F4.3): si la fase modificó una entidad que otra suite usa (creando registros de esa entidad o accediendo a sus relaciones), esa suite se corre.

NO correr por defecto:
- La suite completa del proyecto ("por si acaso").
- Suites de módulos que no aparecen en la matriz de dependencias del refactor.
- Suites que solo comparten servicios de infraestructura (base de datos, autenticación) sin tocar el código refactorizado.

**Anti-patrón:** correr toda la suite de pruebas a secas al terminar la fase → ejecuta cientos de tests, tarda varios minutos, sube el consumo de memoria y produce ruido de rojos que ya existían pre-fase. Reemplazar por corrida quirúrgica de las suites del punto 1-3.

Si un chequeo global es realmente necesario (por ejemplo, antes de cortar release), se declara EXPLÍCITAMENTE como "regresión total pre-release" — no como parte del flujo normal de fase.

```
INCORRECTO: implementar + escribir pruebas + "listo"
CORRECTO:   implementar + escribir + EJECUTAR + "Verdes 4/4"
```

## F6 · Persiste el trabajo y las decisiones

El chat se pierde; los archivos quedan. Al cerrar, guarda en documentación versionada: qué se planeó, qué se probó, qué quedó, y **las decisiones no obvias con su porqué** (detalle en `13`).

## F7 · Verifica trazabilidad spec → implementación

Antes de cerrar, revisa ítem por ítem que cada afirmación técnica de la spec esté en el código, el esquema, las pruebas y los docs. No cierres con faltantes sin justificar (formato en `13` · DOC3).

```
INCORRECTO: "pruebas verdes → cierro"
CORRECTO:   "pruebas verdes + trazabilidad sin faltantes → cierro"
```

## F8 · Solo se tocan archivos declarados en el plan aprobado — descubrimiento pausa

El `plan_trabajo` aprobado (F4 §5, F4.1 pregunta 9) es un **contrato**, no una guía flexible. El agente **solo edita los archivos declarados** en la tabla de archivos del plan. Descubrir en mitad de la ejecución que otro archivo también necesita cambios es una señal legítima — pero **detiene la ejecución**, no la extiende.

**Protocolo obligatorio al descubrir un archivo fuera del plan:**

1. **PAUSAR** — no editar ese archivo.
2. **Reportar el descubrimiento** al usuario: qué archivo, qué hallazgo lo hace necesario, qué impacto tiene ignorarlo.
3. **Proponer la ampliación del plan** — agregar el archivo a la tabla F4.1 pregunta 9 y actualizar §Alcance / §Fuera-de-scope si cambia.
4. **Esperar OK explícito** del usuario para ampliar.
5. Solo con el OK, retomar la ejecución con el plan ampliado.

Este comportamiento aplica también cuando el archivo "obviamente" necesita el cambio ("es evidente que también hay que tocar Y para que X funcione"). La obviedad no autoriza — la aprobación del plan sí. Si el análisis previo (F4.3) fue insuficiente, la ampliación es la corrección — no un atajo silencioso.

**El plan de trabajo es contrato, no guía flexible.** Ejecutar cambios fuera del plan es la ruta más rápida a que el usuario pierda visibilidad de lo que el agente realmente tocó.

```
INCORRECTO: durante la ejecución de la fase, el agente descubre que también hay que
            editar el archivo Y (dependencia transitiva) → lo edita en el mismo commit
            "porque era necesario" → el usuario descubre después que se cambió algo
            que no estaba en el plan
CORRECTO:   descubre Y → PAUSA + reporta + propone ampliar el plan → usuario aprueba
            (o rechaza y difiere Y a otra fase) → sigue con el plan actualizado
```

**Encadenamiento:** F4.3 (matriz de dependencias antes de aprobar) es la primera defensa contra este escenario — reduce los descubrimientos. F8 es la segunda defensa — cuando el descubrimiento ocurre a pesar del análisis previo, el agente no lo procesa en silencio.

## F9 · Plan aprobado se ejecuta completo — sin subdividir post-aprobación

Cuando el usuario aprueba explícitamente un plan (con "arranque", "hágale", "ok con eso", "sí" o equivalente), ese plan se ejecuta **completo** de principio a fin **sin**:

- Volver a pedir confirmación por sub-decisiones que ya cabían en el plan aprobado.
- Subdividir arbitrariamente en sub-fases pequeñas después de aprobado (excepto si el usuario lo pide explícitamente).
- Ofrecer nuevas opciones sobre detalles que ya estaban implícitos o resueltos con criterio profesional.
- Entregar "a medias" con la excusa del volumen — la solución se entrega funcional, no en pedacitos que dejan al usuario decidiendo cada micro-paso.

**Motivo:** el usuario aprobó porque confía en que la ejecución es coherente con lo pactado. Cada nueva pregunta después de "aprobado" rompe esa confianza y transfiere el peso decisional que YA estaba resuelto.

**Momento correcto para dividir en subfases:** durante el diseño del plan (antes de aprobar) — si el agente evalúa profesionalmente que el volumen amerita subdivisión, la propone en el plan como XX.1/XX.2/XX.3 con criterios de aceptación por subfase. El usuario aprueba el plan **con** la subdivisión ya dentro. Luego cada subfase se ejecuta completa cuando llega su turno.

**Qué SÍ interrumpe legítimamente el flujo:**

- **Descubrimiento genuino** durante la ejecución que NO estaba anticipado en el plan y **requiere** decisión del usuario (bug de negocio no acordado, hallazgo que contradice el plan, dependencia nueva).
- **Hallazgo bloqueante** que impide continuar (dependencia rota, credencial faltante).

Ambos se reportan como "hallazgo derivado", NO como "opción a elegir". Ver también `F8` (archivos fuera del plan) — mismo espíritu: la pausa es la excepción, no el modo de operación.

```
INCORRECTO: usuario aprueba el plan → agente lo divide en 4 sub-fases y vuelve a
            pedir 4 aprobaciones "para hacerlo manejable"
CORRECTO:   si el volumen era problema, se propone la subdivisión ANTES de aprobar;
            después, ejecución continua
```

**Encadenamiento:** `F3` (plan aprobado = ejecución continua) es el enunciado base; `F8` protege archivos fuera del plan; `F9` protege el compromiso de completud post-aprobación.

## F10 · Producción no bloquea el desarrollo — se planifica migración incremental adecuada

Cuando una decisión de diseño requiere modificar algo que **está o puede estar en producción**, el agente **no posterga el trabajo** ni bloquea la fase con la pregunta "¿está en prod?". Asume por defecto **"probablemente sí está en producción"** y **planifica migración incremental adecuada** dentro del mismo plan de trabajo.

**Migración incremental adecuada, según el tipo de cambio:**

- **Cambio aditivo** (agregar columna, agregar tabla): migración nueva. Backfill dentro del script si aplica. Nada destructivo.
- **Rename** (columna, tabla, artefacto persistente): migración nueva reversible. NO editar la migración original de una fase cerrada.
- **Drop de columna/tabla con datos**: **avisar al usuario del riesgo específico** antes de aplicar (posible pérdida de datos). Si aprueba, migración con `down()` que reconstruye el tipo original.
- **Cambio de tipo o restricción** (NOT NULL → NULL, INT → BIGINT, ampliar enum, etc.): **avisar del riesgo específico** (truncamiento, incompatibilidad con datos existentes). Si aprueba, estrategia zero-downtime documentada.
- **Refactor grande** que toca múltiples tablas en producción: dividir en fases pequeñas ordenadas por seguridad — aditivas primero, destructivas al final con backfill previo.

**Qué NO es válido:**

- Preguntar "¿está en producción?" para decidir si hacer o no el trabajo (usar la pregunta solo para elegir estrategia: editar migración original vs. crear migración nueva).
- Postergar una fase "porque está en producción" sin haber propuesto migración incremental.
- Editar migración de fase cerrada asumiendo "no está en producción" sin confirmarlo explícitamente con el usuario.

**Qué SÍ es válido:**

- Preguntar por prod solo para **elegir estrategia** (editar original vs. nueva). Ambas rutas producen el resultado correcto.
- Avisar del **riesgo específico** cuando el cambio incluye drop / tipo / restricción con datos vivos.

**Motivo:** el sistema es vivo y evoluciona. Preguntar "¿está en producción?" antes de cada cambio y postergar por miedo convierte el desarrollo en parálisis. Producción se mejora con migración incremental disciplinada — no se congela.

```
INCORRECTO: "antes de arrancar la fase necesito confirmar si X está en producción" →
            fase bloqueada esperando información que se puede asumir
CORRECTO:   plan de trabajo asume "probablemente está en prod" + declara la estrategia
            de migración (aditiva / rename / drop con aviso / tipo con aviso)
```

**Encadenamiento:** no modera `00 N4` (proteger datos reales) — este sigue vigente para operaciones directas sobre BD. Complementa `02 F4.1` pregunta 12 ("¿toca algo que puede estar en producción?") con la filosofía operativa.

## F11 · Una fase solo modifica código de su propio módulo — cross-módulo prohibido

Una fase pertenece a **un** módulo **y** a **una sola HU** (`F12.1`) — las dos condiciones aplican a la vez. Si una HU abarca varios módulos, se parte en **una fase por módulo**, todas bajo esa misma HU. El módulo se declara al abrir la fase (ver `DOC12` — ORIGEN). Todos los archivos que la fase modifica deben pertenecer a ese módulo. Cross-módulo está prohibido por defecto.

**Si al diseñar la fase (etapa 3 del ciclo `F4.2`) aparece que también hay que modificar archivos de OTROS módulos:**

1. **Descomponer:** crear una fase propia por cada módulo afectado.
2. **Documentar el diferimiento:** listar en el spec del módulo actual los artefactos que quedan pendientes por-módulo (§Fuera-de-scope + tabla "Módulos que requieren fase propia").
3. **NO agrupar** todos los cambios ajenos en una única "fase transversal de reparación". Eso destruye la trazabilidad por módulo.

**Excepciones legítimas — infraestructura compartida que TODA fase puede tocar:**

- Rutas globales del framework (agregar middleware al grupo de la fase).
- Registro de servicios / alias / bindings globales, cuando el módulo lo requiera.
- Mapas y catálogos centrales del proyecto (por ejemplo el mapa de dependencias vivo del `DOC9`, la descripción de módulos declarada por la capa 3).
- Layouts globales SOLO si el cambio es necesario para el módulo de la fase.

**Si durante la ejecución aparece un archivo de otro módulo que rompería por la fase actual:** pausar (`F8` aplica), notificar al usuario, y proponer:

- **Opción A** — documentar el break como esperado en el spec del módulo dueño + agendar fase propia.
- **Opción B** — hacer el cambio mínimo indispensable con nota explícita en el commit + registro en el spec del dueño.

La decisión es del usuario, no del agente.

**Trabajo adelantado que "se metió" en una fase por error:** si el usuario lo aprueba post-hoc, se mantiene y se documenta con nota explícita en el spec del módulo dueño (mecanismo bidireccional de referencias entre specs · ver `13 DOC7`) y NO se documenta como "cerrado" — cada módulo debe tener su fase formal cuando toque.

```
INCORRECTO: fase de módulo A arranca tocando 20 archivos de módulos B, C, D "porque
            el refactor es transversal" → destruye la trazabilidad por módulo
CORRECTO:   fase A toca solo archivos de A; los cambios necesarios en B, C, D se
            agendan como fases propias (o se difieren en §Fuera-de-scope)
```

**Encadenamiento:** `01 C3` (alcance quirúrgico) es el principio base; `F11` lo eleva a nivel de fase completa. `F8` (archivos fuera del plan) es la línea de defensa dentro de la fase; `F11` es la línea de defensa entre fases y módulos.

---




## F12 · Relación y nomenclatura de fases

Regla completa (fuente única): [`02-flujo-de-trabajo/F12/base.md`](02-flujo-de-trabajo/F12/base.md). Molde para crear una fase: `plantillas/fase.md`.

## F13 · Estructura base obligatoria del proyecto   ·   `[GATE DE ARRANQUE · PRECONDICIÓN]`

**Corre primero**, antes de `F1` y de todo el flujo (el ID `F13` es solo catálogo, no orden). Regla completa (fuente única): [`02-flujo-de-trabajo/F13/base.md`](02-flujo-de-trabajo/F13/base.md). Estructura (anexo): [`02-flujo-de-trabajo/F13/estructura-base.md`](02-flujo-de-trabajo/F13/estructura-base.md). Gate: existe la carpeta `proyectos/`.

---

**Secuencia macro (0–6):** en `F0`. **Secuencia del plan hacia abajo:** contexto (F1) → spec (F2) → **línea base verificada del proyecto (F4.3)** → plan + pruebas (F4) responde las 13 preguntas (F4.1) **derivado de los CA de la HU (F4.4)** → **pausa + aprobación explícita (F4 §2-5)** → ejecutar (F3) — **literal a los CA · descubrimientos se proponen (F4.5)** · **solo archivos del plan (F8)** · **completo sin subdividir (F9)** · **solo el propio módulo (F11)** · **con migración incremental cuando toca prod (F10)** → correr pruebas (F5) → persistir (F6) → trazabilidad (F7) → cerrar.

**Fases:** identificador (`F12.6`) y relación con la HU (`F12.1`) en `F12`.

Consolidado como **ciclo de 11 etapas en F4.2** — usar esa tabla como referencia operativa canónica del flujo completo de una fase.