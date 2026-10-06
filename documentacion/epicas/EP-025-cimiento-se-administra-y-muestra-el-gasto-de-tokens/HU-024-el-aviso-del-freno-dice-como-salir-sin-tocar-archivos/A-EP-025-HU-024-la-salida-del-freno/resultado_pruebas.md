# Resultado de Pruebas · Fase `A-EP-025-HU-024-la-salida-del-freno`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-024-la-salida-del-freno` |
| **HU** | [HU-024](../HU-024-el-aviso-del-freno-dice-como-salir-sin-tocar-archivos.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-05 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Máquina local, rama `main`, sobre el commit `2c3b67b` más los cambios sin guardar; versión 55.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Media | `ElAvisoDiceLaSalida` (3) y el enganche en vivo | La salida nombra las cuatro contrarias y la suspensión de la regla con la dirección; la regla del núcleo dice que no se suspende; el aviso la trae solo si viene | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `ElAnalisisDeLaPropiaSesion` (3) | Con dos sesiones y dos análisis, cada freno deja lo de su análisis y detiene lo del otro; el archivo nuevo que nombra el análisis pasa; la transcripción se halla por la primera línea | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Alta | `ElCdDeUnaOrden` (5) | `cd sub && rm x.txt` resuelve `sub/x.txt`; una ruta entre comillas, `cd hondo` y `cd ..` siguen la carpeta; el archivo del análisis pasa después del `cd`; sin `cd`, la orden entera como antes; en el ciclo 2, lo que va entre comillas no se parte (H-10) | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** la prueba en vivo con la sesión de esta conversación hizo que el freno anotara un hallazgo de prueba en el resumen; se quitó. En el ciclo 2: con un `cd`, la orden se partía por líneas antes de mirar las comillas (H-10 del resumen del 2026-10-04, sesión 3); ahora se parte solo por lo que queda fuera.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `cd proyectos\cimiento && python -c "import core.validadores, unittest, sys; r=unittest.TextTestRunner(verbosity=0).run(unittest.defaultTestLoader.loadTestsFromNames(['core.enganches.tests_freno_salida','core.enganches.tests_freno'])); sys.exit(not r.wasSuccessful())"` | Ran 332 tests in 46.078s, OK |
| 2 | El aviso en vivo | `hook_antes.py` con una escritura en `base/` fuera del plan | Detiene y dice la salida, con `http://127.0.0.1:8015/proyectos/4/suspensiones/` |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 3 de 3 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 3 de 3 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios pasan, `tests_freno` (335) sigue en verde, y el aviso en vivo trae la salida con la dirección real de «Suspensiones».

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/enganches/tests_freno_salida.py` (11) |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-05 | 3 | 0 | Primera ejecución |
| 2 | 2026-10-05 | 3 | 0 | Reabierta: con un cd, la orden se partía por líneas antes de mirar las comillas, y un signo dentro de un texto entre comillas parecía una redirección (H-10 del resumen del 2026-10-04, sesión 3) |
