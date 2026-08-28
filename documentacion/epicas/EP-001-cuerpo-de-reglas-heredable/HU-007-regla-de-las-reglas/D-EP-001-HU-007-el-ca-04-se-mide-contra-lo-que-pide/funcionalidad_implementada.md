# Funcionalidad implementada — Fase `D-EP-001-HU-007-el-ca-04-se-mide-contra-lo-que-pide` (módulo Meta-reglas)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `D-EP-001-HU-007-el-ca-04-se-mide-contra-lo-que-pide` |
| **Módulo** | Meta-reglas |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-27 |
| **HU / CA cubiertas** | [HU-007](../HU-007-regla-de-las-reglas.md): el `CA-04` |
| **Fecha de cierre** | 2026-08-27 |
| **Versión del estándar al cerrar** | `35.6.0` — **sin cambio**: no se toca código |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Reemplaza el veredicto de** | `A-EP-001-HU-007-retrodocumentar-el-procedimiento-de-la-regla` |
| **Commit** | Pendiente de aprobación del usuario |

> **Por qué se declara el reemplazo:** se volvió a medir el `CA-04` contra lo que su criterio pide, y cumple en sus tres exigencias. Aquel rojo se puso citando *«249 de 249 sin dato»* — **una cifra que el criterio no menciona**. **El veredicto de aquella fase no se toca** (`20·M11`): la cuenta lo deja atrás, el documento sigue diciendo lo que decía.

---

## 1. Qué se implementó — resumen

**Nada. Esta fase vuelve a medir un criterio contra lo que el criterio pide.**

El `CA-04` pide **tres cosas**: la lista ordenada de la más vieja a la más nueva, cuándo se revisó cada una, y cuántos incumplimientos produce hoy. **Las tres se cumplen**, comprobadas corriendo `vigencia.py`.

| Antes | Ahora |
|---|---|
| «No cumple», citando `249 de 249 sin dato` | **Cumple**: la lista existe, está ordenada, y dice las dos cosas |

**Y `251 de 251 sin fecha` no es una falta: es el diseño.** El procedimiento lo dice en una línea — *«arranca ausente en todas las reglas, a propósito; ponérsela de una vez a las doscientas habría sido escribir doscientas fechas que no responden por ninguna revisión»*.

**Tratarlo como deuda habría llevado a sellar 250 reglas sin revisarlas** — exactamente el sello vacío que ese documento existe para impedir.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem de la historia | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| `CA-04` se obtiene la lista ordenada | servicio | `validadores/vigencia.py` | ✅ | CP-001, CP-003 |
| `CA-04` cada una dice cuándo se revisó | servicio | Columna `REVISADA` | ✅ | CP-002 |
| `CA-04` y cuántos incumplimientos produce hoy | servicio | Columna `FALLA HOY` | ✅ | CP-002 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · correr y comprobar que da una lista | ✅ | CP-001 |
| T-02 · que diga cuándo y cuántos | ✅ | CP-002 |
| T-03 · que esté **ordenada** | ✅ | CP-003 |
| T-04 · que avise y no corrija | ✅ | CP-004 |
| T-05 · declarar el veredicto y el reemplazo | ✅ | Este documento |

**Correspondencia:** 5 tareas, 5 con resultado.

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

```
python validadores/vigencia.py
```

Sin cambios. Las ordena de la que lleva más tiempo sin mirarse a la que menos, y al lado dice cuántos incumplimientos produce cada una.

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué | Señal |
|---|---|---|
| **Se corre, no se cita** | Apoyarse en la medición de la `A` heredaría su error de raíz | `S-064` |
| Se comprueba que esté **ordenada**, no solo que exista | Es lo que el criterio exige y lo que nadie mira | `CP-003` |
| Se comprueba el procedimiento **aunque no sea del `CA-04`** | Es lo que separa «el criterio se cumple» de «además, tratarlo como deuda habría sido un error» | `CP-005` |
| **El hallazgo de la `A` se conserva** | Que nadie hubiera revisado ninguna regla era cierto. Lo mal puesto era la factura | `S-069` |
| El veredicto de la `A` **no se toca** | El error enseña más que la conclusión | `20·M11` |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| **Revisar reglas de fondo** | **Abierta, y ya no es deuda: es trabajo normal.** Cuándo empezar lo decide el usuario |
| **La columna «falla hoy» está vacía en todas** | **Abierta, y vale mirarla.** El procedimiento dice que ese número se lee en las dos direcciones: una regla vieja que nunca ha fallado puede ser una que **ya nadie aplica** |
| El agente recomendó este trabajo **tres veces** sin leer el criterio | **Cerrada** como `S-069` |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El [README](../README.md) de la carpeta de la historia.
- [x] La señal `S-069`.
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**, no se toca `base/` ni `plantillas/`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.** Lo que cambia es que la historia deja de arrastrar un rojo que su criterio no sostiene.
