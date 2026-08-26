# Funcionalidad implementada — Fase A-EP-006-HU-006-retrodocumentar-el-vaciado-del-almacen-local (módulo Memoria)

> **Veredicto de la fase: [No cumple](resultado_pruebas.md#6-veredicto-de-la-fase).** El almacén de esta máquina está **vacío**, el recogido lo vacía y no deja ni el texto ni un puntero. Falla un solo punto: **se lleva también lo que no es un recuerdo**, y resolverlo toca `01·C19`.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-006-retrodocumentar-el-vaciado-del-almacen-local` |
| **Módulo** | Memoria — [`validadores/recuerdos.py`](../../../../../validadores/recuerdos.py) y [`validadores/hook_recuerdos.py`](../../../../../validadores/hook_recuerdos.py) |
| **Especificación del módulo** | No la hay aparte: la especificación son los CA de [HU-006](../HU-006-sacar-del-almacen-local.md) y [`01·C19`](../../../../../base/01-conducta.md#c19--escribe-la-memoria-del-agente-dentro-del-repositorio-del-proyecto) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-006: [CA-01](../HU-006-sacar-del-almacen-local.md#ca-01--el-almacén-queda-vacío), [CA-02](../HU-006-sacar-del-almacen-local.md#ca-02--no-queda-un-puntero-en-lugar-del-texto), su RNF y sus dos transversales |
| **Fecha de cierre** | 2026-08-17 |
| **Commit** | Pendiente de autorización del usuario |

---

## 1. Qué se implementó — resumen

**Nada de programa: la fase escribió las pruebas que faltaban y midió el estado real.** El recogido está en producción y ya tenía doce casos. Lo que no había era la prueba del **puntero puesto a mano** —el escenario que el CA-02 nombra— ni la constancia de qué hay de verdad en el almacén de esta máquina.

Hay nada, que es lo correcto.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| El almacén queda vacío tras recoger | programa | [`recuerdos.migrar`](../../../../../validadores/recuerdos.py) | ✅ Ya existía | CP-001 |
| Recoger **nunca borra**: mueve, y si el nombre choca renombra | programa | El mismo, `_libre()` | ✅ Ya existía | Verificación 2 |
| Correr con el almacén vacío no falla | programa | `sueltos()` devuelve `[]` | ✅ Ya existía | CP-001, paso 4 |
| **El puntero también se saca** | programa | `sueltos()` no distingue: se lleva todo `.md` | ✅ Ya existía | CP-002 |
| **Dejar lo que no es un recuerdo** | programa | `sueltos()` se lleva todo archivo | ❌ **No existe** | CP-001, paso 5 |
| El disparo al abrir y al escribir | programa | [`hook_recuerdos.py`](../../../../../validadores/hook_recuerdos.py) | ✅ Ya existía | CP-003 |
| Las cinco exigencias, con red | pruebas | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `ElAlmacenLocalQuedaVacio` | ✅ Escritas acá | 6 pruebas |

### 2.2 Criterios de aceptación

| CA | Cómo quedó cubierto | Estado |
|---|---|---|
| CA-01 | El almacén queda vacío, y el real lo está. **Pero se lleva lo que no es recuerdo** | ❌ |
| CA-02 | Ni el texto ni el puntero sobreviven; el del repositorio queda intacto y único | ✅ |
| RNF · no hay dos versiones | 0 en el almacén, 1 en el repositorio | ✅ |
| Transversal · Límites | Mayúsculas: `MEMORY.md` y `memory.md` son el mismo archivo en Windows, y el recogido no pisa el índice | ✅ |
| Transversal · Privacidad | Lo movido pasa por el mismo detector de secretos que el resto: 0 hallazgos | ✅ |

---

## 3. Lo que la fase midió

| Medición, 2026-08-17 | Valor |
|---|---|
| Archivos en el almacén local de esta máquina | **0** |
| Recuerdos en el repositorio | 18 |
| Recuerdos borrados a mano durante la fase | **0** |
| Punteros que sobreviven al recogido | **0** |
| Archivos que no son recuerdos llevados por error | **1**, en la prueba |

**Que el almacén esté vacío no significa que nadie use la memoria:** los 18 recuerdos están en el repositorio y el enganche corre al abrir la sesión y cada vez que se escribe un archivo. El cero es la prueba de que el automatismo trabaja.

---

## 4. El punto que no cumple, y por qué no se parcheó

`sueltos()` devuelve **todo archivo** del almacén, no solo los `.md` de recuerdo. Un `config.json` de la herramienta terminaría en `historico-chat/memory/`.

**Parecería un defecto de una línea, y no lo es.** Dejarlo sería incumplir `01·C19`, que exige el almacén **vacío**; con un archivo ajeno dentro, la revisión reprobaría para siempre por algo que ni siquiera es un recuerdo.

| Salida | Qué cuesta |
|---|---|
| **A** · que el recogido distinga y deje lo demás | Hay que relajar `C19` y decirle a la revisión qué ignorar |
| **B** · aceptar que se lleve todo, y dejarlo dicho | El archivo ajeno hay que sacarlo a mano |

**Toca `base/`, así que decide el usuario.** La prueba queda en rojo esperado con las dos salidas explicadas en su propio texto.

---

## 5. Decisiones y señales

| Decisión | Dónde quedó |
|---|---|
| El puntero se prueba **puesto a mano**: es el escenario que el CA-02 nombra y que ninguna prueba cubría | CP-002 del [resultado](resultado_pruebas.md) |
| El almacén real se **mira, no se toca**: si hubiera algo, lo recoge el programa, no el agente | CP-003, pasos 1 y 3 |
| El paso 5 se deja en rojo esperado en vez de parchear: elegir entre las dos salidas toca `01·C19` | §4 de este documento |

---

## 6. Lo que no entró, y dónde sigue

| Qué | Dónde |
|---|---|
| Decidir qué hace el recogido con lo que no es un recuerdo | **Decisión del usuario.** Toca `01·C19` |
| Que lo guardado viva en el repositorio y se vea en el historial | [HU-002](../../HU-002-guardar-en-el-repositorio/HU-002-guardar-en-el-repositorio.md) |
| Separar el aprendizaje del proyecto de la preferencia del usuario | [HU-005](../../HU-005-separar-aprendizaje-de-preferencia/HU-005-separar-aprendizaje-de-preferencia.md) |

**La advertencia que deja esta fase:** el único punto que falla no se arregla programando. Es una regla del estándar y un plan de pruebas que esperan cosas distintas del mismo programa, y hasta que no se decida cuál manda, cualquier parche deja incumplida a la otra.
