# Funcionalidad implementada — Fase B-EP-001-HU-007-primero-que-el-proceso-sirva (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

> Documento de **cierre de una fase** ([`02·F6`](../../../../../base/02-flujo-de-trabajo/reglas/F6-persiste-el-trabajo-y-las-decisiones-antes-de-cerrar-la-fase.md)/[`02·F7`](../../../../../base/02-flujo-de-trabajo/reglas/F7-no-cierres-una-fase-con-trazabilidad-incompleta.md)). Consolida qué se implementó, la trazabilidad especificación → código, qué se probó y qué quedó. Se escribe en la estación de cierre, **antes del commit** de la fase.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-001-HU-007-primero-que-el-proceso-sirva` |
| **Módulo** | Cuerpo de reglas |
| **Especificación del módulo** | [HU-007](../HU-007-regla-de-las-reglas.md) — el `CA-05` es la especificación |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-007 ([CA-05](../HU-007-regla-de-las-reglas.md#ca-05--una-regla-validable-no-se-automatiza-hasta-que-se-sepa-que-sirve)) |
| **Fecha de cierre** | 2026-08-21 |
| **Commit** | Se completa al commitear — lo autoriza el usuario |

---

## 1. Qué se implementó — resumen

El estándar ya sabía decidir **si se puede** automatizar una regla (`20·M9`); ahora también decide **si conviene ya**. Antes de construirle el validador a una regla hay que responder por escrito tres preguntas —¿se cumple hoy a mano?, ¿cuántas veces se incumplió y por qué?, ¿cuántas falsas alarmas daría?—; si se incumplía por estar mal escrita, primero se corrige la regla, y si lo único que falla es acordarse, se automatiza de una vez. Con esto cierra el [pendiente 16](../../../../../pendientes/hecho/primero-que-el-proceso-sirva.md).

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem del especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «El procedimiento exige responder antes, por escrito» las tres preguntas | regla | [`base/20-meta-reglas/reglas/M19-…md`](../../../../../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md) | ✅ | Checklist CUMPLE (20 filas, 2026-08-20) |
| «Si se incumplió por estar mal escrita, manda corregir la regla antes que construir el validador» | regla | Misma regla, segunda frase | ✅ | CP-003 aprobado |
| «Si solo falla acordarse, no lo detiene» | regla | Misma regla, frase final | ✅ | CP-002 aprobado |
| «Escrito como regla del capítulo `20`» y enganchado al procedimiento | doc | [`base/20-meta-reglas/base.md`](../../../../../base/20-meta-reglas/base.md): fila del índice, sección «M19 — las tres preguntas» y paso 7 del procedimiento | ✅ | Las tres apariciones verificadas 2026-08-21 |
| Clasificación: la juzga una persona, no un programa (`M9`) | registro | [`validadores/reglas-validables.md`](../../../../../validadores/reglas-validables.md), lista del capítulo `20` | ✅ | Entrada con su motivo |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | Escribir el `CA-05` en HU-007 | ✅ hecha (línea base, 2026-08-20) | `HU-007-regla-de-las-reglas.md` | Bitácora de la HU |
| T-02 | Escribir `M19` + índice + sección + paso 7 | ✅ hecha (línea base, 2026-08-20) | `base/20-meta-reglas/` | Checklist CUMPLE |
| T-03 | Registrarla como regla de criterio | ✅ hecha (línea base, 2026-08-20) | `validadores/reglas-validables.md` | Entrada del capítulo `20` |
| T-04 | Correr el checklist de veinte filas | ✅ hecha (línea base, 2026-08-20) | `M19-…md`, bloque Checklist | 19 ✅ · 0 ❌ · 1 N/A |
| T-05 | Ejecutar los tres casos del `CA-05` | ✅ hecha (2026-08-21) | [`resultado_pruebas.md`](resultado_pruebas.md) | Ciclo 1: 3 de 3 aprobados |
| T-06 | Versionar: entrada `28.1.0` + `VERSION` | ✅ hecha (2026-08-21) | [`CHANGELOG.md`](../../../../../CHANGELOG.md) · [`VERSION`](../../../../../VERSION) | Entrada 28.1.0 |
| T-07 | Cerrar: este documento, §7 y bitácora de la HU, pendiente 16 a `hecho/`, README de la fase | ✅ hecha (2026-08-21) | Esta carpeta · `pendientes/hecho/` | `cerrar.py` y las filas de los índices |

**Correspondencia con el plan:** 7 tareas en el plan, 7 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba:** ninguno.

**Esfuerzo real contra estimado:** dentro de lo estimado (9,5 h planeadas contando la línea base); la parte del 2026-08-21 tomó una sesión corta. Lo que el plan no estimó fue el costo de **reconstruir el contexto de la sesión cortada**, que fue la mitad del trabajo real — queda como señal.

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

- **Fuente:** [`resultado_pruebas.md`](resultado_pruebas.md) · **Veredicto:** Cumple.
- **Suites ejecutadas + resultado:** ninguna suite de código — el entregable es una regla de criterio y sus tres casos son verificación manual documentada (3/3 aprobados). Los validadores del repositorio (`estandar`, `fases`, `pendientes`, `versionado`) corrieron como comprobación de no-regresión del cierre.
- **Verificaciones manuales:** los tres casos completos, más la comprobación de que ningún paso cambió estado (resultado §3).
- **Defectos abiertos que se aceptaron:** ninguno.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

- **Punto de entrada:** el paso 7 del procedimiento del capítulo [`20`](../../../../../base/20-meta-reglas/base.md): al decidir que una regla es validable (`M9`), el validador no se construye hasta responder las tres preguntas de `M19`. Las respuestas se dejan escritas en el pendiente o el plan de la automatización.
- **Permisos o datos base sembrados:** ninguno. El dato de la segunda pregunta lo da `validar.py vigencia`, que ya existía.

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Lo hecho por la sesión cortada se declaró línea base y se sometió a la misma verificación, en vez de rehacerse o de darse por bueno sin cadena | Rehacer repetía trabajo sin cambiar resultado; darlo por bueno dejaba una regla sin prueba ni versión. El incumplimiento de `F4` quedó declarado, no normalizado | S-018 |
| La subida es MENOR y no MAYOR | `M19` no obliga a un proyecto al día a hacer nada hoy; actúa al construir un validador. Mismo corte de `M17` y `M18` | — (está en el plan §2.6) |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| Ninguna | — | — |

---

## 7. Índices y mapas actualizados

- [x] §7 y bitácora de [HU-007](../HU-007-regla-de-las-reglas.md) con el estado real de la fase B.
- [x] README de la fase creado — repara el enlace del §7 que apuntaba a un archivo inexistente.
- [x] Fila del pendiente 16 en [`pendientes/README.md`](../../../../../pendientes/README.md) en forma de hecho (la dejó `cerrar.py`).
- [x] No aplica mapa de dependencias ni catálogo de módulos: no nace módulo ni cambia código.

---

## 8. Despliegue — si aplica

No aplica despliegue propio: los proyectos herederos reciben `M19` con `base/` en su próxima instalación, avisados por el desfase de versión (28.0.0 → 28.1.0, MENOR).
