# Plan de Pruebas — Fase B-EP-005-HU-009: las reglas llegan también al propio estándar

**Para qué sirve este documento.** Dice **con qué casos se comprueba** lo construido, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba antes de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el [resultado_pruebas.md](resultado_pruebas.md).

| Campo | Valor |
|---|---|
| **Código** | PP-B-EP-005-HU-009 |
| **Versión** | 1.0 |
| **Alcance del plan** | La fase `B-EP-005-HU-009` de la [HU](../HU-009-lo-que-rige-cada-frase-llega-puesto.md) |
| **Fecha** | 2026-08-20 |
| **Elaborado por** | El agente |
| **Aprobado por** | Pendiente: el usuario |
| **Estado** | Borrador |

Una sola fase: van las secciones 3, 5, 6, 9 y 12, como la plantilla indica para una fase chica.

## 3. Estrategia de pruebas

### 3.1 Niveles

| Nivel | Objetivo | Ambiente |
|---|---|---|
| De enganche | Que el arranque sobre la carpeta del estándar traiga las reglas, y sobre un heredero siga igual | Subproceso con JSON por la entrada estándar |
| Banco de evals | Que la promesa quede afirmada donde se afirman las demás | `evals/` |
| Regresión | Que las dos suites sigan en verde | El repositorio |
| Manual | Que la siguiente apertura real de sesión lo traiga | El archivo que la herramienta conserva de la apertura |

### 3.2 Técnicas

- **Las dos carpetas, el mismo programa**: el estándar y un heredero temporal, para aislar que lo único que cambia es la rama del estándar.
- **Buscar el bloque y el texto**: no basta la cabecera; se busca también una regla del núcleo dentro del contexto.
- **El tiempo antes y después**, porque el `RNF-03` de la HU dice que el arranque no se vuelve lento.

### 3.5 Alcance de la ejecución

`validadores/tests/` entera, `validadores/pruebas.py` entera y `python evals/correr.py`.

## 5. Matriz de trazabilidad

| HU | CA / exigencia | Caso | Estado |
|---|---|---|---|
| HU-009 | [CA-01](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#ca-01--los-capítulos-que-rigen-cada-frase-llegan-con-su-texto) en el estándar | [CP-001](#cp-001--el-estándar-recibe-el-bloque-de-reglas-y-el-núcleo) | ☐ |
| HU-009 | El estándar sigue recibiendo memoria e histórico | [CP-002](#cp-002--la-memoria-y-el-histórico-siguen-llegando) | ☐ |
| HU-009 | Los herederos no cambian | [CP-003](#cp-003--un-heredero-recibe-lo-mismo-que-antes) | ☐ |
| HU-009 | RNF-03 · el arranque no se vuelve lento | [CP-004](#cp-004--el-tiempo-del-arranque) | ☐ |
| HU-009 | La promesa queda en el banco | [CP-005](#cp-005--el-caso-de-evals) | ☐ |
| HU-009 | La apertura real | [CP-006](#cp-006--la-siguiente-sesión-lo-trae) | ☐ |
| HU-009 | No regresión | [CP-007](#cp-007--nada-de-lo-que-ya-estaba-deja-de-pasar) | ☐ |

**Cobertura:** 7 de 7 exigencias con caso = 100%.

## 6. Casos de prueba

### CP-001 — El estándar recibe el bloque de reglas y el núcleo

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `hook_sesion.py --raiz <RAIZ>` con un JSON de sesión por la entrada | Sale con 0 y la salida es JSON válido |
| 2 | Buscar en `additionalContext` el texto `[REGLAS BASE DEL ESTÁNDAR — CARGADAS, OBLIGATORIAS]` | Está |
| 3 | Buscar `<<< base/00-nucleo-blindado.md >>>` y `## N1 ·` | Están |
| 4 | Buscar `[ARRANQUE DETENIDO` | No está: el gate `F13` no se le aplica al estándar |

### CP-002 — La memoria y el histórico siguen llegando

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | En la misma salida, buscar `[MEMORIA DEL AGENTE` y `[HISTÓRICO DE SESIONES` | Están los dos |

### CP-003 — Un heredero recibe lo mismo que antes

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Carpeta temporal con `proyectos/`; correr el enganche con `--raiz` ahí | Sale con 0, JSON válido, con el bloque de reglas y con la revisión de arranque |
| 2 | Carpeta temporal sin `proyectos/` | Trae solo el gate `F13`, como hoy |

### CP-004 — El tiempo del arranque

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Medir el enganche sobre `RAIZ` con el cambio | Menos de 3 segundos, y no más del doble de lo que tarda sobre el heredero temporal |

### CP-005 — El caso de evals

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `python evals/correr.py` | El caso `arranque-reglas-en-el-estandar` en verde, y los 8 anteriores también |

### CP-006 — La siguiente sesión lo trae

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir una sesión nueva en este repositorio y leer el archivo de apertura que la herramienta conserva | Trae el bloque de reglas. Se anota en el resultado con la fecha |

### CP-007 — Nada de lo que ya estaba deja de pasar

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `validadores/tests/` y `validadores/pruebas.py` enteras | Pasan |

## 9. Gestión de defectos

| Severidad | Qué sería acá | Atención |
|---|---|---|
| **Crítica** | Que un heredero deje de recibir las reglas o la revisión | Inmediato |
| **Alta** | Que el estándar reciba el gate en vez de las reglas | Antes de cerrar |
| **Media** | El texto del docstring | Se reporta |

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — 7 de 7 |
| Aperturas del estándar con el bloque de reglas | de 0 de 30 a 1 de 1 |
| Tiempo del arranque sobre el estándar | < 3 s |
| Pruebas del repositorio que dejan de pasar | 0 |

Un solo concepto: **Cumple** o **No cumple**. Se escribe en el resultado, no acá.
