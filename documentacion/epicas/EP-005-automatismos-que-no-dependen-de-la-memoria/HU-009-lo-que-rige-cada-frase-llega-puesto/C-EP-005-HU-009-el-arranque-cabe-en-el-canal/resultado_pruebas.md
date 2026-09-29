# Resultado de Pruebas · Fase `C-EP-005-HU-009-el-arranque-cabe-en-el-canal`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra qué se ejecutó de verdad y con qué resultado, y de ahí sale el **veredicto** de la fase: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección *Qué se probó* del `funcionalidad_implementada.md`. El diseño de los casos vive en el `plan_pruebas.md` de esta misma fase, que no se modifica al ejecutar: se aprobó antes y así se queda.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `C-EP-005-HU-009-el-arranque-cabe-en-el-canal` |
| **HU** | [HU-009](../HU-009-lo-que-rige-cada-frase-llega-puesto.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md), versión 2.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-09-28 |
| **Ejecutado por** | El agente |
| **Ambiente y versión** | El repositorio del estándar, rama `main`, versión 39.4.0 sin commit; carpetas temporales para el proyecto de prueba y el gate |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 5 | 5 | 5 | 0 | 0 | 0 |

## 2. Ejecución caso por caso

**CA-04 · CP-001, que el arranque quepa y diga cómo llegan las reglas**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Arranque en el estándar | 10.000 o menos; código 0 | 9.499 caracteres; código 0 |
| 2 | Arranque en un proyecto que pasa el gate | 10.000 o menos, con la revisión | 960, con la revisión |
| 3 | Arranque en una carpeta sin estructura base | 10.000 o menos, con el gate | 4.735, con el gate y sin la instrucción |
| 4 | Leer lo del paso 1 | La instrucción, el mapa y la memoria | Los tres |
| 5 | Buscar el texto de las reglas | Ni `## N1 ·` ni el bloque viejo | No están |
| 6 | Caso `arranque-reglas-en-el-estandar` de `evals/` | Pasa | Pasa |

**CA-04 · CP-002, que lo que no cabe se recorte y se diga**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Memoria de prueba con tope de 3.000 | 3.000 o menos, sin filas cortadas, con la ruta | Cumple (`test_la_memoria_con_tope_cabe_sin_filas_cortadas`) |
| 2 | Histórico con tope de 1.000 | 1.000 o menos, con la ruta | Cumple |
| 3 | Arranque con la memoria larga | 10.000 o menos, con el bloque de lo que no cupo | Cumple |
| 4 | Los dos sin tope | Igual que antes | Cumple |

**CA-04 · CP-003, que los `CLAUDE.md` digan cómo llegan las reglas**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | `CLAUDE.md` §0 | No pide cargar todo; nombra el mapa | Cumple |
| 2 | Paso 2 de la plantilla | Lo mismo | Cumple |
| 3 | Guías de `cargador.py` y `hook_sesion.py` | El tope y la salida nueva | Cumple |

**RNF-01 · CP-004, tiempo, versión y pruebas**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Medir el arranque | Menos de 3 segundos | Entre 0,22 y 0,34 s |
| 2 | `VERSION` y `CHANGELOG.md` | `39.4.0`, entrada MENOR en palabras llanas | Cumple; `test_la_entrada_del_registro_se_entiende` en OK |
| 3 | `versionado`, `estandar` y las pruebas tocadas | 0 fallas y OK | 0 fallas; 77 pruebas en OK, más las 12 del andamio |

**CA-04 · CP-005, que ningún texto describa el arranque viejo**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Buscar las frases del arranque viejo | Ninguna fuera de lo que cuenta la historia | Ninguna. La búsqueda ampliada encontró más textos que la lista del plan, en el código, las guías, la especificación del módulo y la plataforma; los de este módulo se corrigieron acá y los de la plataforma en la fase `A` de EP-016 HU-005 |
| 2 | Anatomía y glosario | Dicen lo que hacen ahora | Cumple |
| 3 | La nota de la compactación | Dice lo que hace el arranque ahora | Cumple |
| 4 | RN-01 a RN-03 y CA-01 de HU-009, y sus marcas | Reemplazados; cero marcas fuera de código | Cumple |
| 5 | Los avisos de `hook_reglas.py` | No mencionan las reglas del arranque | Cumple |
| 6 | Pruebas de `hook_reglas.py` y `recuperar.py` | OK | OK |

**Decidido por el usuario al ejecutar:** el título de HU-009 pasa a «Lo que gobierna cada frase llega a tiempo».

## 3. Veredicto

| CA | Veredicto |
|---|---|
| CA-04 | Cumple |
| RNF-01, RNF-02 | Cumple |

**Concepto de la fase:** Cumple, 5 de 5 casos. **Defectos abiertos:** ninguno.
