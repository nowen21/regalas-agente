# Funcionalidad implementada — Fase `A-EP-003-HU-007-retrodocumentar-el-procedimiento-que-dirige` (módulo Documentos modelo)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-003-HU-007-retrodocumentar-el-procedimiento-que-dirige` |
| **Módulo** | Documentos modelo y procedimientos |
| **Especificación del módulo** | La propia [HU-007](../HU-007-procedimiento-que-dirige.md). El entregable es un procedimiento escrito |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | [HU-007](../HU-007-procedimiento-que-dirige.md): `CA-01`, `CA-02` y `CA-03`. Los tres |
| **Fecha de cierre** | 2026-08-26 |
| **Versión del estándar al cerrar** | `35.1.0` |
| **Commit** | `b19ca91` |

> **Se ejecutó el 2026-08-22 y se cierra el 2026-08-26.** Entre las dos fechas no se tocó nada de esta fase: faltaba este documento.

---

## 1. Qué se implementó — resumen

**El procedimiento que dirige el trabajo ya existía, y esta fase comprobó que dirige de verdad.** Llama a los demás procedimientos en orden, se detiene donde tiene que aprobar una persona, y se puede retomar días después sin perder el hilo.

**La evidencia no es una lectura del procedimiento: es el trabajo real de la jornada.** Cuatro fases construidas ese día en ese orden, once detenidas esperando aprobación, y tres sesiones distintas en cinco días trabajando sobre los mismos once planes.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem de la historia | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| `CA-01` llama a los procedimientos en orden | procedimiento | La tabla de trece estaciones | ✅ | **Cuatro fases construidas ese día** en ese orden |
| `CA-02` se detiene donde aprueba una persona | procedimiento | Las estaciones con marca de persona | ✅ | **Once fases paradas en la estación 12**, y una decisión devuelta |
| `CA-03` se retoma sin perder el hilo | procedimiento | El `estado-fase.md` de cada fase | ✅ | **Tres sesiones en cinco días** sobre los mismos once planes |

**El `CA-03` es el que más vale de los tres**, porque es el que no se puede fingir: o el trabajo se retomó de verdad después de días, o no.

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado |
|---|---|
| Las del plan | ✅ hechas |

**Lo que no se hizo:** cerrar la trazabilidad, que es este documento. **La fase quedó cuatro días en la estación 11.**

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Qué | Resultado |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, los tres criterios |
| **Defectos abiertos que se aceptaron** | `D-01` (alta) y `D-02` (baja). Ver §6 |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

El procedimiento se sigue al abrir una fase. Su estado en vivo vive en el `estado-fase.md` de cada fase, con la tabla de trece estaciones y cuál está pasada.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué |
|---|---|
| La evidencia son **fases reales**, no un recorrido de prueba | Un procedimiento que dirige se comprueba dirigiendo. Recorrerlo a mano probaría que se puede leer, no que se usa |
| El `CA-03` se comprueba con **días de por medio**, no dentro de la misma sesión | Retomar sin perder el hilo solo se puede afirmar si hubo algo que perder |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Severidad | Estado al cerrar |
|---|---|---|
| **`D-01` · El procedimiento no manda verificar la línea base del plan al retomarlo.** Un plan aprobado se lee como vigente aunque el árbol haya cambiado debajo | Alta | **Abierta** |
| **`D-02` · La estación 12 no tiene forma de saber cuánto lleva esperando.** Once fases detenidas ahí se ven igual que una | Baja | **Abierta** |

**`D-01` es la que más pesa, y esta jornada lo demostró.** Varias veces hubo que medir la línea base antes de construir, porque el plan afirmaba cosas que el árbol ya no decía. El procedimiento no lo manda: se hizo por criterio.

**Y `D-02` se ve hoy con más claridad que cuando se escribió**: el pendiente [87](../../../../../pendientes/87-la-estacion-del-commit-casi-nunca-se-marca.md) mostró que 23 fases estaban cerradas de hecho y nadie lo había marcado. Una estación que no sabe cuánto lleva esperando es una estación donde el trabajo se pierde de vista.

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La historia [HU-007](../HU-007-procedimiento-que-dirige.md): su §8 nombra esta fase.
- [x] El inventario de historias, que **ya no se mantiene a mano** desde la `35.0.0`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna. El entregable es un procedimiento escrito.
- **Qué cambia para quien ya tenía el estándar:** nada. El procedimiento ya estaba publicado.
- **Reversión:** no aplica. La fase no cambió el procedimiento: lo comprobó.
