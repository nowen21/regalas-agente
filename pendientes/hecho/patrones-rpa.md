# Pendiente · Patrón RPA (opt-in)

**Estado:** cerrado 2026-08-18 · anotado 2026-08-04.

| | |
|---|---|
| **Historia de usuario** | [EP-001 · HU-013 — Capítulos opt-in de dominio](../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-013-capitulos-opt-in-de-dominio/HU-013-capitulos-opt-in-de-dominio.md) — es un capítulo opt-in del cuerpo de reglas, como el 18 y el 19 que ya entraron |

Agregar soporte específico de **RPA** (Robotic Process Automation) como **patrón opt-in** (estilo `15`/`16`/`17`, con toggle en `CLAUDE.md.plantilla §5.1`). Hoy el estándar sirve para **desarrollar** un proyecto RPA como cualquier otro (flujo brief→épica→HU→spec→plan), pero **no trae conocimiento ni patrones propios de RPA**.

## Qué cubriría el patrón

- **Diseño de bots:** selectors/locators robustos, separación proceso ↔ elementos de UI, componibles/reutilizables.
- **Orquestación:** colas de trabajo (work queues), disparadores, orquestador, concurrencia de robots.
- **Resiliencia:** manejo de excepciones (de negocio vs de sistema), reintentos, recuperación, idempotencia del proceso.
- **Credenciales:** vault/almacén seguro (nunca en el bot), sesiones, permisos.
- **Datos:** entrada/salida, transaccionalidad por ítem de la cola, trazabilidad.
- **Pruebas de bots:** entornos que no tocan sistemas productivos reales, datos sintéticos, verificación manual de lo que el runtime no reproduce.
- **Gobernanza:** control de versiones de los procesos, despliegue a orquestador, monitoreo de ejecuciones.
- **Plantilla(s):** ficha de proceso a automatizar (PDD/SDD de RPA), mapa de excepciones.

## Principio que lo justifica

El agente **desarrolla** la solución RPA (código/config/docs del bot) — todo expresable como artefacto. **Fuera de alcance por diseño:** el agente **no ejecuta** RPA (no maneja mouse/teclado ni recorre UIs como robot); eso lo hace el **runtime de RPA** (UiPath, Automation Anywhere, Power Automate, Blue Prism, etc.). El stack RPA concreto se declara en `.agente/stack.md`.

## Relación con otros pendientes

Comparte espíritu con los [07 · patrones DevOps](patrones-devops.md) (18/19, ya hechos): son extensiones opt-in de dominio; el agente produce artefactos, no opera en vivo. Ninguno de los dos depende de los pendientes 01-06.


---

# Cómo cerró — 2026-08-18

**Nace el capítulo [`21 · Automatización de procesos`](../../base/21-automatizacion-de-procesos.md), opt-in, con ocho reglas.** El interruptor está en la plantilla del `CLAUDE.md`, junto a los del `15` al `19`, y arranca en `no` como todos.

| | Qué exige |
|---|---|
| `AU1` | lo que el proceso hace se separa de dónde lo hace |
| `AU2` | el elemento se alcanza por lo que es, no por dónde está |
| `AU3` | el trabajo se toma de una cola y cada ítem se cierra solo |
| `AU4` | el fallo del negocio y el del sistema no se tratan igual |
| `AU5` | el proceso no guarda con qué entra a ningún sistema |
| `AU6` | se prueba contra un entorno que no es el de verdad |
| `AU7` | cada proceso trae su ficha, y la ficha se mantiene |
| `AU8` | una corrida que no se mira no está terminada |

## El capítulo se llama distinto de lo que pedía este pendiente

**No dice «RPA» en ninguna parte, y es a propósito.** [`20·M3`](../../base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) no admite en la base el nombre de una tecnología ni de un producto, y este pendiente nombraba cuatro motores concretos. **La sigla también es de la industria**, y las siglas de industria envejecen: lo que no envejece es el problema.

**El problema, dicho sin sigla:** un proceso que corre solo contra sistemas que no se pueden cambiar ni avisar. **De ahí salen casi todas las ocho reglas** — si la pantalla se mueve el proceso se rompe, y nadie lo sabe hasta que alguien mira.

## Qué del pedido entró y qué no

**Entró todo lo que era exigencia.** Diseño, orquestación, resiliencia, credenciales, datos, pruebas y gobernanza están, una regla cada uno o repartidos.

**No entraron las plantillas** —la ficha del proceso, el mapa de excepciones—. `AU7` **exige** que la ficha exista y se mantenga; **qué campos lleva es del proyecto**, porque depende de qué sistemas toca y con qué entra. Un molde en la base sería adivinar.

## Las dos que más valen, y por qué

**`AU3` · la cola.** Es la que separa un proceso que se puede retomar de uno que hay que volver a lanzar entero. Extiende [`03·D6`](../../base/03-datos.md): acá **repetir es lo normal**, porque un corte a mitad de camino se retoma reprocesando lo que quedó abierto.

**`AU8` · mirar la corrida.** Es la que más se incumple, y por eso cierra el capítulo: un proceso automatizado se instala, funciona, y **se vuelve invisible**. Nadie mira lo que no falla ruidosamente, y así puede pasar meses apartando el noventa por ciento de los ítems sin que nadie se entere.

## El límite, que el pendiente ya tenía bien puesto

**El agente construye el proceso; no lo ejecuta.** Produce el diseño, la configuración, la ficha y las pruebas. Quien lo corre es el motor, y quién lo lanza en producción lo decide el humano. Eso quedó en la cabecera del capítulo, no como comentario.
