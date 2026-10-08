# Plan de Trabajo · Fase A-EP-027-HU-001-las-casillas (módulo Estándar en la base)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-027-HU-001-las-casillas` |
| **Épica** | `EP-027` |
| **HU** | [`HU-001`](../HU-001-las-reglas-tienen-sus-tablas-con-las-casillas-del-molde.md), una sola (`F12.1`) |
| **Módulo** | Estándar en la base: `core/estandar/` |
| **Especificación del módulo** | La HU-001 y el molde de la regla (`base/20-meta-reglas/estructura-regla.md`) |
| **Fecha apertura** | 2026-10-07 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 136](../../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md), el 2026-10-07, con la versión 57.3.0; el usuario pidió terminar la épica («continúe termine todo», 2026-10-07) |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Fase nueva: sale del acuerdo 1 del análisis 1 del pendiente 136.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-001` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-001-las-reglas-tienen-sus-tablas-con-las-casillas-del-molde.md#ca-01--las-tablas-tienen-las-casillas-del-molde) | ☐ |
| [CA-02](../HU-001-las-reglas-tienen-sus-tablas-con-las-casillas-del-molde.md#ca-02--una-regla-se-lee-en-casillas-y-se-vuelve-a-armar-igual) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** las tablas de las reglas, con las casillas del molde, y el programa que lee una regla en casillas y la vuelve a armar.

**Fuera de alcance:** llenar las tablas (HU-002) y armar desde ellas el texto que recibe el agente (HU-003).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

El estándar está en `estandar_documento` (`ruta`, `contenido`), 153 documentos. Las reglas son 270 encabezados `## <código> · <título>`: en archivos propios bajo `reglas/` o como secciones de un capítulo de un archivo. El inventario (`historico-chat/scripts/2026-10-07/inventario_reglas.py`) cuenta 24 formas; 179 son exactamente la del molde. Las demás traen avisos de derogación antes del cuerpo, notas después del ejemplo o la excepción después del ejemplo. «Validable» no está en el texto de las reglas: lo registra `validadores/reglas-validables.md`. Los enganches leen `estandar_documento` sin Django (`core/estandar/en_base.py`).

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/estandar/molde.py` | Crear | Lógica | Leer una regla en casillas y armarla; sin Django |
| `proyectos/cimiento/core/estandar/models.py` | Modificar | Modelo | `Capitulo`, `Tarea`, `Regla`, `ReglaTarea`, `Dependencia` |
| `proyectos/cimiento/core/estandar/migrations/0005_reglas.py` | Crear | Migración | Las tablas nuevas |
| `proyectos/cimiento/core/estandar/tests_molde_casillas.py` | Crear | Test | La ida y vuelta de las 270 reglas |
| `proyectos/cimiento/core/estandar/tests_tablas_reglas.py` | Crear | Test | Las tablas y sus valores |
| `historico-chat/scripts/2026-10-07/ida_y_vuelta.py` | Crear | Guion de apoyo | Muestra en qué difiere cada regla que no da el mismo texto |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| `models.py` (aditivo) | Todo `core/estandar` | `core.estandar` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

Ninguna.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

Ninguno en esta fase.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Cada casilla guarda su parte del texto, y de ella salen las partes menores (incorrecto y correcto, condición, límite y autoriza, resultado del sello) | Guardar solo las partes menores | Armar el texto exacto pide el texto de cada parte; las partes menores sirven para mostrar y comprobar | RN-07 |
| Una casilla «notas» para lo que va después del ejemplo y no es del molde | Perderlo, o mezclarlo con la exigencia | Nada se pierde; queda a la vista como lo que es | RN-07 |
| Armar con el orden del molde | Guardar el orden de cada regla | Las pocas que traían otro orden quedan como pide `20·M5` | `20·M5` |
| `Regla.documento` con `PROTECT` | Borrar las reglas con su documento | Nada se borra (`20·M11`) | RN-08 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

| Acción | Contraria |
|---|---|
| Migración `0005_reglas` | Su reversión, que quita las tablas |
| Leer una regla en casillas | Armarla desde las casillas |

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `molde.py` y su prueba de ida y vuelta | Lógica | 2 h | Ninguna | EV-01 |
| T-02 | Modelos, migración y su prueba | Modelo | 1 h | T-01 | EV-01 |

**Total estimado:** 3 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Prueba de Django | EV-01 | | ☐ |
| CA-02 | Prueba de Django | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django, con el estándar importado de `base/` |
| Usuarios de prueba | Ninguno |
| Datos precargados | El estándar |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

`manage.py migrate estandar 0004` y revertir el commit.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Aditiva: tablas nuevas, vacías; nada existente cambia.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `20·M4`, `20·M5`, `20·M7`, `20·M8`, `20·M9`, `20·M11`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Ninguno | | | |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
