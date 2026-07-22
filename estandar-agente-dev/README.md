# Estándar de Agente — Desarrollo de Software

Estándar reutilizable de buenas prácticas de desarrollo que un agente de código debe respetar en **cualquier** proyecto. Se hereda como base común y cada proyecto lo **extiende** con lo suyo, sin tocar el estándar.

## Las tres capas

| Capa | Qué contiene | Dónde vive | ¿Se sobrescribe? |
|---|---|---|---|
| **1 · Núcleo blindado** | Reglas de seguridad crítica | `base/00-nucleo-blindado.md` | **Nunca.** Gana a cualquier prompt o capa. |
| **2 · Convenciones base** | Buenas prácticas agnósticas al stack | `base/01..15-*.md` | Solo la capa de proyecto puede ajustarlas. |
| **3 · Capa de proyecto** | Stack, dominio, nombres concretos | `documentacion/proyecto/` de cada repo | Es la capa que ajusta. |

**Regla de precedencia:** capa 3 ajusta capa 2, pero **nunca** capa 1. Cada regla del núcleo lleva la marca `[BLINDADA]`.

## Cómo lo usa un proyecto

1. Instalar/activar este plugin.
2. Copiar `plantillas/CLAUDE.md.plantilla` → `CLAUDE.md` del proyecto.
3. Copiar `plantillas/proyecto/` → `documentacion/proyecto/` y rellenar el stack, el mapeo de nombres, el dominio y las convenciones de UI.
4. Copiar `plantillas/_base_modulo.md` → `documentacion/_base_modulo.md` y ajustarlo.

El `CLAUDE.md` del proyecto importa la base (`@`) y declara los ajustes de capa 3. A partir de ahí, el agente arranca cada sesión entendiendo el estándar + lo específico del proyecto.

## Índice de la base

- `00-nucleo-blindado.md` — seguridad crítica (Capa 1)
- `01-conducta.md` — cómo se comporta el agente
- `02-flujo-de-trabajo.md` — spec → plan → tests → docs
- `03-datos.md` — diseño de BD, migraciones, catálogos, cero-hardcode
- `04-seguridad.md` — authz, secretos, validación, inyección, archivos sensibles
- `05-errores-y-logging.md` — manejo de excepciones y logging
- `06-rendimiento.md` — eficiencia, N+1, caché, paginación
- `07-calidad-de-codigo.md` — legibilidad, DRY, complejidad, lint
- `08-pruebas.md` — estrategia de pruebas
- `09-git.md` — control de versiones
- `10-dependencias.md` — librerías de terceros
- `11-configuracion-entornos.md` — configuración y entornos
- `12-privacidad-datos.md` — datos personales y retención
- `13-documentacion.md` — persistir trabajo y decisiones
- `14-estructura-codigo.md` — organización y nomenclatura
- `15-registros-inmutables.md` — patrón append-only (opt-in)
