# 06 · Rendimiento y eficiencia

> **Capa 2 · agnóstica al stack.** Cómo escribir código que no se degrade con el volumen de datos ni de usuarios. La regla general: **medir antes de optimizar**, pero **no introducir ineficiencias evidentes** que un mínimo de cuidado evita. La capa 3 declara herramientas concretas (motor de caché, profiler, límites).

---

## R1 · Evitar consultas en bucle (problema N+1)

El error de rendimiento más común: ejecutar una consulta por cada elemento de una lista.

- Cargar de antemano las relaciones que se van a usar (**eager loading**), en vez de consultarlas dentro del bucle.
- Al recorrer una colección y acceder a datos relacionados, verificar que no se dispara una consulta por iteración.
- Preferir una consulta con join o un `IN (...)` a N consultas puntuales.

```
INCORRECTO: for (factura in facturas) { imprimir(factura.cliente.nombre) }  // 1 + N consultas
CORRECTO:   cargar facturas con su cliente por adelantado → 1 (o 2) consultas
```

---

## R2 · Nunca cargar en memoria conjuntos sin límite

- Toda lista que se muestra al usuario va **paginada**. No traer "todos los registros" a la vista.
- El procesamiento de grandes volúmenes se hace **por lotes / en streaming** (chunking), no cargando todo el dataset en memoria de una vez.
- Traer **solo las columnas necesarias**, no `SELECT *` cuando se necesitan tres campos.

```
INCORRECTO: cargar los 200.000 registros en una vista y renderizarlos todos
CORRECTO:   paginar (p. ej. 25-50 por página) y consultar solo lo visible

INCORRECTO: recorrer un millón de filas cargándolas todas en memoria
CORRECTO:   procesar por lotes, liberando cada lote antes del siguiente
```

---

## R3 · Índices en lo que se filtra y se ordena

Las columnas por las que se filtra, se une o se ordena con frecuencia llevan **índice** (claves foráneas, fechas, estados, columnas de búsqueda). Un índice de más ralentiza las escrituras; uno de menos convierte una consulta en un escaneo completo. Indexar según el patrón real de consulta, no "por si acaso" en todo. (Diseño de esquema en `03-datos.md` D1.)

```
INCORRECTO: filtrar por una columna de fecha sin índice en una tabla grande → escaneo completo
CORRECTO:   índice en la columna de fecha usada por el filtro
```

---

## R4 · Cachear lo costoso y estable, con invalidación clara

Cachear tiene sentido cuando el cálculo es **caro** y el dato **cambia poco**: catálogos, agregados pesados, resultados de consultas frecuentes e idénticas.

- Definir **cuándo se invalida** la caché desde el diseño: sin estrategia de invalidación, la caché sirve datos viejos y genera bugs difíciles.
- No cachear lo que cambia a cada momento ni lo que es barato de recalcular.
- Invalidar la caché en el evento que cambia el dato de origen (p. ej. al anular un documento que afecta un saldo agregado).

```
INCORRECTO: cachear un saldo y no invalidarlo nunca → el usuario ve un saldo desactualizado
CORRECTO:   cachear el saldo e invalidarlo en el evento que lo modifica
```

---

## R5 · Trabajo pesado fuera del ciclo de petición

Lo que tarda (envío de correos, generación de reportes grandes, llamadas a servicios externos lentos, procesamiento masivo) **no bloquea** la respuesta al usuario: va a un proceso en segundo plano / cola de trabajos. La petición confirma que se encoló y el trabajo se ejecuta aparte.

```
INCORRECTO: generar y enviar 5.000 correos dentro de la petición → timeout y mala UX
CORRECTO:   encolar el envío → responder de inmediato → procesar en segundo plano
```

---

## R6 · Medir antes de optimizar; no adivinar

- Ante una sospecha de lentitud, **medir** (profiler, tiempos, conteo de consultas) para hallar el cuello de botella real, en vez de optimizar por corazonada.
- No sacrificar legibilidad por micro-optimizaciones sin impacto medible (`07-calidad-de-codigo.md`).
- Las ineficiencias de esta sección (N+1, sin paginar, sin índice) son **evidentes** y se evitan desde el diseño; el resto se optimiza con datos en mano.

```
INCORRECTO: reescribir código a mano "porque parece lento", sin medir, y romper legibilidad
CORRECTO:   medir → localizar el cuello de botella → optimizar ese punto → volver a medir
```

---

## Relación con el resto del estándar

- **`03-datos.md`** — el diseño de esquema (índices, normalización) es la base del rendimiento en BD.
- **`07-calidad-de-codigo.md`** — no sacrificar legibilidad por optimizaciones sin impacto medible.
- **Núcleo `00` · N5** — las operaciones masivas, además de eficientes, llevan preview + log + confirmación.
