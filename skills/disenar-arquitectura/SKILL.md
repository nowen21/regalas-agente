---
name: disenar-arquitectura
description: Define cómo se construye un módulo a partir de su spec aprobada: modelo de datos, servicios, dónde vive cada cosa y las decisiones técnicas con su porqué. Úsala entre la spec aprobada y el plan de tareas, o cuando el usuario pida "diseñá la arquitectura", "cómo lo estructuramos". Es el rol Designer. No escribe código.
---

# Diseñar arquitectura (rol Designer)

Traduce una **spec aprobada** en un **diseño técnico**: cómo se construye. Solo diseña; **no implementa**. Toma decisiones técnicas con criterio profesional y las **documenta con su porqué** (`13`·DOC2); escala al usuario solo lo que impacta UX, contrato de datos o alcance (`02`·F4.3).

## Procedimiento (en orden)

1. **Partir de la spec aprobada** (`02`·F2) y del contexto real (`02`·F1).
2. **Modelo de datos** (`03`): entidades, campos, relaciones y cardinalidad, restricciones (UNIQUE, FK con política de borrado), índices, auditoría. Valores configurables → catálogo, no hardcode (`03`·D4). Migración retrocompatible si hay datos (`03`·D3).
3. **Estructura y ubicación** (`14`): dónde vive cada elemento nuevo por módulo, con la nomenclatura del proyecto (capa 3: `mapeo-nombres.md`). Respetar el legacy: lo nuevo sigue la convención, lo viejo no se renombra (`14`·EST3).
4. **Seguridad y rendimiento por diseño** (`04`/`06`): dónde se verifica authz + scope, qué se pagina/indexa, qué va a segundo plano.
5. **Decisiones de diseño:** por cada elección no obvia (X en vez de Y), registrar el **porqué** como señal/decisión (`13`·DOC2). Considerar alternativas y descartarlas con razón.
6. **Presentar** el diseño para revisión antes de planificar las tareas.

## Salida

Un diseño técnico: modelo de datos, ubicación de artefactos, puntos de seguridad/rendimiento, y las decisiones con su porqué. Alimenta al Task Planner (`planificar-tareas`). No escribir código desde aquí.

Ver: `02`·F2 (spec previa), `03` (datos), `14` (estructura), `04`/`06` (seguridad/rendimiento), `13`·DOC2 (decisiones). Alimenta al Task Planner.
