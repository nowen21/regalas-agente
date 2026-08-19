# Funcionalidad implementada — Fase «A-EP-005-HU-010-el-capitulo-llega-al-escribir-el-archivo»   ·   `[CAPA 3]`

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-005-HU-010-el-capitulo-llega-al-escribir-el-archivo` |
| **Épica / HU** | [EP-005](../../epica.md) · [HU-010](../HU-010-la-regla-llega-al-escribir-el-archivo.md) |
| **Versión** | sin cambio — no se toca `base/` ni `plantillas/` |
| **Fecha de cierre** | 2026-08-18 |

---

## 1. Qué quedó

**Al escribir o cambiar un documento que un capítulo gobierna, llegan las reglas relacionadas con él**: las que dependen de lo que se está tocando, sus dependencias declaradas y lo que cita.

Nace [`validadores/relacionadas.py`](../../../../../validadores/relacionadas.py) —la consulta— y [`hook_relacionadas.py`](../../../../../validadores/hook_relacionadas.py), que la entrega al escribir. El instalador lo deja puesto.

**Sin base de datos.** La respuesta ya estaba en el repositorio: `citas.py` sabe dónde vive cada regla, `metareglas.py` lee las dependencias declaradas, y `20·M15` obliga a que toda cita lleve su enlace. **Quién cita a quién estaba escrito y era seguible; faltaba preguntarlo.**

---

## 2. Buscar, no cargar

El criterio decía *«llega completo el capítulo»*. Se cambió antes de construir, y no por el peso:

**El volcado obliga a encontrar la relación uno mismo, que es exactamente lo que falla.** La consulta la pone delante.

**Y solo trae a los vecinos del mismo capítulo.** De las cinco reglas que dependen de `02·F2`, **tres viven en otros** — `00·ID3`, `00·ID5` y `13·DOC3`. El capítulo entero no las habría traído, y son las que más fácil se rompen sin notarlo.

De paso: el capítulo `02` pesa **98 KB** contra los ~2 KB de una regla.

---

## 3. Las que dependen van primero

**Cambiar una regla rompe a quien dependía de ella, y ese es el lado que no se mira.** Lo que la regla cita al menos está delante mientras se escribe; lo que la cita a ella, no.

Por eso el aviso abre con *«las que dependen de lo que está tocando»* y nombra la fila 17 del checklist: quien lo recibe tiene que saber para qué le llega.

---

## 4. El límite, y por qué importa

**Una relación que nadie declaró no se encuentra.** `20·M17` se relaciona con `00·ID7` y no sale: esa relación se argumentó en el sello y nunca se declaró en el cuerpo.

**Eso hace que [`20·M7`](../../../../../base/20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md) y [`20·M15`](../../../../../base/20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md) dejen de ser trámite: son lo que hace la consulta posible.** Está fijado en un caso de prueba, para que se vea en vez de descubrirse el día que algo falte.

---

## 5. Lo que no hace

- **No detiene.** Es información para decidir, no una comprobación; lo que se comprueba tiene su validador.
- **No ve el choque entre dos reglas que no se citan.** Eso solo lo ve quien lee.
- **Al reiniciar la máquina el aviso vuelve**, porque la marca de «ya avisé» vive en la carpeta temporal cuando el proyecto no tiene `.agente/` — el caso del propio estándar, que no se instala a sí mismo. Repetirlo una vez cuesta menos que perderlo.
