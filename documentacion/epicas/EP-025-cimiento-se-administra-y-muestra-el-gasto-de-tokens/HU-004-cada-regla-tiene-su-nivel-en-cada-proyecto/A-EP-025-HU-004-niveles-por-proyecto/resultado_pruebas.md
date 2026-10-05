# Resultado de Pruebas · Fase `A-EP-025-HU-004-niveles-por-proyecto`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-004-niveles-por-proyecto` |
| **HU** | [HU-004](../HU-004-cada-regla-tiene-su-nivel-en-cada-proyecto.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 2 |
| **Fecha de ejecución** | 2026-10-05 |
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
| CP-001 | CA-01 | Alta | `ElCatalogo` (3 pruebas) y `UnAdministradorCambiaUnNivel` (3) | El catálogo trae `02·F8` y más de 200 reglas, sin núcleo; todas empiezan en «frena»; `02·F8` en «avisa» solo en el primer proyecto; sin cambios no se guarda nada | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `ElNucleoYLoInvalidoNoSeGuardan` (4 pruebas) | `00·N1` no aparece; con él, una regla inventada o un nivel inexistente, el envío completo se rechaza con su mensaje y no se guarda nada | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Media | `CadaCambioQuedaRegistrado` | El cambio guarda regla, «frena», «avisa», la cuenta y la fecha, y el historial los muestra | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-04 | Alta | `ConsultaSoloVeLosNiveles` (2 pruebas) | Ve los niveles sin listas ni «Guardar»; su envío recibe 403 sin guardar | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** nada.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | La migración en la base local | `makemigrations` y `preparar_base` | Tablas creadas, sin migraciones pendientes |
| 2 | Que lo de las HU-001 a HU-003 siga andando | `manage.py test core.niveles core.proyectos core.cuentas core.inicio` | 63 pruebas, todas pasan |
| 3 | Ciclo 2: la pantalla contra la base real reiniciada | Cliente de pruebas de Django con una cuenta temporal, dentro de una transacción que se deshace, sobre `dp_card` | Reglas e historial: 200; las tablas de niveles apuntan a la tabla nueva de proyectos |

## 4. Defectos encontrados

| ID | Caso | Qué pasó | Esperado | Obtenido | Estado |
|---|---|---|---|---|---|
| D-01 | CP-001 | Visto el 2026-10-05, en la HU-006, contra la base real | La pantalla de reglas del proyecto | Falla al leer el proyecto: la tabla es la de la plataforma vieja (D-01 de la HU-003) | Corregido en el ciclo 2 de la fase de la HU-003 |

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| CA-04 | CP-004 | Aprobado | Sí |
| RNF-01 | CP-003 | Los cinco datos del cambio | Sí |
| RNF-02 | CP-001 | `reglas_configurables` con `lru_cache` | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 4 de 4 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 4 de 4 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los cuatro criterios pasan en la base de pruebas y, desde el ciclo 2, la pantalla abre contra la base real.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/niveles/` (13 pruebas en `tests.py`) |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-05 | 4 | 0 | Primera ejecución |
| 2 | 2026-10-05 | 4 | 0 | D-01 corregido en la HU-003; base reiniciada |
