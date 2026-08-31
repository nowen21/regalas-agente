# Funcionalidad implementada — Fase `B-EP-006-HU-005-manda-el-recuerdo-y-la-senal-se-reemplaza` (módulo Memoria)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-006-HU-005-manda-el-recuerdo-y-la-senal-se-reemplaza` |
| **Módulo** | Memoria |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [HU-005](../HU-005-separar-aprendizaje-de-preferencia.md): el CA-01, nada está guardado en los dos sitios diciendo cosas distintas |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `36.0.0` — **sin cambio**: no se toca `base/` ni `plantillas/` |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |
| **Reemplaza el veredicto de** | `A-EP-006-HU-005-retrodocumentar-la-separacion-aprendizaje-preferencia` |

> **Por qué se declara el reemplazo:** la decisión que faltaba está tomada y aplicada. Aquel rojo era cierto el 2026-08-17. **El veredicto de aquella fase no se toca** (`20·M11`).

---

## 1. Qué se implementó — resumen

La fase [`A-EP-006-HU-005-retrodocumentar-la-separacion-aprendizaje-preferencia`](../A-EP-006-HU-005-retrodocumentar-la-separacion-aprendizaje-preferencia/resultado_pruebas.md) cerró en rojo porque **una cosa estaba guardada en los dos sitios y las dos versiones ya decían cosas distintas**: el recuerdo de terminología decía «Cimiento» desde el 2026-08-14, y la señal `S-002` seguía diciendo «el agente = Claude Code».

**Manda el recuerdo.** El usuario lo decidió el 2026-08-30 con la frase que zanja el caso: *«el agente (Cimiento) no es Claude Code»*.

**Por qué manda el recuerdo y no la señal.** El recuerdo es lo que el agente carga al abrir cada sesión: es lo que rige mientras trabaja. La señal es historia de por qué se decidió algo. Cuando las dos se contradicen, la que manda es la que se está leyendo.

**Y la señal no se borra.** El propio [`documentacion/senales.md`](../../../../../documentacion/senales.md) lo tiene escrito en su cabecera desde el principio: *«una señal revertida no se borra: se marca `reemplazada` y se enlaza la nueva»*. Nadie lo había aplicado a esta.

**Lo que hizo daño mientras tanto.** No es hipotético: el 2026-08-13 esa misma frase llevó a responder que el agente maneja machine learning. Quien lo maneja es Claude, que no es el agente. El recuerdo lo cuenta con fecha.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| CA-01, nada está guardado en los dos sitios diciendo cosas distintas | decisión aplicada | Este cierre | ✅ | CP-001 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · medir los dos sitios | ✅ | §3 del resultado |
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
| **Suites ejecutadas** | Ninguna nueva: esta fase no cambia código |
| **Defectos abiertos** | Ninguno |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Sin cambios.

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué |
|---|---|
| Manda el recuerdo | El recuerdo es lo que el agente carga al abrir sesión: es lo que rige mientras trabaja |
| La señal vieja se marca `reemplazada`, no se borra | Reescribirla borraría el rastro de que se creyó lo contrario, y de que eso causó un error |
| La nueva se escribe en la misma base | Una señal reemplazada por nada deja al lector sin dónde ir |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| `memoria.py supersede` recibe `--by` y no lo guarda: solo lo imprime | **Abierta.** Acá se rodeó escribiendo la nueva con `--reemplaza`, que sí queda |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia y su tabla de fases.
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**, no se toca `base/` ni `plantillas/`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.**
