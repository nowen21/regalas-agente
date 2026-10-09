# Resultado de Pruebas · Fase `A-EP-029-HU-002-revisar-y-su-pagina`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-029-HU-002-revisar-y-su-pagina` |
| **HU** | [HU-002](../HU-002-el-boton-revisar-muestra-que-parte-de-cada-proyecto-queda-sin-pruebas.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 2 |
| **Fecha de ejecución** | 2026-10-08 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | La base de pruebas de Django sobre MariaDB, con la herramienta de cada lenguaje simulada; versión 56.8.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 2 | 9 | 9 | 9 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `ReconoceCadaLenguaje` | Django, Laravel, Angular y Python; Django dentro de `proyectos/app/`; nada dentro de `node_modules/` ni `.venv/` | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-01 | Alta | `ElQueNoReconoceQuedaSinMedicion` | «sin medición» con mensaje | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-02 | Alta | `DjangoGuardaPorcentajeYArchivos` | 75%, el archivo de 30% primero, con sus líneas | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-02 | Alta | `LaravelYAngularLeenSuResultado` | 80% y 62,5% | Aprobado | EV-01 | Ninguno |
| CP-005 | CA-02 | Alta | `FaltaLaHerramientaOElPython` | «falló» con el mensaje de cada caso | Aprobado | EV-01 | Ninguno |
| CP-006 | CA-03 | Alta | `ElBotonArrancaLaRevisionAparte` | Se arranca aparte y dice «Revisando»; quien no administra recibe 403 | Aprobado | EV-01 | Ninguno |
| CP-007 | CA-03 | Alta | `LaOrdenHaceLaMismaRevision` | Revisión guardada con 75%, «Revisando» apagado | Aprobado | EV-01 | Ninguno |
| CP-008 | CA-04 | Alta | `LaPaginaMuestraTodosLosProyectos` | Dos filas, «Al día» y «Nunca se ha revisado»; el menú lleva | Aprobado | EV-01 | Ninguno |
| CP-009 | CA-04 | Alta | `ElDetalleYSuContraria` | Menos pruebas primero; la revisión se borra | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 9 casos en el plan, 9 acá.

**Qué salió distinto de lo esperado:** en el ciclo 1, la simulación no reemplazaba al programa real porque se fijaba al cargar el módulo; se corrigió `Revisor` para buscarlo al usarlo, y de paso que un programa que no abre dé un mensaje en vez de un error. La regresión del ciclo 1 pidió la sección del manual (H-3), que agregó el análisis 3 del pendiente 141.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que Django no pida más migraciones | `manage.py makemigrations --check --dry-run` | No changes detected |

## 4. Defectos encontrados

Los de §2, corregidos en esta fase. Fuera de la fase, la regresión de `core.estandar` mostró una prueba de la guía en rojo desde la EP-028 (H-4, pendiente 143); no se tocó.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001, CP-002 | Aprobado | Sí |
| CA-02 | CP-003, CP-004, CP-005 | Aprobado | Sí |
| CA-03 | CP-006, CP-007 | Aprobado | Sí |
| CA-04 | CP-008, CP-009 | Aprobado | Sí |
| RNF-01 | CP-002, CP-005 y la ayuda | Aprobado | Sí |
| RNF-02 | CP-006 y el tope de 30 minutos de `Revisor` | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los cuatro criterios tienen sus casos aprobados y la regresión de `core.pruebas core.inicio core.ayuda core.proyectos` pasa entera.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `manage.py test core.pruebas core.inicio core.ayuda core.proyectos`: Ran 120 tests, OK |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-08 | 7 | 2 | La simulación de la herramienta y la sección del manual |
| 2 | 2026-10-08 | 9 | 0 | |
