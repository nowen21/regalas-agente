# Hecho · Validadores + hooks

Capa de **verificación mecánica** del estándar: scripts que comprueban lo comprobable y hooks que los disparan solos. Esta era la base del backlog; lo que faltó —los validadores que leen el código del proyecto— sigue abierto en [01 · Validadores de código de proyecto](../01-validadores-de-codigo-de-proyecto.md).

Cada entrada dice qué se cerró, cuándo y dónde quedó.

---

## Hooks · 2026-08-04

Activos y probados de punta a punta. No se solapan: cada uno cubre un momento.

- **Git `commit-msg`** → corre `commits.py`; bloquea el commit si el mensaje no cumple `G2`/`G8`.
- **Git `pre-commit`** → corre `versionado.py` sobre lo preparado (`G3`).
- **Claude Code `PostToolUse`** sobre `.md` → `hook_md.py`; revisa enlaces e índices al editar.
- **Claude Code `SessionStart`** → `hook_sesion.py`; gate `F13` + sincronía de `CLAUDE.md`.

Instalación en `validadores/instalar.py`; enganche en `.githooks/` y `.claude/settings.json`.

## Validadores · 2026-08-04/05

`validadores/*.py`, solo biblioteca estándar de Python, reportan sin arreglar.

| Validador | Regla | Comprueba |
|---|---|---|
| `enlaces.py` | — | enlaces `.md` rotos, índices desactualizados |
| `plantillas.py` | `16·CQ1` | marcadores sin llenar, secciones ausentes |
| `commits.py` | `G2`, `G8` | formato del mensaje, sin atribución de herramienta |
| `versionado.py` | `G3` | secretos/artefactos/config por **nombre** de archivo |
| `fases.py` | `F12.1–13` | jerarquía épica→HU→fase, nomenclatura, consecutivo sin huecos |
| `trazabilidad.py` | `DOC16`/`DOC12`/`DOC3`/`DOC11` | épica↔HU, ORIGEN en el plan, tabla de cierre |
| `secretos.py` | `S4`/`N6` | secretos incrustados en el **código** (probado vs agro-system) |
| `dependencias.py` | `DEP2` | lockfile presente y versionado (probado vs agro-system) |

**~22 reglas** con validador; **62 pruebas** verdes. Detalle regla por regla en [validadores/reglas-validables.md](../../validadores/reglas-validables.md).

## Lo que sigue abierto en el 01

Los **~38** validadores que necesitan un proyecto real más allá de su documentación: inspeccionar código/config o correr una herramienta instalada (linter, pruebas, audit de dependencias), más las **puertas de flujo** (`F2`: código de fase sin spec) y las **precondiciones de cierre**.
