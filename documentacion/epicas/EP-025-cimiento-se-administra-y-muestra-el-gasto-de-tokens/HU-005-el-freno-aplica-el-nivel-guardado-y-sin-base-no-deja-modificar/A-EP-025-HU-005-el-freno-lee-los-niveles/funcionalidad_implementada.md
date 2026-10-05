# Funcionalidad implementada · Fase `A-EP-025-HU-005-el-freno-lee-los-niveles` (módulo `proyectos/cimiento/core/enganches/` y `adaptadores/claude-code/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-005-el-freno-lee-los-niveles` |
| **Módulo** | `proyectos/cimiento/core/enganches/`, `adaptadores/claude-code/`, `proyectos/cimiento/core/herramientas/` |
| **Especificación del módulo** | Los CA de la [HU-005](../HU-005-el-freno-aplica-el-nivel-guardado-y-sin-base-no-deja-modificar.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-005 (CA-01 a CA-04) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 54.2.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Cuando el freno detiene una acción por una regla, mira el nivel que esa regla tiene en el proyecto, en la base de Cimiento: «frena» detiene, «avisa» deja hacer y le avisa al agente y al usuario, «apagada» deja hacer. El núcleo siempre frena. Lo lee con PyMySQL, sin Django. Sin base, el freno no deja modificar nada y dice que hay que prender MariaDB; leer sigue pasando. La instalación del estándar deja PyMySQL donde corren los enganches.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/core/enganches/niveles.py`, `proyectos/cimiento/core/enganches/freno.py`, `proyectos/cimiento/config/ambiente.py`, `adaptadores/claude-code/hook_antes.py`, `adaptadores/claude-code/hook_despues.py` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/enganches/freno.py` | ✅ | CP-002 |
| CA-03 | Programa | `proyectos/cimiento/core/enganches/freno.py`, `proyectos/cimiento/core/enganches/niveles.py` | ✅ | CP-003 |
| CA-04 | Programa | `proyectos/cimiento/core/herramientas/instalar.py`, `validadores/instalar.py`, `proyectos/cimiento/requirements/base.txt` | ✅ | CP-004 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 8 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno. `requirements/base.txt` y `lock.txt` se agregaron al plan antes de tocarlos.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Se registra el proyecto en Cimiento y se baja una regla en «Reglas»: desde la acción siguiente, el freno de ese proyecto la aplica. El nivel de la regla es el del motivo que el freno da, por ejemplo `02·F8` en «el plan de la fase en curso no lo declara».

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| «Avisa» se entrega como contexto adicional y mensaje, sin `permissionDecision` | Un «allow» saltaría la confirmación de la herramienta | S-301 |
| La regla sale del motivo | Todos los motivos ya la nombran entre paréntesis | No hace falta: está en el freno |
| Sin base, «sin_base» no se anota como hallazgo | No es algo fuera del plan: es la base apagada | No hace falta |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

No aplica.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Rige en toda la máquina desde que se guarda: los enganches de todos los proyectos usan la clase `Freno` de Cimiento.
