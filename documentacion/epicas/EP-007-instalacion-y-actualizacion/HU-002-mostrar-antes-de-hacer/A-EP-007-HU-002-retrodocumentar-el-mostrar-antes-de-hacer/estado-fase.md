# Estado de fase — Fase A-EP-007-HU-002-retrodocumentar-el-mostrar-antes-de-hacer (módulo Instalación)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-007-HU-002-retrodocumentar-el-mostrar-antes-de-hacer` |
| **Módulo** | Instalación — [`validadores/instalar.py`](../../../../../validadores/instalar.py) |
| **Épica / HU / origen** | [EP-007](../../epica.md) · [HU-002](../HU-002-mostrar-antes-de-hacer.md) · retro-documentación, fila de HU-002 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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
| 6 | Ejecución continua | 5 tareas, ninguna empezada | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** Esta fase **mide** el instalador; no lo cambia. Es el programa que modifica otros proyectos.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 2 |
| **CA en "No"** | Ninguno todavía. El **CA-01 está sin establecer**: hay que medir si el instalador muestra el plan **antes** y espera, o lo cuenta mientras lo hace |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Pendiente | Bitácora de la corrida, paso por paso — CP-001 |
| T-02 | Pendiente | Buscar si hay vista previa sin ejecutar — CP-002 |
| T-03 | Pendiente | Caso de qué se escribe y qué se pide antes — CP-003 |
| T-04 | Pendiente | Anotar el resultado y, si falta la vista previa, proponerla con su costo |
| T-05 | Pendiente | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 5. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| **Se mide antes de proponer.** Ya pasó en esta casa que una HU nació pidiendo algo que ya existía, y hubo que recortarla el mismo día | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| La corrida va sobre un proyecto de prueba: el instalador escribe archivos, y sobre un proyecto vivo eso es tocar trabajo ajeno | §2.6 del plan |
| Si falta la vista previa, se propone **con el costo**: es el programa que modifica otros proyectos, y cambiarlo se aprueba aparte | §2.6 del plan y riesgo `R-03` |
| Lo que el instalador escribió se mide **sobre el árbol**, no sobre lo que el programa dice que hizo | CP-001 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar: §2.7 no dejó dudas.
- **El módulo de instalación no tiene especificación aparte.** Se declara como deuda en las fases hermanas de esta épica.
- **Si el CA-01 resulta cumplido** (riesgo `R-01`), la fase igual deja un resultado: qué muestra el instalador y en qué momento, que hoy no está escrito en ninguna parte.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 4 esperando la aprobación del plan, que es la puerta normal, no un bloqueo.
