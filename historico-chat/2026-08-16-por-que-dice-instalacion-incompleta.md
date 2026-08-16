<!-- sesion: f611da36-ba9e-4c6d-bd01-da7f248cc014 -->
<!-- nombre: preguntado -->

# 2026-08-16 — Por que dice instalacion incompleta

## Conversación

### 1 · Usuario — 2026-08-16 14:42:03
> me salió este mensaje: "Instalación incompleta · 10 de 13 — claude-md, stack-instalacion y recuerdos" en un proyecto. Explique por qué?

**Agente** — 2026-08-16 14:45:06
<!-- agente: fee5dff8-64db-4f4a-a569-384b39414863 -->

**No le falta nada al proyecto: tiene las copias viejas.**

El aviso lo escribe [hook_checklist.py](validadores/hook_checklist.py) en cada mensaje, corriendo [checklist.py](validadores/checklist.py) sobre 13 componentes. Tres de ellos llevan un **sello de huella** que compara la copia del proyecto contra la plantilla del estándar ([versiones.py:78-98](validadores/versiones.py#L78-L98)):

| Componente | Copia en el proyecto | Plantilla central |
|---|---|---|
| `claude-md` | `CLAUDE.md` | `plantillas/CLAUDE.md.plantilla` |
| `stack-instalacion` | `.agente/stack-instalacion.md` | `plantillas/stack-instalacion.md` |
| `recuerdos` | `historico-chat/memory/memory.md` | `plantillas/memoria.md` |

La versión [`20.0.1`](CHANGELOG.md) cambió los 91 enlaces de las plantillas (`../base/…` → `«RUTA-ESTANDAR»/base/…`). Eso cambió el contenido, y con él la huella. Los sellos del proyecto quedaron apuntando a la anterior:

```
claude-md          448fee3ff1ab → a5ceeb693286   viejo
stack-instalacion  6cb6be770748 → ed454ca0ae7d   viejo
historico          2a3060c58acb = 2a3060c58acb   al día   ← su plantilla no se tocó
recuerdos          284610f2cee3 → 83db0387a355   viejo
```

Por eso son exactamente esos tres y no otros: son los únicos sellados cuya plantilla cambió en el parche.

**Cuál proyecto es.** Corrí el checklist sobre los ocho registrados en `plantillas/proyectos.md`. El de 10 de 13 con esos tres es **`dp`** (`C:\DesarrollosClaude\dp`). Siete de los ocho están en rojo por lo mismo; `agro-system`, `gestion de servicios tecnologicos` y `dp_card` suman además `enganches-claude`. El único en 13 de 13 es `shopnest-mesa`, que se reinstaló después del parche.

**Se arregla reinstalando** — el `CHANGELOG` de 20.0.1 ya lo pide:

```sh
python "c:/Ing. Jose/ia/agente/validadores/instalar.py" "C:/DesarrollosClaude/dp" --aplicar
```

No pisa lo escrito: en `CLAUDE.md` y en `memory.md` solo llena marcadores, agrega secciones nuevas al final y refresca el sello; `stack-instalacion.md` sí se reescribe entero porque es copia literal.

**Dos cosas que vale la pena que sepa, y las dejé escritas en el resumen de la sesión:**

1. La línea que usted vio dice **«falta»** cuando lo correcto es «quedó viejo». [checklist.py:308](validadores/checklist.py#L308) usa la misma palabra para los tres casos que el propio módulo separa a propósito. El detalle largo sí lo distingue; la línea de pantalla, no.
2. `20.0.1` se versionó como PARCHE —«no cambia qué se exige»— pero obliga a reinstalar los ocho proyectos y, hasta que se haga, todos avisan «incompleto» en cada mensaje. Es justamente el aviso-que-siempre-suena que ese parche decía estar arreglando.

¿Reinstalo `dp`, o los siete de una vez? ¿Y abro pendiente por la palabra «falta»?

### 2 · Usuario — 2026-08-16 14:48:02
> Aplique la regla: 00·ID9 para darme la respuesta

**Agente** — 2026-08-16 14:48:14
<!-- agente: d2367906-a87f-4306-afe8-7acdb8efa3cb -->

No le falta nada al proyecto: tiene copias viejas. El parche [20.0.1](CHANGELOG.md) cambió los enlaces de las plantillas, y con ellos la huella de las tres que llevan sello: `CLAUDE.md`, `.agente/stack-instalacion.md` y `historico-chat/memory/memory.md`.

El proyecto es `dp`. Se arregla reinstalando —no pisa lo escrito—:

```sh
python "c:/Ing. Jose/ia/agente/validadores/instalar.py" "C:/DesarrollosClaude/dp" --aplicar
```

Siete de los ocho proyectos registrados están igual. El detalle y los dos defectos que salieron de esto están en [sesion-4.md](historico-chat/resumenes/2026-08-16/sesion-4.md).

¿Reinstalo los siete? ¿Abro pendiente porque el aviso dice «falta» en vez de «desactualizado»?

### 3 · Usuario — 2026-08-16 14:49:51
> no entiendo por qué sale el mansaje, no se supone que el proyecto debe detectar la nueva versión e instalar?

**Agente** — 2026-08-16 14:50:10
<!-- agente: 2c9e7d17-36f8-4209-9d85-ff0f06680631 -->

Sí lo detectó — el mensaje **es** la detección. Lo que no hace es instalar solo, y eso es a propósito.

Reinstalar reescribe archivos del proyecto (`CLAUDE.md`, `memory.md`, `.agente/`). El enganche corre en **cada mensaje** suyo: si instalara solo, tocaría el repositorio sin que nadie lo apruebe, y usted vería cambios que no pidió. Por eso el estándar separa las dos cosas ([checklist.py:15-19](validadores/checklist.py#L15-L19)): detectar es automático, adoptar es decisión suya. Es la misma regla de retroactividad del [CHANGELOG](CHANGELOG.md) — «el aviso de desfase informa, no migra solo».

El aviso se queda hasta que usted corra el instalador.

¿Lo corro en `dp`, o en los siete?

### 4 · Usuario — 2026-08-16 14:52:37
> si ya entendí

**Agente** — 2026-08-16 14:52:44
<!-- agente: 765907aa-a404-4155-8b05-4e6e31dbab08 -->

Listo. Dos cosas cortas antes de cerrar:

Esta sesión la guardo como `2026-08-16-por-que-dice-instalacion-incompleta.md` — por qué el checklist marca «falta» cuando lo que hay son copias viejas del estándar, ¿va? Si aprueba, también péguele `/rename por-que-dice-instalacion-incompleta`.

Y queda pendiente decidir: reinstalar los siete proyectos, y si abro pendiente por la palabra «falta».

### 5 · Usuario — 2026-08-16 14:53:40
> si: 2026-08-16-por-que-dice-instalacion-incompleta.md
> /rename por-que-dice-instalacion-incompleta

**Agente** — 2026-08-16 14:54:29
<!-- agente: 30acc06b-19de-406f-afd8-13772ff572f3 -->

Renombrada: [2026-08-16-por-que-dice-instalacion-incompleta.md](historico-chat/2026-08-16-por-que-dice-instalacion-incompleta.md), índice al día. El resumen también.

Al renombrar volvió a pasar el [pendiente 35](pendientes/35-renombrar-una-sesion-deja-roto-el-enlace-de-su-resumen.md): el enlace interno del resumen quedó apuntando al nombre viejo. Lo corregí a mano y lo dejé escrito como H-2 — es la segunda vez en el mismo día.

La sesión **no cierra todavía**: faltan sus dos decisiones (reinstalar los siete proyectos, y si abro pendiente por la palabra «falta») y el commit.

### 6 · Usuario — 2026-08-16 15:04:39
> esta sesión se puede cerrar?

**Agente** — 2026-08-16 15:04:44
<!-- agente: b7035f8d-b93e-4dd7-aaad-6deb6db2ffd7 -->

No.

Faltan dos de las cuatro casillas en [el resumen](historico-chat/resumenes/2026-08-16/por-que-dice-instalacion-incompleta.md):

- **Hallazgo abierto sin pendiente** — H-1 dejó dos decisiones suyas: reinstalar los siete proyectos desactualizados, y si se abre pendiente porque el aviso dice «falta» en vez de «desactualizado».
- **Sin commit** — el resumen está escrito pero no guardado.

Con eso resuelto, cierra. ¿Le abro el pendiente y reinstalo?

### 7 · Usuario — 2026-08-16 15:05:33
> cada proyecto lo instala: Hallazgo abierto sin pendiente de hecho estoy en dos y ya detectaron los cambios

### 8 · Usuario — 2026-08-16 15:06:28
> Hallazgo abierto sin pendiente: cada proyecto lo instala, de hecho estoy en dos y ya detectaron los cambios

**Agente** — 2026-08-16 15:06:51
<!-- agente: eee89747-4319-4eac-abac-cace6543c0da -->

Anotado: reinstalar no es trabajo de este repositorio, cada proyecto lo corre en su sesión — y el aviso hizo justo lo suyo, dos ya lo detectaron. Esa casilla queda marcada.

Queda una sola cosa antes de cerrar: **el commit** del resumen y del renombrado. ¿Lo hago?

(Y si quiere, en el mismo commit abro el pendiente por la palabra «falta» — o lo dejamos así.)

### 9 · Usuario — 2026-08-16 15:07:54
> no entiendo de cuál palabra: "falta" habla

**Agente** — 2026-08-16 15:08:02
<!-- agente: ce24940d-fe35-4cd3-9554-0b6e68e67304 -->

La del mensaje que le salió:

```
INSTALACIÓN INCOMPLETA · dp · 10 de 13 · falta: claude-md, stack-instalacion, recuerdos
                                         ─────
```

Esa palabra dice que los archivos **no están**. Y sí están: lo que tienen es la copia vieja. Por eso su primera pregunta fue «¿por qué sale este mensaje?» — la línea le dio la idea equivocada.

La escribe [checklist.py:308](validadores/checklist.py#L308). El detalle largo sí lo dice bien («quedó viejo: la plantilla cambió en el estándar»); la línea corta, no.

El pendiente sería: que diga `desactualizado:` cuando el componente está pero viejo, y `falta:` solo cuando de verdad no está. ¿Lo abro?

### 10 · Usuario — 2026-08-16 15:08:28
> eso no tiene nada que ver para que se enfrasque en eso

**Agente** — 2026-08-16 15:08:39
<!-- agente: fde0e6b9-3df0-4069-a834-42ad95915d67 -->

Descartado, no lo abro.

Queda solo el commit del resumen y del renombrado. ¿Lo hago?

### 11 · Usuario — 2026-08-16 15:09:06
> osea eso ya lo tenía como un pendiente?

**Agente** — 2026-08-16 15:09:18
<!-- agente: e7b3868f-3d47-4b19-906a-45d11b14dfe0 -->

No. No existía como pendiente: fue una propuesta mía de esta sesión, no algo que ya estuviera anotado.

Lo más parecido en el backlog es el [pendiente 30](pendientes/30-el-checklist-no-ve-la-cadena.md), pero es otra cosa — ahí el reclamo es que el checklist **no dice** que falta el planteamiento; acá era que dice «falta» de más.

Queda registrado como descartado en el resumen, y no se abre nada.

### 12 · Usuario — 2026-08-16 15:09:29
> listo suba

**Agente** — 2026-08-16 15:11:31
<!-- agente: a7bebb97-5640-497b-a120-9b0eba854894 -->

Subido: commit `c2ded0e`, publicado en `main`.

Van la transcripción, el resumen y su línea en el índice del día. Dejé fuera lo de la sesión 5 y de la sesión de pendientes, que son de otras sesiones.

Con eso la sesión **cierra**: las cuatro casillas quedaron marcadas. Falta un último commit menor con esa marca, si quiere que lo haga.

### 13 · Usuario — 2026-08-16 15:11:57
> cierro?

**Agente** — 2026-08-16 15:12:04
<!-- agente: 1379f713-68f9-4e75-8703-347f3179f5e0 -->

Sí, cierra: las cuatro casillas están marcadas.

Queda una línea sin guardar — la casilla que dice que ya está commiteado. ¿La subo y con eso terminamos?
