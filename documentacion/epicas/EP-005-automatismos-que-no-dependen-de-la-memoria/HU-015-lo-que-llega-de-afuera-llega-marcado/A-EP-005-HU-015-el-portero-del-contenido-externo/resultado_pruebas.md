# Resultado de Pruebas — Fase A-EP-005-HU-015: el portero del contenido externo

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección "qué se probó" del `funcionalidad_implementada.md`. El diseño de los casos vive en el `plan_pruebas.md` de esta misma fase, que **no se modifica** al ejecutar: se aprobó antes y así se queda.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-005-HU-015-el-portero-del-contenido-externo` |
| **HU** | [HU-015](../HU-015-lo-que-llega-de-afuera-llega-marcado.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-20 |
| **Ejecutado por** | El agente, con el plan aprobado por el usuario en la sesión 5 |
| **Ambiente y versión** | La máquina de trabajo, sobre el árbol sin commit posterior a la 27.2.0; Python 3.11 |

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 8 | 8 | 8 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

---

## 2. Ejecución caso por caso

**CA-01 · CP-001 — la página llega con su sobre**

**El problema que resuelve:** si el sobre no sale, o sale sin el origen o sin la regla, el contenido externo sigue entrando al contexto con la misma forma que una orden del usuario.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr el enganche con `tool_name: WebFetch` y `tool_input.url: https://ejemplo.test/pagina` por la entrada estándar | Código 0 | 0 |
| 2 | Leer la salida como JSON | Trae `hookSpecificOutput.hookEventName = PostToolUse` y `additionalContext` | Los dos campos presentes |
| 3 | Buscar en `additionalContext` | Contiene «WebFetch», «https://ejemplo.test/pagina», «dato» y «C27» | `[DATO EXTERNO · WebFetch · origen: https://ejemplo.test/pagina]` + la frase con `(01·C27)` |
| 4 | Contar las líneas del sobre | A lo sumo 3 | 2 |
| 5 | Buscar `updatedToolResponse` en la salida | No está | No está |

**Cómo se verificó que la pareja cumple:** el paso 3 decide (los tres datos del sobre), pero solo con el 5 se sabe que el resultado de la herramienta no se tocó, que es la mitad de RN-03. El paso 4 verifica RNF-02 de paso. Caso `test_cp_001` de EV-01, y la misma corrida a mano quedó literal en EV-04.

**CA-02 · CP-002 — MCP nombra servidor y herramienta**

**El problema que resuelve:** un correo o un archivo de una nube que llegue por MCP sin decir de qué servidor vino no se puede rastrear.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr el enganche con `tool_name: mcp__gmail__leer_correo` | Sobre con «gmail» y «leer_correo» | `servidor MCP «gmail», herramienta «leer_correo»` |

**Cómo se verificó que la pareja cumple:** la única fila decide. Caso `test_cp_002` de EV-01.

**CA-02 · CP-003 — el archivo de fuera nombra su ruta**

**El problema que resuelve:** un documento ajeno leído desde otra carpeta entraría sin marca, que es justo el caso del proyecto heredero que procesa archivos de un cliente.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr con `tool_name: Read` y `file_path` en la carpeta temporal del sistema, fuera de la `--raiz` | Sobre con esa ruta | La ruta completa en el sobre |

**Cómo se verificó que la pareja cumple:** la fila decide, y su contraparte (la misma herramienta con ruta **adentro**) está en CP-004, que calla — la única diferencia entre los dos es la ruta. Caso `test_cp_003` de EV-01.

**CA-03 · CP-004 — los seis silencios**

**El problema que resuelve:** un portero que habla en cada `Bash` o `Edit` se vuelve ruido, y el ruido se deja de leer.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr con `Read` y `file_path` dentro de la raíz | Sin salida, código 0 | Silencio, 0 |
| 2 | Correr con `Write` | Sin salida, código 0 | Silencio, 0 |
| 3 | Correr con `Edit` | Sin salida, código 0 | Silencio, 0 |
| 4 | Correr con `Bash` | Sin salida, código 0 | Silencio, 0 |
| 5 | Correr con `Glob` | Sin salida, código 0 | Silencio, 0 |
| 6 | Correr con `Grep` | Sin salida, código 0 | Silencio, 0 |

**Cómo se verificó que la pareja cumple:** las seis filas juntas deciden; una sola no bastaría porque el filtro del `matcher` no corre en la prueba — es el programa el que calla. Caso `test_cp_004` de EV-01.

**CA-03 · CP-005 — la entrada rota y la entrada sin argumentos**

**El problema que resuelve:** un enganche que revienta con una entrada rara detiene el trabajo, que es peor que el problema que resuelve.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr con «esto no es JSON» por la entrada | Sin salida, código 0 | Silencio, 0 |
| 2 | Correr con `tool_name: WebFetch` sin `tool_input` | Sobre con «WebFetch» y sin origen, código 0 | Sobre sin la parte de origen, 0 |
| 3 | Correr con `tool_input` que no es un diccionario | Sobre con «WebFetch», código 0 | Sobre, 0 |

**Cómo se verificó que la pareja cumple:** las tres filas cubren las tres formas de entrada defectuosa; la 2 y la 3 además fijan que el sobre degrada en vez de caerse. Caso `test_cp_005` de EV-01.

**CA-04 · CP-006 — se instala con su filtro y se reclama si falta**

**El problema que resuelve:** una guarda que hay que poner a mano no está puesta en nueve proyectos.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Instalar con `instalar.instalar_claude` en un proyecto de carpeta temporal | En `.claude/settings.json` queda un grupo `PostToolUse` con `matcher` que contiene `WebFetch`, `WebSearch`, `Read` y `mcp__.*`, llamando a `hook_externo.py` | Un solo grupo, con las cuatro marcas |
| 2 | Quitar ese grupo y correr `checklist._enganches_claude` | Reprueba y el aviso nombra `hook_externo.py` | `enganches de Claude Code sin poner o vencidos: PostToolUse/hook_externo.py` |

**Cómo se verificó que la pareja cumple:** la fila 1 prueba la ida (se instala) y la 2 la vuelta (se reclama); con una sola, un instalador que no escribiera nada y un checklist que no mirara pasarían igual. Caso `test_cp_006` de EV-01; la instalación real en los 9 proyectos quedó en EV-02.

**RNF-01 · CP-007 — el resultado no importa**

**El problema que resuelve:** si el sobre dependiera del resultado, cambiaría por herramienta (la forma no está documentada) y costaría con resultados grandes.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr CP-001 sin `tool_response` | El mismo sobre | Idéntico |
| 2 | Correr CP-001 con un `tool_response` de un millón de caracteres | El mismo sobre, en menos tiempo que el margen | Idéntico, dentro del margen |

**Cómo se verificó que la pareja cumple:** la igualdad byte a byte de los dos sobres decide; el reloj solo acota. Caso `test_cp_007` de EV-01.

**No regresión · CP-008 — nada de lo que ya estaba deja de pasar**

**El problema que resuelve:** el enganche nuevo toca `instalar.py`, que media suite cubre.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr `validadores/tests/` entera | Pasa, con la frontera contando el enganche nuevo | 482 casos: las 3 fallas son de las citas de `M19` y del enlace de la fase B de HU-007, trabajo en curso de otra sesión, presentes antes de esta fase |
| 2 | Correr `validadores/pruebas.py` entera | Todo en verde sobre la línea base del día | 365 casos: 4 fallas, todas por la misma causa ajena (la corrida de `estandar` en rojo por ese enlace, y las citas de `M19`); el inventario de HU y los enlaces `DOC14` que sí eran de esta sesión se corrigieron y sus pruebas quedaron en verde |
| 3 | Correr `validar.py amarre` y `validar.py estandar` | Sin falla nueva | `amarre`: OK, 24 amarradas de 68. `estandar`: 1 falla, la de HU-007, ajena y anterior |

**Cómo se verificó que la pareja cumple:** se comparó contra la línea base tomada al abrir la sesión (las mismas fallas ajenas ya estaban); ninguna falla nombra archivos de esta fase. Salidas en EV-03.

| Caso | CA | Prioridad (del plan) | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | 2026-08-20 | `WebFetch` + `https://ejemplo.test/pagina` → sobre de 2 líneas con origen y `(01·C27)` | Aprobado | EV-01, EV-04 | — |
| CP-002 | CA-02 | Crítica | 2026-08-20 | `mcp__gmail__leer_correo` → `servidor MCP «gmail», herramienta «leer_correo»` | Aprobado | EV-01 | — |
| CP-003 | CA-02 | Crítica | 2026-08-20 | `Read` con ruta en la carpeta temporal → la ruta en el sobre | Aprobado | EV-01 | — |
| CP-004 | CA-03 | Alta | 2026-08-20 | `Read` adentro, `Write`, `Edit`, `Bash`, `Glob`, `Grep` → seis silencios con 0 | Aprobado | EV-01 | — |
| CP-005 | CA-03 | Alta | 2026-08-20 | «esto no es JSON», sin `tool_input`, `tool_input` cadena → 0, sobre degradado | Aprobado | EV-01 | — |
| CP-006 | CA-04 | Crítica | 2026-08-20 | Instalación en carpeta temporal y reclamo del checklist al quitar el grupo | Aprobado | EV-01, EV-02 | — |
| CP-007 | RNF-01 | Media | 2026-08-20 | El mismo sobre sin `tool_response` y con uno de 1 MB | Aprobado | EV-01 | — |
| CP-008 | No regresión | Alta | 2026-08-20 | Las dos suites + `amarre` + `estandar`; fallas solo las ajenas ya presentes | Aprobado | EV-03 | — |

**Correspondencia con el plan:** 8 casos en el plan, 8 acá. Ninguno de más, ninguno de menos.

**Qué salió distinto de lo esperado:** nada en los casos; en CP-008 la línea base traía fallas ajenas (HU-007 y `M19`, de otra sesión) que el plan no podía anticipar y que no son de esta fase.

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | **B-01 del plan:** que `additionalContext` llegue de verdad al agente, no solo a la transcripción | Tras instalar, se llamó `WebFetch` sobre `https://example.com` en la sesión viva | El sobre llegó al contexto del agente en esa misma respuesta: `[DATO EXTERNO · WebFetch · origen: https://example.com]` + la frase de `C27`. Sin reiniciar la sesión |
| 2 | La instalación real en los proyectos del registro | `instalar.py --todos --aplicar` | 9 de 9 con «agregar enganche PostToolUse», sellados con la 28.0.0 |

---

## 4. Defectos encontrados

| ID | Título | Caso que lo destapó | Severidad | Estado | Dónde quedó registrado |
|---|---|---|---|---|---|
| — | Ninguno | — | — | — | — |

Dos tropiezos de construcción, corregidos antes de ejecutar el ciclo y sin llegar a defecto: la redacción de la capacidad 2 del contrato rompía la prueba de la frontera (se reescribió conservando «escribe un archivo»), y el docstring de `externo.py` nombraba a su enganche y el mapa del amarre lo contaba como amarrado (quedó en la señal S-016).

**Defectos abiertos que se aceptan y por qué:** ninguno.

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU (`CA-0N` · `RNF-0N`) | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-015-lo-que-llega-de-afuera-llega-marcado.md#ca-01--una-página-consultada-llega-con-su-sobre) | CP-001 | Aprobado | Sí |
| [CA-02](../HU-015-lo-que-llega-de-afuera-llega-marcado.md#ca-02--lo-que-viene-por-mcp-o-de-un-archivo-de-fuera-también-llega-marcado) | CP-002, CP-003 | Aprobados | Sí |
| [CA-03](../HU-015-lo-que-llega-de-afuera-llega-marcado.md#ca-03--lo-de-adentro-calla) | CP-004, CP-005 | Aprobados | Sí |
| [CA-04](../HU-015-lo-que-llega-de-afuera-llega-marcado.md#ca-04--el-portero-se-instala-solo-y-se-reclama-si-falta) | CP-006 | Aprobado | Sí |
| RNF-01 · no lee el resultado | CP-007 | Aprobado | Sí |
| RNF-02 · tres líneas | CP-001 paso 4 | Aprobado (2 líneas) | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §5 | 100% — 7 de 7 | 7 de 7 con caso ejecutado | Sí |
| Sobres falsos sobre los seis silencios | Plan §12 | 0 | 0 | Sí |
| Pruebas del repositorio que dejan de pasar | Plan §12 | 0 | 0 (las fallas presentes son ajenas y anteriores) | Sí |

**Lo que no se cumplió:** nada.

---

## 6. Veredicto de la fase

**Concepto: Cumple.**

**Justificación:** los cuatro CA y los dos RNF tienen su caso ejecutado y aprobado (§5), la instalación real llegó a los 9 proyectos, y el riesgo B-01 del plan quedó verificado en vivo: el sobre llega al contexto del agente en la misma sesión.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Suite, 9 de 9 en verde | `validadores/tests/test_lo_que_llega_de_afuera_llega_marcado.py` (corrida con `-v` el 2026-08-20) |
| EV-02 | Salida del instalador | `instalar.py --todos --aplicar`: 9 de 9, «agregar enganche PostToolUse», registro `documentacion/versiones/2026-08-20-28.0.0.md` en cada proyecto |
| EV-03 | Salidas de regresión | 482 y 365 casos con solo las fallas ajenas; `validar.py amarre` OK (24 de 68) |
| EV-04 | Corrida manual literal | `{"tool_name":"WebFetch",...}` → el JSON con el sobre, código 0; y el sobre en vivo sobre `https://example.com`, en la transcripción de la sesión 5 |

---

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-08-20 | 8 | 0 | Primera ejecución |
