# Estado de fase — Fase A-EP-004-HU-012-contar-las-marcas-de-generacion-automatica (módulo Comprobación automática)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-012-contar-las-marcas-de-generacion-automatica` |
| **Módulo** | Comprobación automática — [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) y [`marcadores-de-ia.md`](../../../../../base/00-identidad-y-rol/marcadores-de-ia.md) |
| **Épica / HU / origen** | [EP-004](../../epica.md) · [HU-012](../HU-012-marcas-de-generacion-automatica.md) · ✨ funcionalidad nueva. Fila de HU-012 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** cerrada. **Última puerta pasada:** 9, el commit `cf21890`.

> **La estación se corrigió el 2026-08-25**, leyendo el historial: el trabajo de esta fase estaba guardado desde hacía tiempo, y lo que faltaba era la marca. El hash sale de `git log` sobre su documento de cierre, no de una suposición.

**La duda que la detenía ya estaba contestada en el pendiente 11**, desde el 2026-08-10 — ver §4 del [resultado_pruebas.md](resultado_pruebas.md).

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 presentado el 2026-08-17 | ☑ |
| 5 | Aprobación del plan detallado | 👤 «autorizados los planes de trabajo», 2026-08-17 | ☑ |
| 6 | Ejecución continua | 7 tareas | ☑ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☑ Cumple, ciclo 1 |
| 8 | Cierre documental | trazabilidad sin faltantes | ☑ |
| 9 | Commit único | 👤 Commit `cf21890`, verificado en el historial | ☑ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Construido el 2026-08-18.** Era cierto que ningún programa las comprobaba: [`validadores/marcas.py`](../../../../../validadores/marcas.py) es el primero. El recuento dio **16 477 marcas en 820 archivos** fuera del histórico, y **4 491 en lo que se hereda**.


---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 3 |
| **CA en "No"** | Los **tres están en «No» de entrada**: la exigencia está escrita y ningún programa la mira |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

> **Puesto al día el 2026-08-22.** Este documento decía que no se había ejecutado ninguna tarea, y la fase estaba **hecha y probada**: su [resultado_pruebas](resultado_pruebas.md) trae el veredicto y su [funcionalidad_implementada](funcionalidad_implementada.md) el cierre. Lo que faltaba era este archivo, que es justo el que una sesión nueva lee para saber por dónde va. Sale del [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md).

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | Comprobación de las marcas de tipografía. Duda 1: cambia qué archivos recorre |
| T-02 | Hecha | Caso del texto con marcas — CP-002 |
| T-03 | Hecha | Comprobación de los caracteres invisibles |
| T-04 | Hecha | Caso de las marcas invisibles — CP-003 |
| T-05 | Hecha | Lista de lo que es notación del estándar. **Va primero: sin ella el programa reporta todo** |
| T-06 | Hecha | Caso de la corrida sobre `base/` — CP-001 |
| T-07 | Hecha | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 7 de 7. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| La lista de marcas se **lee** del capítulo y no se copia dentro del programa: dos listas de lo mismo se separan solas, y la del capítulo es la que manda | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| La notación propia se declara en el mismo capítulo, no como excepción escondida en el código: quien reciba un hallazgo tiene que poder leer por qué su símbolo cuenta y otro no | §2.6 del plan |
| El programa cuenta y **no corrige**: borrar marcas de un texto ajeno sin aprobación es cambiar el entregable | §2.6 del plan |
| El caso del falso positivo se prueba **antes** que el acierto: un programa que reporta el estándar entero no llega a correrse dos veces | CP-001 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **Duda 1 de §2.7:** si la comprobación aplica a todo el repositorio o solo a lo que se entrega. El histórico, por ejemplo, es transcripción y no entregable. Cambia qué archivos recorre el programa.
- **La aprobación del plan.** Sin ella no se escribe el validador.
- **El propio estándar tiene marcas** (pendiente [11](../../../../../pendientes/hecho/limpiar-marcadores-de-ia-del-texto-del-estandar.md)). La corrida va a dar una cuenta alta; se presenta **aparte** de la de un entregable nuevo, o el programa parece inservible (riesgo `R-01`).
- **Si un símbolo no se puede clasificar por contexto** (riesgo `R-02`): se declara no comprobable y se escribe por qué.

---

## 4. Si se bloqueó

- **Estación:** 6 — ejecución continua, detenida. **Motivo:** el plan **está aprobado** desde el 2026-08-17, y la duda 1 cambia qué recorre el programa. **Qué falta para desbloquear:** que el usuario apruebe el plan y diga si la comprobación aplica a todo el repositorio o solo a lo entregable. La lista de notación propia (T-05) puede escribirse apenas se apruebe, y conviene que sea lo primero.
