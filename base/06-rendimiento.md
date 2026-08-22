# 06 · Rendimiento y eficiencia  ·  `[CAPA 2]`

> **Historia dueña del texto:** [EP-001 HU-019](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-019-el-capitulo-06-rendimiento-y-eficiencia/HU-019-el-capitulo-06-rendimiento-y-eficiencia.md). Todo cambio de este capítulo baja por ella ([`02·F23`](02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md)).

Código que no se degrada con el volumen. Regla general: **mide antes de optimizar**, pero no metas ineficiencias evidentes. La capa 3 declara herramientas (caché, profiler, límites).

---

## R1 · Evita consultas en bucle (N+1)

No ejecutes una consulta por cada elemento de una lista. Carga las relaciones por adelantado (**eager loading**). Prefiere un join o un `IN (...)` a N consultas.

```
INCORRECTO: for (factura in facturas) { imprimir(factura.cliente.nombre) }  // 1 + N
CORRECTO:   cargar facturas con su cliente por adelantado → 1-2 consultas
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

El análisis del 2026-08-07 en [analisis/base-2026-08-07-cumplimiento-meta-reglas.md](../analisis/base-2026-08-07-cumplimiento-meta-reglas.md) la daba por cumplida, y las once filas que se cuentan se volvieron a contar con el programa. Coincide: 161 caracteres de 320.

La fila **5** pasa aunque el ejemplo tenga forma de código: no nombra lenguaje, framework ni motor. `for` e `IN (...)` son de cualquiera.

Está clasificada y con validador escrito —`rendimiento.py`—, así que la fila **18** pasa con programa detrás y no solo con el registro.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## R2 · Nunca cargues conjuntos sin límite

- Toda lista para el usuario va **paginada**.
- Procesa grandes volúmenes **por lotes** (chunking), no todo en memoria.
- Trae **solo las columnas necesarias**, no `SELECT *` para tres campos.

```
INCORRECTO: cargar 200.000 registros en la vista y renderizarlos todos
CORRECTO:   paginar (25-50 por página) y consultar solo lo visible
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**La fila 9 pasa aunque el cuerpo tenga tres viñetas**, y el análisis del 2026-08-07 lo dice mejor de lo que se podría decir acá: *«paginar, lotes y columnas son caras de la misma exigencia»*. Las tres responden a lo mismo — no traer más de lo que se necesita — y ninguna se sostiene sin las otras: paginar la vista y traerse todas las columnas deja el problema donde estaba.

Es el contraste útil con [`14·EST2`](14-estructura-codigo.md#est2--nomenclatura-consistente), que reprueba esa fila hoy: allá las partes se cumplen por separado, acá no.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## R3 · Índices en lo que se filtra y ordena

Las columnas por las que se filtra, une u ordena seguido llevan **índice** (FKs, fechas, estados, búsqueda). Uno de más frena las escrituras; uno de menos vuelve la consulta un escaneo completo. Indexa según el patrón real, no "por si acaso".

```
INCORRECTO: filtrar por fecha sin índice en una tabla grande → escaneo completo
CORRECTO:   índice en la columna de fecha del filtro
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**El análisis del 2026-08-07 la marcaba en amarillo, y no por ella: [`03·D1`](03-datos.md#d1--la-tabla-nueva-nace-normalizada) duplica su contenido.** El veredicto de entonces fue explícito — *«un solo dueño: `R3`; [`03·D1`](03-datos.md#d1--la-tabla-nueva-nace-normalizada) enlaza»*.

Se comprobó contra el texto de hoy: **`R3` no cita a [`03·D1`](03-datos.md#d1--la-tabla-nueva-nace-normalizada) ni le toma nada prestado.** Dice lo suyo entero y por su cuenta, así que la fila **11** pasa. Lo que hay que corregir vive en el capítulo `03`, y va al [pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md](../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md).

**Es el mismo caso que [`10·DEP3`](10-dependencias.md#dep3--audita-vulnerabilidades-y-mantén-al-día) por el lado bueno.** Allá la regla del capítulo dueño repite a la de otro y por eso reprueba; acá la dueña está limpia y quien repite es la de al lado. Cuál de las dos reprueba depende de quién copió, no de quién duplica.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## R4 · Cachea lo caro y estable, con invalidación clara

Cachea lo **caro** que **cambia poco** (catálogos, agregados pesados, consultas frecuentes idénticas). Define **cuándo se invalida** desde el diseño: sin eso, la caché sirve datos viejos. Invalídala en el evento que cambia el dato de origen.

```
INCORRECTO: cachear un saldo y no invalidarlo nunca
CORRECTO:   cachearlo e invalidarlo en el evento que lo modifica
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

Cumplía en el análisis del 2026-08-07 y se volvió a contar: 241 de 320.

La fila **9** pasa aunque el cuerpo diga qué cachear **y** cuándo invalidarlo: no se pueden cumplir por separado. Una caché sin invalidación definida no es una caché a medias — es una fuente de datos viejos, que es peor que no tenerla. La regla lo dice con esas palabras.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## R5 · Trabajo pesado fuera del ciclo de petición

Lo que tarda (correos, reportes grandes, servicios externos lentos, procesamiento masivo) va a **segundo plano / cola**, no bloquea la respuesta.

```
INCORRECTO: enviar 5.000 correos dentro de la petición → timeout
CORRECTO:   encolar → responder de inmediato → procesar aparte
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

Cumplía en el análisis del 2026-08-07 y se volvió a contar: 145 de 320, la más corta del capítulo.

La fila **12** pasa con un ejemplo que trae número —cinco mil correos dentro de la petición—, y eso es lo que la fila pide: el error que se comete de verdad, no uno exagerado.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## R6 · Mide antes de optimizar

Ante lentitud, **mide** (profiler, tiempos, conteo de consultas) para hallar el cuello real, no optimices por corazonada. No sacrifiques legibilidad por micro-optimizaciones sin impacto medible (`07`). Las ineficiencias de arriba (N+1, sin paginar, sin índice) son evidentes y se evitan desde el diseño.

```
INCORRECTO: reescribir "porque parece lento", sin medir, y romper legibilidad
CORRECTO:   medir → localizar el cuello → optimizar ahí → volver a medir
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

Cumplía en el análisis del 2026-08-07, que además anota algo que conviene saber antes de tocarla: **es la regla que [base/20-meta-reglas/estructura-regla.md](20-meta-reglas/estructura-regla.md) usa como modelo** de cómo se escribe un ejemplo mínimo. Editarla es editar el molde que se le enseña a quien escribe una regla nueva.

La fila **9** pasa: medir antes de optimizar y no sacrificar legibilidad son la misma exigencia —no tocar sin evidencia—, y la última frase es su límite, no una tercera: las ineficiencias evidentes no necesitan medición previa porque ya están medidas.

Se volvió a contar: 303 de 320. **Pasa raspando**, y queda dicho para que quien la edite sepa que no hay margen.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

---

Ver: `03` (diseño de esquema), `07` (no sacrificar legibilidad), `00` N5 (masivas).
