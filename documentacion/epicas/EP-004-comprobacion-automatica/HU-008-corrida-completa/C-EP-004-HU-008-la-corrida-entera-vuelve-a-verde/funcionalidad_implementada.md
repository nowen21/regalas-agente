# Funcionalidad implementada — Fase «C-EP-004-HU-008-la-corrida-entera-vuelve-a-verde» (módulo «Programas de comprobación — la corrida»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **qué quedó hecho**, con la trazabilidad de la historia y del plan, para que quien llegue después no tenga que deducirlo del código ni del historial.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `C-EP-004-HU-008-la-corrida-entera-vuelve-a-verde` |
| **Módulo** | Programas de comprobación — la corrida |
| **Especificación del módulo** | la del [plan_trabajo.md](plan_trabajo.md) §0 |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | [HU-008](../HU-008-corrida-completa.md) (CA-04) |
| **Fecha de cierre** | 2026-08-20 |
| **Commit** | se completa al commitear; el usuario lo autoriza aparte |

## 1. Qué se implementó — resumen

La suite entera de `validadores/tests/` volvió a `OK`. Las dos causas ajenas se cerraron: el resumen del 19 lleva la `H-` del molde, y los dos enganches que escriben índices (`historico.py` y `resumen.py`) escriben el texto del enlace con la ruta desde la raíz, como pide `13·DOC14`. Los cuatro enlaces que ya estaban mal se corrigieron.

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem de la historia | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-04 · lo que los programas escriben no pone la corrida en rojo | programa | `validadores/historico.py` (`_enlace_al_resumen`) · `validadores/resumen.py` (`_indexar_dias`) | ✅ | CP-001, CP-002 |
| CA-04 · la corrida entera en verde | prueba | `validadores/tests/` | ✅ | CP-003 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | Las dos funciones escriben el texto con la ruta desde la raíz | ✅ hecha | `validadores/historico.py` · `validadores/resumen.py` | CP-001, CP-002 |
| T-02 | Renumerar el hallazgo y corregir los cuatro enlaces | ✅ hecha | `historico-chat/resumenes/2026-08-19/sesion-3.md` · `evals/README.md` · `historico-chat/README.md` · `historico-chat/resumenes/README.md` | CP-003 |
| T-03 | Los casos y la corrida entera | ✅ hecha | `validadores/tests/test_los_indices_nacen_legibles.py` | 2 de 2, y `OK` |

**Correspondencia con el plan:** 3 tareas en el plan, 3 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba**  ·  [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md): ninguno.

**Esfuerzo real contra estimado:** cerca de diez minutos contra 1 h estimada.

## 3. Qué se probó

- **Fuente:** [resultado_pruebas.md](resultado_pruebas.md) · **Veredicto:** Cumple.
- **Suites:** la de la fase (2 de 2), y las dos enteras en `OK`.
- **Defectos abiertos aceptados:** ninguno.

## 4. Cómo se usa / puntos de entrada

- **Punto de entrada:** ninguno nuevo; los enganches del histórico y del resumen siguen corriendo como siempre.

## 5. Decisiones no obvias  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Corregir el programa y los cuatro enlaces, no solo los enlaces | Solo los cuatro: la próxima sesión agregaría el quinto | S-011 |

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| Los índices viejos de los proyectos instalados siguen con la forma anterior hasta que cada uno corra `validar.py enlaces --reparar` | Diferido por el plan | Cada proyecto, cuando quiera |

## 7. Índices y mapas actualizados

- [x] README de la HU y de la fase al día.
- N/A mapas y catálogo.

## 8. Despliegue

Los proyectos instalados reciben el cambio en su próxima sesión: los índices nuevos nacen bien. Reversión: revertir el commit.
