# 03 · Datos y persistencia

> **Capa 2 · agnóstica al stack.** Cómo diseñar y modificar el almacenamiento de datos: esquema, migraciones, catálogos y valores configurables. Los nombres concretos (motor de BD, prefijos de tabla, tabla de catálogo, trait de auditoría) los declara la capa 3; aquí van los principios. No puede ablandar lo que el núcleo (`00`) blinda sobre datos reales.

---

## D1 · Toda tabla nueva se normaliza y lleva auditoría

**Normalización.** Diseñar en formas normales (1FN, 2FN, 3FN; BCNF cuando aplique). No se acepta:

- Columnas multivaluadas (listas separadas por coma, arrays serializados, JSON con estructura relacional). Si el dato es 1:N va en una tabla hija con clave foránea; si es N:M, en una tabla intermedia.
- Duplicar atributos que ya viven en el registro padre referenciado.
- Dependencias transitivas (no guardar un valor derivable por join).
- Valores tipificados "quemados" como enum nativo en la columna: van a un catálogo (ver D4).

**Auditoría.** Toda tabla nueva (salvo tablas intermedias puras sin datos propios) registra: **quién creó** y **quién editó** por última vez, y **marcas de tiempo** de creación y actualización. Las tablas con valor transaccional, contable o legal llevan además **borrado lógico** (soft delete) en vez de borrado físico.

**Integridad a nivel de BD** — no depender solo de la validación en la aplicación:

- Toda clave foránea con su restricción y política de borrado explícita (cascada / restringir / anular según el caso).
- Toda columna con unicidad conceptual lleva restricción `UNIQUE` en la BD (la validación en la app complementa, no reemplaza).
- Índices en las columnas que se filtran con frecuencia (claves foráneas, fechas, estados).

```
INCORRECTO: guardar "Guantes,Mascarilla,Botas" como texto en una columna
CORRECTO:   tabla hija + relación por clave foránea

INCORRECTO: tabla nueva sin campos de auditoría "porque es un catálogo simple"
CORRECTO:   todas las tablas llevan auditoría, salvo intermedias puras
```

---

## D2 · Cada cambio de esquema es una migración reversible

- Cada cambio de esquema es una **migración independiente** con su rutina de aplicación y de reversión, ambas funcionales.
- **Nunca modificar una migración ya ejecutada** — siempre crear una nueva.
- Documentar en la migración **qué** cambia y **por qué**.
- Correr una migración contra una BD con datos reales es una operación sensible: requiere autorización explícita (núcleo `00` · N1/N4).

---

## D3 · Migraciones retrocompatibles con los datos existentes

Toda migración que agregue columnas, cambie tipos o refactorice el esquema debe **preservar los datos y el comportamiento existentes sin intervención manual**.

- Al agregar una columna obligatoria, darle un **valor por defecto** semánticamente equivalente al comportamiento previo.
- Al reemplazar un valor tipificado por una referencia a catálogo: (1) crear/asegurar el catálogo, (2) agregar la columna nueva y **poblarla** mapeando cada valor viejo, (3) recién entonces aplicar la obligatoriedad.
- **Nunca borrar datos históricos al migrar.** Los registros preexistentes quedan consultables después del cambio.
- Si la reversión no puede recuperar datos (p. ej. al eliminar una columna vieja), documentarlo explícitamente en la migración.

```
INCORRECTO: agregar columna obligatoria sin default → falla si ya hay filas
CORRECTO:   agregar con default equivalente al comportamiento previo, luego endurecer
```

---

## D4 · Valores configurables viven en catálogo — cero hardcode

**Nada** que pueda cambiar por decisión del negocio, de la normativa o de la operación se "quema" en el código (constantes, arrays, `switch`/`match`, literales en condiciones). Ese tipo de dato vive en un **catálogo** consultable: umbrales, listas de valores válidos, mapas de configuración por tipo, plantillas de texto editables, banderas de comportamiento.

**Regla dura:** si al implementar detectás que necesitás escribir un mapa/array/switch con valores del dominio, **detente y creá el catálogo (o la tabla) primero**. El código consulta esos valores, no los inventa como literal.

**Cómo se consume el catálogo:**

- **Bifurcar por un código semántico estable**, no por el identificador numérico (los ids son opacos y cambian entre entornos).
- Las banderas de comportamiento de un tipo/estado viven **junto al catálogo** (p. ej. en una columna de metadatos), no dispersas en el código. Las validaciones las leen dinámicamente.
- Los códigos que el código de la aplicación referencia se marcan como **protegidos** (no se pueden renombrar/eliminar desde la UI).
- Cachear en memoria los catálogos que se consultan repetidamente.

**Excepciones legítimas** (cero hardcode ≠ cero literales): constantes técnicas del framework y del dominio técnico (nombres de columnas, rutas, eventos), fórmulas matemáticas fijas, y códigos externos estables por ley. Ante la duda de si algo "puede cambiar", **inclínate al catálogo**: el costo de una tabla nueva es una migración; el de descubrir tarde que era configurable es un parche de emergencia.

```
INCORRECTO: if (saldo < 100000) { ... }          // umbral quemado
CORRECTO:   leer el umbral del catálogo y comparar

INCORRECTO: 'modalidad' => 'required|in:efectivo,especie,industria'   // lista quemada
CORRECTO:   validar contra los códigos leídos del catálogo

INCORRECTO: if (tipo_id === 3) { ... }            // bifurca por id opaco
CORRECTO:   if (tipo_codigo === 'especie') { ... } // bifurca por código semántico
```

Al detectar hardcode existente en el código que estás tocando, agregá su migración a catálogo como tarea explícita del plan; no lo dejes "para después".

---

## D5 · Con la BD ya desplegada, las validaciones nuevas van en la aplicación

Cuando la BD ya está en producción, su estructura es un **contrato vigente**. Una validación o invariante nueva que **no encaje limpiamente** en el esquema actual (por limitación del motor, por incompatibilidad con datos legacy, por costo prohibitivo de migrar) **no se fuerza a nivel BD**: se implementa en la aplicación (servicio / observador / regla de validación).

- Si una restricción propuesta **falla** al aplicarse o exigiría **borrar/modificar filas históricas**, se **descarta a nivel BD** (salvo autorización explícita para limpiar datos) y la validación queda en el servicio.
- El servicio que sostiene la validación lleva una **prueba dedicada** que cubre la violación esperada. Sin prueba, la regla se degrada en silencio.
- Documentar en la migración **por qué** la validación no vive en la BD.

**Cuándo NO aplica:** en un diseño desde cero (la BD aún no tiene datos ni está desplegada) sí es correcto llevar el invariante al esquema. Esta regla protege la BD existente, no la nueva.

```
INCORRECTO: la migración falla contra los datos existentes → editar la BD a la fuerza
CORRECTO:   dejar la validación en el servicio + prueba que la verifica + nota en la migración
```

---

## Relación con el resto del estándar

- **Núcleo `00` · N4/N5** — nunca operar destructivamente sobre datos reales; operaciones masivas con preview + log + confirmación.
- **`04-seguridad.md`** — la validación de entrada y la autorización complementan la integridad del esquema.
- **`06-rendimiento.md`** — índices, paginación y N+1 se apoyan en un buen diseño de datos.
- **`08-pruebas.md`** — las validaciones que viven en la app (D5) exigen prueba dedicada.
- **`15-registros-inmutables.md`** — patrón para datos con valor legal/contable que no se editan, se anulan.
