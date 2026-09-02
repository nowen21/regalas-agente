# Funcionalidad implementada — Fase `B-EP-001-HU-003-la-clave-dentro-de-una-frase-no-se-tapa` (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-001-HU-003-la-clave-dentro-de-una-frase-no-se-tapa` |
| **Módulo** | Cuerpo de reglas |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [HU-003](../HU-003-nucleo-que-no-se-sobrescribe.md): el CA-02, la clave no queda en claro |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `36.0.0` — **sin cambio**: no se toca `base/` ni `plantillas/` |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |
| **Reemplaza el veredicto de** | `A-EP-001-HU-003-retrodocumentar-el-nucleo-blindado` |

> **Por qué se declara el reemplazo:** la decisión que faltaba está tomada y comprobada. Aquel rojo era cierto el 2026-08-22. **El veredicto de aquella fase no se toca** (`20·M11`).

---

## 1. Qué se implementó — resumen

La fase [`A-EP-001-HU-003-retrodocumentar-el-nucleo-blindado`](../A-EP-001-HU-003-retrodocumentar-el-nucleo-blindado/resultado_pruebas.md) cerró en rojo porque de seis formas de escribir una clave, **tres se enmascaran y tres no**. Las tres que no son las que dicen la clave dentro de una frase normal: «mi clave es Patito2026».

**No se tapa la clave dicha dentro de una frase, y queda declarado.** Lo decidió el usuario el 2026-08-30.

**Por qué no se intenta.** Para tapar «mi clave es Patito2026» habría que suponer que la palabra que sigue a «clave» es la clave. Con esa misma suposición se tapa «la clave del asunto es que el proceso sirva», que es una frase corriente.

**Y el daño de tapar de más no es un falso positivo:** es que un enmascarado que estorba se apaga. Apagado no tapa ninguna de las seis, así que intentar tapar tres más pone en riesgo las tres que hoy sí se tapan.

**Lo que sí queda cubierto**, medido ejecutándolo: las tres formas en que la clave va pegada a su nombre, que son las que salen de un archivo de configuración, de un registro o de un comando pegado. Son las que aparecen sin que nadie las escriba a propósito.

**Lo que queda descubierto, dicho sin adorno:** si alguien escribe su clave dentro de una frase, queda escrita. La defensa ahí no es el programa: es `00·N6`, que prohíbe escribirla.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| CA-02, la clave no queda en claro | decisión aplicada | Este cierre | ✅ | CP-001 |

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
| No se tapa la clave dicha dentro de una frase | Habría que suponer que la palabra siguiente a «clave» es la clave, y con eso se tapa «la clave del asunto es que sirva» |
| El límite se escribe, no se calla | Un criterio que se da por cumplido escondiendo lo que no cubre es la mentira optimista que esta cuenta existe para impedir |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| La clave dicha dentro de una frase queda en claro | **Abierta y declarada**, con su motivo. La defensa ahí es `00·N6`, no el programa |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia y su tabla de fases.
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.**
