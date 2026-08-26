# Estado de fase — Fase B-EP-006-HU-007-marcar-deja-fecha-y-referencia (módulo Memoria)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `B-EP-006-HU-007-marcar-deja-fecha-y-referencia` |
| **Módulo** | Memoria — [`memoria/memoria.py`](../../../../../memoria/memoria.py) |
| **Épica / HU / origen** | [EP-006](../../epica.md) · [HU-007](../HU-007-marcar-lo-que-dejo-de-aplicar.md) · **defecto** de la fase [`A`](../A-EP-006-HU-007-retrodocumentar-la-marca-de-lo-que-dejo-de-aplicar/resultado_pruebas.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 4 — pausa y presentación. **Última puerta pasada:** 3, con el plan de trabajo y el plan de pruebas escritos.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 🐞 el veredicto «No cumple» de la fase A | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 pendiente: falta presentarlo | ☐ |
| 5 | Aprobación del plan detallado | 👤 pendiente | ☐ |
| 6 | Ejecución continua | 7 tareas, ninguna empezada | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** **Sin migración:** las tres columnas que hacen falta ya existen desde el pendiente 03.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 2. El CA-02 ya estaba en «Sí» tras la fase A y hay que mantenerlo |
| **CA en "No"** | El **CA-01** y el **transversal de trazabilidad** vienen en «No» desde la fase A, y son lo que esta viene a cerrar |
| **Defectos abiertos aceptados** | Ninguno propio. Hereda los dos de la fase A, que son su motivo |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Pendiente | `cmd_supersede` guarda el `--by` y la fecha |
| T-02 | Pendiente | Destapar la prueba del reemplazo |
| T-03 | Pendiente | Caso del enlace en los dos sentidos — CP-001 |
| T-04 | Pendiente | `cmd_archivar` guarda la fecha |
| T-05 | Pendiente | Destapar la prueba de archivar |
| T-06 | Pendiente | Caso de la señal vieja que **no** se rellena — CP-004 |
| T-07 | Pendiente | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 7. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Se reutilizan `cerrada_en` y `cierra_ref` para los tres caminos: tres pares de columnas para lo mismo obliga a migrar y a mirar tres sitios | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Las columnas **no se renombran**, aunque el nombre quede corto: renombrar obliga a migrar las bases que existen, y el costo no lo paga un nombre | §2.6 del plan |
| **Las señales marcadas antes del cambio se quedan sin fecha.** Rellenarlas con hoy sería inventar cuándo se marcaron: se vería más prolijo y sería falso | CP-004 del [`plan_pruebas.md`](plan_pruebas.md) |
| «Quién» se cubre con la referencia: no hay identidad de usuario en la base, y agregarla es otra decisión | §2.6 del plan |
| Lo que dice **qué** pasó es el estado; la fecha solo dice **cuándo**. Por eso reutilizar la columna no confunde archivada con cerrada | CP-002, paso 5 |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar: §2.7 no dejó dudas.
- **Si alguien rellena después las señales viejas «para que queden completas»** (riesgo `R-03`): queda escrito por qué se dejan vacías. Es el riesgo de que un arreglo cosmético falsee historia.
- **Registrar quién marcó** queda fuera: no hay identidad en la base. Si alguna vez se quiere, es una decisión aparte.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 4 esperando la aprobación del plan, que es la puerta normal, no un bloqueo.
