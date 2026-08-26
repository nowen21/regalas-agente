# Plan de Pruebas — Fase C-EP-005-HU-003: el veredicto se copia solo

**Para qué sirve este documento.** Dice **con qué casos se comprueba** lo construido, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba antes de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el [resultado_pruebas.md](resultado_pruebas.md).

| Campo | Valor |
|---|---|
| **Código** | PP-C-EP-005-HU-003 |
| **Versión** | 1.0 |
| **Alcance del plan** | La fase `C-EP-005-HU-003` de la [HU](../HU-003-disparo-al-escribir-un-archivo.md) |
| **Fecha** | 2026-08-20 |
| **Elaborado por** | El agente |
| **Aprobado por** | Pendiente: el usuario |
| **Estado** | Borrador |

Una sola fase: van las secciones 3, 5, 6, 9 y 12, como la plantilla indica para una fase chica.

## 3. Estrategia de pruebas

### 3.1 Niveles

| Nivel | Objetivo | Ambiente |
|---|---|---|
| Unitarias | Que `veredicto.py` lea el §6 y reescriba los tres sitios, y nada más | Carpetas temporales |
| De enganche | Que el programa del adaptador lea la ruta, propague y salga con 0 | Subproceso con JSON por la entrada |
| De comando | Que `cerrar.py` deje la fila «hecho» | Copia temporal del índice |
| Regresión | Las dos suites | El repositorio |

### 3.2 Técnicas

- **Las dos formas del §8** (tres y seis columnas), para aislar que se reescribe la última celda y no una posición fija.
- **El mismo resultado con y sin concepto**, para fijar que el borrador calla.
- **Huella del `estado-fase.md`** antes y después.

### 3.5 Alcance de la ejecución

`validadores/tests/` entera y `validadores/pruebas.py` entera.

## 5. Matriz de trazabilidad

| HU | CA / exigencia | Caso | Estado |
|---|---|---|---|
| HU-003 | [CA-04](../HU-003-disparo-al-escribir-un-archivo.md#ca-04--lo-que-se-deriva-del-veredicto-lo-copia-el-programa) · los tres sitios | [CP-001](#cp-001--cumple-llega-a-los-tres-sitios-con-seis-columnas), [CP-002](#cp-002--no-cumple-llega-igual-con-tres-columnas) | ☐ |
| HU-003 | CA-04 · el borrador calla | [CP-003](#cp-003--sin-concepto-no-se-toca-nada) | ☐ |
| HU-003 | CA-04 · el checkpoint intacto | [CP-004](#cp-004--el-estado-fase-no-cambia) | ☐ |
| HU-003 | CA-04 · la fila «hecho» | [CP-005](#cp-005--cerrar-deja-la-fila-en-forma-de-hecho) | ☐ |
| HU-003 | Límites · otro archivo, fila que no está | [CP-006](#cp-006--lo-que-no-le-toca-y-lo-que-no-encuentra) | ☐ |
| HU-003 | No regresión | [CP-007](#cp-007--nada-de-lo-que-ya-estaba-deja-de-pasar) | ☐ |

**Cobertura:** 6 de 6 exigencias con caso = 100%.

## 6. Casos de prueba

### CP-001 — «Cumple» llega a los tres sitios, con seis columnas

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Historia de prueba con §8 de seis columnas y fila de la fase `A-EP-001-HU-001-p`; README de fase con `**Estado:** …` y README de HU con la fila | Listo |
| 2 | Escribir `resultado_pruebas.md` con `**Concepto** | **Cumple**` y `**CA cumplidos** | 2 de 2`; correr el enganche con esa ruta | Código 0; imprime los tres archivos tocados |
| 3 | Leer la última celda de la fila del §8 | `Cerrada el 2026-08-20: Cumple, 2 de 2 CA` |
| 4 | Leer los dos README | El mismo veredicto |

### CP-002 — «No cumple» llega igual, con tres columnas

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Historia con §8 de tres columnas; resultado con `**Concepto** | **No cumple**` y `1 de 2` | La última celda dice `No cumple, 1 de 2 CA`; las otras dos celdas no cambian |

### CP-003 — Sin concepto no se toca nada

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Resultado con `**Concepto** | Todavía no se ejecutó` | Sin salida; los tres archivos con la misma huella |

### CP-004 — El estado-fase no cambia

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Huella de `estado-fase.md` antes y después de CP-001 | La misma |

### CP-005 — Cerrar deja la fila en forma de hecho

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Copia temporal de `pendientes/` con un pendiente `99-p.md` y su fila `| 99 | **P2** | [t](99-p.md) | q |`; `cerrar.cerrar(raiz, 99, "p", escribir=True)` | La fila empieza por `| ~~99~~ | — | **hecho** → [t](hecho/p.md) |` y conserva la celda «q» |

### CP-006 — Lo que no le toca, y lo que no encuentra

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el enganche con `plan_trabajo.md` | Sin salida, código 0 |
| 2 | Historia sin fila para la fase | Imprime que no encontró la fila; no toca nada; código 0 |

### CP-007 — Nada de lo que ya estaba deja de pasar

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Las dos suites enteras | Pasan |

## 9. Gestión de defectos

| Severidad | Qué sería acá | Atención |
|---|---|---|
| **Crítica** | Que toque el `estado-fase.md` o pise una celda que no es la del estado | Inmediato |
| **Alta** | Que propague un borrador | Antes de cerrar |

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Copias del veredicto a mano por fase cerrada | 0 |
| Veredictos que `validar.py fases` encuentre contradichos | 0 |

Un solo concepto: **Cumple** o **No cumple**. Se escribe en el resultado, no acá.
