# Resultado de Pruebas · Fase `C-EP-023-HU-001-el-analisis-principal-de-cimiento`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `C-EP-023-HU-001-el-analisis-principal-de-cimiento` |
| **HU** | [HU-001](../HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-02 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Repositorio del estándar en la máquina local, rama `main`, sobre el commit `a0b83ae` más los cambios de la fase |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

**CA-08 · CP-001: el análisis principal está en `analisis/` y se basa en todo el proyecto**

**El problema que resuelve:** sin esto, ningún documento dice lo que se construye hoy, y los análisis individuales no tienen a dónde llevar lo que deciden.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir `analisis/proyecto-2026-10-02-analisis-principal.md` | Existe | Existe |
| 2 | Leer qué dice de Cimiento y de lo que se construye | Enlaza el planteamiento y el índice de épicas, sin copiarlos | Los enlaza; de cada uno dice una frase |
| 3 | Buscar el análisis 1 del pendiente 103 | Está enlazado | Está, en la primera fila de la lista de cambios |

**Cómo se verificó que la pareja cumple:** los tres pasos, por lectura.

**CA-08 · CP-002: lleva su lista de cambios**

**El problema que resuelve:** sin la lista, no se sabe por qué cambió lo que se construye.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer la lista de cambios | Una línea por cada análisis 1, 2, 4 y 5 del pendiente 103, con su fecha y su enlace | Cuatro líneas, cada una con su fecha y su enlace |

**Cómo se verificó que la pareja cumple:** por lectura, contra `13·DOC25`.

**CA-08 · CP-003: el índice lo nombra**

**El problema que resuelve:** sin esto, quien abre `analisis/` no encuentra el análisis principal, y el índice sigue describiendo la regla derogada.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer `analisis/README.md` | Nombra el análisis principal y ya no dice que un análisis es una fotografía | Así |
| 2 | Correr `python validadores/validar.py estandar` | Sin fallas | `OK: sin incumplimientos` |
| 3 | Medir con `marcas.py` los dos archivos | Ninguna marca nueva | El principal, 0; el índice bajó de 2 a 1 |

**Cómo se verificó que la pareja cumple:** el paso 1 por lectura; el 2 y el 3, con los programas.

**RNF-06 · CP-004: cada tarea cita su criterio**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr `validar.py flujo` y leer el plan | Ninguna tarea sin su criterio | Sin avisos de tareas sueltas; queda el aviso de que la especificación es la HU |

| Caso | CA | Prioridad (del plan) | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-08 | Alta | 2026-10-02 | Lectura del análisis principal | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-08 | Alta | 2026-10-02 | Lectura de la lista de cambios: 4 líneas | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-08 | Alta | 2026-10-02 | `validar.py estandar` sin fallas; marcas 0, y de 2 a 1 | Aprobado | EV-02 | Ninguno |
| CP-004 | RNF-06 | Media | 2026-10-02 | `validar.py flujo` | Aprobado | EV-02 | Ninguno |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** nada.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que el análisis principal no repita el planteamiento ni las épicas | Lectura | Los enlaza; solo dice lo que no está en otro sitio |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU (`CA-0N` · `RNF-0N`) | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-08 | CP-001, CP-002, CP-003 | Aprobado | Sí |
| RNF-06 | CP-004 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 2 de 2 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 4 de 4 | Sí |
| Hallazgos al ejecutar | Plan §12.1 | Los que no se podían prever | 0 | Sí |

**Lo que no se cumplió:** nada.

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** el CA-08 y el RNF-06 tienen sus casos ejecutados y aprobados.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | El análisis principal | `analisis/proyecto-2026-10-02-analisis-principal.md` |
| EV-02 | Salida de `validar.py estandar`, `flujo` y `marcas.py` | Transcripción de la sesión del 2026-10-01 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-02 | 4 | 0 | Primera ejecución |
