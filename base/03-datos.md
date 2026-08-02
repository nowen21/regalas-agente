# 03 · Datos y persistencia  ·  `[CAPA 2]`

Diseño y cambio del almacenamiento: esquema, migraciones, catálogos. La capa 3 declara los nombres concretos (motor, prefijos, tabla de catálogo, trait de auditoría).

---

## D1 · Toda tabla nueva se normaliza y lleva auditoría

**Normalización (1FN/2FN/3FN).** No se acepta: columnas multivaluadas (listas/JSON/arrays serializados — el 1:N va en tabla hija con FK, el N:M en pivot), atributos duplicados del padre, dependencias transitivas, ni enums nativos (van a catálogo, D4).

**Auditoría** en toda tabla nueva (salvo pivots puras): quién creó, quién editó, timestamps de creación/actualización. Las tablas transaccionales/contables/legales llevan **soft delete**.

**Integridad en la BD** (no solo en la app): FK con política de borrado explícita; `UNIQUE` en columnas con unicidad conceptual; índices en lo que se filtra (FKs, fechas, estados).

```
INCORRECTO: guardar "Guantes,Mascarilla,Botas" como texto
CORRECTO:   tabla hija + FK

INCORRECTO: tabla sin auditoría "porque es un catálogo simple"
CORRECTO:   todas la llevan, salvo pivots puras
```

## D2 · Cada cambio de esquema es una migración reversible

Migración independiente, con aplicación y reversión funcionales. **Nunca modifiques una migración ya ejecutada** — crea una nueva. Documenta qué y por qué. Correrla contra datos reales requiere autorización (`00` · N4).

## D3 · Migraciones retrocompatibles con los datos existentes

Preservar datos y comportamiento sin intervención manual.

- Columna obligatoria nueva → con **default** equivalente al comportamiento previo.
- Enum → FK a catálogo: (1) crear el catálogo, (2) poblar la columna nueva mapeando cada valor viejo, (3) recién ahí hacerla obligatoria.
- **Nunca borres datos históricos** al migrar. Si la reversión no puede recuperar datos, documéntalo.

```
INCORRECTO: columna obligatoria sin default → falla si ya hay filas
CORRECTO:   default equivalente al comportamiento previo, luego endurecer
```

## D4 · Valores configurables van a catálogo — cero hardcode

Nada que pueda cambiar por decisión del negocio, la ley o la operación se quema en el código (constantes, arrays, `switch`/`match`, literales en condiciones): umbrales, listas válidas, mapas por tipo, textos editables, flags de comportamiento. Va a un **catálogo** consultable.

Si necesitas escribir un mapa/array/switch con valores del dominio, **detente y crea el catálogo primero**.

- **Bifurca por código semántico**, no por id (los ids cambian entre entornos).
- Los flags de un tipo/estado viven **junto al catálogo** (metadata), no en el código.
- Los códigos que el código referencia se marcan **protegidos** (no borrables desde la UI).
- Cachea los catálogos que se consultan seguido.

Excepciones (cero hardcode ≠ cero literales): constantes técnicas (columnas, rutas, eventos), fórmulas matemáticas fijas, códigos externos estables por ley. Ante la duda, **inclínate al catálogo**.

**Cuando el catálogo genérico no cabe** — a veces el valor configurable tiene estructura propia (mapas por tipo, rangos numéricos con intervalos, relaciones internas entre valores) que no encaja en la tabla genérica de parámetros (típicamente `codigo` + `valor` + `flags`). En ese caso, **crear una tabla propia de dominio** para ese conjunto (`<dominio>_<subdominio>`) con auditoría estándar (D1), FKs a otros catálogos si aplica, y **seed inline en la migración**. Sigue siendo cero hardcode — el catálogo es específico, no genérico. Al detectar hardcode existente durante una unidad de trabajo, agregar tarea explícita al plan para migrarlo antes del cierre.

```
INCORRECTO: if (saldo < 100000)                          // umbral quemado
CORRECTO:   leer el umbral del catálogo

INCORRECTO: validar: modalidad ∈ {'efectivo','especie'}   // lista fija quemada en el código
CORRECTO:   validar contra los códigos leídos del catálogo

INCORRECTO: if (tipo_id === 3)                            // id opaco
CORRECTO:   if (tipo_codigo === 'especie')               // código semántico
```

## D5 · Con la BD desplegada, la validación nueva va en la app

Si la BD ya está en producción, su estructura es un contrato vigente. Una validación nueva que no encaje limpio (limita el motor, choca con datos legacy, migrar es caro) **no se fuerza en la BD**: va al servicio/observer/regla.

- Si una restricción falla al aplicarse o exigiría borrar/modificar filas históricas, se **descarta en BD** (salvo autorización para limpiar datos) y queda en el servicio.
- El servicio que sostiene la validación lleva **prueba dedicada** (sin ella, se degrada en silencio).
- Documenta en la migración por qué no vive en la BD.

**No aplica** en diseño desde cero (sin datos aún): ahí el invariante sí va al esquema.

```
INCORRECTO: la migración falla contra los datos → editar la BD a la fuerza
CORRECTO:   validación en el servicio + prueba + nota en la migración
```

---

## D6 · Concurrencia e idempotencia

Cuando dos operaciones pueden tocar el mismo dato a la vez, protegé la integridad — no confíes en que "no va a pasar".

- **Idempotencia:** una operación repetida (doble clic, doble submit, reintento) no debe duplicar efectos. Usá una clave de idempotencia o verificá el estado antes de aplicar.
- **Actualización concurrente (lost update):** al modificar un valor compartido (un saldo, un contador), usá **bloqueo optimista** (una versión / `updated_at` que se revalida al guardar) o una operación **atómica** en la BD; nunca leer-modificar-escribir sin control.
- **Duplicados por carrera:** una restricción `UNIQUE` en la BD es la **única** garantía real contra dos inserciones simultáneas del mismo registro; la validación en la app no alcanza (dos procesos la pasan a la vez).

```
INCORRECTO: leer saldo → sumar en memoria → guardar   (dos procesos se pisan, se pierde una suma)
CORRECTO:   incrementar el saldo de forma atómica en la BD, o bloqueo optimista con revalidación
```

## D7 · Persistencia histórica SCD-2 — patrón canónico para valores que evolucionan

Complementa `D5` (validación en la app cuando la BD ya está desplegada). Aplica cuando un valor de negocio **cambia con el tiempo** y las consultas históricas necesitan saber **"cómo estaba X en fecha Y"**, no solo "cómo está X hoy".

Los cálculos al vuelo dan siempre el estado actual — pierden la historia. Auditorías, informes legales, disputas, reportes retrospectivos necesitan el estado histórico real. La estrategia "reconstruir sumando datos vivos hasta fecha X" **solo funciona si el pasado es inmutable**; en cuanto haya anulaciones diferidas, ediciones bajo ventana, reversiones o cambios de relación, la reconstrucción al vuelo devuelve el estado teórico, no el histórico real.

**Cuándo aplica:**

- Cálculos derivados de datos operativos que cambian (participación, saldos por período, totales acumulados).
- Relaciones que evolucionan y afectan cálculos históricos (jerarquía padre/hijo, asignación a responsable, categoría del cliente).
- Estados de entidades que se referencian en reportes históricos.
- Cualquier valor que pueda aparecer en una demanda, auditoría o disputa con la pregunta "¿cuánto era esto en fecha X?".

**Cuándo NO aplica:**

- Datos de configuración estáticos (catálogos que no cambian con el uso).
- Cálculos sin relevancia histórica (estadísticas del día actual, dashboards operativos en tiempo real).
- Datos ya inmutables por diseño (snapshots firmados · registros congelados por regla del dominio · ver `15` registros inmutables).
- Reportes de "estado actual" donde una consulta con soft-delete + timestamps es suficiente y auditable.

**Patrón canónico (SCD-2 · tramos con `desde_at` / `hasta_at`):**

1. **Tabla `<entidad>_historial`** con: PK · FK a la entidad fuente · las columnas del estado que se congelan · `desde_at NOT NULL` · `hasta_at NULL` (null = tramo vigente) · `motivo` corto que identifica el evento que abrió el tramo · auditoría estándar (D1) · índice `(fuente_id, desde_at)`.
2. **Backfill en la migración**: por cada registro fuente existente, insertar tramo inicial con `desde_at = fuente.created_at`, `hasta_at = NULL`, motivo `"backfill migración inicial"`.
3. **Evento de dominio por cada cambio significativo** en la entidad fuente (creado/actualizado/eliminado/cualquier acción del negocio que cambie los valores del tramo).
4. **Listener dedicado** que, dentro de transacción, (a) cierra el tramo vigente afectado (`hasta_at = ahora`) y (b) inserta el tramo nuevo con los valores del nuevo estado.
5. **Consulta canónica** en el modelo / servicio: `estadoEn(fecha) → valores del tramo vigente en esa fecha`.
6. **UI — línea de tiempo visible** en la ficha de la entidad, para que el usuario final audite la evolución sin salir del sistema.
7. **Tests obligatorios**: backfill correcto · evento dispara actualización · estado en fecha pasada devuelve valor histórico (no el actual) · un solo tramo vigente por entidad a la vez.
8. **Cascada de eliminación cuidadosa**: la entidad fuente NO se hard-delete si tiene historial; solo soft-delete. El historial sobrevive.

**Consideración de volumen** — SCD-2 puro puede generar N filas por evento si el evento afecta a N entidades relacionadas. Cuando el volumen sea prohibitivo, alternativa: **snapshot vector** (una fila por evento con el mapa completo del estado en un campo estructurado). Se decide al abrir la unidad con datos reales, no anticipadamente.

**Anti-patrón rechazado:** "calcular al vuelo y ya, es más simple". Simple hoy, incorrecto mañana. Consulta histórica → lee historial persistido. Consulta actual → puede leer estado directo. No mezclar.

```
INCORRECTO: "totalHoy" y "totalEnFecha(X)" leen del mismo estado vivo · el segundo devuelve valor teórico si el pasado se editó
CORRECTO:   tabla historial con tramos + consulta canónica estadoEn(fecha) → valor congelado que refleja lo que era realmente ese día
```

**Encadenamiento:** `D1` (auditoría toda tabla nueva) — la tabla historial también lleva audit · `D5` (validación en la app cuando la BD está desplegada) — SCD-2 vive fuera del modelo original, no invade su esquema · `15` (registros inmutables) — el tramo cerrado es inmutable por diseño.

## D8 · Distinguir pertenencia de autoría en el modelo de datos

En proyectos con múltiples usuarios trabajando sobre entidades compartidas (multi-tenant, multi-proyecto, multi-organización), el modelo debe distinguir explícitamente **dos conceptos**:

- **Pertenencia** — a quién pertenece el dato como entidad de negocio: `tenant_id`, `organizacion_id`, `proyecto_id`, `cuenta_id`, `equipo_id`, etc. Ancla la entidad al contenedor de negocio que lo posee.
- **Autoría** — quién manipuló el dato: `usercreate_id` / `userupdate_id` (o los equivalentes del stack). Es auditoría, no pertenencia.

**No confundir los dos.** La confusión típica es anclar la entidad al `usuario que la creó` (`Auth::id()` / `usercreate_id`) y filtrar los listados por autoría. Esto rompe el sistema en cuanto un segundo usuario del mismo tenant/proyecto edita, o el usuario original se va y otro debe operar sobre las mismas entidades.

**Consecuencias operativas del modelo correcto:**

- **Consultas de listado** filtran por **pertenencia** (según el acceso del usuario actual a tenants/proyectos), no por autoría.
- **Permisos + scope** validan el acceso: "el usuario X tiene permiso Y sobre el tenant Z", no "el usuario X es el creador del registro".
- **Ediciones** no requieren ser "el creador" — cualquier usuario con acceso al contenedor y permiso puede operar.
- **Reportes de auditoría** usan la columna de autoría (quién hizo qué), no la de pertenencia.

**Excepción legítima:** entidades genuinamente personales del usuario (favoritos, borradores privados, preferencias de UI). Ahí la pertenencia sí es `user_id`. Cuando lo dudes, preguntá: "¿esto es del usuario, o del tenant/proyecto donde el usuario está trabajando?"

```
INCORRECTO: `Aporte::where('usercreate_id', Auth::id())` para listar aportes del
            proyecto activo → el segundo usuario del mismo proyecto no ve nada
CORRECTO:   `Aporte::where('proyecto_id', $proyectoActivo)` — pertenencia del proyecto;
            usercreate_id queda solo como campo de auditoría
```

**Encadenamiento:** `D1` (auditoría toda tabla nueva) — la columna de autoría es parte de la auditoría estándar · `D6` (concurrencia) — múltiples usuarios operando el mismo tenant refuerza la necesidad de este modelo · `04 S1` (autorización con scope) — la validación de scope opera sobre la columna de pertenencia, no de autoría.

---

Ver: `00` N4/N5 (datos reales, masivas), `04` (validación/authz), `05` E2 (transacciones), `06` (índices, N+1), `15` (registros inmutables).
