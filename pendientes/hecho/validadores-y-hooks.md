# Hecho · Validadores + hooks

Capa de **verificación mecánica** del estándar: scripts que comprueban lo comprobable y hooks que los disparan solos. Cubre los hooks, los validadores de documentación/estructura y buena parte de los que leen el **código del proyecto**. Lo que queda —más validadores de código— sigue abierto en [01 · Validadores de código de proyecto](../01-validadores-de-codigo-de-proyecto.md).

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

**Documentación y estructura** — corren sobre las carpetas y el markdown:

| Validador | Regla | Comprueba |
|---|---|---|
| `enlaces.py` | — | enlaces `.md` rotos, índices desactualizados |
| `plantillas.py` | `16·CQ1` | marcadores sin llenar, secciones ausentes |
| `commits.py` | `G2`, `G8` | formato del mensaje, sin atribución de herramienta |
| `versionado.py` | `G3` | secretos/artefactos/config por **nombre** de archivo |
| `fases.py` | `F12.1–13` | jerarquía épica→HU→fase, nomenclatura, consecutivo |
| `trazabilidad.py` | `DOC16/DOC12/DOC3/DOC11` | épica↔HU, ORIGEN, tabla de cierre |

**Código del proyecto** — multiproyecto (universales o por detección de stack); probados contra agro-system con hallazgos reales:

| Validador | Regla | Comprueba |
|---|---|---|
| `secretos.py` | `S4`/`N6` | secretos incrustados en el código |
| `dependencias.py` | `DEP2` | lockfile presente y versionado |
| `rama.py` | `G4` | rama dedicada y al día con la principal |
| `migraciones.py` | `D2` | cada migración declara su reversión |
| `esquema.py` | `D1` (FK) | clave foránea con política de borrado |
| `errores.py` | `E1` | capturas de error vacías |
| `rendimiento.py` | `R2` | `SELECT *` |
| `codigo.py` | — | base común: recorre el código fuente versionado |

**Corren la herramienta del stack** — a demanda, no en hook (dependen del toolchain, tardan, tienen efectos):

| Validador | Regla | Corre |
|---|---|---|
| `herramientas.py` · `linter` | `Q6` | pint/phpstan · eslint · ruff |
| `herramientas.py` · `suite` | `T5` | phpunit · npm test · pytest |
| `herramientas.py` · `audit` | `DEP3`/`S7` | composer/npm/pip audit |

**~30 reglas** con validador; **95 pruebas** verdes. Detalle regla por regla en [validadores/reglas-validables.md](../../validadores/reglas-validables.md).

## Lo que sigue abierto en el 01

Las **~29** reglas restantes son del mismo tipo (leen código/config del proyecto): entre otras `NOT NULL` sin default (`D3`), concatenación en SQL/shell (`S3`), secretos en logs (`E5`), N+1 (`R1`), complejidad de función (`Q3`), ubicación/nombres de módulos (`EST1`/`EST2`)… más las **puertas de flujo** (`F2`: código de fase sin spec) y las **precondiciones de cierre**.
