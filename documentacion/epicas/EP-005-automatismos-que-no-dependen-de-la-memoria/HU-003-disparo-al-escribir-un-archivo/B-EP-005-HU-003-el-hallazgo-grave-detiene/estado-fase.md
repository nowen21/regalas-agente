# Estado de fase — Fase B-EP-005-HU-003-el-hallazgo-grave-detiene (módulo Automatismos)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `B-EP-005-HU-003-el-hallazgo-grave-detiene` |
| **Módulo** | Automatismos — [`validadores/hook_md.py`](../../../../../validadores/hook_md.py) |
| **Épica / HU / origen** | [EP-005](../../epica.md) · [HU-003](../HU-003-disparo-al-escribir-un-archivo.md) · **defecto** de la fase [`A`](../A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir/resultado_pruebas.md) |
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
| 6 | Ejecución continua | 8 tareas, ninguna empezada | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |


---

> **Puesto al día el 2026-08-22.** La fase estaba detenida esperando dudas que solo el usuario podía contestar, y hoy las contesta el propio repositorio: quedan escritas en el §0.1 del [resultado_pruebas](resultado_pruebas.md). Se corrieron los casos y se cerró. Sale del [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md). El enganche ya estaba construido; faltaba correrlo por el camino real y escribir lo que dio.

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 1. El CA-01 y el CA-02 ya estaban en «Sí» tras la fase A y hay que mantenerlos |
| **CA en "No"** | El **CA-03** viene en «No» desde la fase A, y es lo que esta viene a cerrar |
| **Defectos abiertos aceptados** | Ninguno propio. Hereda el `D-01` de la fase A, que es su motivo |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | Que la falla pida detener el trabajo |
| T-02 | Hecha | Que el mensaje diga **qué arreglar y dónde** |
| T-03 | Hecha | Casos de detener y de **no** detener — CP-001 y CP-002 |
| T-04 | Hecha | Caso de reversibilidad: el archivo queda entero — CP-003 |
| T-05 | Hecha | Escribir qué pasa con el archivo ya escrito |
| T-06 | Hecha | Los transversales que ya pasaban, otra vez — CP-004 |
| T-07 | Hecha | §4.3 de la especificación pasa de «lo que no hace» a la regla |
| T-08 | Hecha | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 8 de 8. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| **«Detener» es detener el trabajo, no la escritura.** El enganche corre después de escribir: deshacer la escritura de otro sería más peligroso que el defecto que busca | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Solo detiene la **falla**, nunca el aviso — y la **cantidad de avisos no convierte un aviso en falla** | §2.6 del plan y CP-002 paso 4 |
| Lo que detiene **dice qué arreglar y dónde**: detener sin decir qué obliga a investigar, y eso es lo que hace que alguien apague el enganche | §2.6 del plan |
| **Esta fase enciende un transversal que hoy no aplica.** «Detener sin dejar el archivo a medias» deja de ser teoría en cuanto algo detenga | §0 del plan |
| Queda escrito **cómo desactivarlo por proyecto**: si detener resulta insoportable, mejor una puerta conocida que apagarlo a escondidas | §8 del plan |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar: §2.7 no dejó dudas de implementación.
- **Le sirve de precedente a dos preguntas del usuario.** Las 8 y 9 del [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md) —si el control del mensaje de commit y el de versión detienen o avisan— son la misma pregunta en otro sitio. **No bloquean esta fase**, pero lo que se decida acá debería valer allá.
- **Si un falso positivo llega como falla** (riesgo `R-02`): es defecto del validador que lo emite, y se reporta a su fase, no se tapa acá.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 4 esperando la aprobación del plan, que es la puerta normal, no un bloqueo.
