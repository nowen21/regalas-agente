# Estado de fase — Fase A-EP-004-HU-006-retrodocumentar-la-comprobacion-de-la-estructura (módulo Comprobación automática)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-006-retrodocumentar-la-comprobacion-de-la-estructura` |
| **Módulo** | Comprobación automática — [`validadores/fases.py`](../../../../../validadores/fases.py) |
| **Épica / HU / origen** | [EP-004](../../epica.md) · [HU-006](../HU-006-nomenclatura-y-estructura.md) · retro-documentación, fila de HU-006 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 9 — commit único. **Última puerta pasada:** 8, con la trazabilidad cerrada.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 presentado el 2026-08-17 | ☑ |
| 5 | Aprobación del plan detallado | 👤 «autorizados los planes de trabajo», 2026-08-17 | ☑ |
| 6 | Ejecución continua | 5 tareas, las 5 hechas | ☑ |
| 7 | Pruebas | [`resultado_pruebas.md`](resultado_pruebas.md) con veredicto **Cumple** | ☑ |
| 8 | Cierre documental | [`funcionalidad_implementada.md`](funcionalidad_implementada.md), §8 de la HU y fila del inventario 48 | ☑ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** §2.7 no dejó dudas abiertas.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3, y los dos transversales |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | 1 — `D-02`, que el plan declaró cobertura completa sin contar los transversales. `D-01` se corrigió acá | 
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) de esta fase |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | **Hecha** | Caso del nombre mal armado y el complemento válido — CP-001 |
| T-02 | **Hecha** | Caso del hueco en el consecutivo — CP-002 |
| T-03 | **Hecha** | Caso de la fase incompleta — CP-003 |
| T-04 | **Hecha** | Anotar la cuenta de avisos como línea base fechada — CP-004 |
| T-05 | **Hecha** | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 5 de 5. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Las partes de `F12` que piden criterio se declaran no comprobables en vez de simularse: una comprobación que se equivoca vale menos que ninguna, y `F12.10` —que la fase represente trabajo real— no lo decide un programa | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Los casos negativos se arman en carpeta temporal: romper una fase del árbol real dejaría el repositorio en rojo para las demás sesiones | §2.6 del plan |
| La cuenta de avisos se toma **al final** y con su fecha: los avisos cambian mientras se trabaja porque se abren fases, y una cuenta tomada al empezar nace vieja | §2.6 del plan y riesgo `R-01` |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar.
- **Los avisos que `F12.13` reporta hoy** incluyen las HU sin fase y las fases abiertas en esta sesión, a las que les faltan documentos. Esta fase los **cuenta** como línea base; no los arregla.
- **Si las pruebas nuevas repiten las que ya están en la suite** (riesgo `R-02`): se lee primero qué cubre la suite.
- **Si otra sesión está tocando `validadores/pruebas.py`** (riesgo `R-03`): se guarda solo lo propio.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 9 esperando la autorización del commit, que es la puerta normal.
