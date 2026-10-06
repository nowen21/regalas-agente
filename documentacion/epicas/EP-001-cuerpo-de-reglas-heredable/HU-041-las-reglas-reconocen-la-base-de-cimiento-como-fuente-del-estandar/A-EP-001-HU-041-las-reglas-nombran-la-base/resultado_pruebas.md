# Resultado de Pruebas · Fase A-EP-001-HU-041-las-reglas-nombran-la-base   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra qué se ejecutó de verdad y con qué resultado, y de ahí sale el **veredicto** de la fase. El diseño de los casos vive en el `plan_pruebas.md` de esta misma fase, que no se modifica al ejecutar.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-001-HU-041-las-reglas-nombran-la-base` |
| **HU** | [HU-041](../HU-041-las-reglas-reconocen-la-base-de-cimiento-como-fuente-del-estandar.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-06 |
| **Ejecutado por** | El agente |
| **Ambiente y versión** | Repositorio del estándar en la máquina local, sobre el commit `592b426` con los cambios de la fase sin guardar, versión 56.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

**[CA-01](../HU-041-las-reglas-reconocen-la-base-de-cimiento-como-fuente-del-estandar.md#ca-01--2010-pone-la-versión-y-su-registro-en-la-base) con [CP-001](plan_pruebas.md#cp-001--m10-dice-versión-y-registro-en-la-base), que `M10` ponga la versión y su registro en la base**

**El problema que resuelve:** sin esto, un ajuste de un proyecto cambia sin versión ni rastro, y la EP-026 incumpliría `M10` al guardar el estándar en la base.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir `M10` | El título no cambió | «## M10 · Todo cambio de regla se versiona y se registra», igual que antes |
| 2 | Leer el cuerpo | Todo cambio, del estándar o de un proyecto, sube su versión y queda registrado en la base de datos del agente; mientras no la tenga, `CHANGELOG.md` y `VERSION` | Dice eso, con «quién, cuándo, antes, después y por qué» |
| 3 | Leer la sección «M10» de `base.md` | Las dos preguntas que fijan el tipo | Están, en orden, con «Qué versión sube» |
| 4 | Leer el checklist | CUMPLE contra 56.0.0, con el enlace al análisis | «contra **v56.0.0**, el **2026-10-06**» y «Lo que cambió en v56.0.0» enlaza el análisis 1 del pendiente 132 |

**Cómo se verificó que la pareja cumple:** el paso 2 decide; el 1 asegura que el ancla no cambió y el 4 cubre RNF-01.

**[CA-02](../HU-041-las-reglas-reconocen-la-base-de-cimiento-como-fuente-del-estandar.md#ca-02--lo-que-decía-la-fuente-es-el-texto-queda-derogado) con [CP-002](plan_pruebas.md#cp-002--nada-dice-que-la-fuente-es-el-texto), que nada diga ya que la fuente es el texto**

**El problema que resuelve:** con la decisión vieja escrita sin marcar, se puede volver a aplicar.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer `C19` (línea 789 de `base/01-conducta.md`) | La memoria vive en la base de datos del agente cuando la tiene | «la base de datos del agente o, sin ella, `historico-chat/memory/`» |
| 2 | Abrir la nota de la fuente de las reglas | Derogada, con el enlace | Abre con «Derogada el 2026-10-06» y el enlace al análisis |
| 3 | Abrir EP-016, secciones 7, 10 y 13 | La restricción derogada, con el enlace | Las tres tachadas y marcadas, con el enlace |
| 4 | Leer `CLAUDE.md`, secciones 2 y 4 | Versionar y hacer commit desde la pantalla cuando exista | La 2 nombra EP-026 y la 4 el botón de la HU-007 |

**[CA-03](../HU-041-las-reglas-reconocen-la-base-de-cimiento-como-fuente-del-estandar.md#ca-03--las-reglas-pasan-sus-comprobaciones) con [CP-003](plan_pruebas.md#cp-003--los-validadores-del-estándar-pasan) y [CP-004](plan_pruebas.md#cp-004--la-versión-sube-a-5600), que las reglas pasen sus comprobaciones y queden versionadas**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr `python validadores/validar.py metareglas` | Sin fallas | `0 falla(s), 4 aviso(s)`; ninguno nombra `M10` ni `C19` |
| 2 | Correr `python validadores/validar.py estandar` | Sin fallas nuevas | `OK: sin incumplimientos.` |
| 3 | Abrir `VERSION` | Dice 56.0.0 | Dice 56.1.0: otra sesión sumó la 56.1.0 («Respondo») encima de la 56.0.0 de esta fase |
| 4 | Abrir `CHANGELOG.md` | Entrada 56.0.0, MAYOR, que nombra `20·M10` y `01·C19` | Está, debajo de la 56.1.0 de la otra sesión |

**Cómo se verificó que la pareja cumple:** los pasos 1 y 2 deciden el molde. En la primera corrida, `metareglas` avisó que `C19` medía 359 caracteres y `M10` 393, contra 320; se acortaron y la última corrida ya no los nombra (§8). El paso 3 da otra versión porque la 56.1.0 es posterior; la 56.0.0 de esta fase está en el registro.

| Caso | CA | Prioridad (del plan) | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01, RNF-01 | Crítica | 2026-10-06 | Lectura de `M10` y de la sección «M10» de `base.md` | Aprobado | EV-01 | — |
| CP-002 | CA-02 | Alta | 2026-10-06 | Lectura de `C19`, la nota, EP-016 y `CLAUDE.md` | Aprobado | EV-02 | — |
| CP-003 | CA-03 | Alta | 2026-10-06 | `validar.py metareglas` y `validar.py estandar` | Aprobado | EV-04 | DEF-01, corregido |
| CP-004 | CA-03 | Alta | 2026-10-06 | `CHANGELOG.md` con la 56.0.0 MAYOR | Aprobado | EV-03 | — |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las copias de `M10` y `C19` en `reglas-por-tarea/` quedaron iguales a las reglas | `git diff` de `cambiar-estandar.md` y `escribir-documento-1.md` después de `mapa_tareas.py` | Iguales al cuerpo nuevo |
| 2 | El ancla de la sección «M10» de `base.md` sigue igual | Búsqueda de `m10--los-tipos` | La cita un análisis aprobado; se conservó el título |

## 4. Defectos encontrados

| ID | Título | Caso que lo destapó | Severidad | Estado | Dónde quedó registrado |
|---|---|---|---|---|---|
| DEF-01 | Los cuerpos de `C19` y `M10` pasaban el largo del molde | CP-003 | Baja | Corregido | Este documento, §8 |

**Defectos abiertos que se aceptan y por qué:** ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU (`CA-0N` · `RNF-0N`) | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003, CP-004 | Aprobados | Sí |
| RNF-01 | CP-001 | Aprobado | Sí |

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de criterios y requisitos no funcionales | Plan §5 | 100 % | 4 de 4 | Sí |
| Casos críticos y altos ejecutados | Plan §5 | 100 % | 4 de 4 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios y el requisito no funcional tienen sus casos aprobados, y el único defecto quedó corregido en la misma ejecución.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Texto de la regla | `M10-…md` y `base/20-meta-reglas/base.md` |
| EV-02 | Texto | `base/01-conducta.md` (`C19`), la nota, EP-016, `CLAUDE.md` |
| EV-03 | Versión | `CHANGELOG.md`, `VERSION` |
| EV-04 | Salida de validadores | §2 de este documento |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-06 | 4 | 0 | En la primera corrida de CP-003, `metareglas` avisó que `C19` medía 359 y `M10` 393 caracteres; se acortaron y se volvió a correr |
