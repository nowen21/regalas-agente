# 02 · Flujo de trabajo  ·  `[CAPA 2]`

Cómo trabaja el agente: de la solicitud a la tarea terminada. La capa 3 define dónde viven los documentos y cómo se corren las pruebas.

---

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
| 1 | **Declaración macro de la fase** en el spec/prompt del módulo (§Fases). | Agente (redacta) + usuario (aprueba spec en su momento) | Bloque `### Fase XX` con origen, alcance macro, fuera-de-scope |
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

---

**Secuencia:** contexto (F1) → spec (F2) → **línea base verificada del proyecto (F4.3)** → plan + pruebas (F4) responde las 13 preguntas (F4.1) → **pausa + aprobación explícita (F4 §2-5)** → ejecutar (F3) → correr pruebas (F5) → persistir (F6) → trazabilidad (F7) → cerrar.

Consolidado como **ciclo de 11 etapas en F4.2** — usar esa tabla como referencia operativa canónica del flujo completo de una fase.
