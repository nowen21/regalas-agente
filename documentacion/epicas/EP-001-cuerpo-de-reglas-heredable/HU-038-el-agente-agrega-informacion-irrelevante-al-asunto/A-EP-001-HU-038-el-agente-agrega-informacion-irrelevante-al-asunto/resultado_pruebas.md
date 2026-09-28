# Resultado de Pruebas · Fase `A-EP-001-HU-038-el-agente-agrega-informacion-irrelevante-al-asunto`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra qué se ejecutó de verdad y con qué resultado, y de ahí sale el **veredicto** de la fase: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección *Qué se probó* del `funcionalidad_implementada.md`. El diseño de los casos vive en el `plan_pruebas.md` de esta misma fase, que no se modifica al ejecutar: se aprobó antes y así se queda.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-001-HU-038-el-agente-agrega-informacion-irrelevante-al-asunto` |
| **HU** | [HU-038](../HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-09-27 |
| **Ejecutado por** | El agente |
| **Ambiente y versión** | El repositorio del estándar, rama `main`, versión 38.1.0 sin commitear |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 5 | 5 | 5 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

**CA-01 · CP-001, que la regla exista y cumpla su molde**

**El problema que resuelve:** una regla mal formada no rige; el validador no la ve o la lee a medias.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir `base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md` | Tiene encabezado, cuerpo, ejemplo INCORRECTO/CORRECTO y checklist en CUMPLE | Tiene `## ID11 · Escribe solo lo pertinente al asunto`, el cuerpo, el ejemplo y el checklist con 19 ✅ y 1 N/A |
| 2 | Abrir `base/00-identidad-y-rol/base.md` | `ID11` está en la tabla, con su enlace | Está en la fila siguiente a `ID10`, con el enlace al archivo |
| 3 | Correr `python validadores/validar.py metareglas` | 0 fallas | `0 falla(s), 1 aviso(s)`. El aviso es el de `M17` sobre la entrada 38.0.3, que ya estaba en la línea base |

**Cómo se verificó que la pareja cumple:** el paso 3 decide; los pasos 1 y 2 confirman que lo que el validador acepta es la regla nueva y que está en el índice.

**CA-02 · CP-002, que el cuerpo recoja las cuatro reglas de negocio**

**El problema que resuelve:** si el cuerpo no dice contra qué se mide la pertinencia, cada lector la juzga a su gusto.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Buscar en el cuerpo a qué contenido aplica | Documentos y chat (RN-01) | «en documentos y en el chat» |
| 2 | Buscar contra qué se mide la pertinencia | Tema, objetivo y alcance (RN-02) | «el tema, el objetivo y el alcance de lo que se trata» |
| 3 | Buscar qué pasa con lo no pertinente | Se omite aunque sea breve, claro y correcto (RN-03) | «se omite aunque sea breve, claro y correcto» |
| 4 | Leer el cuerpo y el ejemplo buscando la relación con la extensión | Un texto corto también puede incumplirla (RN-04) | «Ser corto no lo vuelve pertinente», y el ejemplo INCORRECTO es una frase corta |

**Cómo se verificó que la pareja cumple:** cada paso encuentra el texto literal de su RN en el cuerpo.

**CA-03 · CP-003, que la dependencia esté declarada y resuelva**

**El problema que resuelve:** sin la dependencia, la regla se lee como si reemplazara a `ID9`, y las dos dejan de sumarse.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer el paréntesis del cuerpo | `extiende` con `00·ID7`, `00·ID8` y `00·ID9`, enlazadas | «(extiende `00·ID7`, `00·ID8` y `00·ID9`)», las tres con enlace |
| 2 | Correr `python validadores/validar.py estandar` | Sin incumplimientos | La primera corrida dio 1 aviso: la cita `C5` del checklist sin enlace. Se enlazó y la segunda dio `OK: sin incumplimientos` |

**Cómo se verificó que la pareja cumple:** el paso 2 prueba que los tres enlaces resuelven; el aviso era del checklist, no del cuerpo, y quedó corregido en la misma fase.

**CA-04 · CP-004, que quede clasificada como no validable**

**El problema que resuelve:** una regla sin clasificar no dice si alguien la comprueba, y `M9` la reprueba.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Buscar `ID11` en `validadores/reglas-validables.md` | Entre las no validables del capítulo 00, con su motivo | En la línea del capítulo 00: «ID9, ID11», y la frase «`ID11` ... tampoco: decidir si un dato sirve al tema, al objetivo y al alcance de lo que se trata pide leerlo» |

**Cómo se verificó que la pareja cumple:** el paso 1 encuentra la clasificación y su motivo; `metareglas` dejó de reportar la falla de `M9` que dio antes de clasificarla.

**RNF-01 · CP-005, que el cambio quede versionado**

**El problema que resuelve:** una regla nueva sin versión no se puede adoptar ni rastrear.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir `VERSION` | `38.1.0` | `38.1.0` |
| 2 | Abrir `CHANGELOG.md` | Entrada `38.1.0` con qué nació y por qué, marcada `**MENOR**` | La entrada está, con `**MENOR** (aditivo)`, y la prueba `test_toda_entrada_del_registro_declara_su_tipo` dio OK |

**Cómo se verificó que la pareja cumple:** los dos pasos encuentran lo esperado, y la prueba automática confirma el formato del tipo.

| Caso | CA | Prioridad (del plan) | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | 2026-09-27 | El archivo de la regla, la tabla del capítulo y `metareglas`: 0 fallas | Aprobado | EV-01 | — |
| CP-002 | CA-02 | Crítica | 2026-09-27 | Las cuatro RN encontradas con su texto literal en el cuerpo | Aprobado | EV-01 | — |
| CP-003 | CA-03 | Alta | 2026-09-27 | El paréntesis con las tres reglas enlazadas y `estandar`: sin incumplimientos | Aprobado | EV-02 | DEF-01 |
| CP-004 | CA-04 | Alta | 2026-09-27 | `ID11` en la lista de no validables del capítulo 00, con su motivo | Aprobado | EV-03 | — |
| CP-005 | RNF-01 | Media | 2026-09-27 | `VERSION` en 38.1.0, entrada `**MENOR**` y su prueba en OK | Aprobado | EV-04 | — |

**Correspondencia con el plan:** 5 casos en el plan, 5 aquí.

**Qué salió distinto de lo esperado:** en el CP-003, la primera corrida de `estandar` dio un aviso por la cita `C5` sin enlace en el checklist; se corrigió en la misma fase (DEF-01).

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que las cuatro RN estén en el cuerpo | Lectura del cuerpo, CP-002 | Están |

## 4. Defectos encontrados

| ID | Título | Caso que lo destapó | Severidad | Estado | Dónde quedó registrado |
|---|---|---|---|---|---|
| DEF-01 | La cita `01·C5` del checklist de `ID11` sin enlace | CP-003 | Baja | Verificado | Este documento |

**Defectos abiertos que se aceptan y por qué:** ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU (`CA-0N` · `RNF-0N`) | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| CA-04 | CP-004 | Aprobado | Sí |
| RNF-01 | CP-005 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de criterios y requisitos no funcionales | Plan §5 | 100% | 5 de 5 con caso | Sí |
| Fallas de `metareglas` | Plan §12 | 0 | 0 | Sí |

**Lo que no se cumplió:** nada de las metas del plan.

## 6. Veredicto de la fase

**Concepto:** Cumple

**Justificación:** las cinco exigencias de la HU, CA-01 a CA-04 y RNF-01, cumplen con su caso ejecutado (§5).

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Archivo resultante y salida de `metareglas` | `base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md` |
| EV-02 | Salida de `validar.py estandar` | Esta ejecución, 2026-09-27 |
| EV-03 | Archivo resultante | `validadores/reglas-validables.md` |
| EV-04 | Archivos resultantes y prueba | `VERSION`, `CHANGELOG.md` y `test_toda_entrada_del_registro_declara_su_tipo` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-09-27 | 5 | 0 | Primera ejecución |
