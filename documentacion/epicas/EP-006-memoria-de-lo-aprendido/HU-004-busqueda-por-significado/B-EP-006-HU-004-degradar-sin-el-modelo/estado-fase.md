# Estado de fase — Fase B-EP-006-HU-004-degradar-sin-el-modelo (módulo Memoria)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `B-EP-006-HU-004-degradar-sin-el-modelo` |
| **Módulo** | Memoria — [`memoria/semantica.py`](../../../../../memoria/semantica.py) y [`memoria/memoria.py`](../../../../../memoria/memoria.py) |
| **Épica / HU / origen** | [EP-006](../../epica.md) · [HU-004](../HU-004-busqueda-por-significado.md) · **defecto** de la fase [`A`](../A-EP-006-HU-004-retrodocumentar-la-busqueda-por-significado/resultado_pruebas.md) |
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

**Nada se ejecutó todavía.** **Es la fase más urgente de las ocho que dejó la sesión:** hoy, una máquina nueva o una caché borrada dejan la memoria entera sin responder.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 1 |
| **CA en "No"** | El **CA-02** y el **transversal de privacidad** vienen en «No» desde la fase A, y son lo que esta viene a cerrar |
| **Defectos abiertos aceptados** | Ninguno propio. Hereda los dos de la fase A, que son su motivo |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Pendiente | `disponible()` comprueba que el modelo cargue, y recuerda el resultado |
| T-02 | Pendiente | `cmd_search` atrapa el fallo y sigue con la léxica, diciéndolo |
| T-03 | Pendiente | Destapar la prueba en rojo esperado |
| T-04 | Pendiente | Caso: con el modelo ausente responde **y avisa** — CP-001 |
| T-05 | Pendiente | Cargar el modelo en modo sin conexión |
| T-06 | Pendiente | Caso del socket **cortado**, no caído — CP-003 |
| T-07 | Pendiente | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 7. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| `disponible()` pasa a responder «¿puedo buscar por significado?» y no «¿están las librerías?»: que responda que sí y después reviente **es** el defecto | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Si el modelo falta se **degrada y se dice**, no se descarga: instalar algo sin que nadie lo pida es lo contrario de opt-in | §2.6 del plan |
| **Degradar en silencio es peor que caerse**: el usuario creería que buscó por significado | CP-001 del [`plan_pruebas.md`](plan_pruebas.md) |
| El socket se **corta**, no se hace fallar. Con un fallo de conexión el `hub` degrada a la caché y el caso pasaría aunque el programa saliera a la red — es lo que le pasó a la fase A | CP-003 del plan de pruebas |
| El modelo ausente se simula apuntando a uno inexistente: borrar la caché rompe el entorno de quien corre la prueba | §6 del plan |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar: §2.7 no dejó dudas.
- **Si el modo sin conexión impide descargar el modelo la primera vez** (riesgo `R-02`): se comprueba que la orden `indexar`, que es explícita, sí pueda, y se escribe cómo se instala.
- **Si atrapar el fallo esconde un error distinto** (riesgo `R-03`): se atrapa el de la carga, no cualquiera, y el aviso dice qué pasó.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 4 esperando la aprobación del plan, que es la puerta normal, no un bloqueo.
