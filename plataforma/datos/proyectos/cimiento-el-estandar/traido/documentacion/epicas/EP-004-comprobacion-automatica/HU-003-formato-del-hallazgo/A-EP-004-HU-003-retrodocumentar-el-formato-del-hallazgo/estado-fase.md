# Estado de fase — Fase A-EP-004-HU-003-retrodocumentar-el-formato-del-hallazgo (módulo Comprobación automática)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-003-retrodocumentar-el-formato-del-hallazgo` |
| **Módulo** | Comprobación automática — [`validadores/comun.py`](../../../../../validadores/comun.py) |
| **Épica / HU / origen** | [EP-004](../../epica.md) · [HU-003](../HU-003-formato-del-hallazgo.md) · retro-documentación, fila de HU-003 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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

**Nada se ejecutó todavía.** §2.7 no dejó dudas abiertas.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **No cumple** |
| **CA cumplidos** | 3 de 3 numerados, y el transversal de límites. El de errores, en «No» |
| **CA en "No"** | El **transversal de errores**: un `.md` que no se puede decodificar revienta la corrida con un volcado de Python y se lleva los hallazgos ya encontrados |
| **Defectos abiertos aceptados** | 3 — `D-01` el archivo ilegible tumba la corrida; `D-02` el contrato no estaba escrito (corregido acá); `D-03` el plan declaró cobertura completa sin contar los transversales |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) de esta fase |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | **Hecha** | Caso de los tres datos en cada hallazgo — CP-001 |
| T-02 | **Hecha** | Caso de arreglar sin abrir el programa — CP-002 |
| T-03 | **Hecha** | Prueba del código de salida con solo avisos — CP-003 |
| T-04 | **Hecha** | Prueba del código de salida con una falla — CP-004 |
| T-05 | **Hecha** | Escribir el contrato en la documentación del módulo común, correr y cerrar |

**Hechas:** 5 de 5. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| El contrato de la salida se escribe en la documentación del módulo, no como regla de `base/`: el formato es de esta herramienta y `base/` es agnóstico de herramienta | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El código de salida se prueba con hallazgos armados, no provocando una falla real: así la prueba no depende de que exista un archivo roto | §2.6 del plan |
| El CA-01 se cierra **arreglando** dos defectos sin abrir el validador, no contando campos: es la única forma de saber si el hallazgo alcanza | CP-002 del [`plan_pruebas.md`](plan_pruebas.md) |
| El caso recorre todos los hallazgos de la corrida y no una lista fija, para que un validador nuevo entre solo y el contrato no envejezca | Riesgo `R-03` del plan |

---

## 3. Pendiente / preguntas abiertas

- **`D-01`, que la fase no preveía:** un `.md` que no se puede decodificar tumba la corrida entera. `comun.leer` abre sin red. Pide la fase `B-EP-004-HU-003`.
- **El riesgo `R-01` no se materializó:** los 85 hallazgos sin línea son todos de archivo entero, que es su forma definida, no un hueco.
- **Si otra sesión está tocando `validadores/pruebas.py`**: se guarda solo lo propio, y el estado de la suite se anota antes de tocarla.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 9 esperando la autorización del commit, que es la puerta normal.
