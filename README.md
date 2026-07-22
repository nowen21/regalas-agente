# Estándar de Agente para Desarrollo de Software

> Reglas y buenas prácticas que guían a un agente de IA al programar.

**Un estándar de buenas prácticas de desarrollo de software para agentes de código.**

Este repositorio define las reglas que un agente de IA (Claude Code u otro asistente de programación) debe respetar al desarrollar software: cómo comportarse, cómo trabajar, y qué buenas prácticas de ingeniería aplicar siempre. El objetivo es que **cualquier sesión de desarrollo con un agente sea predecible, segura y consistente**, sin que cada conversación reinterprete el proyecto a su manera.

## El problema que resuelve

Cuando un agente de IA desarrolla software sin reglas claras, cada sesión:

- Reinventa el diseño y contradice decisiones previas.
- Olvida el contexto del proyecto y toma decisiones funcionales por su cuenta.
- Aplica —o ignora— buenas prácticas de forma inconsistente.
- Puede ejecutar acciones peligrosas (tocar datos reales, publicar cambios, exponer secretos).

Este estándar convierte todo eso en un **contrato explícito y versionado** que el agente lee antes de actuar.

## Qué contiene el repositorio

| Carpeta | Qué es |
|---|---|
| [`estandar-agente-dev/`](estandar-agente-dev/) | **El estándar reutilizable.** Reglas agnósticas al stack, empaquetadas como plugin para heredar en cualquier proyecto y extender con lo propio. Es el corazón del repo. |

## El estándar en tres capas

El estándar (`estandar-agente-dev/`) está organizado para que lo universal se **herede** y lo específico de cada proyecto se **agregue encima**, sin mezclarse:

| Capa | Qué contiene | ¿Se sobrescribe? |
|---|---|---|
| **1 · Núcleo blindado** | Reglas de seguridad crítica (proteger datos reales, control de versiones bajo demanda, no exponer secretos) | **Nunca.** Gana a cualquier regla o instrucción. |
| **2 · Convenciones base** | Buenas prácticas agnósticas: conducta, flujo de trabajo, datos, seguridad, errores, rendimiento, pruebas, git, dependencias, documentación… | Solo la capa de proyecto puede ajustarlas. |
| **3 · Capa de proyecto** | Stack concreto, dominio del negocio, nombres y convenciones propias | Es la capa que ajusta. |

**Precedencia:** la capa 3 ajusta la capa 2, pero **nunca** la capa 1.

## Estado

En construcción. La base de comportamiento (núcleo, conducta y flujo de trabajo) ya está redactada; el resto de las convenciones (datos, seguridad, errores, rendimiento, calidad, pruebas, git, dependencias, entornos, privacidad, documentación, estructura) está en desarrollo. Ver [`estandar-agente-dev/README.md`](estandar-agente-dev/README.md) para el detalle y el índice completo.
