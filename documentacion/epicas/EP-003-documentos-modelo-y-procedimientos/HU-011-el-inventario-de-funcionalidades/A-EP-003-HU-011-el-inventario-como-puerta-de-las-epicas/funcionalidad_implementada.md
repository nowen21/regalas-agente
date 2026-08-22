# Funcionalidad implementada — Fase A-EP-003-HU-011-el-inventario-como-puerta-de-las-epicas (módulo Documentos modelo)   ·   `[CAPA 3]`

> Documento de **cierre de una fase** ([`02·F6`](../../../../../base/02-flujo-de-trabajo/reglas/F6-persiste-el-trabajo-y-las-decisiones-antes-de-cerrar-la-fase.md)/[`02·F7`](../../../../../base/02-flujo-de-trabajo/reglas/F7-no-cierres-una-fase-con-trazabilidad-incompleta.md)). Consolida qué se implementó, qué se probó y qué quedó. Se escribe antes del commit de la fase.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-003-HU-011-el-inventario-como-puerta-de-las-epicas` |
| **Módulo** | Documentos modelo |
| **Especificación del módulo** | [HU-011](../HU-011-el-inventario-de-funcionalidades.md) — sus CA son la especificación |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-011 ([CA-01](../HU-011-el-inventario-de-funcionalidades.md#ca-01--el-molde-del-inventario-existe-y-nace-para-madurar-hasta-manual), [CA-02](../HU-011-el-inventario-de-funcionalidades.md#ca-02--sin-inventario-aprobado-no-se-derivan-épicas), [CA-03](../HU-011-el-inventario-de-funcionalidades.md#ca-03--queda-escrito-si-la-conducta-existente-cubría-preguntar-el-alcance)) |
| **Fecha de cierre** | 2026-08-21 |
| **Commit** | Se completa al commitear — lo autoriza el usuario |

---

## 1. Qué se implementó — resumen

El alcance de un desarrollo lo confirma ahora el usuario, no el agente: toda propuesta viene con su **inventario de funcionalidades** (molde nuevo [`plantillas/inventario-funcionalidades.md`](../../../../../plantillas/inventario-funcionalidades.md)) y ninguna épica se deriva hasta que el usuario lo apruebe (regla nueva [`02·F26`](../../../../../base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md)). El inventario madura con el sistema hasta ser el manual del producto. Con esto cerró el [pendiente 74](../../../../../pendientes/hecho/el-inventario-es-la-puerta-de-las-epicas.md), con aviso a los nueve instalados.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem del especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| El molde con los cuatro estados, lo del usuario definido, preguntas abiertas y destino de manual | plantilla | [`plantillas/inventario-funcionalidades.md`](../../../../../plantillas/inventario-funcionalidades.md) | ✅ | CP-001 |
| La regla de la puerta, por el procedimiento del `20` | regla | [`02·F26`](../../../../../base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md), checklist CUMPLE 20/20 | ✅ | CP-002 |
| Su fila en el índice del capítulo | doc | [`base/02-flujo-de-trabajo/base.md`](../../../../../base/02-flujo-de-trabajo/base.md) | ✅ | CP-002 paso 2 |
| Registro `M9`/`M19` sin validador todavía | registro | [`validadores/reglas-validables.md`](../../../../../validadores/reglas-validables.md) | ✅ | CP-002 paso 5 |
| El veredicto de conducta con citas | análisis | [`resultado_pruebas.md`](resultado_pruebas.md), bloque CP-003 | ✅ | CP-003 |
| El molde en el mapa del sitio | doc | [`anatomia/mapa-del-sitio.md`](../../../../../anatomia/mapa-del-sitio.md) | ✅ | Fila puesta (y de paso la de la plantilla Django, que faltaba) |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | Escribir el molde generalizado | ✅ hecha | `plantillas/inventario-funcionalidades.md` | CP-001 |
| T-02 | Indexarlo | ✅ hecha, con desvío declarado | `anatomia/mapa-del-sitio.md` | El plan decía `plantillas/README.md`, pero ese README no indexa moldes uno a uno (solo separa modelos de fuentes de generación); el índice real de archivos es el mapa del sitio, y ahí quedó |
| T-03 | Escribir `F26` con checklist | ✅ hecha | `base/02-flujo-de-trabajo/` | CP-002 |
| T-04 | Registro con las tres preguntas de `M19` | ✅ hecha | `validadores/reglas-validables.md` | CP-002 paso 5 |
| T-05 | El veredicto de conducta | ✅ hecha | `resultado_pruebas.md` CP-003 | CP-003 |
| T-06 | Ejecutar los casos y registrar | ✅ hecha | `resultado_pruebas.md` | Ciclo 1: 3 de 3 |
| T-07 | Versionar MAYOR | ✅ hecha | CHANGELOG 29.0.0 · `VERSION` | Entrada del 2026-08-21 |
| T-08 | Cerrar: pendiente, fase y HU | ✅ hecha | `pendientes/hecho/` + 9 avisos + esta carpeta | Salida de `cerrar.py` |

**Correspondencia con el plan:** 8 tareas en el plan, 8 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba:**

| Archivo | Por qué hubo que tocarlo | Quién autorizó ampliar el plan |
|---|---|---|
| `anatomia/mapa-del-sitio.md` | Es donde de verdad se indexan los moldes (T-02); el plan nombró `plantillas/README.md` por línea base imprecisa | Consecuencia directa de la tarea aprobada; queda declarado acá en vez de forzar la fila en un README que no lista moldes |

**Esfuerzo real contra estimado:** dentro de lo estimado (8,8 h); la ejecución tomó una fracción de sesión.

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

- **Fuente:** [`resultado_pruebas.md`](resultado_pruebas.md) · **Veredicto:** Cumple.
- **Suites ejecutadas + resultado:** `validar.py metareglas` (sin hallazgos sobre `F26`), `estandar` (enlaces y marcas) y el trinquete de marcas; el resto es verificación manual documentada (3 casos, 3 aprobados).
- **Verificaciones manuales:** molde↔semilla en las dos direcciones; `F26` aplicada a los dos momentos del caso real; `shopnest-mesa` solo se leyó, nada se editó allá.
- **Defectos abiertos que se aceptaron:** ninguno.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

- **Punto de entrada:** al armar una propuesta, se copia el molde junto a ella y se llena; la regla `F26` llega con el capítulo `02` en el arranque de cada sesión y detiene la derivación de épicas hasta la aprobación del usuario.
- **Permisos o datos base sembrados:** ninguno.

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| No se extiende el capítulo `01`: la brecha de conducta la cierra `F26` en el flujo | Una conducta «pregunta el alcance» sería la misma exigencia dicha dos veces (`20·M12`); la puerta documental es más fuerte que la conducta | El veredicto completo vive en CP-003; no amerita señal aparte |
| `F26` nace sin validador, con las tres preguntas de `M19` respondidas | Construirlo ya daría falsas alarmas sin formato fijo de la cita ítem→épica | En `reglas-validables.md` |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| Ninguna | — | — |

---

## 7. Índices y mapas actualizados

- [x] Índice del capítulo `02` con la fila de `F26`.
- [x] Mapa del sitio con el molde nuevo (y la plantilla Django que faltaba); conteo 25 → 27.
- [x] §7, estado y bitácora de HU-011 al día.
- [x] Fila del 74 en el backlog en forma de hecho (la dejó `cerrar.py`).

---

## 8. Despliegue — si aplica

Los herederos reciben `F26` y el molde con su próxima instalación; el desfase 28.2.0 → 29.0.0 les avisa la MAYOR. Los nueve instalados recibieron el aviso de cierre del 74; el de `shopnest-mesa` les confirma que su inventario sirve tal cual (la única mejora anotada: la cuenta por grupo) y queda esperando la aprobación del usuario, como su propio documento declara.
