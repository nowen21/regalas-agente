# Pendiente · El aviso de vuelta llega a uno de nueve proyectos

**Estado:** abierto · anotado 2026-08-18 · sale de correr por primera vez de verdad el aviso de [`02·F24`](../base/02-flujo-de-trabajo/reglas/F24-el-defecto-del-estandar-se-reporta-no-se-corrige.md), al cerrar el [36](hecho/el-defecto-del-estandar-se-reporta-y-se-avisa-de-vuelta.md).

| | |
|---|---|
| **Historia de usuario** | [EP-007 · HU-003 — Crear la estructura de carpetas del trabajo](../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-003-estructura-de-carpetas/HU-003-estructura-de-carpetas.md) — la carpeta que falta es la que el instalador debería dejar puesta |
| **Proyecto de origen** | Nace acá, no lo reportó ningún proyecto |

## El problema

El [36](hecho/el-defecto-del-estandar-se-reporta-y-se-avisa-de-vuelta.md) decía «avisar a **todos** los proyectos instalados, no solo al de origen: la regla los rige a todos». Al correrlo, el aviso llegó a **uno**.

| Proyecto del registro | Existe en disco | Tiene `pendientes/` |
|---|:--:|:--:|
| AgroSystem | ☑ | ☐ |
| RNI (Defensoría) | ☑ | ☐ |
| LocalHub | ☑ | ☐ |
| Proyecto de grado | ☑ | ☐ |
| Aspectos legales | ☑ | ☐ |
| Gestión de Servicios Tecnológicos | ☑ | ☐ |
| dp_card | ☑ | ☐ |
| shopnest-mesa | ☑ | ☑ |
| `tmp5xnc44vw` | ☑ | ☐ |

**No es una falla del aviso.** Está haciendo lo que se decidió: a un proyecto que no lleva backlog **no se le inventa la carpeta**, porque escribir en el repositorio de otro tiene que tener el alcance de una línea. La decisión sigue siendo la correcta.

**Lo que falla es más arriba:** el instalador no deja `pendientes/` puesta, así que ocho de nueve proyectos **no tienen dónde recibir nada**. Y ahí no se trata de un aviso: es que **ninguno de esos ocho tiene dónde escribir un pendiente**, ni suyo ni de nadie. El aviso solo lo hizo visible.

## Qué se debe decidir

| # | Decisión | Nota |
|---|---|---|
| 1 | Si `pendientes/` entra a la estructura que crea el instalador | Es la salida limpia: la carpeta existe desde el día uno y el aviso llega solo |
| 2 | Si el que ya está instalado la recibe al ponerse al día | Sin esto, los ocho siguen sin carpeta hasta que alguien reinstale |
| 3 | Qué hacer con los proyectos que no la quieran | Hoy no recibir nada es el comportamiento, y es silencioso: nadie se entera de que se perdió un aviso |

**El 3 es el que importa.** Un aviso que no llega y no se dice **es el mismo defecto que el 36 vino a cerrar**, un nivel más abajo: allá el estándar no avisaba; acá avisa y el aviso se cae sin ruido.

## Y una línea de limpieza

El registro tiene una fila `tmp5xnc44vw` que apunta a una carpeta temporal — resto de una corrida de prueba. No hace daño porque esa carpeta no lleva `pendientes/`, pero es un destinatario que nadie puso a propósito. [`plantillas/proyectos.md`](../plantillas/proyectos.md) no se versiona, así que se borra y ya.
