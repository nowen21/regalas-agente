# Validadores del estándar

Comprueban **lo que se puede comprobar sin criterio**. Cierran la brecha entre "el estándar dice" y "el estándar se cumple" — pendiente [01](../pendientes/01-validadores-de-codigo-de-proyecto.md).

Solo biblioteca estándar de Python 3.11+. Sin dependencias, sin instalación.

## El principio

> Si dos personas pueden discutir si se cumplió → se queda en el `.md`.
> Si un script puede decir sí/no sin opinar → validador.

**La norma no se duplica aquí.** El validador de plantillas abre `plantillas/X.md` y compara; si la plantilla cambia, el validador cambia con ella sin tocar código. Los validadores **reportan, no arreglan**.

## Dos severidades

| | Significado | ¿Rompe? |
|---|---|---|
| `FALLA` | Incumplimiento claro, sin ambigüedad. | Sí — código de salida 1 |
| `AVISO` | Algo que un humano debe mirar. | No — código de salida 0 |

La distinción no es cosmética. Las plantillas dicen *"elimine las secciones que no apliquen"*, así que una sección ausente **no** es un incumplimiento: es un `AVISO`. Un validador que grita por todo se termina ignorando.

## Uso

```sh
# Coherencia de este repositorio: enlaces rotos e índices desactualizados
python validadores/validar.py estandar

# Un documento contra su plantilla (la deduce del ID: HU-014 -> plantillas/HU.md)
python validadores/validar.py plantilla proyectos/pos/HU-014.md
python validadores/validar.py plantilla doc.md --contra plantillas/epica.md

# Mensaje de commit
python validadores/validar.py commit                          # HEAD
python validadores/validar.py commit --archivo .git/COMMIT_EDITMSG

# Suite
python validadores/pruebas.py
```

## Qué comprueba cada uno

| Archivo | Comprueba | Contra |
|---|---|---|
| [enlaces.py](enlaces.py) | Enlaces `.md` rotos; índices que no listan todos sus archivos | El disco |
| [plantillas.py](plantillas.py) | Marcadores sin llenar, notas de plantilla sin borrar, secciones ausentes | `plantillas/*.md` |
| [commits.py](commits.py) | Asunto con contenido, línea en blanco antes del cuerpo, rastros de herramienta | [`base/09-git.md`](../base/09-git.md) · G2 |
| [fases.py](fases.py) | Jerarquía y nomenclatura épica→HU→fase; consecutivo sin huecos; los 4 documentos | `02·F12` (`F12.1/2/3/4/5/6/7/11/12/13`) |
| [trazabilidad.py](trazabilidad.py) | Enlace bidireccional épica↔HU; ORIGEN en el plan; tabla de cierre | `13·DOC16/DOC12/DOC3/DOC11` |
| [flujo.py](flujo.py) | El plan de trabajo trae las 13 preguntas y no deja marcas de incertidumbre | `02·F4.1/F4.3` |
| [versionado.py](versionado.py) | Secretos/artefactos/config local versionados (por **nombre** de archivo) | `base/09-git.md` · G3 |
| [secretos.py](secretos.py) | Secretos **incrustados en el código** (claves AWS, tokens, `password = "…"`) | `base/04·S4` · `00·N6` |
| [dependencias.py](dependencias.py) | Lockfile del ecosistema presente y versionado | `base/10·DEP2` |
| [rama.py](rama.py) | Trabajo en rama dedicada (no la principal) y al día con ella | `base/09-git.md` · G4 |
| [migraciones.py](migraciones.py) | Cada migración declara su reversión (multi-stack: Laravel/Django/Alembic/Rails/Node/SQL) | `base/03·D2` |
| [esquema.py](esquema.py) | FK con política de borrado; `NOT NULL` nuevo sin default; longitud de identificador | `base/03·D1/D3` · `14·EST2` |
| [errores.py](errores.py) | Capturas de error vacías; secretos en llamadas de log | `base/05·E1/E5` |
| [rendimiento.py](rendimiento.py) | `SELECT *`; consulta ejecutada dentro de un bucle (N+1) | `base/06·R2/R1` |
| [seguridad.py](seguridad.py) | Concatenación SQL/shell; asignación masiva; flags de cookie de sesión | `base/04·S3/S5` |
| [calidad.py](calidad.py) | Funciones demasiado largas | `base/07·Q3` |
| [aislamiento.py](aislamiento.py) | Pruebas contra BD efímera; orden aleatorio; fuentes flaky | `base/08·T4/T3` |
| [ci.py](ci.py) | Existe un pipeline de CI que corre pruebas y linter | `base/09·G6` |

### Validadores que corren una herramienta (a demanda)

Categoría aparte, en [herramientas.py](herramientas.py). No leen archivos: **invocan la herramienta del ecosistema** y traducen su salida. Detectan el stack por el manifiesto (`composer.json`, `package.json`…) y corren en su carpeta.

| Subcomando | Corre | Regla |
|---|---|---|
| `linter` | pint/phpstan · eslint/prettier · ruff/flake8 | `07·Q6` |
| `suite` | phpunit · npm test · pytest | `08·T5` |
| `audit` | composer/npm/pip audit | `10·DEP3` |

**No van en el hook automático**: dependen del toolchain instalado, tardan y tienen efectos (`suite` toca la BD, `audit` va a la red). Se corren a demanda. Si no encuentran la herramienta, avisan; no inventan.

### Lo que deliberadamente NO comprueba

- **Enlaces a código de proyecto** (`app/PagoService.php`). Ese código no vive en este repositorio por diseño; exigir que exista sería exigir que el estándar contenga los proyectos que lo usan.
- **Ejemplos de formato** (`[<ruta legible>](<path-relativo>.md)`). Llevan `<>` y son documentación, no enlaces.
- **Anclas** (`archivo.md#seccion`). Se comprueba el archivo, no la sección.
- **Puertas del flujo** (código de fase sin spec + plan aprobado · `F2`) y la **trazabilidad hasta el commit**. Necesitan inspeccionar el código del proyecto, no solo su documentación; quedan para cuando haya un proyecto real bajo `proyectos/`. La trazabilidad **de la documentación** (épica↔HU, ORIGEN, tabla de cierre) sí está: `trazabilidad.py` — corre contra el árbol `documentacion/epicas/` de un proyecto.

## Enganche automático (hooks) — instalado

Los dos enganches están activos y probados de punta a punta. **No se solapan**: cada uno cubre un momento distinto.

**1. Git — [`.githooks/commit-msg`](../.githooks/commit-msg).** Revisa el mensaje antes de aceptar el commit. Si incumple, el commit **no se crea**.

Aplica a **todo** commit del repositorio, venga de una persona o del agente — por eso no hace falta un hook aparte en Claude Code para lo mismo.

```sh
git config core.hooksPath .githooks     # activar
git config --unset core.hooksPath       # desactivar
```

> Va en `.githooks/` y no en `.git/hooks/` porque **`.git/hooks/` no se versiona**. Así el hook viaja con el repo; cada clon nuevo solo necesita correr el `git config` de arriba una vez (y `chmod +x .githooks/commit-msg` en Unix).

**2. Claude Code — `PostToolUse` sobre `Write|Edit`.** Tras editar un `.md`, corre [`hook_md.py`](hook_md.py), que comprueba enlaces e índices. Si la edición rompió algo, devuelve el detalle al agente para que lo corrija en el momento, sin esperar al commit. Configurado en [`.claude/settings.json`](../.claude/settings.json).

Ignora en silencio lo que no le toca: archivos que no son `.md`, y `.md` fuera de este repositorio.

> Usa Python y no `jq` a propósito: en esta máquina no hay `jq`, y así el hook no depende de qué trae instalado cada equipo.

## Regla de oro

**Nada se comprueba aquí que no esté escrito en la norma.**

Si aparece la necesidad de exigir algo nuevo, el orden es: **primero se escribe en `base/`**, después se comprueba. Al revés, un validador bloquea trabajo por un motivo que nadie puede consultar.

Ya pasó una vez: la prohibición de `Co-Authored-By` estuvo en el código antes que en la norma. Se corrigió escribiéndola en [`base/09-git.md`](../base/09-git.md) · **G8**.
