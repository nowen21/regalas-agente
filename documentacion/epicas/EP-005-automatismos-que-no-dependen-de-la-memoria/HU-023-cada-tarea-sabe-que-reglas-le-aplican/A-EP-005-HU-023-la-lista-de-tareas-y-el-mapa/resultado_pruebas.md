# Resultado de Pruebas · Fase `A-EP-005-HU-023-la-lista-de-tareas-y-el-mapa`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra qué se ejecutó de verdad y con qué resultado, y de ahí sale el **veredicto** de la fase: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección *Qué se probó* del `funcionalidad_implementada.md`. El diseño de los casos vive en el `plan_pruebas.md` de esta misma fase, que no se modifica al ejecutar: se aprobó antes y así se queda.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-005-HU-023-la-lista-de-tareas-y-el-mapa` |
| **HU** | [HU-023](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-09-28 |
| **Ejecutado por** | El agente |
| **Ambiente y versión** | El repositorio del estándar, rama `main`, versión 39.2.0 sin commit; carpetas temporales para las pruebas del programa |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

**CA-01 · CP-001, que la lista exista y no se superponga**

**El problema que resuelve:** sin lista cerrada, cada regla nombra la tarea a su manera y el mapa no agrupa nada.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir `base/tareas.md` | Una tabla con cada tarea, su nombre y cuándo aplica | Diez tareas, de `recibir-pedido` a `trabajar-cadena`, cada una con su frase |
| 2 | Comparar las tareas de dos en dos | Ninguna acción cae en dos a la vez | Ninguna se superpone: cada frase nombra una acción distinta (escribir un documento no es cambiar código, y cambiar el estándar es cambiar una regla, plantilla o validador) |
| 3 | Tomar cada regla del núcleo anotada | Cada una encontró al menos una tarea | Las diez tienen entre una y siete tareas de la lista; ninguna necesitó una tarea nueva |

**Cómo se verificó que la pareja cumple:** el paso 3 es el que prueba que la lista sirve con reglas reales; los pasos 1 y 2 prueban que es cerrada y que no se pisa.

**CA-02 · CP-002, que la línea no cambie la regla**

**El problema que resuelve:** si la línea contara, anotar las 261 reglas anularía sus 261 checklists.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | En la prueba `test_no_cuenta_para_el_largo`, medir una regla sin la línea y con ella | El mismo número | El mismo, y igual al largo del cuerpo solo |
| 2 | En la prueba `test_no_vence_el_sello`, comparar con `_sin_declaracion` el texto sin la línea y con ella | Iguales | Iguales |
| 3 | Medir `N1` a `N10` antes y después de anotarlas | El mismo largo | El núcleo actual, quitándole las 10 líneas `**Aplica a:**`, es idéntico al de `HEAD`; como la línea queda fuera del cuerpo, el largo de cada regla no cambia (N1 232, N10 224) |
| 4 | Correr `python validadores/validar.py metareglas` | Ninguna regla del núcleo con el sello vencido | `OK: sin incumplimientos` |

**Cómo se verificó que la pareja cumple:** los pasos 1 y 2 prueban el mecanismo; el 3 y el 4, que en el repositorio real no cambió nada más que las líneas.

**CA-03 · CP-003, que el mapa salga de las reglas**

**El problema que resuelve:** un mapa escrito a mano envejece sin que nadie lo note.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | En la prueba `test_una_regla_con_dos_tareas_sale_en_las_dos`, armar el mapa con una regla de dos tareas | Sale bajo las dos | Sale bajo `cambiar-codigo` y `escribir-documento` |
| 2 | En la prueba `test_cambiar_la_tarea_mueve_la_regla`, cambiarle la tarea y volver a armar | Sale bajo la nueva y no bajo la vieja | Sale bajo `tocar-git` y ya no bajo `cambiar-codigo` |
| 3 | Correr `python -m unittest test_cada_tarea_sabe_que_reglas_le_aplican` desde `validadores/tests` | OK | `Ran 8 tests`, `OK` |
| 4 | Correr `python validadores/mapa_tareas.py` | Escribe `base/mapa-de-tareas.md` con `N1` a `N10` bajo sus tareas | «Mapa escrito en base/mapa-de-tareas.md». Las diez reglas aparecen; `trabajar-cadena` y `cambiar-estandar` tienen solo `N1` o ninguna, porque el núcleo casi no les habla |
| 5 | Abrir un enlace del mapa | Lleva a la regla | Los enlaces usan el ancla de `citas.ancla`, la misma que ya usa el estándar, y `estandar` los resolvió sin incumplimientos |

**Cómo se verificó que la pareja cumple:** los pasos 1 a 3 prueban el programa en aislamiento; el 4 y el 5, sobre el repositorio.

**RNF-01 y RNF-02 · CP-004, versionado y pruebas**

**El problema que resuelve:** un cambio sin versión no se puede rastrear, y un programa sin pruebas se rompe sin aviso.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir `VERSION` | `39.2.0` | `39.2.0` |
| 2 | Abrir `CHANGELOG.md` | Entrada `39.2.0`, `**MENOR**`, en palabras llanas | Está; sus dos primeros párrafos no tienen rutas ni identificadores |
| 3 | Correr `python validadores/validar.py versionado` y `test_la_entrada_del_registro_se_entiende` | 0 fallas y OK | `0 falla(s), 1 aviso(s)`, el de la 15.4.0 que ya estaba; la prueba dio OK |
| 4 | Buscar el archivo de pruebas nuevo | Existe | `validadores/tests/test_cada_tarea_sabe_que_reglas_le_aplican.py`, 8 pruebas |

**Cómo se verificó que la pareja cumple:** los cuatro pasos dan lo esperado.

| Caso | CA | Prioridad (del plan) | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | 2026-09-28 | Diez tareas sin superponerse; las diez reglas del núcleo encontraron las suyas | Aprobado | EV-01 | — |
| CP-002 | CA-02 | Crítica | 2026-09-28 | Dos pruebas del mecanismo; el núcleo sin las líneas es idéntico a `HEAD`; `metareglas` sin incumplimientos | Aprobado | EV-02 | — |
| CP-003 | CA-03 | Crítica | 2026-09-28 | 8 pruebas en OK; el mapa del repositorio escrito por el programa, con enlaces que `estandar` resolvió | Aprobado | EV-03 | DEF-01 |
| CP-004 | RNF-01, RNF-02 | Media | 2026-09-28 | `VERSION` en 39.2.0, entrada `**MENOR**`, `versionado` sin fallas, archivo de pruebas con 8 | Aprobado | EV-04 | — |

**Correspondencia con el plan:** 4 casos en el plan, 4 aquí.

**Qué salió distinto de lo esperado:** el mapa salió la primera vez con 25 marcas de `ID8`: el punto medio entre el identificador y el nombre de cada regla (DEF-01). Además, las pruebas del amarre pasaron de 4 fallas a 5 porque el programa nuevo no estaba clasificado (DEF-02).

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que el programa nuevo quede clasificado en el mapa del amarre | `python validadores/validar.py amarre` | `mapa_tareas.py` ya no aparece; quedan las 2 fallas que ya estaban, de dos programas que no son de esta fase |

## 4. Defectos encontrados

| ID | Título | Caso que lo destapó | Severidad | Estado | Dónde quedó registrado |
|---|---|---|---|---|---|
| DEF-01 | El mapa escribía `·` entre el identificador y el nombre, y en una lista eso es marca de `ID8` | CP-003 | Baja | Verificado | Este documento; el formato cambió en `mapa_tareas.py` |
| DEF-02 | `mapa_tareas.py` sin clasificar en el mapa del amarre | Verificación manual 1 | Media | Verificado | Este documento |

**Defectos abiertos que se aceptan y por qué:** ninguno. Al corregir el DEF-02 salió otro problema, que no es de esta fase: el validador del amarre da por clasificado un programa con solo nombrarlo. Quedó como H-8 en el resumen de la sesión.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU (`CA-0N` · `RNF-0N`) | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| RNF-01 | CP-004 | Aprobado | Sí |
| RNF-02 | CP-004 | Aprobado | Sí |

**Los que no cumplen:** ninguno. CA-04 y CA-05 son de la fase `B`.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias de la fase | Plan §12 | 100% | 5 de 5 con caso | Sí |
| Fallas de `metareglas`, `estandar` y `versionado` | Plan §12 | 0 | 0, 0 y 0 | Sí |
| Pruebas nuevas | Plan §12 | Todas | 8 de 8 | Sí |

**Lo que no se cumplió:** nada.

## 6. Veredicto de la fase

**Concepto:** Cumple

**Justificación:** CA-01, CA-02, CA-03, RNF-01 y RNF-02 cumplen con sus casos ejecutados (§5). Los dos defectos se corrigieron dentro de la fase.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Archivo resultante | `base/tareas.md` y las líneas `**Aplica a:**` de `base/00-nucleo-blindado.md` |
| EV-02 | Pruebas y salida de `metareglas` | `test_no_cuenta_para_el_largo`, `test_no_vence_el_sello` |
| EV-03 | Pruebas, programa y archivo resultante | `validadores/mapa_tareas.py`, sus 8 pruebas y `base/mapa-de-tareas.md` |
| EV-04 | Archivos resultantes y prueba | `VERSION`, `CHANGELOG.md` y `test_la_entrada_del_registro_se_entiende` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-09-28 | 4 | 0 | Primera ejecución |
