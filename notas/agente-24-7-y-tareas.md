# ¿Agente 24/7 o que ejecute tareas asignadas?

> Sí se puede, con un matiz de seguridad. Opciones de automatización, el trade-off con el modelo humano-en-el-medio, y la recomendación.

## Formas que permite Claude Code

| Forma | Qué es | Buen uso |
|---|---|---|
| **Rutinas programadas (cron)** | Corre a una hora/frecuencia fija | pruebas nocturnas, chequeos diarios |
| **Loop / intervalo** | Repite una tarea cada X tiempo | vigilar un estado, reintentar |
| **Headless / CI** | Disparar el agente desde un script con una tarea definida | un paso en un pipeline |
| **Cola de tareas** | Lista de tareas que el agente toma y ejecuta | asignar trabajo y que lo procese |

## El matiz (importante)

El estándar está hecho para **humano-en-el-medio**: el núcleo (`00`) exige OK para commits, push, tocar datos reales. Eso choca con "24/7 totalmente solo". Dos caminos:

- **Semi-autónomo (recomendado):** trabaja solo hasta una **puerta de aprobación** (spec, plan, commit) y ahí **pausa y espera**. Siempre disponible, avanza en lo seguro, no cruza lo riesgoso sin el usuario. Mantiene la seguridad. El **orquestador** ya sabe pausar en las puertas.
- **Autónomo total:** se relajan esas puertas para que no pare. Gana autonomía, **pierde la red de seguridad** (commits/cambios sin revisión). Riesgoso y contra el diseño.

## Qué dejar solo vs qué no

- ✅ **Seguro sin supervisión (solo lectura):** correr pruebas y reportar, análisis/diagnóstico, generar borradores de spec, buscar en la memoria.
- ⚠️ **Necesita OK:** escribir código, migraciones, commits, push, tocar datos.

## Costo

Un agente corriendo mucho consume tokens/crédito de API — 24/7 real es **caro**. Lo eficiente es **programarlo para tareas concretas** (ej. "de noche, X"), no dejarlo prendido sin parar.

## Recomendación

**Cola de tareas + rutinas programadas, en modo semi-autónomo:**
- El usuario deja tareas (en un archivo o en la DB, como una tabla `tareas`).
- El agente corre solo lo seguro y **pausa en las puertas** para aprobación.
- Se programan las de solo-lectura para que corran sin el usuario (ej. pruebas nocturnas).

Encaja con lo que ya hay: el orquestador pausa en las puertas; la memoria y el visor podrían mostrar el estado de las tareas.

## Posible construcción (pendiente, si se decide)

- Una **cola de tareas** (tabla o archivo) que el agente procese, con estado (pendiente / en curso / esperando OK / hecha).
- Una **vista en el visor** para asignar tareas y ver su estado.
- Una **rutina programada** para tareas de solo-lectura.
