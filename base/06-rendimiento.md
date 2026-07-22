# 06 · Rendimiento y eficiencia  ·  `[CAPA 2]`

Código que no se degrada con el volumen. Regla general: **mide antes de optimizar**, pero no metas ineficiencias evidentes. La capa 3 declara herramientas (caché, profiler, límites).

---

## R1 · Evita consultas en bucle (N+1)

No ejecutes una consulta por cada elemento de una lista. Carga las relaciones por adelantado (**eager loading**). Prefiere un join o un `IN (...)` a N consultas.

```
INCORRECTO: for (factura in facturas) { imprimir(factura.cliente.nombre) }  // 1 + N
CORRECTO:   cargar facturas con su cliente por adelantado → 1-2 consultas
```

## R2 · Nunca cargues conjuntos sin límite

- Toda lista para el usuario va **paginada**.
- Procesa grandes volúmenes **por lotes** (chunking), no todo en memoria.
- Trae **solo las columnas necesarias**, no `SELECT *` para tres campos.

```
INCORRECTO: cargar 200.000 registros en la vista y renderizarlos todos
CORRECTO:   paginar (25-50 por página) y consultar solo lo visible
```

## R3 · Índices en lo que se filtra y ordena

Las columnas por las que se filtra, une u ordena seguido llevan **índice** (FKs, fechas, estados, búsqueda). Uno de más frena las escrituras; uno de menos vuelve la consulta un escaneo completo. Indexa según el patrón real, no "por si acaso".

```
INCORRECTO: filtrar por fecha sin índice en una tabla grande → escaneo completo
CORRECTO:   índice en la columna de fecha del filtro
```

## R4 · Cachea lo caro y estable, con invalidación clara

Cachea lo **caro** que **cambia poco** (catálogos, agregados pesados, consultas frecuentes idénticas). Define **cuándo se invalida** desde el diseño: sin eso, la caché sirve datos viejos. Invalídala en el evento que cambia el dato de origen.

```
INCORRECTO: cachear un saldo y no invalidarlo nunca
CORRECTO:   cachearlo e invalidarlo en el evento que lo modifica
```

## R5 · Trabajo pesado fuera del ciclo de petición

Lo que tarda (correos, reportes grandes, servicios externos lentos, procesamiento masivo) va a **segundo plano / cola**, no bloquea la respuesta.

```
INCORRECTO: enviar 5.000 correos dentro de la petición → timeout
CORRECTO:   encolar → responder de inmediato → procesar aparte
```

## R6 · Mide antes de optimizar

Ante lentitud, **mide** (profiler, tiempos, conteo de consultas) para hallar el cuello real, no optimices por corazonada. No sacrifiques legibilidad por micro-optimizaciones sin impacto medible (`07`). Las ineficiencias de arriba (N+1, sin paginar, sin índice) son evidentes y se evitan desde el diseño.

```
INCORRECTO: reescribir "porque parece lento", sin medir, y romper legibilidad
CORRECTO:   medir → localizar el cuello → optimizar ahí → volver a medir
```

---

Ver: `03` (diseño de esquema), `07` (no sacrificar legibilidad), `00` N5 (masivas).
