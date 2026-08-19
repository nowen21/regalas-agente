# Pendiente · El aviso de vuelta llega a uno de nueve proyectos

**Estado:** cerrado 2026-08-18 · anotado 2026-08-18 · sale de correr por primera vez de verdad el aviso de [`02·F24`](../../base/02-flujo-de-trabajo/reglas/F24-el-defecto-del-estandar-se-reporta-no-se-corrige.md), al cerrar el [36](el-defecto-del-estandar-se-reporta-y-se-avisa-de-vuelta.md).

| | |
|---|---|
| **Historia de usuario** | [EP-007 · HU-003 — Crear la estructura de carpetas del trabajo](../../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-003-estructura-de-carpetas/HU-003-estructura-de-carpetas.md) — la carpeta que falta es la que el instalador debería dejar puesta |
| **Proyecto de origen** | Nace acá, no lo reportó ningún proyecto |

## El problema

El [36](el-defecto-del-estandar-se-reporta-y-se-avisa-de-vuelta.md) decía «avisar a **todos** los proyectos instalados, no solo al de origen: la regla los rige a todos». Al correrlo, el aviso llegó a **uno**.

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

El registro tiene una fila `tmp5xnc44vw` que apunta a una carpeta temporal — resto de una corrida de prueba. No hace daño porque esa carpeta no lleva `pendientes/`, pero es un destinatario que nadie puso a propósito. [`plantillas/proyectos.md`](../../plantillas/proyectos.md) no se versiona, así que se borra y ya.


---

# Cómo cerró — 2026-08-18

**Las tres decisiones las tomó el usuario.**

| # | Decisión | Qué se hizo |
|---|---|---|
| 1 | `pendientes/` entra a la estructura | ✅ Entró a `CARPETAS_BASE` del instalador y a [`02·F13`](../../base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md) |
| 2 | El que ya está instalado la recibe | ✅ **Sale gratis:** esa lista se recorre en **cada** instalación, no solo en la primera |
| 3 | El aviso que no llega se dice | ✅ `cerrar.py` lista a quién no llegó y por qué |

## La 2 no costó nada, y conviene que se sepa por qué

`instalar_estructura()` recorre `CARPETAS_BASE` y crea lo que falte, en cada corrida. **No hubo que escribir una migración:** los ocho proyectos reciben la carpeta la próxima vez que se pongan al día. Está fijado en un caso de prueba, porque es la clase de cosa que se rompe sin que nadie note.

## La 3 es la que importaba, y el pendiente ya lo decía

> *Un aviso que no llega y no se dice **es el mismo defecto que el 36 vino a cerrar**, un nivel más abajo: allá el estándar no avisaba; acá avisa y el aviso se cae sin ruido.*

Antes, un proyecto sin carpeta era un `continue` mudo. Ahora `avisar()` devuelve **dos** listas —lo entregado y lo que no— y `cerrar.py` imprime la segunda:

```
  El aviso NO llegó a 8 proyecto(s):
    · AgroSystem — no tiene `pendientes/` — la crea el instalador al ponerse al día
```

**No se le inventa la carpeta a nadie**, que era la decisión de fondo y sigue en pie: escribir en el repositorio de otro tiene que tener el alcance de una línea. Lo que cambió es que ahora se sabe.

Y se agregó un caso que el pendiente no nombraba: **el proyecto cuya carpeta ya no existe**. El registro de proyectos es un archivo local, y una ruta puede haber desaparecido; eso también se dice en vez de callarse.

## La línea de limpieza

La fila `tmp5xnc44vw` del registro local —resto de una ejecución de prueba— quedó borrada.

## Cómo se comprueba

**9 casos** en [`validadores/tests/test_aviso_de_vuelta.py`](../../validadores/tests/test_aviso_de_vuelta.py), sobre 23 del archivo. Cubren los dos lados en la misma vuelta: se escribe al que tiene carpeta y se reporta al que no.
