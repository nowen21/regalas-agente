# Resultado de Pruebas · Fase `A-EP-029-HU-001-ajustes-y-estado-de-la-revision`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-029-HU-001-ajustes-y-estado-de-la-revision` |
| **HU** | [HU-001](../HU-001-la-configuracion-de-cada-proyecto-dice-que-tan-estricta-es-la-revision-de-pruebas.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-08 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | La base de pruebas de Django sobre MariaDB; versión 56.8.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 5 | 5 | 5 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `SinValoresPropiosValeLoDeFabrica` | De fábrica «solo avisar» y 7; el proyecto y la base mandan en su capa | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-01 | Alta | `LoQueNoEsValidoSeRechaza` | «avisar siempre» y 0 dan `ValueError` | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-02 | Alta | `LosAjustesSalenEnLosFormulariosConSuAyuda` | Los dos formularios traen los dos campos; su ayuda no dice «cobertura», «coverage» ni «commit» | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-03 | Alta | `SeGuardaUnaRevisionYEsLaUltima` | La de hoy es la última, con su herramienta, sus archivos y el navegador | Aprobado | EV-01 | Ninguno |
| CP-005 | CA-03 | Alta | `UnProyectoSinRevisiones` | Sin revisiones da ninguna; la parte que revisa empieza en no y se marca | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 5 casos en el plan, 5 acá.

**Qué salió distinto de lo esperado:** en la regresión falla `test_la_opt_in_apagada_no_autoriza_y_la_encendida_si` de `core.enganches.tests_freno`. No la causa esta fase: está en rojo desde el commit `041984a` y la registra el pendiente 140 («la regla opt-in de un capítulo que no es opt-in ya no se puede apagar»).

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que Django no pida más migraciones | `manage.py makemigrations --check --dry-run` | No changes detected |

## 4. Defectos encontrados

Ninguno de esta fase. El de §2 es del pendiente 140.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001, CP-002 | Aprobado | Sí |
| CA-02 | CP-003 | Aprobado | Sí |
| CA-03 | CP-004, CP-005 | Aprobado | Sí |
| RNF-01 | CP-003 | Aprobado | Sí |
| RNF-02 | Migraciones aditivas | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios tienen sus casos aprobados; de 595 pruebas de regresión pasan 594, y la que falla es ajena a la fase (pendiente 140).

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `manage.py test core.pruebas core.proyectos core.ayuda core.enganches`: Ran 595 tests, 1 falla ajena (pendiente 140) |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-08 | 5 | 0 | Primera ejecución |
