# Resultado de Pruebas · Fase `B-EP-001-HU-011-nada-del-proyecto-queda-fuera-del-proyecto`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra qué se ejecutó de verdad y con qué resultado, y de ahí sale el **veredicto** de la fase: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección *Qué se probó* del `funcionalidad_implementada.md`. El diseño de los casos vive en el `plan_pruebas.md` de esta misma fase, que no se modifica al ejecutar: se aprobó antes y así se queda.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-001-HU-011-nada-del-proyecto-queda-fuera-del-proyecto` |
| **HU** | [HU-011](../HU-011-buscar-antes-de-preguntar.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-09-28 |
| **Ejecutado por** | El agente |
| **Ambiente y versión** | El repositorio del estándar, rama `main`, versión 39.1.0 sin commit |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

**CA-04 · CP-001, que la regla exista y cumpla su molde**

**El problema que resuelve:** sin la regla, lo que la herramienta guarda afuera no incumple nada.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Buscar `## C29` en `base/01-conducta.md` | Encabezado en imperativo | Línea 939: `## C29 · Guarda dentro del repositorio todo lo del agente y del proyecto` |
| 2 | Leer su cuerpo | Lo que pide RN-06, en una sola exigencia | Todo lo del agente o del proyecto vive en el repositorio y se llega por enlace; lo que la herramienta guarda afuera se corrige en su origen y no se lee de allá |
| 3 | Buscar el enlace a `04·S9` | Está, con el límite de leer afuera | «Leer afuera vale solo para lo que no es del proyecto; escribir afuera lo cubre `04·S9`», enlazada |
| 4 | Leer su ejemplo y la línea de quién la hace cumplir | INCORRECTO real, CORRECTO que lo resuelve, y la línea con su motivo | INCORRECTO: el arranque entrega las reglas, la herramienta las guarda en su almacén y el agente las lee de allá. CORRECTO: el arranque entrega enlaces. La línea «Nadie la hace cumplir» nombra las dos partes que sí tienen quien las cuide |
| 5 | Leer su checklist y buscar `C29` en `validadores/reglas-validables.md` | CUMPLE; registrada | CUMPLE, 17 ✅ y 3 N/A. Registrada en la lista del capítulo 01 y en la nota del conteo |
| 6 | Correr `python validadores/validar.py metareglas` y `python validadores/validar.py estandar` | Sin incumplimientos | `OK: sin incumplimientos` en los dos. La primera corrida de `metareglas` reportó que faltaba el registro y que el cuerpo medía 583: se corrigieron (DEF-01 y DEF-02) |

**Cómo se verificó que la pareja cumple:** el paso 6 decide el molde; los pasos 2 y 3 comprueban lo que pide RN-06, que un validador no lee.

**CA-04 · CP-002, que `C19` la extienda y siga cumpliendo**

**El problema que resuelve:** si `C19` no la declara, las dos reglas se leen como sueltas; si al declararla se sale del molde, reprueba.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer el cuerpo de `C19` | «extiende `01·C29`», enlazada, y la misma exigencia sobre la memoria | Está al final del primer párrafo, enlazada. Sigue pidiendo un archivo por recuerdo en `historico-chat/memory/` y el almacén de la herramienta vacío |
| 2 | Contar los caracteres de su cuerpo | 320 o menos | 314, medido con `Regla.largo()` de `metareglas.py`. En la primera medición dio 341 y después 329: se acortó dos veces (DEF-03) |
| 3 | Leer su checklist | Del 2026-09-28, en CUMPLE, fila 14 en ✅ | CUMPLE contra v39.0.0, 19 ✅ y 1 N/A, filas 14 y 15 en ✅ |

**Cómo se verificó que la pareja cumple:** los tres pasos dan lo esperado; el 2 es el que decidía el riesgo B-01 del plan.

**RNF · CP-003, que el cambio quede versionado y el recuerdo anotado**

**El problema que resuelve:** una regla sin versión no se puede adoptar ni rastrear.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir `VERSION` | `39.1.0` | `39.1.0` |
| 2 | Abrir `CHANGELOG.md` | Entrada `39.1.0`, `**MENOR**`, en palabras llanas | Está. Sus dos primeros párrafos no tienen rutas, identificadores ni palabras internas |
| 3 | Correr `python validadores/validar.py versionado` y `python -m unittest test_la_entrada_del_registro_se_entiende` desde `validadores/tests` | 0 fallas y OK | `0 falla(s), 1 aviso(s)`, el aviso de la 15.4.0 que ya estaba; la prueba dio OK |
| 4 | Abrir `historico-chat/memory/nada-del-proyecto-queda-en-la-herramienta.md` | Dice que subió a regla `01·C29` | Tiene el párrafo «El 2026-09-28 subió a regla», con el enlace; el resto sigue igual |

**Cómo se verificó que la pareja cumple:** los cuatro pasos dan lo esperado.

| Caso | CA | Prioridad (del plan) | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-04 | Crítica | 2026-09-28 | `C29` en la línea 939, cuerpo de 294 caracteres, enlace a `S9`, checklist en CUMPLE, registrada; `metareglas` y `estandar` sin incumplimientos | Aprobado | EV-01 | DEF-01, DEF-02 |
| CP-002 | CA-04 | Alta | 2026-09-28 | `C19` extiende `C29`, cuerpo de 314 caracteres, checklist del 2026-09-28 en CUMPLE | Aprobado | EV-01 | DEF-03 |
| CP-003 | RNF | Media | 2026-09-28 | `VERSION` en 39.1.0, entrada `**MENOR**`, `versionado` sin fallas, prueba del registro en OK, recuerdo con su párrafo | Aprobado | EV-02 | — |

**Correspondencia con el plan:** 3 casos en el plan, 3 aquí.

**Qué salió distinto de lo esperado:** en el CP-001, la primera corrida de `metareglas` dio una falla (faltaba el registro, que era la T-02 sin hacer todavía) y un aviso (el cuerpo contaba la línea de quién la hace cumplir). En el CP-002, `C19` se pasó del molde dos veces antes de caber.

## 3. Verificaciones manuales  ·  `08·T4`

Ninguna.

## 4. Defectos encontrados

| ID | Título | Caso que lo destapó | Severidad | Estado | Dónde quedó registrado |
|---|---|---|---|---|---|
| DEF-01 | `C29` sin registrar en `reglas-validables.md` | CP-001 | Baja | Verificado | Este documento |
| DEF-02 | La línea de quién la hace cumplir decía «Nadie la hace cumplir entera», y el validador solo la saca del cuerpo con la forma exacta | CP-001 | Baja | Verificado | Este documento |
| DEF-03 | `C19` se pasaba del molde con la dependencia: 341 y después 329 caracteres | CP-002 | Media | Verificado | Este documento |

**Defectos abiertos que se aceptan y por qué:** ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU (`CA-0N` · `RNF-0N`) | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-04 | CP-001, CP-002 | Aprobado | Sí |
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

**Justificación:** el CA-04 y el requisito de versionado cumplen con sus casos ejecutados (§5). Los tres defectos se corrigieron dentro de la fase.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Archivo resultante y salida de `metareglas` y `estandar` | `base/01-conducta.md` y `validadores/reglas-validables.md` |
| EV-02 | Archivos resultantes y prueba | `VERSION`, `CHANGELOG.md`, `historico-chat/memory/nada-del-proyecto-queda-en-la-herramienta.md` y `test_la_entrada_del_registro_se_entiende` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-09-28 | 3 | 0 | Primera ejecución |
