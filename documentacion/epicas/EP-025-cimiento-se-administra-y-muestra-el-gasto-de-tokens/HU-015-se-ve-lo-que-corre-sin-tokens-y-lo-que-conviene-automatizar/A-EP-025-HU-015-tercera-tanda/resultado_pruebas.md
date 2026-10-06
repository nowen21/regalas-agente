# Resultado de Pruebas · Fase `A-EP-025-HU-015-tercera-tanda`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-015-tercera-tanda` |
| **HU** | [HU-015](../HU-015-se-ve-lo-que-corre-sin-tokens-y-lo-que-conviene-automatizar.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-05 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Máquina local, rama `main`, sobre el commit `2c3b67b` más los cambios sin guardar; base de pruebas y base real en MariaDB 11.4.9; versión 55.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `LoQueCorreSinTokens` (2) | Tres corridas guardadas, sin duplicar al leer otra vez; la sección trae el enganche que no agrega con cero tokens y una vez, y el que sí agrega con sus tokens | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `LaOrdenDeUnComando` (1) y `CandidatosAAutomatizar` (2) | `git status`, `python manage.py`, `python -m unittest`, `python validar.py`, `curl` y `echo` sin su texto; el archivo leído tres veces con 2.000 tokens de ahorro y el de dos no; el enganche de cada mensaje sí y el de una vez no; el comando repetido; la página trae las dos secciones | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 2 casos en el plan, 2 acá.

**Qué salió distinto de lo esperado:** al aplicar la migración `0004` en la base real, el vigilante que corría con el código viejo falló al guardar sin la columna nueva y se cayó. Ahora un archivo que falla queda para el próximo cambio y el vigilante sigue.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `cd proyectos\cimiento && .venv\Scripts\python.exe manage.py test core.consumo` | Ran 47 tests in 9.077s, OK |
| 2 | En vivo | Migración `0004`, vigilante reiniciado, conteo en la base real | 14 corridas y 65 órdenes guardadas en segundos; ninguna con el comando completo |
| 3 | Rendimiento | Cada sección de `GastoDelPeriodo(30)` medida aparte | 0,6 s en total; las dos nuevas, 0,06 s |

## 4. Defectos encontrados

Uno, corregido en la fase: el vigilante se caía con el primer error de un archivo.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 2 de 2 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 2 de 2 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los dos criterios pasan; en vivo se guardan las corridas y las órdenes; «Gasto» con 30 días tarda 0,6 s.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/consumo/tests_tercera_tanda.py` (5) y la prueba nueva de `tests_vigilante.py` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-05 | 2 | 0 | Primera ejecución |
