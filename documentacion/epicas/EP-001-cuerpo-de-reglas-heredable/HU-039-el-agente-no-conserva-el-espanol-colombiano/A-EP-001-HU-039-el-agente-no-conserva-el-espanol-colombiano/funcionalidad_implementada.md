# Funcionalidad implementada · Fase `A-EP-001-HU-039-el-agente-no-conserva-el-espanol-colombiano` (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-001-HU-039-el-agente-no-conserva-el-espanol-colombiano` |
| **Módulo** | Cuerpo de reglas, capítulo 00 |
| **Especificación del módulo** | Las reglas de negocio RN-01 a RN-04 de [HU-039](../HU-039-el-agente-no-conserva-el-espanol-colombiano.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-039 (CA-01 a CA-07) |
| **Fecha de cierre** | 2026-09-27 |
| **Versión del estándar al cerrar** | 38.2.0 |
| **Commit** | Se completa al commitear |

## 1. Qué se implementó, resumen

Existe la regla `00·ID12`, «Escribe con la norma del español de Colombia», con su anexo `espanol-de-colombia.md`: ortografía, léxico, gramática y redacción. Rige cuando el proyecto declara español de Colombia. El léxico que estaba en el anexo de marcas quedó solo en el anexo nuevo, y el recordatorio de cada turno trae ahora `ID11` e `ID12`.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-01 · rige documentos y chat si el proyecto declara español de Colombia | doc | `base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md` | ✅ | CP-002, CP-006 |
| RN-02 · cuatro frentes | doc | La regla y `base/00-identidad-y-rol/espanol-de-colombia.md` | ✅ | CP-002, CP-003 |
| RN-03 · la variedad no basta, también la norma | doc | El ejemplo de la regla | ✅ | CP-005 |
| RN-04 · el léxico en un solo sitio | doc | `base/00-identidad-y-rol/marcadores-de-ia.md` y el anexo nuevo | ✅ | CP-004 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | Crear el archivo de la regla | ✅ hecha | El archivo de la regla | CP-001 |
| T-02 | Su fila en la tabla del capítulo | ✅ hecha | `base/00-identidad-y-rol/base.md` | CP-001 |
| T-03 | El cuerpo con la condición, los frentes y la dependencia | ✅ hecha | El archivo de la regla, 278 caracteres leídos | CP-002 |
| T-04 | El anexo con sus cuatro secciones | ✅ hecha | `base/00-identidad-y-rol/espanol-de-colombia.md` | CP-003 |
| T-05 | Llevar el léxico de la sección 5 al anexo | ✅ hecha | `marcadores-de-ia.md` §5 | CP-004 |
| T-06 | El cierre de `marcadores-de-ia.md` cita `ID10` e `ID12` | ✅ hecha | `marcadores-de-ia.md`, «Lo que este anexo no cubre» | CP-004 |
| T-07 | El ejemplo con una falta de cada frente | ✅ hecha | El archivo de la regla | CP-005 |
| T-08 | La condición al comienzo del cuerpo | ✅ hecha | El archivo de la regla | CP-006 |
| T-09 | La clasificación en `reglas-validables.md` | ✅ hecha | `validadores/reglas-validables.md` | CP-007 |
| T-10 | `ID12` en `CADA_TURNO` de `hook_reglas.py` | ✅ hecha, y con `ID11` | `adaptadores/claude-code/hook_reglas.py` | Verificación manual 1 |
| T-11 | Versión 38.2.0 | ✅ hecha | `CHANGELOG.md` y `VERSION` | CP-008 |
| T-12 | Cerrar el pendiente 96 y actualizar HU-039 | ✅ hecha | `pendientes/96-...md`, `pendientes/README.md` y HU-039 | — |

**Correspondencia con el plan:** 12 tareas en el plan, 12 aquí.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno. La T-10 agregó también `ID11`, en el mismo archivo declarado, porque el usuario pidió resolverlo en esta fase en vez de anotarlo como pendiente.

**Esfuerzo real contra estimado:** cerca de 2 h reales contra 4,8 h del plan. Se sobrestimó el anexo: la mitad de su contenido ya existía en la sección 5 del anexo de marcas.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | Cumple |

- Suites ejecutadas y resultado: `metareglas`, `estandar`, `marcas`, `pendientes` y `ejecutable`, sin fallas; `test_toda_entrada_del_registro_declara_su_tipo`, OK.
- Verificaciones manuales:
  - El recordatorio de cada turno trae `ID11` e `ID12`.
  - El léxico del anexo se entiende en todo el país.
- Defectos abiertos que se aceptaron: ninguno.

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

- Punto de entrada: la regla le llega al agente al abrir la sesión y en el recordatorio de cada turno.
- Permisos o datos base sembrados: no aplica.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La sección 5 de `marcadores-de-ia.md` conserva dos filas | Mezclar *usted* y *tú* y el español neutro sin giro propio son marcas de texto generado, no norma; se descartó moverlas al anexo | En el plan §2.6 y en la sección 5 misma |
| `ID11` entra en el recordatorio de cada turno junto con `ID12` | El usuario pidió resolverlo en esta fase en vez de dejarlo como pendiente | En el `estado-fase.md` §2 |

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino (fase futura / ticket / `pendientes/`) |
|---|---|---|
| Contar en `marcas.py` las tildes de pregunta, los signos de apertura y el léxico de España | Diferido por el plan | Queda declarado en `validadores/reglas-validables.md`, en la fila de `ID12` |

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] Tabla de reglas del capítulo 00 actualizada.
- [x] Registro de reglas comprobables actualizado.
- [x] Índice de pendientes con el 96 cerrado.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica: la regla entra con la versión 38.2.0, y los proyectos la reciben al actualizar el estándar.
