# Resultado de Pruebas · Fase `A-EP-025-HU-013-tres-capas`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-013-tres-capas` |
| **HU** | [HU-013](../HU-013-cada-proyecto-tiene-su-configuracion-en-tres-capas.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-05 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Máquina local, rama `main`, sobre el commit `2c3b67b` más los cambios sin guardar; base de pruebas y base real en MariaDB 11.4.9; versión 55.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `ElCatalogo` (3), `LasCapasSinDjango` (2) y `LasPantallas` (4) | Fábrica, base y proyecto en orden; cambiar la base no pisa al proyecto; sin base, fábrica; un valor roto cuenta como vacío; «Configuración» la guarda el administrador y la consulta recibe 403; el proyecto guarda y vacía lo suyo; un valor que no vale no se guarda | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `ElFrenoAplicaLasSuspensiones` (3) y `SuspenderYLevantar` (4) | La regla suspendida queda «apagada»; el freno entero apaga todo menos el núcleo; vencida o levantada ya no cuenta; levantar guarda quién; el núcleo, una regla que no existe, sin motivo, más de 30 días y fecha pasada se rechazan; el histórico no se puede nombrar; la consulta no suspende ni levanta | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Media | `LasPantallas`, `SuspenderYLevantar`, `LaMigracionPasaLosLimites` y `LosLimitesSonLosDelProyecto` (4) | La copia `.agente/configuracion.md` dice el valor y su capa y las suspensiones vigentes; los límites salen de los ajustes; la migración pasa el límite propio a su ajuste y la reversa lo devuelve | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** al cambiar `niveles.py` antes de migrar, el freno se quedó sin base y detuvo toda escritura hasta aplicar la `0004` (H-9 del resumen del 2026-10-04, sesión 3). Y dos pruebas de fases anteriores (`tests_analisis_prendido.py`, `tests_vigilante.py`) tumbaban a las que venían después por no llevar `serialized_rollback`; se corrigieron.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `cd proyectos\cimiento && .venv\Scripts\python.exe manage.py test core.proyectos core.niveles core.consumo` | Ran 109 tests in 101.256s, OK |
| 2 | El freno y los límites | `core.enganches.tests_limites` y `core.enganches.tests_freno` | 335 pruebas pasan |
| 3 | La base real | `manage.py migrate proyectos` y `manage.py check` | La `0004` aplicada; sin problemas |

## 4. Defectos encontrados

Ninguno abierto.

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

**Justificación:** los tres criterios pasan; con las suites del freno y de los límites (335) y las de proyectos, niveles y consumo juntas (109), y la `0004` aplicada en la base real.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/proyectos/tests_configuracion.py` (17), y las pruebas cambiadas de proyectos, registro y límites |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-05 | 3 | 0 | Primera ejecución |
