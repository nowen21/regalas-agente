# Resultado de Pruebas · Fase `A-EP-023-HU-002-cada-punto-dice-de-donde-sale`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si cada criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-023-HU-002-cada-punto-dice-de-donde-sale` |
| **HU** | [HU-002](../HU-002-cada-documento-sale-del-anterior.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 2.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-02 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Repositorio del estándar en la máquina local, rama `main`, sobre el commit `c02a859` más los cambios de la fase |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 7 | 7 | 7 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

**CA-01 · CP-001: `F27` exige «Sale de»**

**El problema que resuelve:** sin esto, un punto puede entrar a un documento sin salir del anterior.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer `F27` | Exige «Sale de» con el punto del anterior; lo que no tiene origen no entra | Así |
| 2 | Leer su dependencia | «extiende `02·F18`»; `F18` sin cambios | Así |
| 3 | Correr `validar.py metareglas` | Sin fallas | `OK: sin incumplimientos` |

**CA-01 · CP-002: el validador sobre documentos de prueba**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Todos los puntos con su origen | Ninguna falla | Ninguna |
| 2 | Criterio sin «Sale de» | Una falla | «el CA-01 no tiene «Sale de»» |
| 3 | Criterio que cita un punto que no existe | Una falla | «el CA-01 cita el punto 9 del análisis 1, que no existe» |
| 4 | Conclusión que cita un turno que no existe | Una falla | Así |
| 5 | Fila que cita una conclusión que no existe | Una falla | Así |
| 6 | Pendiente sin origen, y con un hallazgo que no existe | Una falla por cada uno | Así |
| 7 | Épica sin análisis | Ninguna falla | Ninguna |
| 8 | Correr `test_origen` | Pasan | 8 de 8 |

**Cómo se verificó que la pareja cumple:** con las pruebas. En la primera corrida fallaron seis porque la ruta del resumen de prueba tenía un nivel de menos; era un error de la prueba, dentro del plan, y se corrigió.

**CA-01 · CP-003: el validador sobre el repositorio**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr `validar.py origen` | Sin fallas | `OK: sin incumplimientos`; revisó EP-023, la única épica con análisis |

**CA-02 · CP-004: `F28` dice que el cambio baja en orden**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer `F28` | Donde nace, aunque sea el planteamiento, y en orden: épica, HU, especificación y plan | Así |
| 2 | Leer su dependencia y su checklist | «extiende `02·F0`»; CUMPLE | Así |

**CA-03 · CP-005: la plantilla de la HU**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer la sección 3 | Los dos casos, con el enlace a la épica | Así |
| 2 | Leer los criterios de ejemplo | «Sale de» encima del escenario | Los tres lo tienen |
| 3 | Correr `validar.py estandar` | Sin fallas | `OK: sin incumplimientos` |

**CA-01, CA-02 · CP-006: registro, reglas por tarea y versión**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr `validar.py tareas`, `amarre` y `version` | Sin fallas; 42.0.0 | Sin fallas. `amarre` deja un aviso que ya existía: el mapa nombra `leidas.py`, que no está. `version` deja el de siempre: el `CLAUDE.md` de este repositorio no declara versión |
| 2 | Leer `reglas-validables.md` | `F27` validable; `F28` no | Así |
| 3 | Medir las marcas | Ninguna nueva | Ninguna en `base/` ni en `plantillas/`; el mapa del amarre suma el semáforo que lleva cada fila de su tabla |

**RNF-06 · CP-007: cada tarea cita su criterio**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr `validar.py flujo` | Ninguna tarea sin su criterio | Así; queda el aviso de que la especificación es la HU |

| Caso | CA | Prioridad (del plan) | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | 2026-10-02 | Lectura, `metareglas` | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-01 | Alta | 2026-10-02 | `test_origen` | Aprobado | EV-02 | DEF-01, corregido |
| CP-003 | CA-01 | Alta | 2026-10-02 | `validar.py origen` | Aprobado | EV-02 | Ninguno |
| CP-004 | CA-02 | Media | 2026-10-02 | Lectura | Aprobado | EV-01 | Ninguno |
| CP-005 | CA-03 | Media | 2026-10-02 | Lectura, `estandar` | Aprobado | EV-01 | Ninguno |
| CP-006 | CA-01, CA-02 | Media | 2026-10-02 | `tareas`, `amarre`, `version`, marcas | Aprobado | EV-02 | Ninguno |
| CP-007 | RNF-06 | Media | 2026-10-02 | `flujo` | Aprobado | EV-02 | Ninguno |

**Correspondencia con el plan:** 7 casos en el plan, 7 acá.

**Qué salió distinto de lo esperado:** la suite del estándar (`pruebas.py`) falló una vez en la prueba de enlaces rotos, porque `funcionalidad_implementada.md` ya enlazaba este archivo antes de que existiera; con este archivo escrito pasa. En la corrida final, 570 de 571 pasan: falla `NumeracionDePendientes.test_la_linea_sale_en_la_corrida_de_verdad`, porque a `pendientes/103-…md` le falta la fila «Historia de usuario» (`02·F23`). Esa falla ya estaba en el commit `c02a859` y depende del traslado del pendiente, que es de la HU-003.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que el validador revise solo las épicas que nacen de un análisis | `origen.epicas()` sobre el repositorio | Solo EP-023 |

## 4. Defectos encontrados

| ID | Caso | Qué pasó | Estado |
|---|---|---|---|
| DEF-01 | CP-002 | La prueba armaba el enlace al resumen con un nivel de carpeta de menos | Corregido en la prueba |

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU (`CA-0N` o `RNF-0N`) | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001, CP-002, CP-003, CP-006 | Aprobado | Sí |
| CA-02 | CP-004, CP-006 | Aprobado | Sí |
| CA-03 | CP-005 | Aprobado | Sí |
| RNF-06 | CP-007 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 4 de 4 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 7 de 7 | Sí |
| Hallazgos al ejecutar | Plan §12.1 | Los que no se podían prever | 0. El H-7 salió al escribir el plan, antes de aprobarlo | Sí |

**Lo que no se cumplió:** nada.

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios y el RNF-06 tienen sus casos ejecutados y aprobados.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Las reglas y la plantilla | `F27`, `F28`, `plantillas/ciclo-vida-proyectos/04-HU.md` |
| EV-02 | Salida de los validadores y las pruebas | Transcripción de la sesión del 2026-10-01 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-02 | 7 | 0 | Primera ejecución |
