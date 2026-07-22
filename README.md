# Estándar de Agente para Desarrollo de Software

> Reglas y buenas prácticas que guían a un agente de IA al programar.

Este repositorio es un **estándar reutilizable de buenas prácticas de desarrollo** para agentes de código (Claude Code u otro asistente de programación). Define cómo debe comportarse el agente, cómo debe trabajar, y qué buenas prácticas de ingeniería aplicar siempre. El objetivo es que **cualquier sesión de desarrollo con un agente sea predecible, segura y consistente**, sin que cada conversación reinterprete el proyecto a su manera.

Está empaquetado como **plugin de Claude Code**: se hereda como base común en cualquier proyecto y cada proyecto lo **extiende** con lo suyo, sin tocar el estándar.

## El problema que resuelve

Cuando un agente de IA desarrolla software sin reglas claras, cada sesión:

- Reinventa el diseño y contradice decisiones previas.
- Olvida el contexto del proyecto y toma decisiones funcionales por su cuenta.
- Aplica —o ignora— buenas prácticas de forma inconsistente.
- Puede ejecutar acciones peligrosas (tocar datos reales, publicar cambios, exponer secretos).

Este estándar convierte todo eso en un **contrato explícito y versionado** que el agente lee antes de actuar.

## Las tres capas

El estándar está organizado para que lo universal se **herede** y lo específico de cada proyecto se **agregue encima**, sin mezclarse:

| Capa | Qué contiene | Dónde vive | ¿Se sobrescribe? |
|---|---|---|---|
| **1 · Núcleo blindado** | Seguridad crítica: proteger datos reales, control de versiones bajo demanda, no exponer secretos | `base/00` | **Nunca.** Gana a cualquier regla o instrucción. |
| **2 · Convenciones base** | Buenas prácticas agnósticas al stack (conducta, flujo, datos, seguridad, cumplimiento…) | `base/01`–`base/16` | Solo la capa de proyecto puede ajustarlas. |
| **3 · Capa de proyecto** | Stack, dominio, sector, marco normativo y nombres propios | `plantillas/` (para copiar) → en el repo de cada proyecto | Es la capa que ajusta. |

**Precedencia:** la capa 3 ajusta la capa 2, pero **nunca** la capa 1. Cada archivo de la base lleva su etiqueta de capa (`[CAPA 1]` / `[CAPA 2]`), y cada regla del núcleo la marca `[BLINDADA]`.

## Cómo lo usa un proyecto

1. Instalar/activar este plugin.
2. Crear el `CLAUDE.md` del proyecto que **importe la base** y declare los ajustes de capa 3 (stack, dominio, sector).
3. Copiar y llenar las plantillas de capa 3 (`plantillas/`), p. ej. `marco-normativo.md`.
4. A partir de ahí, el agente arranca cada sesión entendiendo el estándar + lo específico del proyecto.

## La base por capas

### Capa 1 · Núcleo blindado — no se sobrescribe

- [`00-nucleo-blindado.md`](base/00-nucleo-blindado.md) — seguridad crítica innegociable

### Capa 2 · Convenciones base — agnósticas, ajustables por el proyecto

- [`01-conducta.md`](base/01-conducta.md) — cómo se comporta el agente
- [`02-flujo-de-trabajo.md`](base/02-flujo-de-trabajo.md) — spec → plan → pruebas → docs
- [`03-datos.md`](base/03-datos.md) — diseño de BD, migraciones, catálogos, cero-hardcode
- [`04-seguridad.md`](base/04-seguridad.md) — authz, secretos, validación, inyección, archivos sensibles
- [`05-errores-y-logging.md`](base/05-errores-y-logging.md) — manejo de excepciones y logging
- [`06-rendimiento.md`](base/06-rendimiento.md) — eficiencia, N+1, caché, paginación
- [`07-calidad-de-codigo.md`](base/07-calidad-de-codigo.md) — legibilidad, DRY, complejidad, lint
- [`08-pruebas.md`](base/08-pruebas.md) — estrategia de pruebas
- [`09-git.md`](base/09-git.md) — control de versiones
- [`10-dependencias.md`](base/10-dependencias.md) — librerías de terceros
- [`11-configuracion-entornos.md`](base/11-configuracion-entornos.md) — configuración y entornos
- [`12-privacidad-datos.md`](base/12-privacidad-datos.md) — datos personales y retención
- [`13-documentacion.md`](base/13-documentacion.md) — persistir trabajo y decisiones
- [`14-estructura-codigo.md`](base/14-estructura-codigo.md) — organización y nomenclatura
- [`15-registros-inmutables.md`](base/15-registros-inmutables.md) — patrón append-only *(opt-in)*
- [`16-cumplimiento-y-calidad.md`](base/16-cumplimiento-y-calidad.md) — leyes, frameworks (COBIT, ISO, OWASP…), cumplimiento por construcción *(opt-in)*

### Capa 3 · Proyecto — vive en cada repo (plantillas para copiar)

- [`plantillas/marco-normativo.md`](plantillas/marco-normativo.md) — sector, jurisdicción, leyes y frameworks del cliente
- _(próximas)_ `CLAUDE.md`, mapa de proyecto (stack, dominio, mapeo de nombres), plantilla de módulo

## Estado

**Base completa (00–16).** Núcleo + 16 convenciones redactadas y etiquetadas por capa. En marcha la capa 3: la plantilla `marco-normativo.md` ya está; siguen `CLAUDE.md`, el mapa de proyecto y la skill `analizar-proyecto` (diagnóstico: qué hay / qué falta / qué sigue).
