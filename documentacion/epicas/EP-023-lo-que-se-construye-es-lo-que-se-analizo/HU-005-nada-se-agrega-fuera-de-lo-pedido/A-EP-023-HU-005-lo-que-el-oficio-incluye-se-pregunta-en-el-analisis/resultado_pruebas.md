# Resultado de Pruebas · Fase `A-EP-023-HU-005-lo-que-el-oficio-incluye-se-pregunta-en-el-analisis`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si cada criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-023-HU-005-lo-que-el-oficio-incluye-se-pregunta-en-el-analisis` |
| **HU** | [HU-005](../HU-005-nada-se-agrega-fuera-de-lo-pedido.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 2.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-02 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Repositorio del estándar en la máquina local, rama `main`, sobre el commit `16ad8a1` más los cambios de la fase |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 7 | 7 | 7 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

**CA-01 · CP-001: `C30` y `F19` se complementan, y `F19` no choca con `S1`**

**El problema que resuelve:** sin esto, una regla manda agregar y la otra lo prohíbe, y el ejemplo de `F19` prohíbe lo que exige la seguridad.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer `01·C30` y `02·F19` | `F19` pide implementar literal el CA; `C30` dice que lo que el oficio suele incluir no se agrega y se pregunta en el análisis | Así |
| 2 | Buscar un caso que una permita y la otra prohíba | Ninguno | Ninguno |
| 3 | Leer la dependencia de `C30` | «extiende `02·F19`» | Así |
| 4 | Leer qué es lo pedido en `C30` | El CA más lo que exigen las reglas | «el criterio de aceptación más lo que exigen las reglas del estándar» |
| 5 | Leer el ejemplo de `F19` junto a `04·S1` | No prohíbe revisar el permiso en el servidor; checklist sellado de nuevo | El ejemplo es la exportación que nadie pidió; sellado contra v41.0.0 |

**Cómo se verificó que la pareja cumple:** por lectura.

**CA-02 · CP-002: `C14` derogada y `C30` escrita con su molde**

**El problema que resuelve:** sin esto, `C14` seguiría llegando al agente con cada mensaje.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer el encabezado de `C14` | `[DEROGADA en 41.0.0 → ver 01·C30]`, nota y texto debajo | Así |
| 2 | Leer `C30` | Una exigencia, cuerpo corto, «deroga `01·C14`», ejemplo, «Aplica a» y checklist en CUMPLE | Así |
| 3 | Correr `validar.py metareglas` y `checklist` | Sin fallas | `OK: sin incumplimientos` |
| 4 | Correr las pruebas de las derogaciones | Pasan | `test_version_derogaciones`: OK |

**Cómo se verificó que la pareja cumple:** los pasos 1 y 2 por lectura; el 3 y el 4, con los programas.

**CA-02 · CP-003: `C25` y `C15` ya no extienden una regla derogada**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer `C25` | «extiende `01·C4`», debajo de `C4`, checklist sellado de nuevo | Así |
| 2 | Leer `C15` | «extiende `01·C30`», checklist sellado de nuevo | Así |
| 3 | Comparar lo que exigen con la 40.1.0 | Lo mismo | Solo cambió la dependencia |

**CA-02 · CP-004: reglas por tarea, registro y versión**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr `validar.py tareas` | Sin fallas | `OK: sin incumplimientos` |
| 2 | Buscar `C14` y `C30` en `base/reglas-por-tarea/` | `C30` en escribir-documento y cambiar-codigo; `C14` no | `C30` en los dos; ninguna regla `C14` |
| 3 | Leer la lista del capítulo 01 en `reglas-validables.md` | Nombra `C30`, y `C14` derogada | Así |
| 4 | Correr `validar.py version`, `versiones` y `estandar` | Sin fallas; `VERSION` en 41.0.0 | Sin fallas; queda el aviso de siempre: el `CLAUDE.md` de este repositorio no declara versión |
| 5 | Medir las marcas de los archivos tocados | Ninguna nueva | `ID1` bajó de 2 a 0; `F19` y los recuerdos quedaron igual; `01-conducta.md` sumó las de los puntos medios que pide el formato de las dependencias y del sello del checklist |

**CA-03 · CP-005: los recuerdos solo valen dentro del plan aprobado**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer «Corregir el defecto detectado» | Vale solo dentro del plan aprobado; lo de afuera es un hallazgo | Así |
| 2 | Leer «Una instrucción se cumple entera» | Un hallazgo detiene la ejecución | Así |
| 3 | Leer sus líneas en `memory.md` | Dicen lo mismo | Así |

**CA-04 · CP-006: `ID1` rige dentro de lo pedido**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer `ID1` | Dentro de lo pedido, sin citar a `C14` | Así; remite a `C30` |
| 2 | Medir su cuerpo y leer su checklist | Corto; CUMPLE | `metareglas` sin fallas; sellado contra v41.0.0 |

**RNF-06 · CP-007: cada tarea cita su criterio**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr `validar.py flujo` y leer el plan | Ninguna tarea sin su criterio | Sin avisos de tareas sueltas; queda el aviso de que la especificación es la HU |

| Caso | CA | Prioridad (del plan) | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | 2026-10-02 | Lectura | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | 2026-10-02 | Lectura, `metareglas`, `checklist`, pruebas | Aprobado | EV-01, EV-02 | Ninguno |
| CP-003 | CA-02 | Alta | 2026-10-02 | Lectura | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-02 | Alta | 2026-10-02 | `tareas`, `version`, `versiones`, `estandar`, marcas | Aprobado | EV-02 | Ninguno |
| CP-005 | CA-03 | Media | 2026-10-02 | Lectura | Aprobado | EV-03 | Ninguno |
| CP-006 | CA-04 | Alta | 2026-10-02 | Lectura, `metareglas` | Aprobado | EV-01 | Ninguno |
| CP-007 | RNF-06 | Media | 2026-10-02 | `flujo` | Aprobado | EV-02 | Ninguno |

**Correspondencia con el plan:** 7 casos en el plan, 7 acá.

**Qué salió distinto de lo esperado:** en `01-conducta.md` el conteo de marcas subió, por los puntos medios de «deroga · extiende» y de los sellos del checklist. Es el formato que piden `20·M7` y el checklist, igual en todo el capítulo.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que ninguna otra regla cite el ancla vieja de `C14` | Búsqueda en `base/` y `validar.py estandar` | Ninguna; los enlaces resuelven |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU (`CA-0N` · `RNF-0N`) | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002, CP-003, CP-004 | Aprobado | Sí |
| CA-03 | CP-005 | Aprobado | Sí |
| CA-04 | CP-006 | Aprobado | Sí |
| RNF-06 | CP-007 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 5 de 5 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 7 de 7 | Sí |
| Hallazgos al ejecutar | Plan §12.1 | Los que no se podían prever | 0 al ejecutar. Antes de ejecutar salieron el H-5 y el choque de `F19` con `S1`, al escribir el plan; y el H-6, de otra fase | Sí |

**Lo que no se cumplió:** nada.

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los cuatro criterios y el RNF-06 tienen sus casos ejecutados y aprobados.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Las reglas | `base/01-conducta.md`, `ID1` y `F19` |
| EV-02 | Salida de los validadores y las pruebas | Transcripción de la sesión del 2026-10-01 |
| EV-03 | Los recuerdos | `historico-chat/memory/` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-02 | 7 | 0 | Primera ejecución |
