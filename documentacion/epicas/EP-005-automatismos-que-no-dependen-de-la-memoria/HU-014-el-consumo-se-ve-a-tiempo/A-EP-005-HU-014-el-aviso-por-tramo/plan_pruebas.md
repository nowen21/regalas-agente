# Plan de Pruebas — Fase A-EP-005-HU-014: el aviso por tramo

**Para qué sirve este documento.** Dice **con qué casos se comprueba** lo construido, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba antes de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el [resultado_pruebas.md](resultado_pruebas.md).

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-005-HU-014 |
| **Versión** | 1.0 |
| **Alcance del plan** | La fase `A-EP-005-HU-014` de la [HU](../HU-014-el-consumo-se-ve-a-tiempo.md) |
| **Fecha** | 2026-08-20 |
| **Elaborado por** | El agente |
| **Aprobado por** | Pendiente: el usuario |
| **Estado** | Borrador |

Una sola fase: van las secciones 3, 5, 6, 9 y 12, como la plantilla indica para una fase chica.

## 3. Estrategia de pruebas

### 3.1 Niveles

| Nivel | Objetivo | Ambiente |
|---|---|---|
| Unitarias | Que el cruce de tramo se decida bien en los límites | Listas de consumos en memoria |
| De enganche | Que el programa lea la transcripción, avise solo al cruzar y salga con 0 | Subproceso con JSON por la entrada estándar |
| Regresión | Que el reporte de cierre y las dos suites sigan iguales | El repositorio |

### 3.2 Técnicas

- **Valores límite**: 999.999, 1.000.000 y 1.000.001; umbral 0.
- **La misma transcripción con un turno más**, para aislar que lo único que cambia es si el último turno cruzó.
- **Entradas rotas**: sin ruta, ruta inexistente, línea ilegible.

### 3.5 Alcance de la ejecución

`validadores/tests/` entera y `validadores/pruebas.py` entera: se tocan `presupuesto.py` e `instalar.py`, que ya tienen casos allá.

## 5. Matriz de trazabilidad

| HU | CA / exigencia | Caso | Estado |
|---|---|---|---|
| HU-014 | [CA-01](../HU-014-el-consumo-se-ve-a-tiempo.md#ca-01--al-terminar-se-reporta-el-consumo-de-la-sesión) | [CP-001](#cp-001--el-reporte-de-cierre-no-cambia) | ☐ |
| HU-014 | [CA-02](../HU-014-el-consumo-se-ve-a-tiempo.md#ca-02--al-cruzar-un-tramo-se-avisa-una-vez) | [CP-002](#cp-002--el-último-turno-cruza-el-millón), [CP-003](#cp-003--un-turno-más-dentro-del-mismo-tramo), [CP-004](#cp-004--el-segundo-millón) | ☐ |
| HU-014 | [CA-03](../HU-014-el-consumo-se-ve-a-tiempo.md#ca-03--sin-transcripción-calla-y-nunca-detiene) | [CP-005](#cp-005--sin-ruta-ruta-inexistente-y-línea-ilegible) | ☐ |
| HU-014 | Límites · igual al tramo, y umbral 0 | [CP-006](#cp-006--exactamente-el-tramo-y-el-umbral-apagado) | ☐ |
| HU-014 | RNF-01 · silencio entre tramos | [CP-003](#cp-003--un-turno-más-dentro-del-mismo-tramo) | ☐ |
| HU-014 | RNF-02 · no se nota | [CP-007](#cp-007--la-transcripción-más-grande-se-lee-rápido) | ☐ |
| HU-014 | No regresión | [CP-008](#cp-008--nada-de-lo-que-ya-estaba-deja-de-pasar) | ☐ |

**Cobertura:** 7 de 7 exigencias con caso = 100%.

## 6. Casos de prueba

### CP-001 — El reporte de cierre no cambia

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Transcripción de dos turnos (100+20 y 50+30 fichas); correr el enganche sin `--modo` | Una línea «Consumo de la sesión: 2 turno(s) · 150 fichas de entrada · 50 de salida · 5 leídas de caché» |
| 2 | Correr con `--modo cierre` | La misma línea |

### CP-002 — El último turno cruza el millón

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Transcripción con turnos que suman 950.000 y uno final de 100.000; `--modo aviso` | Aviso que nombra el tramo 1 y el total 1.050.000 |

### CP-003 — Un turno más, dentro del mismo tramo

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Agregar un turno de 10.000 a la anterior; `--modo aviso` | Sin salida, código 0 |

### CP-004 — El segundo millón

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Agregar turnos hasta 2.050.000; `--modo aviso` | Aviso del tramo 2 |

### CP-005 — Sin ruta, ruta inexistente y línea ilegible

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `--modo aviso` con entrada sin `transcript_path` | Sin salida, código 0 |
| 2 | Con una ruta que no existe | Sin salida, código 0 |
| 3 | Con un archivo que mezcla una línea válida de 1.000.000 y una ilegible | Aviso del tramo 1, código 0 |

### CP-006 — Exactamente el tramo, y el umbral apagado

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `cruzo_tramo` con 999.999 y luego 1.000.000 | Falso, luego verdadero |
| 2 | `cruzo_tramo` con umbral 0 sobre 5.000.000 | Falso: sin umbral no hay aviso |

### CP-007 — La transcripción más grande se lee rápido

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `--modo aviso` sobre la transcripción real más grande de la máquina (3.407 turnos) y medir | Menos de 2 segundos |

### CP-008 — Nada de lo que ya estaba deja de pasar

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `validadores/tests/` entera | Pasa |
| 2 | `validadores/pruebas.py` entera | 365 de 365, incluido `TestPresupuesto` sin cambios |

## 9. Gestión de defectos

| Severidad | Qué sería acá | Atención |
|---|---|---|
| **Crítica** | Que el enganche salga con código distinto de 0 | Inmediato |
| **Alta** | Que avise dos veces en el mismo tramo, o que el reporte de cierre cambie | Antes de cerrar |
| **Media** | La redacción del aviso | Se reporta |

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — 7 de 7 |
| Avisos por tramo cruzado | exactamente 1 |
| Tiempo sobre la transcripción de 3.407 turnos | < 2 s |
| Pruebas del repositorio que dejan de pasar | 0 |

Un solo concepto: **Cumple** o **No cumple**. Se escribe en el resultado, no acá.
