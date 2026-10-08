# Resultado de Pruebas · Fase `B-EP-027-HU-006-reglas-en-la-tabla`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-027-HU-006-reglas-en-la-tabla` |
| **HU** | [HU-006](../HU-006-las-reglas-de-cada-proyecto-viven-en-la-misma-tabla.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-07 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | La base de pruebas de Django y una carpeta temporal de proyecto; versión 57.4.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-02 | Alta | `PasanALaTabla` (3 pruebas) y `UnCodigoRepetidoNoPasa` | Las reglas en `###` quedan con su proyecto, sus casillas y su grupo, y suben la versión del proyecto; las de `##` también; pasar dos veces no duplica; con un código repetido no pasa nada, se dice cuál y el archivo queda | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `ElArchivoQuedaEnLaHistoria` | Con `--borrar`, el archivo queda entero en la historia del proyecto y se borra | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-02 | Alta | `SeVenYSeCambian` (4 pruebas) | La pantalla muestra cada regla con su grupo; `ver_regla` da el índice y la regla entera; cambiar desde la pantalla pasa a la tabla y la regla quitada queda apartada; la consulta no puede cambiar | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** el lector, probado sin escribir contra los archivos reales, encontró 56, 1, 7, 10 y 5 reglas, como el inventario; y en AgroSystem, dos reglas con el código P45 (H-26). Se agregó al caso CP-001 que un código repetido no pase.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `proyectos\cimiento\.venv\Scripts\python.exe proyectos\cimiento\manage.py test core.estandar.tests_reglas_del_proyecto --noinput` | Ran 9 tests in 6.835s, OK |
| 2 | El lector con los cinco archivos reales, sin escribir | `molde.partir` con el nivel de cada archivo | AgroSystem 56 en siete grupos (P45 dos veces), dp_card 1, Gestión de Servicios 7, LocalHub 10, RNI 5 |

## 4. Defectos encontrados

Ninguno en el programa. En los datos: AgroSystem tiene dos P45 (H-26), y lo decide el usuario.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-02 | CP-001, CP-002, CP-003 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §5 | 100% | 1 de 1 | Sí |
| Casos ejecutados | Plan §12 | 100% | 3 de 3 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres casos están aprobados, y `core.estandar` y `core.ayuda` pasan completas.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `manage.py test core.estandar core.ayuda`: 91 pruebas, todas en verde tras la corrección del código repetido |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-07 | 3 | 0 | Primera ejecución |
