# Funcionalidad implementada — Fase A-EP-001-HU-014-adoptar-la-guia-del-desarrollo-profesional (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

> Documento de **cierre de una fase** ([`02·F6`](../../../../../base/02-flujo-de-trabajo/reglas/F6-persiste-el-trabajo-y-las-decisiones-antes-de-cerrar-la-fase.md)/[`02·F7`](../../../../../base/02-flujo-de-trabajo/reglas/F7-no-cierres-una-fase-con-trazabilidad-incompleta.md)). Consolida qué se implementó, qué se probó y qué quedó. Se escribe antes del commit de la fase.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-001-HU-014-adoptar-la-guia-del-desarrollo-profesional` |
| **Módulo** | Cuerpo de reglas |
| **Especificación del módulo** | [HU-014](../HU-014-la-guia-de-entrada-del-estandar.md) — sus CA son la especificación |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-014 ([CA-01](../HU-014-la-guia-de-entrada-del-estandar.md#ca-01--la-guía-existe-en-el-estándar-completa-y-enlazada-al-cuerpo-normativo), [CA-02](../HU-014-la-guia-de-entrada-del-estandar.md#ca-02--la-guía-llega-a-los-herederos-y-se-encuentra-sin-saber-que-existe)) |
| **Fecha de cierre** | 2026-08-21 |
| **Commit** | Se completa al commitear — lo autoriza el usuario |

---

## 1. Qué se implementó — resumen

El estándar tiene ahora su puerta de entrada: [`base/guia-de-entrada.md`](../../../../../base/guia-de-entrada.md), que explica en lenguaje llano los 10 pasos del ciclo de desarrollo y las 9 cualidades del producto para producción, cada uno enlazado a la regla o capítulo que lo exige. Viaja a todos los proyectos herederos con `base/`; la escribió el usuario en el proyecto `matematica` y el estándar la adoptó. Con esto cerró el [pendiente 73](../../../../../pendientes/hecho/la-guia-de-entrada-es-del-estandar.md), con aviso a los nueve proyectos instalados.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem del especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| Documento de entrada con los 10 pasos y las 9 cualidades | doc | [`base/guia-de-entrada.md`](../../../../../base/guia-de-entrada.md) | ✅ | CP-001 pasos 1-2 |
| Cada punto enlazado a su regla o capítulo | doc | El mismo, todas sus listas | ✅ | CP-001 paso 3, `validar.py estandar` |
| Sin restos del proyecto de origen | doc | El mismo | ✅ | CP-001 paso 4 (`grep` en 0) |
| Nombrada como puerta de entrada | doc | [`base/README.md`](../../../../../base/README.md) y [mapa del sitio](../../../../../anatomia/mapa-del-sitio.md) | ✅ | CP-002 pasos 2-3 |
| Sin engordar el arranque | doc | Medición del cargador | ✅ | CP-002 paso 4: 69,9 de 90 KB; solo la línea de índice (102 bytes), desvío declarado |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | Escribir la guía desde el adjunto, enlazada y agnóstica | ✅ hecha | `base/guia-de-entrada.md` | CP-001 |
| T-02 | Nombrarla en README y mapa | ✅ hecha | `base/README.md` · `anatomia/mapa-del-sitio.md` | CP-002 |
| T-03 | Ejecutar los casos y registrar | ✅ hecha | [`resultado_pruebas.md`](resultado_pruebas.md) | Ciclo 1: 2 de 2 |
| T-04 | Versionar MENOR | ✅ hecha | [`CHANGELOG.md`](../../../../../CHANGELOG.md) 28.2.0 · `VERSION` | Entrada del 2026-08-21 |
| T-05 | Cerrar: pendiente a `hecho/` con avisos, borrar el adjunto, cierre de fase y HU | ✅ hecha | `pendientes/hecho/` + 9 avisos + esta carpeta | Salida de `cerrar.py` |

**Correspondencia con el plan:** 5 tareas en el plan, 5 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba:** ninguno. (Las referencias al adjunto en la HU y los planes pasaron a texto al borrarlo: es parte de T-05, que declaraba el borrado.)

**Esfuerzo real contra estimado:** dentro de lo estimado (5,5 h); la ejecución completa tomó una fracción de sesión.

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

- **Fuente:** [`resultado_pruebas.md`](resultado_pruebas.md) · **Veredicto:** Cumple.
- **Suites ejecutadas + resultado:** `validar.py estandar` (0 fallas sobre la guía) como comprobación de enlaces; el resto es verificación manual documentada (2 casos, 2 aprobados).
- **Verificaciones manuales:** comparación sección por sección contra el adjunto; lectura de README y mapa.
- **Defectos abiertos que se aceptaron:** ninguno. Decisión aceptada: la línea de índice de 102 bytes en el arranque (resultado §4).

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

- **Punto de entrada:** el [README de `base/`](../../../../../base/README.md) («¿Primera vez acá?») y el mapa del sitio; desde el arranque, su línea de índice.
- **Permisos o datos base sembrados:** ninguno.

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| `base/` y no `anatomia/` | `anatomia/` no viaja a los herederos; la plantilla-copia ya la había descartado el pendiente | Está en el plan §2.6 y en el CHANGELOG; no amerita señal aparte |
| La línea de índice se acepta, no se suprime | Suprimirla exigía tocar `cargador.py` (fuera del plan, `02·F8`) para ocultar lo que el CA quiere que se encuentre | Resultado §4 |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| Ninguna | — | — |

---

## 7. Índices y mapas actualizados

- [x] README de `base/` y mapa del sitio con la guía.
- [x] §7 y bitácora de HU-014 al día.
- [x] Fila del 73 en el índice del backlog en forma de hecho; la del adjunto, retirada con él.
- [x] No aplica catálogo de módulos ni mapa de dependencias: no hay código.

---

## 8. Despliegue — si aplica

Los herederos reciben la guía con `base/` en su próxima instalación (aviso de desfase 28.1.0 → 28.2.0). Los nueve proyectos instalados recibieron además el aviso de cierre del pendiente, con `matematica` incluido para reemplazar su copia por la referencia central.
