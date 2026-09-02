# Funcionalidad implementada — Fase `B-EP-006-HU-006-se-lleva-todo-y-el-almacen-queda-vacio` (módulo Memoria)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-006-HU-006-se-lleva-todo-y-el-almacen-queda-vacio` |
| **Módulo** | Memoria |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [HU-006](../HU-006-sacar-del-almacen-local.md): el CA-01, el almacén local queda vacío |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `36.0.0` — **sin cambio**: no se toca `base/` ni `plantillas/` |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |
| **Reemplaza el veredicto de** | `A-EP-006-HU-006-retrodocumentar-el-vaciado-del-almacen-local` |

> **Por qué se declara el reemplazo:** la decisión que faltaba está tomada y comprobada. Aquel rojo era cierto el 2026-08-22. **El veredicto de aquella fase no se toca** (`20·M11`).

---

## 1. Qué se implementó — resumen

La fase [`A-EP-006-HU-006-retrodocumentar-el-vaciado-del-almacen-local`](../A-EP-006-HU-006-retrodocumentar-el-vaciado-del-almacen-local/resultado_pruebas.md) cerró en rojo porque el almacén estaba vacío y el programa lo vaciaba, pero fallaba el paso 5: `sueltos()` devuelve **todo** archivo, así que un `config.json` de la herramienta terminaría en `historico-chat/memory/` como si fuera un recuerdo.

**Se lleva todo.** Lo decidió el usuario el 2026-08-30.

**Por qué manda `01·C19` tal como está escrita.** Exige que el almacén local quede **vacío**, y eso es lo que se sostiene: lo que queda ahí es lo que se pierde. La carpeta de la herramienta no la mira nadie, no se versiona y desaparece con la máquina.

**El costo de la otra salida era peor.** Si el programa dejara ahí lo que no es recuerdo, `revisar()` reprobaría para siempre por un archivo que nadie va a mover, y un reclamo que no se puede cerrar se aprende a ignorar.

**Y el archivo de más no se pierde de vista:** un `config.json` en `historico-chat/memory/` se ve, se lee y se borra cuando estorbe. Uno olvidado en una carpeta de la herramienta, no.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| CA-01, el almacén local queda vacío | decisión aplicada | Este cierre | ✅ | CP-001 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · ejecutar el criterio y su contraprueba | ✅ | §3 del resultado |
| T-02 · aplicar la decisión | ✅ | §3 del resultado |
| T-03 · declarar el veredicto | ✅ | Este documento |

**Correspondencia:** 3 tareas, 3 con resultado.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Defectos abiertos** | Ninguno |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Sin cambios.

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué |
|---|---|
| Se lleva todo | Lo que queda en el almacén es lo que se pierde: esa carpeta no la mira nadie y no se versiona |
| `01·C19` no se toca | Aflojarla dejaría vivo el caso que la regla existe para evitar |
| La prueba comprueba las dos mitades | Un programa que borrara el almacén sin traer nada también lo dejaría vacío |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| Al repositorio puede entrar un archivo que no es recuerdo | **Abierta y declarada.** Se ve y se borra cuando estorbe, que es la diferencia con dejarlo afuera |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia y su tabla de fases.
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.**
