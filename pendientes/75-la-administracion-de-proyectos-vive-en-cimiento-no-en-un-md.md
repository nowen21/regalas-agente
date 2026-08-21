# Pendiente · La administración de los proyectos vive en Cimiento, no en un `.md` hardcodeado

**Estado:** abierto, anotado el 2026-08-21.

| | |
|---|---|
| **Historia de usuario** | [EP-007 · HU-006 — Poner al día lo ya instalado](../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-006-poner-al-dia/HU-006-poner-al-dia.md). Es la épica dueña del ciclo de vida de los proyectos instalados; si la interfaz crece a más que el registro, puede pedir épica propia y eso se decide al bajar este pendiente |
| **De dónde sale** | Pedido del usuario en el chat del 2026-08-21, al analizar el pendiente [73](hecho/la-guia-de-entrada-es-del-estandar.md); sus palabras literales en [prompts/la-administracion-de-proyectos-desde-cimiento.md](../prompts/la-administracion-de-proyectos-desde-cimiento.md) |
| **Proyecto de origen** | El estándar mismo |

## El problema

Cimiento existe para **obligar a cada proyecto a cumplir los estándares y reglas definidos**, pero la lista de proyectos sobre la que actúa es un archivo estático: [plantillas/proyectos.md](../plantillas/proyectos.md), donde cada proyecto está escrito a mano. Todo lo que administra proyectos cuelga de ese archivo: el instalador lo lee para desplegar, los pendientes reportados dicen «avisar a todos los instalados: la lista está en `plantillas/proyectos.md`», y nada impide que la lista envejezca sin que nadie lo note.

El usuario fijó la dirección: los proyectos deben poderse **registrar, configurar, consultar y administrar desde la propia interfaz de Cimiento**, de manera que el sistema les aplique las reglas y valide su cumplimiento de forma centralizada — no desde un `.md` hardcodeado.

## Por qué importa

No bloquea nada hoy: el `.md` funciona. El daño es el de todo registro a mano: se desactualiza en silencio (un proyecto que se movió de carpeta, uno que ya no existe, uno instalado que nadie anotó), y cada operación sobre «todos los instalados» —desplegar un enganche, avisar un cierre, medir cumplimiento— depende de que esa lista esté al día. Además deja la administración fuera del propio mecanismo que Cimiento predica: el estándar exige a los proyectos datos estructurados y validables, pero se administra a sí mismo con texto suelto.

## Qué falta

Decidir y construir la interfaz de administración. Piezas visibles desde hoy, en orden de dependencia:

1. **El registro como dato estructurado, no como prosa**: qué es un proyecto para Cimiento (ruta, stack, versión adoptada, estado, pendientes de seguimiento) y dónde vive ese dato de forma consultable por programa.
2. **Las operaciones sobre el registro**: registrar, configurar, consultar, dar de baja — desde la interfaz de Cimiento (hoy, sus comandos; lo que sea «aplicación» lo decide el diseño), no editando un archivo.
3. **Lo que consume el registro se reconecta**: el instalador, los avisos de cierre de pendientes reportados y la validación centralizada de cumplimiento leen del registro, y `plantillas/proyectos.md` deja de ser la fuente (o pasa a generarse desde ella).

## La decisión del usuario — 2026-08-21

**La interfaz ya existe y es [`interfaz/`](../interfaz/README.md)**: la aplicación Django del visor (panel, memoria, documentos). Y el usuario fijó su segunda exigencia: **debe tener la estructura de la plantilla [plantillas/estructura-proyecto-django.md](../plantillas/estructura-proyecto-django.md)** — la misma que el estándar le exige a cualquier proyecto Django heredero.

Hoy no la tiene. Verificado el 2026-08-21 contra lo versionado:

| Lo que la plantilla exige | Lo que `interfaz/` tiene hoy |
|---|---|
| Nada de terceros copiado al repositorio: se declara en `requirements/` y lo junta `collectstatic` | `visor/static/vendor/` versionado: Bootstrap, AdminLTE, Bootstrap Icons y Chart.js copiados |
| `requirements/` con `base.txt`, `local.txt` y `lock.txt` (`10·DEP2`) | Un `requirements.txt` plano |
| `config/settings/` con `base.py` y `local.py` | Un `config/settings.py` único |
| `.env` fuera del repo y `.env.example` versionado con las variables sin valor | No hay ninguno de los dos |
| Cada módulo con `models.py · admin.py · forms.py · views.py · tests.py · apps.py · migrations/` | `visor/` no tiene modelos, admin, formularios, pruebas ni migraciones |

Lo que sí está bien: la base de datos local (`_visor.sqlite3`) y los `__pycache__/` ya los ignora git.

Con esto el pendiente deja de ser «falta decidir» en lo grueso; queda **P2** con dos frentes que pueden ser fases separadas: **(a)** llevar `interfaz/` a la estructura de la plantilla, y **(b)** el registro de proyectos como dato administrable desde ella (las piezas 1 a 3 de arriba).

## El límite

No pide construir una aplicación gráfica ya: pide sacar la administración del `.md` y centralizarla en Cimiento. Tampoco toca el contenido de las reglas ni cómo se validan — solo sobre **qué proyectos** y **desde dónde** se administra. Y no cubre el pendiente 73 (la guía doctrinal), que sigue su propio camino.

## Cómo se sabrá que cerró

Un proyecto se puede registrar, consultar, configurar y dar de baja sin editar ningún `.md` a mano; el instalador y los avisos a instalados operan leyendo ese registro; y `plantillas/proyectos.md` ya no es la fuente de verdad (existe solo si se genera desde el registro).
