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

**Estación actual:** 9 — commit único. **Última puerta pasada:** 8, con la trazabilidad cerrada.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 presentado el 2026-08-17 | ☑ |
| 5 | Aprobación del plan detallado | 👤 «autorizados los planes de trabajo», 2026-08-17 | ☑ |
| 6 | Ejecución continua | 5 tareas, las 5 hechas | ☑ |
| 7 | Pruebas | [`resultado_pruebas.md`](resultado_pruebas.md) con veredicto **No cumple** | ☑ |
| 8 | Cierre documental | [`funcionalidad_implementada.md`](funcionalidad_implementada.md), §8 de la HU y fila del inventario 48 | ☑ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** Esta fase **mide** el instalador; no lo cambia. Es el programa que modifica otros proyectos.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **No cumple** |
| **CA cumplidos** | 1 de 2, y los dos transversales |
| **CA en "No"** | El **CA-02**: la simulación dice que no hay registro de versión que escribir, y al aplicar lo escribe |
| **Defectos abiertos aceptados** | 3 — `D-01` el archivo que aparece sin anunciarse; `D-02` la línea de `git config` pide saber de git; `D-03` el plan declaró cobertura completa sin contar los transversales |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) de esta fase |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | **Hecha** | Bitácora de la corrida, paso por paso — CP-001 |
| T-02 | **Hecha** | Buscar si hay vista previa sin ejecutar — CP-002 |
| T-03 | **Hecha** | Caso de qué se escribe y qué se pide antes — CP-003 |
| T-04 | **Hecha** | Anotar el resultado y, si falta la vista previa, proponerla con su costo |
| T-05 | **Hecha** | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 5 de 5. **Bloqueadas:** ninguna.

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

No se bloqueó. Está detenida en la etapa 9 esperando la autorización del commit, que es la puerta normal.
