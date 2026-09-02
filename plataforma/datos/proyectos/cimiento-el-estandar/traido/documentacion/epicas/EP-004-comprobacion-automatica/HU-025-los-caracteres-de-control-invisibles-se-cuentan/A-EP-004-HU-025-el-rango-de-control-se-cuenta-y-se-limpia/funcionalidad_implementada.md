# Funcionalidad implementada — Fase `A-EP-004-HU-025-el-rango-de-control-se-cuenta-y-se-limpia` (módulo Programas de comprobación)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-025-el-rango-de-control-se-cuenta-y-se-limpia` |
| **Módulo** | Programas de comprobación |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [HU-025](../HU-025-los-caracteres-de-control-invisibles-se-cuentan.md): los tres |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `36.0.3` — **PARCHE**, y este cambio es el que la sube |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |

---

## 1. Qué se implementó — resumen

**Que lo que no se ve y rompe la tabla se cuente y se quite.**

| Antes | Ahora |
|---|---|
| Siete caracteres invisibles conocidos, ninguno de control | El rango completo, menos los tres que significan algo al escribir |
| Un carácter al principio de una fila la hacía desaparecer del cuadro | Se cuenta, se nombra y se borra |
| El anexo de la norma no lo mencionaba | Tiene su fila |

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| CA | Ubicación | Estado | Evidencia |
|---|---|---|---|
| CA-01 · se reporta con su nombre | `validadores/marcas.py` | ✅ | CP-001 |
| CA-02 · el árbol queda en cero | `validadores/marcas.py` y los 14 archivos limpios | ✅ | CP-004, CP-005 |
| CA-03 · lo legítimo no se toca | El rango excluye salto, retorno y tabulador | ✅ | CP-003 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Evidencia |
|---|---|
| T-01 · contar el rango | CP-002 |
| T-02 · que la limpieza los quite | CP-004 |
| T-03 · la fila en el anexo | El anexo |
| T-04 · limpiar lo que ya lo traía | CP-005 |

**Correspondencia:** 4 tareas, 4 con resultado.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Suites ejecutadas** | 5 pruebas nuevas, 5 en verde |
| **Defectos abiertos** | Ninguno |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

```
python validadores/marcas.py            ← el recuento del árbol
python validadores/validar.py marcas    ← lo que se hereda
```

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué |
|---|---|
| Se barre el rango completo | Agregar de a uno deja el trabajo a medias: el próximo se cuela igual, y no se ve |
| Se borran, no se reemplazan | No hay reemplazo que elegir: no significan nada dentro de un texto |
| El histórico y los datos de la plataforma no se tocan | Una transcripción no se reescribe, y esa carpeta es una copia que se vuelve a traer |
| La fila va también en el anexo | Si la lista escrita dice menos que el programa, la norma miente |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| De dónde salieron esos caracteres | **Abierta y declarada.** Saberlo no era condición para limpiarlos |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia y su tabla de fases.
- [x] `CHANGELOG.md` y `VERSION`, en `36.0.3`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.**
