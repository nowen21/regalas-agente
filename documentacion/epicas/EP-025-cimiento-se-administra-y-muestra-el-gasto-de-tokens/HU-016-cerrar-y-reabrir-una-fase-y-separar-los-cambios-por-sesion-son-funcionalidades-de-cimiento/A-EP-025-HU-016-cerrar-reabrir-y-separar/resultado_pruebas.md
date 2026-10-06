# Resultado de Pruebas · Fase `A-EP-025-HU-016-cerrar-reabrir-y-separar`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-016-cerrar-reabrir-y-separar` |
| **HU** | [HU-016](../HU-016-cerrar-y-reabrir-una-fase-y-separar-los-cambios-por-sesion-son-funcionalidades-de-cimiento.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-05 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Máquina local, rama `main`, sobre el commit `2c3b67b` más los cambios sin guardar; versión 54.4.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `CerrarYReabrirUnaFase` (3) | La primera pasada escribe los tres documentos y nombra las marcas sin tocar la HU ni la épica; ya llenos, cierra en el plan, la HU y la épica; una tercera vez no cambia nada | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `CerrarYReabrirUnaFase` (2) | Reabrir deja la estación 8, la HU y la épica en «En curso», el motivo y el ciclo 2; sin llenarlo no cierra, llenándolo sí; lo que no está cerrado o no trae motivo no se reabre | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Alta | `SepararLosCambiosPorSesion` (2), en un repositorio git temporal | Cada sesión con lo suyo, el archivo de las dos aparte, el de nadie aparte; preparar lleva solo lo de una y soltar lo saca | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-04 | Media | `CerrarYReabrirUnaFase` (4) y `SepararLosCambiosPorSesion` (2) | Una carpeta que no es fase y una sesión que no existe dan error; con pruebas que fallan no se toca nada; sin aplicar nada cambia | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** `--pruebas` corre en `cmd`, que no entiende `/` en la ruta del programa: la orden va con la ruta de Windows y entre comillas.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `"C:\Ing. Jose\ia\agente\proyectos\cimiento\.venv\Scripts\python.exe" -m unittest core.herramientas.tests_fase core.herramientas.tests_cambios` | Ran 13 tests in 4.818s, OK |
| 2 | Las órdenes con el repositorio real | `manage.py cambios_por_sesion` y `manage.py cerrar_fase` sobre esta fase | Lista lo de cada sesión; la primera pasada dejó 20 marcas y nombró dónde |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| CA-04 | CP-004 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 4 de 4 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 4 de 4 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los cuatro criterios pasan, y esta misma fase se cerró con `cerrar_fase`.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/herramientas/tests_fase.py` (9 pruebas) y `tests_cambios.py` (4) |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-05 | 4 | 0 | Primera ejecución |
