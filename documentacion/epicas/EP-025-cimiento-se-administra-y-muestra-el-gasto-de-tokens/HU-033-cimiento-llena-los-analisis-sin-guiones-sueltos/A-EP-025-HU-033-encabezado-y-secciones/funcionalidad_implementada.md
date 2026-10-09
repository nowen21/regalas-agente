# Funcionalidad implementada · Fase `A-EP-025-HU-033-encabezado-y-secciones` (módulo análisis en curso)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-033-encabezado-y-secciones` |
| **Módulo** | Análisis en curso: `proyectos/cimiento/core/enganches/` y un comando de `core/proyectos/` |
| **Especificación del módulo** | Los CA de la [HU-033](../HU-033-cimiento-llena-los-analisis-sin-guiones-sueltos.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-033 (CA-01 y CA-02) |
| **Fecha de cierre** | 2026-10-09 |
| **Versión del estándar al cerrar** | 59.3.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Al prender un análisis nuevo, Cimiento pone las rutas al estándar, el número del análisis siguiente y la copia del pendiente; en el análisis 1, también la copia del hallazgo que enlaza el «De dónde sale». Lo que no encuentra queda con su marca. El comando `manage.py analisis seccion` guarda el texto de una sección, muestra lo que tenía antes y, si la sección no existe, dice cuáles hay.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Funcional | `core/enganches/llenar_analisis.py` (`llenar_encabezado`), `core/enganches/analisis_en_curso.py` (`nuevo_analisis`) | ✅ | CP-001, CP-002 |
| CA-02 | Funcional | `core/enganches/llenar_analisis.py` (`poner_seccion`), `core/proyectos/management/commands/analisis.py` | ✅ | CP-003, CP-004 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 3 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple: 4 de 4 casos |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

1. El encabezado se llena solo al escribir «Analicemos: el pendiente N».
2. Para guardar una sección: escribir el texto en un archivo y correr `manage.py analisis seccion «ruta del analisis-N.md» "Lo acordado" --archivo texto.md`. El título puede ir completo o solo su comienzo.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La copia del hallazgo solo en el análisis 1 | Desde el 2, el hallazgo que abre el análisis es nuevo y no está en el pendiente | No hace falta: está en el plan, §2.6 |

## 6. Deuda técnica y pendientes generados

Ninguno. Cuando la EP-030·HU-003 pase los análisis a la base, el comando cambia dónde guarda.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica.
