# Funcionalidad implementada — Fase `D-EP-005-HU-003-el-ca-03-se-vuelve-a-medir` (módulo Automatismos — enganches)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `D-EP-005-HU-003-el-ca-03-se-vuelve-a-medir` |
| **Módulo** | Automatismos — enganches |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-29 |
| **HU / CA cubiertas** | [HU-003](../HU-003-disparo-al-escribir-un-archivo.md): CA-03 · El hallazgo grave detiene, y el resto avisa |
| **Fecha de cierre** | 2026-08-29 |
| **Versión del estándar al cerrar** | `35.10.0` — **sin cambio**: no se toca código |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |
| **Reemplaza el veredicto de** | `A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir` |

> **Por qué se declara el reemplazo:** se volvió a verificar CA-03, ejecutándolo, y hoy se cumple. Aquel rojo era cierto el 2026-08-17. **El veredicto de aquella fase no se toca** (`20·M11`): la cuenta lo deja atrás, el documento sigue diciendo lo que decía.

---

## 1. Qué se implementó — resumen

**Nada. Esta fase comprueba y declara.**

La fase [`A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir`](../A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir/resultado_pruebas.md) cerró en rojo el
2026-08-17 porque el disparo corría en el momento y callaba con lo que no le tocaba, pero **todo avisaba**: nada distinguía el hallazgo grave del que solo informa, y **era cierto**. Lo resolvió después
`B-EP-005-HU-003-el-hallazgo-grave-detiene`.

Lo que faltaba era que **alguien volviera a mirarlo**. Nadie lo hace por su
cuenta (`S-061`), y mientras tanto la historia arrastraba un «no cumple» que ya
no existía.

| Antes | Ahora |
|---|---|
| CA-03 · El hallazgo grave detiene, y el resto avisa, en rojo desde el 2026-08-17 | **Cumple**, comprobado ejecutando |

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| CA-03 · El hallazgo grave detiene, y el resto avisa | comprobación | `B-EP-005-HU-003-el-hallazgo-grave-detiene` | ✅ | CP-001, CP-002 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · ejecutar el criterio | ✅ | el enlace roto devuelve 2 y el documento sano devuelve 0 |
| T-02 · la contraprueba | ✅ | §3 del resultado |
| T-03 · el `Estado` de la historia | ✅ | — |
| T-04 · declarar el veredicto | ✅ | Este documento |

**Correspondencia:** 4 tareas, 4 con resultado.

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

Sin cambios. No se agrega ni se modifica ningún punto de entrada.

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué | Señal |
|---|---|---|
| Una fase que **declara**, sin tocar la roja | Aquel veredicto fue cierto. Reescribirlo borra el rastro | `20·M11` |
| Se comprueba **ejecutando**, no leyendo | Existir no es funcionar | `04·R4` |
| Las cifras las **mide un programa** | Nadie relee el número veinte de una serie | `S-081` |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| Nadie vuelve a mirar un veredicto en rojo | **Abierta.** Es `S-061`; esta fase es una de las que lo hizo a mano |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia.
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**, no se toca `base/` ni `plantillas/`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.** Lo que cambia es que la historia deja de arrastrar un
rojo que ya no existe.
