# Estado de fase — Fase A-EP-007-HU-005-retrodocumentar-que-no-se-pisa-lo-escrito (módulo Instalación)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-007-HU-005-retrodocumentar-que-no-se-pisa-lo-escrito` |
| **Módulo** | Instalación — [`validadores/instalar.py`](../../../../../validadores/instalar.py) |
| **Épica / HU / origen** | [EP-007](../../epica.md) · [HU-005](../HU-005-no-pisar-lo-escrito.md) · retro-documentación, fila de HU-005 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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

**Nada se ejecutó todavía.** Todo va sobre copias temporales: ningún proyecto vivo se actualiza.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 2 |
| **CA en "No"** | Ninguno todavía. El **CA-02 está sin establecer**: hay que medir si el registro dice, archivo por archivo, qué se reemplazó |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Pendiente | Prueba del archivo modificado a mano — CP-001 |
| T-02 | Pendiente | Caso del `CLAUDE.md` con texto propio — CP-002 |
| T-03 | Pendiente | Levantar qué se reemplaza y qué se conserva — CP-003 |
| T-04 | Pendiente | Caso del registro de la versión — CP-004 |
| T-05 | Pendiente | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 5. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| La prueba modifica un archivo a mano **antes** de actualizar: existir y conservar el contenido no es lo mismo, y lo que se pierde es el contenido | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Se prueba con el archivo que **más duele**: el `CLAUDE.md` del proyecto, que mezcla lo heredado con lo propio | §2.6 del plan |
| Lo que se encuentre mal **se para y se reporta**: que el instalador pise algo es un defecto grave y merece su plan, no un arreglo al vuelo | §2.6 del plan y riesgo `R-01` |
| El registro puede mentir por los pendientes [44](../../../../../pendientes/44-el-registro-de-version-no-se-escribe-si-no-cambia-una-huella.md) y [46](../../../../../pendientes/46-el-registro-de-version-dice-que-falta-escribirse.md): se prueba igual, y lo que salga es la evidencia que esos pendientes necesitan | Riesgo `R-03` del plan |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar: §2.7 no dejó dudas.
- **El caso ambiguo**: un archivo **heredado** que el proyecto modificó a mano. Ahí conservar y actualizar se contradicen, y lo que importa es que el instalador tenga una respuesta y quede escrita.
- **El módulo de instalación no tiene especificación aparte.** Se declara como deuda en las fases hermanas de esta épica.
- **Si el CA-01 falla, la fase se detiene** (riesgo `R-01`) y no sigue hasta que el usuario decida.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 4 esperando la aprobación del plan, que es la puerta normal, no un bloqueo.
