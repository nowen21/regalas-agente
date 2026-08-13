<!-- sesion: 3243b9dc-d78c-4ff8-9b56-a128b68f4b99 -->
<!-- nombre: preguntado -->

# 2026-08-12 — Regla de respaldo de las reglas de proyecto

## Conversación

### 1 · Usuario — 2026-08-12 22:19:19
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\prompts\regla-reglas-proyecto.md in the IDE. This may or may not be related to the current task.</ide_opened_file>
> revisa prompts y deme un ejemplo de cómo quedaria la regla y cómo se haría en reglas-proyecto de cada proyecto

**Agente** — 2026-08-12 22:21:17
<!-- agente: 86161b23-1d76-4db9-8de2-df4b89e9a67a -->

I'll look at the `prompts/` folder first.

Revisé [prompts/regla-reglas-proyecto.md](prompts/regla-reglas-proyecto.md). Es una meta-regla (habla de cómo son las reglas, no de qué hacer), así que va al capítulo 20 con el prefijo `M`, y el ID libre siguiente es `M16`.

**Un aviso antes del ejemplo:** tal como está redactada en el prompt puede trancarse. Una regla de proyecto suele ser específica de stack (`/ordenes-de-compra` en kebab-case), y eso nunca puede subir a `base/` porque `M3` la exige agnóstica. La salida es que el respaldo sea del **criterio**, no del detalle: la base fija el criterio agnóstico y la `P` le pone el valor concreto del proyecto. Con esa lectura la regla funciona; sin ella, obliga a meter stack en `base/`. El ejemplo va escrito así.

## 1 · La regla del estándar

Archivo: `base/20-meta-reglas/reglas/M16-ninguna-regla-de-proyecto-existe-sin-una-regla-de-base-que-la-respalde.md`

```markdown
> Regla del capítulo [`20 · Meta-reglas`](../base.md).

## M16 · Ninguna regla de proyecto existe sin una regla de base que la respalde

Cada regla `P` del catálogo de un proyecto declara la regla de `base/` cuyo criterio
concreta o endurece (extiende 20·M13). Si ningún criterio de `base/` la cubre, primero
se crea allí la regla —agnóstica (M3) y por el procedimiento completo (M14)— y solo
después se escribe la `P`.

```
INCORRECTO: P4 · Los reintentos son 3 · Por qué: lo acordó el equipo
CORRECTO:   P4 · Los reintentos son 3 · Respaldo: 05·E3 — fija el número para este proyecto
```
```

Y su bloque `### Checklist · CUMPLE` al final, como el de [M13](base/20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md).

## 2 · Cómo queda en `reglas-proyecto` de cada proyecto

El campo **Relación con la base** de la plantilla pasa a llamarse **Respaldo** y deja de ser opcional:

```markdown
### P3 · Las rutas HTTP van en kebab-case y en plural

- **Regla:** toda ruta nueva se nombra en kebab-case y en plural: `/ordenes-de-compra`.
- **Respaldo:** [`07·Q2 · Nombres que dicen la intención`](...) — concreta ese criterio
  con la convención de nombres de este proyecto (`20·M16`).
- **Por qué:** el front consume rutas de tres servicios; mezclar estilos obliga a recordar
  cuál usa cada uno.
- **Señal asociada:** `restriccion/rutas-kebab-case`.
```

Y cuando no hay respaldo, la `P` no se escribe todavía:

```markdown
### P5 · «Todo formulario guarda un borrador automático»

- ⛔ **No se publica.** Ningún criterio de `base/` cubre la persistencia de borradores.
  Primero se crea la regla agnóstica en `base/17-interfaz.md` (`20·M14`); luego esta `P`
  la concreta con «cada 30 s en `localStorage`».
```

## 3 · Lo que arrastra el cambio

| Qué | Por qué |
|---|---|
| [plantillas/reglas-proyecto.md](plantillas/reglas-proyecto.md) | Hoy admite `«regla nueva, no cubierta por la base»` (línea 28) — eso queda prohibido; el campo pasa a **Respaldo**, obligatorio. |
| [validadores/reglas-validables.md](validadores/reglas-validables.md) | `M16` **sí** es validable: un script comprueba que cada `P<N>` tiene `Respaldo:` con un ID que existe en `base/`. |
| [CHANGELOG.md](CHANGELOG.md) + [VERSION](VERSION) | **MAYOR**: 7.0.0 → 8.0.0. Los proyectos con `P` ya escritas tienen que agregarles el respaldo. |

¿Lo escribo así, o ajustamos primero la redacción del respaldo por criterio?

### 2 · Usuario — 2026-08-12 22:24:11
> si pero se le ovide el stándard

**Agente** — 2026-08-12 22:34:19
<!-- agente: 812a56ae-353b-4cf4-be6f-b36395545880 -->

Ahora sí, aplicando el procedimiento completo del capítulo 20. Escribo los archivos.

Ahora la plantilla que usan los proyectos:

Hecho, con los nueve pasos del capítulo 20 esta vez.

| Paso | Qué quedó |
|---|---|
| Buscar (`M12`) | `13·DOC10` exige registrar la regla propia, no de dónde sale; `M13` enruta lo que va en `base/`, no lo que va en capa 3. No había dónde colgarla. |
| Enrutar | Capítulo 20, preámbulo. ID libre: `M16`. |
| Escribir (`M5`, `M15`) | [M16 · Toda regla de proyecto nombra la regla de base que concreta](base/20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md), cuerpo de dos frases, cada cita con su enlace, ejemplo INCORRECTO/CORRECTO. |
| Dependencia (`M7`) | `extiende M1`. Sin ciclo y sin apuntar a una `[BLINDADA]`. |
| Validable (`M9`) | Registrada en [reglas-validables.md](validadores/reglas-validables.md): 🔶 necesita el catálogo del proyecto, comprueba que cada `P` trae **Respaldo** y que el ID existe. |
| Versionar (`M10`) | [CHANGELOG.md](CHANGELOG.md) 8.0.0 MAYOR ⚠ obliga a migrar, [VERSION](VERSION) en 8.0.0. |
| Checklist (`M14`) | Dentro de la regla: **CUMPLE**, 19 ✅ · 0 ❌ · 1 N/A. |

Lo que arrastró: el índice y la sección *M16 — el respaldo es del criterio, no del detalle* en [base/20-meta-reglas/base.md](base/20-meta-reglas/base.md), y la [plantilla del catálogo](plantillas/reglas-proyecto.md), donde *Relación con la base* pasó a **Respaldo** obligatorio con enlace y desapareció la salida *"regla nueva, no cubierta por la base"*.

`citas.py`, `enlaces.py` e índices: 0 hallazgos.

Dos cosas antes de seguir:

1. Esta sesión la guardo como `2026-08-12-regla-de-respaldo-de-las-reglas-de-proyecto.md` (nace `20·M16`: ninguna regla de proyecto existe sin un criterio de la base que la respalde), ¿va? Si sí, péguele también `/rename regla-de-respaldo-de-las-reglas-de-proyecto`.
2. ¿Commiteo esto?

### 3 · Usuario — 2026-08-12 22:35:01
> si para las 2
