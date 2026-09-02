# Funcionalidad implementada — Fase `A-EP-004-HU-010-declaracion-y-comprobacion` (módulo Comprobación automática)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-010-declaracion-y-comprobacion` |
| **Módulo** | Comprobación automática |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), escrito el 2026-08-17 y aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [HU-010](../HU-010-convencion-declarada-por-el-proyecto.md): los cinco |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `36.0.2` — **sin cambio**: no se toca `base/` ni `plantillas/` |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |

---

## 1. Qué se implementó — resumen

**Lo que el proyecto declara es lo que se le comprueba, y lo que no declara se dice.**

Los programas ya estaban escritos cuando llegó la aprobación. Lo que faltaba era **ejecutar los cinco criterios**, y ahí apareció lo que importa.

| Antes | Ahora |
|---|---|
| Los cinco criterios, sin ejecutar | Los cinco ejecutados, tres provocados con su contraprueba |
| El reclamo de que un inmutable no tiene permiso salía **siempre** | Sale solo cuando el permiso de verdad falta |

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| CA | Cómo se verificó | Estado |
|---|---|---|
| CA-01 | Contra tres proyectos reales, en tres estados distintos | ✅ |
| CA-02 | Provocado, con contraprueba | ✅ |
| CA-03 | Provocado, con contraprueba | ✅ |
| CA-04 | Provocado, con contraprueba, y encontró el defecto | ✅ |
| CA-05 | Contra un proyecto real y provocado | ✅ |

### 2.2 Plan de trabajo → ejecución

Las tareas del plan que construían los programas ya estaban hechas al llegar la
aprobación. Lo que esta fase ejecutó es la verificación de los cinco criterios,
y la corrección del defecto que encontró.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno. `entidades.py`
estaba declarado en el §2.1 del plan.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Suites ejecutadas** | `test_las_entidades_no_acusan_a_ciegas.py`: 7 pruebas, 7 en verde |
| **Defectos abiertos** | Ninguno |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

```
python validadores/validar.py estructura --raiz <proyecto>
python validadores/validar.py entidades  --raiz <proyecto>
python validadores/validar.py esquema    --raiz <proyecto>
```

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué |
|---|---|
| Tres criterios se provocan en un proyecto temporal | Ningún proyecto real sirve para verlos, y provocarlos en uno real está prohibido |
| Cada provocación lleva su contraprueba | Un validador que reclamara siempre pasaría igual |
| El marcador se reemplaza sobre lo escapado, buscando lo mismo que se escapó | No suponer cómo quedó escapado: eso fue lo que se rompió al cambiar de versión de Python |
| El proyecto de prueba es un repositorio con sus archivos guardados | Las comprobaciones solo miran lo versionado, y sin eso no encuentran nada |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| Ningún proyecto real tiene migraciones legibles **y** entidades declaradas a la vez | **Abierta y declarada.** Por eso tres criterios se provocan; el día que haya uno, se verifican también ahí |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia y su tabla de fases.
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.** El proyecto que corra las comprobaciones deja de recibir
el reclamo falso del permiso.
