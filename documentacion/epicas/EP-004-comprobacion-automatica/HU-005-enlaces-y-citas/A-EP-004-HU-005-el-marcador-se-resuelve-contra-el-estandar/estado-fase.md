# Estado de fase — Fase «A-EP-004-HU-005-el-marcador-se-resuelve-contra-el-estandar» (módulo «Comprobación»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-005-el-marcador-se-resuelve-contra-el-estandar` |
| **Módulo** | Comprobación (`validadores/enlaces.py`) |
| **Planteamiento / Épica / HU** | [EP-004](../../epica.md) · [HU-005](../HU-005-enlaces-y-citas.md) · [pendiente 41](../../../../../pendientes/41-el-marcador-no-se-resuelve-dentro-de-un-proyecto.md) |
| **Última actualización** | 2026-08-16 |

---

## 1. En qué estación va

**Estación actual:** 9 — commit único. **Última puerta pasada:** 8.

Se usan las **once etapas de [`02·F15`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F15-no-saltes-ni-reordenes-las-once-etapas-de-la-fase.md)**.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 el usuario pidió las tres piezas | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | presentados al usuario | ☑ |
| 5 | Aprobación del plan detallado | 👤 aprobados el 2026-08-16 | ☑ |
| 6 | Ejecución continua | plan implementado | ☑ |
| 7 | Pruebas | `resultado_pruebas` con veredicto por CA | ☑ Cumple, ciclo 1 |
| 8 | Cierre documental | trazabilidad sin faltantes | ☑ |
| 9 | Commit único | 👤 **acá está detenida** | ☐ |
| 10 | Reporte al usuario | hash, resumen y estado | ☐ |
| 11 | Publicación / despliegue | 👤 autorizado | ☐ |

**Fue después de la fase hermana**, como pedía el orden: [`A-EP-007-HU-001-rellenar-los-marcadores-al-copiar`](../../../EP-007-instalacion-y-actualizacion/HU-001-instalar-con-una-linea/A-EP-007-HU-001-rellenar-los-marcadores-al-copiar/) quitó la causa y esta puso la red. Al revés se habría tapado el síntoma.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3 (CA-01, la no regresión y el RNF de compatibilidad) |
| **CA en "No"** | ninguno |
| **Defectos abiertos aceptados** | ninguno |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | Línea base guardada: `0 falla(s), 5 aviso(s)` |
| T-02 | Hecha | El marcador se resuelve contra `ESTANDAR` |
| T-03 | Hecha | CP-003, las dos raíces |
| T-04 | Hecha | CP-002, el marcador que no resuelve |
| T-05 | Hecha | Salidas **idénticas** antes y después |
| T-06 | Hecha | `validadores/docs/enlaces.md` |
| T-07 | Hecha | `CHANGELOG` 21.1.1 y `VERSION` |

**Hechas:** 7 de 7. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas

| Decisión / aprendizaje | Señal registrada |
|---|---|
| La rama del marcador se conserva aunque el pendiente 40 haga que dejen de llegar marcadores: es la red para el que se escape | Queda en el plan §2.6 |
| `enlaces.py` no tiene bloque `__main__`, así que correrlo directo no imprime nada y sale con código 0 | Fuera de alcance; anotado en el [pendiente 41](../../../../../pendientes/41-el-marcador-no-se-resuelve-dentro-de-un-proyecto.md) |

---

## 3. Pendiente / preguntas abiertas

- **El commit.** Lo autoriza el usuario aparte, y es lo único que detiene la fase.
- El CP-004 **no** reprodujo el [punto 1 del pendiente 33](../../../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md): la carpeta con espacio y tilde dio el mismo resultado. Ese punto sigue abierto, pero no apareció acá.

---

## 4. Si se bloqueó

No se bloqueó en ningún momento.
