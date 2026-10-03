# Funcionalidad implementada · Fase `B-EP-023-HU-007-el-freno-detiene-antes-y-despues-de-actuar` (módulo `validadores/` y `adaptadores/claude-code/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-023-HU-007-el-freno-detiene-antes-y-despues-de-actuar` |
| **Módulo** | `validadores/` y `adaptadores/claude-code/` |
| **Especificación del módulo** | El CA-02 de la [HU-007](../HU-007-nada-se-escribe-fuera-del-plan-aprobado.md), en sus capas 1 y 2 |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 2 |
| **HU / CA cubiertas** | HU-007 (CA-02, capas 1 y 2) |
| **Fecha de cierre** | 2026-10-03 |
| **Versión del estándar al cerrar** | 51.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Antes de toda acción, el freno detiene lo que no está en el plan de la fase en curso ni lo autoriza una regla vigente, por cualquier canal: la herramienta de escritura, la consola, el segundo plano, las instalaciones y los procesos que quedan corriendo; lo que se publica se pregunta. Después de cada orden de consola compara lo que cambió en git. Al detener, anota el hallazgo en el resumen de la sesión.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-02, capa 1: antes de actuar | Programa y enganche | `validadores/freno.py`, `adaptadores/claude-code/hook_antes.py` | ✅ | CP-001 a CP-003, CP-005 |
| CA-02, capa 2: después de actuar | Programa y enganche | `validadores/freno.py`, `adaptadores/claude-code/hook_despues.py` | ✅ | CP-004 |
| Lo autorizado: reglas vigentes, HU, épica y pendiente | Programa y reglas | `validadores/autorizado.py`, `13·DOC15`, `13·DOC16`, `02·F23` | ✅ | CP-001 |
| La instalación | Instalador | `validadores/instalar.py` | ✅ | CP-001 |

**Faltantes / diferimientos:** la capa 4 y el contrato de cada adaptador van en la fase `C`.

### 2.2 Plan de trabajo → ejecución

Las 10 tareas de la versión 2 del plan quedaron hechas; cada una está en la tabla del plan con su archivo y su caso de prueba.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

- Pruebas: las de la fase y las de los programas que cambió.
- Defectos abiertos que se aceptaron: ninguno. Las tres pruebas de la EP-005 que describen el freno viejo quedan en el [pendiente 109](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-023-cada-tarea-sabe-que-reglas-le-aplican/pendientes/109-las-pruebas-del-freno-describen-el-freno-viejo/pendiente.md).

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Los dos enganches corren solos una vez que el instalador los pone. La fila de un análisis que se hace «de una y sin fase» nombra sus rutas exactas para que el freno las deje pasar.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La capa 2 compara con una foto tomada antes de cada orden, guardada en `.git/` | Lo que ya estaba cambiado, por ejemplo de otra sesión, no lo hizo esa orden | Por escribir |

## 6. Deuda técnica y pendientes generados

El [pendiente 109](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-023-cada-tarea-sabe-que-reglas-le-aplican/pendientes/109-las-pruebas-del-freno-describen-el-freno-viejo/pendiente.md), en la HU-023 de EP-005.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] `CHANGELOG.md` y `VERSION`.
- [x] `anatomia/mapa-del-sitio.md`: el programa nuevo.
- [x] `base/mapa-de-tareas.md`, regenerado.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Cada proyecto lo recibe al adoptar la 51.0.0 con el instalador.
