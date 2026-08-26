# Funcionalidad implementada — Fase A-EP-003-HU-009-modelo-del-resumen-de-sesion (módulo Documentos modelo)

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · [`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-003-HU-009-modelo-del-resumen-de-sesion` |
| **Módulo** | Documentos modelo |
| **Especificación del módulo** | [documentacion/documentos-modelo/spec.md](../../../../documentos-modelo/spec.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-009: [CA-01](../HU-009-modelo-del-resumen-de-sesion.md#ca-01--el-modelo-existe-y-se-distingue-de-la-transcripción), [CA-02](../HU-009-modelo-del-resumen-de-sesion.md#ca-02--un-hallazgo-dice-si-está-cerrado-y-por-dónde-sigue), [CA-03](../HU-009-modelo-del-resumen-de-sesion.md#ca-03--el-resumen-dice-si-la-sesión-se-puede-cerrar) y los tres [RNF](../HU-009-modelo-del-resumen-de-sesion.md#5-requisitos-no-funcionales) |
| **Fecha de cierre** | 2026-08-14 |
| **Commit** | `e998cc2`, autorizado el 2026-08-14 |

---

## 1. Qué se implementó — resumen

Lo que una sesión deja ahora es obligatorio escribirlo, se encuentra desde donde se busca, y un hallazgo se puede seguir aunque cruce varias sesiones.

Sirve a quien retoma un trabajo días después: entra por el índice del histórico, ve el resumen al lado de la transcripción, y desde ahí sabe qué quedó abierto y con qué pregunta seguir, sin leer la conversación.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-08 · el resumen es un documento aparte | doc | `base/13-documentacion/reglas/DOC22-…` | ✅ | CP-001 |
| RN-09 · una carpeta por día y un archivo por sesión | doc | `historico-chat/resumenes/README.md` | ✅ | Ya se cumplía; queda escrito |
| RN-10 a RN-14 · qué dice cada hallazgo | doc | `plantillas/sesion.md` | ✅ | CP-002 y CP-004 |
| RN-15 · el resumen dice de dónde viene la sesión | doc | `plantillas/sesion.md` | ✅ | CP-003 |
| RN-16 · el hallazgo que se arrastra conserva dónde nació | doc | `plantillas/sesion.md` | ✅ | CP-003 |
| El resumen se encuentra desde el índice | doc · programa | `historico-chat/README.md` · `validadores/historico.py` | ✅ | 35 de 35 líneas siguen reconociéndose |
| Cuál de los dos documentos abrir | doc | `historico-chat/resumenes/README.md` | ✅ | CP-001 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | Qué responde el resumen y qué la transcripción | ✅ hecha | `historico-chat/resumenes/README.md` | La tabla de "cuál de los dos abrir" |
| T-02 | Escribir [`DOC22`](../../../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md) con su checklist | ✅ hecha | `base/13-documentacion/reglas/DOC22-…` | La regla, checklist en CUMPLE |
| T-03 | Su fila en el índice del capítulo | ✅ hecha | `base/13-documentacion/base.md` | El índice |
| T-04 | Cómo se identifica un hallazgo entre sesiones | ✅ hecha | `plantillas/sesion.md` | `AAAA-MM-DD · tema · H-N` |
| T-05 | Qué hace la sesión que hereda un hallazgo | ✅ hecha | `plantillas/sesion.md` | "El hallazgo que se hereda no se copia" |
| T-06 | Revisar `historico.py` antes de tocar el índice | ✅ hecha | — | Encontró que había que modificarlo |
| T-06b | Modificar `historico.py` | ✅ hecha | `validadores/historico.py` | 35 de 35 líneas reconocidas |
| T-07 | Enlazar el resumen en la línea de cada sesión | ✅ hecha | `historico-chat/README.md` | Las dos sesiones que tienen resumen |
| T-08 | Comprobar la sección de cierre | ✅ hecha | — | CP-004 |
| T-09 | Medir cuánto se demora leer un resumen | ✅ hecha | — | CP-005: 2.426 palabras el más largo |
| T-10 | Retomar un hallazgo sin la transcripción | ✅ hecha | — | CP-002 |
| T-11 | Comparar los dos resúmenes campo por campo | ✅ hecha | — | CP-006: los 12 campos, idénticos |
| T-12 | [`DOC22`](../../../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md) en `reglas-validables.md` | ✅ hecha | `validadores/reglas-validables.md` | Su fila |
| T-13 | `CHANGELOG.md` y `VERSION` | ✅ hecha | — | Versión 14.0.0 |

**Correspondencia con el plan:** 14 tareas en el plan, 14 acá. Cuadra.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba**  ·  [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md):

| Archivo | Por qué hubo que tocarlo | Quién autorizó ampliar el plan |
|---|---|---|
| `validadores/historico.py` | El plan lo declaraba solo para revisar, y la revisión mostró que el índice no se puede tocar sin él | El usuario, el 2026-08-14, antes de escribir la primera línea |

**Esfuerzo real contra estimado:** 17 h estimadas tras la ampliación, contra las 15 del plan aprobado. Lo que se subestimó fue el índice: se declaró como documentación cuando en realidad lo escribe un programa.

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

- **Fuente:** [resultado_pruebas.md](resultado_pruebas.md) · **Veredicto:** Cumple.
- **Suites corridas + resultado:** `validar.py estandar`, 0 fallas y 2 avisos que ya venían de antes.
- **Verificaciones manuales** ([`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)):
  - Retomar un hallazgo abierto real sin abrir su transcripción.
  - Seguir el H-4 del 2026-08-14 en las dos direcciones, entre las dos sesiones que lo tocaron.
  - Leer entero el resumen más largo y comparar campo por campo los dos.
  - Pasar las 35 líneas del índice del histórico por el reconocedor del programa, antes y después de agregarle el enlace.
- **Defectos abiertos que se aceptaron:** DEF-01, el campo «viene de» que le falta al resumen más viejo. Estaba fuera de alcance desde el plan.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

- **Punto de entrada:** el índice de [`historico-chat/README.md`](../../../../../historico-chat/README.md). Cada línea de sesión lleva su transcripción y, después del `·`, su resumen.
- **Permisos o datos base sembrados:** N/A.

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / `DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El resumen se enlaza por sesión, no por día | Cada sesión resuelve un tema. Se descartó una línea por día porque obliga a abrir la carpeta y adivinar cuál era | `historico-chat/README.md` |
| Un hallazgo se nombra `AAAA-MM-DD · tema · H-N` | La numeración corrida entre sesiones necesita un contador único, y dos sesiones abiertas a la vez lo rompen. Ya pasó con la versión: pendiente 22 | `plantillas/sesion.md` |
| El hallazgo heredado no se copia | Dos copias del mismo hallazgo terminan diciendo cosas distintas | `plantillas/sesion.md` |
| El enlace al resumen solo se escribe si el resumen existe | Un enlace roto en el índice es peor que no tenerlo | `validadores/historico.py` |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| [`DOC22`](../../../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md) obliga y ningún programa lo comprueba todavía | Diferido por el plan | EP-004, anotado en `validadores/reglas-validables.md` |
| El resumen más viejo no tiene el campo «viene de» | Diferido por el plan | Se llena si alguna vez se toca ese archivo |
| El índice del histórico se declaró como documentación cuando lo escribe un programa | No previsto | Ya corregido en esta misma fase; queda la lección en §13 del plan |

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / `DOC13`

- [x] Índice del capítulo 13 con [`DOC22`](../../../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md).
- [x] Índice del histórico con el enlace al resumen de cada sesión.
- [x] Índice de la carpeta de resúmenes, con los dos días.
- [x] `validadores/reglas-validables.md` con [`DOC22`](../../../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md).
- [x] Especificación del módulo al día con lo realmente implementado.
- [ ] Mapa de dependencias vivo (`DOC9`): N/A, este repositorio no lo tiene.
- [ ] Catálogo de módulos (`DOC13`): N/A, este repositorio no lo tiene.

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

- Cambios de esquema / migraciones: N/A.
- Datos base / permisos: N/A.
- Comandos post-deploy: un proyecto que herede corre su instalador para recibir el modelo y el programa del histórico.
- Reversión: revertir el commit. El índice vuelve a la línea sin enlace, y el programa a reconocer solo esa forma.
