# Estado de fase — Fase B-EP-004-HU-016-todo-pendiente-abierto-nombra-su-historia (módulo Comprobación automática)

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `B-EP-004-HU-016-todo-pendiente-abierto-nombra-su-historia` |
| **Módulo** | Comprobación automática (`validadores/pendientes.py`) |
| **Planteamiento / Épica / HU** | [EP-004](../../epica.md) · [HU-016](../HU-016-el-pendiente-cerrado-nombra-su-fase.md) |
| **De dónde sale** | El usuario, el 2026-08-17: *«todos los pendientes deben estar dentro de una HU, nada puede estar suelto»* |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 4 — pausa y presentación. **Última puerta pasada:** 3.

Se usan las **once etapas de [`02·F15`](../../../../../base/02-flujo-de-trabajo/reglas/F15-no-saltes-ni-reordenes-las-once-etapas-de-la-fase.md)**.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 el usuario dijo «si ya existe la HU se crea otra fase» | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | **acá está** — presentados al usuario | ☑ |
| 5 | Aprobación del plan detallado | 👤 **acá está detenida** | ☐ |
| 6 | Ejecución continua | | ☐ |
| 7 | Pruebas | | ☐ |
| 8 | Cierre documental | | ☐ |
| 9 | Commit único | 👤 | ☐ |
| 10 | Reporte al usuario | | ☐ |
| 11 | Publicación / despliegue | 👤 | ☐ |

**Es la `B` y no la `A` porque la `A` ya existe.** La [fase A](../A-EP-004-HU-016-el-pendiente-cerrado-declara-su-fase/plan_trabajo.md) se abrió el 2026-08-17 con los 51 planes y comprueba al pendiente **cerrado**. Esta comprueba al **abierto**, que es la mitad que el usuario pidió ese mismo día.

---

> **Puesto al día el 2026-08-22.** La fase estaba detenida esperando dudas que solo el usuario podía contestar, y hoy las contesta el propio repositorio: quedan escritas en el §0.1 del [resultado_pruebas](resultado_pruebas.md). Se corrieron los casos y se cerró. Sale del [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md). Construida: la comprobación hacia arriba, que **detiene**.

## 1.1 Veredicto de las pruebas

Sin veredicto: la fase no se ha ejecutado. El `resultado_pruebas.md` y el `funcionalidad_implementada.md` nacen al ejecutar.

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 a T-12 | Hechas | Ejecutadas el 2026-08-22 con la orden del usuario de resolver el pendiente 59 |

**Hechas:** 12 de 12. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas

| Decisión / aprendizaje | Dónde queda |
|---|---|
| La ficha se reconoce por su encabezado sin nombres de columna, no por ser la primera tabla | Plan §2.6 y el `CP-005` |
| La exigencia se le pide al abierto y no al cerrado: el cerrado es de la fase A y de su fecha de corte | Plan §1, fuera de alcance |
| Esta fase **no espera** a la A: escriben funciones distintas del mismo archivo | Plan §2.2, comprobado |
| La fase A declara que **crea** `validadores/pendientes.py` y el archivo ya existe, escrito para HU-018. Su plan quedó viejo en ese punto | Plan §2.2. **Se reporta, no se corrige desde acá** ([`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)) |

---

## 3. Pendiente / preguntas abiertas

**La fase no tiene dudas propias.** Lo que la detiene es la aprobación, y lo que la deja incompleta son dos bloqueos que no le pertenecen:

- **B-01 · El texto de [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) no dice «desde que se abre».** Esta fase construye el programa que comprueba; la regla que exige sigue sin decirlo. Un programa que hace fallar por algo que la regla no pide es peor que no tenerlo.
- **B-02 · Ninguna historia es dueña del texto del capítulo `02`.** Se buscó el 2026-08-17 en las siete épicas: EP-001 declara como módulo los capítulos `00` y `01` y el cuerpo de reglas en general, y nadie declara el `02`. Sin dueño, el B-01 no tiene dónde caer. **Es un hueco del árbol de épicas** y sale como pendiente nuevo.

**Y una que sí es buena noticia:** esta fase **destraba la duda 27** del [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md) —«¿dónde se declara: una línea fija al principio, o una sección?»—, que es la segunda de las dos que detienen a la fase A. La respuesta ya no es una opinión: es la fila `Historia de usuario` de la ficha, medida en 33 archivos. Cerrarla formalmente es de la fase A, no de esta.

---

## 4. Si se bloqueó

No se bloqueó. Está esperando la puerta de la estación 5, que es donde tiene que estar.
