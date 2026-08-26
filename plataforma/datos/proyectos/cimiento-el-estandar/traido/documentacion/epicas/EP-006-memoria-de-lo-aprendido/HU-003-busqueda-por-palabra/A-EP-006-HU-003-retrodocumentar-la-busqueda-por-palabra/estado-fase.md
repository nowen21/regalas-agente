# Estado de fase — Fase A-EP-006-HU-003-retrodocumentar-la-busqueda-por-palabra (módulo Memoria)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-003-retrodocumentar-la-busqueda-por-palabra` |
| **Módulo** | Memoria — [`memoria/memoria.py`](../../../../../memoria/memoria.py) |
| **Épica / HU / origen** | [EP-006](../../epica.md) · [HU-003](../HU-003-busqueda-por-palabra.md) · retro-documentación, fila de HU-003 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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

**`memoria.py` y el esquema no se tocaron**, como decía §2.1 del plan — aun cuando la corrida encontró dos defectos en `cmd_search` que se arreglan con una línea cada uno. Están probados, no parcheados.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **No cumple** |
| **CA cumplidos** | 1 de 2. Y los tres RNF y los dos transversales, todos en «Sí» |
| **CA en "No"** | **CA-01**, en su segunda mitad: la búsqueda encuentra pero **no dice dónde está** lo encontrado, así que el resultado no alcanza para abrir |
| **Defectos abiertos aceptados** | 3 — `D-01` la búsqueda no imprime `where_`; `D-02` el camino sin resultados no cierra la conexión; `D-03` el plan declaró 100% de cobertura sin contar los transversales |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) de esta fase |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | **Hecha** | CP-001. Destapó `D-01`: el paso 2 falla |
| T-02 | **Hecha** | CP-002, en los dos sentidos. Pasa |
| T-03 | **Hecha** | CP-003, con los filtros combinados. Pasa |
| T-04 | **Hecha** | CP-004, incluido el paso que separa archivar de borrar. Pasa |
| T-05 | **Hecha** | Corrida completa (39 pruebas, verde con 2 fallos esperados), resultado escrito y trazabilidad cerrada |

**Hechas:** 5 de 5. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Se prueba que el índice esté **sincronizado**, no solo que la búsqueda responda: un índice desincronizado responde mal, y eso es peor que no responder | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El caso de lo archivado entra en esta fase porque **no aparecer en la búsqueda** es comportamiento de la búsqueda; marcarlo es de [HU-007](../../HU-007-marcar-lo-que-dejo-de-aplicar/HU-007-marcar-lo-que-dejo-de-aplicar.md) | §2.6 del plan |
| Los acentos se prueban en los dos sentidos: un índice que normaliza solo al guardar, o solo al buscar, pasa la mitad de los casos | CP-002 del [`plan_pruebas.md`](plan_pruebas.md) |
| El caso comprueba que la señal archivada **sigue en la base**: con solo comprobar que no aparece, un programa que borra pasaría igual | CP-004 del `plan_pruebas.md` |

---

## 3. Pendiente / preguntas abiertas

- **Los dos arreglos de `cmd_search`**, que son una línea cada uno y no cabían en el plan aprobado: imprimir `where_` (`D-01`) y cerrar la conexión del camino vacío (`D-02`). Piden una fase `B-EP-006-HU-003` — proponerla es del agente, abrirla es del usuario.
- **El riesgo `R-01` no se materializó:** los tres triggers están sincronizados. Se comprobó con alta, modificación y borrado.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 9 esperando la autorización del commit, que es la puerta normal.
