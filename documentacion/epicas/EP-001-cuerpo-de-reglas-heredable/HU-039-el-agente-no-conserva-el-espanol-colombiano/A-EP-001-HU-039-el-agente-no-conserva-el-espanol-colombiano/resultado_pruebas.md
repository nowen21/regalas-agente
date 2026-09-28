# Resultado de Pruebas · Fase `A-EP-001-HU-039-el-agente-no-conserva-el-espanol-colombiano`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra qué se ejecutó de verdad y con qué resultado, y de ahí sale el **veredicto** de la fase: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección *Qué se probó* del `funcionalidad_implementada.md`. El diseño de los casos vive en el `plan_pruebas.md` de esta misma fase, que no se modifica al ejecutar: se aprobó antes y así se queda.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-001-HU-039-el-agente-no-conserva-el-espanol-colombiano` |
| **HU** | [HU-039](../HU-039-el-agente-no-conserva-el-espanol-colombiano.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-09-27 |
| **Ejecutado por** | El agente |
| **Ambiente y versión** | El repositorio del estándar, rama `main`, versión 38.2.0 sin commitear |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 8 | 8 | 8 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

**CA-01 · CP-001, que la regla exista y cumpla su molde**

**El problema que resuelve:** una regla mal formada no rige.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir `base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md` | Encabezado en imperativo, cuerpo, ejemplo y checklist en CUMPLE | `## ID12 · Escribe con la norma del español de Colombia`, cuerpo de 278 caracteres leídos, ejemplo y checklist con 19 ✅ y 1 N/A |
| 2 | Abrir `base/00-identidad-y-rol/base.md` | `ID12` en la tabla, con su enlace | Está, después de `ID11` |
| 3 | Correr `python validadores/validar.py metareglas` | 0 fallas | `0 falla(s), 1 aviso(s)`; el aviso es el de `M17` que ya estaba en la línea base |

**Cómo se verificó que la pareja cumple:** el paso 3 decide; los pasos 1 y 2 confirman que lo aceptado es la regla nueva y que está en el índice.

**CA-02 · CP-002, que el cuerpo recoja las reglas de negocio**

**El problema que resuelve:** sin la condición y los cuatro frentes, la regla no dice qué exige ni a quién.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Buscar a qué contenido aplica y con qué condición | Documentos y chat, si el proyecto declara español de Colombia (RN-01) | «Si el proyecto declara español de Colombia» y «en documentos y en el chat» |
| 2 | Buscar los frentes | Los cuatro (RN-02) | «ortografía, léxico, gramática y redacción» |
| 3 | Leer el paréntesis | «extiende `00·ID8`», enlazada | Está, con su enlace |
| 4 | Correr `python validadores/validar.py estandar` | Sin incumplimientos | La primera corrida dio un aviso: en el anexo, la cita `ID8` apuntaba a la lista de marcas. Se corrigió y la segunda dio `OK: sin incumplimientos` |

**Cómo se verificó que la pareja cumple:** los pasos 1 a 3 encuentran el texto literal; el 4 prueba los enlaces.

**CA-03 · CP-003, que el anexo tenga sus cuatro secciones**

**El problema que resuelve:** sin el anexo, la regla pide una norma que no dice cuál es.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir `base/00-identidad-y-rol/espanol-de-colombia.md` | Existe | Existe |
| 2 | Contar sus secciones `##` de contenido | Una por frente | `1 · Ortografía`, `2 · Léxico`, `3 · Gramática`, `4 · Redacción` |
| 3 | Revisar cada sección | Cada una con su tabla | Las cuatro tienen su tabla «No se escribe / Se escribe» |

**Cómo se verificó que la pareja cumple:** los tres pasos dan lo esperado.

**CA-04 · CP-004, que el léxico quede en un solo sitio**

**El problema que resuelve:** con el léxico en dos archivos, las dos copias se desalinean.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Buscar «ordenador» en `marcadores-de-ia.md` | No está | 0 coincidencias |
| 2 | Leer la sección 5 | Una línea que remite al anexo | Remite a `espanol-de-colombia.md`. Además quedan dos filas que son marcas de texto generado y no norma: mezclar *usted* y *tú*, y el español neutro sin giro propio |
| 3 | Leer «Lo que este anexo no cubre» | Ya no dice que la regla no existe; cita `ID10` e `ID12` | 0 coincidencias de «todavía no existe»; cita `ID10`, `ID12` y el anexo |
| 4 | Correr `python validadores/validar.py marcas` | 0 fallas | `0 falla(s)` |

**Cómo se verificó que la pareja cumple:** el paso 1 prueba que la tabla de léxico salió y el 2 que la sección remite. Las dos filas que quedan no son léxico, y lo que el paso esperaba era que no quedara la tabla de léxico.

**CA-05 · CP-005, que el ejemplo falle en los cuatro frentes**

**El problema que resuelve:** un ejemplo que falla en un solo frente enseña solo ese.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Señalar la falta de ortografía | Hay una | *revisara*, sin la tilde de *revisará* |
| 2 | Señalar la falta de léxico | Hay una | *vale*, *fichero*, *ordenador* y el calco *eventualmente* |
| 3 | Señalar la falta de gramática | Hay una | *os* por *les* y *he dejado* por *dejé* |
| 4 | Señalar la falta de redacción | Hay una | «se revisara» no dice quién revisa |
| 5 | Leer el CORRECTO | Ninguna de las cuatro sigue | «Listo, les dejé el archivo en el computador. El equipo lo revisa el viernes.» |

**Cómo se verificó que la pareja cumple:** cada frente tiene su falta señalada en el INCORRECTO y ninguna queda en el CORRECTO.

**CA-06 · CP-006, que la condición deje fuera a otro idioma**

**El problema que resuelve:** sin la condición, la regla obligaría a cualquier proyecto y rompería `20·M3`.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer el comienzo del cuerpo | «Si el proyecto declara español de Colombia» | El cuerpo empieza así |

**Cómo se verificó que la pareja cumple:** el paso encuentra la condición al comienzo.

**CA-07 · CP-007, que quede clasificada como validable en parte**

**El problema que resuelve:** una regla sin clasificar no dice qué se comprueba solo y qué hay que leer.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Buscar `ID12` en `validadores/reglas-validables.md` | Una fila con lo que se cuenta y lo que se lee | La fila `00·ID12` (la parte que se cuenta): *vosotros* y *os* ya los cuenta `redaccion.py`; las tildes, los signos de apertura y el léxico se pueden contar y falta agregarlos a `marcas.py`; la concordancia y el régimen se leen |

**Cómo se verificó que la pareja cumple:** la fila dice las dos partes.

**RNF-01 · CP-008, que el cambio quede versionado**

**El problema que resuelve:** una regla sin versión no se puede adoptar ni rastrear.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir `VERSION` | `38.2.0` | `38.2.0` |
| 2 | Abrir `CHANGELOG.md` | Entrada `38.2.0`, marcada `**MENOR**` | Está, con `**MENOR** (aditivo)` |
| 3 | Correr `python -m unittest -k test_toda_entrada_del_registro_declara_su_tipo validadores/pruebas.py` | OK | OK |

**Cómo se verificó que la pareja cumple:** los tres pasos dan lo esperado.

| Caso | CA | Prioridad (del plan) | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | 2026-09-27 | Archivo de la regla, tabla del capítulo y `metareglas`: 0 fallas | Aprobado | EV-01 | — |
| CP-002 | CA-02 | Crítica | 2026-09-27 | Condición, cuatro frentes y dependencia en el cuerpo; `estandar` sin incumplimientos | Aprobado | EV-01 | DEF-01 |
| CP-003 | CA-03 | Crítica | 2026-09-27 | El anexo con sus cuatro secciones y sus tablas | Aprobado | EV-02 | — |
| CP-004 | CA-04 | Alta | 2026-09-27 | «ordenador» ya no está en `marcadores-de-ia.md`; la sección 5 remite; `marcas` sin fallas | Aprobado | EV-03 | — |
| CP-005 | CA-05 | Alta | 2026-09-27 | Una falta de cada frente señalada en el INCORRECTO; ninguna en el CORRECTO | Aprobado | EV-01 | — |
| CP-006 | CA-06 | Alta | 2026-09-27 | El cuerpo empieza con la condición | Aprobado | EV-01 | — |
| CP-007 | CA-07 | Alta | 2026-09-27 | La fila de `ID12` en `reglas-validables.md`, con sus dos partes | Aprobado | EV-04 | — |
| CP-008 | RNF-01 | Media | 2026-09-27 | `VERSION` en 38.2.0, entrada `**MENOR**`, prueba del tipo en OK | Aprobado | EV-05 | — |

**Correspondencia con el plan:** 8 casos en el plan, 8 aquí.

**Qué salió distinto de lo esperado:** en el CP-002, la primera corrida de `estandar` dio un aviso por una cita mal apuntada en el anexo (DEF-01), corregida en la fase. En el CP-004, la sección 5 conserva dos filas que no son léxico.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que el recordatorio de cada turno incluya `ID11` e `ID12` | Correr `adaptadores/claude-code/hook_reglas.py` con un mensaje de prueba | La salida trae `00·ID11` y `00·ID12` después de `00·ID10` |
| 2 | Que las entradas del léxico se entiendan en todo el país | Lectura del anexo | Ninguna es regionalismo |

## 4. Defectos encontrados

| ID | Título | Caso que lo destapó | Severidad | Estado | Dónde quedó registrado |
|---|---|---|---|---|---|
| DEF-01 | En el anexo, la cita `ID8` apuntaba a `marcadores-de-ia.md` y no al archivo de la regla | CP-002 | Baja | Verificado | Este documento |

**Defectos abiertos que se aceptan y por qué:** ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU (`CA-0N` · `RNF-0N`) | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| CA-04 | CP-004 | Aprobado | Sí |
| CA-05 | CP-005 | Aprobado | Sí |
| CA-06 | CP-006 | Aprobado | Sí |
| CA-07 | CP-007 | Aprobado | Sí |
| RNF-01 | CP-008 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de criterios y requisitos no funcionales | Plan §5 | 100% | 8 de 8 con caso | Sí |
| Fallas de `metareglas` y de `marcas` | Plan §12 | 0 | 0 y 0 | Sí |

**Lo que no se cumplió:** nada.

## 6. Veredicto de la fase

**Concepto:** Cumple

**Justificación:** las ocho exigencias de la HU, CA-01 a CA-07 y RNF-01, cumplen con su caso ejecutado (§5).

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Archivo resultante y salida de `metareglas` y `estandar` | `base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md` |
| EV-02 | Archivo resultante | `base/00-identidad-y-rol/espanol-de-colombia.md` |
| EV-03 | Archivo resultante y salida de `marcas` | `base/00-identidad-y-rol/marcadores-de-ia.md` |
| EV-04 | Archivo resultante | `validadores/reglas-validables.md` |
| EV-05 | Archivos resultantes y prueba | `VERSION`, `CHANGELOG.md` y `test_toda_entrada_del_registro_declara_su_tipo` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-09-27 | 8 | 0 | Primera ejecución |
