# Funcionalidad implementada — Fase `B-EP-004-HU-002-el-analizador-ve-todas-las-reglas` (módulo Comprobación automática)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-004-HU-002-el-analizador-ve-todas-las-reglas` |
| **Módulo** | Comprobación automática |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), escrito el 2026-08-17 y aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [HU-002](../HU-002-marca-de-comprobable-en-cada-regla.md) |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `36.0.2` — **PARCHE**, y este cambio es el que la sube |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |
| **Reemplaza el veredicto de** | `A-EP-004-HU-002-retrodocumentar-la-clasificacion-de-cada-regla` |

> **Por qué se declara el reemplazo:** la fase `A` cerró en «No cumple» porque el analizador no veía todas las reglas. Ahora las ve. **El veredicto de aquella fase no se toca** (`20·M11`).

---

## 1. Qué se implementó — resumen

**Que el analizador vea todas las reglas, y que sepa distinguir la regla de su eco.**

| Antes | Ahora |
|---|---|
| 252 reglas visibles; las 4 del capítulo 16 no existían para el programa | 256, y el capítulo 16 dentro del molde |
| Un título de nivel bajo con forma de regla se ignoraba siempre | Se acepta si su identificador no está definido arriba |
| Que una regla declare si se comprueba era un aviso | Es una falla |

**Y lo que apareció al verlas**, corregido acá por decisión del usuario: las cuatro escritas con `###`, ninguna con su checklist, y una sin su ejemplo.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| El analizador ve todas las reglas | comprobación | `validadores/metareglas.py` | ✅ | CP-001, CP-002 |
| Toda regla declara si se comprueba | comprobación | `validadores/metareglas.py` | ✅ | CP-004, CP-005 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · reconocer las escritas con `###` | ✅ | CP-001 |
| T-02 · no confundirlas con su eco | ✅ | CP-002 |
| T-03 · destapar la prueba del analizador | ✅ | 9 de 9 en verde |
| T-04 · listar lo que apareciera | ✅ | CP-003 |
| T-05 · el subcomando en `validar.py` | ✅ | Ya existía al llegar acá |
| T-06 · la fila 18 pasa a falla | ✅ | CP-004 |
| T-07 · destapar la prueba de la regla sin clasificar | ✅ | Ya estaba destapada |
| T-08 · caso de las derogadas | ✅ | CP-005 |

**Correspondencia:** 8 tareas, 8 con resultado.

**Archivos tocados que el plan no declaraba** (`02·F8`): `base/16-cumplimiento-y-calidad.md`, `CHANGELOG.md` y `VERSION`. **Se declaran acá, y entraron por decisión expresa del usuario** al ver lo que la fase destapó.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Suites ejecutadas** | `pruebas.ClasificacionDeCadaRegla`: 9 pruebas, 9 en verde, 0 fallos esperados |
| **Defectos abiertos** | Ninguno |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

```
python validadores/validar.py metareglas
```

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué |
|---|---|
| El identificador separa la regla de su eco | `M4` lo exige único: el que ya se definió arriba no puede ser otra definición |
| La distinción se hace en una pasada previa | En el orden del árbol, el eco se lee antes que la regla |
| La fila 18 detiene ahora y no antes | Reclamar por algo que el programa no podía mirar entero es ruido que se aprende a ignorar |
| El capítulo 16 se corrigió en esta fase | Dejarlo habría dejado cuatro fallas sin dueño en el cuerpo de reglas |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| Ninguna | — |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia y su tabla de fases.
- [x] `CHANGELOG.md` y `VERSION`, en `36.0.2`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.**
