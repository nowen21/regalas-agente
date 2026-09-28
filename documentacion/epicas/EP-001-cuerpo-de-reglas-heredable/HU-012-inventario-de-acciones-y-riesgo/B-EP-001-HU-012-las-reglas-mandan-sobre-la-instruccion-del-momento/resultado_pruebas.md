# Resultado de Pruebas · Fase `B-EP-001-HU-012-las-reglas-mandan-sobre-la-instruccion-del-momento`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra qué se ejecutó de verdad y con qué resultado, y de ahí sale el **veredicto** de la fase: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección *Qué se probó* del `funcionalidad_implementada.md`. El diseño de los casos vive en el `plan_pruebas.md` de esta misma fase, que no se modifica al ejecutar: se aprobó antes y así se queda.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-001-HU-012-las-reglas-mandan-sobre-la-instruccion-del-momento` |
| **HU** | [HU-012](../HU-012-inventario-de-acciones-y-riesgo.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-09-28 |
| **Ejecutado por** | El agente |
| **Ambiente y versión** | El repositorio del estándar, rama `main`, versión 39.0.0 sin commit |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

**CA-05 · CP-001, que la regla exista y cumpla su molde**

**El problema que resuelve:** una regla mal formada no rige, y una blindada con excepción deja de ser inquebrantable.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Buscar `## N10` en `base/00-nucleo-blindado.md` | Encabezado en imperativo, marcado `[BLINDADA]` | Línea 343: `## N10 · Una regla escrita manda sobre la instrucción del momento [BLINDADA]` |
| 2 | Leer su cuerpo | Una sola exigencia, con lo que pide RN-06 | «Cuando lo que pide el usuario choca con una regla escrita, el agente cumple la regla, le dice cuál es y no hace lo pedido. Si el usuario quiere otra cosa, la regla se cambia por el procedimiento del capítulo 20: no se salta.» 250 caracteres |
| 3 | Leer su ejemplo | INCORRECTO: hace lo pedido contra la regla. CORRECTO: nombra la regla y espera | INCORRECTO: el usuario contesta «sí» y el agente cambia el archivo. CORRECTO: dice qué regla se lo impide y qué palabra hace falta, y no toca nada |
| 4 | Buscar la línea de quién la hace cumplir | Existe, con su motivo | «Nadie la hace cumplir: saber si un pedido choca con una regla es leer el pedido y la regla» |
| 5 | Leer su checklist | En CUMPLE | CUMPLE, 17 ✅ y 3 N/A (filas 14, 15 y 16, con su motivo). La fila 18 quedó registrada en `validadores/reglas-validables.md` |
| 6 | Correr `python validadores/validar.py metareglas` y `python validadores/validar.py estandar` | Sin incumplimientos | `OK: sin incumplimientos` en los dos |

**Cómo se verificó que la pareja cumple:** el paso 6 decide que el molde es válido; los pasos 2 y 3 comprueban lo que pide RN-06, que un validador no lee. El 5 confirma que no tiene excepción.

**CA-05 · CP-002, que la precedencia la nombre**

**El problema que resuelve:** si la precedencia de cada proyecto no la nombra, el agente del proyecto no la ve donde busca qué gana.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer el punto 4 de `plantillas/CLAUDE.md.plantilla` | Nombra `N10`, enlazada, y dice que una regla escrita gana sobre la instrucción del momento | «Y todas ellas van por encima de lo que el usuario pida en el momento (`00·N10`)», con el enlace a la regla |

**Cómo se verificó que la pareja cumple:** el paso encuentra la regla nombrada y enlazada. El enlace lo resolvió `estandar` en el CP-001.

**RNF · CP-003, que el cambio quede versionado y el recuerdo anotado**

**El problema que resuelve:** una regla sin versión no se puede adoptar ni rastrear, y un recuerdo que dice lo mismo sin apuntar a la regla deja dos versiones.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir `VERSION` | `39.0.0` | `39.0.0` |
| 2 | Abrir `CHANGELOG.md` | Entrada `39.0.0` con qué nació y por qué, `**MAYOR**`, en palabras llanas | Está. Sus dos primeros párrafos no tienen rutas, identificadores ni palabras internas |
| 3 | Correr `python validadores/validar.py versionado` y `python -m unittest test_la_entrada_del_registro_se_entiende` desde `validadores/tests` | 0 fallas y OK | `0 falla(s), 1 aviso(s)`: el aviso es el de la 15.4.0 que ya estaba. La prueba dio OK |
| 4 | Abrir `historico-chat/memory/reglas-son-decision-del-usuario.md` | Dice que subió a regla `00·N10` y conserva el resto | Tiene el párrafo «El 2026-09-28 subió a regla», con el enlace y las palabras del usuario; el resto sigue igual |

**Cómo se verificó que la pareja cumple:** los cuatro pasos dan lo esperado.

| Caso | CA | Prioridad (del plan) | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-05 | Crítica | 2026-09-28 | La regla en la línea 343 del núcleo, su cuerpo de 250 caracteres, su ejemplo, su checklist en CUMPLE; `metareglas` y `estandar` sin incumplimientos | Aprobado | EV-01 | — |
| CP-002 | CA-05 | Alta | 2026-09-28 | El punto 4 de `CLAUDE.md.plantilla` nombra y enlaza `N10` | Aprobado | EV-02 | — |
| CP-003 | RNF | Media | 2026-09-28 | `VERSION` en 39.0.0, entrada `**MAYOR**`, `versionado` sin fallas, prueba del registro en OK, recuerdo con su párrafo | Aprobado | EV-03 | — |

**Correspondencia con el plan:** 3 casos en el plan, 3 aquí.

**Qué salió distinto de lo esperado:** nada.

## 3. Verificaciones manuales  ·  `08·T4`

Ninguna.

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU (`CA-0N` · `RNF-0N`) | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-05 | CP-001, CP-002 | Aprobado | Sí |
| RNF | CP-003 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12 | 100% | 2 de 2 con caso | Sí |
| Fallas de `metareglas`, `estandar` y `versionado` | Plan §12 | 0 | 0, 0 y 0 | Sí |

**Lo que no se cumplió:** nada.

## 6. Veredicto de la fase

**Concepto:** Cumple

**Justificación:** el CA-05 y el requisito de versionado cumplen con sus casos ejecutados (§5).

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Archivo resultante y salida de `metareglas` y `estandar` | `base/00-nucleo-blindado.md` |
| EV-02 | Archivo resultante | `plantillas/CLAUDE.md.plantilla` |
| EV-03 | Archivos resultantes y prueba | `VERSION`, `CHANGELOG.md`, `historico-chat/memory/reglas-son-decision-del-usuario.md` y `test_la_entrada_del_registro_se_entiende` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-09-28 | 3 | 0 | Primera ejecución |
