# Resultado de Pruebas · Fase `A-EP-025-HU-003-registro-de-proyectos`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-003-registro-de-proyectos` |
| **HU** | [HU-003](../HU-003-los-proyectos-quedan-registrados-en-cimiento.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 2 |
| **Fecha de ejecución** | 2026-10-04; ciclo 2, 2026-10-05 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Máquina local, rama `main`, sobre el commit `29a30ad` más los cambios sin guardar; base de pruebas en MariaDB 11.4.9; versión 54.2.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |
| 2 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `LaCarpetaDeClaudeSaleDeLaRuta` (4 pruebas) y `UnAdministradorRegistra` (3) | `c--Ing--Jose-ia-agente`; la `ó` y los espacios dan `-`; el proyecto queda activo en la lista con su carpeta y los límites 2000 y 10 000, o los escritos | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `LoQueNoValeNoSeGuarda` (5 pruebas) | Ruta inexistente, ruta repetida con otras mayúsculas, nombre repetido, límite 0 o negativo y nombre vacío: cada uno con su mensaje, y un solo proyecto en la base | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Media | `SeEditaYSeDesactiva` (3 pruebas) | El límite nuevo en la lista; «Inactivo» sin borrar; la ruta propia no se da por repetida | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-04 | Alta | `ConsultaSoloVe` (3 pruebas) | Lista sin «Registrar» ni «Editar»; 403 en los formularios y en el POST, sin guardar | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** en Windows la carpeta se encuentra con cualquier letra de unidad, porque el sistema no distingue mayúsculas; la prueba revisa que la carpeta calculada exista, no la letra.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | La migración en la base local | `makemigrations` y `preparar_base` | Tabla creada, sin migraciones pendientes |
| 2 | Que lo de las HU-001 y HU-002 siga andando | `manage.py test core.proyectos core.cuentas core.inicio` | 50 pruebas, todas pasan |
| 3 | Ciclo 2: los proyectos que existen entran a la base nueva | Respaldo en `cimiento_respaldo_20261005` (17 tablas, 13 proyectos); `DROP DATABASE cimiento`; `preparar_base` | 12 proyectos traídos de `plantillas/proyectos.md`; `plataforma` no, porque su carpeta ya no existe |
| 4 | Ciclo 2: las pantallas contra la base real | Cliente de pruebas de Django con una cuenta temporal, dentro de una transacción que se deshace | `/`, `/proyectos/`, editar, reglas e historial: 200; ninguna cuenta quedó guardada |
| 5 | Ciclo 2: la migración, la orden `registrar` y el instalador | `tests_registro.py` (9 pruebas) y `manage.py test core.proyectos core.niveles core.consumo core.cuentas core.inicio` | 89 pruebas, todas pasan |

## 4. Defectos encontrados

| ID | Caso | Qué pasó | Esperado | Obtenido | Estado |
|---|---|---|---|---|---|
| D-01 | CP-001 | Visto el 2026-10-05, en la HU-006, contra la base real | La tabla de proyectos de este módulo | `proyectos_proyecto` es la de la plataforma vieja (`interfaz/`), con 13 proyectos; la migración de este módulo se dio por aplicada | Corregido en el ciclo 2: se respaldó la base, se reinició con las migraciones y la `0002` trajo los proyectos que existen |

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| CA-04 | CP-004 | Aprobado | Sí |
| RNF-01 | CP-001 | Los formularios llevan `csrf_token` | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 4 de 4 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 4 de 4 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los cuatro criterios pasan en la base de pruebas y, desde el ciclo 2, también contra la base real.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/proyectos/` (18 pruebas en `tests.py`) |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-04 | 4 | 0 | Primera ejecución |
| 2 | 2026-10-05 | 4 | 0 | D-01: base reiniciada, migración `0002` y orden `registrar` |
