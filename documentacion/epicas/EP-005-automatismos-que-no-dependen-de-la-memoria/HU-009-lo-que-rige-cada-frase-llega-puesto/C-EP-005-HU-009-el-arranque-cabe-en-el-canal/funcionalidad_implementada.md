# Funcionalidad implementada · Fase `C-EP-005-HU-009-el-arranque-cabe-en-el-canal` (módulo Adaptador y validadores)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-005-HU-009-el-arranque-cabe-en-el-canal` |
| **Módulo** | El enganche de arranque, `validadores/` y los `CLAUDE.md` |
| **Especificación del módulo** | RN-06 de [HU-009](../HU-009-lo-que-rige-cada-frase-llega-puesto.md), y la regla 62 de [documentacion/automatismos/spec.md](../../../../automatismos/spec.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), versión 2 |
| **HU / CA cubiertas** | HU-009 (CA-04, que reemplaza al CA-01) |
| **Fecha de cierre** | 2026-09-28 |
| **Versión del estándar al cerrar** | 39.4.0 |
| **Commit** | Se completa al commitear |

## 1. Qué se implementó, resumen

El arranque ya no manda las reglas: manda cómo llegan, con cada mensaje, y dónde está el mapa de tareas. Todo lo que entrega, con la memoria y el histórico, cabe en los 10.000 caracteres que acepta la herramienta por enganche; lo que no cabe se recorta por renglones enteros y se dice dónde está completo. Ningún texto vigente del estándar ni de la plataforma dice ya que las reglas llegan al abrir.

## 2. Trazabilidad  ·  `13·DOC11`

| Tarea | Qué se hizo | Dónde quedó | Evidencia |
|---|---|---|---|
| T-01 | La instrucción corta en vez de las reglas; el gate igual | `validadores/cargador.py` | CP-001 |
| T-02 | Tope en caracteres, recorte por renglones y ruta de lo completo | `validadores/recuerdos.py`, `validadores/historico.py` | CP-002 |
| T-03 | Tope de 10.000 caracteres y armado por prioridad | `adaptadores/claude-code/hook_sesion.py` | CP-001, CP-002 |
| T-04 | Cómo llegan las reglas | `CLAUDE.md`, `plantillas/CLAUDE.md.plantilla` | CP-003 |
| T-05 | Guías al día | `validadores/docs/cargador.md`, `hook_sesion.md`, `recuerdos.md`, `historico.md` | CP-003 |
| T-06 | Pruebas reescritas y la que falla por encima del tope | `validadores/tests/test_las_reglas_llegan_al_propio_estandar.py`, `validadores/pruebas.py`, `evals/casos.jsonl` | CP-001, CP-002 |
| T-07 | `39.4.0`, MENOR | `CHANGELOG.md`, `VERSION` | CP-004 |
| T-08 | Cierre de HU-009, del pendiente 101 y del H-1 | HU-009, `pendientes/`, resumen de la sesión | — |
| T-09 | Los avisos de cada mensaje y los comentarios del código | `hook_reglas.py`, `recuperar.py`, `instalar.py`, `marcas.py`, `relacionadas.py`, `enlaces.py` | CP-005 |
| T-10 | El comentario del caso de arranque | `evals/correr.py` | CP-005 |
| T-11 | Anatomía, glosario, README de `base/` y de `validadores/` | `anatomia/mapa-del-sitio.md`, `base/glosario.md`, `base/README.md`, `validadores/README.md`, `validadores/docs/README.md` | CP-005 |
| T-12 | La fila del despliegue | `cvds/despliegue/README.md` | CP-005 |
| T-13 | La nota de la compactación | `notas/compactacion-mata-decisiones.md` | CP-005 |
| T-14 | Criterios reemplazados, marcas y título nuevo | HU-009, su épica y sus índices, y la prueba del andamio | CP-005 |
| T-15 | La búsqueda final; la especificación del módulo con la regla 62 | `documentacion/automatismos/spec.md` | CP-005 |

**Faltantes / diferimientos:** ninguno. Lo de la plataforma lo cerró la fase [`A` de EP-016 HU-005](../../../EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/HU-005-entregarle-las-reglas-al-agente/A-EP-016-HU-005-la-promesa-dice-cuando-llegan-las-reglas/funcionalidad_implementada.md).

## 3. Qué se probó

| Qué | Resultado |
|---|---|
| CP-001 a CP-005 | Cumple; detalle en [resultado_pruebas.md](resultado_pruebas.md) |
| Pruebas tocadas | 77 en OK, más las 12 del andamio |
| `validar.py estandar` y `versionado` | Sin incumplimientos |
