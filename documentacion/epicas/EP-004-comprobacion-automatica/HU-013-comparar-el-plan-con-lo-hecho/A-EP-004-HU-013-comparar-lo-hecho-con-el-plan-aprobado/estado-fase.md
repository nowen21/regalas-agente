# Estado de fase — Fase A-EP-004-HU-013-comparar-lo-hecho-con-el-plan-aprobado (módulo Comprobación automática)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-013-comparar-lo-hecho-con-el-plan-aprobado` |
| **Módulo** | Comprobación automática — [`flujo.py`](../../../../../validadores/flujo.py), [`fases.py`](../../../../../validadores/fases.py) y [`trazabilidad.py`](../../../../../validadores/trazabilidad.py) |
| **Épica / HU / origen** | [EP-004](../../epica.md) · [HU-013](../HU-013-comparar-el-plan-con-lo-hecho.md) · 🔀 híbrido: parte compara hoy, la comparación de archivos no existe. Fila de HU-013 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 4 — pausa y presentación. **Última puerta pasada:** 3, con el plan de trabajo y el plan de pruebas escritos.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 pendiente: falta presentarlo y resolver las dudas 1 y 2 | ☐ |
| 5 | Aprobación del plan detallado | 👤 pendiente | ☐ |
| 6 | Ejecución continua | 7 tareas, ninguna empezada | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** Ninguna fase cerrada se reabre: lo que la comparación destape sobre trabajo viejo se anota.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 3 |
| **CA en "No"** | Ninguno todavía. El **CA-01 está en «No» de entrada** —nadie compara los archivos tocados con los declarados— y el **CA-02 a medias** |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Bloqueada | Comparar el §2.1 con los archivos que la rama tocó. Duda 1 |
| T-02 | Bloqueada | Caso del archivo no declarado — CP-001 |
| T-03 | Pendiente | Comparar los casos del plan de pruebas con los criterios |
| T-04 | Pendiente | Caso del criterio sin caso y el caso sin criterio — CP-003 |
| T-05 | Pendiente | Revisión a mano de tres fases cerradas — CP-004. **No depende de las dudas** |
| T-06 | Bloqueada | Declarar si el CA-03 es comprobable. Duda 2 |
| T-07 | Pendiente | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 7. **Bloqueadas:** T-01, T-02 y T-06.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Los archivos tocados se leen del control de versiones: una lista a mano es justo lo que el programa viene a reemplazar | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Ante un §2.1 con formato que no entiende, el programa **avisa y no falla**: los planes existentes llenan esa tabla de varias formas, y fallar dejaría el repositorio en rojo por un formato viejo | §2.6 del plan |
| Si el CA-03 no es comprobable, se declara así en el registro. Decir qué **no** se comprueba es un resultado, no un pendiente indefinido | §2.6 del plan |
| Decidir si algo es automatizable **después** de haberlo hecho a mano vale más que decidirlo antes | CP-004 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **Duda 1 de §2.7:** contra qué se comparan los archivos tocados — la rama de la fase, el commit único, o lo que esté sin guardar. Bloquea el CA-01.
- **Duda 2 de §2.7:** si el CA-03 se intenta comprobar o se declara criterio humano. Bloquea T-06; el caso a mano de T-05 se puede hacer igual.
- **La aprobación del plan.** Sin ella no arranca la ejecución.
- **Si la mayoría de los §2.1 no se pueden leer** (riesgo `R-01`): el aviso del CA-01 no vale hasta que la proporción suba. Por eso se mide primero.
- **Si la comparación destapa incumplimientos de `F8` en fases cerradas** (riesgo `R-02`): se anotan. Reabrir lo cerrado está fuera de alcance.

---

## 4. Si se bloqueó

- **Estación:** 4 — pausa y presentación. **Motivo:** el plan está escrito y sin aprobar, y las dos dudas bloquean el CA-01 y la declaración del CA-03. **Qué falta para desbloquear:** que el usuario apruebe el plan, diga contra qué se comparan los archivos tocados y si el CA-03 se intenta comprobar. El CA-02 y la lectura de T-05 pueden arrancar apenas se apruebe.
