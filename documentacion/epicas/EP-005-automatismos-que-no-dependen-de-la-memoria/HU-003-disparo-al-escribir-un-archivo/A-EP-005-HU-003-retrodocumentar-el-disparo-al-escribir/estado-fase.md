# Estado de fase — Fase A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir (módulo Automatismos)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir` |
| **Módulo** | Automatismos — [`hook_md.py`](../../../../../validadores/hook_md.py) |
| **Épica / HU / origen** | [EP-005](../../epica.md) · [HU-003](../HU-003-disparo-al-escribir-un-archivo.md) · retro-documentación, fila de HU-003 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 4 — pausa y presentación. **Última puerta pasada:** 3, con el plan de trabajo y el plan de pruebas escritos.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 pendiente: falta presentarlo | ☐ |
| 5 | Aprobación del plan detallado | 👤 pendiente | ☐ |
| 6 | Ejecución continua | 6 tareas, ninguna empezada | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** El enganche corre en cada escritura: esta fase lo **mide**, no lo cambia.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 3 |
| **CA en "No"** | Ninguno todavía. El **CA-03 está a medias de entrada**: el enganche no distingue entre detener y avisar como sí lo hace la línea de comandos |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Pendiente | Caso del documento con enlace roto — CP-001 |
| T-02 | Pendiente | Prueba del silencio ante lo que no es documento — CP-002 |
| T-03 | Pendiente | Caso del documento de otra carpeta — CP-002 |
| T-04 | Pendiente | Levantar qué hace hoy con una falla y con un aviso — CP-003 |
| T-05 | Pendiente | Caso del enlace roto contra el índice desactualizado — CP-003 |
| T-06 | Pendiente | Correr, escribir el incremento de la especificación y cerrar la trazabilidad |

**Hechas:** 0 de 6. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| El CA-03 se responde **midiendo**, no cambiando: tocar el enganche que corre en cada escritura sin saber qué hace es la forma de romper el flujo de todas las sesiones | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| La prueba del silencio pesa igual que la del disparo: un enganche que habla de más se apaga, y apagado no dispara nada | §2.6 del plan |
| Se prueba la **función que decide**, no el disparo: atar la prueba a la herramienta que lo dispara la vuelve frágil | Riesgo `R-02` del plan |
| Si el CA-03 queda sin cumplir, se escribe qué falta y se propone. Es un resultado, no un fracaso | Riesgo `R-01` del plan |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar: §2.7 no dejó dudas.
- **El CA-03 puede quedar sin cumplir.** Lo que falte se propone; cambiar el enganche es otra fase con su propio plan.
- **Si otra sesión está tocando `validadores/pruebas.py`** (riesgo `R-03`): se guarda solo lo propio.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 4 esperando la aprobación del plan, que es la puerta normal, no un bloqueo.
