# Estado de fase — Fase A-EP-006-HU-004-retrodocumentar-la-busqueda-por-significado (módulo Memoria)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-004-retrodocumentar-la-busqueda-por-significado` |
| **Módulo** | Memoria — [`memoria/semantica.py`](../../../../../memoria/semantica.py) |
| **Épica / HU / origen** | [EP-006](../../epica.md) · [HU-004](../HU-004-busqueda-por-significado.md) · retro-documentación; salió del pendiente [05](../../../../../pendientes/hecho/memoria-semantica.md), ya cerrado. Fila de HU-004 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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

**No se desinstaló ni se instaló nada.** El escenario «sin dependencias» se simuló apagando `semantica.disponible()`, y el «sin modelo» apuntando `MEMORIA_MODELO` a uno inexistente. Tocar el entorno de trabajo lo habría roto, y no hacía falta.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **No cumple** |
| **CA cumplidos** | 1 de 2. El transversal de rendimiento, en «Sí» |
| **CA en "No"** | **CA-02** y su RNF: «sin el modelo la búsqueda sigue funcionando» — y **sin el modelo se cae entera**, incluida la parte léxica. Y el transversal de **privacidad**, que pedía cero conexiones y hay una |
| **Defectos abiertos aceptados** | 4 — `D-01` sin modelo se cae todo; `D-02` cargar el modelo abre una conexión; `D-03` de cinco resultados, tres son ruido; `D-04` el plan no contó los transversales |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) de esta fase |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | **Hecha** | CP-001. **3 de 3 consultas reales pasaron de 0 a 5 resultados** |
| T-02 | **Hecha** | CP-002. No pierde nada, y se midió el ruido: 2 de 5 sirven |
| T-03 | **Hecha** | CP-003. Sin librerías pasa; **sin modelo falla** — `D-01` |
| T-04 | **Hecha** | CP-004. El contenido no sale, pero abre una conexión — `D-02` |
| T-05 | **Hecha** | Corrida completa (59 pruebas, verde con 5 fallos esperados), resultado escrito y trazabilidad cerrada |

**Hechas:** 5 de 5. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| El escenario sin modelo se **simula**, no se desinstalan las dependencias: desinstalar rompe el entorno de trabajo de quien corre la prueba | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Que nada salga de la máquina se **comprueba**, porque es una regla blindada. Y se comprueba sobre el programa, no sobre la red: con la red caída, un programa que manda datos pasaría igual | §2.6 del plan y riesgo `R-02` |
| La mejora se mide con búsquedas reales, no con un puntaje del modelo: importa si encuentra lo que alguien buscaría | §2.6 del plan |
| Si la mejora es chica, es un resultado útil: se escribe la medida y se decide con el dato | Riesgo `R-01` del plan |
| **«Sin el modelo» y «sin las librerías» son dos escenarios distintos**, y el plan los trataba como uno. El segundo funciona; el primero se cae | CP-003 del [`resultado_pruebas.md`](resultado_pruebas.md) |
| **El ruido se mide y se escribe**: de cinco resultados de una consulta real, dos sirven. Pasar de nada a algo mayormente ruido es mejora; llamarlo precisión, no | `D-03` del resultado |
| Las pruebas que necesitan el modelo se **saltan** si no está, en vez de fallar: probar el complemento opcional no puede volverlo obligatorio | Clase `BusquedaPorSignificado` de [`memoria/pruebas.py`](../../../../../memoria/pruebas.py) |

---

## 3. Pendiente / preguntas abiertas

- **`D-01`, el más grave de la épica:** con las librerías instaladas y el modelo ausente, la búsqueda se cae entera y se lleva la léxica, que no necesita nada. Le pasaría a cualquier máquina nueva o con la caché borrada. Pide la fase `B-EP-006-HU-004`.
- **`D-02`:** cargar el modelo abre una conexión al repositorio remoto. No viaja el contenido de las señales, y aun así el caso pedía cero conexiones.
- **El riesgo `R-01` no se materializó:** la mejora **no** es chica. Tres de tres consultas reales pasaron de cero resultados a cinco.
- **El módulo de la memoria no tiene especificación aparte.** Es uno de los casos que [EP-001 · HU-010](../../../EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) viene a resolver.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 9 esperando la autorización del commit, que es la puerta normal.
