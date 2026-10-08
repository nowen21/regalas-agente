# Resultado de Pruebas · Fase `E-EP-027-HU-006-la-plantilla-y-el-paso`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `E-EP-027-HU-006-la-plantilla-y-el-paso` |
| **HU** | [HU-006](../HU-006-las-reglas-de-cada-proyecto-viven-en-la-misma-tabla.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-07 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | La plantilla rellenada como la deja el instalador, y la base viva; versión 58.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-05 | Alta | `LaPlantillaDiceDondeViven` (3 pruebas) | El paso 4 y el punto 5.2 dicen que las reglas del proyecto registrado viven en Cimiento y llegan como índice; el archivo queda para el no registrado; ningún espacio por llenar nuevo; el instalador no crea el archivo | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-05 | Alta | El paso en la base viva | dp_card (1), Gestión de Servicios (7), LocalHub (10) y RNI (5) pasaron; su archivo quedó entero en la historia y se borró; `ver_regla` da sus reglas; AgroSystem no pasó por la P45 repetida y lo dijo; las cinco propuestas quedaron (10 a 14) | Aprobado | EV-02 | Ninguno |

**Correspondencia con el plan:** 2 casos en el plan, 2 acá.

**Qué salió distinto de lo esperado:** el texto guardado de Gestión de Servicios y de LocalHub mide 82 y 140 bytes menos que el archivo: son los retornos de carro de Windows, uno por renglón. El texto está entero.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `proyectos\cimiento\.venv\Scripts\python.exe proyectos\cimiento\manage.py test core.herramientas.tests_reglas_en_cimiento --noinput` | Ran 3 tests in 0.312s, OK |
| 2 | La copia antes del paso (`00·N7`) | `copiar_base` y `probar_copia` | Se restaura: 36 tablas, 160.627 filas |
| 3 | El paso | `migrate estandar` y `pasar_reglas_proyecto --todos --borrar` | Cuatro proyectos pasaron, cada uno en su versión 1.1.0; AgroSystem no |
| 4 | Cada proyecto, después | El archivo, la historia, la versión y el índice | Sin archivo, con su texto en la historia y su índice: 1, 7, 10 y 5 reglas |
| 5 | La versión del estándar | `registrar_version --obliga si` | 58.0.0 (MAYOR) |

## 4. Defectos encontrados

Ninguno en el programa. AgroSystem sigue con su archivo hasta que el usuario decida la P45 (H-26).

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-05 | CP-001, CP-002 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §5 | 100% | 1 de 1 | Sí |
| Casos ejecutados | Plan §12 | 100% | 2 de 2 | Sí |
| Copia antes y después del paso | Plan §8 | 2 | 1: la de después habría pisado la de antes, que lleva la misma fecha | Parcial |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los dos casos están aprobados, `core.herramientas` pasa completa (310 pruebas) y `validar.py flujo` no marca fallas.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `manage.py test core.herramientas`: 310 OK |
| EV-02 | El paso en la base viva | §3, filas 2 a 5 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-07 | 2 | 0 | Primera ejecución |
