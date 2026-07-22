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

```
INCORRECTO: if (saldo < 100000)                          // umbral quemado
CORRECTO:   leer el umbral del catálogo

INCORRECTO: 'modalidad' => 'required|in:efectivo,especie' // lista quemada
CORRECTO:   validar contra los códigos del catálogo

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

Ver: `00` N4/N5 (datos reales, masivas), `04` (validación/authz), `06` (índices, N+1), `15` (registros inmutables).
