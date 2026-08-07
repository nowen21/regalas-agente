# 2026-08-06 — Se crea el histórico de sesiones (sesión 1)

> Transcripción del diálogo. Las horas de esta sesión no se registraron y no se inventan.
> El trabajo de despliegue/observabilidad (`base/18`, `base/19`) es anterior a esta sesión y a la regla del histórico: no hay transcripción de él, solo el inventario de archivos que quedó al final.

## Conversación

### 1 · Usuario — hora no registrada
> cree una carpeta: historico-chat para que ahí se gurade todo lo que se va haciendo encada una de las sesiones y eso debe quedar en memory

**Agente** — hora no registrada

*(Crea `historico-chat/README.md`, `historico-chat/2026-08-06-historico-chat.md`, la memoria `historico-chat.md` y la línea en `MEMORY.md`.)*

Listo.

**En el repo:**

- `historico-chat/README.md` — la regla: un archivo por sesión, `AAAA-MM-DD-tema.md`, con plantilla (qué se pidió / qué se hizo / decisiones / abierto) e índice.
- `historico-chat/2026-08-06-historico-chat.md` — entrada de hoy: la creación de la carpeta y el trabajo de despliegue/observabilidad que está sin commitear.

**En memoria:** `historico-chat.md` + línea en `MEMORY.md`, para que en cada sesión futura escriba la entrada aquí.

Decisión que tomé: la bitácora vive en el repo (se ve en git), la memoria solo guarda la regla. Sin commit, esperando tu visto bueno.

## Estado del repo al crear la carpeta

Trabajo hecho antes de esta sesión, sin commitear:

- `base/18-despliegue-e-infraestructura.md` y `base/19-observabilidad-y-operacion.md` → nuevas reglas del estándar.
- `plantillas/checklist-despliegue.md` y `plantillas/postmortem.md` → plantillas de apoyo.
- `pendientes/07-patrones-devops.md` → movido a `pendientes/hecho/patrones-devops.md`.
- `plantillas/base-proyecto.md` → movido a `base/02-flujo-de-trabajo/F13/estructura-base.md`.
- Ajustes en `README.md`, `CHANGELOG.md`, `VERSION`, `base/02-flujo-de-trabajo.md` (y F12/F13), `plantillas/CLAUDE.md.plantilla`, `pendientes/08-patrones-rpa.md`, `pendientes/README.md`.

## Decisiones

- La bitácora va en el repo, no en la memoria del agente. La memoria solo guarda la regla ("escribe aquí"); el contenido histórico es del proyecto y debe verse en git.
- Carpeta aparte de `notas/`: `notas/` explica diseño y decisiones vivas; `historico-chat/` es cronológico y no se reescribe.

## Abierto

- Falta commitear el trabajo de despliegue/observabilidad (pendiente de aprobación del usuario).
- `pendientes/08-patrones-rpa.md` sigue abierto.
