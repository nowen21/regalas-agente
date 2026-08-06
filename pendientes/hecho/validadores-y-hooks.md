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
| `flujo.py` | `F0` · `F4.1` · `F4.3` | padres de la fase; 13 preguntas del plan; sin incertidumbre |
| `plantillas.py` | `DOC1/DOC8/DOC10/DOC13/DOC15` | completitud de cada doc del proyecto contra su plantilla |

**Código del proyecto** — multiproyecto (universales o por detección de stack); probados contra agro-system con hallazgos reales:

| Validador | Regla | Comprueba |
|---|---|---|
| `secretos.py` | `S4`/`N6` | secretos incrustados en el código |
| `dependencias.py` | `DEP2` | lockfile presente y versionado |
| `rama.py` | `G4` | rama dedicada y al día con la principal |
| `migraciones.py` | `D2` | cada migración declara su reversión |
| `esquema.py` | `D1` (FK) · `D3` · `EST2` (longitud) | FK con política; `NOT NULL` nuevo sin default; identificador sobre el límite |
| `errores.py` | `E1` · `E5` | capturas de error vacías; secretos en logs |
| `rendimiento.py` | `R2` · `R1` | `SELECT *`; consulta en bucle (N+1) |
| `seguridad.py` | `S3` · `S5` | concatenación SQL/shell; asignación masiva; flags de cookie |
| `calidad.py` | `Q3` | funciones demasiado largas |
| `aislamiento.py` | `T4` · `T3` | BD efímera; orden aleatorio; fuentes flaky |
| `ci.py` | `G6` | existe pipeline de CI con pruebas y linter |
| `codigo.py` | — | base común: recorre el código fuente versionado |

**Corren la herramienta del stack** — a demanda, no en hook (dependen del toolchain, tardan, tienen efectos):

| Validador | Regla | Corre |
|---|---|---|
| `herramientas.py` · `linter` | `Q6` | pint/phpstan · eslint · ruff |
| `herramientas.py` · `suite` | `T5` | phpunit · npm test · pytest |
| `herramientas.py` · `audit` | `DEP3`/`S7` | composer/npm/pip audit |

(`DEP4` y `CFG2` los cubre `versionado.py`.) **~50 reglas** con validador; **137 pruebas** verdes. Detalle regla por regla en [validadores/reglas-validables.md](../../validadores/reglas-validables.md).

## Lo que sigue abierto en el 01

Quedan **~9** reglas. Cuatro son fuzzy o pesadas: `F2` (cruzar código de fase con su spec), `F4.4` (intervención→CA), `DOC7` (cruce narrativo A↔B), `DOC14`-formato (forzar texto=ruta marca todo link descriptivo). Cinco necesitan que el proyecto **declare** en `.agente/` su convención o dominio: `EST1`, resto de `EST2`, resto de `D1` (auditoría), `IM2`, `IM5`.
