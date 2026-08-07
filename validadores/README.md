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
| [flujo.py](flujo.py) | Cada fase tiene sus padres (épica/HU); el plan trae las 13 preguntas y sin incertidumbre | `02·F0/F4.1/F4.3` |
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
| [checklist.py](checklist.py) | El stack de instalación del agente: qué componentes le faltan al proyecto y si alguno quedó viejo | [`plantillas/stack-instalacion.md`](../plantillas/stack-instalacion.md) |

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
- **Los enlaces dentro de una transcripción de `historico-chat/`.** Las escribe el enganche copiando el chat **literal**, y en el chat los enlaces se escriben relativos a la raíz del proyecto, no a esa carpeta: se romperían por definición. Reescribirlos al copiar dejaría de ser literal, y el histórico vale por eso. El `README.md` de la carpeta sí se comprueba — ese lo escribe una persona.
- **Puertas del flujo** (código de fase sin spec + plan aprobado · `F2`) y la **trazabilidad hasta el commit**. Necesitan inspeccionar el código del proyecto, no solo su documentación; quedan para cuando haya un proyecto real bajo `proyectos/`. La trazabilidad **de la documentación** (épica↔HU, ORIGEN, tabla de cierre) sí está: `trazabilidad.py` — corre contra el árbol `documentacion/epicas/` de un proyecto.

## Enganche automático (hooks) — instalado

Los enganches están activos y probados de punta a punta. **No se solapan**: cada uno cubre un momento distinto.

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

**3. Claude Code — `UserPromptSubmit` y `Stop`.** Escriben el histórico de la sesión con [`hook_historico.py`](hook_historico.py): el primero anota el mensaje del usuario apenas lo envía, el segundo anota la respuesta del agente apenas termina, leyéndola del transcript. La hora sale del reloj de la máquina en ese instante.

Este es el único que **escribe** en vez de comprobar, y a propósito: la regla dice que toda sesión queda registrada, y mientras eso dependa de que el agente se acuerde, no se cumple siempre. Un `CLAUDE.md` informa; un enganche ejecuta.

- Cada archivo lleva `<!-- sesion: <id> -->` en la primera línea. La sesión se busca por esa marca, no por el nombre — así el archivo se puede renombrar para ponerle el tema real sin que se parta en dos.
- Los mensajes entran **antes** de `## Abierto`, no al final del archivo.
- Cada respuesta lleva `<!-- agente: <uuid> -->`, que evita que se duplique si el enganche vuelve a correr.
- No copia el razonamiento del agente ni la salida de herramientas: el histórico es la conversación.
- Un proyecto sin carpeta `historico-chat/` no se ve afectado — el enganche sale sin hacer nada.

**4. Claude Code — `UserPromptSubmit`.** [`hook_checklist.py`](hook_checklist.py) revisa el **stack de instalación** en cada mensaje: qué componentes le faltan al proyecto y si alguno quedó viejo.

La lista no vive en el código: está en [`plantillas/stack-instalacion.md`](../plantillas/stack-instalacion.md), que se copia a `.agente/` de cada proyecto. `checklist.py` solo aporta la comprobación de cada `id`, y una prueba exige que las dos listas coincidan — si se separan, el checklist mentiría por omisión.

- Mientras falte algo, escribe `.agente/INSTALACION-INCOMPLETA.md` con el detalle, se lo muestra al usuario y se lo pasa al agente para que lo diga.
- Cuando ya no falta nada, **borra** la marca y calla. Su ausencia es la señal de instalación completa; un aviso permanente se deja de leer.
- **No bloquea.** El único que detiene es el gate `02·F13`, y eso ya era así.
- La copia del stack en `.agente/` lleva la huella del original: si el estándar agrega un componente, la huella deja de coincidir y se reporta como actualización pendiente.

A mano: `python validadores/validar.py checklist --raiz "<proyecto>"`.

**Se replica solo.** Los cuatro enganches, la carpeta `historico-chat/` y la copia del stack los instala [`instalar.py`](instalar.py) en cualquier proyecto, y el paso 6 de [`CLAUDE.md.plantilla`](../plantillas/CLAUDE.md.plantilla) lo corre en cada sesión. Una herramienta nueva del estándar se agrega a `HOOKS_CLAUDE` (y al stack, si el proyecto tiene que tener algo) y llega sola a todos los proyectos: si exige configurarla a mano, está mal hecha.

## Regla de oro

**Nada se comprueba aquí que no esté escrito en la norma.**

Si aparece la necesidad de exigir algo nuevo, el orden es: **primero se escribe en `base/`**, después se comprueba. Al revés, un validador bloquea trabajo por un motivo que nadie puede consultar.

Ya pasó una vez: la prohibición de `Co-Authored-By` estuvo en el código antes que en la norma. Se corrigió escribiéndola en [`base/09-git.md`](../base/09-git.md) · **G8**.
