# Funcionalidad implementada — Fase «B-EP-005-HU-009-las-reglas-llegan-tambien-al-propio-estandar» (módulo «Automatismos — enganches»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **qué quedó hecho**, con la trazabilidad de la especificación y del plan, para que quien llegue después no tenga que deducirlo del código ni del historial.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-005-HU-009-las-reglas-llegan-tambien-al-propio-estandar` |
| **Módulo** | Automatismos — enganches |
| **Especificación del módulo** | [documentacion/automatismos/spec.md](../../../../automatismos/spec.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | [HU-009](../HU-009-lo-que-rige-cada-frase-llega-puesto.md) (CA-01, en la carpeta del propio estándar) |
| **Fecha de cierre** | 2026-08-20 |
| **Commit** | se completa al commitear; el usuario lo autoriza aparte |

## 1. Qué se implementó — resumen

Al abrir una sesión en la carpeta del estándar, el enganche de apertura entrega las reglas de `base/` completas, como a cualquier proyecto, junto con la memoria y el histórico, sin el gate `F13` y sin la revisión de instalación. Un caso nuevo en `evals/` afirma que el bloque de reglas llega.

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-31 · al propio estándar le llegan las reglas, sin gate ni revisión | programa | `adaptadores/claude-code/hook_sesion.py` (`main`, rama del estándar) | ✅ | CP-001, CP-002 |
| RN-01 a RN-03 · el reparto no cambia para los herederos | programa | `validadores/cargador.py` (sin tocar) | ✅ | CP-003 |
| La promesa queda en el banco | prueba | `evals/correr.py` (tipo `arranque`) · `evals/casos.jsonl` | ✅ | CP-005 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | La rama del estándar suma las reglas al contexto | ✅ hecha | `adaptadores/claude-code/hook_sesion.py` | CP-001 a CP-003 |
| T-02 | Casos: el estándar trae el bloque y el núcleo; un heredero sigue igual; el JSON es válido | ✅ hecha | `validadores/tests/test_las_reglas_llegan_al_propio_estandar.py` | 7 de 7 |
| T-03 | Tipo `arranque` en evals y su caso | ✅ hecha | `evals/correr.py` · `evals/casos.jsonl` | 9 de 9 casos |
| T-04 | Especificación §4.1 y §13 | ✅ hecha | `documentacion/automatismos/spec.md` (RN-31) | `validar.py estandar` OK |
| T-05 | Abrir una sesión nueva y comprobar que el bloque llega | ✅ hecha en lo que se puede desde adentro | El caso CP-001 corre el enganche real sobre la carpeta real; la apertura de la próxima sesión lo confirma y queda anotada en el resultado §3 | CP-006 |

**Correspondencia con el plan:** 5 tareas en el plan, 5 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba**  ·  [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md): ninguno.

**Esfuerzo real contra estimado:** cerca de quince minutos de sesión contra 2,1 h estimadas.

## 3. Qué se probó

- **Fuente:** [resultado_pruebas.md](resultado_pruebas.md) · **Veredicto:** Cumple.
- **Suites ejecutadas:** `validadores/tests/test_las_reglas_llegan_al_propio_estandar.py` 7 de 7; `python evals/correr.py` 9 de 9; las dos suites enteras, ver el resultado §2.
- **Verificaciones manuales:** la apertura real de la próxima sesión de este repositorio (CP-006), que se anota en el resultado cuando ocurra.
- **Defectos abiertos aceptados:** ninguno.

## 4. Cómo se usa / puntos de entrada

- **Punto de entrada:** el enganche `SessionStart`, ya instalado en este repositorio. No hay nada que configurar.
- **Permisos o datos base:** ninguno.

## 5. Decisiones no obvias  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Al estándar no se le aplica `F13` | Crear `proyectos/` para engañar al gate sería mentirle al propio `F13`; `instalar.es_el_estandar()` ya sabe que no es un proyecto | S-007 |
| No se corre la revisión de instalación en el estándar | Reportaría faltantes que no son faltantes | S-007 |
| Un caso en `evals/` además de la prueba | Quince días sin nadie que midiera la primera promesa del estándar | S-007 |

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| CP-006 (la apertura real) se cierra en la próxima sesión, no en esta | Diferido por el plan | El resultado §3 lo deja anotado con la fecha en que se confirme |

## 7. Índices y mapas actualizados

- [x] Especificación del módulo actualizada (§4.1 RN-31, §13 y la tabla de incrementos).
- [x] README de la HU (que no existía: hueco previo, `13·DOC17`) y de la fase.
- N/A el mapa de dependencias y el catálogo de módulos.

## 8. Despliegue

N/A en el sentido de producción: el cambio llega a cada proyecto corriendo `python validadores/instalar.py --todos --aplicar`, que ya se corrió sobre los 9 del registro. Reversión: revertir el commit y volver a correr el instalador.
