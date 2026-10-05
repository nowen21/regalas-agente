# Resultado de Pruebas · Fase `A-EP-025-HU-001-mariadb-y-plantilla-comun`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-001-mariadb-y-plantilla-comun` |
| **HU** | [HU-001](../HU-001-cimiento-corre-sobre-mariadb-y-tiene-la-base-de-sus-pantallas.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 2 |
| **Fecha de ejecución** | 2026-10-04 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Máquina local, rama `main`, sobre el commit `29a30ad` más los cambios sin guardar; MariaDB 11.4.9 en `127.0.0.1:3307`; `.venv` de Cimiento con Django 5.2.17; versión 54.2.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 2 | 5 | 5 | 5 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `manage.py preparar_base` dos veces, `showmigrations`, lectura de `.env.example` | «La base «cimiento» en 127.0.0.1:3307 está lista, sin migraciones pendientes» las dos veces; ninguna migración sin aplicar; las cinco `DB_*` sin valores | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `preparar_base` con `DB_PUERTO=3399`; clases `SinBaseLaPantallaDiceQueHacer` y `ElErrorSeTraduceAQueHacer` de `core/inicio/tests.py` | «CommandError: MariaDB no responde en 127.0.0.1:3399. Hay que prenderla y volver a intentar.», código 1, sin traza; la página responde 503 con el mismo mensaje | Aprobado | EV-01, EV-02 | Ninguno |
| CP-003 | CA-03 | Media | Lectura de `plantillas/estructura-proyecto-django.md`, `CHANGELOG.md` y `VERSION` | El árbol trae `package.json`, `package-lock.json` y `node_modules/`; «Dependencias» explica npm; 54.2.0 con su entrada | Aprobado | EV-03 | Ninguno |
| CP-004 | CA-04 | Media | Clases `LaPaginaDeInicioUsaLaPlantillaComun` y `LosEstaticosDeNpmSeSirven`; la página pedida con el cliente de Django contra la base real | 200 con menú y cabecera; los cuatro estáticos se sirven; «Base de datos: cimiento, en MariaDB 11.4.9» | Aprobado | EV-02 | D-01, corregido |
| CP-005 | CA-05 | Alta | `validadores/instalar.py` en simulación sobre el estándar; clase `PrepararCimiento` de `tests_instalacion.py` (7 pruebas); el paso real con `preparar_cimiento(True)` | El paso sale antes de los enganches; sin `.venv`, sin npm o sin MariaDB queda «OMITIDO» con el motivo; en un proyecto que no es el estándar no corre; el paso real deja la base lista | Aprobado | EV-04 | Ninguno |

**Correspondencia con el plan:** 5 casos en el plan, 5 acá.

**Qué salió distinto de lo esperado:** el paso 2 de CP-004 pedía levantar el servidor y pedir un estático. El freno no deja correr el servidor en segundo plano, así que se probó con la vista que sirve los estáticos y con el cliente de Django, que es lo que usa el servidor. Las pruebas de `PrepararCimiento` se corrieron importando `core.validadores` primero, por el ciclo del pendiente 121.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que la configuración cargue | `manage.py check` | Sin problemas |
| 2 | Estructura y enlaces de los documentos de la fase | `validar.py fases`, `trazabilidad` y `estandar` | Sin fallas; los avisos son de HU-002 a HU-010, que no tienen fase todavía |
| 3 | Marcas de redacción en lo escrito | El enganche de redacción en cada escritura | Las que avisó se corrigieron |

## 4. Defectos encontrados

| ID | Caso | Qué pasó | Esperado | Obtenido | Estado |
|---|---|---|---|---|---|
| D-01 | CP-004 | Las carpetas `dist` de npm con prefijo en `STATICFILES_DIRS` | 200 | 404: en Windows, Django compara el prefijo con `\` | Corregido sin prefijo; prueba nueva `LosEstaticosDeNpmSeSirven`; señal S-299 |
| D-02 | CP-001 | El motor de las tablas, visto al probar la HU-002 | Tablas con transacciones | MyISAM, el motor por defecto del MariaDB de WAMP: sin transacciones ni llaves foráneas | Corregido: `init_command` fija InnoDB, `preparar_base` pasa a InnoDB lo que esté en otro motor, pruebas `LasTablasSonInnoDB`; señal S-300. La base local se rehízo con las migraciones de Django; no tenía cuentas |

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| CA-04 | CP-004 | Aprobado | Sí |
| CA-05 | CP-005 | Aprobado | Sí |
| RNF-01 | CP-001 | `.env.example` sin valores; el `.env` está en `.gitignore` | Sí |
| RNF-02 | CP-003 | `package-lock.json` con las versiones exactas | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 5 de 5 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 5 de 5 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los cinco criterios tienen sus casos ejecutados y aprobados; el único defecto se corrigió dentro de los archivos del plan.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Orden y configuración | `proyectos/cimiento/core/inicio/management/commands/preparar_base.py`, `proyectos/cimiento/core/inicio/base_de_datos.py`, `proyectos/cimiento/.env.example` |
| EV-02 | Pantallas y pruebas | `proyectos/cimiento/core/inicio/tests.py` (13 pruebas), `proyectos/cimiento/templates/base.html` |
| EV-03 | Plantilla y versión | `plantillas/estructura-proyecto-django.md`, `CHANGELOG.md`, `VERSION` |
| EV-04 | Instalador y pruebas | `proyectos/cimiento/core/herramientas/instalar.py`, `proyectos/cimiento/core/herramientas/tests_instalacion.py`, `validadores/instalar.py` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-04 | 5 | 0 | Primera ejecución |
| 2 | 2026-10-04 | 5 | 0 | D-02: las tablas pasan a InnoDB; `core/inicio/tests.py` con 16 pruebas |
