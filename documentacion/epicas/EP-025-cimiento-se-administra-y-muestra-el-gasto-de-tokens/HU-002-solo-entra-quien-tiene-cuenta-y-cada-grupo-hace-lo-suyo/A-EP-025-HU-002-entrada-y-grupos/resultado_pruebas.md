# Resultado de Pruebas · Fase `A-EP-025-HU-002-entrada-y-grupos`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-002-entrada-y-grupos` |
| **HU** | [HU-002](../HU-002-solo-entra-quien-tiene-cuenta-y-cada-grupo-hace-lo-suyo.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-04 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Máquina local, rama `main`, sobre el commit `29a30ad` más los cambios sin guardar; base de pruebas `test_cimiento` en MariaDB 11.4.9; versión 54.2.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `SinCuentaSePideEntrar` (4 pruebas) y `SinBaseLaPantallaDiceQueHacer` | `/` sin cuenta va a `/entrar/?next=/`; con la cuenta vuelve a `/` con el usuario y «Salir»; salir vuelve a pedir entrar; sin base, 503 sin pedir entrar | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `LaContrasenaEquivocadaNoDejaEntrar` (2 pruebas) | El mismo mensaje para la contraseña equivocada y el usuario que no existe; sin sesión | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Alta | `CadaGrupoHaceLoSuyo` (4 pruebas) con una vista de prueba | Consulta y sin grupo: 403 «No tiene permiso» sin el contenido; administrador y superusuario: 200 | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-04 | Media | `CrearCuenta` (6 pruebas); los grupos en la base local | Los dos grupos existen; la cuenta queda en su grupo con la contraseña en resumen; claves distintas, grupo inexistente, usuario repetido y clave débil dan error sin crear nada | Aprobado | EV-01 | D-01, corregido |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** al correr las pruebas juntas, los grupos desaparecían después del primer caso. Las tablas eran MyISAM y Django vaciaba la base entre casos.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Configuración y migraciones | `manage.py check` y `makemigrations --check` | Sin problemas, sin migraciones faltantes |
| 2 | Los grupos en la base local | `preparar_base` y la consulta de `Group` | `administrador` y `consulta` |
| 3 | Que lo de la HU-001 siga andando | `manage.py test core.inicio`, junto con `core.cuentas` | 32 pruebas, todas pasan |

## 4. Defectos encontrados

| ID | Caso | Qué pasó | Esperado | Obtenido | Estado |
|---|---|---|---|---|---|
| D-01 | CP-004 | Las tablas de la base eran MyISAM | Cada prueba con los datos de las migraciones | Django vaciaba la base entre casos | Corregido en la fase de la HU-001 (su D-02), que declara esos archivos; señal S-300 |

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| CA-04 | CP-004 | Aprobado | Sí |
| RNF-01 | CP-004 | La contraseña guardada no es la escrita | Sí |
| RNF-02 | CP-001 | Salir es por POST desde un formulario con su protección CSRF | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 4 de 4 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 4 de 4 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los cuatro criterios tienen sus casos ejecutados y aprobados.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/cuentas/` (16 pruebas en `tests.py`), `proyectos/cimiento/core/inicio/middleware.py`, `proyectos/cimiento/config/settings/base.py` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-04 | 4 | 0 | Primera ejecución |
