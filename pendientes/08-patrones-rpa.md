# Pendiente · Patrón RPA (opt-in)

**Estado:** abierto · anotado 2026-08-04.

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

Comparte espíritu con los [07 · patrones DevOps](07-patrones-devops.md) (18/19): son extensiones opt-in de dominio; el agente produce artefactos, no opera en vivo. Ninguno de los dos depende de los pendientes 01–06 — si un proyecto los necesita, se adelantan.
