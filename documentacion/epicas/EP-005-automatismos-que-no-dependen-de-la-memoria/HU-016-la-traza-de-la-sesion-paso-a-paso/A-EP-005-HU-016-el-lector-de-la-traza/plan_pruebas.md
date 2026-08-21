# Plan de Pruebas — Fase A-EP-005-HU-016: el lector de la traza

**Para qué sirve este documento.** Dice **con qué casos se comprueba** lo construido, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba antes de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el [resultado_pruebas.md](resultado_pruebas.md).

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-005-HU-016 |
| **Versión** | 1.0 |
| **Alcance del plan** | La fase `A-EP-005-HU-016` de la [HU](../HU-016-la-traza-de-la-sesion-paso-a-paso.md) |
| **Fecha** | 2026-08-20 |
| **Elaborado por** | El agente |
| **Aprobado por** | Pendiente: el usuario |
| **Estado** | Borrador |

Una sola fase: van las secciones 3, 5, 6, 9 y 12, como la plantilla indica para una fase chica.

## 3. Estrategia de pruebas

### 3.1 Niveles

| Nivel | Objetivo | Ambiente |
|---|---|---|
| Unitarias | Que el lector empareje, recorte, mida y cierre bien | Transcripciones sintéticas en carpetas temporales |
| De escritura | Que `--escribir` deje el archivo con el nombre del histórico y lo indexe una vez | Proyecto de mentira con `historico-chat/` |
| Sobre datos reales | Que una transcripción de este repositorio se trace entera en menos de 2 segundos | El repositorio |
| Regresión | Que las dos suites y `amarre` sigan en verde | El repositorio |

### 3.2 Técnicas

- **Marcas de tiempo fijas** en la sintética: las duraciones esperadas se conocen de antemano.
- **Un caso por rareza**: ilegible, sin respuesta, vacío, inexistente, cada uno aislado.
- **Búsqueda negativa**: el contenido de los `tool_result` lleva una palabra centinela que no debe aparecer en la salida.

### 3.5 Alcance de la ejecución

`validadores/tests/` entera y `validadores/pruebas.py` entera: se tocan `validar.py` e `historico.py`, que las dos cubren. Además `validar.py amarre`.

## 5. Matriz de trazabilidad

| HU | CA / exigencia | Caso | Estado |
|---|---|---|---|
| HU-016 | [CA-01](../HU-016-la-traza-de-la-sesion-paso-a-paso.md#ca-01--la-línea-de-tiempo-de-una-sesión) | [CP-001](#cp-001--tres-pasos-uno-con-error) | ☐ |
| HU-016 | [CA-02](../HU-016-la-traza-de-la-sesion-paso-a-paso.md#ca-02--el-cierre-dice-los-totales) | [CP-002](#cp-002--el-cierre) | ☐ |
| HU-016 | [CA-03](../HU-016-la-traza-de-la-sesion-paso-a-paso.md#ca-03--con---escribir-queda-junto-al-histórico-indexada) | [CP-003](#cp-003--escribe-junto-al-histórico-e-indexa-una-vez), [CP-004](#cp-004--sin-histórico-no-inventa) | ☐ |
| HU-016 | [CA-04](../HU-016-la-traza-de-la-sesion-paso-a-paso.md#ca-04--lo-raro-no-revienta) | [CP-005](#cp-005--lo-raro) | ☐ |
| HU-016 | RNF-01 · 1 MB en menos de 2 s | [CP-006](#cp-006--una-sesión-real) | ☐ |
| HU-016 | RNF-02 · privacidad | [CP-001](#cp-001--tres-pasos-uno-con-error) paso 4 | ☐ |
| HU-016 | No regresión | [CP-007](#cp-007--nada-de-lo-que-ya-estaba-deja-de-pasar) | ☐ |

**Cobertura:** 7 de 7 exigencias con caso = 100%.

## 6. Casos de prueba

### CP-001 — Tres pasos, uno con error

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir una transcripción con `Read`, `Bash` (`is_error: true`) y `WebFetch`, con respuestas a 2, 5 y 1 segundos, y la palabra `CENTINELA` dentro de cada `tool_result` | El archivo existe |
| 2 | Correr `validar.py traza <archivo>` | Código 0 |
| 3 | Leer las filas | Tres, numeradas 1-3, con hora, herramienta, entrada recortada, `2 s`, `5 s`, `1 s`, y la fila 2 con `error` |
| 4 | Buscar `CENTINELA` en la salida | No aparece |

### CP-002 — El cierre

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer las últimas líneas de CP-001 | «3 pasos», «1 error», `Read 1 · Bash 1 · WebFetch 1`, el más lento `Bash (5 s)`, duración total entre el primer `tool_use` y el último `tool_result` |

### CP-003 — Escribe junto al histórico e indexa una vez

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Crear `historico-chat/2026-08-20-sesion.md` con `<!-- sesion: abc -->` y la transcripción `abc.jsonl` con `sessionId: abc` | Los dos existen |
| 2 | Correr con `--escribir --raiz <carpeta>` | Existe `historico-chat/trazas/2026-08-20-sesion.md` con las filas; `trazas/README.md` lo enlaza con la ruta desde la raíz |
| 3 | Correr de nuevo | El archivo se reescribe; el README tiene una sola línea para él |

### CP-004 — Sin histórico no inventa

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr con `--escribir` sobre una carpeta sin `historico-chat/` | Una frase que lo dice, código 1, nada escrito |
| 2 | Correr con `historico-chat/` pero sin ningún archivo con la marca de esa sesión | Una frase que lo dice, código 1, nada escrito |

### CP-005 — Lo raro

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Una línea «esto no es JSON» entre pasos válidos | La traza sale igual |
| 2 | Un `tool_use` sin `tool_result` | Fila con `sin respuesta` y duración vacía |
| 3 | Archivo vacío | Una frase, código 1 |
| 4 | Ruta inexistente | Una frase, código 1, sin traza de error de Python |

### CP-006 — Una sesión real

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr sobre la transcripción de esta sesión (≈1 MB) midiendo el tiempo | Menos de 2 segundos |
| 2 | Contar los `tool_use` del archivo con un conteo directo | El mismo número que «pasos» en el cierre |

### CP-007 — Nada de lo que ya estaba deja de pasar

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `validadores/tests/` entera | Pasa |
| 2 | `validadores/pruebas.py` entera | Todo en verde |
| 3 | `validar.py amarre` | `traza.py` no aparece como amarrado |

## 9. Gestión de defectos

| Severidad | Qué sería acá | Atención |
|---|---|---|
| **Crítica** | Que copie el contenido de un resultado a la traza | Inmediato |
| **Alta** | Que empareje mal y atribuya un error al paso equivocado, o que reviente con una línea rara | Antes de cerrar |
| **Media** | El formato de la fila | Se reporta |

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — 7 de 7 |
| Fragmentos de resultado en la salida | 0 |
| Pruebas del repositorio que dejan de pasar | 0 |

Un solo concepto: **Cumple** o **No cumple**. Se escribe en el resultado, no acá.
