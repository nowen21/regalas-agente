# Funcionalidad implementada · Fase `A-EP-001-HU-038-el-agente-agrega-informacion-irrelevante-al-asunto` (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-001-HU-038-el-agente-agrega-informacion-irrelevante-al-asunto` |
| **Módulo** | Cuerpo de reglas, capítulo 00 |
| **Especificación del módulo** | Las reglas de negocio RN-01 a RN-04 de [HU-038](../HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-038 ([CA-01](../HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md#ca-01--la-regla-existe-con-su-identificador-y-su-checklist), [CA-02](../HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md#ca-02--el-cuerpo-de-la-regla-recoge-las-cuatro-reglas-de-negocio), [CA-03](../HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md#ca-03--la-regla-declara-en-qué-se-apoya), [CA-04](../HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md#ca-04--la-regla-queda-clasificada-como-no-validable)) |
| **Fecha de cierre** | 2026-09-27 |
| **Versión del estándar al cerrar** | 38.1.0 |
| **Commit** | Se completa al commitear |

## 1. Qué se implementó, resumen

Existe la regla `00·ID11`, «Escribe solo lo pertinente al asunto». Exige que lo que el agente entrega, en documentos y en el chat, se limite al asunto: un dato es pertinente si se relaciona con el tema, el objetivo y el alcance de lo que se trata, y el que no lo es se omite aunque sea corto y correcto.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-01 · rige documentos y chat | doc | `base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md` | ✅ | CP-002 |
| RN-02 · pertinente si se relaciona con el tema, el objetivo y el alcance | doc | El mismo archivo | ✅ | CP-002 |
| RN-03 · lo no pertinente se omite aunque sea breve, claro y correcto | doc | El mismo archivo | ✅ | CP-002 |
| RN-04 · ser corto no lo vuelve pertinente | doc | El mismo archivo | ✅ | CP-002 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | Crear el archivo de la regla con encabezado, ejemplo y checklist | ✅ hecha | `base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md` | CP-001 |
| T-02 | Agregar su fila a la tabla del capítulo | ✅ hecha | `base/00-identidad-y-rol/base.md` | CP-001 |
| T-03 | Redactar el cuerpo con RN-01 a RN-04 | ✅ hecha | El archivo de la regla, 318 caracteres leídos | CP-002 |
| T-04 | Declarar que extiende `ID7`, `ID8` e `ID9` | ✅ hecha | El archivo de la regla | CP-003 |
| T-05 | Clasificarla como no validable | ✅ hecha | `validadores/reglas-validables.md` | CP-004 |
| T-06 | Registrar la regla y subir `VERSION` a 38.1.0 | ✅ hecha | `CHANGELOG.md` y `VERSION` | CP-005 |
| T-07 | Cerrar el pendiente 95 y actualizar HU-038 | ✅ hecha | `pendientes/95-...md`, `pendientes/README.md` y HU-038 | — |

**Correspondencia con el plan:** 7 tareas en el plan, 7 aquí.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`):

| Archivo | Por qué hubo que tocarlo | Quién autorizó ampliar el plan |
|---|---|---|
| `pendientes/96-la-norma-del-espanol-de-colombia-no-tiene-regla.md` y `pendientes/97-el-andamio-exige-la-historia-antes-que-el-pendiente.md` | El plan aprobado los incluía, y se les quitó una frase no pertinente a cada uno. Después el usuario decidió que aplicar la regla a esos pendientes no es parte de esta fase y salió del plan; las dos frases quedan quitadas | El usuario, 2026-09-27 |

**Esfuerzo real contra estimado:** cerca de 1,5 h reales contra 1,9 h del plan. Se subestimó la conversación sobre el título: el imperativo de `20·M5` no se había mirado al elegirlo.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | Cumple |

- Suites ejecutadas y resultado: `metareglas`, `estandar` y `pendientes`, sin fallas; `test_toda_entrada_del_registro_declara_su_tipo`, OK.
- Verificaciones manuales:
  - Que las cuatro RN estén en el cuerpo de la regla: están.
- Defectos abiertos que se aceptaron: ninguno.

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

- Punto de entrada: la regla le llega al agente al abrir la sesión, porque el arranque carga todas las reglas de `base/`.
- Permisos o datos base sembrados: no aplica.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El encabezado en imperativo, «Escribe solo lo pertinente al asunto», y el archivo con el nombre de la HU | `20·M5` exige título imperativo; se descartó usar el título de la HU en el encabezado, que habría dejado la fila 8 del checklist en ❌ | En el checklist de la regla, fila 8 |
| Aplicar la regla a los pendientes 96 y 97 sale de esta fase | Crear la regla y aplicarla a documentos ya escritos son trabajos distintos, y el RNF-02 dice que ningún documento ya escrito se reescribe por ella | En el `estado-fase.md` §2 |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] Tabla de reglas del capítulo 00 actualizada.
- [x] Registro de reglas comprobables actualizado.
- [x] Índice de pendientes con el 95 cerrado.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica: la regla entra con la versión 38.1.0, y los proyectos la reciben al actualizar el estándar.
