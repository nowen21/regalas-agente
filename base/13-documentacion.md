# 13 · Documentación  ·  `[CAPA 2]`

El chat se pierde y el contexto se comprime; los archivos quedan. Documentar es parte del entregable. La capa 3 declara ubicación, nombres y estructura.

---

## DOC1 · Persiste el trabajo de cada unidad completada

Al cerrar, guarda en documentación versionada: **qué se planeó** (el plan aprobado), **qué se probó** (escenarios + verificaciones manuales que el entorno automático no cubre — [`08·T4`](08-pruebas.md#t4--protege-los-datos-reales-al-probar)), **qué quedó** (cómo usarlo, puntos de entrada, enlaces al código). El chat no sustituye los archivos.

```
INCORRECTO: implementar, mostrar todo en el chat y cerrar
CORRECTO:   implementar + persistir plan, pruebas y resultado
```

## DOC2 · Documenta las decisiones no obvias y su porqué

**Documenta:** reglas de negocio, decisiones de diseño que no se ven en el código (por qué X y no Y), convenciones del módulo, dónde se aplica cada regla (enlace a archivo y línea).
**No documentes:** cómo funciona el código línea por línea, ni lo obvio de leer el archivo.

```
INCORRECTO: comentar el porqué en el código y confiar en que lo relean
CORRECTO:   registrar la decisión y su motivo en la doc, enlazando al código
```

## DOC3 · Verifica la trazabilidad spec → implementación antes de cerrar

Revisa ítem por ítem que cada afirmación técnica de la spec ([`02·F2`](02-flujo-de-trabajo/reglas/F2-sin-spec-acordada-no-hay-codigo.md)) esté en el código, el esquema, las pruebas y los docs. No cierres con faltantes sin justificar.

Formato: una tabla persistida en el documento de resultado, una fila por afirmación:

| Ítem de la spec | Categoría | Ubicación esperada | Estado | Evidencia |
|---|---|---|---|---|
| (frase de la spec) | (esquema/modelo/servicio/vista/prueba/permiso/ruta/doc) | (archivo real) | ✅ / ❌ / N/A / parcial | (enlace o prueba) |

Faltante, parcial y N/A llevan justificación. Si al revisar una unidad cerrada aparece un faltante, se corrige **en su lugar** y se actualiza la tabla.

```
INCORRECTO: "pruebas verdes → cierro"
CORRECTO:   "pruebas verdes + tabla de trazabilidad sin faltantes → cierro"
```

## DOC4 · Documenta lo que producción necesita

Los pasos de despliegue (cambios de esquema, datos base, permisos, comandos post-deploy) se documentan **auto-suficientes y ejecutables**. Quien despliega lo hace leyendo el entregable, sin volver a mirar el código.

## DOC5 · Registrar señales (memoria) — *opt-in*

Guardar las **señales** de alto valor que **no se pueden recuperar del código**. Una señal = **what / why / where / learned** + un **tipo** (`decisión`, `error-resuelto`, `patrón`, `aprendizaje`, `alternativa-descartada`, `supuesto`, `restricción`, `pregunta-abierta`, `gotcha`, `deuda-técnica`) + un **scope** (a quién sirve: proyecto o toda la organización).

**Dónde se guardan (backend — lo elige la capa 3, uno solo):**
- **Archivo** `documentacion/senales.md` (versionado, simple) — plantilla `plantillas/senales.md`. Para pocas señales.
- **Base central buscable** `memoria/` (SQLite+FTS5, con `scope`, buscable y compartida entre proyectos) — se opera con la skill `usar-memoria`; es data local, no se versiona. Para muchas señales.

Guardan la **misma** señal; se elige por volumen (ver [`notas/memoria-por-senales.md`](../notas/memoria-por-senales.md)). **Opt-in**: se activa cuando la capa 3 declara el backend (el `CLAUDE.md` del proyecto).

- **No borrar** una señal revertida: marcarla `reemplazada` y enlazar la nueva (rastro, como `## Decisiones` clásico).
- **Verificar antes de confiar:** una señal vieja puede estar obsoleta ([`01·C2`](01-conducta.md#c2--no-inventes-verifica)).
- Es la defensa contra "la compactación mata decisiones": la señal vive en la memoria, no en el chat.

```
INCORRECTO: la decisión "elegimos X y no Y porque Z" queda solo en el chat → se pierde al compactar
CORRECTO:   se registra como señal (decisión) en la memoria con what/why/where/learned
```

## DOC6 · Retro-documentar módulos existentes sin spec

Cuando el proyecto tiene módulos productivos que nunca tuvieron spec, o cuya spec está desactualizada (más vieja que refactors recientes al código), la retrodocumentación es una **unidad de trabajo formal** — no un comentario apurado.

Procedimiento canónico (6 pasos):

1. **Exploración con lectura amplia** — mapear el módulo real: archivos, tablas/estructuras, relaciones, dependencias con otros módulos.
2. **Persistir el análisis** — archivo `analisis/<modulo>-<fecha>-<tema>.md` con lo que se encontró, con enlaces a los archivos concretos. Es la fotografía del estado actual.
3. **Crear el prompt vivo base** — spec de referencia del módulo con las 13 secciones canónicas de la plantilla `_base_modulo.md`. Marcar como *retro-doc inicial* — se completará al primer audit profundo.
4. **Preguntas abiertas al usuario** — todo dato de negocio que el código no dice se anota como pregunta en la spec (§Supuestos, dependencias y preguntas abiertas). No inventar.
5. **Gaps y divergencias** — lo que hoy hace el código y no debería (deuda técnica) o lo que debería hacer y no hace, se lista en §Qué falta como `[gap-N]` numerados.
6. **Registrar el módulo** — en el índice de dominio del proyecto (`dominio.md` o equivalente) con puntero al prompt vivo recién creado.

El módulo queda documentado en estado *provisional* — su cierre real ocurre en el primer audit profundo (fase dedicada) cuando el prompt se completa según la plantilla canónica.

```
INCORRECTO: encontrar un módulo sin spec y decir "asumo que hace X" en la próxima fase
CORRECTO:   crear la retro-doc formal antes de tocarlo · el análisis persistido queda como fotografía del punto de partida
```

## DOC7 · Referencias entre docs con historial cruzado bidireccional

Cuando el prompt de un módulo A menciona al prompt de otro módulo B, la referencia lleva **contexto**, no un mero puntero:

**En A**, la mención declara:
- **Por qué** se referencia (qué del módulo B consume A · qué dependencia funcional o semántica).
- **Mejoras aplicadas a B desde A** — si al trabajar A se descubrió algo que mejora a B (una columna, una convención, un dato de negocio), listarlo aquí como "mejora aplicada hacia B" con enlace a la sección de B donde quedó.

**En B**, en su sección `## Historial cruzado — mejoras recibidas desde otros módulos`, se registra:
- Fecha, módulo origen (A), qué cambió (columna añadida, sección actualizada, decisión adoptada), enlace a la fase o commit que lo aplicó.

Bidireccional obligatorio: si A menciona una mejora hacia B, B debe reflejar la recepción. Así el conocimiento no se queda atrapado en un solo lado.

Descartar como "referencia cruzada" formal las **menciones de paso** ("como se hizo en el módulo X algo similar" — es analogía, no dependencia). La regla aplica cuando hay **consumo funcional real** o **decisión compartida**.

```
INCORRECTO: prompt A menciona "ver módulo B para más" sin decir por qué ni actualizar B
CORRECTO:   A dice "consume la columna X de B por Y motivo · aplicó la mejora Z hacia B" + B registra en §Historial cruzado
```

## DOC8 · Cierre de análisis con tabla de trazabilidad

Todo análisis persistido bajo `analisis/<...>.md` (DOC6 paso 2 · exploraciones · auditorías) genera al terminar un **archivo de cierre** que consolida lo que quedó:

- **Ruta canónica:** `analisis/<modulo>-YYYY-MM-DD-cierre.md`. Plantilla: `plantillas/cierre-analisis.md`.
- **Contenido mínimo:** tabla de mapeo con una fila por pregunta abierta o hallazgo detectado durante el análisis:

| Pregunta / hallazgo | Decisión tomada | Estado | Gap generado (si aplica) |
|---|---|---|---|
| (frase del hallazgo o pregunta original) | (respuesta del usuario o decisión de diseño) | resuelta / diferida / descartada | `[gap-N]` con enlace a §Qué falta del prompt vivo |

- **Puntero desde el análisis original** — el archivo del análisis inicial pasa a ser *fotografía inmutable* con un banner al inicio: `> Cerrado en <ruta-del-cierre> — consultar allí para el estado vigente de cada decisión`.
- **Referencia desde el prompt vivo** — la sección `## Historial de análisis` del prompt lista `YYYY-MM-DD · <tema> · <ruta-al-cierre>` en orden cronológico.

Así queda un rastro consultable de cada análisis: se abrió, se preguntó, se decidió, se cerró — no se pierde en el chat ni en un archivo huérfano.

```
INCORRECTO: análisis abre 15 preguntas al usuario, el usuario responde en chat, se cierra sin dejar rastro persistido
CORRECTO:   análisis → chat con respuestas → archivo de cierre con tabla + puntero desde el análisis original + registro en §Historial del prompt vivo
```

## DOC9 · Mapa de dependencias vivo — consultar antes, actualizar después

Existe un **artefacto vivo** por proyecto (ruta canónica declarada en la capa 3 · ej. `.agente/mapa-dependencias.md`) que consolida el conocimiento del sistema: modelos → tablas → columnas, componentes → qué consumen, rutas → destinos, middleware, permisos, traits, layouts, pruebas. Plantilla: `plantillas/mapa-dependencias.md`.

**Es la fuente autoritativa consultable** de "cómo está armado esto hoy". No versionado si es local al desarrollador; declarado como pública si el equipo lo comparte.

**Al planificar cualquier unidad de trabajo** (etapa de análisis de un plan · `02` F4.3): consultar primero el mapa. Solo hacer exploración amplia si el mapa NO cubre la duda o si aparece contradicción con el código real (indicador de que el mapa envejeció). Orden operativo:

1. Leer el mapa.
2. Si duda puntual → verificación con búsqueda + lectura del archivo concreto.
3. Si contradicción o cobertura insuficiente → exploración acotada (no global).

**Al cerrar la unidad** (bloque de cierre documental · `02` F6): actualizar el mapa en el mismo commit. Sin excepción. Modelo nuevo → sección modelos + fillable + relaciones + consumidores. Migración nueva → tabla + índices + FKs. Refactor grande → actualizar consumidores. El mapa es un compromiso vivo, no una foto de una fecha.

```
INCORRECTO: cerrar una unidad sin actualizar el mapa · siguiente unidad relee 15 archivos que ya estaban mapeados
CORRECTO:   consultar mapa (rápido) → si falta, verificar puntual → cerrar la unidad con el mapa al día
```

## DOC10 · Catálogo de reglas del proyecto sincronizado con la memoria

Todo proyecto tiene un **catálogo de reglas específicas** en la ruta que la capa 3 declara (ej. `.agente/reglas-proyecto.md`). Cada regla es una restricción, convención o principio del equipo/proyecto que sobrescribe o complementa la base común, numerada (`P1`, `P2`, …) para permitir referencias estables.

**Regla del sync bidireccional** entre catálogo y memoria (DOC5 · señales):

- **Cuando se crea una regla nueva** (o se endurece una existente): registrar la señal correspondiente en la memoria con tipo `restriccion`, `patron` o `aprendizaje` según aplique, con puntero al catálogo (`Ver P<N> en <ruta-del-catálogo>`).
- **Cuando se guarda una señal generalizable** (una decisión, un aprendizaje que aplica más allá de la unidad puntual): considerar si merece ser regla del catálogo. Si sí, crearla en el mismo cierre.
- **Cuando una regla P se promueve a la base común** (por P28): dejar banner "promovida a base" al inicio de la regla del catálogo con puntero a la sección base **y compactar la regla P al mínimo específico** — matiz que la base no cubre + ejemplos concretos + encadenamientos internos. Borrar el cuerpo duplicado con la base. Duplicar cuerpo entre catálogo y base es defecto (dos fuentes autoritativas → divergencia con el tiempo). La regla P conservada tiene el rol de anclar los nombres del proyecto (rutas, tablas, comandos) a la versión canónica, no de repetirla.

Para el conjunto de reglas C1-C10 · DOC1-DOC10 · F1-F5 (y demás secciones de la base): tienen numeración estable pensada para citarse desde el catálogo del proyecto. Ej. desde `.agente/reglas-proyecto.md` es válido referenciar `Endurece base 13 DOC7 con esta restricción específica del proyecto...`.

```
INCORRECTO: usuario dice "de aquí en adelante siempre X" · agente aplica · nada queda en el catálogo · próxima sesión olvida
CORRECTO:   aplica + crea regla P<N+1> en el catálogo + registra señal `restriccion` en la memoria con puntero al catálogo
```

Ver: `01` C10 (mensaje del usuario como posible mejora del setup), `13` DOC5 (señales).

## DOC11 · Tabla canónica de trazabilidad spec → implementación (extiende DOC3)

`DOC3` establece la trazabilidad spec → implementación como cierre obligatorio de una unidad de trabajo. `DOC11` fija el **formato canónico** de esa tabla, para que sea comparable entre unidades y auditable en el tiempo.

**Formato canónico** — 5 columnas obligatorias, una fila por afirmación técnica del spec:

| Ítem del spec | Categoría | Ubicación esperada | Estado | Evidencia |
|---|---|---|---|---|
| (frase literal o resumida) | (esquema · modelo · servicio · vista · prueba · permiso · ruta · doc) | (archivo real del proyecto) | ✅ / ❌ / N/A / parcial | (prueba concreta o commit) |

**Reglas de estado:**

- **✅ implementado** — la afirmación está reflejada íntegramente en la ubicación indicada y hay evidencia (prueba verde, commit apuntado).
- **❌ pendiente** — la afirmación no está implementada. Requiere justificación explícita (por qué se difiere, a qué unidad de trabajo se traslada).
- **N/A** — la afirmación no aplica en esta unidad (ej. la spec la enuncia como opcional o de otra fase). Requiere justificación.
- **parcial** — implementada solo en parte. Requiere descripción precisa de qué parte queda y a dónde se traslada.

**Regla operativa:** si al revisar la tabla aparece un faltante que **debería** estar en esta unidad, se **corrige in situ** — no se difiere. La tabla es el arbitraje final antes de cerrar. Los diferimientos legítimos se registran como `❌` con destino explícito, no como N/A.

**Ubicación de la tabla:** el documento de cierre de la unidad de trabajo (la capa 3 declara la ruta canónica — típicamente `funcionalidad_implementada.md` o equivalente). Plantilla: `plantillas/funcionalidad-implementada.md`.

```
INCORRECTO: cerrar con tabla incompleta o con "N/A porque sí" · próximo trabajo no sabe qué quedó pendiente ni por qué
CORRECTO:   tabla completa · faltantes justificados · diferimientos con destino explícito · N/A con motivo
```

**Encadenamiento:** `DOC3` establece la trazabilidad como principio · `DOC11` fija el formato tabular concreto · `02 F7` (verificar trazabilidad antes de cerrar) lo pide al final del flujo.

## DOC12 · Cada fase declara ORIGEN al abrirse — 3 categorías

Toda fase nueva declarada en el spec de un módulo (§Fases) debe abrir con un campo **ORIGEN** en 1 de 3 categorías (o híbrido):

- **📝 Modifica fase(s) anterior(es)** — nombrar cada fase que toca (ej. "arregla defectos de Fase F-3 y F-5 — gaps del cierre YYYY-MM-DD"). Si existe cierre de análisis (`DOC8`), referenciarlo.
- **✨ Funcionalidad nueva** — declarar que introduce funcionalidad no cubierta por fases previas (ej. "introduce el flujo X — nueva funcionalidad derivada de decisión Y").
- **🔀 Híbrido** — declarar ambos: "arregla gaps de F-3 + agrega funcionalidad nueva X".

**Motivo:** trazabilidad. Quien lea la §Fases del spec debe entender inmediatamente qué relación tiene cada fase con las anteriores. Sin esto, aparecen fases "sueltas" cuyo origen no es claro — el lector no sabe si es continuación del roadmap declarado, reacción a un análisis posterior o feature nueva no anticipada.

**Formato canónico del bloque de fase en el spec:**

```
### Fase «A-EP01-HU03-Descripción»   (identificador según 02·F12.6)

ORIGEN: <una o más categorías>
- 📝 Modifica fases anteriores: <lista>. <qué defecto/promesa se retoma>. Referencia: <cierre DOC8 si aplica>.
- ✨ Funcionalidad nueva: <qué introduce que no existía en el roadmap previo>.

Alcance:      «qué entra y qué explícitamente no».
Cambios técnicos:  «esquema/modelos/servicios/UI/comandos» (uno por bloque).
Criterios de aceptación: «medibles».
```

**Cuándo aplica:** toda fase nueva declarada desde la adopción de esta regla en adelante.

**Cuándo NO aplica:**

- Fases ya cerradas (retroactivo no) — quedan inmutables per DOC1 · su origen se infiere del historial.
- Sub-fases o hitos intermedios dentro de una fase (esos no son "fase" en el sentido de una unidad de trabajo con cierre propio).

**Réplica en el plan de trabajo:** la carpeta de la fase (ruta según [`02·F12.13`](02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md), identificador [`02·F12.6`](02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) replica el ORIGEN en su cabecera. Así el spec y el plan de trabajo coinciden en la trazabilidad de origen.

```
INCORRECTO: "Fase XX — cambios menores" sin ORIGEN · lector no sabe si es continuación
            de fase anterior o reacción a un análisis · o feature nueva
CORRECTO:   ORIGEN declarado con 1 de las 3 categorías · lector entiende de dónde sale
            la fase con solo leer el bloque de apertura
```

**Encadenamiento:** `DOC1` (persistir el trabajo) — el ORIGEN persiste con el resto de la fase · `DOC5` (señales) — si el ORIGEN es "arregla gap de análisis", la señal del gap queda apuntada · `DOC8` (cierre de análisis) — si el ORIGEN cita un cierre de análisis, cada `[gap-N]` que arregla se marca como ejecutado en el cierre correspondiente al terminar la fase.

## DOC13 · Catálogo de módulos vivo — registrar cada módulo al crearlo

Todo proyecto con múltiples módulos mantiene un **catálogo de módulos** consolidado — un índice de "qué existe" a nivel de módulo. Distinto del mapa de dependencias vivo (`DOC9`) que consolida las relaciones técnicas (modelos, componentes, rutas); el catálogo de módulos es la vista de más alto nivel: **qué módulos tiene el proyecto y qué hace cada uno**.

**Ruta canónica** — declarada por la capa 3 del proyecto (típicamente `.agente/dominio.md`, `documentacion/modulos.md` o equivalente). Plantilla: `plantillas/catalogo-modulos.md`.

**Contenido mínimo por entrada:**

- **Nombre del módulo** — el identificador estable.
- **Prefijo de rutas** (o namespace equivalente) — cómo se accede.
- **Descripción** — 1-2 líneas de qué hace y a quién sirve.
- **Estado** — activo · en desarrollo · scaffold · deprecado.
- **Puntero al spec** — enlace al prompt vivo del módulo si existe (`DOC6` retro-doc).
- **Entidades principales** — nombres cortos de las entidades de negocio propias del módulo (si aporta a la comprensión global).

**Regla operativa:** cada módulo nuevo se registra en el catálogo **antes de cerrar** la unidad de trabajo que lo crea. No se pregunta al usuario si registrar — es obligatorio.

**Qué cuenta como módulo nuevo:**

- Prefijo de rutas propio o dominio funcional autónomo con permisos propios.
- Submódulo con semántica propia y spec separado.

**Qué NO cuenta como módulo nuevo:**

- Una fase de un módulo existente.
- Un fix o refactor interno.
- Un componente hijo reutilizable dentro de un módulo ya registrado.

**Motivación:** sin este catálogo, sesiones sucesivas asumen el sistema como "solo lo que recuerdo del código" y omiten módulos existentes al planificar. El catálogo es la fuente autoritativa consultable de "qué módulos tiene el proyecto hoy" — se consulta al inicio de cada unidad de trabajo (encadena con `02 F1`).

```
INCORRECTO: se crea un módulo nuevo · sesiones posteriores asumen que el proyecto
            "solo tiene X e Y" porque el nuevo módulo no está en el catálogo
CORRECTO:   al cerrar la unidad de trabajo que creó el módulo, agregar entrada
            completa al catálogo — nombre + prefijo + descripción + estado + spec
```

**Encadenamiento:** `DOC6` (retro-doc de módulos existentes) — el catálogo lista los módulos, el spec de cada uno vive en su propio archivo · `DOC9` (mapa de dependencias) — DOC13 es el índice de alto nivel; DOC9 es el detalle técnico interno · `02 F1` (cargar contexto) — el catálogo se consulta como primer paso al abrir una unidad.

## DOC14 · Referencias a `.md` del proyecto: path relativo + route "atrapa .md" para render local

Toda referencia desde cualquier archivo `.md` a **otro `.md` del proyecto** usa el patrón **link markdown de dos partes**:

- **Texto visible** = ruta absoluta desde `documentacion/...` (o desde la raíz del proyecto si vive fuera de `documentacion/`). Da contexto legible sin abrir el link — el lector sabe exactamente dónde queda el archivo sin adivinar.
- **Link real** = path RELATIVO desde el archivo actual al archivo destino, terminando en `.md`. Con esta forma:
  - **GitHub / GitLab** renderizan el `.md` destino nativamente al hacer clic.
  - **Local (con framework corriendo)** un route "atrapa cualquier URL terminada en `.md`" lo renderiza como HTML.
  - **VSCode / editores** el Ctrl+Click abre el archivo local.

**Formato canónico:** `[<ruta absoluta legible>](<path-relativo>.md)`.

**Ejemplos:**

```
✅ Desde documentacion/prompts/erp/analisis/multitenancy.md apuntando a
   documentacion/organizacion-jerarquica/fase-hg-slug/plan_trabajo.md:
   [documentacion/organizacion-jerarquica/fase-hg-slug/plan_trabajo.md](../../../organizacion-jerarquica/fase-hg-slug/plan_trabajo.md)

✅ Desde documentacion/organizacion-jerarquica/fase-hg-slug/funcionalidad_implementada.md apuntando a
   documentacion/prompts/erp/analisis/multitenancy.md:
   [documentacion/prompts/erp/analisis/multitenancy.md](../../prompts/erp/analisis/multitenancy.md)

❌ URL absoluta del route local — funciona local pero cae en 404 en GitHub:
   [documentacion/.../plan_trabajo.md](/prompt/organizacion-jerarquica/fase-hg-slug/plan_trabajo)

❌ Solo el nombre corto sin contexto:
   [plan_trabajo.md](../../../organizacion-jerarquica/fase-hg-slug/plan_trabajo.md)

❌ Solo el path como texto plano, sin link markdown:
   `documentacion/organizacion-jerarquica/fase-hg-slug/plan_trabajo.md`
```

**Requisito del proyecto** (para que funcione la parte "local render HTML"): existe una ruta que atrapa cualquier URL terminada en `.md` y la renderiza como HTML. En pseudocódigo agnóstico:

```
RUTA  GET  /<path>.md          # el comodín <path> captura también las barras "/"
    si el entorno NO es local            → 404
    candidatos = [ raíz_proyecto/<path>.md,
                   raíz_proyecto/<prefijo_canónico>/<path>.md ]   # <prefijo> = documentacion/ u el que aplique
    archivo = primer candidato que exista en disco
    si no existe ninguno                 → 404
    devolver  render_markdown_a_html(archivo)
```

El **fallback** al segundo candidato (bajo el prefijo canónico) permite que los links relativos servidos desde rutas "atajo" —que no incluyen ese prefijo en la URL— resuelvan igual al archivo real.

**Requisito crítico del fallback:** cuando el proyecto usa un route "atajo" que renderiza `.md` con URLs cortas (ej. `/prompt/<slug>` sin prefijo de carpeta), los links relativos dentro del `.md` se resuelven contra la URL del navegador — no contra el path físico del archivo. Sin el fallback, un link válido a nivel de filesystem falla como 404 al hacer clic desde el atajo. El fallback bajo el prefijo canónico (`documentacion/` en este proyecto · el que aplique en cada uno) mantiene el patrón funcional en las dos formas de acceso.

Con ese route en su sitio, el mismo link relativo funciona en los 3 contextos (GitHub, local, editor) — sin duplicar el link ni hardcodear URLs.

**Motivo:** un lector nuevo puede leer el documento entero como texto plano y saber dónde vive cada referencia sin resolverla mentalmente. Y a la vez, el clic abre el `.md` como HTML formateado en el navegador local (mucho más legible que Markdown crudo) o directamente en la vista nativa de GitHub — sin cambiar el link ni duplicar el patrón.

**No aplica** a:
- Nombres cortos usados como identificadores (`_base_modulo.md`, `MEMORY.md`) mencionados en prosa cuando el lector ya sabe dónde viven.
- Referencias a **código fuente** (archivos de código, plantillas de vista, migraciones, seeds — cualquier extensión del stack): también son links relativos, pero se abren directamente en el editor, no como HTML (ej. `[<ruta/legible/al/archivo>](../../../ruta/relativa/al/archivo)`).

**Encadenamiento:** `DOC7` (referencias entre docs con historial cruzado bidireccional) — DOC14 define el **formato del link**; DOC7 el **contenido del cruce** (por qué + qué mejora aporta). Los dos aplican juntos.

## DOC15 · Historias de Usuario desde plantilla central

Al crear una Historia de Usuario (HU), el agente parte de la plantilla central `plantillas/HU.md` (fuente única, agnóstica) — **no** de una copia local ni de memoria. El resultado, ya rellenado, se escribe versionado en la ubicación de la HU según [`02·F12.13`](02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md) (la HU vive dentro de su épica).

- **La plantilla NO se copia** a `.agente/` ni al proyecto: se lee del centro **cada vez**. Así, una mejora a `plantillas/HU.md` llega a todos los proyectos sin drift (a diferencia de los 4 archivos de `.agente/`, que sí se copian porque guardan datos propios de cada proyecto — la HU es formato, no datos).
- **Nomenclatura:** `HU-<NNN>` correlativo por proyecto (o por módulo si la capa 3 lo declara) · `<slug>` corto en kebab-case.
- **Contenido real, no plantilla en crudo:** rol específico (no "usuario" genérico), criterios de aceptación en Gherkin que cubran camino feliz + validación/error + caso borde, y las secciones que no apliquen se eliminan (no se dejan con los `[…]`).
- **Trazabilidad:** cada HU nace en `Backlog`/`Ready` según su DoR; la §12 (bitácora) registra creación y cambios. Las tareas técnicas derivadas (§7) alimentan la planificación (`02` F4).
- **Override capa 3:** un proyecto puede ajustar ruta, nomenclatura o secciones de la HU en `reglas-proyecto.md` (nunca el núcleo `00`).

**Índice `README.md` en cada nivel del árbol.** Ninguna carpeta del árbol de la HU ([`02·F12.13`](02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md): épicas → HU → fases) queda "muda": cada una —empezando por la raíz y bajando a cada subcarpeta— tiene un `README.md` que **lista y explica su contenido inmediato** (solo lo que cuelga directo de ella, no el árbol entero):

- Si la carpeta tiene **subcarpetas** (una por módulo/épica/lo que aplique): una línea por subcarpeta con su nombre y una frase de qué contiene. **Cada subcarpeta repite el patrón** (su propio `README.md`) — recursivo hasta el último nivel.
- Si la carpeta **solo tiene archivos** (las HU sueltas): igual se listan uno por uno, cada uno con su título y estado (`HU-012 — Alta de cliente · Ready`).
- El `README.md` es **vivo**: se actualiza en el mismo cambio en que se crea, mueve o cierra una HU o carpeta. No es una foto de una fecha.

> El árbol es el de [`02·F12.13`](02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md) (épicas → HU → fases). La regla del README aplica a **cada carpeta** de ese árbol.

```
INCORRECTO: escribir la HU de memoria o inventando el formato · o copiar HU.md dentro de .agente/ (se vuelve vieja)
            · o dejar carpetas del árbol sin README que diga qué hay dentro
CORRECTO:   copiar de plantillas/HU.md (central) → rellenar con datos reales → guardar en la ubicación de `02·F12.13`
            + actualizar el README.md de esa carpeta (y los de arriba si se creó una carpeta nueva)
```

**Encadenamiento:** `DOC1` (persistir el trabajo) — la HU es entregable versionado · `DOC13` (catálogo de módulos) — la HU declara su módulo; el `README.md` del árbol ([`F12.13`](02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) es su índice navegable · `DOC9` (mapa vivo) — mismo principio de "índice que se actualiza al cerrar, no foto" · `02` F1/F2/F4 (contexto → spec → plan) — la HU precede o acompaña al spec del módulo y sus §7 tareas alimentan el plan.

## DOC16 · Épicas desde plantilla central

Al crear una Épica, el agente parte de `plantillas/epica.md` (fuente única, agnóstica) — no de memoria ni de una copia local. El resultado, rellenado, se guarda versionado en la ubicación de la épica según [`02·F12.13`](02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md) (la épica es la raíz de su subárbol HU → fases).

- **La plantilla NO se copia** a `.agente/`: se lee del centro **cada vez** (misma razón que `DOC15`·HU — es formato, no datos de proyecto).
- **Nomenclatura:** `EP-<NNN>` correlativo por proyecto · `<slug>` corto en kebab-case.
- **Enlace bidireccional con las HU:** la épica lista sus HUs (§9 de la plantilla) y cada HU declara a qué épica pertenece (`HU.md §1`). Al crear o mover una HU se actualizan **los dos lados**.
- **Criterios de resultado, no de pantalla:** los criterios de aceptación de la épica (§7) son de negocio/resultado; el detalle de comportamiento vive en las HU.
- **La épica es obligatoria:** toda HU pertenece a una épica, aunque la épica agrupe **una sola** HU. No se omite ni se fusiona por tamaño ([`02·F0`](02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) cadena obligatoria). El brief le da origen: sin brief no hay épica.
- **Índice vivo:** el árbol de [`02·F12.13`](02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md) sigue el mismo `README.md` por nivel de `DOC15`.
- **Override capa 3:** ruta, nomenclatura o secciones ajustables en `reglas-proyecto.md` (nunca el núcleo `00`).

```
INCORRECTO: escribir la épica de memoria · o meter en la épica criterios de pantalla que son de HU · o listar HUs en la épica pero no declarar la épica en cada HU
CORRECTO:   copiar de plantillas/epica.md → rellenar → guardar en la ubicación de `02·F12.13` → enlazar con sus HU en ambos sentidos
```

**Encadenamiento:** `DOC15` (HU) — la épica agrupa HUs con enlace bidireccional · `DOC13` (catálogo de módulos) — una épica puede cruzar varios módulos · [`02·F0`](02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) paso 4 (la épica en el flujo macro) · [`02·F0`](02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) estación de épica en el orquestador (`sdd-orchestrator`).

---

Ver: `02` F1/F2/F6/F7, `08` (plan de pruebas y verificaciones manuales), `07` Q5 (documentar, no solo comentar), `11` CFG3.
