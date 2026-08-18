# Estado de fase — Fase B-EP-006-HU-003-la-busqueda-dice-donde-esta (módulo Memoria)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `B-EP-006-HU-003-la-busqueda-dice-donde-esta` |
| **Módulo** | Memoria — [`memoria/memoria.py`](../../../../../memoria/memoria.py) |
| **Épica / HU / origen** | [EP-006](../../epica.md) · [HU-003](../HU-003-busqueda-por-palabra.md) · **defecto** de la fase [`A`](../A-EP-006-HU-003-retrodocumentar-la-busqueda-por-palabra/resultado_pruebas.md) |
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

**Nada se ejecutó todavía.** Los dos defectos ya tienen su prueba escrita, en rojo esperado, desde la fase A.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 1 |
| **CA en "No"** | El **CA-01** viene en «No» desde la fase A, y es lo que esta viene a cerrar |
| **Defectos abiertos aceptados** | Ninguno propio. Hereda los dos de la fase A, que son su motivo |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Pendiente | `where_` al `SELECT` y a la línea |
| T-02 | Pendiente | Destapar `test_el_resultado_dice_donde_esta_la_senal` |
| T-03 | Pendiente | Caso de la señal **sin** `where_` — CP-002 |
| T-04 | Pendiente | Cerrar la conexión del camino vacío |
| T-05 | Pendiente | Destapar `test_la_busqueda_sin_resultados_cierra_su_conexion` |
| T-06 | Pendiente | Quitar `ignore_cleanup_errors` de la clase — CP-003 paso 4 |
| T-07 | Pendiente | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 7. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Las dos pruebas **se destapan**, no se reescriben: están escritas contra el criterio y ya describen el defecto | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El orden importa: **primero arreglar, después destapar**. Al revés, la suite queda en rojo y no se sabe si falló el arreglo o la prueba | §4 del plan |
| `where_` sale solo cuando tiene valor: una columna vacía en cada línea ensucia la salida de todas para servir a algunas | §2.6 del plan |
| **El plan de pruebas cuenta los transversales**, que es lo que le faltó a las 51 fases del 2026-08-17 | La nota de cabecera del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar: §2.7 no dejó dudas.
- **Si la línea queda ilegible con rutas largas** (riesgo `R-01`): se anota con la salida a la vista y se decide. No se adivina antes de verla.
- **Si al destapar una prueba sigue en rojo** (riesgo `R-02`): el arreglo no era el que faltaba. Es el resultado honesto y se escribe.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 4 esperando la aprobación del plan, que es la puerta normal, no un bloqueo.
