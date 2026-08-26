# Plan de Pruebas — Fase A-EP-005-HU-015: el portero del contenido externo

**Para qué sirve este documento.** Dice **con qué casos se comprueba** lo construido, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba antes de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el [resultado_pruebas.md](resultado_pruebas.md).

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-005-HU-015 |
| **Versión** | 1.0 |
| **Alcance del plan** | La fase `A-EP-005-HU-015` de la [HU](../HU-015-lo-que-llega-de-afuera-llega-marcado.md) |
| **Fecha** | 2026-08-20 |
| **Elaborado por** | El agente |
| **Aprobado por** | Pendiente: el usuario |
| **Estado** | Borrador |

Una sola fase: van las secciones 3, 5, 6, 9 y 12, como la plantilla indica para una fase chica.

## 3. Estrategia de pruebas

### 3.1 Niveles

| Nivel | Objetivo | Ambiente |
|---|---|---|
| Unitarias | Que el módulo decida bien externa / interna y arme el sobre con su origen | Proceso de prueba |
| De enganche | Que el programa del adaptador lea la entrada, devuelva el JSON y salga con 0 | Subproceso con JSON por la entrada estándar |
| De instalación | Que el instalador escriba la fila con su filtro y el checklist la reclame si falta | Proyecto de mentira en carpeta temporal |
| Regresión | Que las dos suites sigan en verde y la de la frontera cuente el enganche nuevo | El repositorio |

### 3.2 Técnicas

- **Partición por herramienta**: una externa de cada clase (web, MCP, archivo de fuera) y las seis internas.
- **El mismo nombre en dos estados**: `Read` dentro y fuera de la raíz, para aislar que la única diferencia es la ruta.
- **Resultado ausente y resultado enorme**: lo que comprueba que el sobre no depende de `tool_response`.

### 3.5 Alcance de la ejecución

`validadores/tests/` entera y `validadores/pruebas.py` entera: se toca `instalar.py`, que las dos cubren. Además `validar.py amarre` y `validar.py estandar`.

## 5. Matriz de trazabilidad

| HU | CA / exigencia | Caso | Estado |
|---|---|---|---|
| HU-015 | [CA-01](../HU-015-lo-que-llega-de-afuera-llega-marcado.md#ca-01--una-página-consultada-llega-con-su-sobre) | [CP-001](#cp-001--la-página-llega-con-su-sobre) | ☐ |
| HU-015 | [CA-02](../HU-015-lo-que-llega-de-afuera-llega-marcado.md#ca-02--lo-que-viene-por-mcp-o-de-un-archivo-de-fuera-también-llega-marcado) | [CP-002](#cp-002--mcp-nombra-servidor-y-herramienta), [CP-003](#cp-003--el-archivo-de-fuera-nombra-su-ruta) | ☐ |
| HU-015 | [CA-03](../HU-015-lo-que-llega-de-afuera-llega-marcado.md#ca-03--lo-de-adentro-calla) | [CP-004](#cp-004--los-seis-silencios), [CP-005](#cp-005--la-entrada-rota-y-la-entrada-sin-argumentos) | ☐ |
| HU-015 | [CA-04](../HU-015-lo-que-llega-de-afuera-llega-marcado.md#ca-04--el-portero-se-instala-solo-y-se-reclama-si-falta) | [CP-006](#cp-006--se-instala-con-su-filtro-y-se-reclama-si-falta) | ☐ |
| HU-015 | RNF-01 · no lee el resultado | [CP-007](#cp-007--el-resultado-no-importa) | ☐ |
| HU-015 | RNF-02 · tres líneas | [CP-001](#cp-001--la-página-llega-con-su-sobre) | ☐ |
| HU-015 | No regresión | [CP-008](#cp-008--nada-de-lo-que-ya-estaba-deja-de-pasar) | ☐ |

**Cobertura:** 7 de 7 exigencias con caso = 100%.

## 6. Casos de prueba

### CP-001 — La página llega con su sobre

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el enganche con `tool_name: WebFetch`, `tool_input.url: https://ejemplo.test/pagina` | Código 0 |
| 2 | Leer la salida como JSON | Tiene `hookSpecificOutput.hookEventName = PostToolUse` y `additionalContext` |
| 3 | Buscar en `additionalContext` | Contiene «WebFetch», «https://ejemplo.test/pagina», «dato» y «C27» |
| 4 | Contar las líneas de `additionalContext` | A lo sumo 3 |
| 5 | Buscar `updatedToolResponse` en la salida | No está |

### CP-002 — MCP nombra servidor y herramienta

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr con `tool_name: mcp__gmail__leer_correo` y `tool_input` cualquiera | Sobre con «gmail» y «leer_correo» |

### CP-003 — El archivo de fuera nombra su ruta

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr con `tool_name: Read`, `file_path` fuera de la `--raiz` | Sobre con esa ruta |

### CP-004 — Los seis silencios

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr con `Read` y `file_path` dentro de la raíz | Sin salida, código 0 |
| 2 | Correr con `Write` | Sin salida, código 0 |
| 3 | Correr con `Edit` | Sin salida, código 0 |
| 4 | Correr con `Bash` | Sin salida, código 0 |
| 5 | Correr con `Glob` | Sin salida, código 0 |
| 6 | Correr con `Grep` | Sin salida, código 0 |

### CP-005 — La entrada rota y la entrada sin argumentos

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr con «esto no es JSON» | Sin salida, código 0 |
| 2 | Correr con `tool_name: WebFetch` y sin `tool_input` | Sobre con «WebFetch» y sin origen, código 0 |
| 3 | Correr con `tool_input` que no es un diccionario | Sobre con «WebFetch», código 0 |

### CP-006 — Se instala con su filtro y se reclama si falta

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Instalar en un proyecto temporal | En `.claude/settings.json` hay un `PostToolUse` con `matcher` que contiene `WebFetch`, `WebSearch`, `Read` y `mcp__.*`, llamando a `hook_externo.py` |
| 2 | Quitar esa entrada y correr el checklist | El aviso nombra `hook_externo.py` |

### CP-007 — El resultado no importa

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr CP-001 sin `tool_response` | El mismo sobre |
| 2 | Correr CP-001 con un `tool_response` de un megabyte | El mismo sobre, en menos de un segundo |

### CP-008 — Nada de lo que ya estaba deja de pasar

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `validadores/tests/` entera | Pasa, incluida la de la frontera con el enganche nuevo |
| 2 | `validadores/pruebas.py` entera | Todo en verde, sobre la línea base del día |
| 3 | `validar.py amarre` y `validar.py estandar` | Sin falla nueva |

## 9. Gestión de defectos

| Severidad | Qué sería acá | Atención |
|---|---|---|
| **Crítica** | Que el enganche modifique o borre el resultado de la herramienta, o que bloquee | Inmediato |
| **Alta** | Que calle con una herramienta externa, o que hable con una interna | Antes de cerrar |
| **Media** | La redacción del sobre | Se reporta |

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — 7 de 7 |
| Sobres falsos sobre los seis silencios | 0 |
| Pruebas del repositorio que dejan de pasar | 0 |

Un solo concepto: **Cumple** o **No cumple**. Se escribe en el resultado, no acá.
