# Plan de Trabajo · Fase `A-EP-023-HU-008-el-plan-cita-el-analisis-que-lo-aprueba` (módulo `base/02-flujo-de-trabajo/` y `proyectos/cimiento/core/enganches/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-023-HU-008-el-plan-cita-el-analisis-que-lo-aprueba` |
| **Épica** | [EP-023](../../epica.md) |
| **HU** | [HU-008](../HU-008-aprobar-el-analisis-aprueba-lo-que-sale-de-el.md), una sola (`F12.1`) |
| **Módulo** | `base/02-flujo-de-trabajo/`, `plantillas/ciclo-vida-proyectos/`, `proyectos/cimiento/core/enganches/` |
| **Especificación del módulo** | Los CA de la [HU-008](../HU-008-aprobar-el-analisis-aprueba-lo-que-sale-de-el.md) |
| **Fecha apertura** | 2026-10-04 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva. Sale del punto 8 del [análisis 1 del pendiente 116](../../../../../historico-chat/resumenes/2026-10-04/pendientes/116-el-codigo-de-cimiento-se-repite-en-vez-de-reusarse/analisis-1.md) (acuerdo 6).

**Carencias que cierra** (`02·F14` Q3): con el análisis aprobado, cada plan que sale de él pide otra aprobación que repite lo ya decidido.

**Aprobación** (`02·F4`): Ing. José Dúmar Jiménez Ruíz, el 2026-10-04, con la versión 53.3.0

**Disparo** (`02·F15`, etapa 2): el usuario pidió construir lo decidido en el análisis el 2026-10-04 con «Hágalo: el 1».

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-008 | Estado |
|---|---|
| CA-01 · Las reglas dicen que el análisis aprobado aprueba sus planes | ☐ |
| CA-02 · El plan aprobado por un análisis lo cita, y el programa lo acepta | ☐ |
| CA-03 · La plantilla del plan permite citar el análisis | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que un plan cuya línea de aprobación cita un análisis aprobado que nombra su HU cuente como aprobado, en las reglas, en la plantilla y en el programa.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | `02·F4` y `02·F25` | Regla | Baja |
| CA-02 | La aprobación que cita un análisis, válida o no | Programa | Media |
| CA-03 | La fila **Aprobación** de la plantilla | Plantilla | Baja |

**Fuera de alcance:** las demás filas del análisis 1 del pendiente 116.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-04, sobre la versión 53.3.0:

- `PlanDeTrabajo.aprobacion()` de `proyectos/cimiento/core/enganches/plan_vs_hecho.py` lee la línea `**Aprobación**` como «quién, el fecha, con la versión X.Y.Z»; `aprobado_desde()` solo mira la versión.
- Lo llaman `core/enganches/freno.py` (línea 127, qué rutas deja escribir), `core/enganches/plan_vs_hecho.py` (líneas 264 y 332, el commit contra el plan) y `core/enganches/origen.py` (línea 221). `core/validadores/flujo.py` usa `revisar_aprobado()` y `core/enganches/acuerdos.py` usa `aprobacion()`.
- Un análisis aprobado lleva la línea `> **Aprobado**` (`core/enganches/analisis_en_curso.py`, línea 54), y su sección «Lo que se tiene que hacer» nombra la HU de cada fila (por ejemplo «`EP-023` HU-008»).
- `F4` y `F25` se copian en `base/reglas-por-tarea/cambiar-codigo-4.md`, `recibir-pedido.md`, `trabajar-cadena-1.md` y `trabajar-cadena-2.md`, que escribe `core/herramientas/mapa_tareas.py`.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md` | Modificar | Regla | El análisis aprobado aprueba sus planes; su sello |
| `base/02-flujo-de-trabajo/reglas/F25-autorizar-el-arranque-no-aprueba-el-plan.md` | Modificar | Regla | El segundo OK no se pide si lo dio el análisis; su sello |
| `base/reglas-por-tarea/cambiar-codigo-4.md`, `base/reglas-por-tarea/recibir-pedido.md`, `base/reglas-por-tarea/trabajar-cadena-1.md`, `base/reglas-por-tarea/trabajar-cadena-2.md` | Modificar | Generado | Los vuelve a escribir `mapa_tareas.py` |
| `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` | Modificar | Plantilla | La fila **Aprobación** con las dos formas |
| `proyectos/cimiento/core/enganches/plan_vs_hecho.py` | Modificar | Programa | `PlanDeTrabajo.aprobado()` acepta el análisis aprobado que nombra la HU |
| `proyectos/cimiento/core/enganches/freno.py`, `proyectos/cimiento/core/enganches/origen.py` | Modificar | Programa | Llaman a `aprobado()` con la ruta del plan |
| `proyectos/cimiento/core/enganches/tests_freno.py` | Modificar | Pruebas | Los casos del plan de pruebas |
| `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/HU-008-aprobar-el-analisis-aprueba-lo-que-sale-de-el/HU-008-aprobar-el-analisis-aprueba-lo-que-sale-de-el.md` | Modificar | Documentación | La fila de esta fase |
| `CHANGELOG.md`, `VERSION` | Modificar | Versión | Versión MAYOR: 54.0.0 |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| `PlanDeTrabajo.aprobado_desde(texto)` | `freno.py`, `plan_vs_hecho.py`, `origen.py` | Se suma `aprobado(ruta_plan, texto, desde)`, que además valida el análisis citado; `aprobado_desde()` queda para quien no tiene la ruta |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Se cambian `F4` y `F25`, sin regla nueva | Crear una regla | Así lo acordó el usuario | Análisis 1, acuerdo 6 |
| La aprobación cita el análisis con un enlace en el lugar de «quién»: «[análisis N del pendiente P](ruta), el AAAA-MM-DD, con la versión X.Y.Z» | Un campo aparte | El programa ya lee esa línea; cambiar su forma rompería los planes aprobados | Análisis 1, acuerdo 6 |
| El análisis citado vale si tiene la marca `> **Aprobado**` y su «Lo que se tiene que hacer» nombra la HU del plan | Aceptar cualquier análisis citado | Lo que el análisis no contempló pide aprobación otra vez | Análisis 1, acuerdo 6 |
| Versión MAYOR | MENOR | Así lo dice el punto 8: cambia cómo se aprueba en todo proyecto | Análisis 1, acuerdo 6 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| Plan que sale de un análisis aprobado | Pide su propio OK | Queda aprobado citando el análisis | `02·F4`, `02·F25` |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-01 · Las reglas dicen que el análisis aprobado aprueba sus planes

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | `F4` y `F25` dicen que el plan que sale de un análisis aprobado y cumple sus filas queda aprobado; lo no contemplado pide el OK. Checklist, sello y `mapa_tareas.py` | `base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md`, `base/02-flujo-de-trabajo/reglas/F25-autorizar-el-arranque-no-aprueba-el-plan.md`, `base/reglas-por-tarea/cambiar-codigo-4.md`, `base/reglas-por-tarea/recibir-pedido.md`, `base/reglas-por-tarea/trabajar-cadena-1.md`, `base/reglas-por-tarea/trabajar-cadena-2.md` | CA-01 | Todo proyecto que adopte la versión | 1 h | Ninguna | CP-001 |

### CA-02 · El plan aprobado por un análisis lo cita, y el programa lo acepta

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-02 | `PlanDeTrabajo.aprobado(ruta_plan, texto, desde)`: si «quién» enlaza un `analisis-N.md`, el análisis tiene que estar aprobado y nombrar la HU del plan | `proyectos/cimiento/core/enganches/plan_vs_hecho.py` | CA-02 | El freno y el commit | 1,5 h | Ninguna | CP-002 |
| T-03 | El freno y el origen llaman a `aprobado()` | `proyectos/cimiento/core/enganches/freno.py`, `proyectos/cimiento/core/enganches/origen.py` | CA-02 | Toda escritura en una fase | 0,5 h | T-02 | CP-002 |

### CA-03 · La plantilla del plan permite citar el análisis

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | La fila **Aprobación** muestra las dos formas | `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` | CA-03 | Todo plan nuevo | 0,5 h | Ninguna | CP-003 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-05 | Los casos del plan de pruebas; la fila de la fase en la HU; la versión 54.0.0 | `proyectos/cimiento/core/enganches/tests_freno.py`, `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/HU-008-aprobar-el-analisis-aprueba-lo-que-sale-de-el/HU-008-aprobar-el-analisis-aprueba-lo-que-sale-de-el.md`, `CHANGELOG.md`, `VERSION` | CA-01 a CA-03 | Todo proyecto adopta la versión | 0,5 h | T-01 a T-04 | CP-001 a CP-003 |

## 4. Secuencia de ejecución

T-01, T-02, T-03 y T-04; al final T-05, con los validadores, las pruebas de la fase y la medición de marcas (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Leer `F4`, `F25`, `CHANGELOG.md` y `VERSION`; `validar.py metareglas` sin fallas nuevas | CP-001 |
| CA-02 | Un plan que cita un análisis aprobado que nombra su HU, uno sin aprobar y uno que no la nombra | CP-002 |
| CA-03 | Leer la fila **Aprobación** de la plantilla | CP-003 |

## 6. Datos y ambiente de prueba

Un proyecto de prueba en una carpeta temporal, con una fase en curso, su plan y un análisis en `pendientes/`.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Aditiva: los planes aprobados por una persona siguen valiendo igual; la forma nueva es una opción más.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`02·F4`, `02·F25`, `02·F8`, `20·M5`, `20·M10`, `20·M12`, `02·F27`, `00·ID8`, `00·ID9`, `02·F5`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Que un análisis apruebe un plan que no contempló | Se exige que nombre la HU del plan |

## 11. Definition of Done

- [ ] CA-01 a CA-03 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Los validadores y las pruebas de la fase sin fallas, y cero marcas nuevas.
- [ ] `VERSION` y `CHANGELOG.md` al día.
- [ ] Aprobación del usuario.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 5 tareas quedaron hechas el 2026-10-04, con la versión 54.0.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** 1. La carpeta `proyectos/cimiento/.venv/` apareció a mitad de la fase y el freno la tomó por escrituras; se resolvió ignorándola en `.gitignore`, con la aprobación del usuario.
